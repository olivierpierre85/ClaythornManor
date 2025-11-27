label nurse_generic_other_guests_saturday_morning:

    nurse """
    Oh, up until now, I've mostly kept to myself.

    I haven't talked to many people.

    I am seated next to Samuel Manning, but we haven't had a very deep conversation yet.

    Our host is the only other person I've had any real exchange with.

    But we stuck mostly to simple pleasantries.
    """

    call run_menu(current_character.saved_variables["nurse_generic_other_guests_menu"])

    return


label nurse_generic_drunk_saturday_morning:

    nurse """
    I usually don't like to spread gossip.

    But in this case, I don't think it's a big secret.

    I believe Samuel Manning is an alcoholic.

    He was barely intelligible both at dinner yesterday and this morning.

    Those were two pretty unpleasant meals for me.
    """

    if current_character.text_id == "psychic":

        """
        Well, that's nothing I didn't already know.
        """


    $ drunk_details.description_hidden.unlock('addict') 

    return


label nurse_generic_other_guests_saturday_evening_doctor:

    nurse """
    Well, I must admit I have not tried to socialise much.

    I have spoken a little with our host, though nothing of any real substance.

    This afternoon I shared lunch with Amelia Baxter, quite an interesting character.

    And of course there was our poor Mister Manning, ...
    """

    """
    She realises to whom she is speaking and falls silent.
    """

    doctor """
    Yes, a most tragic event. I still can scarcely believe what has happened.
    """

    nurse """
    I am terribly sorry, Doctor. I did not mean to upset you.
    """

    doctor """
    That is all right.
    """

    call run_menu(current_character.saved_variables["nurse_generic_other_guests_menu"])

    return


label nurse_generic_psychic_saturday_evening_doctor:

    nurse """
    Miss Baxter is a very pleasant woman, quite easy to talk to.

    But she made me a little uneasy when she spoke of her "gift".
    """

    doctor """
    Gift? What do you mean?
    """

    nurse """
    She is convinced that she can speak with the deceased, or with some other version of them that exists upon another plane.

    I must confess I did not follow every word. I do not care to speak of the dead, and I found it most unsettling.
    """

    doctor """
    I can imagine. It is a delicate subject to raise with a stranger.

    Did she seem well otherwise?
    """

    nurse """
    She did. 
    
    You might be thinking as I did at first. That she might be ill.

    I have seen this sort of thing in certain patients, particularly those approaching the end of their lives.

    But the rest of her behaviour was perfectly normal, and that was what troubled me most.
    """

    doctor """
    I see. It is not unheard of for someone to hold a fixed idea upon a single matter, yet remain entirely sound in all others.

    In my experience such notions may arise from strain or some powerful emotional shock, even when the mind is otherwise quite stable.

    So she could be perfectly well in every other respect.

    Of course, we cannot disregard the possibility of a more serious condition.

    In rare cases a fixed belief of that nature may be an early sign of dementia praecox, or what some of my colleagues have begun to call schizophrenia.

    But I would not draw conclusions too hastily. It is far more likely that Miss Baxter is of sound mind, eccentricities notwithstanding.
    """

    nurse """
    Thank you. That is a relief.
    """

    $ psychic_details.description_hidden.unlock('background') 

    return


label nurse_generic_host_saturday:

    nurse """
    I only share a few words with the Lady of the house.

    I tried to know more about the details of the Manor, the staff, that sort of things.
    
    She was quite polite, but her responses were short and not very informative.

    I hope I wasn't rude to her.
    """

    return