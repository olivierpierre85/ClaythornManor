screen current_time:
    modal False

    $ current_hour = current_time.hour
    $ current_minutes = current_time.minute
    if current_hour >= 12:
        $ current_period = "Afternoon"
        $ current_hour = current_hour - 12
    else:
        $ current_period = "Morning"


    $ hours_angle = ((int(current_hour) * 60) + int(current_minutes))/2
    
    $ minutes_angle = int(current_minutes) * 6
    # Terrible quickfix to force clockwise rotation... (constant) TODO  replace???
    python:
        while old_minutes_angle > minutes_angle:
            minutes_angle = minutes_angle + 360

    add "images/ui/day_background.png"

    text "[current_day] [current_period], [minutes_angle]" xoffset 20

    imagebutton:
        xoffset 30
        yoffset 50
        idle "images/ui/clock_small.png" 

    add "images/ui/clock_hours.png" at rotate_hours(hours_angle)
    add "images/ui/clock_minutes.png" at rotate_minutes(minutes_angle)

    $ old_minutes_angle = minutes_angle
        
transform rotate_hours( angle = 0 ):
    xoffset -16
    yoffset 31
    linear 3.0 rotate angle 

transform rotate_minutes( angle = 0 ):
    xoffset -16
    yoffset 31 
    linear 3.0 rotate angle 

screen in_game_menu_btn:

    style_prefix "confirm" # TODO use own style
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        ypadding 10

        textbutton _("Menu") action ShowMenu("manor_map")
        

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

# Display of manor map in menu => Make it more like
screen manor_map:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Map of The Manor")):

        # Copy of in_game_map_menu because problem with var when use in sub screen
        $ left_floor = current_floor - 1
        $ right_floor = current_floor + 1
        hbox:
            yoffset 120
            xoffset -175
            if current_floor > MIN_FLOOR:
                imagebutton:
                    idle "gui/button/page_button_left_idle.png" 
                    hover "gui/button/page_button_left_hover.png" 
                    yalign 0.5 
                    xoffset 0                     
                    action SetVariable("current_floor", left_floor) at map_button_left
            else:
                imagebutton:
                    idle "gui/button/page_button_left_idle.png" 
                    yalign 0.5 
                    xoffset 0                     
            
            imagemap: 
                xalign 0.5                       
                idle "images/ui/map_bw_idle_[current_floor].png"
                hover "images/ui/map_bw_hover_[current_floor].png"
                use map_information
                
            if current_floor < MAX_FLOOR:
                imagebutton:
                    idle "gui/button/page_button_right_idle.png" 
                    hover "gui/button/page_button_right_hover.png" 
                    yalign 0.5 
                    xoffset 0                     
                    action SetVariable("current_floor", right_floor) at map_button_right
            else:
                imagebutton:
                    idle "gui/button/page_button_right_idle.png" 
                    yalign 0.5 
                    xoffset 0       

screen map_information:
    if current_floor == 1:
        if map_info['hero_room'] == True:
            text "Hero room room floor 1":
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
        left_floor = current_floor - 1
        right_floor = current_floor + 1

        # Full Map of the MANOR
        rooms = [
            Room('nurse_room',      'Y Room',           1, (0, 100, 200, 100)),
            Room('hero_room',       'X ROOM',           1, (200, 100, 200, 100)),

            Room('billiard_room',   'Billiard room',    0, (0, 100, 200, 100)),
            Room('library',         'Library',          0, (200, 100, 200, 100))
        ]

        # For each Room, check if the menu has a possible option for the floor
        # If there is one, add it to the map options
        hotspots = []
        for room in rooms:
            for idx, choice in enumerate(choices):
                if room.id == choice.room and room.floor == current_floor:
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
                if current_floor > MIN_FLOOR:
                    imagebutton:
                        idle "gui/button/page_button_left_idle.png" 
                        hover "gui/button/page_button_left_hover.png" 
                        yalign 0.5 
                        xoffset 0                     
                        action SetVariable("current_floor", left_floor) at map_button_left
                else:
                    imagebutton:
                        idle "gui/button/page_button_left_idle.png" 
                        yalign 0.5 
                        xoffset 0                     
                
                imagemap: 
                    xalign 0.5                       
                    idle "images/ui/map_bw_idle_[current_floor].png"
                    hover "images/ui/map_bw_hover_[current_floor].png"
                    
                    # for hot in hotspots:
                    for hot in hotspots:
                        hotspot (hot.area_points[0], hot.area_points[1], hot.area_points[2], hot.area_points[3]):
                            action Return(hot.position)
                            tooltip hot.description

                    use map_information
                    
                if current_floor < MAX_FLOOR:
                    imagebutton:
                        idle "gui/button/page_button_right_idle.png" 
                        hover "gui/button/page_button_right_hover.png" 
                        yalign 0.5 
                        xoffset 0                     
                        action SetVariable("current_floor", right_floor) at map_button_right
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


# Display of storyline tree
screen objects:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Objects"), scroll="viewport"):

        style_prefix "object"

        vbox:
            text _("TODO imagemap with all objects, explanation on hover?")

# Display of storyline tree
screen storyline:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Storyline"), scroll="viewport"):

        style_prefix "map"

        vbox:
            text _("TODO story tree (One image map by user, possibility to change user with small button face")

screen characters:
    tag menu
    use game_menu(_("Characters")):
        fixed:
            xalign 0.5
            yoffset 120
            xoffset -100

            use character_list

screen character_selection:
    modal True
    zorder 200

    # Copy of the confirm style (TODO change later properly to a map style)
    style_prefix "confirm"
    
    frame:
        xalign .5
        yalign .5
        margin (310,110,310,150)
        label "With whom will you start the adventure again ?":
            yoffset -50
            style "confirm_prompt" # TODO specific styling TODO space after label .... why so complicated.....
            xalign 0.5
        use character_list(True)

screen character_list(is_selection = False):
    #Two hbox of 4 characters
    python:
        #TODO Move to somewhere else? Take from Character class?
        char_list = [
            [("The Lad", "lad"), ("The Psychic", "psychic"), ("The Captain", "captain"), ("The Broken Face", "broken")],
            [("The Doctor", "doctor"), ("The Drunk", "drunk"), ("The Host", "host"), ("The Nurse", "nurse")]
        ]
        char_x_offset = 0
        char_y_offset = 0

    for char_sub_list in char_list:
        hbox:
            yoffset char_y_offset
            for char in char_sub_list:
                vbox:
                    xoffset char_x_offset
                    textbutton char[0]:
                        if is_selection:
                            action Return(char[1])
                        else:
                            action ShowMenu("character_detail", char[1])
                    imagebutton:
                        idle "images/characters/" + char[1] +".png"
                        if is_selection:
                            action Return(char[1])
                        else:
                            action ShowMenu("character_detail", char[1])
                $ char_x_offset += 50

        $ char_x_offset = 0

        if is_selection:
            $ char_y_offset += 340
        else:
            $ char_y_offset += 340

screen character_detail(selected_char):
    tag menu # ????
    use game_menu(_("Characters"), scroll="viewport"):

        style_prefix "characters" #???

        vbox:
            text _(selected_char)

        
        # TODO show bottom right
        textbutton _("Return") action ShowMenu("characters") xalign 0.95 yalign 0.93
