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
                text "blah blah blah" 
                
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
            Room('nurse_room',      'Sun Room',         1, (0, 100, 200, 100)),
            Room('billiard_room',   'Billiard room',    0, (0, 100, 200, 100)),
            Room('library',         'Library',          0, (200, 100, 200, 100))
            # Room('Go downstairs to visit the kitchens', 'hero_day1_evening_kitchens', 10),
            # Room('You give up and go back to your room', 'hero_day1_evening_cancel', early_exit = True)
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

                    
                    # TODO make use map_extra_info for other map too
                                        # Add extra information over map
                    if current_floor == 1:
                        text "Super duper room floor 1":
                            pos(54,200)
                            color "#be0c0c"
                            size 30
                            font "gui/font/BurtonScratch-Regular.ttf"

                    
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

# Display of manor map in menu
screen characters:
    tag menu # ????
    use game_menu(_("Characters"), scroll="viewport"):

        style_prefix "characters" #???

        #Two hbox of 4 characters
        hbox:
            vbox:
                textbutton _("The Lad") action ShowMenu("character_detail", "lad")
                imagebutton:
                    idle "images/characters/lad.png"
                    action ShowMenu("character_detail", "lad")
            
            vbox:
                xoffset 30
                textbutton _("The Captain") action ShowMenu("character_detail", "captain")
                imagebutton:
                    idle"images/characters/captain.png"
                    action ShowMenu("character_detail", "captain")  

        hbox:
            yoffset 30
            vbox:
                # Text unknow character
                if False:
                    textbutton _( "The Psychic") action ShowMenu("character_detail", "psychic")
                    imagebutton:
                        idle"images/characters/psychic.png"
                        action ShowMenu("character_detail", "psychic")  
                else:
                    textbutton _("Locked")
                    imagebutton:
                        idle"images/ui/locked_character.png"

screen character_detail(selected_char):
    tag menu # ????
    use game_menu(_("Characters"), scroll="viewport"):

        style_prefix "characters" #???

        vbox:
            text _(selected_char)

        
        # TODO show bottom right
        textbutton _("Return") action ShowMenu("characters") xalign 0.95 yalign 0.93
