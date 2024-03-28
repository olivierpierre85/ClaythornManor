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
    nurse """
    Mister Harring ?!

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