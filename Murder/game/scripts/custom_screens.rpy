screen current_time:
    modal False

    # python:
    #     current_hour = current_time.hour
    #     current_minutes = current_time.minute
    #     extra_hour_rotation = 0
    #     if current_hour >= 12:
    #         current_period = "PM"
    #         extra_hour_rotation += 1
    #     else:
    #         current_period = "AM"
        
    #     if current_day == "Saturday":
    #         extra_hour_rotation += 2
    #     elif current_day == "Sunday":
    #         extra_hour_rotation += 4

    #     hours_angle = (360 * extra_hour_rotation) + ((int(current_hour) * 60) + int(current_minutes))/2
    #     print(hours_angle)
        
    #     minutes_angle = int(current_minutes) * 6
    
    # Terrible quickfix to force clockwise rotation... (constant) TODO  replace???
    # python:
    #     while old_minutes_angle > minutes_angle:
    #         minutes_angle = minutes_angle + 360

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

    # needle
    add "images/ui/clock_hours.png" at rotate_hours(hours_angle)
    add "images/ui/clock_minutes.png" at rotate_minutes(minutes_angle)

    # $ old_minutes_angle = minutes_angle
        
transform rotate_hours( angle = 0 ):
    xoffset -16
    yoffset 1
    linear 3.0 rotate angle 

transform rotate_minutes( angle = 0 ):
    xoffset -16
    yoffset 1 
    linear 3.0 rotate angle 

# BLACK transition
label black_screen_transition(display_text, display_text_2 = None):
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