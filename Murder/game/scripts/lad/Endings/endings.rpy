# Ending for hero

label ending_generic:

    $ stop_music(2)

    if first_death:

        """
        Don't worry, you'll have more chances to change the fate of this character.

        You can start again now. Ideally, you've learned something that will help you in your next attempts.

        But perhaps you haven't learned anything.

        In that case, try to look at the story from a different perspective.

        This story isn't about just one hero.

        You'll get to play as different characters.

        And you must.

        Because otherwise, you'll never uncover the whole truth about what happened that weekend at Claythorn Manor.
        """

        $ first_death = False

    python:
        if not seen_tutorial_timeline:
            seen_tutorial_timeline = True
            renpy.call('tutorial_map')

        if full_testing_mode:
            f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/full_testing.txt", "a")
            f.write('You are DEAD - TODO save last death info\n')
            f.close()

    hide screen centered_text

    jump character_selection

    return


label survived_generic:

    $ stop_music(2)

    if first_survive:

        """
        You made it out alive.

        But it's not the perfect ending either.

        Don't get me wrong, it's still an impressive feat.

        But surviving Claythorn Manor is merely the first step.

        Your goal is to save everyone.

        To do that, you might need to start the story over.
        """

        $ first_survive = False

    hide screen centered_text

    jump character_selection

    return

label lad_ending_day1_poisoned:

    $ lad_details.endings.unlock('poisoned')
    $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('poisoned'))
    
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
    Well, you're dead.

    Shot to death.

    And no explanation was given.

    If you feel you're owed one, think again.

    Why would someone explain to their victims why they're being killed?

    It wouldn't make sense.

    If you want a clearer understanding, you'll have to seek it out yourself.
    """

    jump ending_generic

label lad_ending_day3_poisoned:

    call death_screen_transition
    
    $ lad_details.add_ending_checkpoint(ending = CharacterInformation(2, "poisoned", "You were poisoned", type="ending", image_file="poisoned"))

    """
    You lay on the floor, saliva dripping from your mouth.

    Whatever poison you ingested is now coursing through your veins.

    Let this be a lesson to you.

    Never trust anyone.
    """

    $ lad_details.intuitions.unlock('psychic_poisons')

    jump ending_generic

label lad_ending_day3_fell:

    call death_screen_transition

    """
    You fell.

    Right onto the picket fence.

    An iron pole pierced through your belly.

    You didn't stand a chance.

    But you were so close to escaping.

    It must be incredibly frustrating.

    You'll need to be more cautious next time.
    """

    jump ending_generic


label lad_ending_day3_escape:

    scene police_station

    """
    After what felt like an eternity, I finally reached the town.

    I rushed into the police station and told them everything.

    I was exhausted, panicked, and probably came off as unhinged.

    But they agreed to investigate the matter.

    I was too drained and frightened to accompany them, but they told me everything when they came back.
    """

    pause 1

    # TODO check every death with last version
    """
    They discovered Sushil Sinha's body on the road, likely where I last saw him.

    He'd been shot in the head.

    At that moment, the two police officers took the situation very seriously.

    They hastened to Claythorn Manor.

    There, they discovered that all of the remaining guests had died.

    Samuel Manning, Thomas Moody, and Daniel Baldwin were still in their beds.

    Poor Miss Baxter was found in the hallway, probably poisoned.
    
    She didn't even make it to her room.

    Rosalind Marsh was apparently hiding in the attic. 

    But that didn't help her, as she had in the back.    

    We still have no idea where Lady Claythorn and her staff are.
    """

    call survive_screen_transition

    jump survived_generic