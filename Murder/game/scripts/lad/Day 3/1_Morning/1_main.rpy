# --------------------------------------------
#   Lad
#           
#   Sunday - Morning
# 
#   7:30 / 9:30 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic
#       - Dead : broken, doctor, drunk
#       -? : Host, nurse
#
#   Notes : 
#       - Map 90, 150 minutes
# --------------------------------------------
label lad_day3_morning:

    $ lad_details.add_checkpoint("lad_day3_morning") 

    call black_screen_transition("Ted Harring", "Sunday Morning")

    $ change_room('lad_room', irisout)

    if lad_details.saved_variables["day2_believe_psychic"]:
        call change_time(7, 30, "Morning", "Sunday", hide_minutes=True)
        # You talked to and believed the psychic
        # So she came to wake you at dawn
    else:
        # Otherwise, you'll have less time to explore
        call change_time(9, 30, "Morning", "Sunday", hide_minutes=True)

    play sound door_knock

    """
    I am awaken by the sound of frantic knocking at the door.
    """

    play sound door_knock

    if lad_details.saved_variables["day2_drunk"]:
        """
        My head is throbbing.

        I wish I could've slept longer.
        """    

    psychic """
    Mister Harring, are you there?
    """

    if lad_details.saved_variables["day2_believe_psychic"]:

        """
        Miss Baxter?

        Right, we agreed to wake each other up.

        I just didn't expect it to be this early.
        """

        lad """
        I'm coming!
        """

        """
        I quickly get dressed and open the door.

        Amelia Baxter enters, looking visibly nervous.
        """

        $ play_music('mysterious', 2)

        psychic """
        I believe my hunch was right yesterday.

        Something strange is afoot.
        """

        lad """
        What do you mean?
        """

        psychic """
        I haven't seen any staff members on my way here.

        At this hour, they should be busy with lighting fires, cleaning, and setting up breakfast.

        Yet, I neither saw nor heard anyone.

        It's as silent as a graveyard in here.
        """

        lad """
        Are you sure it's not just because it's so early?
        """

        psychic """
        I'm certain.

        I was up at this time yesterday, and the house was bustling with activity.

        Something's not right, I assure you.
        """

        lad """
        Okay, if you say so. 

        But how is that related to a robbery?
        """

        psychic """
        I'm not so sure anymore that this is about a robbery.

        I have a feeling it could be something much worse.
        """

        """
        A chill goes through my body.

        Worse than a robbery? What could she mean?

        But I'm hesitant to ask her.

        Instead, I try to appear confident.
        """

        lad """
        Alright, we'd better investigate then.
        """
    else:
        """
        Miss Baxter, again?

        What does she want now?
        """

        lad """
        I'm coming!
        """

        """
        I hastily dress and open the door.
        """

        lad """
        Miss Baxter, is everything okay?
        """

        $ play_music('mysterious', 2)

        psychic """
        I'm not sure.

        Something unusual seems to be happening.

        I woke up early as always and wanted to get a cup of tea before breakfast.

        But, there's no one around.
        """

        lad """
        What do you mean?
        """

        psychic """
        The staff is missing. Every single one of them.

        I searched everywhere - the kitchen, outdoors, everywhere.

        I haven't found anyone.
        """

        lad """
        Perhaps they're still sleeping?
        """

        psychic """
        Oh, Mister Harring, that's highly unlikely.

        They're usually up at dawn, preparing the house for the day.

        It's inconceivable that they all overslept.

        Moreover, I tried checking on Lady Claythorn, but she's not answering.
        """

        lad """
        Try not to worry too much. I'm sure there's a reasonable explanation.
        """

        psychic """
        I'm not so sure.

        But I don't want to continue my search alone.

        Would you accompany me to check on the others?
        """

        lad """
        Well, since I'm up, I might as well.

        If it helps put your mind at ease.
        """

        """
        We decide it's best to check each room together.

        So, we start with...
        """

    if lad_details.saved_variables["day2_believe_psychic"]:
        $ time_left = 135
        call change_time(8, 45)
    else:
        $ time_left = 45
        call change_time(10, 15)


    call run_menu(lad_details.saved_variables["day3_morning_map_menu"])

    call change_time(11,00)

    $ change_room('tea_room')

    if lad_details.saved_variables["day3_morning_captain_found"]:

        """
        I doubt we'll find anyone now.

        So we settled in the tea room to wait for the captain.
        """

        captain """
        It's unbelievable, but it seems we're the only three living souls left here.

        Did you find anything?
        """

        lad """
        Nothing.

        It seems everyone is gone.

        Except for the bodies.
        """

    else:

        """
        Just when we started losing hope, we decided to rest in the tea room.

        But as we settled down, an authoritative voice echoed from outside the room.
        """

        captain """
        Is anyone here?
        """

        """
        Without hesitation, I responded.
        """

        lad """
        Yes, Ted Harring. I'm here, and Amelia Baxter's with me.
        """

        """
        Amelia stiffens. I sense her unease, perhaps thinking I replied too quickly.

        It's too late for second thoughts now.

        Captain Sinha soon joins us in the room.
        """
        
        call lad_day3_morning_meeting_captain

    lad """
    By the way, did you check on Samuel Manning?

    You're the only one with the key to his room.
    """

    captain """
    No, not yet. I assumed he couldn't have gone far.

    But you're right, we should check on him.
    """

    lad """
    I think so too.

    We'll follow you.
    """

    """
    Amelia shoots me a concerned look but remains silent.

    She follows us nonetheless.
    """

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
    He unlocks the door, and we trail behind.

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

    Miss Baxter lets out a scream.
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

    $ stop_music()

    jump lad_day3_afternoon

    return
