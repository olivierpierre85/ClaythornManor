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



define current_floor = 1 # 1 Equal ground floor, 0 is kitchen floor
define tooltip = "Click on a room to move there"
define MIN_FLOOR = 0
define MAX_FLOOR = 2 # TODO Add floors

# The game starts here.
label start():

    # TODO SOME INIT should be reset at character selection, check which ones

    call init_characters

    $ current_character = lad_details

    call init_storylines

    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "manor_map"

    # TODO move to a map SCRIPT page
    $ map_info = dict()
    $ map_info['lad_room'] = False
    $ map_info['psychic_room'] = False

    $ test_mode = False

    show screen current_time

    show screen in_game_menu_btn
    
    # Debug Menu # TODO remove when prod
    jump debug_choices

    # These display lines of dialogue.
    jump character_selection

    return
