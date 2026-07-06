label broken_config_progress:
    python:
    # First define the possible progress
        broken_progress = [
            # Row 0: Main path (written to the end - walked_out is the final ending)
            [
                Chapter(image_checkpoint_start, "start", "broken_introduction", "friday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day2_evening", "saturday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day3_morning", "sunday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day3_afternoon", "sunday_afternoon"),
                Chapter(image_ending_question, "ending", "walked_out", "end"),
            ],
            # Row 1: trunks drop one row - friday_evening at col1, the hunt at col3,
            # saturday_evening's single branch (burned) turns right at col4, and
            # sunday_afternoon's single branch (ambushed) turns right at col6
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_line),            # col1 trunk (Saturday-morning deaths)
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col3 trunk (Saturday-hunt deaths)
                Chapter(image_checkpoint_corner),          # col4 branch (burned - the only one)
                Chapter(image_ending_question, "ending", "burned", "saturday_evening"),
                Chapter(image_checkpoint_empty_half),      # filler completing the burned cell
                Chapter(image_checkpoint_corner),          # col6 branch (ambushed - the only one)
                Chapter(image_ending_question, "ending", "ambushed", "sunday_afternoon"),
            ],
            # Row 2: first branch on each trunk, on the same line -
            #   col1 -> deathbed (Friday whisky), col3 -> strangled (killed the Captain)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_double_corner),   # col1 branch (more below)
                Chapter(image_ending_question, "ending", "deathbed", "saturday_morning"),
                Chapter(image_checkpoint_empty_half),      # filler completing the deathbed cell
                Chapter(image_checkpoint_double_corner),   # col3 branch (more below)
                Chapter(image_ending_question, "ending", "strangled", "saturday_afternoon"),
            ],
            # Row 3: col1's last branch (throat_cut) and col3's second hunt branch
            #   (shot); the col3 trunk carries on one row lower to the grove death.
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_corner),          # col1 branch (last)
                Chapter(image_ending_question, "ending", "throat_cut", "saturday_morning"),
                Chapter(image_checkpoint_empty_half),      # filler completing the throat_cut cell
                Chapter(image_checkpoint_double_corner),   # col3 branch (more below)
                Chapter(image_ending_question, "ending", "shot", "saturday_afternoon"),
            ],
            # Row 4: the western-grove death hangs one row lower on the col3 trunk -
            #   shielded (took Manning's bullet meant for Doctor Baldwin)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_corner),          # col3 branch (last)
                Chapter(image_ending_question, "ending", "shielded", "saturday_afternoon"),
            ],
        ]

    # Define Checkpoints for TEST
    # Each chapter maps to a list of checkpoint configurations
    # Each config has: label (Ren'Py label) and threads (dict of thread_id: True/False)
    # Only the written chapters are listed here.
        broken_test_checkpoints = {
            # ===== FRIDAY AFTERNOON =====
            # First chapter - no threads set yet
            'friday_afternoon': [
                {"label": "broken_introduction", "threads": {}},
            ],

            # ===== FRIDAY EVENING =====
            # No threads from previous chapters are relevant yet.
            'friday_evening': [
                {"label": "broken_day1_evening", "threads": {}},
            ],

            # ===== SATURDAY MORNING =====
            # Branches on whether the maid was questioned (talked_to_maid) and
            # whether the rat poison was taken from the scullery (found_poison)
            # on Friday night.
            'saturday_morning': [
                {"label": "broken_day2_morning", "threads": {}},
                {"label": "broken_day2_morning", "threads": {'talked_to_maid': True}},
                {"label": "broken_day2_morning", "threads": {'found_poison': True}},
                {"label": "broken_day2_morning", "threads": {'talked_to_maid': True, 'found_poison': True}},
            ],

            # ===== SATURDAY AFTERNOON (THE HUNT) =====
            # Anger beats are tempered by host_lies / talked_to_maid. With
            # talked_to_maid the player gets the spare/kill menu; without it the
            # kill is forced.
            'saturday_afternoon': [
                {"label": "broken_day2_hunt", "threads": {}},
                {"label": "broken_day2_hunt", "threads": {'host_lies': True}},
                {"label": "broken_day2_hunt", "threads": {'talked_to_maid': True, 'host_lies': True}},
            ],

            # ===== SATURDAY EVENING (AFTER THE HUNT) =====
            # Only reachable via the western grove with Mr Manning talked down,
            # so talked_to_maid, host_lies and drunk_letter are always unlocked
            # here. Branches on found_poison (the scullery bottle, Friday night):
            # with it Broken refuses to sleep, without it the manor burns.
            'saturday_evening': [
                {"label": "broken_day2_evening", "threads": {'talked_to_maid': True, 'host_lies': True, 'drunk_letter': True, 'found_poison': False}},
                {"label": "broken_day2_evening", "threads": {'talked_to_maid': True, 'host_lies': True, 'drunk_letter': True, 'found_poison': True}},
            ],

            # ===== SUNDAY MORNING (AN EMPTY MANOR) =====
            # Only reachable from the vigil, so found_poison is always unlocked.
            # The departure menu branches on the 'ambushed' ENDING (intuition),
            # not on a thread, so a single checkpoint config suffices.
            'sunday_morning': [
                {"label": "broken_day3_morning", "threads": {'talked_to_maid': True, 'host_lies': True, 'drunk_letter': True, 'found_poison': True}},
            ],

            # ===== SUNDAY AFTERNOON (THE WALK) =====
            # Branches on left_together (set in the morning): without it the
            # two-man walk ends in the ambush, with it the whole party reaches
            # the police station.
            'sunday_afternoon': [
                {"label": "broken_day3_afternoon", "threads": {'talked_to_maid': True, 'host_lies': True, 'drunk_letter': True, 'found_poison': True, 'left_together': False}},
                {"label": "broken_day3_afternoon", "threads": {'talked_to_maid': True, 'host_lies': True, 'drunk_letter': True, 'found_poison': True, 'left_together': True}},
            ],
        }
