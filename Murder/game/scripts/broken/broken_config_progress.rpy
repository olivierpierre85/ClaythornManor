label broken_config_progress:
    python:
    # First define the possible progress
        broken_progress = [
            # Row 0: Main path (written up to the Saturday hunt)
            [
                Chapter(image_checkpoint_start, "start", "broken_introduction", "friday_afternoon"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day1_evening", "friday_evening"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day2_morning", "saturday_morning"),
                Chapter(image_checkpoint_right, "checkpoint", "broken_day2_hunt", "saturday_afternoon"),
                Chapter(image_checkpoint_empty),   # saturday_evening  (unwritten)
                Chapter(image_checkpoint_empty),   # sunday_morning    (unwritten)
                Chapter(image_checkpoint_empty),   # sunday_afternoon  (unwritten)
                Chapter(image_ending_question, "ending", "todo", "end"),
            ],
            # Row 1: both trunks drop one row - friday_evening at col1, the hunt at col3
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_line),            # col1 trunk (Saturday-morning deaths)
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_line),            # col3 trunk (Saturday-hunt deaths)
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
                Chapter(image_checkpoint_empty),
            ],
            # Row 2: first branch on each trunk, on the same line -
            #   col1 -> deathbed (Friday whisky), col3 -> silenced (killed the Captain)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_double_corner),   # col1 branch (more below)
                Chapter(image_ending_question, "ending", "deathbed", "saturday_morning"),
                Chapter(image_checkpoint_empty_half),      # filler completing the deathbed cell
                Chapter(image_checkpoint_double_corner),   # col3 branch (more below)
                Chapter(image_ending_question, "ending", "silenced", "saturday_afternoon"),
            ],
            # Row 3: last branch on each trunk, on the same line -
            #   col1 -> throat_cut (questioned the maid), col3 -> overtaken (spared the Captain)
            [
                Chapter(image_checkpoint_empty_small),
                Chapter(image_checkpoint_corner),          # col1 branch (last)
                Chapter(image_ending_question, "ending", "throat_cut", "saturday_morning"),
                Chapter(image_checkpoint_empty_half),      # filler completing the throat_cut cell
                Chapter(image_checkpoint_corner),          # col3 branch (last)
                Chapter(image_ending_question, "ending", "overtaken", "saturday_afternoon"),
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
        }
