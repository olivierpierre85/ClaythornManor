# Generic nurse Dialogs.
# Accessible from :
#                   - The Psychic

#?TODO add extra choices possibilities?
label nurse_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["nurse_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["nurse_generic_menu"])

    return


label nurse_generic_weather_saturday:

    nurse """
    This night was dreadful, wasn't it?

    I couldn't sleep at all.
    """

    return


label nurse_generic_weather_sunday:

    return


label nurse_generic_room:

    nurse """
    My room is named after "Queen Alexandra."

    Like the queen mother, I believe.
    """

    $ unlock_map('nurse_room')

    return


label nurse_generic_age:

    nurse """
    I am 42 years old.

    It's hard to believe really.

    I don't feel that old at all.
    """

    $ nurse_details.description_hidden.unlock('age')

    return

label nurse_generic_background:
    
    nurse """
    Oh well, the most obvious thing about me is that I am a nurse.

    I started young and served in various wars. 

    Then I found a job at a hospital that I kept for a while.

    Now I mostly nurse the elderly. 
    """

    psychic """
    In an old person's facility?
    """

    nurse """
    No, not like that. I mostly assisted wealthier individuals who required special in-house assistance.
    """

    $ nurse_details.description_hidden.unlock('manor') 

    psychic """
    Are you taking care of someone at the moment?
    """

    nurse """
    Not lately.

    And perhaps after I receive this prize, I won't have to.

    Nursing is an amazing job that I love,

    but it can be exhausting.
    """

    psychic """
    Yes, one can imagine.
    """

    $ nurse_details.description_hidden.unlock('job') 

    $ current_character.saved_variables['knows_nurse_background'] = True

    return

label nurse_generic_heroic_act:
    
    nurse """
    It is nothing that I did, really.

    But it turns out I was the nurse who served for the longest during wartime in the whole country, apparently.
    """

    psychic """
    Oh my, that is extraordinary. 

    But how many wars did you serve in?
    """

    nurse """
    There have been quite a few, that's true.

    I started my career really early during the Cretan Revolt, where I was stationed on a British frigate.
    
    But I truly experienced the horror of war for the first time during the Boxer Rebellion of 1899.

    The brutality of the combats, then later, the lives they left behind made an impression that would last my whole life.
    
    Afterwards, I followed the army again in small engagements in India.

    When the Great War started, I thought at first that I was too old to go.

    But the atrocities I kept hearing about left me no choice.

    I had to be there to help.

    It's what I do.

    So I joined again and lasted throughout the whole duration of the war.
    """

    psychic """
    How commendable.
    """

    return

label nurse_generic_manor:
    
    nurse """
    It's a grand house. 
    
    I've been in houses of the same style, but none so big or impressive.
    """

    $ nurse_details.description_hidden.unlock('manor') 

    return