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

        $time_left = 1
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

    $ play_music('danger', 2, fadeout=8)

    """
    I summon the courage to go talk to Samuel Manning.

    Ted Harring doesn't follow me, he probably wants nothing to do with the man.
    """

    doctor """
    Mister Manning?
    """
    
    """
    He looks bewildered that I am speaking to him.
    """

    drunk """
    Hum,... yes?
    """

    doctor """
    I was wandering if we could talk alone for a bit.

    I have somewhat a sensitive subject to broach with you.
    """

    drunk """
    Well, hum, yes I guess we could, of course.
    """

    doctor """
    Very well, can you come this way?
    """

    drunk """
    Fine.
    """

    """
    I move a few paces from our luncheon place, enough to be out of earshot.

    But close enough that if something happens, they can join us quickly.
    """

    doctor """
    Here is perfect mister Manning.
    """

    drunk """
    Alright, what is it doctor?
    """

    """
    I don't see a reason to beat about the bust.
    """

    doctor """
    It's about the letter I found in your room, the one where you wrote that "I must pay".
    """

    """
    This confession seems to take him by surprise.

    But he quickly regain his composure, and talks in a more assertive tone.

    Any trace of intoxication is gone from his face.

    He was likely faking it, I should have guessed.
    """

    $ doctor_details.description_hidden.unlock('lie') 

    drunk """
    What were you doing in my room?

    Who gave you permission?

    But I shouldn't be surprised, doctors do as they please.

    They always do.
    """

    doctor """
    That's not the point, you wrote you wanted to hurt me, and I am not even sure to know why.
    """

    """
    My words struck him strongly, and that's with anger that he answers.
    """

    drunk """
    You don't know why?!!!

    I thought it was clear enough!

    You killed her.

    My poor Margaret.

    My God, you stood by her bedside and watched her slip away.
    
    And now you come here as though nothing happened, you probably don't even remember do you?

    Is it because you killed so many of them?
    """

    """
    I am dumbstruck, I can't find the right words to say.

    Samuel Manning takes his gun and points it at me.
    """

    """
    Lower the weapon, Mr Manning.

    You don't understand, someone is manipulating you.

    They want you to do this!
    """

    """
    Well, that's all right because I want to do it too.
    """

    """
    He is about about to shoot, so I jump towards him.
    """

    play sound gun
    
    """
    He missed me and I am on him.

    We struggle.

    I grap his rifle and try to wrestle it out of his arms.
    """

    play sound gun

    """
    For a moment everything is silent, until I felt the weight of Samuel Manning against me.

    I push him and he collapsed at my feet.

    The rifle lay beside him.

    I knelt at once, though a single glance told me the truth.

    He had shot himself in the chest during the fight.
    """

    doctor """
    Dear God.

    What have you done.
    """

    $ doctor_details.description_hidden.unlock('wife') 

    jump doctor_day2_evening