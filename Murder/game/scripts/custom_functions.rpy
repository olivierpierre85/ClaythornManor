transform character_talking_left:
    xpos 250  
    ypos 520

transform character_talking_right:
    zoom 1.3
    xpos 1600  
    ypos 600

# TODO put in python function for consistency
label change_time(hours, minutes, phase = None, day = None, ):
    python:
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
        # print(extra_rotation, "-", hours_angle)
        
        minutes_angle = (360 * current_hour) + int(current_minutes) * 6 # + (360 * extra_rotation * 24) TOO fast?

    play clock "<from 0 to 3.0>audio/sound_effects/clock.ogg"

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

    def play_music(music_style):
        # renpy.music.get_playing(channel='music')
        global current_music, previous_music
        if music_style == 'previous':
            current_music = previous_music
        else:
            previous_music = current_music
            current_music = music_style

        track_lists = dict()
        track_lists['upbeat'] = ['audio/music/upbeat_01.mp3', 'audio/music/upbeat_02.mp3', 'audio/music/upbeat_04.mp3']
        track_lists['chill'] = ['audio/music/chill_01.mp3', 'audio/music/chill_02.mp3']
        track_lists['sad'] = ['audio/music/sad_01.mp3', 'audio/music/sad_02.mp3']
        track_lists['mysterious'] = ['audio/music/mysterious_01.mp3', 'audio/music/mysterious_01.mp3']
        track_lists['scary'] = ['audio/music/scary_01.mp3']
            
        renpy.music.play(track_lists[current_music], loop=True, fadein = 5, fadeout = 5)

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