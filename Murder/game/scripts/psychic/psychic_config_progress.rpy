label psychic_config_progress:
    python: 
        psychic_progress = [
                # First Line
                [
                    Chapter(image_checkpoint_start, "start", "psychic_introduction", "friday_afternoon"),  
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day1_evening", "friday_evening"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_morning", "saturday_morning"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_no_hunt", "saturday_afternoon"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_evening",  "saturday_evening"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day3_morning", "sunday_morning"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day3_afternoon", "sunday_afternoon"),
                    Chapter(image_ending_question, "ending", "burned", "end"),
                ],
                # Second line, ...
                [
                    Chapter(image_checkpoint_empty_small),    
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_line),
                    # Chapter(image_checkpoint_empty),
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_empty),
                    Chapter(image_checkpoint_double_corner),
                    Chapter(image_ending_question, "ending", "shot", "end"),
                ],
                # THird line, ...
                [
                    Chapter(image_checkpoint_empty_small),    
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_line),
                    # Chapter(image_checkpoint_straight_line),
                    Chapter(image_checkpoint_double_corner),
                    Chapter(image_ending_question, "ending", "bludgeoned", "sunday_morning"),
                    Chapter(image_checkpoint_empty_after_ending),
                    Chapter(image_checkpoint_corner),
                    Chapter(image_ending_question, "ending", "escape", "end"),
                ],
                # Fourth line, ...
                [
                    Chapter(image_checkpoint_empty_small),    
                    Chapter(image_checkpoint_corner),
                    Chapter(image_checkpoint_three_sides),
                    Chapter(image_checkpoint_three_sides),
                    # Chapter(image_checkpoint_straight_line),
                    Chapter(image_checkpoint_three_sides),
                    Chapter(image_ending_question, "ending", "fell", "sunday_morning"),
                ],
            ]

        psychic_test_checkpoints ={
            'friday_afternoon': "psychic_introduction",
            'friday_evening': "psychic_day1_evening",
            'saturday_morning': "psychic_day2_morning",
            'saturday_afternoon': "psychic_day2_no_hunt",
            'saturday_evening': "psychic_day2_evening",
            'sunday_morning': "psychic_day3_morning",
            'sunday_afternoon': "psychic_day3_afternoon",
        }