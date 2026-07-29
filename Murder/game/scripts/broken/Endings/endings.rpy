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

    This tragic ending likely happened because you did something careless.

    You just need to figure out what.
    """

    jump ending_generic


# SATURDAY DINNER — the rat poison left in the scullery found its way into
# the meal (no found_poison)
label broken_ending_poisoned:

    $ broken_details.endings.unlock('poisoned')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('poisoned'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You never rise from the floor.

    People died around you, all at the same time and under horrific circumstances.

    This made you think of the war.

    Only here you had no idea who the enemy was.

    That made the experience even more terrifying.

    Now, you may try to understand why this terrible ending occurred.

    You probably think you did not make a misstep here.

    But sometimes, things put in motion a long time ago can have consequences much later.

    You should keep that in mind.
    """

    jump ending_generic


# SATURDAY NIGHT — nobody kept watch, the manor was put to the torch,
# and the leap from the window ended on the iron fence
label broken_ending_impaled:

    $ broken_details.endings.unlock('impaled')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('impaled'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You avoided being burnt alive, but ended up impaled on an iron fence.

    Hard to say which ending would have been better.

    It hardly matters anyway.
    """

    jump ending_generic


# SUNDAY MORNING - took off the mask to win the argument; the Captain
# arrested the impostor, tied him to his bed and walked out alone
label broken_ending_burned:

    $ broken_details.endings.unlock('burned')
    $ broken_details.add_ending_checkpoint(ending = broken_details.endings.get_item('burned'))

    call death_screen_transition

    $ play_music('mysterious')

    """
    You took off your mask in front of frightened people, hoping they would understand.

    But these were no ordinary circumstances.

    And it gave the most sensible man in the house every reason to bind you to a bed.

    The worst part is that, had you been in his place, you know you would probably have done the same.
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
    It was a long and arduous road.

    But you brought them out together.

    A captain, a psychic, a doctor, a nurse and one drunkard.

    The only casualty was Ted Harring.

    You later found out it was indeed the rat poison that killed him.

    But who gave it to him remains a mystery.

    Everything points towards Lady Claythorn.

    But there is a catch.

    In all your enquiries, you never thought to look into her properly.

    The police did that job for you, and found there was no Lady Claythorn at all.

    The owner of the manor is a certain Lady Kilbraith.

    She lives peacefully in an apartment in London.

    You visited her and learned that Claythorn Manor had been empty for years.

    She had been trying to sell it and had no idea anyone had been staying there.

    You kept searching for years, but you never learned what the weekend was truly about.
    """

    # TODO add a UNLOCK FOR LADY CLAYTHORN?

    jump ending_generic
