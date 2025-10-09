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

    $ unlock_map('bedroom_nurse')

    return


label nurse_generic_age:

    nurse """
    I am 42 years old.

    It's hard to believe really.

    I don't feel that old at all.
    """

    $ nurse_details.description_hidden.unlock('age')

    return

label nurse_generic_background_psychic:
    
    nurse """
    Oh well, the most obvious thing about me is that I am a nurse.

    I started young and served in various wars. 

    In peacetime, I usually took a job at a hospital.

    Now I mostly nurse the elderly. 
    """

    psychic """
    In an old person's facility?
    """

    nurse """
    No, not like that. I mostly assist wealthier individuals who require special in-house assistance.
    """

    psychic """
    Are you taking care of someone at the moment?
    """

    nurse """
    Not right now.

    And perhaps after I receive this prize, I won't have to.

    Nursing is an amazing job that I love,

    but it can be exhausting.
    """

    psychic """
    Yes, one can imagine.
    """

    $ nurse_details.description_hidden.unlock('job') 

    return


label nurse_generic_background_doctor:
    
    nurse """
    Oh well, the most obvious thing about me is that I am a nurse.

    I started young and served in various wars. 

    In peacetime, ....
    """

    doctor """
    Wait a minute, in which wars did you actually serve?
    """

    nurse """
    Well, the Great War, and before that I was...
    """

    doctor """
    Sorry, to interrupt, but I think I remember you now.
    
    Were you in China during the Boxer's Rebellion by chance?
    """

    nurse """
    I was indeed, I wouldn't think you would remember me.
    """

    doctor """
    Right, so we did work together.

    Why didn't you say something?
    """

    nurse """
    I didn't want to presume.

    I was a young nurse among many.

    And it was a very long time ago.
    """

    $ doctor_details.observations.unlock('remember_nurse')

    doctor """
    It was indeed.

    But it is nice to see again.
    """

    nurse """
    Likewise.
    """

    return

label nurse_generic_heroic_act_doctor:

    nurse """
    Well, I don’t wish to sound boastful.

    But I’ve been told I’m the nurse who’s served in the most wars in the whole country, apparently.
    """

    doctor """
    Truly? You kept going, even after everything that happened in China?
    """

    nurse """
    Indeed. I daresay some would have lost heart after what happened there.

    But not me. It only strengthened my belief that nursing was my true calling.

    When I returned to England, I kept volunteering wherever I was needed.
    """

    doctor """
    Then you must have witnessed a great many conflicts.
    """

    nurse """
    Yes. Before the Boxer Rebellion, there was the Cretan Revolt.

    And afterwards, several others — until, of course, the last one.

    Which I rather think will be the last for me.
    """

    doctor """
    We all hoped it would be the last for everyone.

    But I fear war is not likely to vanish from the world just yet.
    """

    nurse """
    No, I’m not so naïve as to think so.

    But one can at least hope that nothing as dreadful as the Great War will ever come again.
    """

    doctor """
    I sincerely hope you’re right, Miss Marsh.
    """

    $ nurse_details.description_hidden.unlock('heroic_act')

    return


label nurse_generic_heroic_act_psychic:
    
    nurse """
    It is nothing special, really.

    But it turns out I am the nurse who served in the most wars in the whole country, apparently.
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

    $ nurse_details.description_hidden.unlock('heroic_act') 

    return


label nurse_generic_manor:
    
    nurse """
    It's a grand house. 
    
    I've been in many houses of the same style, but none so big or impressive.
    """

    $ nurse_details.description_hidden.unlock('manor') 

    return