label psychic_config_progress:
    python: 
        psychic_progress = [
                # First Line
                [
                    Chapter(image_checkpoint_start, "start"), 
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day1_evening", "Evening", "Friday Evening"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_morning", "Morning", "Saturday Morning"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_no_hunt", "The Hunt", "Saturday - The Hunt"),
                    # Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_afternoon", "Afternoon", "Saturday Afternoon"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_evening", "Evening", "Saturday Evening"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day3_morning", "Morning", "Sunday Morning"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day3_afternoon", "Afternoon", "Sunday Afternoon"),
                    Chapter(image_ending_question, "ending", "burned"),
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
                    Chapter(image_ending_question, "ending", "shot"),
                ],
                [
                    Chapter(image_checkpoint_empty_small),    
                    Chapter(image_checkpoint_corner),
                    Chapter(image_checkpoint_three_sides),
                    Chapter(image_checkpoint_three_sides),
                    # Chapter(image_checkpoint_straight_line),
                    Chapter(image_checkpoint_three_sides),
                    Chapter(image_ending_question, "ending", "fell"),
                    Chapter(image_checkpoint_empty_after_ending),
                    Chapter(image_checkpoint_corner),
                    Chapter(image_ending_question, "ending", "escape")
                ],
            ]

        psychic_test_checkpoints = [
            (
                'psychic_day1_evening',
                [],
                []
            ),
            (
                'psychic_day2_morning',
                [
                    # ('important_choice', 'whisky'),
                    # ('important_choice', 'day1_drunk'),
                    # ('important_choice', 'downstairs_1')
                ],
                [

                ]
            ),
            (
                'psychic_day2_no_hunt',
                [],
                []
            ),
            (
                'psychic_day2_afternoon',
                [],
                []
            ),
            (
                'psychic_day2_evening',
                [
                    ('important_choice', 'visit_lad')
                ],
                []
            ),
            (
                'psychic_day3_morning',
                [
                    ('important_choice', 'visit_lad')
                ],
                []
            ),
            (
                'psychic_day3_afternoon',
                [
                    ('observation', 'visited_attic'),
                    ('observation', 'lord_name'),
                    ('observation', 'lord_age'),
                ],
                [
                    {
                        'label': 'fell',
                        'condition_id': 'psychic_fell'
                    },
                ]
            ),
            (
                'psychic_day3_endings_fake_chapter',
                [
                    ('important_choice', 'steal_gun'),
                    ('important_choice', 'leave_manor'),
                    
                ],
                [
                    {
                        'label': 'shot',
                        'condition_id': 'psychic_shot'
                    },
                    {
                        'label': 'burned',
                        'condition_id': 'psychic_burned'
                    },
                    {
                        'label': 'escape',
                        'condition_id': 'psychic_escape'
                    },
                ]
            ),
        ]