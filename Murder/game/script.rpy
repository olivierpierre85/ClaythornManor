# The script of the game goes in this file.
# Global Variable

# CLOCK
init -100 python:
    from datetime import datetime, time, timedelta, date
    renpy.music.register_channel("clock", "sfx", loop=False)

# TODO move to init var ? Sort it out
define time_left = 0
define current_day = "Friday"
define current_time = time(17,00,00)
define hours_angle = 0
define old_minutes_angle = 0 

define current_year = "1924"

# The game starts here.
label start():

    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "manor_map"

    call init_variables

    call init_characters

    call init_storylines

    call  init_map

    show screen current_time

    show screen in_game_menu_btn
    
    # Debug Menu # TODO remove when prod
    jump debug_choices

    # These display lines of dialogue.
    jump character_selection

    return

label init_variables:
    python:
        # Technical Variables
        test_mode = False

        if test_mode:
            f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/choices_history.txt", "a")
            f.write("NEW GAME\n-----------\n")
            f.close()

        # Story Variables
        lad_day1_evening_billiard_room_visited = False
        lad_day1_drinks = 0
        lad_day1_poisoned = False

        lad_visited_library = False
        lad_day2_breakfast_follow = False
        lad_day2_hunt = False

        TIME_MAX = 999999

    return