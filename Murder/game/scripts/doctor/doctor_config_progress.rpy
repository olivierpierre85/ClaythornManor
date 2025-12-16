label doctor_config_progress:
    python:  
    # First define the possible progress
        doctor_progress = [
            # First Line
            [
                Chapter(image_checkpoint_start, "start", "doctor_introduction", "friday_afternoon"), 
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day3_afternoon", "sunday_afternoon"),
                Chapter(image_ending_question, "ending", "", "end"),
            ],
            # Second line, ...
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "", "end"),
            ],
            # 3
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "overdose", "saturday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "throat_cut", "sunday_morning"),

            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "burned", "saturday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "shot_by_drunk", "saturday_evening"),
            ],
        ]

    # Define Checkpoints for TEST
    # For each checkpoint we need to identify all the meaningful choice possibilities, that means
    # all the variables changes that will impact future actions... Each meaningful choice must have an image
        doctor_test_checkpoints ={
            'friday_afternoon': "doctor_introduction",
            'friday_evening': "doctor_day1_evening",
            'saturday_morning': "doctor_day2_morning",
            'saturday_afternoon': "doctor_day2_hunt",
            'saturday_evening': "doctor_day2_evening",
            'sunday_morning': "doctor_day3_morning",
            # 'sunday_afternoon': "doctor_day3_afternoon",
        }