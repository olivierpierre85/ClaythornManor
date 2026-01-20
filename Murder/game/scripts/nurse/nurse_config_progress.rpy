label nurse_config_progress:
    python:
        nurse_progress = [
            # Day 1
            [
                Chapter(image_checkpoint_start, "start", "nurse_introduction", "friday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day1_evening", "friday_evening"),
            ],
            # Day 2
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day2_no_hunt", "saturday_afternoon_no_hunt"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day2_evening", "saturday_evening"),
            ],
            # Day 3
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day3_afternoon", "sunday_afternoon"),
                Chapter(image_ending_question, "ending", "escaped", "end"),
            ]
        ]

        nurse_test_checkpoints = {
            'friday_afternoon': [
                {"label": "nurse_introduction", "threads": {}},
            ],
            'friday_evening': [
                {"label": "nurse_day1_evening", "threads": {}},
            ],
            'saturday_morning': [
                {"label": "nurse_day2_morning", "threads": {}},
            ],
            'saturday_afternoon_no_hunt': [
                {"label": "nurse_day2_no_hunt", "threads": {}},
            ],
            'saturday_evening': [
                {"label": "nurse_day2_evening", "threads": {}},
            ],
            'sunday_morning': [
                {"label": "nurse_day3_morning", "threads": {}},
            ],
            'sunday_afternoon': [
                {"label": "nurse_day3_afternoon", "threads": {}},
            ],
        }
    return
