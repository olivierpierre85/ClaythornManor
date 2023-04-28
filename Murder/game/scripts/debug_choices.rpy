label debug_choices:
    call debug_routes

    $ skip_clock_movement = True

    $ seen_tutorial_knowledge = True
    $ seen_tutorial_map = True
    $ seen_tutorial_unlock_character = True
    $ seen_tutorial_timeline = True

    # show screen current_time
    show screen in_game_menu_btn
    
    menu: 
        "character selection":
            call unlock_psychic 
            jump character_selection
        
        "debug_lad":
            $ test_choices = debug_lad_poisoned_day1
            jump lad_introduction

        "lad_introduction":
            jump lad_introduction

        # "lad_day1_afternoon":
        #     jump lad_day1_afternoon

        "lad_day1_evening MAP":
            $ test_choices = [0,9,1,12] #SKIP to map menu
            jump lad_day1_evening
        
        # "lad_day1_evening":
        #     jump lad_day1_evening

        # "lad_day2_morning":
        #     jump lad_day2_morning
            
        # "lad_day2_hunt":
        #     jump lad_day2_hunt

        "lad_day2_no_hunt MAP":
            # Has try to go downstairs
            $ lad_details.saved_variables["has_met_maid"] = True
            $ lad_details.saved_variables["has_try_sneaking_downstairs"] = 1
            $ lad_details.saved_variables["library_visited"] = True
            $ lad_details.saved_variables["portrait_gallery_visited"] = True
            $ lad_details.saved_variables["attic_visited"] = True
            
            jump lad_day2_no_hunt

        "lad_day2_afternoon":
            $ lad_details.objects.unlock('burned_letter')
            jump lad_day2_afternoon
            
        # "lad_day2_afternoon_bedroom":
        #     jump lad_day2_afternoon_bedroom
            
        "lad_day2_evening WITH unlocked":
            #$ lad_details.objects.unlock('gun')
            $ lad_details.intuitions.unlock('psychic_poisons')
            $ lad_details.observations.unlock('green_liquid')
            $ doctor_details.unlock_knowledge('addict')

            $ lad_details.saved_variables["day2_saw_accident"] = True
            jump lad_day2_evening

        "lad_day3_morning TES MAP":
            $ unlock_map('captain_room')
            $ unlock_map('host_room')
            $ unlock_map('psychic_room')
            $ unlock_map('lad_room')
            $ unlock_map('drunk_room')
            $ unlock_map('nurse_room')
            $ unlock_map('broken_room')
            $ unlock_map('doctor_room')
            $ lad_details.saved_variables["day2_believe_psychic"] = True
            jump lad_day3_morning
        
        "lad_day3_afternoon":
            call unlock_psychic 
            $ lad_details.observations.unlock('green_liquid')
            $ lad_details.saved_variables['library_visited'] = True
            $ lad_details.test_checkpoint()

            $ lad_day2_believe_psychic = True #TODO put in a information (CHOICE)
            $ lad_details.objects.unlock('gun')
            $ first_death = False
            $ lad_details.intuitions.unlock('psychic_poisons')
            $ lad_details.endings.unlock('gunned_down')
            
            $ lad_details.reset_information()
            $ lad_details.objects.unlock('gun')

            $ lad_details.important_choices.unlock('hunt')

            jump lad_day3_afternoon

        # "lad_day3_stay":
        #     $ lad_details.intuitions.unlock(('psychic_poisons')
        #     jump lad_day3_stay

        "psychic_introduction":
            call unlock_psychic
            $ current_character = psychic_details
            jump psychic_introduction
        
        # "captain_introduction":
        #     jump captain_introduction

        "psychic_day1_arrival":
            call unlock_psychic
            $ current_character = psychic_details
            jump psychic_day1_arrival

        "psychic_day1_dinner":
            $ psychic_details.saved_variables["knows_captain_real_origin"] = True
            call unlock_psychic
            $ current_character = psychic_details
            jump psychic_day1_evening

        "psychic_day1_evening":
            $ psychic_details.saved_variables["knows_captain_real_origin"] = True
            call unlock_psychic
            $ current_character = psychic_details
            jump psychic_day1_evening
            
    return

label unlock_psychic:

    $ psychic_details.unlock_knowledge('background') 
    $ lad_details.saved_variables['knows_psychic_background'] = True
    $ psychic_details.unlock_knowledge('status') 
    $ psychic_details.unlock_knowledge('heroic act') 
    $ psychic_details.unlock_knowledge('lie') 
    
    return

label debug_routes:
    python:
        # record_mode = True
        test_choices = []

        debug_lad_poisoned_day1 = [
            0, # Talk to Samuel Manning
            1, # Talk to Amelia Baxter
            11, # You don't have anymore questions for her
            0, # Talk to Daniel Baldwin
            9, # You don't have anymore questions for him
            1, # Talk to Amelia Baxter
            11, # You don't have anymore questions for her
            2, # Meet the others in the billiard room
            2, # Go to the bar to have a drink
            5, # Leave the room
            3, # Go to sleep
        ]

        debug_lad_first_death = [
        ]

    return
