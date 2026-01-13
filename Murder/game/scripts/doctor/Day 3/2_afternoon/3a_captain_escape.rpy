# TODO what are the options

# Doctor leaves with captain, ted harring stays there
# Doctor stays??? No way too stressfull

# Everyone leaves => If you have Told all the information, TED harring DOESN't want to stay with Amelia
# She is reluctant but end up accepting, realising that everyone is against us, ending at 4 Lives saved BETTER

# OR Ted Harring stays, the doctor exit with the captain, noone shots at them. TWO saved
label doctor_day3_afternoon_captain_escape_without_psychic:

    lad """
    Of course, I'll stay.

    Only a monster would leave you alone here in this condition.
    """

    psychic normal """
    Thank you Mr Harring! 

    That means the world to me.
    """

    captain """
    Very well.

    Doctor Baldwin and I will go right now then. 
    
    I don't want to lose time, darkness will be upon us soon.

    Hopefully, we'll be back with help tonight.
    """

    psychic """
    Very well, we'll wait here. 
    
    Hopefully nothing will happen until then.
    """

    captain """
    That's decided then.

    Doctors, let's grab the bare necessities from our room and be on our way.
    
    The sooner, the better.
    """

    
    $ change_room("forest_road", dissolve)

    call change_time(15, 00)

    """
    We picked just a few things to help us for our trip.

    Most of our luggage remain at the manor, we'll get them back soon enough hopefully.
    """

    doctor """
    That was a rather fast exit there.
    """

    captain """
    Perhaps, but we were at an impasse.

    I don't think we could have learn more by staying.

    There was no point at delaying the inevitable.

    Plus, the night will be upon us in a short time, we shouldn't waste anytime.
    """

    doctor """
    Right.
    """

    """
    So we walked at a very fast pace, hoping to reach the town before.

    I was started to lose hope when we finally reached Aberdeen.

    After a quick search we were able to locate the police station.
    """

    call change_time(17, 00)

    $ change_room("police_station", irisin)

    """


    We must have looked like madmen, and it took a while before they took us seriously.

    They agreed to go and check on the others, while we rested there.

    I agreed...
    """

        
    return


label doctor_day3_afternoon_captain_escape_with_psychic:

    lad """
    I don't know, with everything they just told us, I don't believe we are safe, even the two of us staying here.
    """

    psychic """
    But I can't really travel.
    """

    """
    Ted Harring is looking to the floor, ashamed.
    """

    lad """
    I am sorry, I can't stay here any longer I can't.
    """

    psychic """
    What? Are you really gonna abandonned me?

    And you doctor? Or you Captain? Can't one of you stay with me?
    """

    """
    There is an akward silence.

    None of use reply.
    """

    psychic """
    Oh I see, so there is no chance to convince you is there?
    """

    captain """
    I would stay of course, but I am afraid they will need my military skills to make the trip.

    ....
    """

    return



