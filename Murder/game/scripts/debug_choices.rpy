label debug_choices:
    call debug_routes
    
    menu: 
        "debug_lad_first_death":
            $ test_choices = debug_lad_first_death
            jump lad_introduction

        "lad_introduction":
            jump lad_introduction

        "lad_day1_drinks":
            jump lad_day1_drinks

        "lad_day2_dinner":
            $ test_choices = debug_lad_evening
            jump lad_day2_evening_tea_room
        
        # "lad_day2_hunt":
        #     jump lad_day2_hunt
            
        # "lad_day2_morning_nohunt":
        #     jump lad_day2_morning_nohunt

        # "lad_day2_afternoon":
        #     jump lad_day2_afternoon
            
        # "lad_day2_afternoon_bedroom":
        #     jump lad_day2_afternoon_bedroom
            
        # "lad_day2_evening":
        #     jump lad_day2_evening

        # "lad_day3_morning":
        #     jump lad_day3_morning
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
        ]

        debug_lad_evening = [
            1, # Talk to the woman
            6, # You don't have anymore questions for her
            0, # Talk to the man
        ]

        debug_lad_first_death = [
            1, # Talk to the woman
            6, # You don't have anymore questions for her
            0, # Talk to the man
            1, # Talk to Amelia Baxter
            6, # You don't have anymore questions for her
            0, # Talk to Daniel Baldwin
            5, # You don't have anymore questions for him
            1, # Meet the others in the billiard room
            2, # Go to the bar to have a drink
            5, # Leave the room
            3, # Go to sleep
        ]
