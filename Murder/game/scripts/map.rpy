# Moving buttons for map choice menu
transform map_button_left():
    subpixel True
    yalign 0.5
    xpos 20
    zoom 1.2
    linear 0.7 xpos 0
    linear 0.7 xpos 20
    repeat

transform map_button_right():
    subpixel True
    yalign 0.5
    xpos 0
    zoom 1.2
    linear 0.7 xpos 20
    linear 0.7 xpos 0 
    repeat

label init_map:
    default tooltip = "Click on a room to move there"
    define MIN_FLOOR = 0
    define MAX_FLOOR = 3

    # TODO replace by a nice loop or class
    python:
        # Full Map of the MANOR TODO no need to init each time
        
        # all rooms
        # 'attic_hallway', 'storage', 'males_room', 'females_room', 'butler_room', 'bedrooms_hallway', 'bedroom_lad', 'bedroom_doctor', 'bedroom_captain', 'bedroom_psychic', 'bedroom_host', 'bedroom_drunk', 'bedroom_broken', 'bedroom_nurse', 'basement_stairs', 'library', 'tea_room', 'billiard_room', 'dining_room', 'garden', 'entrance_hall', 'portrait_gallery', 'kitchen', 'scullery', 'garage', 'gun_room'
        rooms = [
            # Attic
            Room(3, None,   'attic_hallway',         'Attic Hallway' ), # No area points so not a real destination
            
            Room(3, (165, 90, 270, 523),   'storage',         'Storage Room' ),
            Room(3, (512, 204, 242, 127),   'males_room',      'Male Servants Room' ), # TODO Extra livery?
            Room(3, (512, 332, 242, 129),   'females_room',     'Female Servants Room' ),
            Room(3, (512, 460, 242, 155),   'butler_room',      'Butler\'s Room' ),
            # Bedrooms
            Room(2, None,   'bedrooms_hallway',         'Bedrooms Hallway' ), # No area points so not a real destination

            Room(2, (25, 90, 205, 190),   'bedroom_lad',         'William the Conqueror Bedroom' ), # (Lad)
            Room(2, (25, 280, 205, 130),   'bedroom_doctor',      'Edward II Bedroom'), # (doctor)
            Room(2, (25, 410, 205, 100),     'bedroom_captain',     'George I Bedroom'), # (captain)
            Room(2, (25, 510, 205, 105),     'bedroom_psychic',     'Elizabeth I Bedroom'), # (Psychic)
            
            Room(2, (717, 90, 178, 190),   'bedroom_host',        'Henry IV Bedroom'), #  (Host)
            Room(2, (717, 280, 178, 130),   'bedroom_drunk',       'George IV Bedroom'), #  (drunk)
            Room(2, (717, 410, 178, 100),   'bedroom_broken',      'Richard III Bedroom'), #  (broken)
            Room(2, (717, 510, 178, 105),   'bedroom_nurse',       'Queen Alexandra'), # (nurse)
            
            # Room(2, (256 , 90, 434, 115),     'servant_stairs_2',          'Servant Stairs'), 
            # Ground Floor
            Room(1, None,     'basement_stairs',          'Basement Stairs'),

            Room(1, (25, 397, 230, 218),   'library',          'Library'),
            Room(1, (25, 90, 230, 305),   'tea_room',         'Tea room'),
            Room(1, (691, 90, 205, 204),     'billiard_room',    'Billiard room'),
            Room(1, (691, 295, 205, 319),   'dining_room',      'Dining Room'),
            Room(1, (360, 552, 203, 60),     'manor_garden',           'Garden'),
            Room(1, (256, 293, 435, 260),     'entrance_hall',           'Entrance Hall'),
            Room(1, (256 , 90, 435, 105),     'servant_stairs',          'Servant Stairs'),
            Room(1, (256 , 195, 435, 100),     'portrait_gallery',          'Portrait Gallery'),
            # Basement
            Room(0, (25, 205, 360, 407),     'kitchen',          'Kitchen'),
            Room(0, (25, 90, 360, 118),   'scullery',         'Scullery'),
            Room(0, (691, 90, 206, 525),   'garage',           'Garage'),
            Room(0, (385, 333, 306, 280),     'gun_room',         'Gun room'), #TODO check in basement geniric?
            Room(0, (0, 0, 0, 0),     'black_background',         'Darkness'), # used or effect
        ]
        # TODO put in the ROOM class????? NOT if multiple info by room? Check at the end
        y_map_info_offset = 60
        x_map_info_offset = 10
        map_information = [
            MapInfo('bedroom_psychic', 'Amelia Baxter',    2, (25 + x_map_info_offset, 510 + y_map_info_offset, 205, 105)),
            MapInfo('bedroom_lad',     'Ted Harring',      2, (25 + x_map_info_offset, 90 + 100, 205, 190)),
            MapInfo('bedroom_broken',  'Thomas Moody',     2, (717 + x_map_info_offset, 410 + y_map_info_offset, 178, 100)),
            MapInfo('bedroom_host',    'Lady Claythorn',   2, (717 + x_map_info_offset, 90 + 100 , 178, 190)),
            MapInfo('bedroom_captain', 'Sushil Sinha',     2, (25 + x_map_info_offset, 410 + y_map_info_offset, 205, 100)),
            MapInfo('bedroom_doctor',  'Daniel Baldwin',   2, (25 + x_map_info_offset, 280 + y_map_info_offset, 205, 130)),
            MapInfo('bedroom_drunk',  'Samuel Manning',   2, (717 + x_map_info_offset, 280 + y_map_info_offset, 178, 130)),
            MapInfo('bedroom_nurse',  'Rosalind Marsh',   2, (717 + x_map_info_offset, 510 + y_map_info_offset, 178, 105)),
            
            MapInfo('bedroom_footman',  'Andrew',   3, (575 + x_map_info_offset, 200 + y_map_info_offset, 178, 105)),
        ]

    call change_floor(1) # ground floor

    return

init python:
    
    def unlock_map(room):
        global seen_tutorial_map
        for info in map_information:
            if info.id == room and not info.active:
                info.active = True
                if not hide_notifications:
                    renpy.notify("You have written new information on the map.")
                    renpy.play("audio/sound_effects/writing_short.ogg", "sound")

        if not seen_tutorial_map:
            seen_tutorial_map = True
            renpy.call('tutorial_map')
        return

    def is_unlock_map(room):
        for info in map_information:
            if info.id == room:
                return info.active

        return False

label change_floor(floor):
    # 0 = basement
    # 1 = Ground Floor
    # 2 = Bedrooms
    # 3 = Attic /..???? 
    $ current_floor = floor
    $ selected_floor = floor 

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
            yoffset 130
            xoffset -120
            if selected_floor > MIN_FLOOR:
                imagebutton:
                    mouse "hover"
                    idle "gui/button/page_button_left_idle_bright.png" 
                    hover "gui/button/page_button_left_hover.png" 
                    yalign 0.5 
                    xoffset 0                     
                    action SetVariable("selected_floor", left_floor) at map_button_left
            else:
                add Solid("#00000000", xsize=168, ysize=90) xpos 0 yalign 0.5
                # imagebutton:
                #     mouse "hover"
                #     idle "gui/button/page_button_left_idle.png" 
                #     yalign 0.5 
                #     xoffset 0                     
            
            imagemap: 
                xalign 0.5                       
                idle "images/ui/map/map_idle_[selected_floor].png"
                hover "images/ui/map/map_hover_[selected_floor].png"
                use map_information
                
            if selected_floor < MAX_FLOOR:
                imagebutton:
                    mouse "hover"
                    idle "gui/button/page_button_right_idle_bright.png" 
                    hover "gui/button/page_button_right_hover.png" 
                    yalign 0.5 
                    xoffset 0                     
                    action SetVariable("selected_floor", right_floor) at map_button_right
            else:
                add Solid("#00000000", xsize=168, ysize=90) xpos 0 yalign 0.5
                # imagebutton:
                #     mouse "hover"
                #     idle "gui/button/page_button_right_idle.png" 
                #     yalign 0.5 
                #     xoffset 0       

screen map_information:

    for info in map_information:
        if info.floor == selected_floor and info.active:
                text info.name:
                    pos info.area_points
                    size 16
                    color gui.map_writing_color                    
                    font gui.map_writing_font

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
        ALREADY_TRIED_CHOICE = " (I already went there)" 
        
        hotspots = []

        for room in rooms:
            if room.floor != selected_floor:
                continue

            new_hotspot     = None        # what we will eventually append
            first_choice_ix = None        # remembered for the fallback case

            for ix, choice in enumerate(choices):
                if choice.room != room.id:
                    continue               # not a choice for this room

                # keep the index of *any* choice for the fallback
                if first_choice_ix is None:
                    first_choice_ix = ix

                # ---------- normal, “active” branch ----------
                if choice.get_condition():
                    label      = choice.text if not choice.hidden else ALREADY_TRIED_CHOICE
                    is_active  = not choice.hidden

                    new_hotspot = Hotspot(label, ix, room.area_points, room.id,active=is_active)

                    if choice.is_already_chosen():
                        new_hotspot.description += "*"

                    break                  # we found a usable choice → stop scanning MAKE sure there is only 1 choice possible at a time


            # ---------- no usable choice found ----------
            if new_hotspot is None:
                # treat the whole thing as “already tried”
                # (first_choice_ix is guaranteed to exist because every room has ≥1 choice)
                new_hotspot = Hotspot(ALREADY_TRIED_CHOICE,first_choice_ix,room.area_points, room.id,active=False)     # greyed-out / inactive
                # if you also want to flag the underlying Choice object as “used”
                # you can do it here:
                # choices[first_choice_ix].hidden = True

            hotspots.append(new_hotspot)
                        

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label "Where do you want to go?":
                style "confirm_prompt" # TODO specific styling
                text_size 46
                xalign 0.5


            # use show_map # TODO problem with hot var in tooltip not working, so instead we need to duplicate code
            hbox:
                if selected_floor > MIN_FLOOR:
                    imagebutton:
                        mouse "hover"
                        idle "gui/button/page_button_left_idle_bright.png" 
                        hover "gui/button/page_button_left_hover.png" 
                        yalign 0.5 
                        xoffset 0                     
                        action SetVariable("selected_floor", left_floor) at map_button_left
                else:
                    add Solid("#00000000", xsize=168, ysize=90) xpos 0 yalign 0.5
                    # imagebutton:
                    #     mouse "hover"
                    #     idle "gui/button/page_button_left_idle.png" 
                    #     yalign 0.5 
                    #     xoffset 0                     
                
                imagemap: 
                    xalign 0.5                       
                    idle "images/ui/map/map_idle_[selected_floor].png"
                    hover "images/ui/map/map_hover_[selected_floor].png"
                    insensitive "images/ui/map/map_insensitive_[selected_floor].png"
                    
                    for hot in hotspots:
                        if hot.area_points:
                            hotspot (hot.area_points[0], hot.area_points[1], hot.area_points[2], hot.area_points[3]):
                                if hot.active:
                                    if '*' in hot.description and not seen_tutorial_already_chosen_map: 
                                        action [ SetVariable("show_tutorial_already_chosen_map", True), Return(hot.room) ]
                                    else:
                                        action Return(hot.room)
                                else:
                                    action None
                                tooltip hot.description
                                mouse "hover"

                    use map_information
                    
                if selected_floor < MAX_FLOOR:
                    imagebutton:
                        mouse "hover"
                        idle "gui/button/page_button_right_idle_bright.png" 
                        hover "gui/button/page_button_right_hover.png" 
                        yalign 0.5 
                        xoffset 0                     
                        action SetVariable("selected_floor", right_floor) at map_button_right
                else:
                    add Solid("#00000000", xsize=168, ysize=90) xpos 0 yalign 0.5
                    # imagebutton:
                    #     mouse "hover"
                    #     idle "gui/button/page_button_right_idle.png" 
                    #     yalign 0.5 
                    #     xoffset 0       

            $ tooltip = GetTooltip()
            if not tooltip:
                $ tooltip = "Click on a room to move there"
            
            # Used the * to show the choices already made, then remove the * 
            
            label [tooltip.replace('*', '')]:
                yoffset -10
                if "*" in tooltip:
                    text_color gui.accent_color
                else:
                    text_color gui.highlight_color
                text_size 46
                xalign 0.5

# Python classes
init -1 python:
    def default_room_text(room_id):
        for room in rooms:
            if room.id == room_id:
                # TODO if map unlock, show the name of the person, not the name of the room
                return room.name
        return "-"

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
    
    class MapInfo:
        def __init__(
            self, 
            id,
            name,
            floor, 
            area_points,
            active = False
        ):
            self.id = id
            self.name = name
            self.floor = floor
            self.area_points = area_points
            self.active = active

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