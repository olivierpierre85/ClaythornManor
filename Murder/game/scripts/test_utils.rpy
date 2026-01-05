init python:
    def disable_all_tutorials():
        """
        Sets all known tutorial flags to True to prevent them from interrupting tests.
        """
        store.seen_tutorial_clock = True
        store.seen_tutorial_description_hidden = True
        store.seen_tutorial_map = True
        store.seen_tutorial_unlock_character = True
        store.seen_tutorial_progress = True
        store.seen_tutorial_progress_details = True
        store.seen_tutorial_restart = True
        store.seen_tutorial_intuition = True
        store.seen_tutorial_icon = True
        store.seen_tutorial_already_chosen = True
        store.seen_tutorial_already_chosen_map = True

    def test_teardown(full_transcript=False):
        """
        Standard teardown for tests: exports transcript and resets autorunner.
        """
        # We need to make sure we are accessing the functions from the store
        if not hasattr(store, "export_transcript"):
            renpy.notify("Error: export_transcript not found")
            return

        export_transcript(full_transcript)
        
        # Reset autorunner if it exists
        if hasattr(store, "test") and hasattr(store.test, "autorunner"):
            store.test.autorunner.reset()
        else:
            # Fallback for when store.test might not be fully initialized or if accessed differently
            # But usually store.test.autorunner is correct in this context
            pass
