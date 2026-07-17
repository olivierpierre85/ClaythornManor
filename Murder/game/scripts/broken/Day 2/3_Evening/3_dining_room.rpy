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
    
    I stop to check if anyone is coming.
    """

    $ change_room('entrance_hall')

    """
    They come down in whatever they had to hand.

    Captain Sinha and Mr Manning are first out of the billiard room, and neither looks the least surprised.

    Miss Marsh next, with a coat over her nightdress, then Miss Baxter, wide awake, as though she had been sitting up waiting for exactly this.

    Doctor Baldwin does not come at all. Whatever he takes of an evening, he has taken it, and his lock will have to stand guard in his stead.

    Lady Claythorn appears last at the head of the stairs, dressed to the collar, not one hair out of place.
    """

    host """
    Mr Moody. I trust the house is on fire, at the very least.
    """

    broken """
    Not yet, madam.

    And I mean to see it stays that way.
    """

    """
    So I say it once, to everyone at the same time, exactly as the Captain advised.

    Mr Harring dead without cause. The staff gone from their floor. The telephone dead, the road blocked, and letters written to set us at one another's throats.

    Nobody laughs at me. Nobody calls it nonsense.

    That silence tells me more than any confession could.
    """

    captain """
    Then it is settled.

    Nobody sleeps alone and unguarded tonight.

    Every door locked, and a watch kept on the landing in turns until morning. Mr Manning and I shall take the first.
    """

    drunk """
    I'll stand mine sober, sir.

    That much I can still promise a man.
    """

    """
    Lady Claythorn watches it all from the stairs, and offers neither protest nor help.
    """

    host """
    Do as you please, gentlemen.

    I shall be in my room.
    """

    """
    She goes up without another word.

    The rest of us divide the night between us.

    Whatever comes for this house tonight will not find it asleep.
    """

    $ broken_details.threads.unlock('gather_everyone')

    return