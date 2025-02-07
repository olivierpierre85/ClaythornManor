label lad_day3_escape:

    call change_time(13,00, "Afternoon", "Sunday")

    lad """
    I think I should come with you.
    
    It would be safer for both of us.
    
    We don't know what's outside.
    """

    captain """
    Alright, that's settled then.
    """

    psychic surprised """
    What?!
    
    You can't abandon me here!
    
    There's a killer in this house.
    
    When you come back, I might be dead.
    """

    captain """
    There's no need to be so dramatic.
    
    If you lock yourself in your room, you'll likely be safe.
    """

    psychic """
    Really? Like Mister Manning was safe?
    """

    captain """
    That's different. Samuel Manning didn't expect anyone would come for him.
    
    He was probably killed in his sleep.
    
    Or maybe he took his own life.
    
    For you, it'll be different. You'll be on your guard.
    """

    psychic """
    What good will that do when someone breaks down my door?
    """

    """
    He ponders this for a second.
    """

    captain """
    Right. You might need a gun to defend yourself.
    
    Here, take this one.
    """

    """
    He hands her a small gun.
    """

    psychic """
    But... I don't know how to use this!
    """

    captain """
    It's simple. If someone breaks down your bedroom door, just point it at them and press the trigger.
    
    That's all there is to it.
    """

    psychic """
    I don't know if I can do that, I...
    """

    captain """
    I know you can.
    
    Now, go to your room and lock the door.
    
    Maybe even move some furniture in front of it.
    
    If anyone other than us tries to enter, shoot them.
    
    Understood?
    """

    """
    Amelia Baxter is visibly terrified.
    
    But the natural authority of Sushil Sinha makes her nod in agreement.
    """

    captain """
    Good.
    
    We'll leave you for now. Time is of the essence.
    
    But we will come back for you, I promise.
    """

    """
    Without waiting for a reply, he gestures for me to follow him to the entrance hall.
    """

    captain """
    Let's go, Mister Harring. The sooner, the better.
    """
    
    """
    We leave Amelia Baxter behind and exit the manor.
    """

    $ change_room('manor_garden')

    # TODO captain asks about the gun room. Tell him you have it or not?

    captain """
    It was rather ungentlemanly to leave her alone like that.
    
    But I understand. I wouldn't want to remain in this house any longer than necessary either.
    """

    """
    He says he understands, but his expression suggests disapproval.
    
    He likely would have preferred if I stayed in the house.
    """

    captain """
    In any case, this won't be an easy journey.
    
    The roads are probably still muddy, and if I recall correctly, the distance to the next house is at least 10 miles.
    
    Maybe even more.
    
    It will likely take us a few hours on the road.
    """

    """
    With that, he begins moving towards the exit gate.
    """

    $ change_room("forest_road")

    if lad_details.objects.is_unlocked('gun'):

        """
        We had been walking for about an hour when he stops.
        """

        lad """
        Is something wrong?
        """

        captain """
        I don't know, you tell me.
        """

        $ play_music('danger')

        """
        He takes out a gun from his back pocket and points it at me.
        """

        lad surprised """
        What the hell?!
        """

        captain """
        Oh, don't act so surprised.
        
        Did you really think you fooled me?
        
        I spotted the gun in your pocket this morning.
        
        If you were waiting for a chance to catch me off-guard, you're in for a disappointment.
        """

        lad surprised """
        No! That's not what I planned, it's ...
        """

        play sound gun

        """
        He fires at me.
        
        He misses.
        
        For the first time, he looks panicked.
        
        I reach for the gun in my pocket.
        
        Pointing it at him, I pull the trigger.
        
        But then realize it's empty.
        """

        play sound gun

        $ lad_details.saved_variables["day3_ending"] = "gunned_down"

        # the captain is dead too, but the killer was lurking in the forest and kills the captain 
    else:

        """
        We had been walking for about two hours when he stops.
        """

        captain """
        Wait!
        
        Did you hear that?
        """

        lad """
        Not really.
        
        What is it?
        """

        $ play_music('danger')

        captain """
        I heard footsteps from the forest.
        
        I think someone's following us.
        """

        lad surprised """
        What?!
        """

        captain """
        Keep quiet.
        
        Pretend nothing's wrong.
        """

        lad """
        What should we do?
        
        Should we make a run for it?
        """

        captain """
        No, I'll try to ambush him.
        
        I think I've pinpointed his location.
        
        I'll charge at him.
        
        When I give the signal, start running on the road to divert his attention.
        
        I'll dash into the forest to try and disarm him.
        
        Ready?
        """

        lad """
        What?! No!
        
        This is too risky!
        """

        captain """
        Trust me, it'll work.
        
        On my mark.
        
        Three.
        
        Two.
        
        One.
        
        Go!
        """

        """
        Before I can even think, I start running.
        """

        play sound gun

        """
        A gunshot rings out.
        
        I glance back to see Sushil Sinha collapsing to the ground.
        
        But I can't stop.
        
        My legs push me forward faster than ever before.
        
        I've never run this fast in my entire life.
        """

        pause 1

        call wait_screen_transition()

        $ play_music("mysterious")

        """
        Minutes later, I'm gasping for breath.
        
        I'm not sprinting anymore, just jogging — barely faster than a brisk walk.
        
        But I have to keep going.
        
        I find a nearly comfortable pace and maintain it, occasionally glancing behind me.
        
        Thankfully, no one is in sight.
        """

        pause 1

        """
        After what felt like an eternity, I finally reached the town.
        """

        $ lad_details.saved_variables["day3_ending"] = "escape"

    return
