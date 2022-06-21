# Generic conversations with between the nurse and the soldier

label nurse_generic:

  if soldier_generic_nurse == 0:

    show nurse scared

    "The woman seems a bit nervous"

    soldier "Hi miss ..."

    nurse "Miss Baxter, Amalia Baxter."

    $ nurse_name = "Amalia Baxter"

    soldier "Nice to meet you miss Baxter. I am Ted Haring"

    nurse "Likewise."
    
  else:
    show nurse scared

    soldier "Hi again Miss Baxter."

    nurse "Mister Harring. I am glad we can continue our conversation"

  # After greeting, general discussion
  call nurse_generic_choices

  hide nurse

  $ soldier_generic_nurse = soldier_generic_nurse + 1

  return
