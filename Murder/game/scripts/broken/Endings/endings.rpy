# Endings for Thomas Moody (broken)

# DAY 1 — drank the poisoned whisky and never woke up
label broken_ending_day1_deathbed:

    $ broken_details.endings.unlock('deathbed')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('deathbed'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You don't wake up.

    You came to this house behind another man's face, certain you were the one doing the watching.

    You were wrong.
    """

    jump ending_generic


# DAY 1 — talked to the maid; the butler made certain he never woke
label broken_ending_day1_throat_cut:

    $ broken_details.endings.unlock('throat_cut')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('throat_cut'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You wake once, to a hand clamped across your mouth and a cold line drawn quick across your throat.

    Then you do not wake again.

    This tragic ending was likely caused because you did something careless.

    You just need to figure out what.
    """

    jump ending_generic
