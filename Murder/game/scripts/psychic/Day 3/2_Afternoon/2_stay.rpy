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
    I don't eat much, neither does Mrs Marsh.

    But Ted Harring finishes his plate off,
    
    then as soon as he is done, stands up.

    He looks anxious to do something.

    But as he is up, he suddenly looks dizzy.
    """

    call common_day3_afternoon_lad_falls

    $ play_music('danger', fadeout_val=2)

    # Rosalind is scared, she is also feeling weird
    psychic """
    Mister Harring?!
    """

    """
    Rosalind Marsh jumps to his side.

    Her nurse's training kicking in.
    """

    nurse """
    Mister Harring, can you hear me?
    """

    psychic """
    What's happened?

    How is he?
    """

    nurse """
    Not well, I don't understand.
    """

    """
    She checks his pulse.
    """

    nurse """
    He has no heartbeat.
    """
    
    psychic """
    What?! No that can't be.

    How is this possible?
    """

    nurse """
    I am not sure, but I doubt it's a coincidence at this point.
    """

    psychic """
    What do you mean?
    """

    nurse """
    I think you know very well what I mean.

    He was killed, probably poisoned.
    """

    psychic """
    No, that makes no sense.
    """

    nurse """
    Well, all I know is that he was not the target.
    
    I switched my plate with his before eating.

    I was the one supposed to die, not him.
    """

    psychic """
    You switched plate? Why?
    """

    nurse """
    Why?

    After all that has happened, you weren't suspecting anything?
    """

    """
    I try to make a coherent response, but words are eluding me.
    """

    psychic """
    ...
    """

    # TODO too revealing for the nurse? she should remain suspicious
    # WHy a scared nurse approached
    nurse """
    When I woke and found an empty house, it was clear something was terribly wrong.

    I heard the three of you rumaging around the house and I hid. 

    I didn't trust Sushil Sinha, but when he left I felt safe enough to show myself.

    But I should have suspected Ted Harring more.

    After all, he was the least respectable of everyone here.

    Clearly at of place in this environment.
    """

    pause 1.0

    """
    She pauses.
    """

    nurse """
    I don't know what his motives were, but...
    """

    nurse """
    ... it doesn't matter now.
    """

    """ 
    Now, she has clear difficulties to speak.
    """

    nurse """
    Wait, now I am feeling weak.
    """

    pause 1.0

    """
    She grasps the chair next to her.
    """

    nurse """
    I am about to faint.

    What did you do?
    """

    """
    I barely notice what she is saying.

    I feel like I am about to collapse myself.
    """

    psychic """
    Me? What about me?
    """

    """
    I turn my head towards her and see she is pointing a gun at me.
    """

    nurse """
    Don't move. 
    """

    psychic """
    Is it a gun?
    """



    # SHE FIGHTS ROSALIND, who dies?

    # 1. Rosalind. 
    # you don't try to argue, you jump her she's dead.
    # then runs outside
    # He is coming towards me, kills him with rosalind gun NOT GREAT
    # Then go back home and see that ted harring is still dead THEN loses it
    # and burn the place down

    # 2. You try to argue with her. She shots you dead

    jump work_in_progress