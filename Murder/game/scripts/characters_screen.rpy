# Character SCREENS
screen characters:
    modal True
    tag menu

    on "show" action SetVariable("last_menu_screen", "characters")
    $ last_menu_screen = "characters"

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
        label "Select a Character":
            yoffset -50
            style "confirm_prompt" # TODO specific styling TODO space after label .... why so complicated.....
            xalign 0.5
        use character_list(True)

screen character_list(is_selection = False):
    #Two hbox of 4 characters
    $ char_x_offset = 0
    $ char_y_offset = 0

    for char_sub_list in char_list:
        hbox:
            yoffset char_y_offset
            for char in char_sub_list:
                vbox:
                    xoffset char_x_offset
                    textbutton char.real_name:
                        if is_selection:
                            if char.is_character_unlocked():
                                action Return(char.text_id)
                        else:
                            action ShowMenu("character_details", char)
                    imagebutton:
                        mouse "hover"
                        if char.is_character_unlocked():
                            idle "images/characters/side/side " + char.text_id + ".png"
                            hover "images/characters/side_hover/side " + char.text_id + " hover.png"
                        else:
                            idle "images/characters/side_bw/side " + char.text_id + " bw.png"
                            if not is_selection:
                                hover "images/characters/side_bw_hover/side " + char.text_id + " bw hover.png"

                        if is_selection:
                            if char.is_character_unlocked():
                                action Return(char.text_id)   
                        else:
                            action ShowMenu("character_details", char)
                
                $ char_x_offset += 50

        $ char_x_offset = 0

        if is_selection:
            $ char_y_offset += 340
        else:
            $ char_y_offset += 340

screen character_details(selected_char):
    # $ selected_char = get_char(char_id)
    tag menu #????
    use game_menu(_("Characters"), scroll="fixed"):

        #style_prefix "characters" #???

        hbox:
            xoffset 80
            xminimum 1600
            vbox yoffset -20:
                text selected_char.real_name:
                    size 48
                    font gui.name_text_font
                    line_leading 10
                    line_spacing 10
                    color gui.accent_color
                    # outlines [ (absolute(1), "#140303", absolute(0), absolute(0)) ]
                
                if selected_char.is_character_unlocked():
                    add "images/characters/side/side " + selected_char.text_id +".png"
                    text "Unlocked":
                        size 36
                        xalign 0.5
                else:
                    add "images/characters/side_bw/side " + selected_char.text_id +" bw.png"
                    text "Locked":
                        # yoffset -25 inside
                        size 36
                        xalign 0.5
                    bar:
                        value selected_char.get_character_progress() 
                        range 100
                        xmaximum 260
                        style 'progress_bar'

                
            vbox:     
                xoffset 50

                hbox:
                    ymaximum 600
                    viewport id "char_description_viewport":
                        draggable True 
                        mousewheel True #
                        vbox:
                            spacing 15
                            for line in selected_char.get_description_full():
                                text line:
                                    font gui.name_text_font
                            # text selected_char.get_description_full():
                            #     font gui.name_text_font
                            #     line_leading  15

                        # You can add more content here if necessary
                    vbar value YScrollValue("char_description_viewport")
                
                textbutton _("Return"): 
                    yoffset 20
                    xalign 1.0 
                    yalign 0.0
                    xpos 1350
                    action ShowMenu("characters")            
