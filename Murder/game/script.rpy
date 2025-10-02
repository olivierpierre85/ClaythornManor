# The script of the game goes in this file.
# Global Variable

# CLOCK
init -1000 python:
    from datetime import datetime, time, timedelta, date
    import copy
    import textwrap
    import re
    import itertools
    import sys, json, base64
    import uuid
    import os, io, glob
    import logging

    from typing import List, Tuple

    import endings_conditions

    renpy.music.register_channel("clock", "sfx", loop=False)
    current_music = 'NONE'
    current_start_song = 1

    # ADD function to renpy error handling
    def dump_state(short_tb, full_tb, tb_file):
        """
        • short_tb  → traceback trimmed to your script files
        • full_tb   → full traceback (engine + your code)
        • tb_file   → path to a .txt file Ren'Py already wrote
        """

        export_choices_to_file(all_choices)

        return False

    # Useful to track error when pickling (on save)
    def scan_pickle():
        bad = []
        for name, val in renpy.store.__dict__.items():
            # direct file objects
            if isinstance(val, io.TextIOWrapper):
                bad.append((name, type(val).__name__, "DIRECT FILE"))
            # logging.FileHandler or anything with .stream
            try:
                if hasattr(val, "stream") and isinstance(val.stream, io.TextIOWrapper):
                    bad.append((name, type(val).__name__, "HAS .stream FILE"))
            except Exception:
                pass
            # logger objects holding file handlers
            if isinstance(val, logging.Logger):
                for h in val.handlers:
                    if getattr(h, "stream", None) and isinstance(h.stream, io.TextIOWrapper):
                        bad.append((name, "logging.Logger", "LOGGER FILEHANDLER"))
        for item in bad:
            renpy.log("UNPICKLEABLE: {}".format(item))
        return bad

    def load_latest_choices_from_testing():
        base = renpy.config.basedir
        folder = os.path.join(base, "testing_paths")
        files = glob.glob(os.path.join(folder, "*.json"))
        if not files:
            return None, []

        latest_file = max(files, key=os.path.getmtime)
        with open(latest_file, "r", encoding="utf-8") as fh:  # use fh, not f
            data = json.load(fh)

        choices = data.get("choices", [])
        return choices

define config.exception_handler = dump_state

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

    stop music fadeout 2.0 # Stops menu music

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
    python: 
   

        full_testing_mode = False
        full_testing_mode_char = "lad"
        full_testing_mode_choices = None

        # Load latest path file for test
        if full_testing_mode:
            full_testing_mode_choices = load_latest_choices_from_testing()
            print(full_testing_mode_choices)


    if debug_activated:
        call init_debug

        # These display lines of dialogue.
        jump character_selection
    else:

        jump lad_introduction

    return

label init_technical_variables:
    
    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "preferences"
    default last_menu_screen = "preferences"

    # NAME OF CHAPTERS
    define chapters_names = {
        'friday_afternoon': "Introduction",
        'friday_evening': "The Arrival",
        'saturday_morning': "A Shocking Morning",
        'saturday_afternoon': "The Hunt",
        'saturday_afternoon_no_hunt': "No Hunt",
        'saturday_evening': "Things Get Darker",
        'sunday_morning': "Exploration",
        'sunday_afternoon': "Final Decisions",
        'end': "Ending"
    }

    define chapter_index = {
        'friday_afternoon': 0,
        'friday_evening': 1,
        'saturday_morning': 2,
        'saturday_afternoon': 3,
        'saturday_afternoon_no_hunt': 3,
        'saturday_evening': 4,
        'sunday_morning': 5,
        'sunday_afternoon': 6,
        'end': 7
    }

    default current_chapter = "friday_afternoon"

    define config.mouse = { }
    define config.mouse['default'] = [ ( "images/ui/default-cursor-icon.png", 4, 0) ]
    define config.mouse['hover'] = [ ( "images/ui/hover-cursor-icon.png", 13, 0) ]

    python:
        # Technical Variables
        all_menus = {}
        all_choices = []

        hide_notifications = False

        show_minutes_movement = 0
        show_hours_movement = 0
        skip_clock_movement = True

        show_skip_hint_for_tutorial = False

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
        seen_tutorial_progress_details = False
        seen_tutorial_restart = False
        seen_tutorial_intuition = False

        # ─────── tutorial data (fractions of the screen) ───────
        #         keep_x  keep_y  keep_w  keep_h   txt_x  txt_y   message
        # PROGRESS TUTORIAL
        tutorial_steps_progress = [
            (17, 294, 1020, 140, 550, 525, "Here you can select the character whose progress you wish to view.\nOnly characters that have been unlocked are selectable."),
            (1050, 290, 566, 140, 1300, 525, "Here are the endings you have already reached for this character."),
            (1630, 290, 280, 140, 1300, 400, "You can see the total number of Choices and Discoveries\nyou have already encountered here."),
            (17, 445, 1890, 500, 1000, 300, 
            "Below is the timeline of the progress you have made so far.\n" +
            "The story is split into chapters occurring over three days."
            ),
            (17, 445, 1890, 500, 1000, 300, 
            "A question mark means you have not reached this chapter before.\n" + 
            "If there is nothing more to discover in a chapter, it will be written in yellow."
            ),
            (17, 445, 1890, 500, 1000, 300,           
            "You can view the details of a particular chapter by clicking on it.\n" +
            "To check which options have been unlocked at the moment, \n" + 
            "try selecting the chapter that is blinking (after closing this tutorial)."
            ),
        ]
        tutorial_step_progress = 0
        tutorial_steps_progress_details = [
            (486, 308, 797, 550, 960, 150, 
                "This is the list of all the times you have started this chapter.\n" + 
                "You can select one of those \"checkpoints\" to see which choices you have made before reaching them.\n"  
            ),
            (1280, 312, 616, 626, 960, 150, 
                "Once a checkpoint is selected, you can see here the possible choices that you faced before reaching this point.\n" + 
                "And below are the ones you can make in this chapter.\n" +  
                "There is a question mark for the ones that have not yet been discovered."  
            ),
        ]
        tutorial_step_progress_details = 0
        tutorial_on = False

        current_run = 1 # TODO move
        current_position = 0 # TODO move

        has_been_restarted = False

        is_death = True # Assume the ending is a death, unless written otherwise
        first_ending = True
        first_survive = True

        is_intuition = False # Assume  a death doesn't provide an intuition, unless written otherwise

        current_checkpoint = None
        current_day = None

        action_needed_fix = False # Use to have a valid action that does nothing

        # Conditions for menu shortcuts
        condition_saturday_morning = "(current_day == 'Saturday' and current_phase == 'Morning')"
        condition_saturday_morning_or_hunt = "(current_day == 'Saturday' and (current_phase == 'Morning' or current_phase == 'The Hunt' or current_phase == 'No Hunt'))"
        condition_saturday_hunt = "(current_day == 'Saturday' and (current_phase == 'The Hunt' or current_phase == 'No Hunt'))"
        condition_saturday_hunt_morning = "(current_day == 'Saturday' and (current_hour<12))"
        condition_saturday_evening = "(current_day == 'Saturday' and current_phase == 'Evening')"
        condition_saturday = "current_day == 'Saturday'"
        condition_friday = "current_day == 'Friday'"
        condition_friday_dinner = "(current_day == 'Friday' and (current_hour<21))" # For doctor talks to Lad during and after dinner
        condition_friday_afternoon = "(current_day == 'Friday' and current_phase == 'Evening')"
        condition_friday_evening = "(current_day == 'Friday' and current_phase == 'Evening')"
        condition_friday_or_saturday = "(current_day == 'Friday' or current_day == 'Saturday')"
        condition_friday_or_saturday_morning = "(current_day == 'Friday' or (current_day == 'Saturday' and current_phase == 'Morning'))"
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

