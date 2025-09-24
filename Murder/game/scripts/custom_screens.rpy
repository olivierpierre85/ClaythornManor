screen current_time:
    modal False

    image "images/ui/clock_small.png":
        xoffset 30
        yoffset 20

    # DAYS
    style_prefix "clock"
    frame:
        xalign 0.0
        yalign 0.0
        xoffset 94
        yoffset 155
        ypadding 2
        xpadding 4
        # Todo get PHASE?
        text current_day[:3].upper() + ", " + current_period:
            size 16
            color gui.choice_button_text_insensitive_color
            font gui.clock_text_font
            bold True

    add "images/ui/clock_hours.png" at rotate_hours(hours_angle)
    add "images/ui/clock_minutes.png" at rotate_minutes(minutes_angle)


transform rotate_hours( angle = 0 ):
    xoffset -16
    yoffset 1
    linear show_hours_movement rotate angle 

transform rotate_minutes( angle = 0 ):
    xoffset -16
    yoffset 1 
    linear show_minutes_movement rotate angle 

# WAIT in the same room
label wait_screen_transition():
    
    scene black_background with dissolve

    pause 1

    $ renpy.scene()
    $ renpy.show(current_room)
    $ renpy.with_statement(dissolve)

    return 

# BLACK transition
label black_screen_transition(display_text, display_text_2 = None):
    if not full_testing_mode:
        scene black_background with irisin
        show screen centered_text(display_text, display_text_2)
        play sound gong
        pause 4.0
        hide screen centered_text
    return 


# Death transition
label death_screen_transition:
    hide screen current_time
    hide screen in_game_menu_btn

    scene black_background with wipedown
    show screen centered_text("You are Dead")
    play sound gong
    pause 5.0
    
    return

label survive_screen_transition:
    scene black_background with wipeup
    show screen centered_text("You Survived")
    play sound gong
    pause 5.0

    return

screen centered_text(display_text, display_text_2 = None):
    vbox:
        xalign 0.5 
        yalign 0.5
        text display_text:
            xalign 0.5 
            yalign 0.5
            font gui.transition_top_text_font
            size gui.transition_top_text_size
        if display_text_2:
            text display_text_2:
                xalign 0.5 
                yalign 0.5
                yoffset 20
                font gui.transition_bottom_text_font
                size gui.transition_bottom_text_size

screen in_game_menu_btn:
    modal False
    zorder 1000
    style_prefix "confirm"  # TODO use own style
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        ypadding 0
        xpadding 0
        textbutton _("Menu") action ShowMenu(last_menu_screen):
            xminimum 200  # Adjust these values as needed
            yminimum 80

screen debug_screen:
    modal False
    zorder 1000
    style_prefix "confirm"  # TODO use own style
    frame:
        xalign 0.0
        yalign 1.0
        xoffset 0
        yoffset 0
        ypadding 0
        xpadding 0
        textbutton "Time left:" + str(time_left) + "\nChapter:" + current_chapter:
        # textbutton "Time left:" + str(time_left) + "\nChapter:" + current_chapter + "\nSubmenu(nurse_generic_menu_psychic):" + str(all_menus['nurse_generic_menu_psychic'].choices[6].is_valid()) :
            # action Function(export_choices_to_file, all_choices)
            action Function(save_transcript_to_file)
            xminimum 200  # Adjust these values as needed
            yminimum 80
            text_size 18

# simple empty
label generic_cancel:
    return

screen custom_key_listener():
    # Replace the standard call to menu with one with the latest screen as parameter
    key "K_ESCAPE" action ShowMenu(last_menu_screen)
    key "K_MENU" action ShowMenu(last_menu_screen)
    key "K_PAUSE" action ShowMenu(last_menu_screen)
    key "mouseup_3" action ShowMenu(last_menu_screen)
    # Todo Explain the shortcuts in the tutorial?
    key "K_m" action [SetVariable("last_menu_screen", "manor_map"), ShowMenu("manor_map")]
    key "K_p" action [SetVariable("last_menu_screen", "progress"), ShowMenu("progress")]
    key "K_c" action [SetVariable("last_menu_screen", "characters"), ShowMenu("characters")]
    

# The standard choice menu is replaced with this one to be able to make easy changes to menu
screen custom_choice(custom_menu):

    style_prefix "choice"

    vbox:
        for idx, choice in enumerate(custom_menu.choices):

            if choice.is_valid():

                # Add the icons based on markers
                if "{{intuition}}" in choice.text:
                    $ btn_text = choice.text.replace("{{intuition}}", "") + " {image=images/ui/intuition_icon.png}"
                elif "{{observation}}" in choice.text:
                    $ btn_text = choice.text.replace("{{observation}}", "") + " {image=images/ui/observation_icon.png}"
                elif "{{object}}" in choice.text:
                    $ btn_text = choice.text.replace("{{object}}", "") + " {image=images/ui/objects_icon.png}"
                else:
                    $ btn_text = choice.text

                if choice.is_already_chosen():
                    textbutton btn_text:
                        mouse "hover"
                        action Return(idx)
                        text_color gui.insensitive_color
                else:
                    textbutton btn_text:
                        mouse "hover" 
                        action Return(idx)


transform blink_skip:
    alpha 1.0
    linear 0.5 alpha 0.25
    linear 0.5 alpha 1.0
    repeat

screen skip_hint():
    # Show only if:
    #   – this line has been seen before
    if renpy.is_seen() or show_skip_hint_for_tutorial:
        add "images/ui/skip_button.png" at blink_skip align (0.15, 0.4)   # top‑right
