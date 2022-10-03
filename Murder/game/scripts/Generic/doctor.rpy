 
label doctor_generic():

  if 'doctor' not in current_character.has_met:
    
    if current_character.text_id == "lad":

      lad "Hi sir ..."

      doctor "Hi, I am doctor Daniel Baldwin."

      lad "Nice to meet you doctor."

  else:
    
    lad "Hello again Doctor."

  if not 'doctor_generic_menu' in locals():
    $ doctor_generic_menu = TimedMenu([
      TimedMenuChoice('Talk about the weather', 'doctor_generic_weather', 5),
      TimedMenuChoice('Ask him about himself', 'doctor_generic_background', 20),
      TimedMenuChoice('Why were you invited here ?', 'doctor_generic_heroic_act', 20),
      TimedMenuChoice('Talk about the manor', 'doctor_generic_manor', 10),
      TimedMenuChoice('Ask him his age', 'doctor_generic_age', 5),
      TimedMenuChoice('You don\'t have anymore questions for him', 'doctor_generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")

  call run_menu(doctor_generic_menu)
  
  return

label doctor_generic_weather:
  # TODO adapt depending of the day
  doctor """
  A dreadful storm if you ask me.

  I don't know what's planed for tomorrow, but I hope it won't involve getting out this house.
  """

  return

label doctor_generic_background:
  doctor "I am a doctor."
  return

label doctor_generic_heroic_act:
  doctor "During the war, I saved a poor man's life. It was nothing really. I don't think I deserve to have been invited."
  return

label doctor_generic_manor:
  doctor "Nice place"
  return

label doctor_generic_age:
  doctor "I am 39 nine years. Why do you ask ?"

  if current_character.text_id == "lad":
    lad "Actually I am not sure."
    
  return

label doctor_generic_cancel:
  return