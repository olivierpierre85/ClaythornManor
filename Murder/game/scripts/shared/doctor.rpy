label doctor_generic_choices:
  if time_left > 0:
    menu:
      set menu_doctor_generic
      "What do you do in life ?":
        call doctor_generic_job
        $ time_left = time_left - 30
        call doctor_generic_choices
        return

      "Why were you invited here ?":
        call doctor_generic_heroic_act
        $ time_left = time_left - 60
        call doctor_generic_choices
        return
      
      "Where are you from":
        call doctor_generic_background
        $ time_left = time_left - 60
        call doctor_generic_choices
        return

      "You have nothing to ask":
        # TODO MAKE SURE THE CHOICE IS ALWAYS PRESENT DESPITE MENUSET
        return
  else:
    return

label doctor_generic_job:
  doctor "I am a doctor."
  return

label doctor_generic_heroic_act:
  doctor "During the war, I saved a poor man's life. It was nothing really. I don't think I deserve to have been invited"
  return

label doctor_generic_background:
  doctor "I am from Candy Ci"
  return