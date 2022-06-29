init python:
  menus_options['nurse_generic_choices'] = [
    { 
      'text': 'What do you do in life ?',
      'redirect': 'nurse_generic_job',
      'time_spent': 20,
    },
    { 
      'text': 'Why were you invited here ?',
      'redirect': 'nurse_generic_heroic_act',
      'time_spent': 10,
    },
    { 
      'text': 'Where are you from',
      'redirect': 'nurse_generic_background',
      'time_spent': 10,
    },
    { 
      'text': 'You have nothing more to ask',
      'redirect': 'nurse_generic_cancel',
      'time_spent': 0,
      'early_exit': True,
      'keep_alive': True,
    },
  ]

label nurse_generic_choices:

  call timed_menu('nurse_generic_choices')
  
  return

label nurse_generic_job:
  nurse "I am a nurse."

  # Special label/function that will also play sound
  $ renpy.notify("You found the occupation for The nurse")
  #TODO problem, they superpose, thus erasing the previous message. They should be queue or something...
  $ renpy.notify("You have unlock a new Character (The nurse)")
  return

label nurse_generic_heroic_act:
  nurse "I saved a poor man's life once. It was nothing really. I don't think I deserve to have been invited"
  return

label nurse_generic_background:
  nurse "I am from Sausage Island"
  return

label nurse_generic_cancel:
  return