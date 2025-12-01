label doctor_day2_hunt_accident:

    $ change_room("forest")
    
    call change_time(12,00, 'The Hunt', 'Saturday')

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

    if doctor_details.observations.is_unlocked('drunk_letter'):

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

    if doctor_details.observations.is_unlocked('drunk_letter'):

        """
        As I did this morning, I take care to keep Samuel Manning within my line of sight.

        """

    """
    At first, it seems the afternoon will be as uneventful as the morning.

    I walk on mechanically, without thinking.

    Finding an animal to shoot is far from my mind.

    """

    if doctor_details.objects.is_unlocked('book_opium'):

        """
        The fact is that I have begun to notice the first symptoms of withdrawal.

        I am sweating profusely, I have cramps, and my hands have begun to tremble.

        Hardly ideal for holding a gun.

        I knew this was coming, and I am worried now.

        From what I have seen in my patients, it will not be easy to manage.

        I hope I can govern it well enough that no one notices.
        """

    elif doctor_details.important_choices.is_unlocked('flirt'):

        """
        Despite my caution, my gaze is drawn again and again to Andrew, looking rather dashing in his footman's livery.

        I wonder if we shall see one another tonight.

        """

    else:

        """
        I regret not taking my "medicine" with me.

        All I can think about is when I shall be alone in my room again.

        I hope we shall not hunt for much longer.
        """

    if doctor_details.observations.is_unlocked('drunk_letter'):

        """
        I am lost in my thoughts when I hear Samuel Manning shout.

        Damn it, for a moment I have let him out of my sight.

        """

    else:
        # He is not suspicious of Samuel Manning
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
    How are you getting on Mr Harring?
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

    $ play_music('danger', 2, fadeout_val=4)

    """
    I summon the courage to go and speak to Samuel Manning.

    Ted Harring does not follow me, he probably wants nothing to do with him.
    """

    doctor """
    Mr Manning?
    """
    
    """
    He looks bewildered that I am addressing him.
    """

    drunk """
    Hum... yes?
    """

    doctor """
    I was wondering if we could talk alone for a moment.

    I have rather a sensitive subject to broach with you.
    """

    drunk """
    Well, hum... yes, I suppose we could, of course.
    """

    doctor """
    Very well, if you would come this way.
    """

    drunk """
    Fine.
    """

    """
    I move a few paces from our luncheon place, far enough to be out of earshot.

    But close enough that, if something happens, they can join us quickly.
    """

    doctor """
    Here is perfect, Mr Manning.
    """

    drunk """
    All right, what is it, doctor?
    """

    """
    I see no reason to beat about the bush.
    """

    doctor """
    It is about the letter I found in your room, the one where you wrote that "I must pay".
    """

    """
    This confession seems to take him by surprise.

    But he quickly regains his composure, and speaks in a more assertive tone.

    Any trace of intoxication is gone from his face.

    He was likely faking it.
    
    I should have guessed.
    """

    $ drunk_details.description_hidden.unlock('lie') 

    drunk """
    What were you doing in my room?

    Who gave you permission?

    But I should not be surprised, doctors do as they please.

    They always do.
    """

    doctor """
    That is not the point, you wrote that you wanted to hurt me, and I am not even certain I know why.
    """

    """
    My words strike him strongly, and he answers in anger.
    """

    drunk """
    You do not know why?!!!

    I thought it was clear enough!

    You killed her.

    My poor Margaret.

    My God, you stood by her bedside and watched her slip away.
    
    And now you come here as though nothing happened, you probably do not even remember, do you?

    Is it because you killed so many of them?
    """

    """
    I am dumbstruck, I cannot find the right words to say.

    Samuel Manning raises his gun and points it at me.
    """

    doctor """
    Lower the weapon, Mr Manning.

    It's a misunderstanding, someone is manipulating you.

    They want you to do this.
    """

    drunk """
    Well, that is all right, because I want to do it too.
    """

    """
    He is about to shoot, so I jump towards him.
    """

    play sound gun
    
    """
    He misses me and I am on him.

    We struggle.

    I grab his rifle and try to wrestle it out of his arms.
    """

    play sound gun

    pause 1.0

    """
    For a moment everything is silent, until I feel the weight of Samuel Manning against me.

    I push him and he collapses at my feet.

    The rifle lies beside him.

    I kneel at once, though a single glance tells me the truth.

    He has shot himself in the chest during the fight.
    """

    doctor """
    Dear God.

    What have I done.
    """

    $ drunk_details.description_hidden.unlock('wife') 

    jump doctor_day2_evening


label doctor_day2_hunt_accident_death_not_careful:


    """
    I am lost in my thoughts when I a hear the voice of Samuel Manning shouting.

    For a second I have forgotten to watch him.
    """

    return