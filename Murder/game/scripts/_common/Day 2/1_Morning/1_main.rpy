# ------------------------------------
#               HOST
# ------------------------------------
label common_day2_morning_host_death:

    """
    Suddenly, Lady Claythorn and the butler are back in the room.
    """

    captain """
    Lady Claythorn, what is happening?
    """

    """
    The lady is visibly distressed.
    """

    host """
    I'm sorry to announce such horrible news, everyone.

    It appears that Mister Moody passed away in his sleep last night.
    """

    $ play_music('scary')

    """
    The room instantly falls silent.
    """

    captain """
    Do we know what happened?
    """

    host """
    Doctor Baldwin is examining him right now.

    He will likely tell us more later.
    """

    """
    She then sits down in her chair.

    Everyone looks shaken up.
    """

    lad """
    How terrible.
    """

    psychic """
    Yes, such sad news.
    """

    """
    We continue eating slowly in silence for a moment when the doctor enters the room.
    """

    return


label common_day2_morning_host_death_doctor:

    host surprised """
    Doctor Baldwin, can you tell us more about what happened?
    """

    doctor """
    I can't say anything definitive for now.

    But it's very likely a natural death, possibly triggered by an old wound from the war.
    
    In any case, we need to call the town to ask for an ambulance.
    """

    # TODO: Add lines? Are they broken? Or does the host pretend everything is fine so everyone stays here?
    host """
    Yes, of course.

    My butler will take care of it.
    """

    doctor """
    Very well.
    """

    """
    We then continue eating in sad silence.

    Nobody speaks much.
    """

    return


label common_day2_morning_host_hunt:
    
    host """
    Well, as I mentioned earlier, activities were planned for today.

    This morning, those who wished to were supposed to go on a hunt.

    A sad event has happened, but it's not a reason to remain idle.

    So, if no one objects, I propose that we continue according to what was planned.
    """

    """
    A murmur of assent runs through the assembly.
    """

    host """
    Excellent.

    Everything is ready for those who wish to join the hunt. 
    
    I know most of you are probably not accustomed to this type of event.

    That's why our staff can lend you everything you'll need—clothes, guns—and they will also assist you throughout the event.

    Of course, you can choose to simply stay here.

    You can relax and enjoy the warmth of the house until the others return.
    """

    return

# ------------------------------------
#               LAD/PSYCHIC
# ------------------------------------
label common_day2_morning_lad_psychic:

    psychic """
    Hello, Mister Harring. How are you?
    """

    lad """
    Very well, thank you.
    """

    psychic """
    I was wondering if everyone would join us on time.
        
    There are still a few people missing.

    For instance, I don't think we'll see Mister Manning anytime soon.

    He was so drunk yesterday that I wouldn't be surprised if he doesn't show up before noon.
    """

    if current_character == lad_details:
        
        """
        Suddenly, Samuel Manning enters the room.

        He stumbles to the buffet table and picks up a plate, visibly shaking.
        """

    else:

        """
        Right after saying those words, Samuel Manning steps into the room.

        Displaying evident unease, he makes his way to the buffet and, with trembling hands, selects a plate.

        He appears to still be drunk, or at least seriously hungover.
        """

    psychic angry """
    Well, I spoke too soon. Here he is. And in such a state.

    How dreadful.
    """

    if current_character == lad_details:

        """
        At the same moment, the butler rushes into the room.
            
        He goes to Lady Claythorn and whispers something in her ear.

        I can tell it's not good news.

        She looks shocked and worried.

        She stands up and walks in my direction, then stops in front of the doctor.
        """

    else:

        """
        While I am watching Samuel Manning, the butler enters and discreetly shares a message with Lady Claythorn.
        
        Her alarmed expression indicates the gravity of the news. 
        
        Rising, she approaches, pausing only when she reaches the doctor.
        """
    
    host """
    Doctor Baldwin, I'm sorry to interrupt your breakfast, but would you mind coming with me?

    We need your assistance.
    """

    """
    Without hesitation, Daniel Baldwin stands up.
    """

    doctor """
    Of course, I'll follow you.
    """

    return