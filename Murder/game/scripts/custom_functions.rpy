transform character_talking_left:
  xpos 250  
  ypos 520

transform character_talking_right:
  xpos 1450  
  ypos 520

transform character_choice_left:
  xpos 100  
  ypos 250

transform character_choice_right:
  xpos 1600  
  ypos 250

label check_characters_knowledge(character, knowledge):
  if  knowledge not in characters_knowledge[character]:
    $ characters_knowledge[character].add(knowledge)
    
    $ renpy.notify("You have found the " + knowledge + " of The " + character)
    play sound "audio/sound_effects/writing_short.ogg"
    # play sound "audio/sound_effects/unlock.ogg"

    if len(characters_knowledge[character]) == 3:
      # Unlock a character
      pause 2.0
      play sound "audio/sound_effects/unlock_char.ogg"
      $ renpy.notify("You have unlock a new Character : The " + character)
  return

label change_time(hours,minutes):
  $ current_time =  time(hours,minutes,00)
  play clock "<from 0 to 3.0>audio/sound_effects/clock.ogg"
  
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