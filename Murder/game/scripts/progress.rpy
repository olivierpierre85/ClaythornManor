# TODO change size in png gimp
transform character_progress:
    zoom 0.4

transform selected_character:
    zoom 0.45

# transform is_small:
#     zoom 0.3

transform blink:
    # alpha 1.0  # Change in color
    # linear 0.5 alpha 0.3
    # linear 0.5 alpha 1.0
    zoom 1.0
    # Grow to 1.2x size over 0.5 seconds
    linear 0.7 zoom 1.2
    linear 0.7 zoom 1.0
    repeat

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
                                    # idle "images/characters/side/side " + char.text_id +".png" at character_progress
                                    idle "images/characters/side/side " + char.text_id + ".png" at selected_character
                                else:                             
                                    if char.is_character_unlocked():
                                        idle "images/characters/side/side " + char.text_id + ".png" at character_progress
                                        hover "images/characters/side_hover/side " + char.text_id + " hover.png"
                                        action [SetVariable("current_storyline", char), SetVariable("current_checkpoint", None)]
                                    else:
                                        idle "images/characters/side_bw/side " + char.text_id +" bw.png" at character_progress

                    hbox:
                        xpos 50
                        vbox:
                            yminimum 120
                            xminimum 530
                            yoffset -20
                            xoffset 0
                            text current_storyline.real_name + "'s Endings":
                                font gui.name_text_font
                                color gui.accent_color
                            hbox:
                                yoffset 10
                                spacing 15
                                for ending in current_storyline.endings.get_list():
                                    imagebutton:
                                        if ending.locked:
                                            idle "images/info_cards/question_mark_bw.png"
                                        else: 
                                            idle ending.image_file
                                            if ending.is_intuition:
                                                tooltip str(ending.content + " {image=images/ui/intuition_icon.png}")  
                                            else:
                                                tooltip str(ending.content)  
                                            action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip    
                        
                        vbox:
                            yminimum 120
                            # Params for intuition
                            yoffset -20
                            xoffset 50
                            text "Choices & Discoveries":
                                font gui.name_text_font
                                color gui.accent_color
                            
                            hbox:
                                yoffset 10
                                spacing 15
                                $ current_status_checkpoint = Checkpoint(run=current_run, position=current_position, objects=copy.deepcopy(current_storyline.objects.get_unlocked()), observations=copy.deepcopy(current_storyline.observations.get_unlocked()), important_choices=copy.deepcopy(current_storyline.important_choices.get_unlocked()), label_id="current", saved_variables=copy.deepcopy(current_character.saved_variables), ending=False)

                                imagebutton:
                                    yoffset 2
                                    mouse "hover"
                                    action [SetVariable("current_checkpoint", current_status_checkpoint), ShowMenu("storyline_details", "current_status", current_storyline)]
                                    if current_storyline.is_everything_completed():
                                        idle "images/info_cards/everything_completed.png"
                                    else:
                                        idle "images/info_cards/everything_completed_bw.png"
                                
                                $ unlocked = current_storyline.get_total_unlocked_discoveries()
                                $ total    = current_storyline.get_total_discoveries()
                                if current_storyline.is_everything_completed():
                                    textbutton "[unlocked]/[total]":
                                        text_size 56
                                        text_font gui.name_text_font
                                        text_color gui.highlight_color
                                        action [SetVariable("current_checkpoint", current_status_checkpoint), ShowMenu("storyline_details", "current_status", current_storyline)]
                                else:
                                    textbutton "{color=#fff}[unlocked]{/color}/[total]":
                                        text_size 56
                                        text_font gui.name_text_font
                                        text_color gui.accent_color
                                        action [SetVariable("current_checkpoint", current_status_checkpoint), ShowMenu("storyline_details", "current_status", current_storyline)]
                vbox:

                    xsize 1700
                    yoffset 20

                    $ checkpoint_x = 283
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
                            text "Sunday" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                        vbox:
                            xminimum checkpoint_x
                            text "" xalign 0 yalign 0 font gui.name_text_font color gui.accent_color
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"

                        vbox:
                            xminimum checkpoint_x
                            text "" font gui.name_text_font
                            # text "Afternoon" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"
                            text "" xalign 0 yalign 0 font gui.name_text_font color "#FFFFFF"
                        # vbox:
                        #     xminimum checkpoint_x_small
                        #     text "" font gui.name_text_font
                    
                    for line_index, line in enumerate(current_storyline.progress):
                        hbox:
                            xalign 0
                            for chapter_index, chapter in enumerate(line):
                                if chapter.chapter_type == "image":
                                    imagemap:
                                        idle chapter.image_file
                                elif chapter.chapter_type == "checkpoint":                       
                                    imagemap:
                                        idle chapter.image_file
                                        # Don't show if the character hasn't reached the chapter yet
                                        if len(current_storyline.get_checkpoints_by_chapter(chapter.label))>0:
                                            $ should_blink = current_chapter == chapter.name
                                            textbutton chapters_names[chapter.name]:
                                                mouse "hover" 
                                                action [SetVariable("current_checkpoint", None), ShowMenu("storyline_details", chapter, current_storyline, is_current=should_blink)]
                                                xoffset -20 
                                                yoffset -5
                                                yalign 0.5
                                                xalign 0.5
                                                text_color gui.accent_color
                                                text_hover_color "#FFFFFF" 
                                                text_font gui.name_text_font 
                                                text_size 28
                                                style "confirm_prompt" # TODO: Something here that centers multiline text. What?
                                                padding (60, 25, 60, 25)
                                                if should_blink:
                                                    text_color gui.highlight_color
                                                    at blink
                                        else:
                                            textbutton "?":
                                                xoffset -20 
                                                yoffset -5
                                                yalign 0.5
                                                xalign 0.5
                                                text_color gui.accent_color
                                                text_font gui.name_text_font 
                                                text_size 28
                                                padding (70, 25, 70, 25) 

                                elif chapter.chapter_type == "ending": 
                                    imagebutton:
                                        if current_storyline.endings.is_unlocked(chapter.label):
                                            idle current_storyline.endings.get_item(chapter.label).image_file
                                            tooltip str(current_storyline.endings.get_item(chapter.label).content)  
                                            # action SetVariable("action_needed_fix", True)
                                            mouse "hover"
                                            action [SetVariable("current_checkpoint", None), ShowMenu("storyline_details", chapter, current_storyline, True)]
                                        else:
                                            idle chapter.image_file 
                                elif chapter.chapter_type == "start": 
                                    imagebutton:
                                        mouse 'hover'
                                        idle image_checkpoint_start
                                        hover image_checkpoint_start_selected
                                        action [SetVariable("current_checkpoint", None), ShowMenu("storyline_details", "start", current_storyline)]

    use tooltip_display

# Define a separate screen for tooltips
screen tooltip_display():
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                style_prefix "confirm"
                padding (50, 50, 50, 50)
                xalign 0.5
                yalign 0.5
                text tooltip

screen info_card(item=None, item_type=None, is_small=False):  
    python:
        if item:
            if item_type == 'object':
                icon_file = "{image=images/ui/objects_icon.png} "
            elif item_type == 'observation':
                icon_file = "{image=images/ui/observation_icon.png} "
            elif item_type == 'choice':
                icon_file = "{image=images/ui/choice_icon.png} "
            else:
                icon_file = "???"
            
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

        if is_small:
            # For the moment, only display the activated choices of this checkpoint

            # if not item:
            #     idle Transform("images/info_cards/empty.png", zoom=0.5)
            # elif not item.discovered:
            #     idle Transform("images/info_cards/question_mark_bw.png", zoom=0.5) 
            #     tooltip "Hidden"
            # elif not locked: 
                idle Transform("images/info_cards/" + item.image_file + ".png", zoom=0.5)   
                tooltip icon_file + item.content
            # else:
            #     idle Transform("images/info_cards/" + item.image_file + "_bw.png", zoom=0.5)                           
            #     tooltip icon_file + item.content_negative
        else:
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
                tooltip icon_file + item.content_negative


screen storyline_details(selected_chapter, selected_char, ending = False, is_current = False):

    #     on "show" action SetVariable("current_checkpoint", None)

    tag menu

    use game_menu(_("Storyline"), scroll="fixed"):

        # Main container
        fixed:
            # Main hbox with columns
            hbox:
                xpos 80
                ypos 20
                spacing 40
                yalign 0.0  # Align columns at the top

                # Left column: Character name and picture
                vbox:
                    spacing 10
                    yalign 0.0

                    text selected_char.real_name:
                        size 48
                        font gui.name_text_font
                        color gui.accent_color
                        outlines [ (absolute(1), "#140303", absolute(0), absolute(0)) ]

                    add "images/characters/side/side " + selected_char.text_id + ".png"

                # Center column: Title and list of save checkpoints in a viewport
                if not selected_chapter == "current_status":
                    vbox:
                        spacing 10
                        yalign 0.0
                        xoffset 100

                        if selected_chapter == "start":
                            text "Introduction":
                                size 48
                                font gui.name_text_font
                        # elif selected_chapter == "current_status":
                        #     text "What has been discovered and what is unlocked now":
                        #         size 48
                        #         font gui.name_text_font
                        elif ending:
                            text current_storyline.endings.get_item(selected_chapter.label).content:
                                size 48
                                font gui.name_text_font
                        else:
                            text chapters_names[selected_chapter.name]:
                                size 48
                                font gui.name_text_font

                        frame:
                            xmaximum 750 
                            ymaximum 360  
                            has viewport:
                                draggable True 
                                mousewheel True
                                scrollbars "vertical"

                            vbox:
                                spacing 0
                                if selected_chapter == "start":
                                    textbutton str("Start"):                                    
                                        xoffset 20
                                        action SetVariable("current_checkpoint", current_storyline.get_init_checkpoint())
                                elif selected_chapter == "current_status":
                                    pass
                                    # textbutton str("See what's currently discovered unlocked"):
                                    #     action SetVariable("current_checkpoint", Checkpoint(
                                    #             run = current_run,
                                    #             position = current_position,
                                    #             objects = copy.deepcopy(current_storyline.objects.get_unlocked()), 
                                    #             observations = copy.deepcopy(current_storyline.observations.get_unlocked()),
                                    #             important_choices = copy.deepcopy(current_storyline.important_choices.get_unlocked()),
                                    #             label_id = "current",
                                    #             saved_variables = copy.deepcopy(current_character.saved_variables),
                                    #             ending = ending
                                    #         ))
                                else:
                                    if is_current:
                                        # TODO: maybe but in function for clarity
                                        $ active_checkpoint = Checkpoint(
                                                run = current_run,
                                                position = current_position,
                                                objects = copy.deepcopy(current_storyline.objects.get_unlocked()), 
                                                observations = copy.deepcopy(current_storyline.observations.get_unlocked()),
                                                important_choices = copy.deepcopy(current_storyline.important_choices.get_unlocked()),
                                                label_id = "current",
                                                saved_variables = copy.deepcopy(current_character.saved_variables),
                                                ending = ending,
                                                all_menus = copy.deepcopy(all_menus),
                                            )
                                        textbutton str("See current status"):
                                            xoffset 20
                                            if current_checkpoint and current_checkpoint.label_id == "current":
                                                text_color gui.accent_color
                                            action SetVariable("current_checkpoint", active_checkpoint)

                                    for i, checkpoint in enumerate(selected_char.get_checkpoints_by_chapter(selected_chapter.label)):
                                        vbox:
                                            xoffset 20
                                            yminimum 70
                                            textbutton "{}".format(checkpoint.get_format_created()):
                                                xpadding 0
                                                ypadding 0
                                                xmargin 0
                                                ymargin 0
                                                action SetVariable("current_checkpoint", checkpoint)
                                                if current_checkpoint == checkpoint:
                                                    text_color gui.accent_color
                                            hbox:
                                            # NOw gets all the choices
                                                for item in current_storyline.get_choices_and_discoveries_by_chapter(selected_chapter.name):
                                                    if item.text_id in checkpoint.get_activated_choices_and_discoveries():
                                                        use info_card(item, item.type, True)
                        
                        if current_checkpoint and not ending and not current_checkpoint.label_id == "current" and seen_tutorial_restart:
                            
                            button:
                                action Show("confirm_restart")
                                background "images/ui/button_idle_small.png"
                                hover_background "images/ui/button_hover_small.png"
                                xysize (430, 65)

                                text "Restart from there":
                                    color "#FFFFFF"
                                    align (0.5, 0.5)

                # Right column: Details of the selected checkpoint
                vbox:
                    spacing 10
                    yalign 0.0
                    xoffset 100
                    # yoffset -40
                    xminimum 650

                    if current_checkpoint:
                        if current_checkpoint.label_id == "current":
                            text "Choices & Discoveries Activated":
                                font gui.name_text_font
                                size 48
                                color gui.accent_color
                        else:
                            text "Choices & Discoveries Activated":
                                font gui.name_text_font
                                size 48
                                color gui.accent_color

                        vbox:
                            # spacing 5
                            yoffset 20
                            # text "Choices & Discoveries" size 24 font gui.name_text_font color gui.accent_color
                            $ number_of_rows = ((len(current_storyline.get_choices_and_discoveries_by_chapter(selected_chapter.name)) + 5) // 6)
                            grid 6 number_of_rows:
                                spacing 13
                                for item in current_storyline.get_choices_and_discoveries_by_chapter(selected_chapter.name):
                                    use info_card(item, item.type)
                        # # SUB-LIST: CHOICES
                        # vbox:
                        #     spacing 5
                        #     text "Choices" size 24 font gui.name_text_font color gui.accent_color
                        #     $ number_of_rows = ((len(current_storyline.important_choices.get_list()) + 4) // 5)
                        #     grid 5 number_of_rows:
                        #         spacing 13
                        #         for item in current_storyline.important_choices.get_list():
                        #             use info_card(item, "choice")

                        # # SUB-LIST: OBJECTS
                        # vbox:
                        #     spacing 5
                        #     text "Objects" size 24 font gui.name_text_font color gui.accent_color
                        #     grid 5 1:
                        #         spacing 13
                        #         for item in current_storyline.objects.get_list():
                        #             use info_card(item, "object")

                        # # SUB-LIST: OBSERVATIONS
                        # vbox:
                        #     spacing 5
                        #     text "Observations" size 24 font gui.name_text_font color gui.accent_color
                        #     grid 5 1:
                        #         spacing 13
                        #         for item in current_storyline.observations.get_list():
                        #             use info_card(item, "observation")
                    else:
                        text "Select a checkpoint to see details.":
                            size 32
                            font gui.name_text_font


        fixed:
            textbutton _("Return"):
                align (1.0, 1.0)
                xoffset 400  
                yoffset -150  
                action ShowMenu("progress")

    use tooltip_display


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

    class Chapter:
        def __init__(self, image_file, chapter_type="image", label=None, name=None):
            self.image_file = image_file  # Mandatory
            self.chapter_type = chapter_type  
            self.label = label
            self.name = name


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
            ending = None,
            all_menus = None,
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
            self.all_menus = all_menus

        def get_format_created(self):
            return self.created.strftime("%A") + f" {self.created.day} " + self.created.strftime("%B %Y, %H:%M")

        # def get_format_created_up(self):
        #     return self.created.strftime("%a %b")

        # def get_format_created_down(self):
        #     return self.created.strftime("%H:%M")

        def get_activated_choices_and_discoveries(self):
            activated_list = []

            # Collect from important_choices
            for item in self.important_choices:
                activated_list.append(item)

            # Collect from observations
            for item in self.observations:
                activated_list.append(item)

            # Collect from objects
            for item in self.objects:
                activated_list.append(item)

            return activated_list

        
        def debug_string(self):
            return 'Run:' + str(self.run) + '; position:' + str(self.position) + '; gun:' + str(len(self.objects))

        def __str__(self):
            return 'Run:' + str(self.run) + '; position:' + str(self.position) + '; objects:' + str(self.objects)