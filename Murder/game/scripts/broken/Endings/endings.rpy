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
label broken_ending_shot:

    $ broken_details.endings.unlock('shot')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('shot'))


    call death_screen_transition

    $ play_music('mysterious')

    """
    You did precisely what that letter was written to make you do.

    And the moment the Captain lay dead, your usefulness died with him.
    """

    jump ending_generic


# SATURDAY HUNT — spared the Captain, but the butler caught him in the rush
label broken_ending_strangled:

    $ broken_details.endings.unlock('strangled')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('strangled'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You would not be made a murderer, and that was to your credit.

    But sparing the Captain did not spare you.
    """

    jump ending_generic


# SATURDAY HUNT — shadowed the western grove, failed to talk Manning down,
# and threw himself into the shot meant for Doctor Baldwin
label broken_ending_shielded:

    $ broken_details.endings.unlock('shielded')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('shielded'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You put yourself between a broken man and the mark someone else had chosen for him, and it cost you everything.

    It was a brave thing.

    It was not a clever one.

    Manning was never the danger.

    The danger was whoever loaded him and left him in that wood, and that person is still beneath this roof, unhurt and unhurried.

    You might have saved the doctor and yourself both, had you only made him talk before he raised the gun.
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


# SATURDAY NIGHT — slept while the butler put the manor to the torch
label broken_ending_burned:

    $ broken_details.endings.unlock('burned')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('burned'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You never leave your bed.

    By morning Claythorn Manor is a shell of blackened stone, and every question you meant to ask has gone up with it.

    You felt all day that something in this house was wrong, yet you found nothing solid enough to keep you from your bed.

    Perhaps you walked past it, somewhere below stairs, on your very first night.
    """

    jump ending_generic


# SUNDAY - set out with only the Captain; the road was waiting for them
# (intuition ending: separating is the mistake, take everyone)
label broken_ending_ambushed:

    $ broken_details.endings.unlock('ambushed')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('ambushed'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You were right to leave. You were wrong to leave like that.

    Whoever holds this estate has shown you twice already that they like their work done quietly, away from watching eyes.

    Two men on an empty road are quiet work.

    Six people are witnesses. Six people are complications.

    Next time, take everyone with you. Every single one.
    """

    jump ending_generic


# SUNDAY - the final ending: everyone walks out together and reaches the police station
label broken_ending_walked_out:

    $ broken_details.endings.unlock('walked_out')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('walked_out'))

    call survive_screen_transition

    """
    Seven miles of bad road, and every one of them a small victory.

    You brought them out together. The Captain, the doctor, both ladies, and one sober lawyer. Every soul left alive under that roof.

    You never learned who wrote the letters, who ended Ted Harring, or what the weekend was truly for.

    But you are a journalist. You know the difference between an ending and a deadline.

    This story is not finished. It has simply passed to other hands, and other eyes, on other nights in Claythorn Manor.
    """

    jump ending_generic
