# The script of the game goes in this file.
# Global Variable

# CLOCK
init -1000 python:
    from datetime import datetime, time, timedelta, date
    import copy

    renpy.music.register_channel("clock", "sfx", loop=False)
    current_music = 'NONE'
    current_start_song = 1

# TODO move to init var? Sort it out
define time_left = 0
define hours_angle = 0

define current_year = "1924"

# The game starts here.
label start():

    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "manor_map"

    call init_technical_variables

    call init_map

    call init_story_variables

    call init_characters

    
    # Debug Menu # TODO remove when prod
    jump debug_choices

    # These display lines of dialogue.
    jump character_selection

    return

label init_technical_variables:
    
    define config.mouse = { }
    define config.mouse['default'] = [ ( "images/ui/default-cursor-icon.png", 4, 0) ]
    define config.mouse['hover'] = [ ( "images/ui/hover-cursor-icon.png", 13, 0) ]
    python:
        # Technical Variables
        # TODO delete those in character select AND start again
        record_mode = False
        full_testing_mode = False

        show_minutes_movement = 0
        show_hours_movement = 0
        skip_clock_movement = True

        if record_mode:
            f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/choices_history.txt", "a")
            f.write("NEW GAME\n-----------\n")
            f.close()

        TIME_MAX = 999999
        TIME_LOW = 5

        current_room = "outside"
        seen_tutorial_knowledge = False
        seen_tutorial_map = False
        seen_tutorial_unlock_character = False
        seen_tutorial_timeline = False

        current_run = 1 # TODO move
        current_position = 0 # TODO move

        has_been_restarted = False

        first_death = True
        first_survive = True

        current_checkpoint = None

        action_needed_fix = False # Use to have a valid action that does nothing

        # Conditions for menu shortcuts
        condition_saturday_morning = "(current_day == 'Saturday' and current_phase == 'Morning')"
        condition_saturday_morning_or_hunt = "(current_day == 'Saturday' and (current_phase == 'Morning' or current_phase == 'Hunt'))"
        condition_saturday_hunt = "(current_day == 'Saturday' and current_phase == 'Hunt')"
        condition_saturday_evening = "(current_day == 'Saturday' and current_phase == 'Evening')"
        condition_saturday = "current_day == 'Saturday'"
        condition_friday = "current_day == 'Friday'"
        condition_sunday = "current_day == 'Sunday'"
        

    return

label init_story_variables:

    call init_lad
    call init_psychic
    call init_captain
    
    return