label psychic_day3_afternoon_stay:

    call change_time(13,00, "Afternoon", "Sunday")

    $ change_room("tea_room", dissolve)

    call common_day3_afternoon_lad_psychic_stay

    """
    We both go on to our room, leaving Rosalind Marsh alone in the dining room.
    """

    call wait_screen_transition()

    """
    I did not waste time going to my room and back, but Rosalind Marsh and Ted Harring are already seated when I come back.

    Ted Harring must have been very fast, I suppose he was scared to stay alone for too long.

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

    call common_day3_afternoon_nurse_revelation

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

    $ time_left = 1
    call run_menu( TimedMenu("psychic_day3_gun", [        
        TimedMenuChoice("Try to talk her", 'psychic_day3_afternoon_convince_nurse', early_exit=True),
        TimedMenuChoice("Try to take the gun by force. It's probably not loaded anyway", 'psychic_day3_afternoon_gun_death', early_exit=True )
        ])
    )


label psychic_day3_afternoon_gun_death:

    $ psychic_details.threads.unlock('steal_gun')

    """
    Without hesitation, I jump at her.

    It happened so swiftly that she didn't have time to react.
    """
    
    nurse surprised """
    Wait! I'll shoot.
    """

    """
    But I am already upon her, grappling for the gun.
    """

    $ stop_music()

    nurse """
    Stop, or I'll ...
    """

    play sound gun

    """
    The sound of a gunshot pierces the air, ending the fight.

    Silence descends, heavy and suffocating. 
    
    I stand frozen, the nurse's body slumping to the ground. 
    
    The gun, now a cold weight in my hand, drops to the floor alongside her.
    """

    play sound body_fall

    $ play_music('sad', 3)

    pause 1.0

    # NOTE: She looks at THE body in disbelief. BUT it's not the nurse's body, it's TED HARRING's
    psychic """
    No... 
    """

    """
    Tears cloud my vision as I stare at the horrific scene before me. 
    
    When I look upon the dead body, the room spins, I am overwhelmed with guilt and disbelief.

    As I feel myself falling, I attempt to grasp the table but end up catching the tablecloth instead.

    It is not strong enough to prevent my fall.
    """

    play sound broken_glass

    pause 1.0

    """
    I am on the floor, having dragged most of the table's contents down with me.

    Broken glass all around me now, shattered plates, spilled food...

    I try to stand up but injure my hands on a shard of glass.

    Once again, I fall onto my back.
    """

    play sound body_fall

    """
    Perhaps I should just rest here.

    I have almost no strength left, anyway.

    But I smell something.

    Something is burning.

    Only then do I see it,
    
    a candle from the table, 

    now lying on the floor.
    """

    play sound fire loop

    """
    And all around it, flames, 

    spreading from the carpet to the entrance door.

    The fire is spreading rapidly.

    I make one last effort to stand and manage to get to my feet.

    But I can see no way out.

    Everything surrounding me is engulfed in smoke, so thick it's hard to breathe.

    Upon this sight, the little strength I had left ebbs away.

    As I am about to lose consciousness, my last feeling is a strong sense.

    I never should have stayed here, I should have left when I had the chance.
    """

    play sound body_fall

    jump psychic_ending_burns


label psychic_day3_afternoon_convince_nurse:

    psychic """
    Don't do this. There's been a terrible misunderstanding.
    """

    """
    The nurse's grip on the gun wavers, her eyes swimming with doubt and fear.
    """

    nurse """
    I... I don't know what to believe anymore.

    None of this makes sense.

    But I can't trust you.
    """

    psychic """
    Yes, you can. No one else needs to get hurt.
    
    We can find a peaceful solution to this.
    """

    """
    As I am talking, I also move slowly towards her.
    """

    nurse """
    Wait!

    Don't come so close, don't...
    """

    play sound gun

    """
    A loud bang resonates in the room.

    I look into Rosalind Marsh's eyes and see she's terrified.
    """

    nurse """
    No!

    Look what you made me do!
    """

    psychic """
    I... just wanted... to...
    """

    """
    I look down at my stomach.

    It's all covered in blood.
    """

    jump psychic_ending_shot

