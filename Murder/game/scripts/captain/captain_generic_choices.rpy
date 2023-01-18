# Generic captain Dialogs.
# Accessible from :
#                   - The lad

# ?TODO add extra choices possibilities?
label captain_generic:

    if not 'captain_generic_menu' in locals():
        $ captain_generic_menu = TimedMenu([
            # TimedMenuChoice('What do you think of this weather?', 'captain_generic_weather_friday', 5, condition = "current_day == 'Friday'"),
            # TimedMenuChoice('What do you think of this weather?', 'captain_generic_weather_saturday', 5, condition = "current_day == 'Saturday'"),
            # TimedMenuChoice('What do you think of this weather?', 'captain_generic_weather_sunday', 5, condition = "current_day == 'Sunday'"),
            # TimedMenuChoice('Tell me more about yourself.', 'captain_generic_background', 15),
            # TimedMenuChoice('Why were you invited here?', 'captain_generic_heroic_act', 20, condition = "captain_details.is_knowledge_unlocked('background')"),
            # TimedMenuChoice('What do you think of this place?', 'captain_generic_manor', 10),
            TimedMenuChoice('Where are you from?', 'captain_generic_origin', 5),
            # TimedMenuChoice('What room are you in?', 'captain_generic_room', 5, condition = "not is_unlock_map('captain_room')"),
            # TimedMenuChoice('What do you think of the other guests?', 'captain_generic_other_guests_friday', 0, condition = "current_day == 'Friday'"),
            # TimedMenuChoice('What do you think of the other guests?', 'captain_generic_other_guests_saturday_morning', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
            # TimedMenuChoice('What do you think of the other guests?', 'captain_generic_other_guests_saturday_hunt', 0, keep_alive = True, condition = "(current_day == 'Saturday' and current_phase == 'Hunt')"),
            # TimedMenuChoice('You don\'t have anymore questions for her', 'captain_generic_cancel', 0, keep_alive = True, early_exit = True)
        ], image_right = "captain")
    else:
        # Reset if previous early exit
        $ captain_generic_menu.early_exit = False

    call run_menu(captain_generic_menu)

    return


label captain_generic_weather_friday:

    captain """
    I can see a storm is coming.

    And it looks like a big one.
    """

    return

label captain_generic_weather_saturday:

    captain """
    d
    """

    return

label captain_generic_weather_sunday:

    captain """
    d
    """

    return

label captain_generic_room:

    captain """
    d
    """

    $ unlock_map('captain_room')

    return


label captain_generic_origin:

    captain """
    I come directly from London.

    I have been living there for the last two decades.    
    """

    if current_character.text_id == "psychic":

        psychic """
        London.

        Right.

        But that's not what I meant. I wanted to say where do you come from before arriving in England?
        """

        captain """
        Oh ... I was raised in Calcutta. 
        
        But I've been living in the UK for so long I don't even think about it anymore.
        """

        psychic """
        Alright. Calcutta behind in the far east right?
        """

        captain """
        In North India yes.

        I was born there.

        TODO long story
        """

        """
        My god, he is ready to tell me his whole life story.

        How rude.

        And there is no way to avoid him here.

        So I nod in assent and barely listens to what he is saying.
        """

        $ captain_details.unlock_knowledge('talker') 



    return
    

label captain_generic_heroic_act:
    
    
    
    return

label captain_generic_background:
    

    return
    
label captain_generic_manor:
    captain """
    o
    """


    
    return

label captain_generic_cancel:
    return