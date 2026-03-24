label nurse_config_progress:
    python:  
    # First define the possible progress
        nurse_progress = [
            # Row 0: Main path -> poisoned
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
            # Row 1: gunned_down branches from sun_aft
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "gunned_down", "end"),
            ],
            # Row 2: psychic_fight_death branches from sun_aft
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "billiard_room_death", "sunday_morning"),
                Chapter(image_checkpoint_double_corner_half),
                Chapter(image_ending_question, "ending", "escape_rich", "sunday_afternoon"),
                Chapter(image_checkpoint_corner_half),
                Chapter(image_ending_question, "ending", "psychic_fight_death", "end"),
            ],
            # Row 3: exhausted - horizontal from sat_eve through to end
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "exhausted", "end"),
                Chapter(image_checkpoint_double_corner_half),
                Chapter(image_ending_question, "ending", "escape_collapse", "sunday_afternoon"),

            ],
            # Row 4: escape_collapse branches from sun_morn
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),
                Chapter(image_checkpoint_three_sides),
                Chapter(image_ending_question, "ending", "escape_poor", "sunday_afternoon"),
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
                {"label": "nurse_day2_morning", "threads": {'day1_exhaustion': True, 'remember_doctor': True}},
            ],
            'saturday_afternoon': [
                {"label": "nurse_day2_hunt", "threads": {}},
                {"label": "nurse_day2_hunt", "threads": {'day1_exhaustion': True}},
                {"label": "nurse_day2_hunt", "threads": {'day1_exhaustion': True, 'remember_doctor': True, 'steal_cutlery_1': True, 'steal_cutlery_2': True, 'take_gun': True}},
                {"label": "nurse_day2_hunt", "threads": {'day1_exhaustion': True, 'remember_doctor': True, 'steal_cutlery_1': True}},
            ],
            'saturday_evening': [
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': False}},
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': True}},
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': True, 'steal_cutlery_1': True,  'steal_cutlery_2': True}},
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': False, 'steal_cutlery_1': True,  'steal_cutlery_2': True}},
                {"label": "nurse_day2_evening", "threads": {'captain_lie_zanzibar': True, 'captain_lie_boxer': True, 'footman_belgian': True, 'maid_actress': True}},
                {"label": "nurse_day2_evening", "threads": {'day1_exhaustion': True, 'remember_doctor': True, 'captain_lie_zanzibar': True, 'captain_lie_boxer': True, 'spotted_by_psychic': True, 'footman_belgian': True, 'maid_actress': True, 'steal_cutlery_1': True, 'steal_cutlery_2': True, 'take_gun': True, 'find_bullets': True}},
            ],
            'sunday_morning': [
                {"label": "nurse_day3_morning", "threads": {'day1_exhaustion': False}},
                {"label": "nurse_day3_morning", "threads": {'day1_exhaustion': True}},
                {"label": "nurse_day3_morning", "threads": {'day2_exhaustion': True}},
                {"label": "nurse_day3_morning", "threads": {'day1_exhaustion': True, 'day2_exhaustion': True}},
                {"label": "nurse_day3_morning", "threads": {'silverware_big': True, 'master_key': True}},
                {"label": "nurse_day3_morning", "threads": {'master_key': True}},
            ],
            'sunday_afternoon': [
                {"label": "nurse_day3_afternoon", "threads": {}},
                {"label": "nurse_day3_afternoon", "threads": {'find_bullets': True, 'take_gun': True}},
                {"label": "nurse_day3_afternoon", "threads": {'steal_cutlery_1': True, 'steal_cutlery_2': True, 'steal_pearls': True, 'take_gun': True, 'find_bullets': True}},
            ],
        }