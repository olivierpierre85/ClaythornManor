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
    
    She seems very nice, but there is something weird about her.
    """

    doctor """
    Really, for what specific reason?
    """

    lad """    
    Sorry, I don't know how to explain it.

    It's just a feeling.
    """

    doctor """
    I see.
    """

    return


label lad_generic_other_guests_saturday_hunt_doctor:

    lad """
    I don't know, I haven't had a chance to talk to everyone yet.

    So far everyone seems normal to me.
    """

    doctor """
    Well, I wasn't expecting a deep character analysis.

    Just wanted to know your general opinion.
    """

    lad """
    Of course then.
    """
    
    call lad_generic_other_guests

    return


label lad_generic_psychic_hunt_doctor:

    if doctor_details.saved_variables["asked_about_psychic"] = True:

        lad """
        Well, we already talked about her haven't we?
        """

        doctor """
        Have we? Well, I guess you are right.    

        And you didn't noticed anything new?
        """

        lad """
        Sorry, I can't say that I have.
        """

    else:

        call lad_generic_psychic_opinion

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return

label lad_generic_drunk_hunt_doctor:

    lad """
    Samuel Manning?

    You really want to talk about him when he is so close to us?
    """

    doctor """
    Never mind that, he won't notice. 
    
    He looks out of his wits again.
    """

    lad """
    Yes, I noticed he is drunk most of the time.

    But that's about all I've witness about him so far.
    """

    doctor """
    Yes, I suppose that was obvious to everyone.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_captain_hunt_doctor:

    lad """
    Captain Sinha is serious and likes to talk about himself it seems.
    """

    doctor """
    Yes, I have noticed that myself.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_host_hunt_doctor:


    lad """
    She is very distinguished.

    I haven't dare talk to her yet.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_nurse_hunt_doctor:

    lad """
    I don't have much to say about her.

    She is as rather discreet woman, because of that I haven't learned much about her.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


label lad_generic_broken_hunt_doctor:

    lad """
    Poor Mister Manning, that is very creepy to imagine that he is still in his room, you know, dead.
    """

    doctor """
    That's how we left him, so I guess his condition hasn't changed indeed.
    """

    $ doctor_details.saved_variables['bored_by_lad'] += 1

    return


