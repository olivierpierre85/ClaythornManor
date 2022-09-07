# Generic conversations with between the doctor and the hero

label doctor_generic():

  if hero_generic_doctor == 0:
    show doctor

    hero "Hi sir ..."

    doctor "Hi, I am doctor Daniel Baldwin."

    show doctor

    hero "Nice to meet you doctor."

    hide doctor
    
    $ hero_generic_doctor = hero_generic_doctor + 1 #TODO replace by already met Boolean

    call doctor_generic_choices

    return

  else:
    
    hero "Hi again ..."

    call doctor_generic_choices

    return 

  return