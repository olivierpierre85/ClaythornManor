# --------------------------------------------
#   Lad
#           
#   Friday - Evening
# 
#   18:10 -> 23:00
#
#   Music: chill
#
#   Position
#       - Dinner Room : Everyone
#
#   Notes : 
#       - Generic Psychic, 15 minutes
#       - Generic Psychic OR Doctor, 60 minutes (Dinner)
#       - Map visit, 90 minutes
#       - Generic Doctor, 80 minutes (Tea Room)
# --------------------------------------------
label lad_day1_evening:

    call change_time(18, 10, "Evening", "Friday", hide_minutes = True, chapter='friday_evening')

    $ current_character.add_checkpoint("lad_day1_evening") 

    call black_screen_transition("Ted Harring", chapters_names[current_chapter])

    $ change_room('entrance_hall', dissolve)

    $ play_music('upbeat')

    butler """
    Welcome, sir.
    """

    lad """
    Hello, I'm Ted Harring. I've been invited by Lady Claythorn.
    """

    butler """
    Yes, of course, Mr Harring.

    Welcome to Claythorn Manor.

    I am afraid you won't have time to change right now. 

    Everyone is already there, and dinner will be ready very soon.

    If you'll follow me to the tea room, you may join the rest of the party for some drinks.
    """

    """
    Well, it's not as if I have multiple changes of clothes anyway. So, I follow him.
    """

    $ change_room('tea_room')

    """
    As I step into the room, the butler loudly announces me.
    """

    butler """
    Mr Ted Harring!
    """

    """
    Everyone turns their heads towards me.
    
    Some people nod in my direction, while others barely acknowledge my presence.

    From afar, the butler provides me with a brief introduction to each guest.
    """

    show captain at truecenter
    butler """ 
    The older gentleman speaking is from India, and his name is Sushil Sinha.
    """

    hide captain

    show nurse at truecenter
    butler """
    He is in conversation with Rosalind Marsh...
    """
    hide nurse

    show doctor at truecenter
    butler """
    ... and with Daniel Baldwin, the gentleman with spectacles.
    """
    hide doctor

    show broken at truecenter
    butler """
    Do not be alarmed by the man in the mask. 

    He is a war veteran, Mr Thomas Moody.
    """
    hide broken

    show drunk at truecenter
    butler """
    The person on the sofa, who looks rather exhausted, is Mr Samuel Manning.
    """
    hide drunk

    show psychic at truecenter
    butler """
    The lady in the corner is Mrs Amelia Baxter.
    """
    hide psychic

    lad """
    I don't see our host in the room.
    """

    butler """
    Lady Claythorn is still busy at the moment.

    You'll meet her at dinner.
    """

    """
    After this introduction, he leaves me and goes to stand in the corner of the room.

    Most of the guests are already engaged in conversation.

    However, Amelia Baxter and Samuel Manning are alone.

    They seem more approachable than the rest.
    """
    
    $ time_left = 20
    
    call run_menu( TimedMenu("lad_introduction", [
        TimedMenuChoice('Talk to Samuel Manning', 'lad_day1_drinks_drunk', 10),
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_drinks_psychic', next_menu="psychic_generic_menu_lad"),
        TimedMenuChoice('Stand awkwardly in the corner', 'generic_cancel', early_exit=True),
        ], image_left = "drunk", image_right = "psychic")
    )

    call change_time(18,30)

    if not seen_tutorial_clock:
        call tutorial_clock

    play sound dinner_gong

    pause 1.0

    """
    What is that? A gong?
    """

    butler """
    Dinner is served. Please, follow me to the dining room.
    """

    pause 1.0

    $ stop_music()

    call change_time(18,30)

    $ change_room('dining_room', irisout)

    # $ renpy.force_autosave(take_screenshot=False, block=False) #WTF IS THIS DOING HERE?

    """
    Everyone takes a seat at the spot labelled with their names.

    As I observe each person, Lady Claythorn makes her entrance into the room.

    She looks younger than I had imagined.

    I don't know why, but I pictured an elderly, bored lady. Yet she looks nothing like that.
    
    Her clothes, which are the most impressive of anyone's in the room, make her status clear.

    She proceeds to take her seat at the table.
    """

    $ play_music('chill', 2)

    call common_day1_evening_host_welcome_speech

    """
    After her speech, everyone appears pleased.
    
    A few of the guests begin to express their appreciation to the host.
    """

    host """
    Please, there's no need to thank me. 
    
    The food will be served shortly. 
    
    Enjoy your meal.
    """

    """
    At that moment, the butler enters the room, accompanied by the footman. 

    They begin to serve the first dish and pour drinks for everyone.

    The mood in the room gradually relaxes, and the sound of various conversations fills the space.

    I turn my attention to the guests seated next to me.

    I find myself sitting between Amelia Baxter and Daniel Baldwin.
    """

    call change_time(19, 30)

    $ time_left = 90

    call run_menu( TimedMenu("lad_day1_evening", [
            TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_evening_dinner_doctor', next_menu="doctor_generic_menu_lad"),
            TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_evening_dinner_psychic', next_menu="psychic_generic_menu_lad"),
            TimedMenuChoice('Eat in silence, like a sociopath', 'generic_cancel', early_exit=True),
        ], image_left = "doctor", image_right = "psychic")
    )

    call change_time(21,00)

    $ stop_music

    """
    The dinner comes to an end.

    The host explains that we can continue our discussion and enjoy drinks in the billiard room, or, for those tired from the journey, we can simply retire for the night.

    Since I haven't seen my room yet, I should probably head there first.

    I ask the footman to show me the way.
    """

    $ change_room('bedrooms_hallway')

    $ play_music('upbeat', 2)

    """
    The footman escorts me up the grand staircase, leading me to the first floor.
    """

    footman """
    Here you are, sir.

    You've been assigned the 'William the Conqueror' room.
    """

    $ unlock_map('bedroom_lad')

    $ change_room('bedroom_lad')

    """
    I step into the bedroom.

    It is more spacious than my flat, and more luxurious than I could have imagined.
    """

    footman """
    I hope the room suits your taste.
    """

    lad """
    This is... this is good, yes. Thank you.
    """

    """
    The footman exits the room.

    I look around in disbelief.

    After a while, I unpack my modest luggage.

    It does not take long. So, what should I do now?
    """

    $ play_music('upbeat')

    call change_time(21,30)

    $ time_left = 90

    call run_menu(lad_details.saved_variables["day1_evening_map_menu"])

    call change_time(23,00)

    $ stop_music()

    if lad_details.threads.is_unlocked('day1_drunk'):

        """
        Wow, I'm not feeling well.

        Even worse, I think I might be getting sick.

        I'd better return to my room.
        """

    else: 

        """
        It's getting quite late now.

        Going back to my room is probably the best thing to do.
        """

    $ stop_music()

    $ change_room('bedroom_lad', dissolve)

    if lad_details.threads.is_unlocked('day1_drunk'):

        """
        I hurry to my room.

        I head straight for the bathroom and throw up all the Port I've been drinking.

        Great. If I didn't look foolish enough before, this surely seals it.

        I should go to bed before I do anything more embarrassing.

        Almost instantly, I fall asleep.
        """

        $ drunk_mode = False

    else:

        """
        It's been a long day and I'm exhausted from the trip.

        So I change and get directly into bed.

        Almost instantly, I fall asleep.
        """

    # If you drank whisky and didn't puke it, you done
    if lad_details.threads.is_unlocked('whisky') and not lad_details.threads.is_unlocked('day1_drunk'):

        jump lad_ending_day1_deathbed

    else:

        jump lad_day2_morning
        
    return


label lad_day1_drinks_psychic:

    """
    I am approaching the middle-aged woman.
    """

    call common_day1_drinks_lad_psychic_encounter

    call psychic_generic

    return


label lad_day1_drinks_drunk:

    """
    I am heading towards the older man.

    He holds an empty glass in his hand. His gaze is empty.
    """
    
    lad """
    Hello, sir. How are you?
    """

    drunk """
    (Snores...)
    """

    """
    He reeks of booze, and he is deeply asleep. Talking to him is useless.
    """

    return


label lad_day1_evening_bedroom_psychic:
  
    $ change_room("bedrooms_hallway")

    play sound door_knock

    """
    I knock on the door.
    """

    psychic """
    Yes? Who is it?
    """

    lad """
    Hi, it's Ted Harring.
    """

    psychic """
    Hello again. What do you want Mr Harring?
    """
    
    lad """
    I am not sure. But maybe we could continue our conversation from earlier.
    """

    psychic """
    Oh, Mr Harring. I'm afraid I was preparing for bed. We can speak again tomorrow.
    """

    lad """
    Of course, I apologize.
    """

    $ unlock_map('bedroom_psychic')

    $ lad_details.saved_variables['knows_bedroom_psychic'] = True

    return


label lad_day1_evening_dinner_psychic:
    
    lad """
    Hi again Miss Baxter.
    """

    psychic """
    Hello Mr Harring.
    """

    call psychic_generic
    
    return
    

label lad_day1_evening_dinner_doctor:

    lad """
    Hello. I am Ted Harring.
    """

    doctor """
    Hi Mr Harring, I am Dr Daniel Baldwin.
    """

    lad """
    Nice to meet you, doctor.
    """

    call doctor_generic

    return