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
    # For each checkpoint we need to identify all the meaningful choice possibilities, that means
    # all the variables changes that will impact future actions... Each meaningful choice must have an image
        lad_test_checkpoints ={
            'friday_afternoon': "lad_introduction",
            'friday_evening': "lad_day1_evening",
            'saturday_morning': "lad_day2_morning",
            'saturday_afternoon': "lad_day2_hunt",
            'saturday_afternoon_no_hunt': "lad_day2_no_hunt",
            'saturday_evening': "lad_day2_evening",
            'sunday_morning': "lad_day3_morning",
            'sunday_afternoon': "lad_day3_afternoon",
        }