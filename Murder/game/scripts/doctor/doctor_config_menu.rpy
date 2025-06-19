label doctor_config_menu:

    $ not_broken_offended = "not doctor_details.important_choices.is_unlocked('broken_offended') "

    #---------------------------------------------------------------------
    # BROKEN
    $ broken_generic_menu_doctor = TimedMenu("broken_generic_menu_doctor", [
        TimedMenuChoice('What do you think of this weather?', 'broken_generic_weather_friday', 10, condition = condition_friday + " and " + not_broken_offended),
        TimedMenuChoice('Tell me more about yourself.', 'broken_generic_background', 0, linked_choice ="broken_generic_heroic_act", condition = not_broken_offended),
        TimedMenuChoice('Why were you invited here?', 'broken_generic_heroic_act', 0, condition = not_broken_offended + "and all_menus[current_menu.id].choices[1].hidden"),
        TimedMenuChoice('What do you think of this place?', 'broken_generic_manor', 0, condition = not_broken_offended),
        TimedMenuChoice('How old are you?', 'broken_generic_age', 10, condition = not_broken_offended),
        TimedMenuChoice('What room are you in?', 'broken_generic_room', 0, condition = not_broken_offended),
        TimedMenuChoice('What do you think of the other guests?', 'broken_generic_other_guests_friday', 0, condition = condition_friday + " and " + not_broken_offended),
        TimedMenuChoice('You don\'t have anymore questions for him', 'generic_cancel', 0, keep_alive = True, early_exit = True, condition = not_broken_offended)
    ], image_right = "broken")

    #---------------------------------------------------------------------
    # LAD

    $ lad_generic_menu_doctor = TimedMenu("lad_generic_menu_doctor", [
        TimedMenuChoice('Tell me more about yourself.', 'lad_generic_background_doctor', 0, linked_choice ="lad_generic_heroic_act_doctor"),
        TimedMenuChoice('Why were you invited here?', 'lad_generic_heroic_act_doctor', 30, condition = "all_menus[current_menu.id].choices[0].hidden"),
        TimedMenuChoice('What do you think of this place?', 'lad_generic_manor', 10),
        TimedMenuChoice('How old are you?', 'lad_generic_age', 10),
        TimedMenuChoice('What room are you in?', 'lad_generic_room_friday', 10, condition = condition_friday),
        # TimedMenuChoice('What room are you in?', 'lad_generic_room_doctor', 10, condition = "not " + condition_friday),
        TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_friday', 10, condition = condition_friday),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
        # TimedMenuChoice('What do you think of the other guests?', 'lad_generic_other_guests_saturday_hunt', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Hunt')"),
        TimedMenuChoice("You don't have anymore questions for him", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "lad")

    return