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
#       - Forest         : host, captain, lad, doctor, drunk
#       - Dead           : Broken (death branch only)
#
#   Notes :
#       - Captain observes Lady Claythorn's poor shooting and weak leadership.
#       - IF both host suspicions unlocked : opportunity to confront her later in the chapter.
# --------------------------------------------

label captain_day2_hunt:

    $ captain_details.add_checkpoint("captain_day2_hunt")

    call change_time(11, 00, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ change_room('bedroom_captain')

    $ play_music('upbeat', 1)

    """
    I retire briefly to my room to change.

    The household has laid out a tweed jacket of about my size, but I have brought my own and prefer it.

    A man should not be dressed by strangers, however well-meaning they may be.

    Properly turned out, I make my way down to the gun room.
    """

    $ change_room('gun_room')

    """
    The butler is already there, attending to the rifles with the unhurried care of a man who has done this many times before.

    He hands me a piece, well-kept and finely balanced.

    I weigh it briefly, then sight along the barrel and find it true.

    It has been some years since I last shouldered such a weapon, yet the hands do not forget.

    I have a passable hand at shooting. Not, perhaps, what my hosts expect of a decorated officer, but sufficient to avoid embarrassment.

    I shall have to be careful, in any event, not to outshine our hostess.
    """

    # TODO: meet the others in the garden, butler splits the parties, observe Lady Claythorn's shooting,
    #       optional confrontation if both host suspicion threads are unlocked.
    jump work_in_progress
