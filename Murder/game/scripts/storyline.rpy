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
            spacing 20
            vbox:
                xminimum 1700
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
                    
                vbox:
                    offset (20, 10) 
                    for i in range(3):
                        text "Day " + str(i):
                            font gui.name_text_font
                            color "#FFFFFF"
                        
                        $ image_time = "images/ui/rectangle_06.png"
                        $ image_arrow = "images/ui/arrow_straight_03.png"
                        for j in range(2):
                            hbox:
                                imagemap: 
                                    idle image_time
                                    text "Drinks{image=images/ui/intuition_icon.png}" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                                add image_arrow
                                imagemap: 
                                    idle image_time
                                    text "Dinner" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                                add image_arrow
                                imagemap: 
                                    idle image_time
                                    text "Evening" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                                add image_arrow
                                imagemap: 
                                    idle image_time
                                    text "Day 2 breakfast" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                                add image_arrow
                                imagemap: 
                                    idle image_time
                                    text "THe hunt" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                                add image_arrow
                                imagemap: 
                                    idle image_time
                                    text "DEAD" xalign 0.5 yalign 0.5 font gui.name_text_font color "#FFFFFF"
                    # hbox:
                    #     add "images/ui/rectangle_empty.png"
                    #     add "images/ui/arrow_empty.png"
                    #     add "images/ui/rectangle_empty.png"
                    #     add "images/ui/arrow_empty.png"
                    #     add "images/ui/rectangle_empty.png"
                    #     add "images/ui/arrow_fork.png"
                    #     imagemap: 
                    #         idle image_time
                    #         text "DEAD" offset (20,20) font "gui/font/BurtonScratch-Regular.ttf" color "#FFFFFF"
            vbox:
                yoffset 150
                spacing 30
                for char in char_list_flat[:4]:
                    imagebutton:
                        idle "images/characters/" + char.text_id +".png" at character_storyline
                        action SetVariable("current_storyline", char.text_id) 
            