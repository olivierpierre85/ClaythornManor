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
    It is me again.

    I wanted to see how you were faring.
    """

    """
    She slightly opens the door but stays inside.
    """

    nurse """
    Oh, Mrs Baxter, I am not feeling at all well.

    Could it wait?
    """

    play sound woman_cough

    """
    A harsh cough rakes her chest.
    """

    pause 1.0

    nurse """
    I am sorry.
    """

    psychic """
    Are you quite all right?
    """

    nurse """
    Yes, it is nothing, really.
    
    I am only a little under the weather.
    """

    """
    She takes out her handkerchief and presses it to her mouth.

    She tries to slip it quickly back into her pocket.

    Yet I catch a glimpse of blood upon the linen.

    She is worse than she would have me believe.
    """

    nurse """
    I should lie down now.
    """

    """
    She is plainly uncomfortable.

    But perhaps I could press her a little.
    """

    call run_menu(TimedMenu("psychic_day2_no_hunt_bedroom_nurse", [
        TimedMenuChoice("Insist, something is clearly wrong here", 'psychic_day2_no_hunt_bedroom_nurse_insist', 10, early_exit=True),
        TimedMenuChoice("Do not push her further", 'psychic_day2_no_hunt_bedroom_nurse_ignore', 10, early_exit=True), 
    ]))
    
    return


label psychic_day2_no_hunt_bedroom_nurse_insist:

    psychic """
    I am afraid it is important.

    Might you let me in? It will not take long.
    """

    nurse """
    Very well, do come in.
    """

    $ change_room("bedroom_nurse")

    nurse """
    What can I do for you?
    """

    psychic """
    Nothing, rather the reverse.

    I am sorry to intrude, but I noticed the blood on your handkerchief.

    I wondered whether there is anything I can do to help.
    """

    nurse """
    I suppose I could not have hidden it forever.

    You see, I am suffering from a most serious disease.
    
    One for which there is no known cure. Consumption.
    """

    play sound woman_cough

    """
    Another racking cough takes her.
    """

    $ psychic_details.observations.unlock('nurse_sick')

    psychic """
    I am so very sorry.

    When did you learn of it?
    """

    nurse """
    A couple of years ago.

    And if I am to trust my doctor, I have perhaps a year at most.
    """

    psychic """
    My goodness, how horrible.

    Is there anything at all I can do?
    """

    nurse """
    There is nothing to be done.

    My doctor has prescribed a strong draught that I must take before bed.
    
    It usually helps me to sleep.

    At times I must take it during the day, which is why I am so often in my room, resting.

    But you should go now. I shall try to sleep a little before dinner.

    Thank you for your kindness.
    """
    
    psychic """
    Of course. I shall go.
    """

    nurse """
    Thank you.
    """  

    $ nurse_details.description_hidden.unlock('sick')    

    return


label psychic_day2_no_hunt_bedroom_nurse_ignore:

    psychic """
    It can wait, of course. Goodbye, Miss Marsh.
    """

    nurse """
    Goodbye, Miss Baxter.
    """

    return
