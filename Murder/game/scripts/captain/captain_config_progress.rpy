label captain_config_progress:
    python:
    # First define the possible progress
        captain_progress = [
            # Row 0: Main path (up to Saturday morning for now)
            [
                Chapter(image_checkpoint_start, "start", "captain_introduction", "friday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "captain_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "captain_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
            ],
            # Second line, ...
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_line),
            ],
            # 3
            [
                Chapter(image_checkpoint_empty_small),    
                Chapter(image_checkpoint_corner),
                Chapter(image_ending_question, "ending", "TODO", "saturday_morning"),
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
            #   - captain_host_suspicion_name: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening']
            #   - captain_host_suspicion_portrait: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening']
            #   - captain_garden_shed_locked: chapters=['friday_evening'], relevant=['friday_evening', 'saturday_morning', 'saturday_evening']
            # All eight combinations covered.
            'saturday_morning': [
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': False}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': True}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': False, 'captain_garden_shed_locked': True}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': False, 'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': True}},
                {"label": "captain_day2_morning", "threads": {'captain_host_suspicion_name': True,  'captain_host_suspicion_portrait': True,  'captain_garden_shed_locked': True}},
            ],
        }
