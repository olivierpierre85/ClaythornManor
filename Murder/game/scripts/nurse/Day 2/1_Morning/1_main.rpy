label nurse_day2_morning:

    call change_time(9,00, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ nurse_details.add_checkpoint("nurse_day2_morning") 

    call black_screen_transition("Rosalind Marsh")

    $ change_room("bedroom_nurse", irisout)

    $ play_music('upbeat', 3)

    """
    My sleep was restless. Fever dreams.
    
    But I am awake now. The coughing has subsided for the moment.
    """

    if nurse_details.threads.is_unlocked('drugged_guest'):
        """
        I wonder how our host slept. Like a baby, I imagine.
        """

    """
    I head to the dining room. I need sustenance.
    """

    call change_time(9,30)

    $ change_room('dining_room')

    """
    Most guests are present. I observe them over the rim of my teacup.
    """

    # We could insert common interactions here, but let's keep it streamlined for her perspective.

    call change_time(10,00)

    """
    Lady Claythorn enters. She looks... distracted.
    """

    call common_day2_morning_host_hunt

    """
    A hunt. Barbaric.
    
    And exhausting. I have no intention of trudging through mud and damp leaves.
    
    Besides, with the mansion half-empty, it's the perfect opportunity to explore undisturbed.
    """

    jump nurse_day2_no_hunt
