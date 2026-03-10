label nurse_ending_exhausted:

    $ nurse_details.endings.unlock('exhausted')
    $ nurse_details.add_ending_checkpoint(ending=nurse_details.endings.get_item('exhausted'))

    call death_screen_transition

    """
    You pushed yourself beyond the limits of your endurance.

    The illness that has been shadowing your every step finally claimed its due.

    There was no one to hear your final, desperate cough.

    No one to offer a glass of water, or a steadying hand.

    In the cold silence of Claythorn Manor, you were simply too tired to go on.

    Perhaps if you had taken a moment to rest, the outcome might have been different.
    """

    jump ending_generic
