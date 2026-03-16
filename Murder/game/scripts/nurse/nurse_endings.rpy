label nurse_ending_exhausted:

    $ nurse_details.endings.unlock('exhausted')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('exhausted'))

    call death_screen_transition

    """
    You pushed yourself beyond the limits of your endurance.

    The illness that has been shadowing your every step finally claimed its due.

    There was no one to hear your final, desperate cough.

    No one to offer a glass of water, or a steadying hand.

    In the cold silence of the night, you were simply too tired to go on.

    Perhaps if you had managed your strength from the start, the outcome might have been different.
    """

    jump ending_generic


label nurse_ending_billiard_room_death:

    $ nurse_details.endings.unlock('billiard_room_death')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('billiard_room_death'))

    call death_screen_transition

    """
    You confronted a dangerous man, alone.

    In a room without witnesses.

    Already weakened by a deadly disease, the shock was enough to be the end of you.

    You died on the floor, your accusations still warm on your lips.
    """

    jump ending_generic


label nurse_ending_poisoned:

    $ nurse_details.endings.unlock('poisoned')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('poisoned'))

    call death_screen_transition

    """
    You swapped plates, thinking yourself clever.

    But the poison was in every dish.

    There was never a way out of that dining room.

    Your instincts were sharp, but not sharp enough.

    In the end, the silver you stole will sit unclaimed in an empty attic, gathering dust.
    """

    jump ending_generic


label nurse_ending_escape_poor:

    $ nurse_details.endings.unlock('escape_poor')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('escape_poor'))

    call survive_screen_transition

    """
    You escaped, but took very little with you. 
    
    Clearly not enough to make a difference to your finances.
    
    You can forget the dreams of vacations in the sun.

    Yet, you are better off than those who stayed.

    Not the ideal ending, but not the worst either, I suppose.
    """

    jump ending_generic