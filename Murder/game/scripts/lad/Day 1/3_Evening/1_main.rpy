# --------------------------------------------
#               Ted Harring
#           Friday 21:00 Evening
#   Playtime : about 10 min from start
#
#   Alive: Everyone
label lad_day1_evening:

    $ lad_details.add_checkpoint("lad_day1_evening") 

    call change_time(21,00, 'Evening', 'Friday')

    scene hallway

    "He takes me through the grand staircase, on to the first floor."

    footman """
    There you go sir.

    You have the 'William The Conqueror' room.

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

    Well that didn't take long. So what do I do now ?
    """

    $ play_music('upbeat')

    $ time_left = 120
    $ print(lad_details.saved_variables["map_menu"].get_visible_choices() )
    call run_menu(lad_details.saved_variables["map_menu"])

    call change_time(23,00)

    stop music fadeout 5.0

    if lad_day1_drunk:
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

    stop music fadeout 5.0

    $ change_room('lad_room')

    if lad_day1_drunk:

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

    if lad_day1_poisoned:

        jump lad_ending_day1_poisoned

    else:

        jump lad_day2_morning
        
    return

# label lad_day1_evening_host_room:
# NO- She is in the billiard room
#     scene hallway

#     "I knock on the door."

#     psychic "Yes ?"

#     lad """
#     Lady Claythorn, it's Ted Harring.

#     I was hoping we could talk?   
#     """

#     host """
#     I am sorry, but it's a very bad time mister Harring.

#     Why don't you meet the others in the billiard room?.
#     """

#     return

label lad_day1_evening_psychic_room:
  
    scene hallway

    "I knock on the door."

    psychic "Yes ? Who is it ?"

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

label lad_day1_evening_cancel:
    return