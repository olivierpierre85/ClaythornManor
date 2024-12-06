label debug_choices:
    call debug_routes

    $ skip_clock_movement = True

    # Comment to test tutorials
    $ seen_tutorial_description_hidden = True
    $ seen_tutorial_clock = True
    $ seen_tutorial_map = True
    $ seen_tutorial_unlock_character = True
    $ seen_tutorial_timeline = True

    # show screen current_time
    show screen in_game_menu_btn

    call unlock_bedrooms
    
    menu: 
        "character selection":
            call unlock_psychic 
            call unlock_lad
            jump character_selection
        
        "debug_test":
            $ test_choices = debug_lad_poisoned_day1
            # call unlock_lad
            # call unlock_psychic
            # call unlock_doctor
            # call unlock_captain
            # call unlock_nurse
            # call unlock_host
            # call unlock_broken
            # call unlock_drunk
            jump lad_introduction

        "lad_introduction":
            jump lad_introduction

        # "lad_day1_afternoon":
        #     jump lad_day1_afternoon

        # "lad_day1_evening MAP":
        #     $ test_choices = [0,9,1,12] #SKIP to map menu
        #     jump lad_day1_evening
        
        # "lad_day1_evening":
        #     jump lad_day1_evening

        # "lad_day2_morning":
        #     jump lad_day2_morning
            
        # "lad_day2_hunt":
        #     jump lad_day2_hunt

        # "lad_day2_no_hunt MAP":
        #     # Has try to go downstairs
        #     $ lad_details.saved_variables["has_met_maid"] = True
        #     $ lad_details.saved_variables["has_try_sneaking_downstairs"] = 1
        #     $ lad_details.saved_variables["library_visited"] = True
        #     $ lad_details.saved_variables["portrait_gallery_visited"] = True
        #     $ lad_details.saved_variables["attic_visited"] = True
            
        #     jump lad_day2_no_hunt

        # "lad_day2_afternoon":
        #     $ lad_details.objects.unlock('burned_letter')
        #     jump lad_day2_afternoon
            
        # # # "lad_day2_afternoon_bedroom":
        # # #     jump lad_day2_afternoon_bedroom
            
        # "lad_day2_evening MAP":
        #     #$ lad_details.objects.unlock('gun')
        #     $ lad_details.intuitions.unlock('psychic_poisons')
        #     $ lad_details.observations.unlock('green_liquid')
        #     $ doctor_details.description_hidden.unlock('addict')

        #     $ lad_details.saved_variables["has_try_sneaking_downstairs"] = 2

        #     $ lad_details.saved_variables["day2_saw_accident"] = True
        #     jump lad_day2_evening

        "lad_day3_morning TES MAP":
            $ lad_details.saved_variables["day2_believe_psychic"] = True
            
            jump lad_day3_morning
        
        "lad_day3_afternoon PROGRESS":
            call unlock_psychic 
            $ lad_details.observations.unlock('green_liquid')
            $ lad_details.saved_variables['library_visited'] = True
            $ lad_details.test_checkpoints()

            $ lad_day2_believe_psychic = True #TODO put in a information (CHOICE)
            $ lad_details.objects.unlock('gun')
            $ first_death = False
            $ lad_details.intuitions.unlock('psychic_poisons')
            $ lad_details.endings.unlock('gunned_down')

            $ lad_details.reset_information()
            # $ lad_details.objects.unlock('gun')
            $ lad_details.important_choices.unlock('hunt')

            jump lad_day3_afternoon

        # "lad_day3_stay":
        #     $ lad_details.intuitions.unlock(('psychic_poisons'))
            
        #     jump lad_day3_stay

        # "psychic_introduction":
        #     call unlock_psychic
        #     $ current_character = psychic_details
        #     jump psychic_introduction
        
        # "captain_introduction":
        #     $ current_character = captain_details
        #     $ lad_details.description_hidden.unlock('origin') 
        #     $ lad_details.description_hidden.unlock('age')
        #     $ doctor_details.description_hidden.unlock('addict') 
        #     jump captain_introduction

        "psychic_day1_evening":
            $ psychic_details.saved_variables["knows_captain_origin"] = True
            $ psychic_details.saved_variables["knows_captain_real_origin"] = True
            call unlock_psychic
            $ current_character = psychic_details

            # $ psychic_details.observations.unlock('lord')
            # $ lord_name = "Sir Nicholas"
            jump psychic_day1_evening
        

        "psychic_day2_morning":
            $ psychic_details.saved_variables["knows_captain_origin"] = True
            $ psychic_details.saved_variables["knows_captain_real_origin"] = True
            call unlock_psychic
            $ current_character = psychic_details

            $ psychic_details.observations.unlock('lord')
            $ lord_name = "Sir Nicholas"

            jump psychic_day2_morning
        
        # "psychic_day2_no_hunt":
        #     $ psychic_details.saved_variables["knows_captain_origin"] = True
        #     $ psychic_details.saved_variables["knows_captain_real_origin"] = True
        #     call unlock_psychic
        #     $ current_character = psychic_details
        #     jump psychic_day2_no_hunt

        "psychic_day2_afternoon":
            $ psychic_details.saved_variables["knows_captain_origin"] = True
            $ psychic_details.saved_variables["knows_captain_real_origin"] = True
            call unlock_psychic
            $ current_character = psychic_details
            jump psychic_day2_afternoon

        "psychic_day2_evening":
            $ psychic_details.saved_variables["knows_captain_origin"] = True
            $ psychic_details.saved_variables["knows_captain_real_origin"] = True
            call unlock_psychic
            $ current_character = psychic_details
            jump psychic_day2_evening

        "psychic_day3_morning":
            $ psychic_details.saved_variables["knows_captain_origin"] = True
            $ psychic_details.saved_variables["knows_captain_real_origin"] = True
            call unlock_psychic
            $ current_character = psychic_details

            jump  psychic_day3_morning

        "psychic_day3_afternoon":
            $ psychic_details.saved_variables["knows_captain_origin"] = True
            $ psychic_details.saved_variables["knows_captain_real_origin"] = True
            call unlock_psychic
            $ current_character = psychic_details
            $ psychic_details.intuitions.unlock('leave_castle')   
            $ psychic_details.endings.unlock('burned')
            jump  psychic_day3_afternoon


            
    return

label unlock_psychic:

    $ psychic_details.description_hidden.unlock('background') 
    $ lad_details.saved_variables['knows_psychic_background'] = True
    $ psychic_details.description_hidden.unlock('status') 
    $ psychic_details.description_hidden.unlock('heroic_act') 
    $ psychic_details.description_hidden.unlock('lie') 
    $ psychic_details.description_hidden.unlock('age') 
    $ psychic_details.description_hidden.unlock('drive') 
    $ psychic_details.description_hidden.unlock('racist') 
    
    return

label unlock_bedrooms:

    $ unlock_map('bedroom_captain')
    $ unlock_map('bedroom_host')
    $ unlock_map('bedroom_psychic')
    $ unlock_map('bedroom_lad')
    $ unlock_map('bedroom_drunk')
    $ unlock_map('bedroom_nurse')
    $ unlock_map('bedroom_broken')
    $ unlock_map('bedroom_doctor')

    return

label unlock_lad:

    $ lad_details.description_hidden.unlock('age')  # "22 years old - which means he was merely 15"
    $ lad_details.description_hidden.unlock('origin')  # "Birmingham"
    $ lad_details.description_hidden.unlock('poor')  # "a wealthy family, nor even a decent one"
    $ lad_details.description_hidden.unlock('childhood')  # "he doesn't have a family at all; he was raised in an orphanage"
    $ lad_details.description_hidden.unlock('education')  # "the best education, and, like a large number of individuals from similar backgrounds, he can barely read"
    $ lad_details.description_hidden.unlock('job')  # "on the 'informal sector' for employment"
    $ lad_details.description_hidden.unlock('thief')  # "sometimes means being on the wrong side of the law"
    $ lad_details.description_hidden.unlock('heroic_act')  # "saving a young infant from a burning building. This act of heroism made him the subject of a newspaper article"
    $ lad_details.description_hidden.unlock('poor_drinker')  # "drinker"
    $ lad_details.description_hidden.unlock('drive')  # "drive a car"
    $ lad_details.description_hidden.unlock('cook')  # "cook a meal"

    return

label unlock_doctor:

    $ doctor_details.description_hidden.unlock('background')
    $ doctor_details.description_hidden.unlock('heroic_act')
    $ doctor_details.description_hidden.unlock('status') 
    $ doctor_details.description_hidden.unlock('age') 
    $ doctor_details.description_hidden.unlock('addict')
    $ doctor_details.description_hidden.unlock('fraud')
    $ doctor_details.description_hidden.unlock('gay')

    return

label unlock_captain:

    $ captain_details.description_hidden.unlock('wars')
    $ captain_details.description_hidden.unlock('talker')
    $ captain_details.description_hidden.unlock('heroic_act') 
    $ captain_details.description_hidden.unlock('city') 
    $ captain_details.description_hidden.unlock('age')
    $ captain_details.description_hidden.unlock('mansion')
    $ captain_details.description_hidden.unlock('table') 
    $ captain_details.description_hidden.unlock('family')
    $ captain_details.description_hidden.unlock('lie')

    return

label unlock_nurse:

    $ nurse_details.description_hidden.unlock('job')
    $ nurse_details.description_hidden.unlock('clothes')
    $ nurse_details.description_hidden.unlock('age') 
    $ nurse_details.description_hidden.unlock('manor') 
    $ nurse_details.description_hidden.unlock('sick')
    $ nurse_details.description_hidden.unlock('heroic_act')
    $ nurse_details.description_hidden.unlock('lie') 

    return

label unlock_host:

    $ host_details.description_hidden.unlock('name')
    $ host_details.description_hidden.unlock('down_to_earth')
    $ host_details.description_hidden.unlock('independent') 
    $ host_details.description_hidden.unlock('guns') 
    $ host_details.description_hidden.unlock('car')
    $ host_details.description_hidden.unlock('lie') 

    return

label unlock_broken:

    $ broken_details.description_hidden.unlock('mask')
    $ broken_details.description_hidden.unlock('age')
    $ broken_details.description_hidden.unlock('background') 
    $ broken_details.description_hidden.unlock('job') 
    $ broken_details.description_hidden.unlock('heroic_act')
    $ broken_details.description_hidden.unlock('city')
    $ broken_details.description_hidden.unlock('shy')
    $ broken_details.description_hidden.unlock('lie') 

    return

label unlock_drunk:
    $ drunk_details.description_hidden.unlock('background')
    $ drunk_details.description_hidden.unlock('status')
    $ drunk_details.description_hidden.unlock('age')
    $ drunk_details.description_hidden.unlock('wife') 
    $ drunk_details.description_hidden.unlock('addict') 
    $ drunk_details.description_hidden.unlock('job')
    $ drunk_details.description_hidden.unlock('heroic_act')
    $ drunk_details.description_hidden.unlock('lie') 

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
