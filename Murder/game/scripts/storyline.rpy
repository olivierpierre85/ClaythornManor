label init_storylines:
    $ current_storyline = "The Lad"
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
                            idle "images/characters/" + char.text_id +".png" at character_storyline
                            action SetVariable("current_storyline", char.nickname) 
                
                # Storyline
                imagemap:
                    yoffset 20 
                    xalign 0.5                       
                    idle "images/ui/storyline_background.jpg"
                    
                    vbox:
                        text current_storyline:
                            font gui.name_text_font
                            color "#000000"
                        offset (20, 10) 
                        hbox:
                            imagemap: 
                                idle "images/ui/rectangle_03.png"
                                text "Drinks" offset (20,20) font "gui/font/BurtonScratch-Regular.ttf" color "#000000"
                            add "images/ui/arrow_straight.png"
                            imagemap: 
                                idle "images/ui/rectangle_03.png"
                                text "Dinner" offset (20,20) font "gui/font/BurtonScratch-Regular.ttf" color "#000000"
                            add "images/ui/arrow_straight.png"
                            imagemap: 
                                idle "images/ui/rectangle_03.png"
                                text "Evening" offset (20,20) font "gui/font/BurtonScratch-Regular.ttf" color "#000000"
                            add "images/ui/arrow_straight.png"
                            imagemap: 
                                idle "images/ui/rectangle_03.png"
                                text "Day 2 breakfast" offset (20,20) font "gui/font/BurtonScratch-Regular.ttf" color "#000000"
                            add "images/ui/arrow_straight.png"
                            imagemap: 
                                idle "images/ui/rectangle_03.png"
                                text "THe hunt" offset (20,20) font "gui/font/BurtonScratch-Regular.ttf" color "#000000"
                        hbox:
                            add "images/ui/rectangle_empty.png"
                            add "images/ui/arrow_empty.png"
                            add "images/ui/rectangle_empty.png"
                            add "images/ui/arrow_empty.png"
                            add "images/ui/rectangle_empty.png"
                            add "images/ui/arrow_fork.png"
                            imagemap: 
                                idle "images/ui/rectangle_03.png"
                                text "DEAD" offset (20,20) font "gui/font/BurtonScratch-Regular.ttf" color "#000000"
            vbox:
                yoffset 150
                spacing 30
                for char in char_list_flat[:4]:
                    imagebutton:
                        idle "images/characters/" + char.text_id +".png" at character_storyline
                        action SetVariable("current_storyline", char.text_id) 
            