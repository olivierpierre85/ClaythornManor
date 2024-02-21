label day1_host_welcome_speech:

    host """ 
    Welcome, everyone. My apologies for keeping you waiting. 
    
    Now that we're all gathered, I'd like to express my gratitude once more.

    As you already know, you are here because of the heroic acts you've committed in the past.

    I've taken notice of these actions and felt it was my responsibility to extend a formal 'thank you.'

    I realize the invitation letter you received was somewhat vague, so let me clarify its contents now.

    My first gift to you is a stay at my manor. 
    
    You'll be fully catered to, enjoying the most refined food, expertly prepared by my personal chef.

    During the three days we'll spend together, we'll also partake in various activities, which I'm sure you'll find enjoyable.

    My second gift is a sum of eight thousand pounds, to be shared among you. 
    
    This is my way of thanking those as selfless as yourselves, who help others without thought of reward.
    """
    
    """
    Following her speech, our host settled back down in her chair.
    """

    return

label day2_breakfast_host_death:

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

label day2_breakfast_host_death_doctor:

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


label day2_breakfast_host_hunt:
    
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
