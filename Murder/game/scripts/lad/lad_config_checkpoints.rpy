label lad_config_checkpoints:
    python:  
        # Define  a list of tuples in the format:
        # (run_number, [list_of_labels], ending_label_if_any)
        lad_test_checkpoints = [
                (1, [
                    ('lad_day1_evening', [('object', 'gun')]), 
                    ('lad_day2_morning', [('important_choice', 'hunt')]),
                    ('lad_day2_hunt', []),
                    ('lad_day2_afternoon', []),
                    ('lad_day2_evening', []),
                    ('lad_day3_morning', []),
                    ('lad_day3_afternoon', []),
                    ],
                'gunned_down'),                
                (2, [
                    ('lad_day2_morning', [('object', 'gun'), ('important_choice', 'hunt')])
                    ], 
                'poisoned'),                
                # (3, ['lad_day1_evening', 'lad_day2_morning'], 'poisoned'),                
                # (4, ['lad_day2_morning', 'lad_day2_afternoon', 'lad_day2_evening'], None),                
                # (5, ['lad_day2_afternoon', 'lad_day2_evening'], None),                
                # (6, ['lad_day2_morning', 'lad_day2_afternoon'], None),
            ]

    return