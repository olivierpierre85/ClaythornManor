# The script of the game goes in this file.
# Global Variable

# CLOCK
init -1000 python:
    from datetime import datetime, time, timedelta, date
    import copy
    import textwrap
    import re
    import itertools

    import endings_conditions

    renpy.music.register_channel("clock", "sfx", loop=False)
    current_music = 'NONE'
    current_start_song = 1


# Var needed BEFORE start
default debug_activated = False
# default persistent.not_already_chosen = {}

# My config variables

# Autosave not Working (probably because of complicated transitions)
# so I deactivated it an replaced with quicksave button (and after change time)
define config.has_autosave = True
define config.autosave_on_choice = True
define config.autosave_on_quit = False

# define config.default_fullscreen = True # TODO activate for DEMO
# define config.rollback_enabled = False # TODO activate for DEMO

# TODO move to init var? Sort it out
default  time_left = 0
default  hours_angle = 0

define current_year = "1924"

# var needed for imbricated menus choices
# default  menu_level = -1
# default  selected_choice = [None, None, None, None, None]
# default  time_diff = [None, None, None, None, None]

label start_debug:

    $ debug_activated = True

    jump start

# The game starts here.
label start():

    default  menu_level = -1
    default  selected_choice = [None, None, None, None, None]
    default  time_diff = [None, None, None, None, None]

    call init_technical_variables

    call init_map

    call init_story_variables

    call init_characters

    show screen in_game_menu_btn
    show screen custom_key_listener

    # INIT first character
    $ current_character = lad_details
    $ current_storyline = lad_details # TODO move

    # TODO: Implement full_testing_mode 
    $ full_testing_mode = False
    $ full_testing_mode_char = "lad"
    $ decision_tree = []

    if debug_activated:
        call init_debug

        # These display lines of dialogue.
        jump character_selection
    else:
        # Could be useful but NEEDS a warning, because it will delete all the saves as well?
        # Delete all persistent data (choices alreay made,....)
        # $ persistent._clear(progress=True)

        jump lad_introduction

    return

label init_technical_variables:
    
    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "preferences"
    default last_menu_screen = "preferences"

    # NAME OF CHAPTERS
    define chapters_names = {
        'friday_afternoon': "The Arrival",
        'friday_evening': "The First Dinner",
        'saturday_morning': "The Morning Surprise",
        'saturday_afternoon': "The Hunt",
        'saturday_afternoon_no_hunt': "No Hunt",
        'saturday_evening': "Things get Darker",
        'sunday_morning': "The Empty Manor",
        'sunday_afternoon': "Final Decisions",
    }

    default current_chapter = "friday_afternoon"

    define config.mouse = { }
    define config.mouse['default'] = [ ( "images/ui/default-cursor-icon.png", 4, 0) ]
    define config.mouse['hover'] = [ ( "images/ui/hover-cursor-icon.png", 13, 0) ]
    python:
        # Technical Variables

        all_menus = {}

        # TODO delete those in character select AND start again
        record_mode = False

        hide_notifications = False

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
        previous_room = "outside"
        seen_tutorial_clock = False
        seen_tutorial_description_hidden = False
        seen_tutorial_map = False
        seen_tutorial_unlock_character = False
        show_tutorial_unlock_character = False
        seen_tutorial_progress = False
        seen_tutorial_restart = False
        seen_tutorial_intuition = False

        current_run = 1 # TODO move
        current_position = 0 # TODO move

        has_been_restarted = False

        is_death = True # Assume the ending is a death, unless written otherwise
        first_ending = True
        first_survive = True

        current_checkpoint = None
        current_day = None

        action_needed_fix = False # Use to have a valid action that does nothing

        # Conditions for menu shortcuts
        condition_saturday_morning = "(current_day == 'Saturday' and current_phase == 'Morning')"
        condition_saturday_morning_or_hunt = "(current_day == 'Saturday' and (current_phase == 'Morning' or current_phase == 'The Hunt' or current_phase == 'No Hunt'))"
        condition_saturday_hunt = "(current_day == 'Saturday' and (current_phase == 'The Hunt' or current_phase == 'No Hunt'))"
        condition_saturday_evening = "(current_day == 'Saturday' and current_phase == 'Evening')"
        condition_saturday = "current_day == 'Saturday'"
        condition_friday = "current_day == 'Friday'"
        condition_friday_or_saturday = "current_day == 'Friday' or current_day == 'Saturday'"
        condition_sunday = "current_day == 'Sunday'"

        # Image for progress view
        image_checkpoint = "images/ui/progress/rectangle_progress.png"
        image_checkpoint_right = "images/ui/progress/rectangle_progress_right.png"          
                          
        image_checkpoint_start = "images/ui/progress/rectangle_small.png"
        image_checkpoint_start_empty = "images/ui/progress/rectangle_small_empty.png"
        image_checkpoint_start_selected = "images/ui/progress/rectangle_small_selected.png"
        image_checkpoint_start_corner = "images/ui/progress/rectangle_small_corner.png"
        image_checkpoint_start_line = "images/ui/progress/rectangle_small_line.png"
        image_checkpoint_start_double_corner = "images/ui/progress/rectangle_small_double_corner.png"

        image_checkpoint_straight_line ="images/ui/progress/rectangle_progress_straight_line.png"
        image_checkpoint_three_sides ="images/ui/progress/rectangle_progress_three_sides.png"

        # Fillers
        image_checkpoint_empty = "images/ui/progress/rectangle_progress_empty.png"
        image_checkpoint_empty_small = "images/ui/progress/rectangle_small_empty.png"
        image_checkpoint_empty_after_ending = "images/ui/progress/rectangle_filler_empty.png"

        image_checkpoint_corner = "images/ui/progress/rectangle_progress_corner.png"
        image_checkpoint_corner_merge = "images/ui/progress/rectangle_progress_corner_merge.png"          
        image_checkpoint_double_corner = "images/ui/progress/rectangle_progress_double_corner.png"
        image_checkpoint_line = "images/ui/progress/rectangle_progress_line.png"

        # Endings
        image_ending_question = "images/info_cards/question_mark_bw.png"

    return

label init_story_variables:

    call init_lad
    call init_psychic
    call init_captain
    call init_nurse
    call init_doctor
    call init_host
    call init_broken
    call init_drunk
    
    return

