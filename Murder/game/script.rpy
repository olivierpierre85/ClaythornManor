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

    call init_characters

    call init_storylines

    call  init_map

    show screen current_time

    show screen in_game_menu_btn
    
    call init_story_variables # TODO put at each loop
    
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
        seen_tutorial_add_knowledge = False

        current_music = 'upbeat'

    return

label init_story_variables:
    python:
        current_day = "Friday"
        current_time = time(17,00,00)

        # Lad Variables
        lad_day1_evening_billiard_room_visited = False
        lad_day1_drinks = 0
        lad_day1_poisoned = False

        lad_visited_library = False
        lad_day2_breakfast_follow = False
        lad_day2_hunt = False
        lad_day3_morning_captain_found = False
        lad_day3_gun_downed = False
        lad_day3_poisoned = False
    
    return