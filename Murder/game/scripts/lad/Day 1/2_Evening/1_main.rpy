# --------------------------------------------
#   Lad
#           
#   Friday - Arrival/Afternoon
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
    Everyone sits at a place with their names on them.

    While I am examining everyone, Lady Claythorn enters the room. 
    
    She takes her place at the table.
    """

    $ play_music('chill', 2)

    call host_welcome_speech

    """
    After the speech, everyone seems pleased. And a few of the guests started showing their appreciation to the host.
    """

    host """
    Please no need to thank me. The food will be served, enjoy your meal.
    """

    """
    The butler then enters the room, accompany by the footman.
    
    They proceed in serving the first dish and pouring drinks to everyone.
    
    The mood starts to relax, and the sound of different conversations fills the room.

    I turn my attention to the guests next to me.

    I am sitting between Amelia Baxter, and Daniel Baldwin.
    """

    $ time_left = 60

    $ current_menu = TimedMenu([
        TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_evening_dinner_doctor'), # SHould they be keep_alive?
        TimedMenuChoice('Talk to Amelia Baxter', 'lad_day1_evening_dinner_psychic')
    ], image_left = "doctor", image_right = "psychic")

    call run_menu(current_menu)

    $ stop_music

    """
    The dinner is ending.

    The host explain that we can continue to discuss and enjoy drinks in the billiard room. Or for those tired by the journey, we can simply go to bed.

    Since I haven't been able to see my room, I better go there first.

    I ask the footman to show me the way.
    """

    call change_time(21,00)

    $ change_room('hallway')

    $ play_music('upbeat', 2)

    """
    The footman takes me through the grand staircase, on to the first floor.
    """

    footman """
    There you go sir.

    You have the \"William The Conqueror\" room.

    I hope it's to your liking.
    """

    $ unlock_map('lad_room')

    $ change_room('lad_room')

    """
    I enter the bedroom. 
    
    It's bigger than my apartment. And more luxurious than I could have dreamed of.
    """

    lad """
    That will do great, thank you.
    """

    """
    The footman exits the room.

    I look around me in disbelief.
    
    After a while I unpack my small luggage.

    Well that didn't take long. So what do I do now?
    """

    $ play_music('upbeat')

    call change_time(21,30)

    $ time_left = 90

    call run_menu(lad_details.saved_variables["map_menu"])

    call change_time(23,00)

    $ stop_music()

    if lad_details.saved_variables["day1_drunk"]:

        """
        Wow I don't feel great.

        And worst, I think I might be getting sick.

        I better go back to my room.
        """

    else: 

        """
        It's getting kinda late now.

        I am exhausted from the trip. 
        
        It's probably best if I go to bed now.
        """

    $ stop_music()

    $ change_room('lad_room')

    if lad_details.saved_variables["day1_drunk"]:

        """
        I rush to my room.

        Find the toilet and puke all the Port I have been drinking.

        Great. If I didn't look stupid enough before that will do it.

        I go to bed before I do anything stupid.

        And I fall asleep almost instantly.
        """

    else:

        """
        It's been a long day.

        So I change a get directly into my bed.

        I fall asleep almost instantly.
        """

    if lad_details.saved_variables["day1_poisoned"]:

        jump lad_ending_day1_poisoned

    else:

        jump lad_day2_morning
        
    return

label lad_day1_evening_psychic_room:
  
    scene hallway

    "I knock on the door."

    psychic "Yes? Who is it?"

    lad "Hi, it's Ted Harring."

    psychic """
    Oh. What do you want mister Harring?
    """
    
    lad """
    I am not sure. But maybe we could continue our conversation from earlier.
    """

    psychic "Oh Mister Harring. I am afraid I was getting ready to bed. We can talk again tomorrow."

    lad "Of course, I am sorry."

    $ unlock_map('psychic_room')

    return

label lad_day1_evening_dinner_psychic:
    
    lad """
    Hi again Miss Baxter.
    """

    psychic """
    Oh Mister Harring. I am glad we can continue our conversation.
    """

    call psychic_generic
    
    return
    

label lad_day1_evening_dinner_doctor:

    lad """
    Hello. I am Ted Harring.
    """

    doctor """
    Hi mister Haring, I am doctor Daniel Baldwin.
    """

    lad """
    Nice to meet you doctor.
    """

    call doctor_generic

    return