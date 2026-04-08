label captain_config_progress:
    python:
    # First define the possible progress
        captain_progress = [
            # Row 0: Main path (first 3 chapters only for now)
            [
                Chapter(image_checkpoint_start, "start", "captain_introduction", "friday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "captain_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
            ],
        ]

        captain_test_checkpoints = {
            'friday_afternoon': [
                {"label": "captain_introduction", "threads": {}},
            ],
            'friday_evening': [
                {"label": "captain_day1_evening", "threads": {}},True}},
            ],
        }
