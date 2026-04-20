# --------------------------------------------
#   Captain
#
#   Saturday - The Hunt
#
#   11:00 -> 15:00
#
#   Music: upbeat
#
#   Position
#       - House, Tea room : nurse, psychic
#       - Forest         : host, captain, lad, doctor, drunk (+broken if alive)
#       - Dead           : Broken (death branch only)
#
#   Notes :
#       - Branches on tell_boxer_story:
#           - told    (Moody dead)  : Captain paired with Lady + butler; optional confrontation
#           - refused (Moody alive) : Moody insists on joining Captain + Lady; linear death
# --------------------------------------------

label captain_day2_hunt:

    $ captain_details.add_checkpoint("captain_day2_hunt")

    call change_time(11, 00, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ change_room('bedroom_captain')

    $ play_music('upbeat', 1)

    """
    I retire briefly to my room to change.

    The household has laid out a tweed jacket of about my size.
    
    I have brought my own but don't want to offend our hostess, so I put this one on.

    Properly turned out, I make my way down to the gun room.
    """

    $ change_room('gun_room')

    """
    The butler is already there, attending to the rifles with unhurried care.

    He hands me a piece, well-kept and finely balanced.

    I weigh it briefly, then sight along the barrel and find it true.

    It has been some years since I last shouldered such a weapon, yet the hands do not forget.

    I have a passable hand at shooting. Not, perhaps, what my hosts expect of a decorated officer, but sufficient to avoid embarrassment.
    """

    $ change_room('manor_garden')

    """
    I step out into the garden, where the others are already gathering.

    Doctor Baldwin is checking the action of his rifle quietly.

    Samuel Manning stands a little apart, a flask in one hand and a gun in the other. A poor pairing.

    Mr Harring hovers at the edge of the group, plainly ill at ease. A footman attends him closely, as well he should.

    Lady Claythorn is the last to emerge, dressed all in tweed.
    """

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):
        
        """
        At least, her outfit is perfect. But we will see if she can act the part.
        """

    if not captain_details.threads.is_unlocked('tell_boxer_story'):

        """
        Next to her, stands Thomas Moody.

        He catches my eye and offers a small nod.

        I return it. Steady. No hesitation.

        Whatever he knows, or believes he knows, I will not give him the satisfaction of a flinch.

        But I feel uneasy nevertheless.
        """

    call common_day2_hunt_butler_groups

    if captain_details.threads.is_unlocked('tell_boxer_story'):

        call captain_day2_hunt_moody_dead

    else:

        call captain_day2_hunt_moody_alive

    jump work_in_progress
    
