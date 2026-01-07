label lad_config_progress:
    python:  
    # First define the possible progress
        lad_progress = [
            # First Line
            [
                Chapter(image_checkpoint_start, "start", "lad_introduction", "friday_afternoon"), 
                Chapter(image_checkpoint_right, "checkpoint", "lad_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day3_afternoon", "sunday_afternoon"),
                Chapter(image_ending_question, "ending", "poisoned", "end"),
            ],
            # Second line, ...
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_corner),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_no_hunt", "saturday_afternoon_no_hunt"),
                Chapter(image_checkpoint_corner_merge),
                # Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "gunned_down", "end"),
            ],
            # 3
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "deathbed", "saturday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                # Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "fell", "end"),
            ],
            #4
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                # Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "escape", "end"),
            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                # Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "real_ending", "end"),
            ],
        ]

    # Define Checkpoints for TEST
    # Each chapter maps to a list of checkpoint configurations
    # Each config has: label (Ren'Py label) and threads (dict of thread_id: True/False)
        lad_test_checkpoints = {
            'friday_afternoon': [
                {"label": "lad_introduction", "threads": {}},
            ],
            'friday_evening': [
                {"label": "lad_day1_evening", "threads": {}},
            ],
            'saturday_morning': [
                {"label": "lad_day2_morning", "threads": {'whisky': False, 'day1_drunk': False, 'downstairs_1': True}},
                {"label": "lad_day2_morning", "threads": {'whisky': True, 'day1_drunk': True, 'downstairs_1': True}},
                {"label": "lad_day2_morning", "threads": {'whisky': False, 'day1_drunk': True, 'downstairs_1': True}},
                {"label": "lad_day2_morning", "threads": {'whisky': False, 'day1_drunk': False, 'downstairs_1': False}},
                {"label": "lad_day2_morning", "threads": {'whisky': True, 'day1_drunk': True, 'downstairs_1': False}},
                {"label": "lad_day2_morning", "threads": {'whisky': False, 'day1_drunk': True, 'downstairs_1': False}},
            ],
            'saturday_afternoon': [
                {"label": "lad_day2_hunt", "threads": {'hunt': True}},
            ],
            'saturday_afternoon_no_hunt': [
                {"label": "lad_day2_no_hunt", "threads": {'hunt': False}},
            ],
            'saturday_evening': [
                {"label": "lad_day2_evening", "threads": {}},
            ],
            'sunday_morning': [
                {"label": "lad_day3_morning", "threads": {}},
            ],
            'sunday_afternoon': [
                {"label": "lad_day3_afternoon", "threads": {}},
            ],
        }