# Endings for hero
label lad_ending_day1_deathbed:

    $ lad_details.endings.unlock('deathbed')
    $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('deathbed'))
    
    call death_screen_transition

    $ play_music('mysterious')

    """
    You don't wake up. 

    You have died during the night.

    It's unfair, I know. 
    
    You don't think that you have done anything wrong.

    And you probably haven't.

    But sometimes, people die without knowing why.
    """

    jump ending_generic

# DAY 3
label lad_gunned_down_ending:

    call death_screen_transition

    # TODO ONE declaration of ENDINGs (not in characterINformation)
    $ lad_details.endings.unlock('gunned_down')
    $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('gunned_down'))
    
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
    
    $ lad_details.endings.unlock('poisoned')
    $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('poisoned'))

    """
    You lay on the floor, saliva dripping from your mouth.

    Whatever poison you ingested is now coursing through your veins.

    Let this be a lesson to you.

    Never trust anyone.
    """

    $ is_intuition = True

    jump ending_generic


label lad_ending_day3_fell:

    call death_screen_transition

    $ lad_details.endings.unlock('fell')
    $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('fell'))

    """
    You fell.

    Right onto the picket fence.

    An iron pole pierced through your stomach.

    You didn't stand a chance.

    But you were so close to escaping.

    It must be incredibly frustrating.

    You'll need to be more cautious next time.
    """

    jump ending_generic


label lad_ending_day3_escape:

    $ change_room("police_station", irisin)

    """
    After what felt like an eternity, I finally reached the town.

    I rushed into the police station and told them everything.

    I was exhausted, panicked, and probably came off as unhinged.

    Yet, they agreed to investigate the matter.

    I was too drained and frightened to accompany them, but they told me everything when they came back.
    """

    pause 1

    # TODO check every death with last version
    """
    They discovered Sushil Sinha's body on the road, likely where I last saw him.

    He'd been shot in the head.

    At that moment, the two police officers took the situation very seriously.

    They rushed to Claythorn Manor.

    There, they discovered that all of the remaining guests had died.

    Samuel Manning, Thomas Moody, and Daniel Baldwin were still in their beds.

    Poor Miss Baxter was found lying lifeless in the hallway.
    
    She didn't even make it to her room.

    Rosalind Marsh was dead too. 
    
    Her body was found in the attic. 

    They have no idea where Lady Claythorn and her staff went.
    """

    call survive_screen_transition

    $ lad_details.endings.unlock('escape')
    $ lad_details.add_ending_checkpoint(ending = lad_details.endings.get_item('escape'))

    $ is_death = False
    jump ending_generic