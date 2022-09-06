screen current_time:
    zorder 1
    modal False

    text "[current_time], [current_day]"

screen in_game_menu_btn:
    # TODO Menu button
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "images/ui/menu_btn.png"
        action ShowMenu("in_game_map_menu")
        

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

screen in_game_map_menu:
    modal True

    zorder 200

    # Copy of the confirm style (TODO change later properly)
    style_prefix "confirm"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            hbox:
                imagebutton:
                    idle "gui/button/page_button_left_idle.png" 
                    hover "gui/button/page_button_left_hover.png" 
                    yalign 0.5 
                    xoffset 0 
                    action Return(3) # TODO call back with parameter for different FLOOR
                    at map_button_left

                
                imagemap: 
                    xalign 0.5                       
                    idle "images/ui/map_bw.png"
                    hover "images/ui/map_bw_hover.png"
                    hotspot (29, 95, 255, 502):
                        action Return(0)
                        tooltip "Go to the scullery ?" 
                    hotspot (288, 95, 300, 100) action Return(1)
                
                imagebutton:
                    idle "gui/button/page_button_right_idle.png" 
                    hover "gui/button/page_button_right_hover.png" 
                    yalign 0.5 
                    xoffset 0 
                    action Return(3) # TODO call back with parameter for different FLOOR
                    at map_button_right
            
            $ tooltip = GetTooltip()
            if not tooltip:
                $ tooltip = "Where do you want to go ?"
            label [tooltip]:
                xalign 0.5

# Display of manor map in menu ? Really needed???
screen manor_map:
    tag menu


    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Map of The Manor")):

        style_prefix "map"

        $ hovered_value = "Choose a direction"
        
        vbox:
            imagemap:
                yoffset 150
                idle "images/ui/map_bw.png"
                hover "gui/overlay/history_overlay.png"

            # hotspot (244, 232, 75, 73) action Return()

            text _(hovered_value):
                xalign 0.5
        


# Display of storyline tree
screen storyline:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Storyline"), scroll="viewport"):

        style_prefix "map"

        vbox:
            text _("story tree")

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
