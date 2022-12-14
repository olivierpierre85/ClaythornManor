# Ending for hero

label ending_generic:

    if first_death:

        """
        Don't worry, you'll have more chances at changing the fate of this character.

        You can start again now. Ideally, you have learn something that will help you in your next attempts.

        But maybe you have learned nothing.

        In this case, you'll better try to look at the story from a different point of view.

        You see, this story is not about only one hero.

        You'll get to play different characters.

        And you'll have to. 

        Because otherwise, you'll never discover to whole truth about what happened that week-end, at Claythorn Manor.
        """

        $ first_death = False

    hide screen centered_text
    jump character_selection

    return

label lad_ending_day1_poisoned:

    call death_screen_transition

    # play music mysterious_01

    """
    You don't wake up. 

    You died during the night.

    It's unfair, I know. 
    
    You don't think that you did anything wrong. 

    And you probably didn't.

    But in real life, people often die without knowing why.
    """

    jump ending_generic


# DAY 3
label lad_gun_downed_ending:

    call death_screen_transition

    """
    Well you are dead.

    Shot to death.

    And no explanation was given.

    If you feel you are owned one, think again.

    Why would someone explains their victims why they are killing them.

    That would make no sense.

    If you want a better explanation, then you will have to find it yourself.
    """

    jump ending_generic

label lad_ending_day3_poisoned:

    call death_screen_transition

    """
    You lay on the floor, saliva coming from you month.

    Whatever poison you ate, it now runs through your veins.

    Let that be a lesson to you.

    Never trust anyone.
    """

    $ lad_details.unlock_intuition('psychic_poisons')

    jump ending_generic

label lad_ending_day3_fell:

    call death_screen_transition

    """
    You fell.

    Right on the picked fence.

    An iron pole got through your belly.

    You didn't stand a chance.

    But you were so close to escaping though.

    How frustrating it must be.

    You'll have to be more careful next time.   
    """

    jump ending_generic