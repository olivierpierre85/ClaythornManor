# ------------------------------------
#               LAD/PSYCHIC
# ------------------------------------
label common_day2_evening_lad_psychic_discussion_0:

    play sound door_knock

    psychic """
    Mister Harring, may I come in?
    """

    if current_character.text_id == "lad":
        """
        Amelia Baxter... What does she want?
        """

    lad """
    Come on in, Mrs. Baxter. The door is open.
    """

    play sound door_open

    if current_character.text_id == "psychic":
        $ change_room('bedroom_lad')

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

        She is probably paranoid.

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

label common_day2_evening_lad_psychic_discussion_1:

    lad """
    Miss Baxter?

    Are you here? It's Ted Harring.
    """

    if current_character.text_id == "lad":
        """
        She slightly opens the door and looks in the hallway.

        She seems worried.
        """

    psychic """
    Mister Harring, are you alone?
    """

    lad """
    I am.
    """

    psychic """
    Come on in then.
    """

    if current_character.text_id == "lad":
        $ change_room('bedroom_psychic')

    psychic """
    So, have you given any thought to what I told you?

    Do you agree that something isn't right?
    """

    return


label common_day2_evening_lad_psychic_discussion_2:

    lad """
    I'm not sure yet. But what happened is strange enough that we should take some precautions.
    """

    psychic """
    I'm glad you agree.

    I've given this a lot of thought, and I believe if what I fear is true, Samuel Manning had help from someone else.
    """

    $ play_music("mysterious")

    lad """
    Do you mean a guest? Or could someone from the staff be involved?
    """

    psychic """
    I wouldn't rule anything out, but it seems less likely that the staff or Lady Claythorn would be implicated.

    Such an act would require a massive operation.

    No, a more plausible theory is that one or two individuals heard about the event and took the places of real guests to infiltrate the manor.
    """

    lad """
    But why would they do that?
    """

    psychic """
    Well, it's rather obvious, isn't it?

    The prize money, of course.

    It was mentioned in the invitation letter that the prize will be given in bearer's bonds.
    """

    lad """
    Bearer's bonds?
    """

    psychic """
    That's a note that you can exchange at the bank without having to prove your identity.

    So, it's almost as easy to use as cash.
    """

    lad """
    That's a lot of money hidden somewhere in the manor.
    """

    lad """
    So you think it could be a mere robbery?
    
    Why not just directly attack the manor?
    """

    psychic """
    It's easier to enter incognito.

    First, observe and then discreetly eliminate potential threats.

    That's the most likely explanation I could think of.
    """

    lad """
    I suppose that's possible.

    But there's no way to determine who might be involved.
    """

    psychic """
    Exactly.

    That's why I suggest we stay safely in our rooms tonight.

    Tomorrow morning, the first one of us to wake up should alert the other.

    Then we stick together the entire day until we can safely leave.

    What do you think?
    """

    $ play_music("PREVIOUS")

    lad """
    It sounds like a good plan.

    Let's do it.
    """

    psychic """
    Great!

    Is there anything else you'd like to discuss?
    """

    return