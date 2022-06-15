# Generic conversations with between the nurse and the soldier

label doctor_generic():

  if soldier_generic_doctor == 0:
    call doctor_generic_1
    $ soldier_generic_doctor = soldier_generic_doctor + 1
  else:
    call doctor_generic_end

  return


label doctor_generic_1:

  show doctor

  soldier "Hi sir ..."

  doctor "Hi, I am doctor Daniel Baldwin."

  hide doctor

  show doctor happy

  soldier "Nice to meet you doctor."



  hide doctor

  return

label doctor_generic_end:
  doctor "Sorry, but I don't think I have nothing to say to you anymore at the moment." 

  return