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
                    Chapter(image_checkpoint_empty),
                    Chapter(image_checkpoint_empty),
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
                    Chapter(image_checkpoint_empty),
                    Chapter(image_checkpoint_empty),
                    Chapter(image_checkpoint_line),
                    # Chapter(image_checkpoint_straight_line),
                    Chapter(image_checkpoint_corner),
                    Chapter(image_ending_question, "ending", "bludgeoned", "sunday_morning"),
                    Chapter(image_checkpoint_empty_after_ending),
                    Chapter(image_checkpoint_corner),
                    Chapter(image_ending_question, "ending", "escape", "end"),
                ],
                # Fourth line, ...
                [
                    Chapter(image_checkpoint_empty_small),  
                    Chapter(image_checkpoint_empty),  
                    Chapter(image_checkpoint_empty),                    
                    Chapter(image_checkpoint_corner),
                    # Chapter(image_checkpoint_straight_line),
                    # Chapter(image_checkpoint_three_sides),
                    Chapter(image_ending_question, "ending", "fell", "sunday_morning"),
                    Chapter(image_checkpoint_empty_after_ending),
                ],
            ]

    # Define Checkpoints for TEST
    # Each chapter maps to a list of checkpoint configurations
    # Each config has: label (Ren'Py label) and threads (dict of thread_id: True/False)
    # Rule: threads must be SET in a previous chapter AND be RELEVANT to the current chapter
        psychic_test_checkpoints = {
            # ===== FRIDAY AFTERNOON =====
            # First chapter - no threads set yet
            'friday_afternoon': [
                {"label": "psychic_introduction", "threads": {}},
            ],

            # ===== FRIDAY EVENING =====
            # No threads from previous chapters are relevant here
            # Threads SET here: visited_attic, lord_name, lord_age
            'friday_evening': [
                {"label": "psychic_day1_evening", "threads": {}},
            ],

            # ===== SATURDAY MORNING =====
            # No threads from previous chapters are relevant here
            # (visited_attic, lord_name, lord_age NOT relevant to saturday_morning)
            'saturday_morning': [
                {"label": "psychic_day2_morning", "threads": {}},
            ],

            # ===== SATURDAY AFTERNOON =====
            # Threads SET before & RELEVANT here:
            #   - visited_attic: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - lord_name: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - lord_age: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            # Note: lord_name and lord_age depend on visited_attic being True
            'saturday_afternoon': [
                {"label": "psychic_day2_no_hunt", "threads": {'visited_attic': False, 'lord_name': False, 'lord_age': False}},
                {"label": "psychic_day2_no_hunt", "threads": {'visited_attic': True, 'lord_name': False, 'lord_age': False}},
                {"label": "psychic_day2_no_hunt", "threads": {'visited_attic': True, 'lord_name': True, 'lord_age': False}},
                {"label": "psychic_day2_no_hunt", "threads": {'visited_attic': True, 'lord_name': True, 'lord_age': True}},
            ],

            # ===== SATURDAY EVENING =====
            # Threads SET before & RELEVANT here:
            #   - visited_attic: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - lord_name: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - lord_age: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - nurse_sick: chapters=['saturday_afternoon', 'saturday_evening'], relevant=['saturday_afternoon', 'saturday_evening', 'sunday_morning']
            'saturday_evening': [
                {"label": "psychic_day2_evening", "threads": {'visited_attic': False, 'lord_name': False, 'lord_age': False, 'nurse_sick': False}},
                {"label": "psychic_day2_evening", "threads": {'visited_attic': True, 'lord_name': False, 'lord_age': False, 'nurse_sick': False}},
                {"label": "psychic_day2_evening", "threads": {'visited_attic': True, 'lord_name': True, 'lord_age': True, 'nurse_sick': False}},
                {"label": "psychic_day2_evening", "threads": {'visited_attic': False, 'lord_name': False, 'lord_age': False, 'nurse_sick': True}},
                {"label": "psychic_day2_evening", "threads": {'visited_attic': True, 'lord_name': True, 'lord_age': True, 'nurse_sick': True}},
            ],

            # ===== SUNDAY MORNING =====
            # Threads SET before & RELEVANT here:
            #   - visited_attic: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - lord_name: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - lord_age: chapters=['friday_evening', 'saturday_afternoon', 'saturday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - nurse_sick: chapters=['saturday_afternoon', 'saturday_evening'], relevant=['saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - visit_lad: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning']
            #   - silverware: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning']
            'sunday_morning': [
                {"label": "psychic_day3_morning", "threads": {'visited_attic': False, 'nurse_sick': False, 'visit_lad': False, 'silverware': False}},
                {"label": "psychic_day3_morning", "threads": {'visited_attic': True, 'lord_name': True, 'lord_age': True, 'nurse_sick': False, 'visit_lad': False, 'silverware': False}},
                {"label": "psychic_day3_morning", "threads": {'visited_attic': False, 'nurse_sick': True, 'visit_lad': False, 'silverware': False}},
                {"label": "psychic_day3_morning", "threads": {'visited_attic': False, 'nurse_sick': False, 'visit_lad': True, 'silverware': False}},
                {"label": "psychic_day3_morning", "threads": {'visited_attic': False, 'nurse_sick': False, 'visit_lad': False, 'silverware': True}},
                {"label": "psychic_day3_morning", "threads": {'visited_attic': True, 'lord_name': True, 'lord_age': True, 'nurse_sick': True, 'visit_lad': True, 'silverware': True}},
            ],

            # ===== SUNDAY AFTERNOON =====
            # Threads SET before & RELEVANT here:
            #   No threads from previous chapters are relevant here
            #   (steal_gun and leave_manor are set DURING this chapter)
            'sunday_afternoon': [
                {"label": "psychic_day3_afternoon", "threads": {}},
            ],
        }