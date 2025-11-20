label doctor_day2_hunt_accident:

    $ change_room("forest")
    
    call change_time(12,00, 'Hunt', 'Saturday')

    $ play_music('chill')


    """
    Our little group made its way into the forest.

    We walked for a while yet encountered nothing.

    So we stopped for luncheon.
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
    If Samuel Manning seemed somewhat sobered at first, he now appears intent on making up for lost drinking.

    He has a flask which I assume is whisky, and he has been drinking from it non-stop since the start of the hunt.
    """

    if doctor_details.objects.is_unlocked('drunk_letter'):

        """
        If I trust the content of the letter, he looks like he is summoning the courage to do something terrible.

        I feel like I should talk to him before he is too drunk.
        
        On the other hand, it could be prudent to wait for a better time.
        
        If I am on my guard, I could probably avoid him until the hunt is over.
        """

        call run_menu(
            TimedMenu("doctor_day2_hunt_accident", [
                TimedMenuChoice("Confront the drunk man with a gun {{object}}", 'doctor_day2_hunt_accident_confront_drunk', early_exit = True),
                TimedMenuChoice("Ignore him and talk with Ted Harring", 'doctor_day2_hunt_accident_lad_conversation', early_exit = True)
            ])
        )

    else:

        """
        I am concerned he is in no condition to handle a gun.

        He mutters to himself and I have no wish to engage him.

        Only Ted Harring is willing to make conversation, so I address him.
        """

        call doctor_day2_hunt_accident_lad_conversation


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


    """
    Very quickly I start to enjoy the familiar feeling of calm.

    It won't be long now.
    """

    if doctor_details.objects.is_unlocked('book_opium'):

        """
        Ironically, I truly believe I would have managed to quit this time.
        """

    else:

        """
        Ironically, this is likely how I was meant to go anyway.
        """

    jump doctor_ending_shot_by_drunk


label doctor_day2_hunt_accident_lad_conversation:

    doctor """
    How are you getting on Mister Harring?
    """

    lad """
    Very well Doctor.
    """

    $ time_left = 30

    call lad_generic

    call change_time(12,30)

    if doctor_details.saved_variables['bored_by_lad'] > 1:

        """
        Well, that was hardly the most stimulating conversation.

        Still, I suppose we're ready to keep going with the hunt.
        """

    else:

        """
        After a short while, we're ready to keep going with the hunt.
        """

    return


label doctor_day2_hunt_accident_confront_drunk:

    # TODO: The Doctor confront Samuel Manning with the letter he found
    # The doctor found out that Sam manning was pretending to be drunk
    # Things got heated and they fought
    # Samuel Manning shot himself in the fight and dies there



    jump doctor_day2_evening