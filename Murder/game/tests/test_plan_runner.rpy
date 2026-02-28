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
            self.unlocked_threads = []
            self.target_chapter = None
            self.start_chapter = None
            self.reached_new_chapter = None

        def load_plan_file(self, path_in_game_dir):
            raw = renpy.open_file(path_in_game_dir).read().decode("utf-8")
            # data = json.loads(raw)
            data = load_json_from_game(path_in_game_dir)
            self.steps = data.get("choices", data)  # accept {"choices":[...]} or directly a list
            self.unlocked_threads = data.get("unlocked_threads", [])
            self.i = 0
            self.active = True

        def _next_step(self):
            if self.i >= len(self.steps):
                raise PlanError("Plan exhausted but a menu was shown.")
            step = self.steps[self.i]
            self.i += 1
            return step

        def assert_consumed(self):
            if self.i != len(self.steps):
                remaining = len(self.steps) - self.i
                nxt = self.steps[self.i] if self.i < len(self.steps) else None
                raise PlanError(
                    f"Chapter ended before plan was fully consumed. "
                    f"{remaining} step(s) left. Next expected: {nxt}"
                )

        def pick_choice_for_menu(self, timed_menu):
            """
            Called from TimedMenu.display_choices() during tests.
            Picks a TimedMenuChoice from timed_menu.choices using the plan.
            """
            step = self._next_step()

            expected_menu_id = step.get("menu")
            if expected_menu_id != timed_menu.id:
                raise PlanError(f"Menu mismatch: expected '{expected_menu_id}', got '{timed_menu.id}'.")

            expected_redirect = step.get("redirect", None)
            expected_text = step.get("selected", None)

            # Only consider choices that are valid (your logic)
            valid_choices = [c for c in timed_menu.choices if c.is_valid()]

            # Prefer redirect match (most stable), fallback to text match
            if expected_redirect:
                for c in valid_choices:
                    if c.redirect == expected_redirect:
                        return c

            if expected_text:
                for c in valid_choices:
                    if c.text == expected_text:
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

                    while renpy.exports.call_stack_depth() > 0:
                        renpy.exports.pop_call()
                
                reset_node = PyCallNode(loc, soft_reset)
                current_node.chain(reset_node)
                current_node = reset_node
            
            # Setup plan & character state
            setup_node = PyCallNode(loc, start, character, chapter_id, plan)
            current_node.chain(setup_node)
            current_node = setup_node
            
            # Apply threads if present in the plan
            def apply_threads():
                if autorunner.unlocked_threads:
                    unlock_threads(renpy.store.current_character, autorunner.unlocked_threads)
            
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
