transform character_talking_left:
  xpos 250  
  ypos 520

transform character_talking_right:
  zoom 1.3
  xpos 1600  
  ypos 600

transform character_choice_left:
  xpos 100  
  ypos 250

transform character_choice_right:
  zoom 1
  xpos 1600  
  ypos 300

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