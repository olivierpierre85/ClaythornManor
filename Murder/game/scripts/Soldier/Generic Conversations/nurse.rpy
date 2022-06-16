# Generic conversations with between the nurse and the soldier

label nurse_generic():

  if soldier_generic_nurse == 0:
    call nurse_generic_1
    $ soldier_generic_nurse = soldier_generic_nurse + 1
  else:
    call nurse_generic_end

  return


label nurse_generic_1:
  show nurse

  "The woman seems a bit nervous"

  soldier "Hi miss ..."

  nurse "Miss Baxter, Amalia Baxter."

  soldier "Nice to meet you miss Baxter."

  hide nurse

  return

label nurse_generic_end:
  nurse "Sorry, but I don't think I have nothing to say to you anymore at the moment." 

  return
