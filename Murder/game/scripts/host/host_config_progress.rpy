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
                # The Captain goes for the town alone, and she sits down to
                # lunch with Mr Harring and Miss Baxter
                Chapter(image_ending_question, "ending", "poisoned", "end"),
            ],
            # Row 1: the col4 trunk drops one row before its first branch (a
            #   corner right under the checkpoint clashes with its image)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col4 trunk
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),   # col6 first branch
                Chapter(image_ending_question, "ending", "shot_by_butler", "end"),
            ],
            # Rows 2-4: the three Saturday-evening deaths hang on the col4 trunk.
            #   Shot in the tea room when the Captain confronts her, died in her
            #   sleep behind the locked door, or shot by the butler on the forest
            #   road after taking the car.
            # Rows 1-3: the three other Sunday endings hang on the col6 trunk.
            #   She hides in the attic and the butler finds her at the table
            #   (shot_by_butler, the intuition), the whole house leaves in the
            #   car and it is stopped in the wood (car_ambush), or the two of
            #   them go now and she drives (escape).
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),   # col4 first branch
                Chapter(image_ending_question, "ending", "shot_tea_room", "sunday_morning"),
                Chapter(image_checkpoint_empty_half),      # completes col5
                Chapter(image_checkpoint_double_corner),   # col6 second branch
                Chapter(image_ending_question, "ending", "car_ambush", "end"),

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
                Chapter(image_ending_question, "ending", "escape", "end"),

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
                # She noticed the old tourer on an earlier evening, so she is the one to bring it up.
                {"label": "host_day3_morning", "threads": {"trust_captain": True, "saw_car": True}},
                {"label": "host_day3_morning", "threads": {"trust_captain": True, "found_poison": True, "family_history": True, "saw_car": True}},
            ],
            'sunday_afternoon': [
                # No car: the Captain goes alone, and she goes in to the others
                # or hides in the attic.
                {"label": "host_day3_afternoon", "threads": {"trust_captain": True}},
                # No car, and she knows about the missing bottle when she sits
                # down to lunch.
                {"label": "host_day3_afternoon", "threads": {"trust_captain": True, "found_poison": True}},
                # Car and petrol found: in to the others and the road, or the
                # car now (intuition, always on the menu in debug).
                {"label": "host_day3_afternoon", "threads": {"trust_captain": True, "car_checked": True, "petrol_tin": True}},
            ],
        }
