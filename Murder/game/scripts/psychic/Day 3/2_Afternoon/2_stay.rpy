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

    """
    Without hesitation I jump at her.

    It was so fast that she didn't have time to react
    """
    
    nurse surprised """
    Wait! I'll shoot.
    """

    """
    But I am already on her, grasping for the gun.
    """

    nurse """
    Stop, I'll ...
    """

    play sound gun

    """
    The sound of a gunshot pierces the air, stopping the fight.

    Silence descends, heavy and suffocating. 
    
    I stand frozen, the nurse's body slumping to the ground. 
    
    The gun, a cold weight in my hand, drops to the floor with her.
    """

    play sound body_fall

    pause 1.0

    # NOTE: She looks at THE body in disbelief. BUT it's not the nurse's body, it's TED HARRING's
    psychic """
    No... 

    Tears cloud my vision as I stare at the horror scene in front me. 
    
    When I look at the dead body, the room spins, I am overwhelmed with guilt and disbelief.

    As I feel myself falling, I try to grasp the table, but end up catching the table cloth instead.

    It's not strong enough to prevent me from falling.
    """

    play sound body_fall

    pause 1.0

    """
    I am on the floor, and in the process, I dragged most of the table contents with me.

    There is broken glass all around me now, broken plates, food...

    I try to stand up but hurt my hands on a shard of glass.

    I fall again on my back.
    """

    play sound body_fall

    """
    Maybe I should just rest there.

    I have almost no strength left anyway.

    But I smell something.

    Something burning.

    Only then I see it,
    
    a candle. 

    On its side.

    And all around it, flames, 

    going from the carpet to the entrance door.

    This went extremely fast.

    I try to stand up one last time and I manage to be on my feet.

    But I can't see a way out.

    Everything around me is engulfed in smoke so dense it's hard to breathe.

    Then, the little strength I had left leaves me.
    """

    play sound body_fall

    return


label psychic_day3_afternoon_convince_psychic:
    #REDO ENTIRELY
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