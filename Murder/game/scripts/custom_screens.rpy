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


screen map_menu_test(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"
                style_prefix "navigation"
                textbutton _("Where to go ?") action None

            frame:
                style "game_menu_content_frame"

                viewport:
                    xoffset -250
                    yoffset 100
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    vbox:
                        transclude
        

screen in_game_map_menu:
    style_prefix "game_menu"

    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"
                style_prefix "navigation"
                textbutton _("Where to go ?") action None

            frame:
                style "game_menu_content_frame"

                viewport:
                    xoffset -250
                    yoffset 100
                    yinitial 0.0
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    vbox:
                        transclude
            
                        imagemap:
                            idle "images/ui/map_bw.png"
                            hotspot (0, 0, 100, 100) action Return(1)
    # use map_menu_test(_("Map ofs"), scroll="viewport"):

    #     imagemap:
    #         idle "images/ui/map_bw.png"
    #         hotspot (0, 0, 100, 100) action Return(1)

# Display of manor map in menu
screen manor_map:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Map of The Manor"), scroll="viewport"):

        style_prefix "map"

        $ hovered_value = "Choose a direction"
        vbox:
            imagemap:
                idle "images/ui/map_bw.png"

            # hotspot (244, 232, 75, 73) action Return()

            text _(hovered_value)


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
