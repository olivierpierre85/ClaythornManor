# --------------------------------------------
#   Psychic
#           
#   Friday - Evening
#   
#   16:30 -> 23:00
#
#   Music: chill
#
#   Alive: Everyone
#
#   Notes
#       - Generic Lad, 15 minutes
#       - Generic Lad, Captain: 60 minutes
#       - Map menu: 120 minutes
# --------------------------------------------
label psychic_day1_evening:

    call change_time(16,30, 'Evening', 'Friday', hide_minutes = True, chapter='friday_evening')

    $ current_character.add_checkpoint("psychic_day1_evening") 

    call black_screen_transition("Amelia Baxter", chapters_names[current_chapter])

    $ change_room('great_hall', dissolve)
    
    $ play_music('upbeat')

    butler """
    Good afternoon, everyone, and welcome to Claythorn Manor.

    I'm sorry that Lady Claythorn can't greet you herself.

    She is still busy preparing for tonight.

    In the meantime, you can enjoy some drinks in the tea room.

    Or, if you wish to change, I can show you to your room right now.
    """

    drunk """
    I'm good, but I could use a drink.

    Which way is the tea room?
    """

    """
    Amazing. He looked passed-out drunk in the car.
    
    How could he possibly want another drink now?
    """

    butler """
    Very well, sir. You'll find the tea room through the door on your left.

    Other guests who arrived earlier are already settled there.

    You can join them.
    """

    captain """
    I'll come with you.
    """

    butler """
    What about you, Miss ...?
    """

    psychic """
    Miss Baxter.

    I think I'll freshen up in my room first.

    It's been a very long trip.
    """

    butler """
    Of course, please follow me upstairs.
    """

    $ change_room("bedrooms_hallway", dissolve)

    butler """
    Here we are, Miss.

    The "Elizabeth I Bedroom."

    I hope it's to your liking.
    """

    $ unlock_map('bedroom_psychic')

    $ change_room('bedroom_psychic')

    """
    He opens my room and lets me in.
    
    At the same time, the driver arrives with my luggage.

    He leaves them there and then excuses himself.
    """

    butler """
    Well, it looks like you're all set.

    Please join us in the dining room when you're ready.
    """

    """
    I nod and take a look at my room.

    It's a bit worn out but it still looks decent.

    I should be comfortable here.
    """
    
    pause 1.0

    """
    When I'm ready, I head downstairs to the tea room.
    """

    $ change_room("tea_room")

    call change_time(18,15, 'Arrival', 'Friday')

    butler """
    Miss Baxter.

    Almost everyone is here now.
    """

    """
    He quickly introduces me to the people I haven't met yet.
    """

    butler """
    Please make yourself at home.

    Now, if you'll excuse me, I hear the car is back with the last guest.
    """

    """
    He leaves me on my own.

    I glance around the room.

    Almost everyone is gathered around Sushil Sinha.

    He's in the midst of what sounds like another tedious story.

    I'm not eager to listen to that again.

    On a chair, Samuel Manning is sitting alone with a glass in his hand.

    I can't believe it.

    He's asleep again.

    Well, I guess I have no choice but to join the larger group.

    But before I could move, the butler returns.
    """

    butler """
    Mister Ted Harring!
    """

    """
    The butler nearly shouts the name of the new guest.

    He's a good-looking young man, but he looks unsure.

    You can tell that he's not in his natural element here.

    I smile at him and, after some hesitation, comes towards me.
    """

    call common_day1_drinks_lad_psychic_encounter

    $ time_left = 15

    call lad_generic

    play sound dinner_gong

    butler """
    Dinner is served. Please follow me to the dining room.
    """

    $ stop_music()

    call change_time(18,30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill')

    """
    I sit down at the place with my name on it.

    Then, a lady enters the room.

    She is wearing expensive clothing.
    """

    call common_day1_evening_host_welcome_speech

    """
    Well said.

    I join in clapping with the rest of the guests.
    """

    host """
    Please no need to thank me. The food will be served, enjoy your meal.
    """

    """
    The food arrives right after the speech.

    Perfect timing here.
    """

    pause 1

    """
    It looks like I already know the persons next to me.
    
    On my left is Mister Sinha.
    
    And Ted Harring is on my right.
    """

    $ time_left = 90 
    call run_menu(TimedMenu("psychic_day1_evening", [
        TimedMenuChoice('Talk to Sushil Sinha', 'psychic_day1_dinner_captain'),
        TimedMenuChoice('Talk to Ted Harring', 'psychic_day1_dinner_lad'),
        TimedMenuChoice("Don't engage with anyone, it's unladylike", 'generic_cancel', early_exit=True),
    ], image_left = "captain", image_right = "lad"))

    $ stop_music()

    """
    The dinner is over.

    The host gave us the opportunity to meet again for drinks. 
    
    But I don't know, this was quite a long day.
    
    Maybe I should just go to bed.

    In any case, I should retire to my room first.
    """

    $ stop_music(3)

    pause 2.0

    call change_time(21,00, 'Evening', 'Friday')

    $ change_room('bedroom_psychic', dissolve)

    """
    Well, I am comfortably settled.

    What should I do now?
    """

    $ play_music('upbeat')

    $ time_left = 120
    
    call run_menu(psychic_details.saved_variables["day1_evening_map_menu"])

    call change_time(23,00)

    $ stop_music()

    """
    It's been a long day.

    I can't stay up any longer.

    It's time to go to bed.
    """

    $ change_room('bedroom_psychic')

    jump psychic_day2_morning
        

label psychic_day1_dinner_lad:
    
    lad """
    Hi again Miss Baxter.
    """

    psychic """
    Oh Mister Harring. I am glad we can continue our conversation.
    """

    $ psychic_details.saved_variables["day1_evening_talk_to_lad"] = True

    call lad_generic
    
    return
    

label psychic_day1_dinner_captain:

    """
    Maybe I was too quick to judge him.

    I should try to talk to him again.
    """

    psychic """
    Mister Sinha.
    """

    captain """
    Miss Baxter.
    """

    if psychic_details.saved_variables["day1_evening_talk_to_lad"] and not psychic_details.saved_variables["day1_evening_talk_to_captain"]:

        captain """
        I don't want to make a big deal out of it, but I am the one on your left.
        
        You should have engaged in conversation with me first.
        """

        psychic """
        Oh right, I am sorry.
        """

        """
        What a stickler he is.

        Also, how does he know this?
        """

        $ captain_details.description_hidden.unlock('table') 

        $ psychic_details.saved_variables["day1_evening_talk_to_captain"] = True


    call captain_generic

    return