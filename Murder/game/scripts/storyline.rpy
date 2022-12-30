label init_storylines:
    $ current_storyline = lad_details
    return

transform character_storyline:
    zoom 0.4

# Display of storyline tree
screen storyline:
    tag menu

    $ 
    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed (You visited this place already, no action?)
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
                            mouse "hover" 
                            if char.text_id == current_storyline.text_id:
                                idle "images/characters/side/side " + char.text_id +".png" at character_storyline
                            else:                                
                                idle "images/characters/side_bw/side " + char.text_id +" bw.png" at character_storyline
                                hover "images/characters/side/side " + char.text_id + ".png"
                            
                            action SetVariable("current_storyline", char) 
                
                # Storyline
                # imagemap:
                #     yoffset 20 
                #     xalign 0.5                       
                #     idle "images/ui/storyline_background.jpg"
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"

                    $ image_time = "images/ui/rectangle_09.png"
                    $ image_time_right = "images/ui/rectangle_09_right.png"
                    $ image_time_new = "images/ui/rectangle_09_new.png"
                    $ image_time_new_2 = "images/ui/rectangle_09_new_2.png"
                    $ image_arrow = "images/ui/arrow_straight_03.png"
                    
                    mousewheel True
                    draggable True

                    xsize 1700
                    
                    yoffset 20
                    ysize 550
                    vbox:
                        grid 8 current_storyline.get_max_run() + 1:
                            # spacing 70
                            xfill True
                            # TITLES
                            vbox:
                                text "Friday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                                text "Start" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "" font gui.name_text_font
                                text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "" font gui.name_text_font
                                text "Evening" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "Saturday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                                text "Morning" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "" font gui.name_text_font
                                text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "" font gui.name_text_font
                                text "Evening" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "Sunday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                                text "Morning" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                text "" font gui.name_text_font
                                text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            # Checkpoints CONTENT
                            for j in range(current_storyline.get_max_run()):
                                for i in range(8):
                                    if current_storyline.has_checkpoint(j+1, i+1):
                                        imagemap: 
                                            
                                            if current_storyline.has_checkpoint(j+1, i+2):
                                                idle image_time_right
                                            else:
                                                idle image_time
                                            textbutton str(current_storyline.get_checkpoint(j+1, i+1).get_format_created()):
                                                mouse "hover" 
                                                action SetVariable("current_checkpoint", current_storyline.get_checkpoint(j+1, i+1)) #NOT used but needed for tooltip
                                                # xoffset 22 
                                                yalign 0.5
                                                if current_checkpoint and current_checkpoint.run == current_storyline.get_checkpoint(j+1, i+1).run and current_checkpoint.position == current_storyline.get_checkpoint(j+1, i+1).position:                
                                                    text_color "#FFFFFF"
                                                else:
                                                    text_color gui.accent_color
                                                text_font gui.name_text_font 
                                                text_size 18
                                                padding (25,25,25,25)
                                                
                                    else:
                                        if current_storyline.has_checkpoint(j+1, i+2):
                                            if current_storyline.has_checkpoint(j+2, i+2):
                                                image image_time_new_2
                                            else:
                                                image image_time_new
                                        else:
                                            text ""
            vbox:
                xminimum 420
                vbox:
                    yminimum 120
                    yoffset -20
                    text "Endings Reached":
                        font gui.name_text_font
                        color gui.accent_color

                    hbox:
                        yoffset 10
                        spacing 25
                        for item in lad_details.get_endings():
                            imagebutton:
                                action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip
                                idle item.image_file                            
                                tooltip str(item.content)

                if current_checkpoint:
                    vbox:
                        ysize 65
                        hbox:
                            # TODO should also be in one                 
                            text current_checkpoint.get_format_created() + str(current_checkpoint.position) + " "
                            imagebutton: 
                                yalign 0.5
                                mouse "hover"
                                auto "images/ui/cancel_icon_small_%s.png"
                                action SetVariable("current_checkpoint", None)
                else:
                    hbox:
                        ysize 65
                        text "Current Checkpoint"
                vbox:
                    ysize 350
                    text "Unlocked":
                        font gui.name_text_font
                        color gui.accent_color
                    hbox:
                        spacing 25
                        if current_checkpoint:
                            for item in current_checkpoint.objects: 
                                use info_card(item,"{image=images/ui/objects_icon.png} " )    
                        else:
                            for item in lad_details.get_objects():
                                use info_card(item,"{image=images/ui/objects_icon.png} " )
                            
                    hbox:
                        spacing 25
                        if current_checkpoint:
                            for item in current_checkpoint.observations:                             
                                use info_card(item, "{image=images/ui/observation_icon.png} ")
                        else:
                            for item in lad_details.get_observations():                            
                                use info_card(item, "{image=images/ui/observation_icon.png} ")

                    hbox:
                        spacing 25
                        for item in lad_details.get_intuitions():
                            use info_card(item, "{image=images/ui/intuition_icon.png} ")

                if current_checkpoint:                    
                    imagebutton:
                        auto 'images/ui/button_%s_small.png'                       
                        mouse "hover"
                        action SetVariable("action_needed_fix", None) # CONFIRM WINDOW => Start at saved thingy 
                    # TODO TERRIBLE positionning, but works SHOULD BE in image map...
                    text "Start again from there":
                        yoffset -60
                        xoffset 65

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
                # textbutton "Cancel" action SetVariable("action_needed_fix", False )

screen info_card(item, icon_file):  
    imagebutton:                        
        mouse "hover"
        action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip
        if not item.discovered:
            idle "images/info_cards/question_mark_bw.png"   
            tooltip "Hidden"
        elif item.locked: 
            idle "images/info_cards/" + item.image_file + "_bw.png"     
            tooltip icon_file + item.content
        else:
            idle "images/info_cards/" + item.image_file + ".png"                                
            tooltip icon_file + item.content