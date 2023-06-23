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
        pause 3.0
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
            font gui.name_text_font
            size gui.name_text_size
        if display_text_2:
            text display_text_2:
                xalign 0.5 
                yalign 0.5
                yoffset 20
                font gui.name_text_font
                size gui.name_text_size

screen in_game_menu_btn:

    modal False

    zorder 1000

    style_prefix "confirm" # TODO use own style
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        ypadding 10
        textbutton _("Menu") action ShowMenu("manor_map")

# simple empty
label generic_cancel:
    return