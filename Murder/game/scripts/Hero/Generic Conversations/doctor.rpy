# Generic conversations with between the doctor and the hero

label doctor_generic():

  if hero_generic_doctor == 0:
    show doctor

    hero "Hi sir ..."

    doctor "Hi, I am doctor Daniel Baldwin."

    show doctor happy

    hero "Nice to meet you doctor."

    hide doctor
    
    $ hero_generic_doctor = hero_generic_doctor + 1

    call doctor_generic_choices

    return

  else:
    doctor "Sorry, but I don't think I have anything to say to you anymore at the moment." 

  return