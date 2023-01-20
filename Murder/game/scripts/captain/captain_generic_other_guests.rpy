label captain_generic_other_guests:

    call run_menu(current_character.saved_variables["captain_generic_other_guests_menu"])

    return

label captain_generic_other_guests_friday:

    captain """
    Well, I don't know.

    I don't have a strong opinion on anyone at this point.

    Do you mean someone in particular?
    """

    call captain_generic_other_guests

    return

label captain_generic_drunk_friday_psychic:

    captain """
    Oh yes, our drunk friend.

    Not much to say here that you haven't noticed yourself.
    """

    return

label captain_generic_host_friday_psychic:

    captain """
    A charming lady for sure.

    Even though, there is someone about her that intrigues me.
    """

    psychic """
    Really?

    What exactly do you mean?
    """

    """
    He seems unsure.

    A bit embarrassed even.
    """

    captain """
    I am sorry, I meant nothing special.

    I shouldn't talk about our gracious host anyway.
    """

    psychic """
    Of course.
    """

    """
    He knows more than he wants to say.

    But he won't say it with other people around us.
    """

    return

label captain_generic_nurse_friday:

    captain """
    A discreet woman.

    She is dressed with style but in a humble way.

    You can directly tell she is at ease in those kind of gatherings.
    """

    $ nurse_details.unlock_knowledge('clothes')

    return

label captain_generic_broken_friday:

    captain """
    One of our war hero I would say.
    """

    # chatGPT
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

    $ broken_details.unlock_knowledge('mask') 

    return

label captain_generic_lad_friday_psychic:

    captain """
    Mister Harring looks like a fine young fellow.

    But you have talked to him more than I have.

    You must have a more accurate opinion of him.
    """

    psychic """
    That's true. Nevertheless, is there anything special you noticed about him?
    """

    captain """
    Well, I just noticed that his clothes are dated, and a bit worn off.
    
    Either he doesn't care about his appearance or he can't afford more recent clothes.

    I'll let you make your own mind about that.
    """

    $ lad_details.unlock_knowledge('poor')

    return

label captain_generic_doctor_friday:

    captain """
    At first glance, I would say he is an upper class gentleman.

    He seemed a bit nervous tough.

    I saw him fidgeting earlier, like he was nervous about something.
    """

    return