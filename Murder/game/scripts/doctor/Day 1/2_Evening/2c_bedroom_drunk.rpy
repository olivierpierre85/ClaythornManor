label doctor_day1_evening_bedroom_drunk_enter:

    $ change_room("bedroom_drunk")

    """
    I step into the room.

    It is a dreadful mess.

    The bottles of whisky, some already emptied, give me a fair idea whose room this is.

    There is no doubt that Samuel Manning sleeps here.
    """
    
    $ unlock_map("bedroom_drunk")

    $ play_music("mysterious")

    """
    I glance around, uncertain what I am hoping to find, when I notice a letter upon the desk.

    I take it up.

    The first part is written in a fine, elegant hand.
    """

    call drunk_letter_first_part

    """
    What on earth does this mean?

    Who could have written such a thing?

    Still, what troubles me most is the second part — barely legible, clearly added later by Samuel Manning himself.
    """

    call drunk_letter_second_part

    """
    My legs feel weak.

    I sit on the edge of the bed, struggling to make sense of it all.

    Someone in this house means me harm.

    And they are trying to use Samuel Manning to hurt me.

    I try to remember him, but I cannot say for certain that I ever treated his wife.

    That does not mean the accusation is false. It is entirely possible I did, and have simply forgotten.

    It must be someone who knows me well, yet I do not recall recognising anyone so far.

    Then again, I have not been paying much attention.

    But what should I do now?

    The prudent choice would be to leave this place at once.

    Yet to explain my departure, I might have to reveal what I found here — and that could prove troublesome.

    I cannot afford to lose the prize money either; heaven knows I need it.

    Besides, it could simply be a cruel joke, or some wretched misunderstanding.

    What should I do now?
    """

    call run_menu( 
        TimedMenu("doctor_day1_evening_bedroom_drunk_enter", [
            TimedMenuChoice("Do not risk your life — leave this place", "doctor_day1_evening_bedroom_drunk_leave_manor", 20, early_exit=True),
            TimedMenuChoice("Do not risk losing the money — stay", "doctor_day1_evening_bedroom_drunk_stay", early_exit=True),
        ])
    )

    return


label doctor_day1_evening_bedroom_drunk_leave_manor:

    """
    Why am I even considering staying here.

    I should leave now, and warn everyone about this.

    I believe that they should all be gathered in the billiard room.
    """

    $ change_room("billiard_room") 
    
    """
    Indeed I find most people here gathered around Captain Sinha.

    I interrupt him.
    """

    doctor """
    Sorry Captain, but I have something that I think you should see.
    """

    """
    I hand the letter to him.

    And he reads it aloud for the assembly.
    """

    captain """
    What's the meaning of this? 

    Where did you find this?
    """

    doctor """
    In Samuel's Manning room.
    """

    captain """
    Really, what were you doing there?
    """

    doctor """
    Well, the door was open, and I was...
    """

    drunk """
    Wait? You went into my room?

    What made you think you do such a thing?
    """

    doctor """
    It doesn't matter now, how can you explain that letter?
    """

    drunk """
    I've never seen this letter before.

    It's not mine.
    """

    doctor """
    Really? And we are supposed to believe you?
    """

    drunk """
    I don't think anyone should be believing you.

    Someone who thinks it appropriate to enter people's room.

    Unless you didn't enter my room, you may have written this yourself.
    """

    doctor """
    Why would I have done that, this makes no sense at all.
    """

    drunk """
    No less sense that what you're implying doctor.

    Do you really expect someone here to believe you?
    """

    """
    I look around the room and see that everyone is looking at us.

    They have an air of perplexity, nobody seems to know what to do about this exchange.

    We remain silent a moment then Captain sinha starts speaking.
    """

    captain """
    There is something wrong here, but I can't say whose at fault.
    """

    doctor """
    Clearly it can't be me, look at Samuel Manning.

    Is he even drunk anymore?
    """

    drunk """
    What makes you say I was drunk?

    Beside, I can gather my wits when needs be.
    """

    captain """
    Stop now!

    I don't understand any of this. We should think about this with a rested head.
    
    Lady Claythorn, what do you think?
    """

    """
    Our is visibly shook, yet she manages to answer.
    """

    host """
    I .. I don't know.

    I am not sure who to believe.

    What do you think we should do Captain?
    """

    captain """
    Well, we won't solve this in a few seconds, this requires thoughts.

    I think we should lock those two in their room until we reach a conclusion.
    """

    doctor """
    What? No!

    I must leave, and right now. I am not safe here.
    """

    captain """
    It is very late to leave now, besides, the storm will make the journey dangerous.

    You'll be safer in your room.
    """

    """
    I pounder that for a second. It is true that leaving now would be risky.

    Yet, staying in my room doesn't feel particulalrly safe ether.

    Everyone is looking at me with unease, I can tell they don't really believe me.
    """

    doctor """
    Fine, I'll go to my room.

    But I want your word you'll let me leave tomorrow at the earliest.

    I don't want to remain one second more that it is necessary.
    """

    captain """
    You have my word doctor.
    
    And what about you Mister Manning?
    """

    drunk """
    All right, I'll go to my room too.

    It's late anyway.
    """

    captain """
    Well it's decided, please follow me Doctor Baldwin.
    """

    """
    Captain Sinha and the footman come with me to my room.

    The butler and Lady Claythorn follow Samuel Manning to his.

    I am not reassured, but I feel like I have no other choice.

    I enter my room while the butler and Captain Sinha stay behind.
    """

    $ change_room("bedroom_doctor")

    captain """
    Sorry about this doctor Baldwin. I am sure we will reach an understanding soon enough.

    In the meantime we will lock you in here.
    """

    play sound door_locked

    """
    Well, I don't want to wait doing nothing, so I barricade myself in case someone I don't trust comes.
    """

    play sound moving_furniture

    """
    NOw all I have to do is wait.
    """
    
    call wait_screen_transition()

    call change_time(23,30)

    """
    After a very long time.

    Someone knocks at my door.
    """

    play sound door_knock

    captain """
    Doctor Baldwin, after some discussion, we've decided that you may be right.

    So we will all leave tomorrow morning.

    Lady Claythorn has agreed to give our present right before.

    In the meantime, we will all feel safer if you and Samuel Manning stayed there for the night.
    """

    doctor """
    Al right, I already barricaded myself anyway.
    """

    captain """
    Good choice doctor, again I am sorry for the inconvenience.
    """

    doctor """
    That is all right, have a good night captain.
    """

    captain """
    Good night Doctor.
    """

    """
    Well, at least this nightmare will be over soon.
    """

    # TODO: Also death by OD????? Easier choice.
    # Or do something else?

    # TODO jump to ending
    return


label doctor_day1_evening_bedroom_drunk_stay:

    """
    I do not believe I am in any great danger.

    I shall stay, though I must be cautious from now on.

    Especially around Samuel Manning.

    And I should try to discover who could have written this wretched letter.
    """

    $ doctor_details.objects.unlock("drunk_letter")

    $ play_music("PREVIOUS")

    return
