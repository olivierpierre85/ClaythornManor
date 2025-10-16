# Init variables for debug
label init_debug:

    $ export_transcript_activated = False
    
    $ hide_notifications = True

    $ skip_clock_movement = True

    # Comment to test tutorials
    $ seen_tutorial_description_hidden = True
    $ seen_tutorial_clock = True
    $ seen_tutorial_map = True
    $ seen_tutorial_unlock_character = True
    $ seen_tutorial_progress = True
    $ seen_tutorial_progress_details = True
    $ seen_tutorial_restart = True
    $ seen_tutorial_intuition = True

    # show screen current_time
    show screen in_game_menu_btn
    show screen debug_screen # Screen to show vara

    call unlock_bedrooms

    $ current_character = psychic_details
    $ current_storyline = psychic_details
    call unlock_psychic 
    $ psychic_details.load_test_checkpoints()

    
    $ current_character = lad_details
    $ current_storyline = lad_details # TODO move
    call unlock_lad
    $ lad_details.load_test_checkpoints()
    
    $ current_character = doctor_details
    $ current_storyline = doctor_details
    call unlock_doctor
    $ doctor_details.load_test_checkpoints()

    $ hide_notifications = False

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


label unlock_psychic:

    $ psychic_details.description_hidden.unlock('background') 
    $ psychic_details.description_hidden.unlock('status') 
    $ psychic_details.description_hidden.unlock('heroic_act') 
    $ psychic_details.description_hidden.unlock('lie') 
    $ psychic_details.description_hidden.unlock('age') 
    $ psychic_details.description_hidden.unlock('drive') 
    $ psychic_details.description_hidden.unlock('racist') 
    
    return


label unlock_lad:

    $ lad_details.description_hidden.unlock('age')  # "22 years old - which means he was merely 15"
    $ lad_details.description_hidden.unlock('origin')  # "Birmingham"
    $ lad_details.description_hidden.unlock('poor')  # "a wealthy family, nor even a decent one"
    # $ lad_details.description_hidden.unlock('childhood')  # "he doesn't have a family at all; he was raised in an orphanage"
    # $ lad_details.description_hidden.unlock('education')  # "the best education, and, like a large number of individuals from similar backgrounds, he can barely read"
    $ lad_details.description_hidden.unlock('job')  # "on the 'informal sector' for employment"
    $ lad_details.description_hidden.unlock('thief')  # "sometimes means being on the wrong side of the law"
    $ lad_details.description_hidden.unlock('heroic_act')  # "saving a young infant from a burning building. This act of heroism made him the subject of a newspaper article"
    # $ lad_details.description_hidden.unlock('lie')
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
    # $ doctor_details.description_hidden.unlock('gay')

    return

label unlock_captain:

    $ captain_details.description_hidden.unlock('wars')
    $ captain_details.description_hidden.unlock('talker')
    $ captain_details.description_hidden.unlock('heroic_act') 
    $ captain_details.description_hidden.unlock('city') 
    $ captain_details.description_hidden.unlock('age')
    $ captain_details.description_hidden.unlock('mansion')
    $ captain_details.description_hidden.unlock('table') 
    # $ captain_details.description_hidden.unlock('family')
    $ captain_details.description_hidden.unlock('lie')

    return

label unlock_nurse:

    $ nurse_details.description_hidden.unlock('job')
    $ nurse_details.description_hidden.unlock('clothes')
    $ nurse_details.description_hidden.unlock('age') 
    $ nurse_details.description_hidden.unlock('manor') 
    $ nurse_details.description_hidden.unlock('sick')
    $ nurse_details.description_hidden.unlock('heroic_act')
    # $ nurse_details.description_hidden.unlock('lie') 

    return


label unlock_broken:

    $ broken_details.description_hidden.unlock('mask')
    $ broken_details.description_hidden.unlock('age')
    $ broken_details.description_hidden.unlock('background') 
    $ broken_details.description_hidden.unlock('job') 
    $ broken_details.description_hidden.unlock('heroic_act')
    # $ broken_details.description_hidden.unlock('city')
    # $ broken_details.description_hidden.unlock('shy')
    # $ broken_details.description_hidden.unlock('lie') 

    return


label unlock_host:

    $ host_details.description_hidden.unlock('name_age')
    $ host_details.description_hidden.unlock('down_to_earth')
    # $ host_details.description_hidden.unlock('independent') 
    # $ host_details.description_hidden.unlock('guns') 
    # $ host_details.description_hidden.unlock('car')
    # $ host_details.description_hidden.unlock('lie') 

    return


label unlock_drunk:
    
    # $ drunk_details.description_hidden.unlock('background')
    # $ drunk_details.description_hidden.unlock('status')
    # $ drunk_details.description_hidden.unlock('age')
    # $ drunk_details.description_hidden.unlock('wife') 
    $ drunk_details.description_hidden.unlock('addict') 
    # $ drunk_details.description_hidden.unlock('job')
    # $ drunk_details.description_hidden.unlock('heroic_act')
    # $ drunk_details.description_hidden.unlock('lie') 

    return
