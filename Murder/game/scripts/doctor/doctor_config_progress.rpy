label doctor_config_progress:
    python:  
    # First define the possible progress
        doctor_progress = [
            # First Line
            [
                Chapter(image_checkpoint_start, "start", "doctor_introduction", "friday_afternoon"), 
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "doctor_day3_afternoon", "sunday_afternoon"),
                Chapter(image_ending_question, "ending", "poisoned", "end"),
            ],
            # Second line, ...
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "escape", "end"),
            ],
            # 3
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "overdose", "saturday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_line),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "throat_cut", "sunday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "escape_group", "end"),

            ],
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "burned", "saturday_morning"),
                Chapter(image_checkpoint_empty_after_ending),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "shot_by_drunk", "saturday_evening"),
            ],
        ]

    # Define Checkpoints for TEST
    # Each chapter maps to a list of checkpoint configurations
    # Each config has: label (Ren'Py label) and threads (dict of thread_id: True/False)
    # Rule: threads must be SET in a previous chapter AND be RELEVANT to the current chapter
        doctor_test_checkpoints = {
            # ===== FRIDAY AFTERNOON =====
            # First chapter - no threads set yet
            'friday_afternoon': [
                {"label": "doctor_introduction", "threads": {}},
            ],

            # ===== FRIDAY EVENING =====
            # No threads from previous chapters are relevant here
            # Threads SET here: broken_offended, flirt, book_mystery, book_opium, footman_french_1, drunk_letter
            'friday_evening': [
                {"label": "doctor_day1_evening", "threads": {}},
            ],

            # ===== SATURDAY MORNING =====
            # Threads SET before (friday_evening) & RELEVANT here:
            #   - book_mystery: chapters=['friday_evening'], relevant=['saturday_morning']
            #   - book_opium: chapters=['friday_evening'], relevant=['saturday_morning', 'saturday_afternoon', 'saturday_evening']
            #   - drunk_letter: chapters=['friday_evening'], relevant=['saturday_morning', 'saturday_afternoon']
            # Note: broken_offended, flirt, footman_french_1 set but NOT relevant to saturday_morning
            'saturday_morning': [
                {"label": "doctor_day2_morning", "threads": {'book_mystery': False, 'book_opium': False, 'drunk_letter': False}},
                {"label": "doctor_day2_morning", "threads": {'book_mystery': True, 'book_opium': False, 'drunk_letter': False}},
                {"label": "doctor_day2_morning", "threads": {'book_mystery': False, 'book_opium': True, 'drunk_letter': False}},
                {"label": "doctor_day2_morning", "threads": {'book_mystery': True, 'book_opium': True, 'drunk_letter': False}},
                {"label": "doctor_day2_morning", "threads": {'book_mystery': False, 'book_opium': False, 'drunk_letter': True}},
                {"label": "doctor_day2_morning", "threads": {'book_mystery': True, 'book_opium': True, 'drunk_letter': True}},
            ],

            # ===== SATURDAY AFTERNOON =====
            # Threads SET before & RELEVANT here:
            #   - flirt: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - book_opium: chapters=['friday_evening'], relevant=['saturday_morning', 'saturday_afternoon', 'saturday_evening']
            #   - drunk_letter: chapters=['friday_evening'], relevant=['saturday_morning', 'saturday_afternoon']
            'saturday_afternoon': [
                {"label": "doctor_day2_hunt", "threads": {'flirt': False, 'book_opium': False, 'drunk_letter': False}},
                {"label": "doctor_day2_hunt", "threads": {'flirt': True, 'book_opium': False, 'drunk_letter': False}},
                {"label": "doctor_day2_hunt", "threads": {'flirt': False, 'book_opium': True, 'drunk_letter': False}},
                {"label": "doctor_day2_hunt", "threads": {'flirt': True, 'book_opium': True, 'drunk_letter': True}},
            ],

            # ===== SATURDAY EVENING =====
            # Threads SET before & RELEVANT here:
            #   - flirt: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - broken_unmasked: chapters=['saturday_morning', 'saturday_evening'], relevant=['saturday_morning', 'saturday_evening', 'sunday_morning', 'sunday_afternoon']
            #   - book_opium: chapters=['friday_evening'], relevant=['saturday_morning', 'saturday_afternoon', 'saturday_evening']
            #   - footman_french_1: chapters=['friday_evening', 'saturday_evening'], relevant=['friday_evening', 'saturday_evening']
            #   - remember_nurse: chapters=['saturday_morning'], relevant=['saturday_evening']
            'saturday_evening': [
                {"label": "doctor_day2_evening", "threads": {'flirt': False, 'broken_unmasked': False, 'book_opium': False, 'footman_french_1': False, 'remember_nurse': False}},
                {"label": "doctor_day2_evening", "threads": {'flirt': True, 'broken_unmasked': False, 'book_opium': False, 'footman_french_1': False, 'remember_nurse': False}},
                {"label": "doctor_day2_evening", "threads": {'flirt': False, 'broken_unmasked': True, 'book_opium': False, 'footman_french_1': False, 'remember_nurse': False}},
                {"label": "doctor_day2_evening", "threads": {'flirt': True, 'broken_unmasked': True, 'book_opium': True, 'footman_french_1': False, 'remember_nurse': False}},
                {"label": "doctor_day2_evening", "threads": {'flirt': True, 'broken_unmasked': False, 'book_opium': False, 'footman_french_1': True, 'remember_nurse': False}},
                {"label": "doctor_day2_evening", "threads": {'flirt': True, 'broken_unmasked': True, 'book_opium': True, 'footman_french_1': True, 'remember_nurse': True}},
            ],

            # ===== SUNDAY MORNING =====
            # Threads SET before & RELEVANT here:
            #   - flirt: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_afternoon', 'saturday_evening', 'sunday_morning']
            #   - broken_unmasked: chapters=['saturday_morning', 'saturday_evening'], relevant=['saturday_morning', 'saturday_evening', 'sunday_morning', 'sunday_afternoon']
            #   - trust_captain: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning', 'sunday_afternoon']
            #   - trust_nurse: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning', 'sunday_afternoon']
            #   - footman_actor: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning']
            'sunday_morning': [
                {"label": "doctor_day3_morning", "threads": {'flirt': False, 'broken_unmasked': False, 'trust_captain': False, 'trust_nurse': False, 'footman_actor': False}},
                {"label": "doctor_day3_morning", "threads": {'flirt': True, 'broken_unmasked': False, 'trust_captain': False, 'trust_nurse': False, 'footman_actor': False}},
                {"label": "doctor_day3_morning", "threads": {'flirt': False, 'broken_unmasked': True, 'trust_captain': False, 'trust_nurse': False, 'footman_actor': False}},
                {"label": "doctor_day3_morning", "threads": {'flirt': False, 'broken_unmasked': False, 'trust_captain': True, 'trust_nurse': False, 'footman_actor': False}},
                {"label": "doctor_day3_morning", "threads": {'flirt': False, 'broken_unmasked': False, 'trust_captain': False, 'trust_nurse': True, 'footman_actor': False}},
                {"label": "doctor_day3_morning", "threads": {'flirt': True, 'broken_unmasked': True, 'trust_captain': True, 'trust_nurse': False, 'footman_actor': True}},
                {"label": "doctor_day3_morning", "threads": {'flirt': True, 'broken_unmasked': True, 'trust_captain': False, 'trust_nurse': True, 'footman_actor': True}},
            ],

            # ===== SUNDAY AFTERNOON =====
            # Threads SET before & RELEVANT here:
            #   - broken_unmasked: chapters=['saturday_morning', 'saturday_evening'], relevant=['saturday_morning', 'saturday_evening', 'sunday_morning', 'sunday_afternoon']
            #   - trust_captain: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning', 'sunday_afternoon']
            #   - trust_nurse: chapters=['saturday_evening'], relevant=['saturday_evening', 'sunday_morning', 'sunday_afternoon']
            'sunday_afternoon': [
                # =========================================================
                # Case A: trust_captain = True, trust_nurse = False
                # remember_nurse can be False/True
                # =========================================================
                # broken_unmasked = False
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': False, 'trust_captain': True,  'trust_nurse': False, 'footman_actor': False, 'remember_nurse': False}},
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': False, 'trust_captain': True,  'trust_nurse': False, 'footman_actor': False, 'remember_nurse': True}},
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': False, 'trust_captain': True,  'trust_nurse': False, 'footman_actor': True,  'remember_nurse': False}},
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': False, 'trust_captain': True,  'trust_nurse': False, 'footman_actor': True,  'remember_nurse': True}},

                # broken_unmasked = True
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': True,  'trust_captain': True,  'trust_nurse': False, 'footman_actor': False, 'remember_nurse': False}},
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': True,  'trust_captain': True,  'trust_nurse': False, 'footman_actor': False, 'remember_nurse': True}},
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': True,  'trust_captain': True,  'trust_nurse': False, 'footman_actor': True,  'remember_nurse': False}},
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': True,  'trust_captain': True,  'trust_nurse': False, 'footman_actor': True,  'remember_nurse': True}},

                # =========================================================
                # Case B: trust_captain = False, trust_nurse = True
                # remember_nurse forced to True
                # =========================================================
                # broken_unmasked = False
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': False, 'trust_captain': False, 'trust_nurse': True,  'footman_actor': False, 'remember_nurse': True}},
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': False, 'trust_captain': False, 'trust_nurse': True,  'footman_actor': True,  'remember_nurse': True}},

                # broken_unmasked = True
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': True,  'trust_captain': False, 'trust_nurse': True,  'footman_actor': False, 'remember_nurse': True}},
                {"label": "doctor_day3_afternoon", "threads": {'broken_unmasked': True,  'trust_captain': False, 'trust_nurse': True,  'footman_actor': True,  'remember_nurse': True}},
            ],
        }