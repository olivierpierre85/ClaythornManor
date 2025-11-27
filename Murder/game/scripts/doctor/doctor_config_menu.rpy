label doctor_config_menu:

    $ not_broken_offended = "not doctor_details.important_choices.is_unlocked('broken_offended') "

    #---------------------------------------------------------------------
    # BROKEN
    $ broken_generic_menu_doctor = TimedMenu("broken_generic_menu_doctor", [
        TimedMenuChoice('What do you think of this weather?', 'broken_generic_weather_friday', 10, condition = condition_friday + " and " + not_broken_offended),
        TimedMenuChoice('Tell me more about yourself.', 'broken_generic_background', 0, linked_choice ="broken_generic_heroic_act", condition = not_broken_offended, next_menu="broken_generic_background_offense"),
        TimedMenuChoice('Why were you invited here?', 'broken_generic_heroic_act', 0, condition = not_broken_offended + "and all_menus['broken_generic_menu_doctor'].choices[1].hidden", next_menu="broken_generic_heroic_act_offended"),
        TimedMenuChoice('What do you think of this place?', 'broken_generic_manor', 0, condition = not_broken_offended, next_menu="broken_generic_manor_offense"),
        TimedMenuChoice('How old are you?', 'broken_generic_age', 10, condition = not_broken_offended),
        TimedMenuChoice('What room are you in?', 'broken_generic_room', 0, condition = not_broken_offended, next_menu="broken_generic_room_offense"),
        TimedMenuChoice('What do you think of the other guests?', 'broken_generic_other_guests_friday', 0, condition = condition_friday + " and " + not_broken_offended, next_menu="broken_generic_other_guests_friday_offense"),
        TimedMenuChoice('You don\'t have anymore questions for him', 'generic_cancel', 0, keep_alive = True, early_exit = True, condition = not_broken_offended)
    ], image_right = "broken")

    #---------------------------------------------------------------------
    # LAD

    $ lad_generic_menu_doctor = TimedMenu("lad_generic_menu_doctor", [
        TimedMenuChoice('Tell me more about yourself.', 'lad_generic_background_doctor', 0, linked_choice ="lad_generic_heroic_act_doctor", next_menu="lad_generic_background_doctor"),
        TimedMenuChoice('Why were you invited here?', 'lad_generic_heroic_act_doctor', 30, condition = "all_menus['lad_generic_menu_doctor'].choices[0].hidden"),
        TimedMenuChoice('What do you think of this place?', 'lad_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'lad_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_friday', 10, condition = condition_friday_dinner),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_doctor', 10, condition = "not " + condition_friday_dinner),
        TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_friday_dinner', 10, condition = condition_friday_dinner),
        TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_friday_doctor', 10, condition = "not " + condition_friday_dinner + " and not " + condition_saturday),
        TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_doctor', 0, keep_alive = True, next_menu='lad_generic_other_guests_menu_doctor', condition = condition_saturday),
        TimedMenuChoice("You don't have anymore questions for him", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "lad")

    $ lad_generic_other_guests_menu_doctor = TimedMenu("lad_generic_other_guests_menu_doctor", [
        # During the hunt
        TimedMenuChoice('What do you think of Samuel Manning?', 'lad_generic_drunk_hunt_doctor', 10, condition = condition_saturday_hunt),
        TimedMenuChoice('What do you think of Samuel Manning?', 'lad_generic_drunk_hunt_doctor_dead', 10, condition = condition_saturday_evening),
        TimedMenuChoice('What do you think of Sushil Sinha?', 'lad_generic_captain_hunt_doctor', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of Lady Claythorn?', 'lad_generic_host_hunt_doctor', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of Rosalind Marsh?', 'lad_generic_nurse_hunt_doctor', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of Thomas Moody?', 'lad_generic_broken_hunt_doctor', 10, condition = condition_saturday),
        TimedMenuChoice('What do you think of Amelia Baxter?', 'lad_generic_psychic_hunt_doctor', 10, condition = condition_saturday),
        # Always Generic 
        TimedMenuChoice('Talk about something else', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "lad")

    #---------------------------------------------------------------------
    # NURSE
    $ nurse_generic_menu_doctor = TimedMenu("nurse_generic_menu_doctor", [
        TimedMenuChoice('What do you think of this weather?', 'nurse_generic_weather_saturday_morning', 10, condition = condition_saturday_morning),
        TimedMenuChoice('What do you think of this weather?', 'nurse_generic_weather_saturday_evening', 10, condition = condition_saturday_evening),
        TimedMenuChoice('Tell me more about yourself.', 'nurse_generic_background_doctor', 30, linked_choice = "nurse_generic_heroic_act_doctor"),
        TimedMenuChoice('Why were you invited here?', 'nurse_generic_heroic_act_doctor', 20, condition = "all_menus['nurse_generic_menu_doctor'].choices[2].hidden"),
        TimedMenuChoice('What do you think of this place?', 'nurse_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'nurse_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'nurse_generic_room', 10),
        TimedMenuChoice('What do you think of the other guests?', 'nurse_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = condition_saturday_morning, next_menu="nurse_generic_other_guests_menu_doctor"),
        TimedMenuChoice('What do you think of the other guests?', 'nurse_generic_other_guests_saturday_evening_doctor', 0, keep_alive = True, condition = condition_saturday_evening, next_menu="nurse_generic_other_guests_menu_doctor"),
        TimedMenuChoice('You don\'t have anymore questions for her', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "nurse")

    $ nurse_generic_other_guests_menu_doctor = TimedMenu("nurse_generic_other_guests_menu_doctor", [
        TimedMenuChoice('What do you think of Samuel Manning', 'nurse_generic_drunk_saturday_morning', 10, condition = condition_saturday_morning),
        TimedMenuChoice('What do you think of Lady Claythorn', 'nurse_generic_host_saturday', 10),
        TimedMenuChoice('What do you think of Amelia Baxter', 'nurse_generic_psychic_saturday_evening_doctor', 10, condition = condition_saturday_evening),
        TimedMenuChoice('I want to talk about something else.', 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "nurse")

    return