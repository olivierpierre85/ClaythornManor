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

    # TODO move to a map SCRIPT page
    $ map_info = dict()
    $ map_info['lad_room'] = False
    $ map_info['psychic_room'] = False

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

screen in_game_map_menu(choices):

    modal True

    zorder 200

    # Copy of the confirm style (TODO change later properly to a map style)
    style_prefix "confirm"

    python:
        # Logic change based on floor
        left_floor = selected_floor - 1
        right_floor = selected_floor + 1

        # Full Map of the MANOR
        rooms = [
            Room('nurse_room',      'Y Room',           2, (0, 100, 200, 100)),
            Room('lad_room',        'William the Conqueror Bedroom',           2, (200, 100, 200, 100)),
            Room('billiard_room',   'Billiard room',    1, (0, 100, 200, 100)),
            Room('library',         'Library',          1, (200, 100, 200, 100))
        ]

        # For each Room, check if the menu has a possible option for the floor
        # If there is one, add it to the map options
        hotspots = []
        for room in rooms:
            for idx, choice in enumerate(choices):
                if room.id == choice.room and room.floor == selected_floor:
                    if not choice.hidden:
                        hotspots.append(Hotspot(choice.text, idx, room.area_points))
                    # else:
                        #hotspots.append(Hotspot("No point going there? or maybe hide ?", idx, room.area_points))
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
                    
                    # for hot in hotspots:
                    for hot in hotspots:
                        hotspot (hot.area_points[0], hot.area_points[1], hot.area_points[2], hot.area_points[3]):
                            action Return(hot.position)
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
            id,
            name, 
            floor, 
            area_points, 
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
        ):
            self.description = description
            self.position = position
            self.area_points = area_points