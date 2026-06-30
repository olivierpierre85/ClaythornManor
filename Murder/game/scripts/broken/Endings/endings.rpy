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


# SATURDAY HUNT — killed the Captain; the butler tidied away the loose end
label broken_ending_silenced:

    $ broken_details.endings.unlock('silenced')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('silenced'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You did precisely what that letter was written to make you do.

    And the moment the Captain lay dead, your usefulness died with him.

    A tool is put back in the drawer once the work is finished.

    Someone went to a great deal of trouble to set that old order in your hands and point you at the wrong man. You might have asked who, and why, before you pulled the trigger.
    """

    jump ending_generic


# SATURDAY HUNT — spared the Captain, but the butler caught him in the rush
label broken_ending_overtaken:

    $ broken_details.endings.unlock('overtaken')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('overtaken'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You would not be made a murderer, and that was to your credit.

    But sparing the Captain did not spare you.

    You ran to save a stranger, alone, through a wood that belonged to them, while the one man who might have stood at your side fled the other way.

    There was never a version of this morning in which they let the masked man walk back out of the trees.
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
