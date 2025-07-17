label captain_generic_other_guests:

    call run_menu(current_character.saved_variables["captain_generic_other_guests_menu"])

    return


label captain_generic_other_guests_friday:

    captain """
    Well, I don't know.

    I don't have a strong opinion about anyone at this point.

    Do you have someone in particular in mind?
    """

    call captain_generic_other_guests

    return


label captain_generic_other_guests_saturday:

    captain """
    I guess we can talk a bit about the other guests.

    Who in particular?
    """

    call captain_generic_other_guests

    return


label captain_generic_drunk_friday_psychic:

    captain """
    Ah yes, our intoxicated friend.

    There's not much to say that you haven't already noticed yourself.
    """

    """
    I guess he's right about that.
    """

    return


label captain_generic_drunk_saturday_psychic:

    captain """
    I can't believe we gave him a gun.

    Anyone could have seen he was drunk more often than not.

    In hindsight, this tragedy ought to have been avoided.
    """

    psychic """
    What do you think will happen to him?
    """

    captain """
    I can't say for certain.

    He could be charged with manslaughter by negligence and face prison time.

    Or he might be acquitted, if the death is ruled an accident.
    """

    psychic """
    Really? He could just walk free after all this?
    """

    captain """
    That depends on how the situation is presented to the police—

    and more importantly, on his connections.

    If he were a prominent aristocrat, I've no doubt he could sweep it all under the rug.

    But I don't believe that'll be the case for our friend.
    """

    return


label captain_generic_host_friday_psychic:

    captain """
    A charming lady, for sure.

    However, there's something about her that intrigues me.
    """

    psychic """
    Really?

    What exactly do you mean?
    """

    """
    He seems unsure.

    A bit embarrassed, even.
    """

    captain """
    I'm sorry, I meant nothing specific.

    I shouldn't be talking about our gracious host in any case.
    """

    psychic """
    Of course.
    """

    """
    He knows more than he's willing to say.

    But he won't disclose it with other people around.
    """

    return


label captain_generic_nurse_friday:

    captain """
    A discreet woman.

    She's stylishly dressed, but in a humble way.

    You can immediately tell she's at ease in these kinds of gatherings.
    """

    $ nurse_details.description_hidden.unlock('clothes')

    return


label captain_generic_broken_friday:

    captain """
    I'd say he's one of our war heroes.
    """

    captain """
    As a veteran of many battles, I have seen my fair share of horrors on the battlefield. 
    
    One of the most devastating and haunting realities of war is the damage it can inflict on a person's face. 
    
    The broken faces of Great War soldiers, disfigured and scarred by shrapnel, bullets, and gas, are a constant reminder of the terrible cost of conflict.

    Many of these soldiers are forced to wear masks to conceal their injuries, both physical and emotional. 
    
    These masks are not only a means of hiding their disfigurement but also a way of protecting themselves from the judgmental and curious gaze of others.

    I have met many of these brave men, and I have seen the pain and sadness in their eyes. 
    
    They have been through something unimaginable, and it is not something anyone should have to face. 

    Their sacrifice for their country is something truly admirable.

    War is not just about the physical injuries, but also the emotional and psychological scars it leaves behind. 
    
    The broken faces of these soldiers are a reminder of the human cost of war. 
    
    They are a reminder that behind every mask, there is a person with a story and a life that has been forever changed.

    I hope that we can learn from the sacrifices of these soldiers and work towards a world where conflicts can be resolved without violence, and where the broken faces of war are a thing of the past.
    """

    $ broken_details.description_hidden.unlock('mask') 

    if current_character.text_id == "psychic":

        """
        Well, that was another tedious speech.

        That's my fault for asking I suppose.
        """

    return


label captain_generic_broken_saturday:

    captain """
    What can I say, other than the obvious?

    It's a shame he died like that.

    Then again, perhaps he was in a great deal of pain from his injuries.

    If so, he might have welcomed death as a release.
    """

    if current_character.text_id == "psychic":

        psychic """
        You don't think there was anything odd about his death?
        """

        captain """
        Not really, no. If there had been, Doctor Baldwin would've said something.

        I believe Thomas Moody died a natural death.
        """

        psychic """
        I suppose you're right.
        """

    return


label captain_generic_lad_friday_psychic:

    captain """
    Mister Harring seems like a fine young fellow.

    But you've talked to him more than I have.

    You must have a more accurate opinion of him.
    """

    psychic """
    That's true. Nevertheless, have you noticed anything specific about him?
    """

    captain """
    Well, I did notice that his clothes are a bit dated and worn.
    
    Either he doesn't care about his appearance, or he can't afford more recent clothing.

    I'll leave it to you to make your own judgment about that.
    """

    $ lad_details.description_hidden.unlock('poor')

    return


label captain_generic_doctor_friday:

    captain """
    At first glance, he seems like a decent gentleman.

    However, he looked a bit nervous to me.

    I noticed him fidgeting earlier, as if he were anxious about something.
    """

    return


label captain_generic_doctor_saturday:

    captain """
    I didn't know him very well but he seemed like a decent person.

    Such a pity he died like that.
    """

    return