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

    if nurse_details.important_choices.is_unlocked('swapped_plates'):

        """
        You swapped plates, thinking yourself clever.

        But that didn't help your fate.
        """

    else:

        """
        You suspected the food, but chose not to act.

        So your fate was sealed.
        """

    jump ending_generic


label nurse_ending_gunned_down:

    $ nurse_details.endings.unlock('gunned_down')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('gunned_down'))

    call death_screen_transition

    """
    You went to a great deal of trouble to find a gun and the bullets to load it.

    But that didn't change a thing.

    In the confusion, the weapon turned against you.

    A firearm is dangerous for those who don't know how to handle one.
    """

    jump ending_generic


label nurse_ending_escape_at_night:

    $ nurse_details.endings.unlock('escape_at_night')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('escape_at_night'))

    call death_screen_transition

    """
    You escaped the manor, but the night swallowed you whole.

    Lost in the woods, cold and exhausted, you sat down to rest and never rose again.

    They found you the next morning, curled beneath an oak, frost on your eyelashes.

    You saw the truth — Lady Claythorn fleeing her own house — and it should have told you everything.

    Don't wait too long. 
    
    Leave this place as fast as you can.
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


label nurse_ending_psychic_fight_death:

    $ nurse_details.endings.unlock('psychic_fight_death')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('psychic_fight_death'))

    call death_screen_transition

    """
    You fought back — unarmed, poisoned, and already half-dead.

    It was never going to be enough.

    The poison had already done its work, and the struggle finished what remained.

    You died on the dining room floor, still reaching for the woman who killed you.
    """

    jump ending_generic


label nurse_ending_escape_collapse:

    $ nurse_details.endings.unlock('escape_collapse')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('escape_collapse'))

    call death_screen_transition

    """
    You made it past the gate and onto the road.

    For a while, the cold air and the promise of freedom kept you moving.

    But your body had nothing left to give.

    The cough came first, then the weakness in your legs, then the ground.

    They found you the next morning, face down in the mud, your bag of stolen silver still clutched to your chest.

    So close. But not close enough.
    """

    jump ending_generic


label nurse_ending_escape_rich:

    $ nurse_details.endings.unlock('escape_rich')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('escape_rich'))

    call survive_screen_transition

    """
    You escaped, and you took enough with you to make a real difference.

    That's about as good as this weekend could have ended.

    As long as you don't think too hard about what happened to the others.
    """

    jump ending_generic