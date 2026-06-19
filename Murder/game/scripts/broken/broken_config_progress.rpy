label broken_config_progress:
    python:
    # First define the possible progress
        broken_progress = [
            # Row 0: Main path (only the first two chapters are written so far)
            [
                Chapter(image_checkpoint_start, "start", "broken_introduction", "friday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_empty),   # saturday_morning  (unwritten)
                Chapter(image_checkpoint_empty),   # saturday_afternoon (unwritten)
                Chapter(image_checkpoint_empty),   # saturday_evening  (unwritten)
                Chapter(image_checkpoint_empty),   # sunday_morning    (unwritten)
                Chapter(image_checkpoint_empty),   # sunday_afternoon  (unwritten)
                Chapter(image_ending_question, "ending", "todo", "end"),
            ],
            # Row 1: empty trunk dropping down from Friday evening to the death branches
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
            ],
            # Row 2: Death branch — drinking the poisoned whisky on Friday night
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "deathbed", "saturday_morning"),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
            ],
            # Row 3: Death branch — questioning the maid, throat cut in his sleep
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "throat_cut", "saturday_morning"),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
            ],
        ]

    # Define Checkpoints for TEST
    # Each chapter maps to a list of checkpoint configurations
    # Each config has: label (Ren'Py label) and threads (dict of thread_id: True/False)
    # Only the written chapters are listed here.
        broken_test_checkpoints = {
            # ===== FRIDAY AFTERNOON =====
            # First chapter - no threads set yet
            'friday_afternoon': [
                {"label": "broken_introduction", "threads": {}},
            ],

            # ===== FRIDAY EVENING =====
            # No threads from previous chapters are relevant yet.
            'friday_evening': [
                {"label": "broken_day1_evening", "threads": {}},
            ],
        }
