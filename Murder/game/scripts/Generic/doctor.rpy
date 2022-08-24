label doctor_generic_choices:
  $ return_menu = current_menu 
  $ current_menu = TimedMenu([
    TimedMenuChoice('What do you do in life ?', 'doctor_generic_job', 20),
    TimedMenuChoice('Why were you invited here ?', 'doctor_generic_heroic_act', 20),
    TimedMenuChoice('Where are you from ?', 'doctor_generic_background', 20),
    TimedMenuChoice('You don\'t have anymore questions for him', 'doctor_generic_cancel', 0, keep_alive = True, early_exit = True)
  ])
  call run_menu(current_menu, return_menu)
  # python:
  #   menus_options['doctor_generic_choices'] = [
  #     { 
  #       'text': 'What do you do in life ?',
  #       'redirect': 'doctor_generic_job',
  #       'time_spent': 20,
  #     },
  #     { 
  #       'text': 'Why were you invited here ?',
  #       'redirect': 'doctor_generic_heroic_act',
  #       'time_spent': 10,
  #     },
  #     { 
  #       'text': 'Where are you from',
  #       'redirect': 'doctor_generic_background',
  #       'time_spent': 10,
  #     },
  #     { 
  #       'text': 'You have nothing to ask',
  #       'redirect': 'doctor_generic_cancel',
  #       'time_spent': 0,
  #       'early_exit': True,
  #     },
  #   ]

  # call timed_menu('doctor_generic_choices')
  
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