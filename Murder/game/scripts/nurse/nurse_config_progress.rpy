label nurse_config_progress:
    python:  
    # First define the possible progress
        nurse_progress = [
            # First Line
            [
                Chapter(image_checkpoint_start, "start", "nurse_introduction", "friday_afternoon"), 
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "nurse_day3_afternoon", "sunday_afternoon"),
                Chapter(image_ending_question, "ending", "poisoned", "end"),
            ],
            # Second line, ...
            [
                # Chapter(image_checkpoint_empty_small),    
                # Chapter(image_checkpoint_line),
                # Chapter(image_checkpoint_empty),
                # Chapter(image_checkpoint_line),
                # Chapter(image_checkpoint_line),
                # Chapter(image_checkpoint_empty),
                # Chapter(image_checkpoint_double_corner),
                # Chapter(image_ending_question, "ending", "run_over", "end"),
            ],
        ]

        nurse_test_checkpoints = {
            'friday_afternoon': [
                {"label": "nurse_introduction", "threads": {}},
            ],
            'friday_evening': [
                {"label": "nurse_day1_evening", "threads": {}},
            ],

        }