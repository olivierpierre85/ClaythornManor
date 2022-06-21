# Generic conversations with between the doctor and the soldier

label doctor_generic():

  if soldier_generic_doctor == 0:
    show doctor

    soldier "Hi sir ..."

    doctor "Hi, I am doctor Daniel Baldwin."

    show doctor happy

    soldier "Nice to meet you doctor."

    hide doctor
    
    $ soldier_generic_doctor = soldier_generic_doctor + 1

    call doctor_generic_choices

  else:
    doctor "Sorry, but I don't think I have anything to say to you anymore at the moment." 

  return