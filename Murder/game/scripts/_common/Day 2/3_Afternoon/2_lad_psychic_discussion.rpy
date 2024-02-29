# ------------------------------------
#               LAD/PSYCHIC
# ------------------------------------
label common_day2_afternoon_lad_psychic_discussion:

    play sound door_knock

    psychic """
    Mister Harring, may I come in?
    """

    """
    Amelia Baxter... What does she want?
    """

    lad """
    Come on in, Mrs. Baxter. The door is open.
    """

    play sound door_open

    if current_character.text_id == "psychic":
        $ change_room('lad_room')

    psychic """
    I'm sorry to intrude, but I believe we should talk.
    """

    if current_character.text_id == "lad":

        """
        She doesn't wait for an answer and begins explaining.
        """

    psychic """
    Something dangerous is happening here.
    """

    lad """
    What do you mean?
    """

    psychic """
    Don't you find it strange that two different people died in the same place, from two different causes?
    """

    lad """
    Well, I don't know about Thomas Moody. 
    
    But for the doctor's death, you said it yourself: Samuel Manning was probably drunk. 
    
    That's tragic, but not really surprising.
    """

    psychic """
    That's what I initially thought. 

    However, I just spoke with the butler. He insisted that Samuel Manning was clear-minded when he handed him his gun.
    """

    lad """
    So, what, you think he staged the accident?

    He might've just drank too much during the hunt.
    """

    psychic """
    Possibly, but it's still suspicious. 

    I have other reasons to believe something is amiss here.

    Let's just say, I have a feeling.
    """

    lad """
    You can "feel" it?
    """

    psychic """
    Don't dismiss what you don't understand, Mister Harring.

    But it's okay. I don't need you to believe me.

    I'm simply warning you to be cautious.
    """

    lad """
    Are you scared of Samuel Manning?
    """

    psychic """
    Yes, but not just him. 
    
    Others might be involved too.

    I don't think we can trust anyone fully.
    """

    lad """
    Yet, you seem to trust me.
    """

    psychic """
    Well, I wouldn't put it that way. 

    If someone were after me, I'd be defenseless. So, I need an ally. 

    You seem capable of defending both of us if there's a direct confrontation.

    So, I chose to confide in you.
    """

    if current_character.text_id == "lad":
        """
        I'm at a loss for words.

        A murder?

        It's probably just a wild theory.

        But still...
        """

    call change_time(18,30)

    play sound dinner_gong

    if current_character.text_id == "lad":
        
        """
        The gong sounds.

        Everything that happened didn't disturbed the order of the house, it seems.
        """

    psychic """
    It is dinner time.

    Not that I'm particularly hungry.

    But we should head downstairs regardless.
    """

    if current_character.text_id == "lad":

        """
        I nod in agreement.
        """

    else:

        """
        He nods in agreement.
        """

    psychic """
    I believe we should continue this conversation later. 
    
    If you agree, come see me in my room after dinner.
    """

    return