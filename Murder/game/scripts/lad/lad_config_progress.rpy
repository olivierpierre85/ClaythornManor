label lad_config_progress:
    python:  
    # First define the possible progress
        lad_progress = [
            # First Line
            [
                Chapter(image_checkpoint_start, "start", "lad_introduction", "friday_afternoon"), 
                Chapter(image_checkpoint_right, "checkpoint", "lad_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day3_afternoon", "sunday_afternoon"),
                Chapter(image_ending_question, "ending", "poisoned", "end"),
            ],
            # Second line, ...
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_corner),
                Chapter(image_checkpoint_right, "checkpoint", "lad_day2_no_hunt", "saturday_afternoon_no_hunt"),
                Chapter(image_checkpoint_corner_merge),
                # Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "gunned_down", "end"),
            ],
            # 3
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "deathbed", "saturday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                # Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "fell", "end"),
            ],
            #4
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                # Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "escape", "end"),
            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                # Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "real_ending", "end"),
            ],
        ]

    # Define Checkpoints for TEST
    # Each chapter maps to a list of checkpoint configurations
    # Each config has: label (Ren'Py label) and threads (dict of thread_id: True/False)
    # Rule: threads must be SET in a previous chapter AND be RELEVANT to the current chapter
        lad_test_checkpoints = {
            # ===== FRIDAY AFTERNOON =====
            # First chapter - no threads set yet
            'friday_afternoon': [
                {"label": "lad_introduction", "threads": {}},
            ],

            # ===== FRIDAY EVENING =====
            # No threads from previous chapters are relevant here
            # Threads SET here: whisky, day1_drunk, downstairs_1
            'friday_evening': [
                {"label": "lad_day1_evening", "threads": {}},
            ],

            # ===== SATURDAY MORNING =====
            # Threads SET before (friday_evening) & RELEVANT here:
            #   - whisky: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning']
            #   - day1_drunk: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening']
            # Note: downstairs_1 was set in friday_evening but NOT relevant to saturday_morning
            'saturday_morning': [
                {"label": "lad_day2_morning", "threads": {'whisky': False, 'day1_drunk': False}},
                {"label": "lad_day2_morning", "threads": {'whisky': True, 'day1_drunk': False}},
                {"label": "lad_day2_morning", "threads": {'whisky': False, 'day1_drunk': True}},
                {"label": "lad_day2_morning", "threads": {'whisky': True, 'day1_drunk': True}},
            ],

            # ===== SATURDAY AFTERNOON (HUNT) =====
            # Threads SET before & RELEVANT here:
            #   - hunt: chapters=['saturday_afternoon', 'saturday_afternoon_no_hunt'], relevant=['saturday_afternoon', ...]
            #     hunt is decided at end of saturday_morning, so it's set "before" entering this chapter
            # hunt_captain_host and hunt_doctor_drunk are set DURING this chapter
            'saturday_afternoon': [
                {"label": "lad_day2_hunt", "threads": {'hunt': True}},
            ],

            # ===== SATURDAY AFTERNOON (NO HUNT) =====
            # Threads SET before & RELEVANT here:
            #   - hunt: must be False to enter this path
            #   - downstairs_1: chapters=['friday_evening', ...], relevant=['friday_evening', 'saturday_afternoon_no_hunt', 'saturday_evening']
            'saturday_afternoon_no_hunt': [
                {"label": "lad_day2_no_hunt", "threads": {'hunt': False, 'downstairs_1': False}},
                {"label": "lad_day2_no_hunt", "threads": {'hunt': False, 'downstairs_1': True}},
            ],

            # ===== SATURDAY EVENING =====
            # Threads SET before & RELEVANT here:
            #   - day1_drunk: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening']
            #   - hunt: chapters=['saturday_afternoon', 'saturday_afternoon_no_hunt'], relevant=['saturday_afternoon', 'saturday_afternoon_no_hunt', 'saturday_evening']
            #   - hunt_captain_host: chapters=['saturday_afternoon'], relevant=['saturday_afternoon', 'saturday_evening']
            #   - downstairs_1: chapters=['friday_evening', ...], relevant=['friday_evening', 'saturday_afternoon_no_hunt', 'saturday_evening']
            #   - downstairs_2: chapters=['saturday_afternoon_no_hunt', 'saturday_evening'], relevant=['saturday_afternoon_no_hunt', 'saturday_evening']
            #   - green_liquid: chapters=['saturday_afternoon_no_hunt', 'saturday_evening'], relevant=['saturday_afternoon_no_hunt', 'saturday_evening']
            #   - burned_letter: chapters=['saturday_afternoon_no_hunt'], relevant=['saturday_afternoon_no_hunt', 'saturday_evening']
            # Note: hunt_doctor_drunk is NOT relevant to saturday_evening
            'saturday_evening': [
                # Hunt path variations
                {"label": "lad_day2_evening", "threads": {'hunt': True, 'hunt_captain_host': True, 'day1_drunk': False}},
                {"label": "lad_day2_evening", "threads": {'hunt': True, 'hunt_captain_host': True, 'day1_drunk': True}},
                {"label": "lad_day2_evening", "threads": {'hunt': True, 'hunt_captain_host': False, 'day1_drunk': False}},
                {"label": "lad_day2_evening", "threads": {'hunt': True, 'hunt_captain_host': False, 'day1_drunk': True}},
                # No-hunt path variations (includes downstairs, green_liquid, burned_letter)
                {"label": "lad_day2_evening", "threads": {'hunt': False, 'downstairs_1': False, 'downstairs_2': False, 'green_liquid': False, 'burned_letter': False, 'day1_drunk': False}},
                {"label": "lad_day2_evening", "threads": {'hunt': False, 'downstairs_1': True, 'downstairs_2': False, 'green_liquid': False, 'burned_letter': False, 'day1_drunk': False}},
                {"label": "lad_day2_evening", "threads": {'hunt': False, 'downstairs_1': True, 'downstairs_2': True, 'green_liquid': True, 'burned_letter': True, 'day1_drunk': False}},
                {"label": "lad_day2_evening", "threads": {'hunt': False, 'downstairs_1': True, 'downstairs_2': True, 'green_liquid': True, 'burned_letter': True, 'day1_drunk': True}},
            ],

            # ===== SUNDAY MORNING =====
            # Threads SET before & RELEVANT here:
            #   - day2_drunk: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning']
            #   - trust_psychic: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning']
            # Note: seen_car and gun are set DURING this chapter
            'sunday_morning': [
                {"label": "lad_day3_morning", "threads": {'day2_drunk': False, 'trust_psychic': False}},
                {"label": "lad_day3_morning", "threads": {'day2_drunk': True, 'trust_psychic': False}},
                {"label": "lad_day3_morning", "threads": {'day2_drunk': False, 'trust_psychic': True}},
                {"label": "lad_day3_morning", "threads": {'day2_drunk': True, 'trust_psychic': True}},
            ],

            # ===== SUNDAY AFTERNOON =====
            # Threads SET before & RELEVANT here:
            #   - seen_car: chapters=['sunday_morning'], relevant=['sunday_morning', 'sunday_afternoon']
            #   - gun: chapters=['sunday_morning'], relevant=['sunday_morning', 'sunday_afternoon', 'end']
            # Note: abandoned_psychic and protect_food are set DURING this chapter
            'sunday_afternoon': [
                {"label": "lad_day3_afternoon", "threads": {'seen_car': False, 'gun': False}},
                {"label": "lad_day3_afternoon", "threads": {'seen_car': True, 'gun': False}},
                {"label": "lad_day3_afternoon", "threads": {'seen_car': False, 'gun': True}},
                {"label": "lad_day3_afternoon", "threads": {'seen_car': True, 'gun': True}},
            ],
        }