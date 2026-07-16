# progress_details.rpy - per-chapter detail view opened from the storyline (progress) screen.
# Split out of progress.rpy. Shared helpers (info_card, tooltip_display,
# tutorial_with_steps, Chapter/Checkpoint classes) remain in progress.rpy.

screen progress_details(selected_chapter, selected_char, ending = False, is_current = False):

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
                                                saved_variables = copy_saved_variables(current_character.saved_variables),
                                                ending = ending,
                                                menus_state = capture_all_menus_state(),
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

                    # Hidden character information unlockable in this chapter,
                    # shown even when no checkpoint is selected
                    if not ending:
                        $ hidden_pairs = selected_char.get_hidden_infos_by_chapter(selected_chapter.name)
                        $ hidden_total = len(hidden_pairs)
                        $ hidden_done = len([info for owner, info in hidden_pairs if not info.locked])

                        if hidden_total > 0:
                            text "{}/{} Backstory in this chapter".format(hidden_done, hidden_total):
                                yoffset 0
                                font gui.name_text_font
                                size 42
                                color gui.accent_color
                                # color (gui.insensitive_color if hidden_done == hidden_total else gui.accent_color)
                        else:
                            text "No Backstory in this chapter":
                                yoffset 0
                                font gui.name_text_font
                                size 42
                                color gui.accent_color

                        # Breathing room before the next section title
                        null height 25

                    if current_checkpoint and selected_chapter.chapter_type != "start":

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
