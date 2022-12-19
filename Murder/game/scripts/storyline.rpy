label init_storylines:
    $ current_storyline = "lad"
    return

transform character_storyline:
    zoom 0.4

# Display of storyline tree
screen storyline:
    tag menu

    
    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Storyline"), scroll="fixed"):

        hbox:
            spacing 10
            vbox:
                xminimum 1400
                xalign 0.5
                # Character choice
                hbox:
                    xalign 0.5
                    spacing 20
                    for char in char_list_flat:
                        imagebutton:
                            if char.text_id == current_storyline:
                                idle "images/characters/side/side " + char.text_id +".png" at character_storyline
                            else:
                                idle "images/characters/side_bw/side " + char.text_id +" bw.png" at character_storyline
                                hover "images/characters/side/side " + char.text_id + ".png"
                            
                            action SetVariable("current_storyline", char.text_id) 
                
                # Storyline
                # imagemap:
                #     yoffset 20 
                #     xalign 0.5                       
                #     idle "images/ui/storyline_background.jpg"
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"

                    $ image_time = "images/ui/rectangle_08.png"
                    $ image_arrow = "images/ui/arrow_straight_03.png"
                    
                    mousewheel True
                    draggable True

                    xsize 1700
                    
                    yoffset 20
                    ysize 550
                    vbox:
                        grid 8 6:
                            # spacing 70
                            xfill True
                            vbox:
                                text "Friday" xalign 0 yalign 0.5 font gui.name_text_font color gui.accent_color
                                text "Start" xalign 0 yalign 0.5 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text ""
                                text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "" 
                                text "Evening" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "Saturday" xalign 0 yalign 0.5 font gui.name_text_font color gui.accent_color
                                text "Morning" xalign 0 yalign 0.5 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "" 
                                text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "" 
                                text "Evening" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "Sunday" xalign 0 yalign 0.5 font gui.name_text_font color gui.accent_color
                                text "Morning" xalign 0 yalign 0.5 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text ""
                                text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            for j in range(4):
                                for i in range(8):
                                    imagemap: 
                                        idle image_time
                                        text "-" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"

                            for i in range(4):
                                imagemap: 
                                    idle image_time
                                    text "12/10 - 18:00" xalign 0.5 yalign 0.5 size 16 font gui.name_text_font color "#FFFFFF"
                            imagemap: 
                                idle image_time
                                text "Dead" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"

                            text ""
                            text ""
                            text ""
            vbox:
                xminimum 420
                spacing 10
                text "Unlocked":
                    font gui.name_text_font
                    color gui.accent_color
                hbox:
                    spacing 25
                    for item in lad_details.get_objects():
                        imagebutton:
                            action SetVariable("info_screen_toggle", True) #NOT used but needed for tooltip
                            idle item.image_file                            
                            tooltip "{image=images/ui/objects_icon.png} " + item.content
                hbox:
                    spacing 25
                    for item in lad_details.get_observations():
                        imagebutton:
                            action SetVariable("info_screen_toggle", True) #NOT used but needed for tooltip
                            idle item.image_file                            
                            tooltip "{image=images/ui/observation_icon.png} " + item.content
                hbox:
                    spacing 25
                    for item in lad_details.get_intuitions():
                        imagebutton:
                            action SetVariable("info_screen_toggle", True) #NOT used but needed for tooltip
                            idle item.image_file                            
                            tooltip "{image=images/ui/intuition_icon.png} " + item.content

                text "Endings":
                    font gui.name_text_font
                    color gui.accent_color
                    
                hbox:
                    spacing 25
                    for item in lad_details.get_endings():
                        imagebutton:
                            action SetVariable("info_screen_toggle", True) #NOT used but needed for tooltip
                            idle item.image_file                            
                            tooltip str(item.content)

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                style_prefix "confirm"
                padding (50,50,50,50)
                xalign 0.5
                yalign 0.5
                text tooltip
                # textbutton "Cancel" action SetVariable("info_screen_toggle", False )