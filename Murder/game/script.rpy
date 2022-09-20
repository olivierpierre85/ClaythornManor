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

define menus_options = dict()

define current_character = "lad"

define current_floor = 1 # 1 Equal ground floor, 0 is kitchen floor
define tooltip = "Click on a room to move there"
define MIN_FLOOR = 0
define MAX_FLOOR = 1 # TODO Add floors

# The game starts here.
label start():

    call init_characters

    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "manor_map"

    $ characters_knowledge['psychic'] = set() #TODO reset all
    $ map_info = dict()
    $ map_info['lad_room'] = True
    $ map_info['psychic_room'] = True

    $ test_mode = False

    show screen current_time

    show screen in_game_menu_btn
    
    # Debug Menu # TODO remove when prod
    jump debug_choices

    # These display lines of dialogue.
    jump character_selection

    return
