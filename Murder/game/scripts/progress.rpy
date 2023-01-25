# TODO change size in png gimp
transform character_progress:
    zoom 0.4

# Display of Progress tree
screen progress:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed (You visited this place already, no action?)
    use game_menu(_("Storyline"), scroll="fixed"):

        hbox:
            spacing 10
            vbox:
                xminimum 1420
                xalign 0.5
                # Character choice
                hbox:
                    xalign 0.5
                    spacing 20
                    for char in char_list_flat:
                        imagebutton:
                            mouse "hover" 
                            if char.text_id == current_storyline.text_id:
                                idle "images/characters/side/side " + char.text_id +".png" at character_progress
                            else:                                
                                idle "images/characters/side_bw/side " + char.text_id +" bw.png" at character_progress
                                hover "images/characters/side/side " + char.text_id + ".png"
                            
                            action [SetVariable("current_storyline", char), SetVariable("current_checkpoint", None)]
                
                viewport:
                    yinitial 0.0
                    scrollbars "vertical"
                    
                    mousewheel True
                    draggable True

                    xsize 1700
                    
                    yoffset 20
                    ysize 550
                    $ checkpoint_x = 173
                    $ checkpoint_x_small = 100
                    vbox:

                        hbox:
                            # TITLES
                            vbox:
                                xminimum checkpoint_x_small
                                text "Friday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                                text "Start" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                xminimum checkpoint_x
                                text "" font gui.name_text_font
                                text "Evening" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                xminimum checkpoint_x
                                text "Saturday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                                text "Morning" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"
                            
                            vbox:
                                xminimum checkpoint_x
                                text "" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                                text "The Hunt" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                xminimum checkpoint_x
                                text "" font gui.name_text_font
                                text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                xminimum checkpoint_x
                                text "" font gui.name_text_font
                                text "Evening" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                xminimum checkpoint_x
                                text "Sunday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                                text "Morning" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                            vbox:
                                xminimum checkpoint_x
                                text "" font gui.name_text_font
                                text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"
                            vbox:
                                xminimum checkpoint_x/2
                                text "" font gui.name_text_font

                        $ image_checkpoint = "images/ui/progress/rectangle_progress.png"
                        $ image_checkpoint_right = "images/ui/progress/rectangle_progress_right.png"                       
                        
                        $ image_checkpoint_start = "images/ui/progress/rectangle_small.png"
                        $ image_checkpoint_start_empty = "images/ui/progress/rectangle_small_empty.png"
                        $ image_checkpoint_start_selected = "images/ui/progress/rectangle_small_selected.png"
                        $ image_checkpoint_start_corner = "images/ui/progress/rectangle_small_corner.png"
                        $ image_checkpoint_start_line = "images/ui/progress/rectangle_small_line.png"
                        $ image_checkpoint_start_double_corner = "images/ui/progress/rectangle_small_double_corner.png"
                        
                        for j in range(current_storyline.get_max_run()):
                            hbox:

                                xalign 0

                                if j == 0 and current_storyline.is_character_unlocked():
                                    imagebutton:
                                        mouse 'hover'
                                        if current_checkpoint and current_checkpoint.position == 0 and  current_checkpoint.run == 1:
                                            idle image_checkpoint_start_selected
                                        else:
                                            idle image_checkpoint_start
                                        action SetVariable("current_checkpoint", current_storyline.get_init_checkpoint())
                                else:
                                    imagebutton:
                                        if current_storyline.has_checkpoint_in_column(j,1):
                                            if current_storyline.has_checkpoint(j+1, 1):
                                                if current_storyline.has_checkpoint_in_column(j+1,1):
                                                    idle image_checkpoint_start_double_corner
                                                else:
                                                    idle image_checkpoint_start_corner
                                            else:
                                                idle image_checkpoint_start_line
                                        else:
                                            idle image_checkpoint_start_empty

                                for i in range(8):                               
                                    if current_storyline.has_checkpoint(j+1, i+1):
                                        if current_storyline.get_checkpoint(j+1, i+1).ending:
                                            imagebutton:
                                                mouse "hover"
                                                action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip
                                                idle current_storyline.get_checkpoint(j+1, i+1).ending.image_file                            
                                                tooltip str(current_storyline.get_checkpoint(j+1, i+1).ending.content)

                                        else:
                                            imagemap:
                                                if current_storyline.has_checkpoint(j+1, i+2):
                                                    idle image_checkpoint_right
                                                else:
                                                    idle image_checkpoint

                                                textbutton str(current_storyline.get_checkpoint(j+1, i+1).get_format_created()): #+ " - " + str(current_storyline.get_checkpoint(j+1, i+1).get_format_created_down()):
                                                    mouse "hover" 
                                                    action SetVariable("current_checkpoint", current_storyline.get_checkpoint(j+1, i+1))
                                                    xoffset -10 
                                                    yalign 0.5
                                                    xalign 0.5
                                                    if current_checkpoint and current_checkpoint.run == current_storyline.get_checkpoint(j+1, i+1).run and current_checkpoint.position == current_storyline.get_checkpoint(j+1, i+1).position:                
                                                        text_color "#FFFFFF"
                                                    else:
                                                        text_color gui.accent_color
                                                    text_font gui.name_text_font 
                                                    text_size 20
                                                    padding (25,25,25,25)
                                                
                                    else:
                                        image current_storyline.get_checkpoint_filler(j+1, i+1)

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
                            text current_checkpoint.debug_string() # + " " str(current_checkpoint.position) + " "
                            # $ test_menu = str(current_checkpoint.saved_variables["psychic_generic_menu"])
                            # text test_menu
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
                        # if current_checkpoint:
                        #     for item in current_checkpoint.objects: 
                        #         use info_card(item,"{image=images/ui/objects_icon.png} " )    
                        # else:
                        for item in lad_details.get_objects():
                            if current_checkpoint:
                                use info_card(item,"{image=images/ui/objects_icon.png} ", not item.text_id in current_checkpoint.objects )
                            else:
                                use info_card(item,"{image=images/ui/objects_icon.png} ", item.locked )
                    hbox:
                        spacing 25
                        for item in lad_details.get_observations():                            
                            if current_checkpoint:
                                use info_card(item,"{image=images/ui/observation_icon.png} ", not item.text_id in current_checkpoint.observations )
                            else:
                                use info_card(item,"{image=images/ui/observation_icon.png} ", item.locked )

                    hbox:
                        spacing 25
                        for item in lad_details.get_intuitions():
                            use info_card(item, "{image=images/ui/intuition_icon.png} ")

                if current_checkpoint:                    
                    imagebutton:
                        auto 'images/ui/button_%s_small.png'                       
                        mouse "hover"
                        action Show("confirm_restart")
                    # TODO TERRIBLE positioning, but works SHOULD BE in image map...
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

screen info_card(item, icon_file, locked = True):  
    imagebutton:                        
        mouse "hover"
        action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip
        if not item.discovered:
            idle "images/info_cards/question_mark_bw.png"   
            tooltip "Hidden"
        elif not locked: 
            idle "images/info_cards/" + item.image_file + ".png"     
            tooltip icon_file + item.content
        else:
            idle "images/info_cards/" + item.image_file + "_bw.png"                                
            tooltip icon_file + item.content
    

screen confirm_restart():

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Are you sure you want to restart from there?"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Restart") action Start("start_again")
                textbutton _("Cancel") action Hide("confirm_restart")

init -100 python:
    class Checkpoint():
        def __init__(
            self, 
            run,
            position,
            objects,
            observations,
            label_id,
            saved_variables,
            ending = None
        ):
            self.run = run
            self.position = position
            self.objects = objects or []
            self.observations = observations or []
            self.created = datetime.now()
            self.label_id = label_id
            self.saved_variables = saved_variables
            self.ending = ending

        def get_format_created(self):
            return self.created.strftime("%a %b, %H:%M")

        def get_format_created_up(self):
            return self.created.strftime("%a %b")

        def get_format_created_down(self):
            return self.created.strftime("%H:%M")
        
        def debug_string(self):
            return 'Run:' + str(self.run) + '; position:' + str(self.position) + '; gun:' + str(len(self.objects))

        def __str__(self):
            return 'Run:' + str(self.run) + '; position:' + str(self.position) + '; objects:' + str(self.objects)