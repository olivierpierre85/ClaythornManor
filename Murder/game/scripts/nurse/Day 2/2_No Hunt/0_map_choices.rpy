label nurse_day2_no_hunt_map_menu:
    
    menu:
        "Go to the Kitchen":
            $ change_room("kitchen")
            "The staff is busy."
            jump nurse_day2_no_hunt_map_menu

        "Go to the Library":
            $ change_room("library")
            "Quiet. Perfect."
            jump nurse_day2_no_hunt_map_menu

        "Visit Thomas Moody's Room":
             $ change_room("bedroom_host")
             "The door is locked. Pity."
             jump nurse_day2_no_hunt_map_menu
        
        "Rest in your room":
            return

    return
