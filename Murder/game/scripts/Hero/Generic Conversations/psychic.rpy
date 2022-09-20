# Generic conversations with between the psychic and the hero

label psychic_generic:

  show psychic at character_talking_right

  if not psychic_details.know_real_name:

    # "The woman seems a bit nervous"

    lad "Hi miss ..."

    psychic "Miss Baxter, Amalia Baxter."

    $ psychic_details.introduce()

    lad "Nice to meet you miss Baxter. I am Ted Haring"

    psychic "Likewise."
    
  else:

    lad "Hi again Miss Baxter."

    psychic "Mister Harring. I am glad we can continue our conversation"
  
  call psychic_generic_choices

  hide psychic
