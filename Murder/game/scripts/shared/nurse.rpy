label nurse_generic_choices:
  python:
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
        'text': 'You have nothing to ask',
        'redirect': 'nurse_generic_cancel',
        'time_spent': 0,
        'early_exit': True,
      },
    ]

  call timed_menu('nurse_generic_choices')
  
  return

label nurse_generic_job:
  nurse "I am a nurse."
  return

label nurse_generic_heroic_act:
  nurse "I saved a poor man's life once. It was nothing really. I don't think I deserve to have been invited"
  return

label nurse_generic_background:
  nurse "I am from Sausage Island"
  return

label nurse_generic_cancel:
  return