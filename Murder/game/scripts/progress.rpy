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
                xminimum 1920
                xalign 0.5
                # Character choice
                hbox:
                    yalign 0
                    hbox:
                        spacing 20
                        xalign 0.0
                        # Character choice list
                        for char in char_list_flat:
                            imagebutton:
                                mouse "hover" 
                                if char.text_id == current_storyline.text_id:
                                    idle "images/characters/side/side " + char.text_id +".png" at character_progress
                                else:                                
                                    idle "images/characters/side_bw/side " + char.text_id +" bw.png" at character_progress
                                    hover "images/characters/side/side " + char.text_id + ".png"
                                if char.is_character_unlocked():
                                    action [SetVariable("current_storyline", char), SetVariable("current_checkpoint", None)]


                    hbox:
                        xpos 50
                        # text current_storyline.real_name:
                        #     yoffset -20
                        #     font gui.name_text_font
                        #     color gui.accent_color
                        vbox:
                            yminimum 120
                            yoffset -20
                            xoffset 30
                            text current_storyline.real_name + "'s Endings":
                                font gui.name_text_font
                                color gui.accent_color
                            hbox:
                                yoffset 10
                                spacing 25
                                for item in current_storyline.endings.get_list():
                                    imagebutton:
                                        if item.locked:
                                            idle "images/info_cards/question_mark_bw.png"
                                        else: 
                                            idle item.image_file
                                            tooltip str(item.content)  
                                            action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip    
                        
                        vbox:
                            yminimum 120
                            yoffset -20
                            xoffset 100
                            text current_storyline.real_name + "'s Intuitions":
                                font gui.name_text_font
                                color gui.accent_color
                            hbox:
                                yoffset 10
                                spacing 25
                                for item in current_storyline.intuitions.get_list():
                                    imagebutton:
                                        if item.locked:
                                            idle "images/info_cards/question_mark_bw.png"
                                        else: 
                                            idle item.image_file
                                            tooltip str(item.content)  
                                            action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip 
                vbox:
                    # yinitial 0.0
                    # scrollbars "vertical"
                    
                    # mousewheel True
                    # draggable True

                    xsize 1700
                    yoffset 20

                    $ checkpoint_x = 236
                    $ checkpoint_x_small = 100

                    hbox:
                        # TITLES
                        vbox:
                            xminimum checkpoint_x_small
                            text "Friday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                        vbox:
                            xminimum checkpoint_x
                            text "" font gui.name_text_font
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                        vbox:
                            xminimum checkpoint_x
                            text "Saturday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"
                        
                        vbox:
                            xminimum checkpoint_x
                            text "" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                        vbox:
                            xminimum checkpoint_x
                            text "" font gui.name_text_font
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                        vbox:
                            xminimum checkpoint_x
                            text "" font gui.name_text_font
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                        vbox:
                            xminimum checkpoint_x
                            text "Sunday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                        vbox:
                            xminimum checkpoint_x
                            text "" font gui.name_text_font
                            # text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"
                        # vbox:
                        #     xminimum checkpoint_x_small
                        #     text "" font gui.name_text_font
                    
                    for line_index, line in enumerate(lad_progress):
                        hbox:
                            xalign 0
                            for chapter_index, chapter in enumerate(line):
                                if chapter.chapter_type == "image":
                                    imagemap:
                                        idle chapter.image_file
                                elif chapter.chapter_type == "checkpoint":                       
                                    imagemap:
                                        idle chapter.image_file
                                        textbutton str(chapter.text): #+ " - " + str(current_storyline.get_checkpoint(j+1, i+1).get_format_created_down()):
                                            mouse "hover" 
                                            # action SetVariable("current_checkpoint", current_storyline.get_checkpoint(j+1, i+1))
                                            action ShowMenu("storyline_details", chapter, current_storyline)
                                            xoffset -20 
                                            yoffset -5
                                            yalign 0.5
                                            xalign 0.5
                                            text_color gui.accent_color
                                            text_hover_color "#FFFFFF" 
                                            text_font gui.name_text_font 
                                            text_size 28
                                            padding (25,25,25,25)
                                elif chapter.chapter_type == "ending": 
                                    imagebutton:
                                        if current_storyline.endings.is_unlocked(chapter.label):
                                            idle current_storyline.endings.get_item(chapter.label).image_file
                                            tooltip str(current_storyline.endings.get_item(chapter.label).content)  
                                            action SetVariable("action_needed_fix", True)
                                        else:
                                            idle chapter.image_file 

            #         for j in range(current_storyline.get_max_run()):
            #                 hbox:

            #                     xalign 0

            #                     if j == 0 and current_storyline.is_character_unlocked():
            #                         imagebutton:
            #                             mouse 'hover'
            #                             # if current_checkpoint and current_checkpoint.position == 0 and  current_checkpoint.run == 1:
            #                             #     idle image_checkpoint_start_selected
            #                             # else:
            #                             idle image_checkpoint_start
            #                             # action SetVariable("current_checkpoint", current_storyline.get_init_checkpoint())
            #                             action ShowMenu("storyline_details", current_storyline.get_init_checkpoint(), current_storyline)
            #                     else:
            #                         imagebutton:
            #                             if current_storyline.has_checkpoint_in_column(j,1):
            #                                 if current_storyline.has_checkpoint(j+1, 1):
            #                                     if current_storyline.has_checkpoint_in_column(j+1,1):
            #                                         idle image_checkpoint_start_double_corner
            #                                     else:
            #                                         idle image_checkpoint_start_corner
            #                                 else:
            #                                     idle image_checkpoint_start_line
            #                             else:
            #                                 idle image_checkpoint_start_empty

            #                     for i in range(8):                               
            #                         if current_storyline.has_checkpoint(j+1, i+1):
            #                             if current_storyline.get_checkpoint(j+1, i+1).ending:
            #                                 imagebutton:
            #                                     mouse "hover"
            #                                     action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip
            #                                     idle current_storyline.get_checkpoint(j+1, i+1).ending.image_file                            
            #                                     tooltip str(current_storyline.get_checkpoint(j+1, i+1).ending.content)

            #                             else:
            #                                 imagemap:
            #                                     if current_storyline.has_checkpoint(j+1, i+2):
            #                                         idle image_checkpoint_right
            #                                     else:
            #                                         idle image_checkpoint

            #                                     textbutton str(current_storyline.get_checkpoint(j+1, i+1).get_format_created()): #+ " - " + str(current_storyline.get_checkpoint(j+1, i+1).get_format_created_down()):
            #                                         mouse "hover" 
            #                                         # action SetVariable("current_checkpoint", current_storyline.get_checkpoint(j+1, i+1))
            #                                         action ShowMenu("storyline_details", current_storyline.get_checkpoint(j+1, i+1), current_storyline)
            #                                         xoffset -10 
            #                                         yalign 0.5
            #                                         xalign 0.5
            #                                         if current_checkpoint and current_checkpoint.run == current_storyline.get_checkpoint(j+1, i+1).run and current_checkpoint.position == current_storyline.get_checkpoint(j+1, i+1).position:                
            #                                             text_color "#FFFFFF"
            #                                         else:
            #                                             text_color gui.accent_color
            #                                         text_font gui.name_text_font 
            #                                         text_size 20
            #                                         padding (25,25,25,25)
                                                
            #                         else:
            #                             image current_storyline.get_checkpoint_filler(j+1, i+1)

            # # vbox:
            #     xminimum 20
                
                # TODO MOVE TO EXTRA SCREEN
                # if current_checkpoint:
                #     vbox:                        
                #         ysize 65
                #         yoffset 20
                #         hbox:    
                #             if current_checkpoint.position == 0:
                #                 text "Start"
                #             else:                            
                #                 text current_checkpoint.get_format_created()        
                #                 # text current_checkpoint.debug_string() # + " " str(current_checkpoint.position) + " "
                #                 text " Checkpoint"
                #             imagebutton: 
                #                 xoffset 10
                #                 yalign 0.5
                #                 mouse "hover"
                #                 auto "images/ui/cancel_icon_small_%s.png"
                #                 action SetVariable("current_checkpoint", None)
                # else:
                #     hbox:
                #         ysize 65
                #         yoffset 20
                #         text "Current Checkpoint"
                # vbox:
                #     ysize 230
                #     yoffset 10
                #     text "Important information":
                #         font gui.name_text_font
                #         color gui.accent_color
                #     # IN GRID
                #     grid 5 2:
                #         spacing 13
                #         $ grid_fill = 10
                #         for item in current_storyline.important_choices.get_list():
                #             $ grid_fill -= 1
                #             if current_checkpoint:
                #                 use info_card(item, "choice")
                #             else:
                #                 use info_card(item, "choice")
                        
                #         for item in current_storyline.objects.get_list():
                #             $ grid_fill -= 1
                #             if current_checkpoint:
                #                 use info_card(item, "objects")
                #             else:
                #                 use info_card(item, "objects")

                #         for item in (current_storyline.observations.get_list()):
                #             $ grid_fill -= 1
                #             if current_checkpoint:
                #                 use info_card(item, "observations")
                #             else:
                #                 use info_card(item, "observations")
                        
                #         if grid_fill > 0 :
                #             for i_fill in range(grid_fill):
                #                 use info_card()#TODO empty image (empty Checkpoint emptu...)

                # if current_checkpoint:                    
                #     imagebutton:
                #         auto 'images/ui/button_%s_small.png'                       
                #         mouse "hover"
                #         action Show("confirm_restart")
                #     # TODO TERRIBLE positioning, but works SHOULD BE in image map...
                #     text "Start again from there":
                #         yoffset -60
                #         xoffset 65

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

screen info_card(item=None, item_type=None):  
    python:
        if item:
            if item_type == 'object':
                icon_file = "{image=images/ui/objects_icon.png} "
            elif item_type == 'observation':
                icon_file = "{image=images/ui/observation_icon.png} "
            else:
                icon_file = "(choice?) "
            
            if current_checkpoint:
                if item_type == 'object':
                    locked = (not item.text_id in current_checkpoint.objects)
                elif item_type == 'observation':
                    locked = (not item.text_id in current_checkpoint.observations)
                else:
                    locked = (not item.text_id in current_checkpoint.important_choices)
            else:
                locked = item.locked

    imagebutton:                        
        mouse "hover"
        action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip
        if not item:
            idle "images/info_cards/empty.png"   
        elif not item.discovered:
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


screen storyline_details(selected_checkpoint, selected_char):

    tag menu #????
    use game_menu(_("Storyline"), scroll="fixed"):

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
                    outlines [ (absolute(1), "#140303", absolute(0), absolute(0)) ]
                add "images/characters/side/side " + selected_char.text_id +".png"
                
            vbox:     
                xoffset 50

                # TODO Add a list of all checkpoints at this TIME SO RETHINK ALL THAT
                # hbox:
                #     ymaximum 600
                #     viewport id "char_description_viewport":
                #         draggable True 
                #         mousewheel True #
                #         vbox:
                #             spacing 15
                #             for line in selected_char.get_description_full():
                #                 text line:
                #                     font gui.name_text_font
                #             # text selected_char.get_description_full():
                #             #     font gui.name_text_font
                #             #     line_leading  15

                #         # You can add more content here if necessary
                #     vbar value YScrollValue("char_description_viewport")
                
                textbutton _("Return"): 
                    yoffset 20
                    xalign 1.0 
                    yalign 0.0
                    xpos 350
                    action ShowMenu("progress")

init -100 python:

    class Chapter:
        def __init__(self, image_file, chapter_type="image", label=None, text=None):
            self.image_file = image_file  # Mandatory
            self.chapter_type = chapter_type  
            self.label = label  # Optional, default is None
            self.text = text  # Optional, default is None


    class Checkpoint():
        def __init__(
            self, 
            run,
            position,
            objects,
            observations,
            important_choices,
            label_id,
            saved_variables,
            ending = None
        ):
            self.run = run
            self.position = position
            self.objects = objects or []
            self.observations = observations or []
            self.important_choices = important_choices or []
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