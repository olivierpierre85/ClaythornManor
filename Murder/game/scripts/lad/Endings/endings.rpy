# Ending for hero

label ending_generic:

    $ stop_music(2)

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

label survived_generic:

    $ stop_music(2)

    if first_survive:

        """
        You made it out alive.

        But it's not the ideal ending either.

        Don't get me wrong, that's still impressive.

        But surviving Claythorn Manor is nothing but the first step.

        You're goal is to save everyone.

        And that would require to start the story again.
        """

        $ first_survive = False

    hide screen centered_text
    jump character_selection

    return

label lad_ending_day1_poisoned:

    $ lad_details.unlock_ending('poisoned')
    $ lad_details.add_ending_checkpoint(ending = lad_details.get_ending('poisoned'))
    
    call death_screen_transition

    $ play_music('mysterious')

    """
    You don't wake up. 

    You died during the night.

    It's unfair, I know. 
    
    You don't think that you did anything wrong. 

    And you probably didn't.

    But sometimes, people die without knowing why.
    """

    jump ending_generic


# DAY 3
label lad_gun_downed_ending:

    call death_screen_transition

    # TODO ONE declaration of ENDINGs (not in characterINformation)
    $ lad_details.add_ending_checkpoint(ending = CharacterInformation(1, "gunned_down", "You die stoned to death", type="ending", image_file="gun_downed"))

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
    
    $ lad_details.add_ending_checkpoint(ending = CharacterInformation(2, "poisoned", "You were poisoned", type="ending", image_file="poisoned"))

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


label lad_ending_day3_escape:

    scene police_station

    """
    After what seemed like an eternity, I finally reached town.

    I rushed into the police station and told them everything.

    I was exhausted panicked, and I probably looked like a maniac.

    But they agreed to go and check anyway.
    """


    """
    I was too tired and too scared to follow them, but they told me everything when they came back.
    """

    pause 1

    """
    They found the body of Sushil Sinha on the road, probably where I last saw him.

    He was shot in the head.
    
    At that point, the two police officers took the matter seriously.

    They rushed to Claythorn Manor.

    There, they found that all of the guests were dead.

    Samuel Manning, Thomas Moody and Daniel Baldwin were still in their bed.

    They found Rosalind Marsh in the attic. 

    She was shot in the head.

    And poor Miss Baxter, she was lying dead in the hallway. 
    
    She was stabbed in the back.

    She didn't even had time to reach her room.

    We still have no idea where Lady Claythorn and her staff is.
    """

    call survive_screen_transition

    jump survived_generic
