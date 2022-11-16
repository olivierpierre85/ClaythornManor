transform character_talking_left:
    xpos 250  
    ypos 520

transform character_talking_right:
    zoom 1.3
    xpos 1600  
    ypos 600

label change_time(hours,minutes):
    $ current_time =  time(hours,minutes,00)
    play clock "<from 0 to 3.0>audio/sound_effects/clock.ogg"

return

label breakpoint:
    menu:
        "keep going":
            "DEBUG"

    return

label change_room(new_room, fadeout = None):
    python:
        renpy.scene()
        renpy.show(new_room)
        # if fadeout:
        renpy.with_statement(irisout)

        current_room = new_room
        print(new_room)
        for room in rooms:
            print(room.name)
            if new_room == room.id:
                current_floor = room.floor
                selected_floor = room.floor

    return

# Smart music changes
init python:
    def play_music(music_style):
        # renpy.music.get_playing(channel='music')
        global current_music
        if music_style == 'previous':
            current_music = previous_music
        else:
            previous_music = current_music
            current_music = music_style

        track_lists = dict()
        track_lists['upbeat'] = ['audio/music/upbeat_01.mp3', 'audio/music/upbeat_02.mp3','audio/music/upbeat_03.mp3', 'audio/music/upbeat_04.mp3']
        track_lists['chill'] = ['audio/music/chill_01.mp3']
            
        renpy.music.play(track_lists[current_music], loop=True, fadein = 10, fadeout = 5)

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