init python:
  doctor_generic_menu = TimedMenu([
    TimedMenuChoice('What do you do in life ?', 'doctor_generic_job', 20),
    TimedMenuChoice('Why were you invited here ?', 'doctor_generic_heroic_act', 20),
    TimedMenuChoice('Where are you from ?', 'doctor_generic_background', 20),
    TimedMenuChoice('You don\'t have anymore questions for him', 'doctor_generic_cancel', 0, keep_alive = True, early_exit = True)
  ])
    
label doctor_generic_choices:
  
  call run_menu(doctor_generic_menu)
  
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