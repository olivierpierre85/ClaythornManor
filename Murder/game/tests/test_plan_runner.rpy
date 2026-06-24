init python in test:
    import json
    import renpy.exports as renpy

    import os

    def load_json_from_game(path_in_game_dir):
        # renpy.file is an alias for renpy.open_file (works with archives too)
        with renpy.file(path_in_game_dir, encoding="utf-8") as f:
            return json.load(f)

    class PlanError(Exception):
        pass

    class ChapterAutoRunner:
        def __init__(self):
            self.reset()

        def reset(self):
            self.active = False
            self.steps = []
            self.i = 0
            self.unlocked_threads_and_endings = []
            self.target_chapter = None
            self.start_chapter = None
            self.reached_new_chapter = None
            self.plan_file = None
            # When True, choices are decided by a local LLM (Ollama) instead of a
            # recorded plan. See ollama_tester.rpy and run_chapter_ollama().
            self.ollama_mode = False

        def load_plan_file(self, path_in_game_dir):
            raw = renpy.open_file(path_in_game_dir).read().decode("utf-8")
            # data = json.loads(raw)
            data = load_json_from_game(path_in_game_dir)
            self.steps = data.get("choices", data)  # accept {"choices":[...]} or directly a list
            # Combine all for ease of use
            self.unlocked_threads_and_endings = data.get("unlocked_threads_and_endings", [])
            self.unlocked_threads_and_endings.extend(data.get("unlocked_threads", []))
            self.unlocked_threads_and_endings.extend(data.get("unlocked_endings", []))

            # Deduplicate just in case
            self.unlocked_threads_and_endings = list(set(self.unlocked_threads_and_endings))

            self.saved_variables = data.get("saved_variables", {})
            self.plan_file = path_in_game_dir
            self.i = 0
            self.active = True

        def _next_step(self):
            if self.i >= len(self.steps):
                raise PlanError("Plan exhausted but a menu was shown.")
            step = self.steps[self.i]
            self.i += 1
            return step

        def assert_consumed(self):
            if self.active and self.i != len(self.steps):
                remaining = len(self.steps) - self.i
                nxt = self.steps[self.i] if self.i < len(self.steps) else None
                raise PlanError(
                    f"Chapter ended before plan was fully consumed "
                    f"(plan {self.plan_file}). "
                    f"{remaining} step(s) left. Next expected: {nxt}"
                )

        def pick_choice_for_menu(self, timed_menu):
            """
            Called from TimedMenu.display_choices() during tests.
            Picks a TimedMenuChoice from timed_menu.choices using the plan,
            or (in ollama_mode) by asking the local LLM.
            """
            # Only consider choices that are valid (your logic).
            # Map menus mirror in-game behaviour: the map UI lets the player
            # revisit any room and only checks the choice condition, so we
            # ignore the `hidden` flag here too.
            if getattr(timed_menu, "is_map", False):
                valid_choices = [c for c in timed_menu.choices if c.get_condition()]
            else:
                valid_choices = [c for c in timed_menu.choices if c.is_valid()]

            # --- Ollama tester mode: a local LLM reads the story so far and picks ---
            if getattr(self, "ollama_mode", False):
                idx = decide_choice(timed_menu, valid_choices)
                return valid_choices[idx]

            # --- Recorded plan mode (default) ---
            step = self._next_step()

            expected_menu_id = step.get("menu")
            if expected_menu_id != timed_menu.id:
                raise PlanError(
                    f"Menu mismatch: expected '{expected_menu_id}', got '{timed_menu.id}' "
                    f"(plan {self.plan_file}, step {self.i}/{len(self.steps)}, "
                    f"expected redirect '{step.get('redirect')}', "
                    f"time_left {getattr(renpy.store, 'time_left', '?')})."
                )

            expected_redirect = step.get("redirect", None)
            expected_text = step.get("selected", None)

            # Prefer redirect match (most stable), fallback to text match
            if expected_redirect:
                for c in valid_choices:
                    if c.redirect == expected_redirect:
                        return c

            if expected_text:
                for c in valid_choices:
                    if c.text == expected_text:
                        if expected_redirect:
                            renpy.log(
                                f"[TEST WARNING] Redirect mismatch in menu '{timed_menu.id}': "
                                f"expected redirect='{expected_redirect}', "
                                f"actual redirect='{c.redirect}'. "
                                f"Matched by text='{expected_text}' instead. "
                                f"Update the setup JSON to fix this."
                            )
                        return c

            available = [(c.text, c.redirect) for c in valid_choices]
            raise PlanError(
                f"Planned choice not found in menu '{timed_menu.id}'. "
                f"Expected redirect='{expected_redirect}' text='{expected_text}'. "
                f"Available: {available}"
            )

    autorunner = ChapterAutoRunner()

    class PyCallNode(renpy.test.testast.Node):
        def __init__(self, loc, func, *args, **kwargs):
            super().__init__(loc)
            self.func = func
            self.args = args
            self.kwargs = kwargs

        def execute(self, state, t):
            self.func(*self.args, **self.kwargs)
            renpy.test.testast.next_node(self.next)
            return None

    def unlock_threads(details_obj, names):
        for n in (names or []):
            details_obj.threads.unlock(n)
            if hasattr(details_obj, 'endings'):
                details_obj.endings.unlock(n)

    def start(character, chapter, plan_file=None, threads=None):
        """
        Consolidated setup for a chapter test.
        """
        import copy
        renpy.store.current_character = character
        renpy.store.current_chapter = chapter
        renpy.store.disable_all_tutorials()
        
        # Save a clean snapshot if not already saved to restore fully between plans
        if not hasattr(character, '_test_pristine_snapshot'):
            character._test_pristine_snapshot = copy.deepcopy(character.saved_variables)
            # We also snapshot threads, progress, and observations.
            character._test_pristine_threads = copy.deepcopy(character.threads)
            character._test_pristine_progress = copy.deepcopy(character.progress)
            character._test_pristine_observations = copy.deepcopy(character.observations)
        
        autorunner.reset()
        if plan_file:
            autorunner.load_plan_file(plan_file)
        
        autorunner.target_chapter = chapter
        autorunner.active = True
        
        if threads:
            unlock_threads(character, threads)

    def discover_plans(character_id, chapter_id):
        """
        Automatically finds all .json plan files for a given character and chapter.
        Expected path: tests/<character_id>/<index>_<chapter_id>/*.json
        """
        import os
        base_dir = os.path.join(renpy.config.gamedir, "tests", character_id)
        matching_plans = []
        
        if not os.path.exists(base_dir):
            return []

        for d in os.listdir(base_dir):
            # Check if directory name matches the chapter_id (exactly or with index prefix)
            if d == chapter_id or (len(d.split('_', 1)) > 1 and d.split('_', 1)[1] == chapter_id):
                path = os.path.join(base_dir, d)
                if os.path.isdir(path):
                    for f in os.listdir(path):
                        if f.endswith(".json"):
                            # Relative path for loading
                            rel_path = f"tests/{character_id}/{d}/{f}"
                            matching_plans.append(rel_path)
        
        return sorted(matching_plans)

    def run_chapter(character, chapter_id, start_label):
        """
        Discovers and executes all plans for a chapter.
        This should be called from within a testcase.
        """
        plans = discover_plans(character.text_id, chapter_id)
        
        if not plans:
            # Allow chapters with strictly linear reads and no choices
            plans = [None]

        import renpy.test.testast as testast
        from renpy.test.testexecution import node_executor

        loc = ("", 0)
        current_node = PyCallNode(loc, lambda: None)
        first_node = current_node

        for i, plan in enumerate(plans):
            if i > 0:
                # Clear state instead of Start() which causes JumpOutException crash
                def soft_reset():
                    renpy.exports.hide_screen('test_end')
                    import copy
                    if hasattr(character, '_test_pristine_snapshot'):
                        character.saved_variables = copy.deepcopy(character._test_pristine_snapshot)
                        character.threads = copy.deepcopy(character._test_pristine_threads)
                        character.progress = copy.deepcopy(character._test_pristine_progress)
                        character.observations = copy.deepcopy(character._test_pristine_observations)
                        
                    if hasattr(character, 'reset_information'):
                        character.reset_information()

                    renpy.store.all_menus.clear()
                    renpy.store.all_choices.clear()

                    # Fix: Reset menu level and choice state
                    renpy.store.menu_level = -1
                    renpy.store.selected_choice = [None, None, None, None, None]
                    renpy.store.time_diff = [None, None, None, None, None]

                    while renpy.exports.call_stack_depth() > 0:
                        renpy.exports.pop_call()
                
                reset_node = PyCallNode(loc, soft_reset)
                current_node.chain(reset_node)
                current_node = reset_node
            
            # Setup plan & character state
            setup_node = PyCallNode(loc, start, character, chapter_id, plan)
            current_node.chain(setup_node)
            current_node = setup_node
            
            # Apply threads and endings if present in the plan
            def apply_threads():
                if autorunner.unlocked_threads_and_endings:
                    unlock_threads(renpy.store.current_character, autorunner.unlocked_threads_and_endings)

                if hasattr(autorunner, "saved_variables") and autorunner.saved_variables:
                    renpy.store.current_character.saved_variables.update(autorunner.saved_variables)
            
            threads_node = PyCallNode(loc, apply_threads)
            current_node.chain(threads_node)
            current_node = threads_node

            # Use test execution to jump and wait
            jump_node = testast.Action(loc, f"Jump('{start_label}')")
            current_node.chain(jump_node)
            current_node = jump_node
            
            screen_selector = testast.DisplayableSelector(loc, screen="'test_end'")
            until_node = testast.Until(loc, testast.Advance(loc), screen_selector, timeout="180.0")
            current_node.chain(until_node)
            current_node = until_node
            
            # TODO (testing management): chain a PyCallNode(loc, autorunner.assert_consumed)
            # here to fail loudly when a chapter ends with unused plan steps.
            # Currently disabled: several old recordings (nurse friday_evening_1,
            # saturday_morning_1, saturday_evening_1, sunday_*_1) leave steps
            # unconsumed and need re-recording first, and a failed testcase leaks
            # its test_end screen into the next one, cascading false failures.

            # Cleanup for next iteration
            cleanup_node = PyCallNode(loc, autorunner.reset)
            current_node.chain(cleanup_node)
            current_node = cleanup_node
            
        if first_node.next:
            # The currently executing node is node_executor.node (a testast.Python node)
            # Its 'next' attribute will be used when it finishes.
            # We chain our generated sequence so it continues to the original next node.
            current_node.chain(node_executor.node.next)

            # We then overwrite its 'next' property to be our dynamic chain.
            node_executor.node.next = first_node.next

    def run_chapter_ollama(character, chapter_id, start_label, runs=3, threads=None):
        """
        Plays a chapter `runs` times, letting the local LLM (Ollama) pick every
        choice instead of a recorded JSON plan. Mirrors run_chapter()'s node
        chaining (jump -> wait for test_end -> soft reset) but with no plan file
        and autorunner.ollama_mode = True. Each run writes its own transcript
        (via the existing change_time export hook) plus an Ollama decision log.

        threads: optional list of thread/ending names to pre-unlock so a later
        chapter exposes the branches that depend on earlier-day discoveries.
        """
        import renpy.test.testast as testast
        from renpy.test.testexecution import node_executor

        loc = ("", 0)
        current_node = PyCallNode(loc, lambda: None)
        first_node = current_node

        def soft_reset():
            renpy.exports.hide_screen('test_end')
            import copy
            if hasattr(character, '_test_pristine_snapshot'):
                character.saved_variables = copy.deepcopy(character._test_pristine_snapshot)
                character.threads = copy.deepcopy(character._test_pristine_threads)
                character.progress = copy.deepcopy(character._test_pristine_progress)
                character.observations = copy.deepcopy(character._test_pristine_observations)

            if hasattr(character, 'reset_information'):
                character.reset_information()

            renpy.store.all_menus.clear()
            renpy.store.all_choices.clear()

            renpy.store.menu_level = -1
            renpy.store.selected_choice = [None, None, None, None, None]
            renpy.store.time_diff = [None, None, None, None, None]

            while renpy.exports.call_stack_depth() > 0:
                renpy.exports.pop_call()

        def setup_ollama():
            # plan_file=None: no recorded steps, decisions come from Ollama.
            start(character, chapter_id, None, threads)
            autorunner.ollama_mode = True
            reset_decision_log()

        for i in range(runs):
            if i > 0:
                reset_node = PyCallNode(loc, soft_reset)
                current_node.chain(reset_node)
                current_node = reset_node

            setup_node = PyCallNode(loc, setup_ollama)
            current_node.chain(setup_node)
            current_node = setup_node

            jump_node = testast.Action(loc, f"Jump('{start_label}')")
            current_node.chain(jump_node)
            current_node = jump_node

            screen_selector = testast.DisplayableSelector(loc, screen="'test_end'")
            until_node = testast.Until(loc, testast.Advance(loc), screen_selector, timeout="180.0")
            current_node.chain(until_node)
            current_node = until_node

            # Save the LLM's reasoning for this run next to the transcript.
            dump_node = PyCallNode(loc, dump_decision_log)
            current_node.chain(dump_node)
            current_node = dump_node

            cleanup_node = PyCallNode(loc, autorunner.reset)
            current_node.chain(cleanup_node)
            current_node = cleanup_node

        if first_node.next:
            current_node.chain(node_executor.node.next)
            node_executor.node.next = first_node.next
