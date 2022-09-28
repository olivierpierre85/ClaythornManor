# Generic conversations with between the psychic and the lad
label psychic_generic:

    if not psychic_details.know_real_name:

        lad "Hi miss ..."

        psychic "Miss Baxter, Amalia Baxter."

        $ psychic_details.introduce()

        lad "Nice to meet you miss Baxter. I am Ted Haring."

        psychic "Nice to meet you mister Haring."
        
    else:

        lad "Hi again Miss Baxter."

        psychic "Oh Mister Harring. I am glad we can continue our conversation."
    
    call psychic_generic_choices
