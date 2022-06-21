label nurse_generic_choices:
  if time_left > 0:
    menu:
      set menu_nurse_generic
      "What do you do in life ?":
        call nurse_generic_job
        $ time_left = time_left - 30
        call nurse_generic_choices
        return

      "Why were you invited here ?":
        call nurse_generic_heroic_act
        $ time_left = time_left - 60
        call nurse_generic_choices
        return
      
      "Where are you from":
        call nurse_generic_background
        $ time_left = time_left - 60
        call nurse_generic_choices
        return

      "You have nothing to ask":
        return
  else:
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