 
label doctor_generic():

  if 'doctor' not in current_character.has_met:
    
    if current_character.text_id == "lad":

      lad "Hi sir ..."

      doctor "Hi, I am doctor Daniel Baldwin."

      lad "Nice to meet you doctor."

      $ current_character.has_met.add('doctor')

  else:
    
    lad "Hello again Doctor."

  if not 'doctor_generic_menu' in locals():
    $ doctor_generic_menu = TimedMenu([
      TimedMenuChoice('Talk about the weather', 'doctor_generic_weather', 5),
      TimedMenuChoice('Ask him about himself', 'doctor_generic_background', 20),
      TimedMenuChoice('Why were you invited here ?', 'doctor_generic_heroic_act', 20, condition = "psychic_details.check_knowledge_unlocked('background')"),
      TimedMenuChoice('Talk about the manor', 'doctor_generic_manor', 10),
      TimedMenuChoice('Ask him his age', 'doctor_generic_age', 5),
      # TimedMenuChoice('Ask about the others', 'doctor_generic_others', 5),
      TimedMenuChoice('You don\'t have anymore questions for him', 'doctor_generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "doctor")

  call run_menu(doctor_generic_menu)
  
  return

label doctor_generic_others:

  return

label doctor_generic_weather:
  # TODO adapt depending of the day
  doctor """
  A dreadful storm if you ask me.

  I don't know what's planed for tomorrow, but I hope it won't involve getting out this house.
  """

  return

label doctor_generic_background:
  doctor """
  I am the chief physician at St Margaret's Hospital.

  It's a charity hospital for persons in need.

  Before that I worked a bit of everywhere.

  I also served in the war twice. 

  In the last one of course, but I was also in China during the insurrection.
  """

  $ doctor_details.add_knowledge('background') 

  return

label doctor_generic_heroic_act:
  doctor """
  Well, I celebrated my ten years at the St Margaret's recently.

  Not a lot of people remains that long at this type of institution.

  Usually, a doctor stays a few year to get a reputation, then moves on to a more luxurious practice.

  Lady Claythorn must have understood how much of a sacrifice I made, hence the reward.

  Not that I consider it a sacrifice of course.

  I love my job and wouldn't change it for the world.

  Still, it's always nice to get some recognition.
  """
  return

label doctor_generic_manor:
  doctor """
  It's a nice house.

  But I couldn't say much more about it. 

  I am not used to visit such places.
  
  That's the first time I am invited in a grand mansion as a guest and not as a doctor.

  The truth is my job doesn't pay as much.

  Nevertheless, I am content with my small apartment.

  I wouldn't want anything this big. It must be such a hassle to manage.
  """

  if current_character.text_id == "lad":
    lad "So you are not accustomed to having a butler, and footmen around ?"

    doctor "No, I can't say that I am."

    "Well, that's a bit reassuring"

  $ doctor_details.add_knowledge('status') 

  return

label doctor_generic_age:
  doctor "I am 39 nine years. Why do you ask ?"

  if current_character.text_id == "lad":
    lad "Actually I am not sure."

  $ doctor_details.add_knowledge('age') 
  
  return

label doctor_generic_cancel:
  return