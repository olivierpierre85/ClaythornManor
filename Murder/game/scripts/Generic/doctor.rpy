label doctor_generic_choices:
  python:
    menus_options['doctor_generic_choices'] = [
      { 
        'text': 'What do you do in life ?',
        'redirect': 'doctor_generic_job',
        'time_spent': 20,
      },
      { 
        'text': 'Why were you invited here ?',
        'redirect': 'doctor_generic_heroic_act',
        'time_spent': 10,
      },
      { 
        'text': 'Where are you from',
        'redirect': 'doctor_generic_background',
        'time_spent': 10,
      },
      { 
        'text': 'You have nothing to ask',
        'redirect': 'doctor_generic_cancel',
        'time_spent': 0,
        'early_exit': True,
      },
    ]

  call timed_menu('doctor_generic_choices')
  
  return

label doctor_generic_job:
  doctor "I am a doctor."
  return

label doctor_generic_heroic_act:
  doctor "During the war, I saved a poor man's life. It was nothing really. I don't think I deserve to have been invited."
  return

label doctor_generic_background:
  doctor "I am from Candy City"
  return

label doctor_generic_cancel:
  return