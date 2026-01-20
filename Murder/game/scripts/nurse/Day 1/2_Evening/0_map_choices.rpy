label nurse_day1_evening_map_menu:
    
    menu:
        "Go to your room":
            $ change_room("bedroom_nurse")
            "I need to rest for a moment."
            jump nurse_day1_evening_map_menu

        "Go to the Kitchen":
             $ change_room("kitchen")
             "The staff is busy preparing dinner. Best not to disturb them."
             jump nurse_day1_evening_map_menu

        "Go to the Library" if not library_visited:
            $ change_room("library")
            "A fine collection of books."
            $ library_visited = True
            jump nurse_day1_evening_map_menu

        "Go to the Billiard Room" if not day1_evening_billiard_room_visited:
            $ change_room("billiard_room")
            "Empty. The baize looks pristine."
            $ day1_evening_billiard_room_visited = True
            jump nurse_day1_evening_map_menu
        
        "Finish looking around":
            return

    return
