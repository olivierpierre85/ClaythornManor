# Generic conversations with between the doctor and the hero

label doctor_generic():

  if lad_generic_doctor == 0:
    show doctor

    lad "Hi sir ..."

    doctor "Hi, I am doctor Daniel Baldwin."

    show doctor

    lad "Nice to meet you doctor."

    hide doctor
    
    $ lad_generic_doctor = lad_generic_doctor + 1 #TODO replace by already met Boolean

    call doctor_generic_choices

    return

  else:
    
    lad "Hi again ..."

    call doctor_generic_choices

    return 

  return