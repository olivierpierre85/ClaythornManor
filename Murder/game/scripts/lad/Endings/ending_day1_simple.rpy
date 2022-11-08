# Ending for hero

# DAY 1
# Either the lad as drank sherry after dinner and die, or he hasn't and is still alive
label lad_ending_day1_poisoned:

    call death_screen_transition

    #TODO factorize depending on how many death
    """
    You don't wake up. 

    You died during the night.

    It's unfair, I know. You don't think that you did anything wrong. 

    And you probably didn't.

    But in life, people often die without knowing why. 

    Even thought we always believe being the hero in our story, sometimes we are just pawns.

    Don't worry, you'll have more chances at changing the fate of this character.

    You can start again now. Ideally, you have learn something that will help you in your next attempts.

    But maybe you have learned nothing.

    In this case, you'll better try to look at the story from a different point of view.

    You see, this story is not about only one hero.

    You'll get to play different characters.

    And you'll have to. 

    Because otherwise, you'll never discover to whole truth of what happened this week-end, at Claythorn Castle.

    """


    # TODO make a function that reset var, and hide text
    hide screen centered_text
    jump character_selection

# DAY 3
label lad_gun_downed_ending:

    call death_screen_transition

    """
    Well you are dead.

    Shot to death.

    And no explanation was given.

    If you feel you are owned one think again.

    Why would someone explains their victims why they are killing them.

    That would make no sense.

    If you want a better explanation, then you will have to get it yourself.
    """

    hide screen centered_text

    jump character_selection

label lad_ending_day3_poisoned:

    call death_screen_transition

    #TODO factorize depending on how many death
    """
    You don't feel too good

    """


    # TODO make a function that reset var, and hide text
    hide screen centered_text
    jump character_selection
