# Generic conversations with between the nurse and the hero

label nurse_generic:

  if lad_generic_nurse == 0:

    show nurse scared

    "The woman seems a bit nervous"

    lad "Hi miss ..."

    nurse "Miss Baxter, Amalia Baxter."

    $ nurse_name = "Amalia Baxter"

    lad "Nice to meet you miss Baxter. I am Ted Haring"

    nurse "Likewise."
    
  else:
    show nurse scared

    lad "Hi again Miss Baxter."

    nurse "Mister Harring. I am glad we can continue our conversation"

  # After greeting, general discussion
  call nurse_generic_choices

  hide nurse

  $ lad_generic_nurse = lad_generic_nurse + 1

  return
