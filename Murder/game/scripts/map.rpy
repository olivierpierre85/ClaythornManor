# Moving buttons for map choice menu
transform map_button_left():
    subpixel True
    yalign 0.5
    xpos 15
    linear 1.0 xpos 0
    linear 1.0 xpos 15
    repeat

transform map_button_right():
    subpixel True
    yalign 0.5
    xpos 0
    linear 1.0 xpos 15
    linear 1.0 xpos 0
    repeat

label init_map:
    define tooltip = "Click on a room to move there"
    define MIN_FLOOR = 0
    define MAX_FLOOR = 2 # TODO Add floors

    # TODO replace by a nice loop or class
    python:
        # Full Map of the MANOR
        rooms = [
            # Bedrooms
            Room(2, (0, 100, 200, 100),     'psychic_room',     'George III Bedroom'),
            Room(2, (200, 100, 200, 100),   'lad_room',         'William the Conqueror Bedroom'),
            Room(2, (400, 100, 200, 100),   'host_room',        'Richard III Bedroom'),
            # Ground Floor
            Room(1, (0, 100, 200, 100),     'billiard_room',    'Billiard room'),
            Room(1, (200, 100, 200, 100),   'library',          'Library'),
            # Basement
            Room(0, (0, 100, 200, 100),   'kitchen',          'Kitchen'),
            Room(0, (200, 100, 200, 100),   'scullery',         'Scullery'),
            Room(0, (400, 100, 200, 100),   'garage',           'Garage'),
        ]
        # Info locked TODO put in the ROOM class?????
        map_info = dict()
        map_info['lad_room'] = False
        map_info['psychic_room'] = False

    call change_floor(1) # ground floor

    return

label change_floor(floor):
    # 0 = basement
    # 1 = Ground Floor
    # 2 = Bedrooms
    # 3 = Attic /..???? 
    $ current_floor = floor
    $ selected_floor = floor 

    return

label unlock_map(room):
    python:
        if not map_info[room]:
            map_info[room] = True
            renpy.notify("You have written new information on the map.")
            renpy.play("audio/sound_effects/writing_short.ogg", "sound")

    return


# Display of manor map in menu => Make it more like
screen manor_map:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Map of The Manor")):

        # Copy of in_game_map_menu because problem with var when use in sub screen
        $ left_floor = selected_floor - 1
        $ right_floor = selected_floor + 1
        hbox:
            yoffset 120
            xoffset -175
            if selected_floor > MIN_FLOOR:
                imagebutton:
                    idle "gui/button/page_button_left_idle.png" 
                    hover "gui/button/page_button_left_hover.png" 
                    yalign 0.5 
                    xoffset 0                     
                    action SetVariable("selected_floor", left_floor) at map_button_left
            else:
                imagebutton:
                    idle "gui/button/page_button_left_idle.png" 
                    yalign 0.5 
                    xoffset 0                     
            
            imagemap: 
                xalign 0.5                       
                idle "images/ui/map_bw_idle_[selected_floor].png"
                hover "images/ui/map_bw_hover_[selected_floor].png"
                use map_information
                
            if selected_floor < MAX_FLOOR:
                imagebutton:
                    idle "gui/button/page_button_right_idle.png" 
                    hover "gui/button/page_button_right_hover.png" 
                    yalign 0.5 
                    xoffset 0                     
                    action SetVariable("selected_floor", right_floor) at map_button_right
            else:
                imagebutton:
                    idle "gui/button/page_button_right_idle.png" 
                    yalign 0.5 
                    xoffset 0       

screen map_information:
    if selected_floor == 2:
        if map_info['lad_room'] == True:
            text "Ted Harring":
                pos(200,100)
                color "#be0c0c"
                size 30
                font "gui/font/BurtonScratch-Regular.ttf"
        
        if map_info['psychic_room'] == True:
            text "Psychic room":
                pos(0,100)
                color "#be0c0c"
                size 30
                font "gui/font/BurtonScratch-Regular.ttf"

screen in_game_map_menu(timed_menu):

    modal True

    zorder 200

    # Copy of the confirm style (TODO change later properly to a map style)
    style_prefix "confirm"

    python:
        choices = timed_menu.choices
        # Logic change based on floor
        left_floor = selected_floor - 1
        right_floor = selected_floor + 1

        
        # TODO fix or remove.NOT VISIBLE at the moment, because inactive hotspot are invisible????
        ALREADY_TRIED_CHOICE = "I already went there." 

        hotspots = []
        for room in rooms:
            if room.floor == selected_floor:
                new_hotspot = None
                # TODO check if idx still needed ?
                for idx, choice in enumerate(choices): 
                    if room.id == choice.room:
                        if not choice.hidden:
                            new_hotspot = Hotspot(choice.text, idx, room.area_points, room.id)
                        else:
                            new_hotspot = Hotspot(ALREADY_TRIED_CHOICE, idx, room.area_points, room.id, active = False)
                
                # When the room is not in the menu, default values applies
                if not new_hotspot:
                    if room.id in timed_menu.default_visited:
                        new_hotspot = Hotspot(ALREADY_TRIED_CHOICE, idx, room.area_points, room.id, active = False)
                    else:
                        new_hotspot = Hotspot(room.name, idx, room.area_points, room.id, active = True)

                hotspots.append(new_hotspot)
                        

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45


            label "Where do you want to go ?":
                style "confirm_prompt" # TODO specific styling
                xalign 0.5


            # use show_map # TODO problem with hot var in tooltip not working, so we need to duplicate code
            hbox:
                if selected_floor > MIN_FLOOR:
                    imagebutton:
                        idle "gui/button/page_button_left_idle.png" 
                        hover "gui/button/page_button_left_hover.png" 
                        yalign 0.5 
                        xoffset 0                     
                        action SetVariable("selected_floor", left_floor) at map_button_left
                else:
                    imagebutton:
                        idle "gui/button/page_button_left_idle.png" 
                        yalign 0.5 
                        xoffset 0                     
                
                imagemap: 
                    xalign 0.5                       
                    idle "images/ui/map_bw_idle_[selected_floor].png"
                    hover "images/ui/map_bw_hover_[selected_floor].png"
                    
                    for hot in hotspots:
                        hotspot (hot.area_points[0], hot.area_points[1], hot.area_points[2], hot.area_points[3]):
                            if hot.active:
                                action Return(hot.room)
                            else:
                                action None
                            tooltip hot.description

                    use map_information
                    
                if selected_floor < MAX_FLOOR:
                    imagebutton:
                        idle "gui/button/page_button_right_idle.png" 
                        hover "gui/button/page_button_right_hover.png" 
                        yalign 0.5 
                        xoffset 0                     
                        action SetVariable("selected_floor", right_floor) at map_button_right
                else:
                    imagebutton:
                        idle "gui/button/page_button_right_idle.png" 
                        yalign 0.5 
                        xoffset 0       

            $ tooltip = GetTooltip()
            if not tooltip:
                $ tooltip = "Click on a room to move there"
            label [tooltip]:
                xalign 0.5

# Python classes
init -1 python:
    class Room:
        def __init__(
            self, 
            floor, 
            area_points, 
            id,
            name
        ):
            self.id = id
            self.name = name
            self.floor = floor
            self.area_points = area_points
    
    class Hotspot:
        def __init__(
            self, 
            description, 
            position,
            area_points, 
            room,
            active = True
        ):
            self.description = description
            self.position = position
            self.area_points = area_points
            self.room = room
            self.active = active