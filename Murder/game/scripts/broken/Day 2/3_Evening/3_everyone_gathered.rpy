# ------------------------------------
#   THE GONG
# ------------------------------------
label broken_day2_evening_ring_gong:

    $ change_room('dining_room')

    """
    The gong stands by the dining room door, the beater hanging at its side.

    I must make sure everybody hears it.
    """

    play sound dinner_gong

    play sound dinner_gong

    play sound dinner_gong

    """
    The sound rolls through the house like a wave, twice, three times.
    
    I stop to check the entrance hall to see if anyone is coming down.
    """

    $ change_room('entrance_hall')

    """
    The first person coming down is Amelia Baxter.

    She gives us a puzzled look.
    """

    psychic angry """
    What is happening here?

    Who ran the gong like that?

    If this is some sort of drunken joke its in very pour taste.
    """

    """
    She looks intensily at Samuel Manning  as she is saying that.
    """

    captain """
    I am sorry Miss Baxter, but I am afraid it is not joke.

    There is some very serious matter we need to discuss urgently with everybody.
    """

    psychic -angry """
    How serious you sound captain.

    What is this about?
    """

    broken """
    We will wait everyone is here before discussing it all.
    """

    """
    Rosalind Marsh is now coming down too, looking tired and perplexed.

    She is followed by Doctor Baldwin.

    Of the three, he is the one looking the worse, holding the stair rail as to not fall.
    """

    doctor """
    What is the meaning of this?
    
    I taught the house might have been on fire.
    """

    captain """
    Nothing so dramatic Doctor.

    But we do need to talk to everyone.
    """

    nurse """
    Well in that case there is only Lady Claythorn missing.

    And the staff too of course, where could they be?
    """

    broken """
    That is what we need to discuss.

    We believe the staff has left.

    Now we have proof.
    """

    captain """
    And it is most then likely than Lady Claythorn is gone as well.
    """

    nurse """
    That is correct, I checked her room before coming down.

    I taught she would already be here.
    """

    captain """
    I am not sure surprised.
    
    We probably are the only living persons left in this house tonight.
    """

    """
    A silence follows this 
    """

    doctor """
    I am sorry Captain, but I am gonna need more explanation that this.
    """

    captain """
    Of course, Mr Moody will explain everything.

    After all he is the closest we have as a investigator.
    """

    doctor """
    An investigator?

    I taught you were a footman turned car mechanic Mr Moody.
    """

    broken """
    I am afraid I led you on Doctor.

    An necessity to avoid attract attention.

    Nobody is suspicious of car mechanic asking questions.
    """

    doctor """
    Right, but what were you investigating at all?

    I do not understand.
    """


    ### TODO
    # People coming down:
    # Psychic, Nurse, Doctor (tired)
    # + Already there : Broken, drunk, captain
    # Missing dead ted harring, and Miss CLaythorn has left




    $ broken_details.threads.unlock('gather_everyone')

    return