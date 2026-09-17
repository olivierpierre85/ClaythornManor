label drunk_config_progress:
    python:
        drunk_progress = [
            [
                Chapter(image_checkpoint_start, "start", "drunk_introduction", "friday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "drunk_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "drunk_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "drunk_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "drunk_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "drunk_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "drunk_day3_afternoon", "sunday_afternoon"),
                # He lies dead for a day, puts the plates back, and walks out
                # of the house when the car has gone
                Chapter(image_ending_question, "ending", "survived", "end"),
            ],
            # Row 1: the trunks drop one row under col3, col4 and col6 before
            #   the first branch (a corner right under the checkpoint clashes
            #   with its image)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col3 trunk
                Chapter(image_checkpoint_line),            # col4 trunk
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col6 trunk
            ],
            # Rows 2-3: the two Saturday-night deaths hang on the col4 trunk.
            #   He drinks what is left and cuts his own throat, or he tells
            #   the whole house and somebody with a key agrees with him.
            # Row 2 also carries the one other Sunday ending on the col6
            #   trunk: the butler checks the bed the Captain did not.
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col3 trunk
                Chapter(image_checkpoint_double_corner),   # col4 first branch
                Chapter(image_ending_question, "ending", "throat_cut", "sunday_morning"),
                Chapter(image_checkpoint_empty_half),      # completes col5
                Chapter(image_checkpoint_corner),          # col6 last branch
                Chapter(image_ending_question, "ending", "found_out", "end"),
            ],
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col3 trunk
                Chapter(image_checkpoint_corner),          # col4 last branch
                Chapter(image_ending_question, "ending", "silenced", "sunday_morning"),
            ],
            # Rows 4-5: the two hunt deaths hang on the col3 trunk. Drunk in
            #   the woods with a dead man at his feet, or the rifle lowered
            #   and the night finishing what the letter asked for.
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),   # col3 first branch
                Chapter(image_ending_question, "ending", "despair", "saturday_evening"),
            ],
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),          # col3 last branch
                Chapter(image_ending_question, "ending", "spared", "saturday_evening"),
            ],
        ]

        drunk_test_checkpoints = {
            'friday_afternoon': [
                {"label": "drunk_introduction", "threads": {}},
            ],
            'friday_evening': [
                {"label": "drunk_day1_evening", "threads": {}},
            ],
            'saturday_morning': [
                # Drank the night away: no choice in the morning, the flask is whisky.
                {"label": "drunk_day2_morning", "threads": {"day1_drink": True}},
                # Read the letter sober, nothing carried up from the bar.
                {"label": "drunk_day2_morning", "threads": {}},
                # Read the letter sober, and the port is in the room.
                {"label": "drunk_day2_morning", "threads": {"raided_bar": True, "port": True}},
            ],
            'saturday_afternoon': [
                # Whisky in the flask: the woods are a blur and the shot is real.
                {"label": "drunk_day2_hunt", "threads": {"day1_drink": True}},
                # Water in the flask: the rabbit is a choice.
                {"label": "drunk_day2_hunt", "threads": {"watered_flask": True}},
                {"label": "drunk_day2_hunt", "threads": {"watered_flask": True, "raided_bar": True, "port": True}},
            ],
            'saturday_evening': [
                # Locked in, no bottle of his own: the footman brings whisky.
                {"label": "drunk_day2_evening", "threads": {"watered_flask": True, "shot_doctor": True}},
                # Locked in with the port: the fake death is on the table.
                {"label": "drunk_day2_evening", "threads": {"watered_flask": True, "shot_doctor": True, "raided_bar": True, "port": True}},
            ],
            'sunday_morning': [
                # Only reachable with the port and the plan.
                {"label": "drunk_day3_morning", "threads": {"watered_flask": True, "shot_doctor": True, "raided_bar": True, "port": True, "understood": True, "played_dead": True}},
                {"label": "drunk_day3_morning", "threads": {"watered_flask": True, "shot_doctor": True, "raided_bar": True, "port": True, "understood": True, "played_dead": True, "butler_face": True, "phone_call": True}},
            ],
            'sunday_afternoon': [
                {"label": "drunk_day3_afternoon", "threads": {"watered_flask": True, "shot_doctor": True, "raided_bar": True, "port": True, "understood": True, "played_dead": True}},
                {"label": "drunk_day3_afternoon", "threads": {"watered_flask": True, "shot_doctor": True, "raided_bar": True, "port": True, "understood": True, "played_dead": True, "butler_face": True, "phone_call": True}},
            ],
        }
