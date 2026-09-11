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
                # She stays for lunch, wakes with the house dead around her,
                # and the butler comes back for the silver
                Chapter(image_ending_question, "ending", "shot_by_butler", "end"),
            ],
            # Row 1: the trunks drop one row under col4 and col6 before the
            #   first branch (a corner right under the checkpoint clashes with
            #   its image)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col4 trunk
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col6 trunk
            ],
            # Rows 2-4: the three Saturday-evening deaths hang on the col4 trunk.
            #   Shot in the tea room when the Captain confronts her, died in her
            #   sleep behind the locked door, or shot by the butler on the forest
            #   road after taking the car.
            # Rows 2-3: the two other Sunday endings hang on the col6 trunk.
            #   She drives out with the Captain (escape), or they set out on
            #   foot and the butler's car meets them (run_over).
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),   # col4 first branch
                Chapter(image_ending_question, "ending", "shot_tea_room", "sunday_morning"),
                Chapter(image_checkpoint_empty_half),      # completes col5
                Chapter(image_checkpoint_double_corner),   # col6 first branch
                Chapter(image_ending_question, "ending", "escape", "end"),
            ],
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),   # col4 second branch
                Chapter(image_ending_question, "ending", "die_in_sleep", "sunday_morning"),
                Chapter(image_checkpoint_empty_half),      # completes col5
                Chapter(image_checkpoint_corner),          # col6 last branch
                Chapter(image_ending_question, "ending", "run_over", "end"),
            ],
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),          # col4 last branch
                Chapter(image_ending_question, "ending", "shot_in_car", "sunday_morning"),
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
                # No mistake at all, so the Captain never confronts her and he is
                # still sitting up in the billiard room at night.
                {"label": "host_day2_evening", "threads": {"found_poison": True, "family_history": True, "go_downstairs": True, "stayed_with_guests": True, "addressed_manning_first": True}},
            ],
            'sunday_morning': [
                # Sunday is only reachable once she has confided in Captain Sinha.
                {"label": "host_day3_morning", "threads": {"trust_captain": True}},
                {"label": "host_day3_morning", "threads": {"trust_captain": True, "found_poison": True, "family_history": True}},
            ],
            'sunday_afternoon': [
                # Nothing found in the morning: on foot, or stay for lunch.
                {"label": "host_day3_afternoon", "threads": {"trust_captain": True}},
                # Car and petrol but no food: the Captain will not take the car.
                {"label": "host_day3_afternoon", "threads": {"trust_captain": True, "seen_car": True, "petrol_tin": True}},
                # Everything found: the car is on the menu.
                {"label": "host_day3_afternoon", "threads": {"trust_captain": True, "seen_car": True, "petrol_tin": True, "provisions": True}},
                {"label": "host_day3_afternoon", "threads": {"trust_captain": True, "found_poison": True, "seen_car": True, "petrol_tin": True, "provisions": True}},
            ],
        }
