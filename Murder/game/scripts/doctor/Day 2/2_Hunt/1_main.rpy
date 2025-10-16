# --------------------------------------------
#   Doctor
#           
#   Saturday - The Hunt
# 
#   11:00 -> 15:00
#
#   Music: upbeat
#
#   Position
#       - House, Tea room : nurse, psychic 
#       - Forest : host, captain, lad, doctor, drunk
#       - Dead : Broken
#
#   Notes : 
#       - Generic lad, 30 minutes
# --------------------------------------------
label doctor_day2_hunt:

    $ current_character.add_checkpoint("doctor_day2_hunt") 

    call change_time(11,00, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])
    
    $ change_room('manor_garden')

    $ play_music('upbeat', 1, fadein_val=10.0)

    """
    Since I could not find a reason to remain behind, I changed for the hunt.

    Fortunately I had thought to bring outdoor clothes for the weekend.

    It was not hard to imagine a shoot would be on the agenda.

    It amuses me that Lady Claythorn pretends it is for our benefit, when she will enjoy it most.

    I doubt she can readily find willing partners in so isolated a place.
    
    In any case, they pressed a hunting rifle upon me, and though it has been a while, I dare say I will remember how to use it.

    I step out to join the others.

    To my surprise, Samuel Manning is there as well. 
    
    He must have sobered up. At least, I hope so.

    I notice the butler following Lady Claythorn.
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        Andrew is there as well.
        """

    else:

        """
        The footman is there as well.
        """
    
    """
    He is tending to Ted Harring, who looks a little out of place.

    The butler clears his throat and addresses us.
    """

    call common_day2_hunt_butler_groups

    """
    I have barely a moment to gather my thoughts before Samuel Manning is upon me.
    """

    drunk """
    Doctor, I would be honoured to partner with you.

    You don't mind, do you?
    """

    """
    I cannot find the words to extricate myself.
    """

    doctor """
    Well... no, of course not.
    """

    drunk """
    Splendid!

    We shall have a jolly time.
    """

    lad """
    You don't mind if I join as well?
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        Andrew is with him and gives me a meaningful look.
        """
    
    doctor """
    Of course not.

    Do come with us, Mr Harring.
    """

    butler """
    Excellent.

    The parties are settled.

    Let us have a pleasant afternoon.
    """

    call doctor_day2_hunt_accident

    jump work_in_progress
