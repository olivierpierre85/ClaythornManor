label psychic_generic_other_guests:

    call run_menu(current_character.saved_variables["psychic_generic_other_guests_menu"])

    return

label psychic_generic_other_guests_saturday:

    psychic """
    I haven't had time to form an opinion of everyone yet.

    I have only had time to speak with Captain Sinha, and with that poor drunkard Samuel Manning.

    And I could also exchange a few words with our hostess, Lady Claythorn.
    """

    return

label psychic_generic_other_guests_saturday_morning:

    call psychic_generic_other_guests_saturday

    call psychic_generic_other_guests

    $ lad_details.saved_variables["psychic_generic_other_guests_saturday_morning_ask"] = True

    return
    

label psychic_generic_other_guests_saturday_hunt:

    if not lad_details.saved_variables["psychic_generic_other_guests_saturday_morning_ask"]:

        call psychic_generic_other_guests_saturday

    else:

        psychic """
        You know that I already talked with Samuel Manning, Captain Sinha and our host.
        """

    psychic """
    Now, I have also talked a little with Miss Marsh.
    """

    call psychic_generic_other_guests

    return

label psychic_generic_other_guests_friday:
    # DRINKS AND DINNER
    psychic """
    I've just met them. So I can't say I know a lot yet.

    All I know is that this guy over there ...
    """

    """
    She points at Sushil Sinha.
    """

    psychic """
    ... is monopolising the conversation.

    And he is very noisy too.

    It's not very tactful if you ask me.
    """

    $ captain_details.description_hidden.unlock('talker') 

    return

label psychic_generic_drunk_saturday_morning:

    psychic """
    Well, I believe you can tell as well as I that he is a dangerous drunk.

    We better stay away from him.
    """

    $ drunk_details.description_hidden.unlock('addict') 

    return

label psychic_generic_captain_saturday_morning:

    psychic """
    He appears to me the very image of a military man.

    Except for, you know, his origin.

    I did not think they would accept indigenous people in the British Army.

    But aside from that, he is exactly like other officers I have met.

    Bold, sure of himself, and never shy of speaking about himself.

    I bet he will keep on telling stories about his "Glorious Days" during one war or another.

    I find it in poor taste, so I shall try to avoid him in the coming days.

    I suggest you do the same, unless you want to be bored to death.
    """

    $ captain_details.description_hidden.unlock('talker') 

    return

label psychic_generic_host_saturday_morning:

    psychic """
    I only exchanged a few pleasantries with the lady of the house.

    She seems delightful to me.

    What pleased me even more was that she addressed me as an equal.

    That's very different from most noble people I've met.
    
    They usually look down on people like you...
    
    ... and me.
    """

    """
    She paused a little too long before adding "and me".

    I don't like that.
    """

    $ host_details.description_hidden.unlock('down_to_earth') 

    return

label psychic_generic_nurse_saturday_hunt:

    psychic """
    From what I've seen, I believe she is a very respectable woman.

    She worked most of her life as a nurse.

    So I believe the prize money could help her retire.
    """

    return

label psychic_generic_other_guests_saturday_evening:

    psychic """
    Good question, we'll be stronger if we know who to be wary of.

    I've thought about it and Samuel Manning is of course the prime suspect.

    But he is locked in his room now, so I wouldn't worry about him too much.

    The other obvious suspect is Thomas Moody. 
    
    The fact that he wears a mask is the perfect way to hide his true identity.

    But he can't really hurt us anymore, can he?

    So that leaves us three persons to worry about: Sushil Sinha, Lady Claythorn and Rosalind Marsh.
    """
    
    call psychic_generic_other_guests

    return

label psychic_generic_captain_saturday_evening:

    psychic """
    Captain Sinha is the one I am most worried about.

    He is the strongest of us, has military experience.
    
    And he often took command during dramatic moments, which means he can try to drive us where he wants.

    I would be very cautious around him if I were you.
    """

    return


label psychic_generic_host_saturday_evening:

    psychic """
    If money is not the reason behind the murders, then I suppose she would be suspicious.

    After all, she is the one who called all of us here.

    But as I said, it would be a lot of work to organise all this, and for what?

    To kill a few of her enemies?

    That seems a bit far-fetched.

    Also, she seemed very nice to me. 

    But of course that doesn't mean much.
    """

    return

label psychic_generic_nurse_saturday_evening:

    psychic """
    Miss Marsh definitely doesn't have the type of a killer.

    But that's not reason enough to think she couldn't be.

    She is very discreet.

    That could be a way to search the manor while she relies on an accomplice for the more "physical" part of the robbery.
    """

    return