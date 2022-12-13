# The script of the game goes in this file.
# Global Variable

# CLOCK
init -1000 python:
    from datetime import datetime, time, timedelta, date
    renpy.music.register_channel("clock", "sfx", loop=False)
    current_music = 'upbeat'

# TODO move to init var ? Sort it out
define time_left = 0
define hours_angle = 0
define old_minutes_angle = 0 

define current_year = "1924"

# The game starts here.
label start():

    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "manor_map"

    call init_technical_variables

    call init_map

    call init_story_variables # TODO put at each loop

    call init_characters

    call init_storylines


    show screen current_time

    show screen in_game_menu_btn
    
    
    # Debug Menu # TODO remove when prod
    jump debug_choices


    # These display lines of dialogue.
    jump character_selection

    return

label init_technical_variables:
    python:
        # Technical Variables
        test_mode = False

        if test_mode:
            f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/choices_history.txt", "a")
            f.write("NEW GAME\n-----------\n")
            f.close()

        TIME_MAX = 999999

        current_room = "outside"
        seen_tutorial_unlock_knowledge = False

        current_music = 'upbeat'

        first_death = True

    return

label init_story_variables:

    call init_lad
    
    return