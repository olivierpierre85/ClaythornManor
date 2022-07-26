screen current_time:
    zorder 1
    modal False

    text "[current_time], [current_day]"

screen in_game_menu_btn:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "images/ui/menu_btn.png"
        action ShowMenu("in_game_menu")



screen in_game_menu:
    zorder 2
    modal False

    text "MENU TODO  sous menu"

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "images/ui/back_btn.png"
        action Return()

# Display of manor map in menu
screen manor_map:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Map of The Manor"), scroll="viewport"):

        style_prefix "map"

        vbox:
            text _("Tea room")

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

        hbox:
            imagebutton:
                idle "images/ui/lad_btn.png"
                action ShowMenu("character_detail", "lad")

            imagebutton:
                xoffset 30
                idle "images/ui/captain_btn.png"
                action ShowMenu("character_detail", "captain")
        
        hbox:
            yoffset 50
            imagebutton:
                idle "images/ui/lad_btn.png"
                action ShowMenu("character_detail", "lad")

            imagebutton:
                xoffset 30
                idle "images/ui/captain_btn.png"
                action ShowMenu("character_detail", "captain")

screen character_detail(selected_char):
    tag menu # ????
    use game_menu(_("Characters"), scroll="viewport"):

        style_prefix "characters" #???

        vbox:
            text _(selected_char)

        
        # TODO show bottom right
        textbutton _("Return") action ShowMenu("characters") xalign 0.95 yalign 0.93
