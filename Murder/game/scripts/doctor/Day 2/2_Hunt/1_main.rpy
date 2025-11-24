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
    As I had no reason to remain behind, I changed for the hunt.

    Fortunately, I had thought to bring more suitable outdoor clothes for the weekend.

    It was not difficult to imagine that a hunt would be on the agenda.

    Lady Claythorn may pretend it is arranged for our benefit, yet I suspect she will enjoy it most of all.

    She might even have planned the entire weekend simply for the pleasure of today's event.

    After all, I doubt she can readily find hunting partners in so isolated a place.
    
    In any case, the butler has provided me with a hunting rifle.

    It has been some time since I last handled one, yet I dare say I will remember how to use it.

    I step outside to join the others.

    To my surprise, Samuel Manning is there as well.
    """

    if doctor_details.objects.is_unlocked('drunk_letter'):

        """
        I must watch him carefully.

        However drunk he appeared this morning, it does not mean he is any less dangerous.
        """

    else:

        """
        I can only hope he has sobered up.
        """

    """
    I notice the butler walking just behind Lady Claythorn.
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        Andrew is there too.
        """

    else:

        """
        The footman is there as well.
        """
    
    """
    He is attending to Ted Harring, who looks somewhat out of place.

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

    if doctor_details.objects.is_unlocked('drunk_letter'):

        """
        He is too eager to join me.

        It may mean he is ready to make good on his threat.

        I am anxious, yet also curious.

        I cannot back out now.
        """

        doctor """
        No, of course. We may go together.
        """

    else:

        """
        I cannot find the words to politely refuse him.
        """

        doctor """
        Well... no, of course not.
        """

    drunk """
    Splendid!

    We shall have a jolly time.
    """

    lad """
    You don't mind if I tag along as well, do you?
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        Andrew stands at his side and gives me a meaningful look.
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