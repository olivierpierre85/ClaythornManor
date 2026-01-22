# --------------------------------------------
#   Lad
#           
#   Saturday - Evening
# 
#   15h -> 23h
#
#   Music: sad
#
#   Position
#       - House: Everyone else
#       - Dead : broken, doctor
#
#   Notes : 
#       - Convince captain
#       - Map 120 minutes
# --------------------------------------------
label lad_day2_evening:

    call change_time(15,00, 'Evening', 'Saturday', chapter='saturday_evening')

    $ lad_details.add_checkpoint("lad_day2_evening") 
    
    call black_screen_transition("Ted Harring", chapters_names[current_chapter])

    $ change_room("entrance_hall", irisout)
    
    if lad_details.threads.is_unlocked('hunt'):

        """
        Everything happened so quickly it is all a blur.

        After the shouting and crying in the woods, Captain Sinha took charge.

        He had us carry the doctor on a makeshift stretcher back to the house.
 
        It took some time, but we eventually reached the mansion.
        """        

    else:
        
        """
        I watch the hunting party enter the house.

        Amelia and Rosalind are already there, near the entrance.

        Lady Claythorn enters first, looking visibly shocked.

        Then the butler and footman follow.

        They're dragging someone on a makeshift stretcher.
        """

    $ play_music('sad')

    call common_day2_evening_entrance_dialog

    $ change_room("bedroom_doctor")

    """
    We carried Doctor Baldwin to his room and laid him on his bed.

    Sushil then covered him with a blanket.
    """

    captain """
    It's the best we can do at the moment.

    We shouldn't linger here.

    I want to keep an eye on Samuel Manning.
    """

    lad """
    Of course.
    """

    captain """
    Also Mr Harring, you might want to change before rejoining us.
    """

    """
    I glance at my clothes.

    They're stained with blood.
    
    He is right, I can't go back downstairs looking like this.
    """
    
    call lad_day2_evening_bedroom

    call change_time(18,30)


    $ change_room("dining_room", irisout)
    
    $ play_music('sad', 3)

    """
    As I enter the room, the atmosphere is gloomy.

    The seats of Daniel Baldwin and Thomas Moody are empty.

    Samuel Manning is absent as well.

    I take my usual seat, with only Amelia Baxter beside me now.

    Lady Claythorn starts a speech.
    """

    call common_day2_evening_dinner_host

    """
    The food is served shortly after the speech.

    Yet, most of us have little appetite.
    """

    call common_day2_evening_dinner_lad_psychic_talk

    """
    Well, that's one less thing to worry about.

    No one seems up for small talk.

    Dinner passes in almost silence.

    Most guests retire to their rooms after eating.

    Given the day's events, I doubt anyone is in the mood for drinks.

    What should I do next?
    """

    call change_time(21,00)

    $ time_left = 120

    call run_menu(lad_details.saved_variables["day2_evening_map_menu"])

    call change_time(23,00)

    $ stop_music()

    if lad_details.threads.is_unlocked('day2_drunk'):

        """
        My head feels thick and foggy.

        I rush to my room.
        """

        $ change_room('bedroom_lad')

        """
        I reach the toilet just in time and empty the contents of my stomach.
        """

        if lad_details.threads.is_unlocked('day1_drunk'):
            
            """
            Drunk two days in a row.

            What does this say about me?
            """

            $ lad_details.description_hidden.unlock('poor_drinker') 

            # TODO: Achievement. DRUNK OR CHEATED DEATH IF drank poison.

        """
        It's best I get some rest now.

        I fall asleep as soon as I lie down.
        """

        $ drunk_mode = False
    
    else:

        """
        Wandering through this house has taken its toll.

        And with everything that happened today, I'm drained.

        I should go back to my room.
        """

        $ change_room('bedroom_lad')

        """
        Before trying to sleep, it seems a good idea to barricade the door with some furniture.

        You can't be too cautious.
        """

        play sound moving_furniture
        
        pause 2.0

        """
        That should be enough.

        Now, I can rest peacefully.
        """

    jump lad_day3_morning


label lad_day2_evening_sleep:

    return


label lad_day2_bedroom_broken_back:

    $ change_room('bedroom_broken')

    """ 
    Although I've been here before, I can't shake the feeling I should inspect the room once more.

    Yet, everything looks the same as I remember.

    Perhaps I should look elsewhere.
    """    

    return

label lad_day2_bedroom_broken_back_for_drink:

    $ change_room('bedroom_broken')

    """ 
    After speaking with Sushil, I wonder if I should try the flask.

    A quick taste would clarify if something is wrong.

    Reaching for it on the nightstand, I find it empty, with its contents spilled.

    I briefly consider licking it but quickly dismiss the idea as too low-class, even for me.

    I'll wait for the experts to provide an answer.
    """    

    return

label lad_day2_bedroom_doctor:

    $ change_room('bedroom_doctor') 

    """
    I didn't have time earlier to take a good look at the room.

    It feels a little weird being in here, but I might as well look for something useful.

    I search his personal effects when I stumble upon his medication suitcase.

    There's nothing out of the ordinary in there.

    A stethoscope, bandages, a few bottles of medication,...

    There's one in particular that he has more of than the others.

    "Laudanum" is written on the label.

    He has almost a dozen of those bottles.

    Laudanum... I've heard of that before.

    It's essentially opium.

    It looks like the doctor wasn't using it only on patients.
    """

    $ doctor_details.description_hidden.unlock('addict') 

    # TODO, should be a choice? Maybe every object should be a choice?
    """
    Just in case, I might as well take a few for myself.
    """

    $ lad_details.threads.unlock('laudanum')

    # TODO add pocketing sound?
    # TODO is the lad a thief? likely ADD HERE
    # TODO add LAUDANUM IN THE OBJECTS LIST?

    return
