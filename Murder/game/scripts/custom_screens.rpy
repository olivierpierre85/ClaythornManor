screen current_time:
    modal False

    # Clock Background
    image "images/ui/clock/clock_2_small_new.png":
        xoffset 30
        yoffset -40

    # Clock Needles
    add "images/ui/clock/clock_hours.png" at rotate_hours(hours_angle)
    add "images/ui/clock/clock_minutes.png" at rotate_minutes(minutes_angle)

    # Plaque with texts
    frame:
        background "images/ui/clock/clock_plaque.png"
        xoffset 55
        yoffset 180
        # Picture Above plaque
        # xoffset 215
        # yoffset 130
        xsize 150

        text current_day.upper() + ", " + current_period:
            xalign 0.5
            yoffset 10
            size 16
            color gui.clock_plaque_text_color
            font gui.clock_text_font
            bold True

        text current_character.real_name:
            xalign 0.5
            yoffset 45
            size 16
            color gui.clock_plaque_text_color
            font gui.clock_text_font
            bold True

    # Add current player face
    # image "images/characters/side/side " + current_character.text_id + ".png" at character_progress:
        # Right below Looks weird
        # xoffset 77
        # yoffset 280
        # Right to clock, looks weird
        # xoffset 220
        # yoffset 30
        # below left, looks weird
        # yalign 1.0
        # yoffset -100
        # xoffset 70
        # Picture Above plaque
        # xoffset 237
        # yoffset 20



transform rotate_hours( angle = 0 ):
    xoffset -16
    yoffset -55
    linear show_hours_movement rotate angle 

transform rotate_minutes( angle = 0 ):
    xoffset -16
    yoffset -55
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
        # textbutton "Time left:" + str(time_left) + "\nChapter:" + current_chapter + "\nSubmenu(nurse_generic_other_guests_menu):" + str(all_menus['nurse_generic_menu_doctor'].choices[6].already_chosen) :
            # action Function(export_choices_to_file, all_choices)
            action Function(export_transcript)
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
                
                if not seen_tutorial_icon and "image=images" in btn_text:
                    $ btn_text = btn_text + "\n{color=#DBB100}{font=gui/font/Redressed.ttf}{i} (Tutorial) An icon means this choice is dependant on previous choices{/i}{/font}{/color}"

                if choice.is_already_chosen():
                    textbutton btn_text:
                        mouse "hover"
                        if not seen_tutorial_already_chosen:
                            action [ SetVariable("show_tutorial_already_chosen", True), Return(idx) ]
                        else:
                            action Return(idx)
                        text_color gui.insensitive_color
                else:
                    if not seen_tutorial_icon and "image=images" in btn_text:
                        textbutton btn_text:
                            mouse "hover" 
                            action [ SetVariable("seen_tutorial_icon", True), Return(idx) ]
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


# Drunk Mode
init python:
    # Base drunk text style derived from say dialogue.
    style.drunk_dialogue = Style(style.say_dialogue)
    # Slightly larger for readability when wobbling.
    style.drunk_dialogue.size = style.say_dialogue.size + 1

    # Faux-blur: multiple soft outlines in the same color with low alpha.
    # (Adjust for your theme; these assume light text on dark window.)
    style.drunk_dialogue.outlines = [
        (1, "#FFFFFF40", 0, 0),
        (2, "#FFFFFF30", 0, 0),
        (3, "#FFFFFF20", 0, 0),
    ]

# Replace your wobble with this one.
transform drunk_wobble_layer:
    subpixel True

    # Place the layer’s CENTER on the screen’s CENTER
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5  # (typo-proofing below; keep yanchor)
    yanchor 0.5

    # Rotate/offset around that center and overscan to hide edges
    zoom 1.10
    parallel:
        linear 1.2 xoffset 6 yoffset -3
        linear 1.2 xoffset -6 yoffset 3
        repeat
    parallel:
        linear 1.3 rotate 1.2
        linear 1.3 rotate -1.2
        repeat

transform drunk_text_wobble:
    subpixel True
    # Much gentler than the scene wobble
    parallel:
        linear 0.7 xoffset 2
        linear 0.7 xoffset -2
        repeat
    parallel:
        linear 1.0 yoffset -1
        linear 1.0 yoffset 1
        repeat