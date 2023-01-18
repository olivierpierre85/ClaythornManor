# Generic captain Dialogs.
# Accessible from :
#                   - The lad

# ?TODO add extra choices possibilities?
label captain_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["captain_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["captain_generic_menu"])

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


label captain_generic_origin_psychic_1:

    captain """
    I come directly from London.

    I have been living there for the last two decades.    
    """

    psychic """
    London.

    Right.

    But that's not what I meant.
    """

    captain """
    I am sorry, what do you meant?
    """

    $ psychic_details.unlock_knowledge("racist")

    return 

label captain_generic_origin_psychic_2:
    
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
    """

    captain """
    TODO add chatGPT story here (all long story by captain should be chat GPT)
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