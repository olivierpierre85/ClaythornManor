label nurse_day3_morning_map_menu:
    
    menu:
        "Check Samuel Manning's Room":
            $ change_room("bedroom_drunk")
            "Dead. Alcohol poisoning... or so it seems."
            jump nurse_day3_morning_map_menu

        "Check Thomas Moody's Room":
             $ change_room("bedroom_host")
             "Dead. It looks like a heart attack."
             jump nurse_day3_morning_map_menu

        "Check Dr. Arbuthnot's Room":
            $ change_room("bedroom_doctor")
            "Also dead. This is... an epidemic."
            jump nurse_day3_morning_map_menu
        
        "Go to the Tea Room (Finish Search)":
            return

    return
