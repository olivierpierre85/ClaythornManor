label lad_config_progress:
    python:  
    # First define the possible progress
        lad_progress = [
            # First Line
            [
                Chapter(image_checkpoint_start, "start"), 
                Chapter(image_checkpoint_right, "checkpoint", "lad_day1_evening", "Evening", "Friday Evening"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_morning", "Morning", "Saturday Morning"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_hunt", "The Hunt", "Saturday - The Hunt"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_afternoon", "Afternoon", "Saturday Afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_evening", "Evening", "Saturday Evening"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day3_morning", "Morning", "Sunday Morning"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day3_afternoon", "Afternoon", "Sunday Afternoon"),
                Chapter(image_ending_question, "ending", "poisoned"),
            ],
            # Second line, ...
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_corner),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_no_hunt", "No Hunt", "Saturday - No Hunt"),
                Chapter(image_checkpoint_corner_merge),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "gunned_down"),
            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "deathbed"),
                Chapter(image_checkpoint_empty_filler),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "fell"),
            ],
                        [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "escape"),
            ],
        ]

    # Define Checkpoints for TEST
    # For each checkpoint we need to identify all the meaningful choice possibilities, that means
    # all the variables changes that will impact future actions... Each meaningful choice must have an image

        lad_test_checkpoints = [
            (
                'lad_day1_evening',
                [],
                []
            ),
            (
                'lad_day2_morning',
                [
                    ('important_choice', 'whisky'),
                    ('important_choice', 'day1_drunk'),
                    ('important_choice', 'downstairs_1')
                ],
                [
                    {
                        'label': 'deathbed',
                        'condition_id': 'lad_deathbed'
                    },
                ]
            ),
            (
                'lad_day2_hunt',
                [                 
                ],
                []
            ),
            (
                'lad_day2_no_hunt',
                [              
                ],
                []
            ),
            (
                'lad_day2_afternoon',
                [   
                    ('important_choice', 'hunt'),               
                    ('important_choice', 'hunt_captain_host'),
                    # ('important_choice', 'hunt_doctor_drunk'), # hide one because they are exclusive
                ],
                []
            ),
            (
                'lad_day2_evening',
                [
                    ('object', 'burned_letter'),               
                ],
                []
            ),
            (
                'lad_day3_morning',
                [   
                    ('important_choice', 'trust_psychic'),         
                    ('important_choice', 'day2_drunk'),  
                    ('important_choice', 'downstairs_2'),  
                ],
                []
            ),
            (
                'lad_day3_afternoon',
                [   
                    ('object', 'gun'),         
                    ('observation', 'seen_car'),      
                ],
                [
                ]
            ),
            (
                'lad_day3_endings_fake_chapter',
                [   
                    ('object', 'gun'),         
                    ('important_choice', 'abandoned_psychic'),      
                    ('important_choice', 'protect_food'),   
                ],
                [
                    {
                        'label': 'gunned_down',
                        'condition_id': 'lad_gunned_down'
                    },
                    {
                        'label': 'poisoned',
                        'condition_id': 'lad_poisoned'
                    },
                    {
                        'label': 'fell',
                        'condition_id': 'lad_fell'
                    },
                    {
                        'label': 'escape',
                        'condition_id': 'lad_escape'
                    },
                ]
            ),
        ]

    return