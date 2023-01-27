transform character_talking_left:
    xpos 250  
    ypos 520

transform character_talking_right:
    zoom 1.3
    xpos 1600  
    ypos 600

# TODO put in python function for consistency
label change_time(hours, minutes, phase = None, day = None, hide_minutes = False):
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

# label change_room(new_room, fadeout = None):
#     python:
#         renpy.scene()
#         renpy.show(new_room)
#         if fadeout:
#             renpy.with_statement(fadeout)

#         current_room = new_room
#         print(new_room)
#         for room in rooms:
#             print(room.name)
#             if new_room == room.id:
#                 current_floor = room.floor
#                 selected_floor = room.floor

#     return

# Smart music changes
init python:
    def change_room(new_room, fadeout = None):
        global current_floor, selected_floor, current_room

        renpy.scene()
        renpy.show(new_room)

        if fadeout:
            renpy.with_statement(fadeout)

        current_room = new_room
        for room in rooms:
            if new_room == room.id:
                current_floor = room.floor
                selected_floor = room.floor

        return

    def play_music(music_style, start_song = 1, fadein_val = 5, fadeout_val = 5, loop_val = True):
        global current_music, previous_music, current_start_song, previous_start_song
        
        # Don't restart same music already in play
        if current_music == music_style:
            return 
        
        if music_style == 'previous':
            current_music = previous_music
            current_start_song = previous_start_song
        else:
            previous_music = current_music
            previous_start_song = current_start_song
            current_music = music_style
            current_start_song = start_song

        track_lists = dict()
        track_lists['upbeat'] = ['audio/music/upbeat_01.mp3', 'audio/music/upbeat_02.mp3', 'audio/music/upbeat_04.mp3']
        track_lists['chill'] = ['audio/music/chill_01.mp3', 'audio/music/chill_02.mp3', 'audio/music/chill_03.mp3']
        track_lists['sad'] = ['audio/music/sad_01.mp3', 'audio/music/sad_02.mp3', 'audio/music/sad_03.mp3']
        track_lists['mysterious'] = ['audio/music/mysterious_01.mp3', 'audio/music/mysterious_02.mp3', 'audio/music/mysterious_03.mp3']
        track_lists['scary'] = ['audio/music/scary_01.mp3']
        track_lists['boxer'] = ['audio/music/boxer_01.mp3']
            
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
        
        previous_music = current_music
        current_music = "none"

        renpy.music.stop(fadeout=fadeout_length)

        return

label start_again():

    hide screen centered_text

    python:
        global has_been_restarted, current_character, current_storyline

        # Change current character
        current_character = current_storyline
        
        # Restart from zero
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
            current_character.unlock_object(item, False)

        for item in current_checkpoint.observations:
            current_character.unlock_observation(item, False)

        current_character.saved_variables = copy.deepcopy(current_checkpoint.saved_variables)

        skip_clock_movement = True # Don't show move clock at first change time

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
    pause 5.0

    """
    You've reached to end of the story written so far.

    But don't worry, the rest of this game will be done soon!
    """

    hide screen centered_text

    jump character_selection