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
    define MIN_FLOOR = 0
    define MAX_FLOOR = 3

    # TODO replace by a nice loop or class
    python:
        # Full Map of the MANOR TODO no need to init each time
        
        # all rooms
        # 'attic_hallway', 'storage', 'males_room', 'females_room', 'attic_butler_room', 'bedrooms_hallway', 'bedroom_lad', 'bedroom_doctor', 'bedroom_captain', 'bedroom_psychic', 'bedroom_host', 'bedroom_drunk', 'bedroom_broken', 'bedroom_nurse', 'basement_stairs', 'library', 'tea_room', 'billiard_room', 'dining_room', 'garden', 'entrance_hall', 'portrait_gallery', 'kitchen', 'scullery', 'garage', 'gun_room'
        rooms = [
            # Attic
            Room(3, None,   'attic_hallway',         'Attic Hallway' ), # No area points so not a real destination
            
            Room(3, (165, 90, 270, 523),   'storage',         'Storage Room' ),
            Room(3, (512, 204, 242, 127),   'males_room',      'Male Servants Room' ), # TODO Extra livery?
            Room(3, (512, 332, 242, 129),   'females_room',     'Female Servants Room' ),
            Room(3, (512, 460, 242, 155),   'attic_butler_room',      'Butler\'s Room' ),
            # Bedrooms
            Room(2, None,   'bedrooms_hallway',         'Bedrooms Hallway' ), # No area points so not a real destination

            Room(2, (25, 90, 205, 190),   'bedroom_lad',         'William the Conqueror Bedroom' ), # (Lad)
            Room(2, (25, 280, 205, 130),   'bedroom_doctor',      'Edward II Bedroom'), # (doctor)
            Room(2, (25, 410, 205, 100),     'bedroom_captain',     'George I Bedroom'), # (captain)
            Room(2, (25, 510, 205, 105),     'bedroom_psychic',     'Elizabeth I Bedroom'), # (Psychic)
            
            Room(2, (717, 90, 178, 190),   'bedroom_host',        'Henry IV Bedroom'), #  (Host)
            Room(2, (717, 280, 178, 130),   'bedroom_drunk',       'George IV Bedroom'), #  (drunk)
            Room(2, (717, 410, 178, 100),   'bedroom_broken',      'Richard III Bedroom'), #  (broken)
            Room(2, (717, 510, 178, 105),   'bedroom_nurse',       'Queen Alexandra Bedroom'), # (nurse)
            
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


# One arrow button for changing floors on the map screens. direction is -1
# (left, down a floor) or +1 (right, up a floor). When there is no further
# floor, a transparent spacer of the same size keeps the imagemap centred.
screen map_floor_arrow(direction):

    $ arrow_target = selected_floor + direction
    # arrow_side is screen-local, so it cannot be used in [bracket] image
    # interpolation (that resolves against the global store) - build the
    # full paths here instead.
    $ arrow_side = "left" if direction < 0 else "right"

    if MIN_FLOOR <= arrow_target and arrow_target <= MAX_FLOOR:
        imagebutton:
            mouse "hover"
            idle "gui/button/page_button_{}_idle_bright.png".format(arrow_side)
            hover "gui/button/page_button_{}_hover.png".format(arrow_side)
            yalign 0.5
            xoffset 0
            action SetVariable("selected_floor", arrow_target) at (map_button_left if direction < 0 else map_button_right)
    else:
        add Solid("#00000000", xsize=168, ysize=90) xpos 0 yalign 0.5


# Display of manor map in menu => Make it more like
screen manor_map:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Map of The Manor")):

        hbox:
            yoffset 130
            xoffset -120

            use map_floor_arrow(-1)

            imagemap:
                xalign 0.5
                idle "images/ui/map/map_idle_[selected_floor].png"
                hover "images/ui/map/map_hover_[selected_floor].png"
                use map_annotations

            use map_floor_arrow(1)


# The names the player has written on the map (unlocked via unlock_map)
screen map_annotations:

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
        ALREADY_TRIED_CHOICE = " (I already went there)"

        hotspots = []

        for room in rooms:
            if room.floor != selected_floor or not room.area_points:
                continue

            # Same matching rule as display_choices, so the room shown and
            # the choice executed always agree.
            choice = find_choice_for_room(timed_menu, room.id)

            if choice is not None:
                label = choice.text if not choice.hidden else ALREADY_TRIED_CHOICE
                new_hotspot = Hotspot(label, room.area_points, room.id, active=not choice.hidden)
                new_hotspot.already_chosen = choice.is_already_chosen()
            else:
                # No usable choice for this room - grey it out as already tried
                new_hotspot = Hotspot(ALREADY_TRIED_CHOICE, room.area_points, room.id, active=False)

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

            hbox:
                use map_floor_arrow(-1)

                imagemap:
                    xalign 0.5
                    idle "images/ui/map/map_idle_[selected_floor].png"
                    hover "images/ui/map/map_hover_[selected_floor].png"
                    insensitive "images/ui/map/map_insensitive_[selected_floor].png"

                    for hot in hotspots:
                        hotspot (hot.area_points[0], hot.area_points[1], hot.area_points[2], hot.area_points[3]):
                            if hot.active:
                                if hot.already_chosen and not seen_tutorial_already_chosen_map:
                                    action [ SetVariable("show_tutorial_already_chosen_map", True), Return(hot.room) ]
                                else:
                                    action Return(hot.room)
                            else:
                                action None
                            tooltip hot
                            mouse "hover"

                    use map_annotations

                use map_floor_arrow(1)

            # The hovered hotspot (if any) drives the caption under the map
            $ hovered_hotspot = GetTooltip()
            if hovered_hotspot:
                label hovered_hotspot.description:
                    yoffset -10
                    if hovered_hotspot.already_chosen:
                        text_color gui.accent_color
                    else:
                        text_color gui.highlight_color
                    text_size 46
                    xalign 0.5
            else:
                label "Click on a room to move there":
                    yoffset -10
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

    def map_choice(room, redirect, time_spent=10, **kwargs):
        """
        Shorthand for a map menu entry: the visible text is the room's
        default name and the room id doubles as the hotspot key. Any extra
        TimedMenuChoice argument (condition, early_exit, ...) passes through.
        """
        return TimedMenuChoice(default_room_text(room), redirect, time_spent, room=room, **kwargs)

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
            area_points,
            room,
            active = True,
            already_chosen = False
        ):
            self.description = description
            self.area_points = area_points
            self.room = room
            self.active = active
            self.already_chosen = already_chosen

        # in_game_map_menu rebuilds a fresh hotspots list (fresh Hotspot
        # instances) on every screen redraw. Ren'Py's tooltip tracking
        # compares the old and new tooltip value to decide whether to call
        # renpy.restart_interaction() - without this, two instances
        # describing the same room are never equal, so every redraw looks
        # like a tooltip change and the game restarts the interaction
        # forever (100-restart safety abort) as soon as the mouse rests on
        # a hotspot.
        def __eq__(self, other):
            if not isinstance(other, Hotspot):
                return NotImplemented
            return (self.room, self.description, self.active, self.already_chosen) == (
                other.room, other.description, other.active, other.already_chosen)

        def __hash__(self):
            return hash((self.room, self.description, self.active, self.already_chosen))