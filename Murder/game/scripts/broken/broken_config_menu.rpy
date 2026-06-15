label broken_config_menu:

    #---------------------------------------------------------------------
    # Host
    $ host_generic_menu_broken = TimedMenu("host_generic_menu_broken", [
        TimedMenuChoice('What do you make of this weather?', 'host_generic_weather', 10),
        TimedMenuChoice('I should like to hear a little about yourself.', 'host_generic_background_broken', 20, linked_choice = "host_generic_invite_broken"),
        TimedMenuChoice('Why did you invite us here, exactly?', 'host_generic_invite_broken', 20, condition = "is_linked_choice_hidden('host_generic_menu_broken', 'host_generic_invite_broken')"),
        TimedMenuChoice('What do you think of the other guests?', 'host_generic_other_guests_broken', 10),
        TimedMenuChoice('This is a fine old house.', 'host_generic_manor', 10),
        TimedMenuChoice('Which room have you given yourself?', 'host_generic_room', 10),
        TimedMenuChoice("You don't have any more questions for her", 'generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_left = "host")

    return
