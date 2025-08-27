transform character_talking_left:
    xpos 250  
    ypos 520

transform character_talking_right:
    zoom 1.3
    xpos 1600  
    ypos 600

# TODO put in python function for consistency
label change_time(hours, minutes, phase = None, day = None, hide_minutes = False, chapter = None):
    python:
        if skip_clock_movement:
            show_minutes_movement = 0
            show_hours_movement = 0
        else:
            show_hours_movement = 3
            if hide_minutes:
                show_minutes_movement = 0
            else:
                show_minutes_movement = 3

        current_time =  time(hours,minutes,00)
        
        if phase:
            current_phase = phase

        if day:
            current_day =  day

        if chapter:
            current_chapter = chapter

        # Compute for clock rotation
        current_hour = current_time.hour
        current_minutes = current_time.minute
        extra_rotation = 0
        if current_hour >= 12:
            current_period = "PM"
        else:
            current_period = "AM"
        
        if current_day == "Saturday":
            extra_rotation += 2
        elif current_day == "Sunday":
            extra_rotation += 4

        hours_angle = (360 * extra_rotation) + ((int(current_hour) * 60) + int(current_minutes))/2
        
        minutes_angle = (360 * (current_hour) ) + int(current_minutes) * 6 # + (360 * extra_rotation * 24) TOO fast?

    show screen current_time
    
    play clock "<from 0 to 3.0>audio/sound_effects/clock.ogg"

    $ skip_clock_movement = False

    return

label breakpoint:
    menu:
        "keep going":
            "DEBUG"

    return

# Smart music changes
init python:
    def change_room(new_room, transition = dissolve):
        global current_floor, selected_floor, current_room, previous_room
        
        if not full_testing_mode:
        
            if new_room == 'PREVIOUS':
                new_room = previous_room
            else:
                previous_room = current_room

            renpy.scene()
            renpy.show(new_room)

            if transition:
                renpy.with_statement(transition)

            current_room = new_room
            for room in rooms:
                if new_room == room.id:
                    current_floor = room.floor
                    selected_floor = room.floor

        return

    def play_music(music_style, start_song = 1, fadein_val = 5, fadeout_val = 5, loop_val = True):
        global current_music, previous_music, current_start_song, previous_start_song
        
        if not full_testing_mode:
            # Don't restart same music already in play
            if current_music == music_style:
                return 
            
            if music_style == 'PREVIOUS':
                current_music = previous_music
                current_start_song = previous_start_song
            else:
                previous_music = current_music
                previous_start_song = current_start_song
                current_music = music_style
                current_start_song = start_song

            if current_music != 'NONE':

                track_lists = dict()
                track_lists['upbeat'] = ['audio/music/upbeat_01.mp3', 'audio/music/upbeat_02.mp3', 'audio/music/upbeat_04.mp3']
                track_lists['chill'] = ['audio/music/chill_01.mp3', 'audio/music/chill_02.mp3', 'audio/music/chill_03.mp3']
                track_lists['sad'] = ['audio/music/sad_01.mp3', 'audio/music/sad_02.mp3', 'audio/music/sad_03.mp3']
                track_lists['mysterious'] = ['audio/music/mysterious_01.mp3', 'audio/music/mysterious_02.mp3', 'audio/music/mysterious_03.mp3']
                track_lists['scary'] = ['audio/music/scary_01.mp3','audio/music/scary_02.mp3', 'audio/music/scary_03.mp3']
                track_lists['boxer'] = ['audio/music/boxer_01.mp3']
                track_lists['danger'] = ['audio/music/danger_01.mp3']
                track_lists['end_credits'] = ['audio/music/end_credits.mp3']
                    
                if current_start_song == 1:
                    track_list_ordered = track_lists[current_music]
                elif current_start_song == 2:
                    track_list_ordered = track_lists[current_music][1:3] + [track_lists[current_music][0]]
                else:
                    track_list_ordered = [track_lists[current_music][2]] + track_lists[current_music][0:2]

                renpy.music.play(track_list_ordered, loop=loop_val, fadein=fadein_val, fadeout=fadeout_val)

        return
    
    def stop_music(fadeout_length = 5):
        global current_music, previous_music

        if not full_testing_mode:
            
            previous_music = current_music
            current_music = 'NONE'

            renpy.music.stop(fadeout=fadeout_length)

        return

    def is_sub_menu_active(sub_menu_id):

        if all_menus.get(sub_menu_id):
            sub_menu = all_menus[sub_menu_id]
        else:
            return True

        # The menu has only 1 or less visible choice, so no reason to display it
        if sub_menu.get_visible_choices_total() > 1:
            return True

        return False

    def export_choices_to_file(choices, tester_id=None):
        # ---- Build JSON payload ----
        data = {
            "tester_id": tester_id or "anon",
            "timestamp": datetime.now().isoformat(),
            "choices": choices,
        }
        json_text = json.dumps(data, indent=2, ensure_ascii=False)
        fname = f"choices_{data['tester_id']}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

        # ---- Desktop / mobile: write to disk ----
        if sys.platform != "emscripten":
            try:
                with open(fname, "w", encoding="utf-8") as f:
                    f.write(json_text)
                renpy.notify(f"Exported to {fname}")
            except Exception as e:
                renpy.notify(f"Export failed: {e}")
            return

        # ---- Web build: run JS that triggers a download ----
        if renpy.emscripten:
            # Base-64 the JSON so we don’t worry about quoting/line-breaks.
            b64 = base64.b64encode(json_text.encode("utf-8")).decode("ascii")

            js = f"""
                (function () {{
                    var data = atob("{b64}");
                    var blob = new Blob([data], {{ type: 'application/json' }});
                    var a = document.createElement('a');
                    a.href = URL.createObjectURL(blob);
                    a.download = "{fname}";
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                }})();
            """

            renpy.emscripten.run_script(js)
            renpy.notify("Download started")


label start_again():

    hide screen centered_text

    # Reset menu options and level
    $ menu_level = -1
    $ selected_choice = [None, None, None, None, None]
    $ time_diff = [None, None, None, None, None]
    

    python:
        global has_been_restarted, current_character, current_storyline, current_checkpoint, all_menus

        # Change current character
        current_character = current_storyline
        
        # Restart from zero TODO: This is not necessary anymore
        if  current_checkpoint.run == 1 and  current_checkpoint.position == 0:
            current_position = 0
            if len(current_character.checkpoints) > 0:
                current_run = current_character.get_max_run() + 1
            else:
                # First run
                current_run = 1 
        else:
            has_been_restarted = True
            
            # For this character, update run +1  in all checkpoint above this
            for checkpoint in current_character.checkpoints:
                if checkpoint.run > current_checkpoint.run:
                    checkpoint.run += 1

            # change current run to += 1
            current_run = current_checkpoint.run + 1
            # Deduct one position because a new checkpoint will immediately be created with pos + 1
            current_position = current_checkpoint.position - 1 

        # Reset object, observation, choices...
        current_character.reset_information()

        # re run objects and observations from checkpoint
        for item in current_checkpoint.objects:
            current_character.objects.unlock(item, True)
            # current_character.objects.unlock(item)

        for item in current_checkpoint.observations:
            current_character.observations.unlock(item, True)
            # current_character.observations.unlock(item)
        
        for item in current_checkpoint.important_choices:
            current_character.important_choices.unlock(item, True)
            # current_character.important_choices.unlock(item)

        # Reset Menus hidden property with debugging output
        for menu_id, menu in all_menus.items():
            menu.early_exit = False # Reset early_exit
            if current_checkpoint.all_menus and menu_id in current_checkpoint.all_menus:
                checkpoint_menu = current_checkpoint.all_menus[menu_id]

                for i, checkpoint_choice in enumerate(checkpoint_menu.choices):
                    if i < len(menu.choices):
                        menu.choices[i].hidden = checkpoint_choice.hidden
            else:
                for i, choice in enumerate(menu.choices):
                    choice.hidden = False

        current_character.saved_variables = copy.deepcopy(current_checkpoint.saved_variables)

        skip_clock_movement = True # Don't show move clock at first change time TODO NOT WORKING??

        stop_music(1)

        renpy.jump(current_checkpoint.label_id) 

    return

# NOT needed, imprint frame in picture
# label show_character(character, talk_position = character_talking_left):
#   $ renpy.show(character, at_list=[talk_position])
#   # $ renpy.show("painting_frame", at_list=[talk_position], tag=character)
#   return

# label hide_character(character):
#   $ renpy.hide(character)
#   $ renpy.hide("painting_frame")
#   return

# Copy from screens.rpy

# TODO remove when game finished
label work_in_progress:

    hide screen current_time
    hide screen in_game_menu_btn

    scene black_background with wipedown
    show screen centered_text("The story is over for now.")
    play sound gong
    pause 2.0

    """
    You've reached to end of the story written so far.

    But don't worry, the rest of this game will be ready soon ! (or at some point in the future).
    """

    hide screen centered_text

    jump character_selection