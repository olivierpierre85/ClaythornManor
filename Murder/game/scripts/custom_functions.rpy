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

# Copy from screens.rpy

label check_characters_knowledge(character, knowledge):
  if  knowledge not in characters_knowledge[character]:
    $ characters_knowledge[character].add(knowledge)
    # Special label/function that will also play sound
    $ renpy.notify("You have found the " + knowledge + " of The " + character)

    if len(characters_knowledge[character]) == 3:
      # Unlock a character
      $ renpy.notify("You have unlock a new Character : The " + character)

