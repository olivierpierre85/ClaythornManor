label host_config_progress:
    python:  
        host_progress = [
            [
                Chapter(image_checkpoint_start, "start", "host_introduction", "friday_afternoon"), 
                Chapter(image_checkpoint_right, "checkpoint", "host_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "host_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "host_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "host_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "host_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "host_day3_afternoon", "sunday_afternoon"),
                Chapter(image_ending_question, "ending", "todo", "end"),
            ],
        ]

        host_test_checkpoints = {
            'friday_afternoon': [
                {"label": "host_introduction", "threads": {}},
            ],
            'friday_evening': [
                {"label": "host_day1_evening", "threads": {}},
            ],
            'saturday_morning': [
                {"label": "host_day2_morning", "threads": {}},
            ],
            'saturday_afternoon': [
                {"label": "host_day2_hunt", "threads": {}},
                {"label": "host_day2_hunt", "threads": {"found_poison": True}},
            ],
            'saturday_evening': [
                {"label": "host_day2_evening", "threads": {}},
                {"label": "host_day2_evening", "threads": {"terrible_shot": True, "go_downstairs": True}},
                {"label": "host_day2_evening", "threads": {"found_poison": True, "family_history": True, "terrible_shot": True, "go_downstairs": True}},
            ],
        }
