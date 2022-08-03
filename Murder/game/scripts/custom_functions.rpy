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

# NOT needed, imprint frame in picture
# label show_character(character, talk_position = character_talking_left):
#   $ renpy.show(character, at_list=[talk_position])
#   # $ renpy.show("painting_frame", at_list=[talk_position], tag=character)
#   return

# label hide_character(character):
#   $ renpy.hide(character)
#   $ renpy.hide("painting_frame")
#   return
