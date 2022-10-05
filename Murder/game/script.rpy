# The script of the game goes in this file.
# Global Variable

# CLOCK
init -100 python:
    from datetime import datetime, time, timedelta, date
    renpy.music.register_channel("clock", "sfx", loop=False)

define time_left = 0
define current_day = "Friday"
# define current_time = "05:00PM" 
define current_time = time(17,00,00)
define hours_angle = 0
define old_minutes_angle = 0 

define current_year = "1924"

define menus_options = dict()

# The game starts here.
label start():

    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "manor_map"

    # TODO SOME INIT should be reset at character selection, check which ones

    call init_characters

    call init_storylines

    call  init_map

    $ test_mode = False

    show screen current_time

    show screen in_game_menu_btn
    
    # Debug Menu # TODO remove when prod
    jump debug_choices

    # These display lines of dialogue.
    jump character_selection

    return
