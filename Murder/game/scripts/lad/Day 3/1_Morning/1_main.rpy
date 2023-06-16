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
        call change_time(7,30, "Morning", "Sunday", hide_minutes = True)
        # You talked to and believed psychic
        # So she came to wake you at dawn
    else:
        # Otherwise, you'll have less time to explore
        call change_time(9,30, "Morning", "Sunday", hide_minutes = True)

    play sound door_knock
    
    """
    I woke up suddenly with the sound of someone knocking frantically at the door.
    """

    play sound door_knock

    if lad_details.saved_variables["day2_drunk"]:
            """
            My head hurts like crazy.

            Oh my god, I wish I could sleep more.
            """    

    psychic """
    Mister Harring are you there?
    """
    
    if lad_details.saved_variables["day2_believe_psychic"]:

        """
        Miss Baxter?

        Right, we agreed to wake each other up.

        I just didn't think it would be that early.
        """

        lad """
        I am coming !
        """

        """
        I dress up in a hurry and open the door.

        Amelia Baxter enters, visibly nervous.
        """

        $ play_music('mysterious', 2)

        psychic """
        I believe I was right yesterday.

        Something strange is happening.
        """

        lad """
        What do you mean?
        """

        psychic """
        I didn't run into any staff members on my way here.

        At this hour, they should be busy with the fires, the cleaning, setting up breakfast.

        But I saw nor heard anything.

        It's quiet as a cemetery in here.
        """

        lad """
        Are you sure it's not normal?

        It's still very early.
        """

        psychic """
        I don't think so.

        I woke at this hour yesterday and the house was teeming with life.

        Something is amiss I am telling you.
        """

        lad """
        Okay, if you say so.

        We better look into it then.
        """


    else:
        """
        Miss Baxter again?

        What is it now?
        """

        lad """
        I am coming !
        """

        """
        I dress up in a hurry and open the door.
        """

        lad """
        Miss Baxter, is everything alright?
        """

        $ play_music('mysterious', 2)

        psychic """
        I don't know.

        I think something weird happening.

        I woke early as usual and tried to get a cup of tea before breakfast.

        But no one is there.
        """

        lad """
        What do you mean?
        """

        psychic """
        That the staff is gone, all of them.

        I tried the kitchen, outside, the whole place even.

        I didn't see anybody.
        """

        lad """
        Couldn't they still be asleep?
        """

        psychic """
        Oh Mister Harring, that's impossible.

        They are supposed to be awake since dawn to get the house ready for the day.

        They couldn't have just slept in.

        I also went to check on Lady Claythorn and she doesn't answer.
        """

        lad """
        Don't worry, I am sure it's not so bad.
        """

        psychic """
        I don't know.

        But I don't want to keep on searching alone.

        Would please accompany me to check on the others?
        """

        lad """
        Well, I am awake now so why not.

        If that can appease you.
        """

        """
        We decide it's better we check again every room together.

        So first we go to ...
        """
    
    if lad_details.saved_variables["day2_believe_psychic"]:

        $ time_left = 135

        call change_time(8,45)

    else:

        $ time_left = 45

        call change_time(10,15)


    call run_menu(lad_details.saved_variables["day3_morning_map_menu"])

    call change_time(11,00)

    $ change_room('tea_room')

    if lad_details.saved_variables["day3_morning_captain_found"]:

        """
        I don't think we'll find someone now.

        So we settled in the tea room to wait for the captain.
        """

        captain """
        That's unbelievable, but it looks like we are the three remaining living souls in this place.

        Did you find anything?
        """

        lad """
        Nothing.

        There is nobody left it seems.

        Except for the bodies.
        """

    else:

        """
        As we were getting discouraged, we settle in the tea room to rest.

        But as we were sitting down, we heard an authoritative voice, shouting from outside the room.
        """

        captain """
        Is there anyone here?
        """

        """
        Without thinking, I answered.
        """

        lad """
        Yes, Ted Harring. I'm here, and Amelia Baxter's with me.
        """

        """
        Amelia tenses. I realize she thinks I shouldn't have answered so fast.

        But it's too late now.

        Soon enough, Captain Sinha enters the room with us.
        """
        
        call lad_day3_morning_meeting_captain


    lad """
    Did you check on Samuel Manning by the way?

    You are the only one who has the key to its room.
    """

    captain """
    No, not yet, I figured he could not have moved.

    But you are right, it's better to go and check ourselves.
    """

    lad """
    I think so too.

    We will follow you.
    """

    """
    Amelia gave me a concerned stare, but doesn't say a thing.

    She follows us anyway.
    """

    $ change_room("bedrooms_hallway")

    $ unlock_map('drunk_room')

    play sound door_knock

    captain """
    Mister Manning, are you there?
    """

    """
    No answers.
    """

    captain """
    OK, I am going in.
    """

    """
    He opens up the door and we follow him in.

    As I enter the room the captain suddenly tries to stop us.
    """

    captain """
    No, stay there.

    Don't enter.
    """

    """
    But it's already too late.
    """

    $ change_room('drunk_room')
    
    $ play_music('scary', fadeout_val = 1)

    """
    What we see inside is the most horrific thing I have ever seen.

    Samuel Manning is in his bed. 

    Covered in blood, his throat cut of in several places.

    He is pure white. His eyes are still opened, fixed in a terrified gaze.

    Miss Baxter let out a scream.
    """

    #TODO add woman scream?

    captain """
    Miss Baxter, please don't stay here.
    """

    """
    She is unable to say anything.

    Her eyes are fixated toward the dead body in the bed.

    Sushil Sinha take her by the arm and drag her out of the room.

    Unable to stay there longer, I follow them outside.
    """

    $ change_room("bedrooms_hallway")

    captain """
    I am sorry you had to see that.

    I should not have let you enter this room.
    """

    psychic surprised """
    Is ... he ... dead?
    """

    captain """
    I am afraid he is.
    """

    lad surprised """
    Are you sure?

    Shouldn't we check his pulse.

    Maybe,... maybe he can still be saved.
    """

    """
    The words are coming slowly out of my mouth.

    I realize I am shaking.
    """

    captain """
    Sorry but it's too late.

    I have seen enough dead bodies to know this.

    The poor guy has been dead for a long time.

    Probably since last night.
    """

    psychic """
    Oh my god.
    """

    """
    She starts to cry.

    I am still shaking from shock.

    So Sushil took us back to the tea room.
    """

    $ stop_music()
    
    jump lad_day3_afternoon

    return