init python in test:
    import json
    import renpy.exports as renpy

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
            self.start_chapter = None
            self.reached_new_chapter = None

        def load_plan_file(self, path_in_game_dir):
            raw = renpy.open_file(path_in_game_dir).read().decode("utf-8")
            # data = json.loads(raw)
            data = load_json_from_game(path_in_game_dir)
            self.steps = data.get("choices", data)  # accept {"choices":[...]} or directly a list
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

    def unlock_threads(details_obj, names):
        for n in (names or []):
            details_obj.threads.unlock(n)
