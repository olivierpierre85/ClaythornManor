label doctor_day2_hunt_accident:

    $ change_room("forest")
    
    call change_time(12,00, 'Hunt', 'Saturday')

    $ play_music('chill')


    """
    Our little group made its way into the forest.

    We walked for a while yet encountered nothing.

    So we stopped for luncheon.

    If Samuel Manning seemed somewhat sobered at first, he now appears intent on making up for lost drinking.

    He has a flask which I assume is whisky, and he has been drinking from it non-stop since the start of the hunt.

    I am concerned he is in no condition to handle a gun.

    He mutters to himself and I have no wish to engage him.
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        I should like to speak further with Andrew, but he is exceedingly cautious and professional.

        He does not respond to any of my meaningful looks.

        I understand only too well that there is no sense in risking discovery here.

        With luck, I shall see more of him later.
        """
    
    else:

        """
        The footman is exceedingly professional and remains silent whilst preparing our food.
        """


    """
    Only Ted Harring is willing to make conversation, so we exchange a few pleasantries.
    """

    $ time_left = 30

    call lad_generic

    call change_time(12,30)

    """
    After a while, we are ready to resume.
    """

    call common_day2_hunt_accident_footman_1

    call wait_screen_transition()

    """
    At first, it seems the afternoon will be as uneventful as the morning.

    I walk on mechanically, without thinking.

    Finding an animal to shoot is far from my mind.
    """

    if doctor_details.objects.is_unlocked('book_opium'):

        """
        The fact is that I have noticed the first symptoms of withdrawal.

        I am sweating profusely, I have cramps, and my hands have begun to tremble.

        Hardly ideal for holding a gun.

        I knew this was coming, and I am worried now.

        From what I have seen in my patients, it will not be easy to manage.

        I hope I can govern it well enough that no one notices.
        """

    else:

        """
        All I can think about is when I shall be alone in my room again.

        I hope we shall not hunt for much longer.
        """

    """
    I am roused from my stupor by Samuel Manning.
    """

    call common_day2_hunt_accident_death

    # jump to death

    return
