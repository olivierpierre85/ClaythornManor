init python:
  psychic_generic_menu = TimedMenu([
    TimedMenuChoice('What do you do in life ?', 'psychic_generic_job', 20),
    TimedMenuChoice('Why were you invited here ?', 'psychic_generic_heroic_act', 20),
    TimedMenuChoice('Where are you from ?', 'psychic_generic_background', 20),
    TimedMenuChoice('You don\'t have anymore questions for her', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
  ])

label psychic_generic_choices:

  # Needed to be able to come back to the menu
  $ return_menu = current_menu 
  $ current_menu = psychic_generic_menu
  call run_menu(current_menu, return_menu)
  
  return

label psychic_generic_job:
  psychic "I am a psychic. I work in an hospital in London."

  # Special label/function that will also play sound
  $ renpy.notify("You found the occupation for The psychic")
  #TODO problem, they superpose, thus erasing the previous message. They should be queue or something...
  $ renpy.notify("You have unlock a new Character (The psychic)")
  return

label psychic_generic_heroic_act:
  psychic """
  Well, I think it's for something I have done during the war.

  I saved a poor man's life once. 
  
  It was nothing really. I don't think I deserve to have been invited.
  """

  "After this short explanation, she asks about your own reason. And you tell her your story."

  psychic "I assume most people are here because of something during the war."
  
  return

# label hero_generic_heroic_act:
#   hero """
#   Me, well I don't think I deserve it either to be honest.

#   Like yourself, it was during the war.


#   """

#   return

label psychic_generic_background:
  psychic "I am from Sausage Island"
  return
  
label psychic_generic_manor:
  psychic "It is certainly spooky right ?"

  # TODO  keep a generic response OR try to have a response different for different characters ?
  $ responses = dict()
  $ responses["hero"] = "I agree, I was a bit afraid of that at first."

  $ renpy.say(eval(current_character), responses[current_character])
  return

label psychic_generic_cancel:
  return