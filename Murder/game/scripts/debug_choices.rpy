label debug_choices:
    call debug_routes
    
    menu: 
        "debug_path_01":
            $ test_choices = debug_path_01
            jump lad_introduction

        "lad_day1_arrival":
            jump lad_day1_arrival

        "lad_day1_evening":
            jump lad_day1_evening

    return

label debug_routes:
    python:
        test_mode = True
        test_choices = []

        debug_path_01 = [
            0,# Talk To the man
            1,# Talk To the woman
            3,# How old are you ?
            1,# Ask her about herself
            0,# Talk to Daniel Baldwin
            2,# Why were you invited here ?
            3,# Talk about the manor
            1,# Ask him about himself
            4,# Ask him his age
            0,# Talk about the weather
            3,# Go to sleep
        ]

        # debug_path = [

        # ]

        # lad_dinner_simple = [
        #     0, # Talk to the man => not needed?
        #     1, # Talk to the woman
        #     5, # Learn nothing about the psychic
        # ]

        # lad_evening_simple = lad_dinner_simple + [
        #     0, # Doctor
        #     3, # Early leave
        #     1, # Psychic
        #     3, # Early leave
        # ]

        # lad_evening_doctor = lad_dinner_simple + [
        #     0, # Learn about the doctor Doctor 
        #     0,
        #     1,
        #     3, # Early leave
        #     1, # Psychic
        #     3, # Early leave
        # ]


        # lad_day1_billiard = lad_evening_doctor + [
        #     1, # Billiard Room 
        # ]
