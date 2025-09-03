label psychic_day2_no_hunt_bedroom_nurse_blood:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on Rosalind Marsh's door.
    """

    nurse """
    Yes? Who is there?
    """

    psychic """
    It's me again.

    I wanted to see how you were doing.
    """

    """
    She slightly opens the door but stays inside.
    """

    nurse """
    Oh, Mrs. Baxter, I'm actually not feeling well.

    Can it wait?
    """

    play sound woman_cough

    """
    She coughs abruptly, a sound that seems to echo painfully.
    """

    pause 1.0

    nurse """
    Sorry about that. 
    """

    psychic """
    Are you alright?
    """

    nurse """
    Yes, it's nothing, really.
    
    I am just a bit under the weather.
    """

    """
    She takes out her handkerchief and brings it to her mouth.

    Then, she tries to quickly put it back in her pocket.

    But I still caught a glimpse of a trace of blood on it.

    She is worse than she wishes to show.
    """

    nurse """
    Well, I should go now.
    """

    """
    She is obviously not comfortable with the situation.

    But maybe I should press her to tell me more.
    """

    call run_menu(TimedMenu("psychic_day2_no_hunt_bedroom_nurse", [
        TimedMenuChoice("Insist, there is clearly something wrong with her", 'psychic_day2_no_hunt_bedroom_nurse_insist', 10, early_exit=True),
        TimedMenuChoice("Do not push any further", 'psychic_day2_no_hunt_bedroom_nurse_ignore', 10, early_exit=True), 
    ]))
    
    return


label psychic_day2_no_hunt_bedroom_nurse_insist:


    psychic """
    I am afraid it is important.

    Could you let me in? It won't take long.
    """

    nurse """
    All right then, come on in.
    """

    $ change_room("bedroom_nurse")

    nurse """
    What can I do for you?
    """

    psychic """
    Nothing, it's more the other way round.

    I am sorry, I do not mean to intrude, but I noticed the blood on your handkerchief.

    I was wondering if there was anything I could do to help you.
    """

    nurse """
    Well, I suppose I could not have hidden it forever.

    You see, I am suffering from a very serious disease.
    
    One that has no known cure: consumption.
    """

    play sound woman_cough

    """
    She lets out another strong cough.
    """

    $ psychic_details.observations.unlock('nurse_sick')

    psychic """
    I am so sorry.

    When did you find out?
    """

    nurse """
    A couple of years ago.

    And if I trust my doctor, I probably don't have more than another year left in me.
    """

    psychic """
    My goodness, how horrible.

    Could I help you with anything?
    """

    nurse """
    There is nothing to be done.

    My doctor prescribed me a strong medicine that I have to take before going to bed.
    
    That usually helps me sleep.

    Sometimes I have to take it during the day, that's why I am often in my room, resting.

    But you should go now, I will try to rest a little before dinner.

    Thank you for your concern anyway.
    """
    
    psychic """
    Of course, I'll go.
    """

    nurse """
    Thanks.
    """  

    $ nurse_details.description_hidden.unlock('sick')    

    return


label psychic_day2_no_hunt_bedroom_nurse_ignore:

    psychic """
    No, it can wait for now, of course. Goodbye, Miss Marsh.
    """

    nurse """
    Goodbye, Miss Baxter.
    """

    return