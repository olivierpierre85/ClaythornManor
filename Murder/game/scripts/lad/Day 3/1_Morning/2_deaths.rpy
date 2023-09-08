label lad_day3_morning_deaths:

    $ change_room("bedrooms_hallway")

    $ unlock_map('drunk_room')

    play sound door_knock

    captain """
    Mister Manning, are you there?
    """

    """
    No response.
    """

    captain """
    Alright, I'm going in.
    """

    """
    He unlocks the door, and we trail behind him.

    But as I step inside, Captain Sinha tries to halt us.
    """

    captain """
    Wait! Don't come in.
    """

    """
    But it's already too late.
    """

    $ change_room('drunk_room')
    
    $ play_music('scary', fadeout_val=1)

    """
    The sight inside is beyond horrifying.

    Samuel Manning lies in his bed, drenched in blood, his throat slashed multiple times.

    Pale as a sheet, his eyes frozen in a ghastly stare.

    Miss Baxter lets out a small scream.
    """

    #TODO: add woman scream?

    captain """
    Miss Baxter, please exit the room.
    """

    """
    She's speechless, her gaze fixed on the macabre scene.

    Sushil Sinha gently pulls her arm, leading her out. I quickly follow.
    """

    $ change_room("bedrooms_hallway")

    captain """
    I regret letting you see that.

    You shouldn't have entered the room.
    """

    psychic surprised """
    Is... is he... dead?
    """

    captain """
    I'm afraid so.
    """

    lad surprised """
    Are you certain?

    Shouldn't we check his pulse?

    Maybe... just maybe, there's a chance he's alive.
    """

    """
    My voice trembles as I speak, realization dawning on me.
    """

    captain """
    I'm sorry, but it's too late.

    I've seen enough to know. He's been gone for a while.

    Likely since last night.
    """

    psychic """
    Oh my God.
    """

    """
    Tears spill from her eyes.

    The weight of shock renders me motionless.

    To help us recover, Sushil guides us back to the tea room.
    """

    $ change_room("tea_room")

    # NEW TEXT

    captain """
    Miss Baxter, you should probably rest here for a little bit.

    I have something to check out, and I'll be back soon.

    Mister Harring, would you mind coming with me?
    """

    """
    I'm still shaken from what we saw, but doing something might help me recover my senses.
    """

    lad """
    Well, sure.

    I'll follow you.
    """

    psychic """
    Please don't be long.
    """

    captain """
    Don't worry, this should only take a few minutes.
    """ 

    """
    He walks back up the stairs and stands in front of another room.
    """

    $ change_room("bedrooms_hallway")

    captain """
    It's Miss Marsh's room.

    It was locked when I tried to open the door earlier.

    At the time, I didn't dare to go further.

    But now, I'm afraid I have to open it by force.
    """

    lad """
    Do you believe she could still be in there?

    Then she would be...
    """

    captain """
    Dead, I'm afraid.

    After what we saw, I think it's a very strong possibility.
    """

    lad """
    Oh my God.
    """

    """
    Captain Sinha draws a deep breath, clenches his fists, and then forcefully kicks the door. 
    
    It bursts open with a deafening crack.
    """

    $ change_room("nurse_room")

    """
    The room is eerily quiet.
    
    And there she is—Rosalind Marsh—lying peacefully on her bed.
    
    There is a trace of blood on the corner of her mouth.
    """

    lad """
    Is she...?
    """

    captain """
    Dead, yes. It appears she was poisoned. 
    """

    """
    My heart pounds in my chest. 
    
    The reality of two dead bodies sets in, and the room feels like it's closing in on me.
    """

    captain """
    Let's return to the tea room. 
    
    We need to warn Miss Baxter and decide our next steps.
    """

    $ change_room("tea_room")

    psychic """
    You've been gone for a while. What happened?
    """

    captain """
    I'm afraid we've found Miss Marsh. She has also passed away.
    """

    psychic """
    No... Not another one...
    """

    """
    Our eyes meet, and though no words are spoken, the gravity of the situation is understood by all.
    """

    return
