label lad_day2_afternoon_bedroom:
    $ change_room('lad_room')

    call change_time(18,00)

    """
    So I retreated to my room to get clean clothes.

    As I was preparing to go downstairs again, someone knocks on my door.
    """

    play sound door_knock

    psychic """
    Mister Harring, can I come in?
    """

    """
    Amelia Baxter... What does she want?
    """

    lad """
    Come on in Mrs Baxter. The door is open.
    """

    play sound door_open

    psychic """
    I am sorry to intrude, but I think we should talk.
    """

    """
    She doesn't wait for an answer and starts explaining.
    """

    psychic """
    There is something dangerous happening here.
    """

    lad """
    What do you mean?
    """

    psychic """
    I mean that I don't think those deaths were an accident.
    """

    lad """
    What makes you think that?
    """

    psychic """
    Don't you think is strange two different persons died in the same place, of two different causes?
    """

    lad """
    Well, I don't know for Thomas Moody. 
    
    But for the doctor's death, you said it yourself: Samuel Manning was probably drunk. 
    
    That's sad, but not really a surprise.
    """

    psychic """
    That's what I thought at first. 

    But I just had a chat with the butler. He could swear that Samuel Manning was clear of mind when he gave him his gun.
    """

    lad """
    So what, you think he faked the accident?

    He could have simply drank too much during the hunt.
    """

    psychic """
    True, but it's still suspicious. 

    And I have other reasons to believe there is something off here.

    Let's just say I can feel it.
    """

    lad """
    You can \"feel\" it?
    """

    psychic """
    Don't mock what you don't understand Mister Harring.

    But it's alright, I don't need you to believe me.

    I am just warning you to be careful.
    """

    lad """
    You are afraid of Samuel Manning?
    """

    psychic """
    Yes, but not only of him. 
    
    Other people may be involved in this.

    I don't think we can trust anyone.
    """

    lad """
    You seem to trust me. 
    """

    psychic """
    Well I wouldn't say that exactly. 

    But if someone is after me, I couldn't defend myself. So I need an ally. 

    And you are strong enough to protect me in case their is a direct confrontation.

    So I made a bet to confide in you.
    """

    """
    I don't know what to say.

    A murder?

    It's probably nonsense.

    But still ...
    """

    call change_time(18,30)

    play sound dinner_gong

    """
    I hear the gong.

    Everything that happened didn't disturb the order of the house apparently.
    """

    psychic """
    Looks like it's dinner time.

    Not that I have much of an appetite.

    But we should head downstairs anyway.
    """

    """
    I nod in agreement.
    """

    psychic """
    But if you want to discuss this further. Come and see me in my room after dinner.
    """

    if not is_unlock_map('psychic_room'): #TODO if lad knows psychic?

        psychic """
        I am in the \"George III\" room.
        """

        $ unlock_map('psychic_room')

    return

