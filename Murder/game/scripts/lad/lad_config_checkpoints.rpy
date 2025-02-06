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
                Chapter(image_ending_question),
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
                Chapter(image_ending_question, "ending", "gunned_down", "Gunned Down", "You were kill by Gun Shot"),
            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "poisoned"),
                Chapter(image_checkpoint_empty_filler),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "poisoned"),
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
                Chapter(image_ending_question, "ending", "fell"),
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
                'lad_day2_morning',  # The normal label
                [
                    ('important_choice', 'whisky'),
                    ('important_choice', 'day1_drunk'),
                    ('important_choice', 'downstairs_1')
                ],
                [
                    # This ending triggers if the player took whisky but isn't drunk => "killed_by_whisky"
                    {
                        'label': 'poisoned',
                        'condition_id': 'poisoned'
                    },
                    # # Another example of an early ending
                    # {
                    #     'label': 'flooded_basement',
                    #     'condition': lambda t: t['downstairs_1'] and t['whisky']
                    # }
                    # # You can keep adding more endings for this label...
                ]
            ),
            # Add more chapters with toggles & possible endings as needed...
        ]

    return