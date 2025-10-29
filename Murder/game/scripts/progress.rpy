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

style chapter_button:
    xalign 0.5
    yalign 0.5
    xoffset -20
    yoffset -5
    # text_font gui.name_text_font
    # text_size 28
    padding (60, 25)
    text_align 0.5   # centers multiline text
    # Optionally set an xminimum or xmaximum to control wrapping

style chapter_button_text:
    xalign 0.5     # center the Text displayable within the button
    text_align 0.5 # center each line within its own box

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
                vbox:
                    # yminimum 120
                    # xminimum 260
                    yoffset -30
                    # xoffset -100 
                    xalign 0
                    # text current_storyline.real_name + "'s :":
                    text current_storyline.real_name:
                        font gui.name_text_font
                        color gui.accent_color
                        size 46
                # Character choice
                hbox:
                    yalign 0
                    hbox:
                        yoffset 25
                        spacing 20
                        xalign 0.0
                        # Character choice list
                        for char in char_list_flat:
                            imagebutton:
                                mouse "hover" 
                                if char.text_id == current_storyline.text_id:
                                    # idle "images/characters/side/side " + char.text_id +".png" at character_progress
                                    if char.is_character_unlocked():
                                        idle "images/characters/side/side " + char.text_id + ".png" at selected_character
                                    else:
                                        idle "images/characters/side_bw/side " + char.text_id + " bw.png" at selected_character
                                else:                             
                                    if char.is_character_unlocked():
                                        idle "images/characters/side/side " + char.text_id + ".png" at character_progress
                                        hover "images/characters/side_hover/side " + char.text_id + " hover.png"
                                        if not tutorial_on:
                                            action [SetVariable("current_storyline", char), SetVariable("current_checkpoint", None)]
                                    else:
                                        idle "images/characters/side_bw/side " + char.text_id +" bw.png" at character_progress
                                        if not tutorial_on:
                                            action [SetVariable("current_storyline", char), SetVariable("current_checkpoint", None)]

                    vbox:
                        xpos 50
                        # vbox:
                        #     # yminimum 120
                        #     # xminimum 260
                        #     yoffset -30
                        #     xoffset 0
                        #     xalign 0.5
                        #     # text current_storyline.real_name + "'s :":
                        #     text current_storyline.real_name:
                        #         font gui.name_text_font
                        #         color gui.accent_color
                        hbox:
                            # TODO REDO ENTIRELY
                            vbox:
                                yminimum 120
                                xminimum 260
                                yoffset -20
                                xoffset 0
                                text "Endings":
                                    font gui.name_text_font
                                    color gui.accent_color
                                    size 28

                                hbox:
                                    yoffset 10
                                    spacing 15

                                    imagebutton:
                                        yoffset 2
                                        mouse "hover"
                                        idle "images/info_cards/everything_completed.png"
                                        action ShowMenu("character_details", current_storyline)

                                    vbox:
                                        textbutton "6/13":
                                            text_size 22
                                            text_font gui.name_text_font
                                            text_color gui.highlight_color
                                        bar:
                                            yalign 0.5
                                            value current_storyline.get_character_progress() 
                                            range 100
                                            xmaximum 150
                                            style 'progress_bar'

                            vbox:
                                yminimum 120
                                xminimum 200
                                yoffset -20
                                xoffset 0
                                text "Description":
                                # text current_storyline.real_name + "'s Description":
                                    font gui.name_text_font
                                    color gui.accent_color
                                    size 28

                                hbox:
                                    yoffset 10
                                    spacing 15

                                    imagebutton:
                                        yoffset 2
                                        mouse "hover"
                                        idle "images/info_cards/everything_completed.png"
                                        action ShowMenu("character_details", current_storyline)

                                    vbox:
                                        textbutton "6/12":
                                            text_size 22
                                            text_font gui.name_text_font
                                            text_color gui.highlight_color
                                        bar:
                                            yalign 0.5
                                            value current_storyline.get_character_progress() 
                                            range 100
                                            xmaximum 150
                                            style 'progress_bar'

                                # hbox:
                                #     yoffset 10
                                #     spacing 15
                                #     for ending in current_storyline.endings.get_list():
                                #         imagebutton:
                                #             if ending.locked:
                                #                 idle "images/info_cards/question_mark_bw.png"
                                #             else: 
                                #                 idle ending.image_file
                                #                 if not tutorial_on:
                                #                     if ending.is_intuition:
                                #                         tooltip str(ending.content + " {image=images/ui/intuition_icon.png}")  
                                #                     else:
                                #                         tooltip str(ending.content)  
                                #                     action SetVariable("action_needed_fix", True) #NOT used but needed for tooltip    
                            
                            vbox:
                                yminimum 120
                                yoffset -20
                                xoffset 50
                                text "Choices & Discoveries":
                                    font gui.name_text_font
                                    color gui.accent_color
                                    size 28
                                
                                hbox:
                                    yoffset 10
                                    spacing 15
                                    $ current_status_checkpoint = Checkpoint(run=current_run, position=current_position, objects=copy.deepcopy(current_storyline.objects.get_unlocked()), observations=copy.deepcopy(current_storyline.observations.get_unlocked()), important_choices=copy.deepcopy(current_storyline.important_choices.get_unlocked()), label_id="current", saved_variables=copy.deepcopy(current_character.saved_variables), ending=False)

                                    imagebutton:
                                        yoffset 2
                                        mouse "hover"
                                        if not tutorial_on and current_character == current_storyline:
                                            action [SetVariable("current_checkpoint", current_status_checkpoint), ShowMenu("progress_details", current_storyline.get_chapter_by_name(current_chapter), current_storyline, is_current=True)]
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
                                            if not tutorial_on and current_character == current_storyline:
                                                action [SetVariable("current_checkpoint", current_status_checkpoint), ShowMenu("progress_details", current_storyline.get_chapter_by_name(current_chapter), current_storyline, is_current=True)]
                                    else:
                                        textbutton "{color=#fff}[unlocked]{/color}/[total]":
                                            text_size 56
                                            text_font gui.name_text_font
                                            text_color gui.accent_color
                                            if not tutorial_on and current_character == current_storyline:
                                                action [SetVariable("current_checkpoint", current_status_checkpoint), ShowMenu("progress_details", current_storyline.get_chapter_by_name(current_chapter), current_storyline, is_current=True)]
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
                            yoffset -20
                            xalign 0
                            for chapter_index, chapter in enumerate(line):
                                if chapter.chapter_type == "image":
                                    imagemap:
                                        idle chapter.image_file
                                elif chapter.chapter_type == "checkpoint":                       
                                    # Precompute once at start of loop over chapters:
                                    $ checkpoints = current_storyline.get_checkpoints_by_chapter(chapter.label)
                                    $ has_checkpoints = bool(checkpoints)
                                    $ is_current = (current_chapter == chapter.name and current_storyline == current_character)
                                    $ is_completed = current_storyline.is_chapter_completed(chapter.name)

                                    # Build a list of tutorial actions if needed:
                                    $ tutorial_actions = []
                                    if not seen_tutorial_progress_details:
                                        $ tutorial_actions = [
                                            SetVariable("tutorial_on", True),
                                            SetVariable("seen_tutorial_progress_details", True),
                                        ]

                                    # Core actions for base and blink (without tutorial vars):
                                    if has_checkpoints:
                                        $ base_core = [ SetVariable("current_checkpoint", checkpoints[0]),
                                                        ShowMenu("progress_details", chapter, current_storyline, is_current=is_current) ]

                                        $ blink_core = [ SetVariable("current_checkpoint", current_status_checkpoint),
                                                        ShowMenu("progress_details", chapter, current_storyline, is_current=is_current) ]

                                        # Prefix tutorial actions when building final action lists:
                                        $ base_action = tutorial_actions + base_core
                                        $ blink_action = tutorial_actions + blink_core

                                    imagemap:
                                        idle chapter.image_file
                                        
                                        if has_checkpoints:
                                            # Determine action_list only once
                                            $ action_list = None
                                            if not tutorial_on:
                                                if is_current:
                                                    $ action_list = blink_action
                                                else:
                                                    $ action_list = base_action
                                            
                                            textbutton chapters_names[chapter.name] style "chapter_button":
                                            # textbutton "An Empty\nManor\nIs for you" style "confirm_prompt":
                                                text_font gui.name_text_font
                                                text_size 28
                                                # xsize 300
                                                if action_list:
                                                    action action_list
                                                # colors
                                                if is_completed:
                                                    text_color gui.insensitive_color
                                                else:
                                                    text_color gui.accent_color
                                                text_hover_color "#FFFFFF"
                                                # blinking transform
                                                if is_current:
                                                    at blink
                                                
                                        else:
                                            textbutton "?" style "chapter_button":
                                                text_font gui.name_text_font
                                                text_size 28
                                                padding (70, 25)
                                                text_color gui.accent_color


                                elif chapter.chapter_type == "ending": 
                                    imagebutton:
                                        if current_storyline.endings.is_unlocked(chapter.label):
                                            idle current_storyline.endings.get_item(chapter.label).image_file
                                            if not tutorial_on:
                                                if current_storyline.endings.get_item(chapter.label).is_intuition:
                                                    tooltip str(current_storyline.endings.get_item(chapter.label).content + " {image=images/ui/intuition_icon.png}") 
                                                else:
                                                    tooltip str(current_storyline.endings.get_item(chapter.label).content)  
                                            # action SetVariable("action_needed_fix", True)
                                            mouse "hover"
                                            if not tutorial_on:
                                                action [SetVariable("current_checkpoint", None), ShowMenu("progress_details", chapter, current_storyline, ending = True)]
                                        else:
                                            idle chapter.image_file 
                                elif chapter.chapter_type == "start": 
                                    imagebutton:
                                        mouse 'hover'
                                        idle image_checkpoint_start
                                        hover image_checkpoint_start_selected
                                        if not tutorial_on:
                                            action [SetVariable("current_checkpoint", None), ShowMenu("progress_details", chapter, current_storyline)]

    use tooltip_display

    use tutorial_with_steps(tutorial_steps_progress, tutorial_step_progress, "tutorial_step_progress")

# ------------------------ TUTORIAL --------------------------------
# -----------------------------------------------
#  Generic tutorial-overlay screen
# -----------------------------------------------
screen tutorial_with_steps(
        tutorial_steps,
        tutorial_step_value,
        tutorial_step_var,
        seen_flag_var=None       # ← optional
    ):

    # -------------------------------------------------
    #  Auto-open only the very first time this screen
    #  is shown during the current play-through
    # -------------------------------------------------
    # if seen_flag_var:
    #     on "show" action If(
    #         "not " + seen_flag_var,            # ← string expression
    #         [                                   # ← actions if it’s still False
    #             SetVariable(seen_flag_var, True),
    #             SetVariable("tutorial_on", True),
    #             SetVariable(tutorial_step_var, 0),
    #         ]
    #     )

    # --------------------------------------------------------------
    #  The normal UI that follows …
    # --------------------------------------------------------------
    fixed:
        yalign 1.0
        yanchor 1.0

        textbutton "Tutorial":
            xpos 20
            ypos 940
            style_prefix "confirm"
            text_size 48
            padding (8, 4)
            action [
                ToggleVariable("tutorial_on"),
                If(tutorial_on, SetVariable(tutorial_step_var, 0), NullAction())
            ]

        if tutorial_on:

            $ keep_x, keep_y, keep_w, keep_h, tx, ty, msg = tutorial_steps[tutorial_step_value]
            $ sw, sh = config.screen_width, config.screen_height
            $ keep_r = keep_x + keep_w
            $ keep_b = keep_y + keep_h

            fixed:
                add Solid("#000B") xpos 0      ypos 0      xsize sw         ysize keep_y
                add Solid("#000B") xpos 0      ypos keep_b xsize sw         ysize sh - keep_b
                add Solid("#000B") xpos 0      ypos keep_y xsize keep_x     ysize keep_h
                add Solid("#000B") xpos keep_r ypos keep_y xsize sw-keep_r  ysize keep_h

                frame:
                    style_prefix "confirm"
                    xpos tx ypos ty
                    padding (30, 30)

                    vbox:
                        xalign .5
                        yalign .5

                        label msg:
                            style "confirm_prompt"
                            text_size 24
                            xalign 0.5

                        hbox:
                            xalign .5
                            spacing 12
                            if tutorial_step_value > 0:
                                textbutton "« Prev" action SetVariable(tutorial_step_var,
                                                                        tutorial_step_value - 1)
                            if tutorial_step_value < len(tutorial_steps) - 1:
                                textbutton "Next »" action SetVariable(tutorial_step_var, tutorial_step_value + 1)
                            else:
                                textbutton "Close" action [
                                    SetVariable("tutorial_on", False),
                                    SetVariable(tutorial_step_var, 0)
                                ]
                        

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
                # tooltip item.content # Use this line to debug infocards
            elif not locked: 
                idle "images/info_cards/" + item.image_file + ".png"     
                tooltip icon_file + item.content
            else:
                idle "images/info_cards/" + item.image_file + "_bw.png"                                
                tooltip icon_file + item.content_negative


screen progress_details(selected_chapter, selected_char, ending = False, is_current = False):

    #     on "show" action SetVariable("current_checkpoint", None)
    # on "show" action If(
    #         "not " + seen_flag_var,            # ← string expression
    #         [                                   # ← actions if it’s still False
    #             SetVariable(seen_flag_var, True),
    #             SetVariable("tutorial_on", True),
    #             SetVariable(tutorial_step_var, 0),
    #         ]
    #     )

    on "show" action SetVariable("tutorial_on", True),

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
                
                vbox:
                    spacing 10
                    yalign 0.0
                    xoffset 100

                    if ending:
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
                            # TODO CHECK it's working without start
                            if selected_chapter.chapter_type == "start":
                                textbutton str("Start"):                                    
                                    xoffset 20
                                    action SetVariable("current_checkpoint", current_storyline.get_init_checkpoint())
                            else:
                                vbox:
                                    xoffset 20
                                    yminimum 70
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

                                        textbutton str("Current Status"):
                                            xpadding 0
                                            ypadding 0
                                            xmargin 0
                                            ymargin 0
                                            text_size 42
                                            if current_checkpoint and current_checkpoint.label_id == "current":
                                                text_color gui.accent_color
                                            # else:                                            
                                            #     text_color gui.highlight_color at blink
                                            action SetVariable("current_checkpoint", active_checkpoint)

                                    for i, checkpoint in enumerate(selected_char.get_checkpoints_by_chapter(selected_chapter.label)):

                                            textbutton "{} - {}".format(i, checkpoint.get_format_created()):
                                                xpadding 0
                                                ypadding 0
                                                xmargin 0
                                                ymargin 0
                                                action SetVariable("current_checkpoint", checkpoint)
                                                if current_checkpoint == checkpoint:
                                                    text_color gui.accent_color
                                            hbox:
                                            # NOw gets all the choices activated for this checkpoint
                                                for item in current_storyline.get_choices_and_discoveries_by_chapter(selected_chapter.name):
                                                    if item.text_id in checkpoint.get_activated_choices_and_discoveries():
                                                        use info_card(item, item.type, True)
                    if current_checkpoint and not ending and not current_checkpoint.label_id == "current" and seen_tutorial_restart:
                        button:
                            xoffset 5
                            action Show("confirm_restart")
                            background "images/ui/button_idle_small.png"
                            hover_background "images/ui/button_hover_small.png"
                            xysize (430, 65)
                            text "Restart from there":
                                color "#FFFFFF"
                                align (0.5, 0.5)
                    else:
                        button:
                            xoffset 5
                            background "images/ui/button_idle_small.png"
                            hover_background "images/ui/button_hover_small.png"
                            xysize (430, 65)
                            text "Restart from there":
                                color "#585353"
                                align (0.5, 0.5)

                # Right column: Details of the selected checkpoint
                vbox:
                    spacing 10
                    yalign 0.0
                    xoffset 100
                    xminimum 650

                    if current_checkpoint and selected_chapter.chapter_type != "start":

                        if current_checkpoint.label_id == "current":
                            text "Previous Choices & Discoveries":
                                font gui.name_text_font
                                size 42
                                color gui.accent_color
                        else:
                            text "Previous Choices & Discoveries":
                                font gui.name_text_font
                                size 42
                                color gui.accent_color

                        vbox:
                            yoffset 20
                            $ number_of_rows = ((len(current_storyline.get_choices_and_discoveries_by_chapter(selected_chapter.name, current_checkpoint.label_id == "current")) + 5) // 6)
                            grid 6 number_of_rows:
                                spacing 13
                                for item in current_storyline.get_choices_and_discoveries_by_chapter(selected_chapter.name, current_checkpoint.label_id == "current"):
                                    use info_card(item, item.type)

                        # TODO: Decide if we want to see all the time or just current status?
                        if current_checkpoint.label_id == "current" or True:
                            text "Choices & Discoveries for this Chapter":
                                yoffset 20
                                font gui.name_text_font
                                size 42
                                color gui.accent_color
                            
                            vbox:
                                yoffset 20
                                $ number_of_rows = ((len(current_storyline.get_choices_and_discoveries_by_chapter_only_current(selected_chapter.name)) + 5) // 6)
                                grid 6 number_of_rows:
                                    spacing 13
                                    for item in current_storyline.get_choices_and_discoveries_by_chapter_only_current(selected_chapter.name):
                                        use info_card(item, item.type)
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

    use tutorial_with_steps(tutorial_steps_progress_details, tutorial_step_progress_details, "tutorial_step_progress_details", "seen_tutorial_progress_details")


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