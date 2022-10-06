label debug_choices:
    call debug_routes
    
    menu: 
        "lad Drinks":
            $ test_choices = []
            jump lad_introduction

        "lad Dinner":
            $ test_choices = lad_dinner_simple
            jump lad_introduction

        "lad Evening":
            # $ test_choices = lad_evening_simple
            $ test_choices = lad_evening_doctor
            jump lad_introduction
        
        "lad Evening - Billiard":
            $ test_choices = lad_day1_billiard
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

        lad_dinner_simple = [
            0, # Talk to the man => not needed?
            1, # Talk to the woman
            5, # Learn nothing about the psychic
        ]

        lad_evening_simple = lad_dinner_simple + [
            0, # Doctor
            3, # Early leave
            1, # Psychic
            3, # Early leave
        ]

        lad_evening_doctor = lad_dinner_simple + [
            0, # Learn about the doctor Doctor 
            0,
            1,
            3, # Early leave
            1, # Psychic
            3, # Early leave
        ]


        lad_day1_billiard = lad_evening_doctor + [
            1, # Billiard Room 
        ]
