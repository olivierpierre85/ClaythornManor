# --------------------------------------------
#   Lad
#           
#   Friday - Evening
# 
#   18:30 -> 23:00
#
#   Music: chill
#
#   Position
#       - Dinner Room : Everyone
#
#   Notes : 
#       - Generic Psychic OR Doctor, 60 minutes (Dinner)
#       - Map visit, 90 minutes
#       - Generic Doctor, 80 minutes (Tea Room)
# --------------------------------------------
label lad_day1_evening:
    
    call change_time(18,30, "Evening", "Friday" )

    $ current_character.add_checkpoint("lad_day1_evening") 

    call black_screen_transition("Ted Harring", "Friday Evening")

    $ change_room('dining_room', irisout)

    """
    Everyone takes a seat at the spot labeled with their names.

    As I observe each person, Lady Claythorn makes her entrance into the room.

    She proceeds to take her seat at the table.
    """

    $ play_music('chill', 2)

    call common_day1_evening_host_welcome_speech

    """
    After the speech, everyone appeared pleased. 
    
    A few of the guests began to express their appreciation to the host.
    """

    host """
    Please, there's no need to thank me. 
    
    The food will be served shortly. 
    
    Enjoy your meal.
    """

    """
    At that moment, the butler entered the room, accompanied by the footman. 

    They began to serve the first dish and pour drinks for everyone.

    The mood in the room gradually relaxed, and the sound of various conversations filled the space.

    I turned my attention to the guests seated next to me.

    I found myself sitting between Amelia Baxter and Daniel Baldwin.
    """

    call change_time(19,00)

    $ time_left = 120

    $ current_menu = TimedMenu("lad_day1_evening", [
        TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_evening_dinner_doctor'),
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_evening_dinner_psychic')
    ], image_left = "doctor", image_right = "psychic")

    call run_menu(current_menu)

    call change_time(21,00)

    $ stop_music

    """
    The dinner is coming to an end.

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

    You've been assigned the \"William The Conqueror\" room.

    I hope it suits your taste.
    """

    $ unlock_map('lad_room')

    $ change_room('lad_room')

    """
    I step into the bedroom.

    It's more spacious than my apartment, and more luxurious than I could have ever imagined.
    """

    lad """
    This is perfect, thank you.
    """

    """
    The footman exists the room.

    I look around in disbelief.

    After a while, I unpack my modest luggage.

    That task didn't consume much time. So, what should I do now?
    """

    $ play_music('upbeat')

    call change_time(21,30)

    $ time_left = 90

    call run_menu(lad_details.saved_variables["day1_evening_map_menu"])

    call change_time(23,00)

    $ stop_music()

    if lad_details.saved_variables["day1_drunk"]:

        """
        Wow, I'm not feeling well.

        Even worse, I think I might be getting sick.

        I'd better return to my room.
        """

    else: 

        """
        It's getting quite late now.

        I'm exhausted from the trip.

        Going to bed now is probably the best thing to do.
        """

    $ stop_music()

    $ change_room('lad_room')

    if lad_details.saved_variables["day1_drunk"]:

        """
        I hurry to my room.

        I head straight for the bathroom and throw up all the Port I've been drinking.

        Great. If I didn't look foolish enough before, this surely seals it.

        I should go to bed before I do anything more embarrassing.

        Almost instantly, I fall asleep.
        """

    else:

        """
        It's been a long day.

        So I change a get directly into my bed.

        Almost instantly, I fall asleep.
        """

    if lad_details.saved_variables["day1_poisoned"]:

        jump lad_ending_day1_poisoned

    else:


        jump lad_day2_morning
        # TODO while testing full testing mode force always dying on first day
        # jump lad_ending_day1_poisoned
        
    return

label lad_day1_evening_psychic_room:
  
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
    Hello again. What do you want mister Harring?
    """
    
    lad """
    I am not sure. But maybe we could continue our conversation from earlier.
    """

    psychic """
    Oh, Mr. Harring. I'm afraid I was preparing for bed. We can speak again tomorrow.
    """

    lad """
    Of course, I apologize.
    """

    $ unlock_map('psychic_room')

    $ lad_details.saved_variables['knows_psychic_room'] = True

    return

label lad_day1_evening_dinner_psychic:
    
    lad """
    Hi again Miss Baxter.
    """

    psychic """
    Hello Mister Harring.
    """

    call psychic_generic
    
    return
    

label lad_day1_evening_dinner_doctor:

    lad """
    Hello. I am Ted Harring.
    """

    doctor """
    Hi mister Harring, I am doctor Daniel Baldwin.
    """

    lad """
    Nice to meet you doctor.
    """

    call doctor_generic

    return