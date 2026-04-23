label captain_config_progress:
    python:
    # First define the possible progress
        captain_progress = [
            # Row 0: Main path (up to Saturday evening for now)
            [
                Chapter(image_checkpoint_start, "start", "captain_introduction", "friday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "captain_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "captain_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "captain_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "captain_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
            ],
            # Second line, ...
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),
            ],
            # Row 3: strangled ending (Moody dead + confront host)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_double_corner),
                Chapter(image_ending_question, "ending", "strangled", "saturday_afternoon"),
            ],
            # Row 4: shot_in_woods ending (Moody alive)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "shot_in_woods", "saturday_afternoon"),
            ],
        ]

    # Define Checkpoints for TEST
    # Each chapter maps to a list of checkpoint configurations
    # Each config has: label (Ren'Py label) and threads (dict of thread_id: True/False)
    # Rule: threads must be SET in a previous chapter AND be RELEVANT to the current chapter
        captain_test_checkpoints = {
            # ===== FRIDAY AFTERNOON =====
            # First chapter - no threads set yet
            'friday_afternoon': [
                {"label": "captain_introduction", "threads": {}},
            ],

            # ===== FRIDAY EVENING =====
            # No threads from previous chapters are relevant here.
            # Threads SET here:
            #   - captain_host_suspicion_name (library)
            #   - captain_host_suspicion_portrait (portrait gallery)
            #   - captain_garden_shed_locked (garden shed)
            'friday_evening': [
                {"label": "captain_day1_evening", "threads": {}},
            ],

            # ===== SATURDAY MORNING =====
            # Threads SET before (friday_evening) & RELEVANT here:
            #   - tell_boxer_story: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening', 'sunday_morning']
            #     (drives the main branching — told: Moody is found dead / refused: Moody arrives alive)
            #   - captain_host_suspicion_name: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening']
            #   - captain_host_suspicion_portrait: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening']
            #   - captain_garden_shed_locked: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening']
            # Alive branch: all 8 suspicion/shed combinations.
            # Death branch: 2 focused entries (bare + both suspicions) to exercise both narration paths.
            'saturday_morning': [
                # --- Alive branch (tell_boxer_story refused) ---
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': True}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': True}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': True}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': True}},
                # --- Death branch (tell_boxer_story told) ---
                {"label": "captain_day2_morning", "threads": {'tell_boxer_story': True, 'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'tell_boxer_story': True, 'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': False}},
            ],

            # ===== SATURDAY AFTERNOON (THE HUNT) =====
            # Threads SET before & RELEVANT here:
            #   - tell_boxer_story: relevant=['saturday_morning', 'saturday_afternoon', ...] — Moody dead/alive context
            #   - captain_host_suspicion_name / _portrait: gate the host confrontation branch
            # Threads SET here:
            #   - captain_host_suspicion_shooting (observed on the hunt itself)
            # Endings fired here:
            #   - Moody alive  -> shot_in_woods (linear death)
            #   - Moody dead + both host suspicions + confront -> strangled
            'saturday_afternoon': [
                # --- Moody alive, no host suspicion (linear death by Moody) ---
                {"label": "captain_day2_hunt", "threads": {'tell_boxer_story': False}},
                # --- Moody alive, both host suspicions (still linear death by Moody) ---
                {"label": "captain_day2_hunt", "threads": {'tell_boxer_story': False, 'captain_host_suspicion_name': True, 'captain_host_suspicion_portrait': True}},
                # --- Moody dead, no host suspicion (silent luncheon, survives) ---
                {"label": "captain_day2_hunt", "threads": {'tell_boxer_story': True}},
                # --- Moody dead, both host suspicions (opens confrontation menu; survives or dies strangled) ---
                {"label": "captain_day2_hunt", "threads": {'tell_boxer_story': True, 'captain_host_suspicion_name': True, 'captain_host_suspicion_portrait': True}},
            ],

            # ===== SATURDAY EVENING =====
            # Only reachable on the Moody-dead branch, so tell_boxer_story is always True here.
            # Threads SET before & RELEVANT here:
            #   - tell_boxer_story: relevant=['saturday_evening'] (doctor carried in, three chairs empty at dinner)
            #   - captain_host_suspicion_name / _portrait: set friday_evening, relevant saturday_evening
            #   - captain_host_suspicion_shooting: set saturday_afternoon, relevant saturday_evening
            #   All three host suspicions together unlock the confrontation menu in the hall.
            # Threads SET here:
            #   - butler_key (pocketed on the normal escort path)
            # Saved variables SET here:
            #   - confronted_host_publicly (changes the dinner narration)
            'saturday_evening': [
                # --- Bare path: no host suspicions, normal escort only ---
                {"label": "captain_day2_evening", "threads": {'tell_boxer_story': True}},
                # --- Two of three suspicions (missing shooting): still no confrontation menu ---
                {"label": "captain_day2_evening", "threads": {'tell_boxer_story': True, 'captain_host_suspicion_name': True, 'captain_host_suspicion_portrait': True}},
                # --- All three host suspicions: unlocks the confrontation menu ---
                {"label": "captain_day2_evening", "threads": {'tell_boxer_story': True, 'captain_host_suspicion_name': True, 'captain_host_suspicion_portrait': True, 'captain_host_suspicion_shooting': True}},
            ],
        }
