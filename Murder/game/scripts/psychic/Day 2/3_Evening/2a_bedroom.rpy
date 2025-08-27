label psychic_day2_evening_bedroom:
    
    $ change_room('bedroom_psychic', dissolve)

    call change_time(18, 00)

    """
    I returned to my room to change and clear my head.
    
    It seems I still have a little time before dinner.

    I suppose I could just rest for a bit,

    or take the opportunity to have a private word with someone.

    I do not think it would be wise to approach Captain Sinha,

    nor Lady Claythorn.

    However, I do not believe I am taking too much of a risk by talking with Rosalind Marsh or Ted Harring.
    """

    if psychic_details.observations.is_unlocked('nurse_blood'):

        """
        Maybe I could see if Rosalind Marsh is feeling better now.
        """

    $ time_left = 99 #TODO possibility to talk to both ???
    call run_menu(TimedMenu("psychic_day2_evening_bedroom", [
            TimedMenuChoice('Try to talk to Rosalind Marsh', 'psychic_day2_evening_bedroom_nurse', 0, early_exit=True),
            TimedMenuChoice('Try to talk to Ted Harring', 'psychic_day2_evening_lad_discussion', 20, early_exit=True),
            TimedMenuChoice('Just have a quick nap instead', 'psychic_day2_evening_cancel_2', 30, early_exit=True),
            # Talk with host anyway??? Intuition things are not going according to plan.
        ])
    )

    return


label psychic_day2_evening_lad_discussion:

    $ change_room("bedrooms_hallway")

    call common_day2_evening_lad_psychic_discussion_0

    $ psychic_details.important_choices.unlock('visit_lad')

    return


label psychic_day2_evening_cancel_2:

    """
    That's about all I can manage right now.

    I should rest for a bit.
    """

    call wait_screen_transition()

    call change_time(18,30)    

    play sound dinner_gong

    """
    Right on time, the dinner gong rings.
    
    I guess I should join the others downstairs.
    """

    return


label psychic_day2_evening_bedroom_nurse:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock gently on the door.

    A faint voice responds.
    """

    nurse """
    Yes? What is it?
    """
    
    $ unlock_map('bedroom_nurse')

    psychic """
    It's Amelia Baxter.

    Are you all right?

    Perhaps we might have a chat?
    """

    nurse """
    I am sorry, Miss Baxter, but I am very tired.

    Unless it is very important, I would prefer to wait.
    """

    if psychic_details.observations.is_unlocked('nurse_blood'):

        call run_menu(TimedMenu("psychic_day2_evening_bedroom_nurse", [
            TimedMenuChoice("Insist, there is clearly something wrong with her", 'psychic_day2_evening_bedroom_nurse_insist', 10, early_exit=True),
            TimedMenuChoice("Do not push any further", 'psychic_day2_evening_bedroom_nurse_ignore', 10, early_exit=True), 
        ]))

        $ change_room('bedroom_psychic')

        """
        I return to my room to rest.

        Digesting the information.

        Rosalind Marsh is dying.

        I don't know what to make of it.
        """

    else:

        call psychic_day2_evening_bedroom_nurse_ignore

        $ change_room('bedroom_psychic')

        """
        I return to my room to rest.
        """

    call change_time(18,30) 

    """
    I am deep in my thoughts when I hear the gong ringing.
    """

    play sound dinner_gong

    """
    I guess I should join the others downstairs.
    """

    return


label psychic_day2_evening_bedroom_nurse_insist:


    psychic """
    I am afraid it is important.

    Could you let me in? It won't take long.
    """

    nurse """
    All right then, come on in.
    """

    $ change_room("bedroom_nurse")

    nurse """
    What can I do for you?
    """

    psychic """
    Nothing, it's more the other way round.

    I am sorry, I do not mean to intrude, but I noticed a trace of blood on your handkerchief.

    I was wondering if there was anything I could do to help you.
    """

    nurse """
    Well, I suppose I could not have hidden it forever.

    You see, I am suffering from a very serious disease.
    
    One that has no known cure: consumption.
    """

    play sound woman_cough

    """
    She lets out another strong cough.
    """

    $ psychic_details.observations.unlock('nurse_sick')

    psychic """
    I am so sorry.

    When did you find out?
    """

    nurse """
    A couple of years ago.

    And if I trust my doctor, I probably don't have more than another year left in me.
    """

    psychic """
    My goodness, how horrible.

    Could I help you with anything?
    """

    nurse """
    There is nothing to be done.

    My doctor prescribed me a strong medicine that I have to take before going to bed.
    
    That usually helps me sleep.

    Sometimes I have to take it during the day, that's why I am often in my room, resting.

    But you should go now, I will try to rest a little before dinner.

    Thank you for your concern anyway.
    """
    
    psychic """
    Of course, I'll go.
    """

    nurse """
    Thanks.
    """  

    $ nurse_details.description_hidden.unlock('sick')    

    return


label psychic_day2_evening_bedroom_nurse_ignore:

    psychic """
    No, it can wait for now, of course. Goodnight, Miss Marsh.
    """

    nurse """
    Goodnight, Miss Baxter.
    """

    return


label psychic_day2_evening_bedroom_nurse_gone:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock gently on the door.

    but there is no answer.
    """

    if psychic_details.observations.is_unlocked('nurse_sick'):

        """
        She is probably resting.

        After all, she said it herself. At night she takes her medicine then falls asleep.

        But I don't know.

        She seemed in really bad shape when I last talked to her.

        Maybe she is in danger.

        Should I try to check on her to be safe?
        """
 
        call run_menu(TimedMenu("psychic_day2_evening_bedroom_nurse_gone", [
                TimedMenuChoice('Try to enter', 'psychic_day2_evening_bedroom_nurse_gone_enter', 20, early_exit=True),
                TimedMenuChoice("Don't try to enter", 'psychic_day2_evening_bedroom_nurse_gone_do_not_enter', 10, early_exit=True),
            ])
        )

    else: 

        call psychic_day2_evening_bedroom_nurse_gone_do_not_enter

    return


label psychic_day2_evening_bedroom_nurse_gone_enter:

    """
    I try to open the door.

    It is unlocked.
    """

    $ change_room("bedroom_nurse")

    """
    But there is no one in here.

    Where is Miss Marsh?

    She seemed so sick earlier.

    I look around the room, 

    and find something weird next to her bedstand.

    Is that silverware?

    What is it doing here?

    It could be she was planning to eat in her room and changed her mind at the last minute.

    But there is more then on set.

    Unless she was wanted to entertain a few guests, there is no reason for her to have that many utensils in her room.

    I am not sure what to make of that.
    """
    
    $ psychic_details.observations.unlock('silverware')

    return


label psychic_day2_evening_bedroom_nurse_gone_do_not_enter:

    """
    She is probably just asleep. 
    
    There is no reason to wake her up.
    """
    
    return