label lad_generic_other_guests:

    call run_menu(current_character.saved_variables["lad_generic_other_guests_menu"])

    return


label lad_generic_other_guests_friday_dinner:

    lad """
    Well, I just arrived.
    
    So I don't really have an opinion on anyone yet.
    """

    return

# TODO: Should I move the character specifics to there character script?
label lad_generic_other_guests_friday_doctor:

    lad """
    I haven't talk a lot to other people yet, except maybe to Miss Baxter.
    """

    doctor """
    And what do you make of her?
    """

    call lad_generic_psychic_opinion

    $ doctor_details.saved_variables["asked_about_psychic"] = True

    return


label lad_generic_psychic_opinion:
        
    lad """
    I am not sure. 
    
    She seems very nice, but there is something odd about her.
    """

    doctor """
    Really, for what specific reason?
    """

    lad """    
    Sorry, I do not know how to explain it.

    It is just a feeling.
    """

    doctor """
    I see.
    """

    return


label lad_generic_other_guests_saturday_doctor:

    lad """
    I do not know, I have not had a chance to talk to everyone yet.

    So far everyone seems normal to me.
    """

    doctor """
    I was not expecting a deep character analysis.

    Merely your general impression.
    """

    lad """
    Right then.
    """
    
    call lad_generic_other_guests

    return


label lad_generic_psychic_hunt_doctor:

    if doctor_details.saved_variables.get("asked_about_psychic", False):

        lad """
        Well, we have already spoken about her, have we not?
        """

        doctor """
        Have we? I suppose you are right.    

        And you have not noticed anything new?
        """

        lad """
        Afraid not.
        """

    else:

        call lad_generic_psychic_opinion

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_drunk_hunt_doctor:

    lad """
    Samuel Manning?

    You really want to talk about him when he is right there?
    """

    doctor """
    Never mind that, he will not notice. 
    
    He looks quite out of his wits again.
    """

    lad """
    Yes, I noticed he is drunk most of the time.

    But that is about all I have witnessed so far.
    """

    doctor """
    Yes, I suppose that was obvious to everyone.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_drunk_hunt_doctor_dead:

    lad """
    Samuel Manning?

    Well does it really matter what I think of him now?
    """

    doctor """
    No, of course not.

    I don't know why I asked you that.

    I am sorry.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_captain_hunt_doctor:

    lad """
    Captain Sinha is serious, and he does go on about himself.
    """

    doctor """
    I have observed the same.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_host_hunt_doctor:

    lad """
    She is very distinguished.

    I have not dared to speak to her yet.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_nurse_hunt_doctor:

    lad """
    I do not have much to say about her.

    She is a rather discreet woman, so I have not learnt much about her.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_broken_hunt_doctor:

    lad """
    Poor Mr Manning, it is creepy to imagine he is still in his room.

    You know, dead.
    """

    doctor """
    That is how we left him, so I daresay his condition has not changed.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return
