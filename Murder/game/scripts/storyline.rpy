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
                    scrollbars "horizontal"
                    
                    mousewheel True
                    draggable True

                    xsize 1700
                    
                    yoffset 20
                    ysize 500

                    hbox:
                        yfill True
                        
                        $ image_time = "images/ui/rectangle_06.png"
                        $ image_arrow = "images/ui/arrow_straight_03.png"
                        vbox:
                            yalign 0.5
                            # text "Friday":
                            #     font gui.name_text_font
                            #     color "#FFFFFF"
                            imagemap: 
                                idle image_time
                                text "Drinks{image=images/ui/intuition_icon.png}" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                        vbox:
                            yalign 0.5
                            add image_arrow
                        vbox:
                            yalign 0.5
                            imagemap: 
                                idle image_time
                                text "Dinner" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                            imagemap: 
                                idle image_time
                                text "DEATH" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                        vbox:
                            yalign 0.5
                            add image_arrow
                            add image_arrow
                        vbox:
                            yalign 0.5
                            imagemap: 
                                idle image_time
                                text "Evening" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                            imagemap: 
                                idle image_time
                                text "Other D" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                            imagemap: 
                                idle image_time
                                text "X" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                        vbox:
                            yalign 0.5
                            add image_arrow
                            add image_arrow
                            add image_arrow
            vbox:
                xminimum 420
                spacing 10
                #vbox:
                text "Information":
                    font gui.name_text_font
                    color gui.accent_color
                # vbox:
                #     yoffset 10                        
                #     spacing 5
                #     yalign 0.0
                #     text "A green liquid next to Thomas Moody bed":
                #         yalign 0.0
                #         size 24
                #     text "An old car without gas in the garage":
                #         yalign 0.0
                #         size 24
                hbox:
                    spacing 25
                    add "images/objects/gun.png"
                    add "images/objects/gun.png"
                    add "images/objects/gun.png"
                    add "images/objects/gun.png"

            #vbox:
                #ypos 300
                text "Intuitions":
                    font gui.name_text_font
                    color gui.accent_color
                # vbox:
                #     yoffset 10
                #     text "{image=images/ui/intuition_icon.png}  There is an old car in the garage, but with no gas in it":
                #         size 24
                #         yalign 0.0
                hbox:
                    spacing 25
                    add "images/objects/gun.png"
                    add "images/objects/gun.png"
                    add "images/objects/gun.png"
            #vbox:
                # ypos 550
                text "Objects":
                    font gui.name_text_font
                    color gui.accent_color
                hbox:
                    spacing 25
                    add "images/objects/gun.png"
                    add "images/objects/gun.png"
                    add "images/objects/gun.png"
                    add "images/objects/gun.png"
                # yoffset 50
                # spacing 30
                # for char in char_list_flat[:4]:
                #     imagebutton:
                #         idle "images/characters/" + char.text_id +".png" at character_storyline
                #         action SetVariable("current_storyline", char.text_id) 

                text "Detail":
                    font gui.name_text_font
                    color gui.accent_color

                text "{image=images/ui/intuition_icon.png}  There is an old car in the garage, but with no gas in it"
            