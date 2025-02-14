label psychic_config_progress:
    python: 
        psychic_progress = [
                # First Line
                [
                    Chapter(image_checkpoint_start, "start"), 
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day1_evening", "Evening", "Friday Evening"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_morning", "Morning", "Saturday Morning"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_no_hunt", "The Hunt", "Saturday - The Hunt"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_afternoon", "Afternoon", "Saturday Afternoon"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day2_evening", "Evening", "Saturday Evening"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day3_morning", "Morning", "Sunday Morning"),
                    Chapter(image_checkpoint_right, "checkpoint", "psychic_day3_afternoon", "Afternoon", "Sunday Afternoon"),
                    Chapter(image_ending_question),
                ],
                # Second line, ...
                [
                    Chapter(image_checkpoint_empty_small),    
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_empty),
                    Chapter(image_checkpoint_line),
                    Chapter(image_checkpoint_empty),
                    Chapter(image_checkpoint_double_corner),
                    Chapter(image_ending_question, "ending", "burned"),
                ],
                [
                    Chapter(image_checkpoint_empty_small),    
                    Chapter(image_checkpoint_corner),
                    Chapter(image_checkpoint_three_sides),
                    Chapter(image_checkpoint_three_sides),
                    Chapter(image_checkpoint_straight_line),
                    Chapter(image_checkpoint_three_sides),
                    Chapter(image_ending_question, "ending", "fell"),
                    Chapter(image_checkpoint_empty_filler),
                    Chapter(image_checkpoint_corner),
                    Chapter(image_ending_question, "ending", "shot"),
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
                [],
                []
            ),
            (
                'psychic_day3_morning',
                [],
                []
            ),
            (
                'psychic_day3_afternoon',
                [],
                [
                ]
            ),
            (
                'psychic_day3_endings_fake_chapter',
                [],
                [
                    # {
                    #     'label': 'gunned_down',
                    #     'condition_id': 'psychic_gunned_down'
                    # },
                    # {
                    #     'label': 'poisoned',
                    #     'condition_id': 'psychic_poisoned'
                    # },
                    # {
                    #     'label': 'fell',
                    #     'condition_id': 'psychic_fell'
                    # },
                    # {
                    #     'label': 'escape',
                    #     'condition_id': 'psychic_escape'
                    # },
                ]
            ),
        ]