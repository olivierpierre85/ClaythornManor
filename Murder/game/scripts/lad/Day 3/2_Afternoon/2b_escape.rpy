label lad_day3_escape:
    
    call change_time(13,00, "Afternoon", "Sunday")

    lad """
    Well, I think I should come with you.

    It will be safer if the two of us go.

    We don't know what's outside.
    """

    captain """
    Alright, that's settled then.
    """

    psychic surprised """
    What?!

    You can't abandoned me here!

    There is a killer in this house.

    When you'll come back, I'll be dead.
    """

    captain """
    There is no need to be so dramatic.

    If you lock yourself up in your room, I am sure you'll be safe.
    """

    psychic """
    Really? Like Mister Manning was safe?
    """

    captain """
    That's different. Samuel Manning didn't suspect anyone would come for him.

    He probably was killed in his sleep.

    Or maybe he killed himself.
    
    So it will be different for you. You'll be on your guard.
    """

    psychic """
    And what good does that make me when someone breaks down my door?
    """

    """
    He pounders this for a second.
    """

    captain """
    Right. You might need a gun to defend yourself.

    Here, you can take this one.
    """

    """
    He hands her a small gun.
    """

    psychic """
    But... I don't know how to use this!
    """

    captain """
    It's simple, if someones breaks down your bedroom door.

    Just point it at them a press the trigger here.

    There is nothing more to it.
    """

    psychic """
    What, I don't know if I can do that, I, ...
    """

    captain """
    I am sure you can.

    Now you should go to your room.

    Close the door.

    Even move some furniture in front of it if you can.

    If anyone else than us tries to enter, just shoot at them.

    Understood?
    """

    """
    Amelia Baxter is visibly scared out of her mind.

    But the natural authority of Sushil Sinha makes her nod in acquiesce.
    """

    captain """
    Great.

    Now will leave you for now. There is no time to waste.

    But we will come back for you, I promise.
    """

    """
    And without waiting for a reply, he gestures me towards the entrance hall.
    """

    captain """
    Let's go mister Harring, the sooner the better.
    """
    
    """
    We leave Amelia Baxter behind us and we exit the manor.
    """

    $ change_room('manor_garden')

    # TODO captain asks about the gun room. Tell him you have it or not?

    captain """
    That was rather ungentlemanly to leave her alone like that.

    But I understand, I wouldn't want to stay in this house more than I have too either.
    """

    """
    He says he understands, but his face tells me he doesn't approve.

    He would have preferred I stayed in the house.
    """

    captain """
    Anyway, I don't think it's gonna be an easy walk.

    The roads must still be muddy, and if I recall well, the trip to the next house is at least 10 miles.
    
    Maybe more.

    So we will probably be on the road for a few hours.
    """

    """
    And like that, he started to move towards the exit gate.
    """

    scene forest_road

    if lad_details.objects.is_unlocked('gun') :

        """
        We have walked for about a hour when he stops.
        """

        lad """
        Is something wrong?
        """

        captain """
        I don't know, you tell me.
        """

        $ play_music('danger')

        """
        He gets a gun from his back pocket and points it at me.
        """

        lad surprised """
        What the hell?!
        """

        captain """
        Oh don't look so surprised.

        You don't really think you fooled me do you?

        I immediately saw the gun in your pocket this morning.

        If you thought you could just wait for me to turn my back on you, I am sorry to disappoint you.
        """

        lad surprised """
        No! That's not what I planned, it's ...
        """

        play sound gun

        """
        He shot at me.

        He missed.

        For the first time he looks panicked.

        I reach for the gun in my pocket.

        I point it at him, pull the trigger.

        But realizes it's empty.
        """

        play sound gun

        $ lad_details.saved_variables["day3_ending"] = "gun_downed"


            # the captain is dead too, but the killer was behind the forest and kills the captains 
    else:

        """
        We walked for about an hour whe he stops.
        """

        captain """
        Wait!

        Didn't you hear something?
        """

        lad """
        Not really.

        What do you mean?
        """

        $ play_music('danger')

        captain """
        I heard footsteps coming from the forest.

        I believe someone is following us.
        """

        lad surprised """
        What?!
        """

        captain """
        Don't say a word.

        Act like nothing unusual is happening.
        """

        lad """
        What are we gonna do?

        Should we run?
        """

        captain """
        No, I will try to surprise him.

        I think I have a good idea of where he is.

        I will run towards him.

        At my signal, just start running on the road to distract him.

        I will rush into the forest and try to disarm him.

        Are you ready?
        """

        lad """
        What?! No!

        I am not ready, it's too dangerous.
        """

        captain """
        Don't worry it will be fine.

        At my signal.

        Three.

        Two.

        One.

        Go!
        """

        """
        I don't have time to think.

        Instinctively, I start running.
        """

        play sound gun

        """
        A gun fires.

        I turn my head and see Sushil Sinha collapsing on to ground.

        But I can't stop.

        My legs are pushing me faster.

        I never ran so fast in my entire life.
        """

        pause 1

        $ play_music("mysterious")

        """
        After a few minutes, I am totally out of breath.

        I am not sprinting anymore. I just running slowly, barely faster than a fast walk.

        But I can't stop.

        When I found a rythm that's almost comfortable, I keep at it without stopping.

        Occasionally glancing back.

        But I don't see anyone.
        """

        pause 2

        $ lad_details.saved_variables["day3_ending"] = "escape"

    return