# Generic conversations with between the psychic and the hero

label psychic_generic:

  if hero_generic_psychic == 0:

    show psychic

    "The woman seems a bit nervous"

    hero "Hi miss ..."

    psychic "Miss Baxter, Amalia Baxter."

    $ psychic_name = "Amalia Baxter"

    hero "Nice to meet you miss Baxter. I am Ted Haring"

    psychic "Likewise."
    
  else:
    show psychic

    hero "Hi again Miss Baxter."

    psychic "Mister Harring. I am glad we can continue our conversation"

  # After greeting, general discussion
  call psychic_generic_choices

  hide psychic

  $ hero_generic_psychic = hero_generic_psychic + 1

  return
