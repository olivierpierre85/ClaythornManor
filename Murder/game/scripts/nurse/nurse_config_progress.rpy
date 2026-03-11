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
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "todo", "end"),
            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "exhausted", "sunday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "todo", "end"),
            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "escape_poor", "sunday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "todo", "end"),
            ],
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
                {"label": "nurse_day2_morning", "threads": {'day1_exhaustion': True}},
            ],
            'saturday_afternoon': [
                {"label": "nurse_day2_hunt", "threads": {}},
                {"label": "nurse_day2_hunt", "threads": {'day1_exhaustion': True}},
            ],
            'saturday_evening': [
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': False}},
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': True}},
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': True, 'steal_cutlery_1': True,  'steal_cutlery_2': True}},
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': False, 'steal_cutlery_1': True,  'steal_cutlery_2': True}},
                {"label": "nurse_day2_evening", "threads": {'captain_lie_rank': True, 'footman_belgian': True,  'maid_actress': True}},
                
            ],
        }