label psychic_day3_afternoon_stay:

    call change_time(13,00, "Afternoon", "Sunday")

    $ change_room("tea_room", dissolve)

    call common_day3_afternoon_lad_psychic_stay

    $ change_room('dining_room', dissolve)

    """
    Rosalind Marsh and Ted Harring are already seated when I come back.

    We start eating in silence, each deep in our own thoughts.
    """
    
    pause 2.0

    """
    I don't eat much, nor does Mrs Marsh.

    But Ted Harring finishes his plate,

    then as soon as he is done, stands up.

    He looks anxious to do something.

    But as he stands, he suddenly looks dizzy.
    """

    call common_day3_afternoon_lad_falls

    $ play_music('danger', fadeout_val=2)

    psychic """
    Mister Harring?!
    """

    """
    Rosalind Marsh rushes to his side.

    Her nurse's training kicks in.
    """

    nurse """
    Mister Harring, can you hear me?
    """

    psychic """
    What's happened?

    How is he?
    """

    nurse """
    He's not well, I don't understand.
    """

    """
    She checks his pulse.
    """

    nurse """
    He has no pulse.

    He's dead.
    """
    
    psychic """
    What?! No, that can't be.

    How is this possible?
    """

    nurse """
    I'm not sure, but I doubt it's a coincidence at this point.

    I believe he's been poisoned.
    """

    psychic """
    No, no, no ...

    Mister Harring, why?
    """

    """
    My hands shake.

    Tears run down my cheeks.

    Rosalind Marsh keeps talking, but I can barely understand what she's saying.
    """

    # TODO add tears filters

    nurse """
    All I know is that he wasn't the target.
    
    I switched my plate with his before we started eating.

    I was the one supposed to die, not him.
    """

    psychic """
    You switched plates? Why?
    """

    nurse """
    Why?!

    After all that's happened, weren't you suspecting anything?
    """

    """
    I try to form a coherent response, but words elude me.
    """

    psychic """
    ...
    """

    # TODO too revealing for the nurse? Should she remain suspicious?
    # Why a scared nurse approached
    nurse """
    When I woke to find this place empty, I knew something was wrong.

    I heard the three of you rummaging around the house and I hid. 

    I didn't trust Sushil Sinha, but once he left I felt safe enough to reveal myself.

    But I should have been more suspicious of Ted Harring.

    After all, he was the least respectable of everyone here.

    Clearly out of place in this environment.

    And I bet I can prove it.
    """

    pause 1.0

    """
    She searches Ted Harring's pockets and takes out a gun.
    """

    nurse """
    Look. He even had a weapon on him the whole time.

    He...
    """

    pause 1.0

    """
    She pauses.
    """

    nurse """
    I don't know what his motives were, but...
    """

    pause 1.0 

    nurse """
    ...it doesn't matter now.
    """

    """ 
    She clearly struggles to speak.
    """

    nurse """
    Wait, something feels off.
    """

    pause 1.0

    """
    She grasps the chair next to her for support.
    """

    nurse """
    I think I'm going to faint.
    """

    pause 1.0

    nurse """
    What have you done?
    """


    """
    I barely register her words.

    It feels like I'm about to collapse myself.
    """

    psychic """
    Me? What about me?
    """

    """
    I turn towards her and see that she is pointing a gun at me.
    """

    nurse """
    Don't move. 
    """

    call run_menu( TimedMenu("psychic_day3_stay", [
        TimedMenuChoice("Try to take the gun by force. It's probably not loaded, right?", 'psychic_day3_afternoon_gun_death', early_exit=True ),
        TimedMenuChoice("It's too risky, try to talk her out of it.", 'psychic_day3_afternoon_convince_psychic', early_exit=True)
        ])
    )

    jump work_in_progress


label psychic_day3_afternoon_gun_death:

    play sound "gunshot.wav"

    psychic "I can't let you do this!"

    """
    In a swift motion, I lunge for the gun, our bodies colliding in a desperate tangle. The struggle is fierce, each of us fueled by our own convictions.
    """

    """
    The sound of a gunshot pierces the air, halting the chaos in an instant.
    """

    """
    Silence descends, heavy and suffocating. I stand frozen, the nurse's body slumping to the ground. The gun, a cold weight in my hand, drops to the floor with a thud.
    """

    psychic "No... This wasn't how it was supposed to end..."

    """
    Tears cloud my vision as I stare at the aftermath of our struggle. The room spins, a maelstrom of guilt and disbelief.
    """

    """
    The sound of footsteps approaches, but I can't move, trapped in a nightmare of my own making.
    """

    return


label psychic_day3_afternoon_convince_psychic:

    play music "tense_background_music.ogg" fadeout 2.0

    psychic "Please, we can talk this out. There's been a terrible misunderstanding."

    """
    The nurse's grip on the gun wavers, her eyes swimming with doubt and fear. For a fleeting moment, hope glimmers in the tense air.
    """

    nurse "I... I don't know what to believe anymore."

    psychic "Trust me, no one else needs to get hurt. We can find a peaceful solution to this."

    """
    But the shadow of fear is too deep, too consuming. Her finger tightens on the trigger, driven by a desperate instinct to survive.
    """

    play sound "gunshot.wav"

    """
    A loud bang shatters the fragile hope, and darkness rushes in as I collapse to the ground.
    """

    psychic "I... just wanted... to help..."

    """
    The world fades away, my final thoughts filled with sorrow for the spiral of fear and violence that brought us here.
    """

    return
