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

    Doctor Baldwin and I will go right now then. I don't want to lose time.

    Hopefully, I'll be back with help before nightfall.
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



