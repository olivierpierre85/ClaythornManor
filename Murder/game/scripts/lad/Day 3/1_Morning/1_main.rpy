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

    $ change_room('bedroom_lad', irisout)

    if lad_details.important_choices.is_unlocked('trust_psychic'):
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

    if lad_details.important_choices.is_unlocked('day2_drunk') :
        """
        My head is throbbing.

        I wish I could've slept longer.
        """    

    psychic """
    Mister Harring, are you there?
    """

    if lad_details.important_choices.is_unlocked('trust_psychic'):

        """
        Miss Baxter?

        Right, we agreed to wake each other up.

        I just didn't expect it to be this early.
        """

        call common_day3_morning_lad_psychic_journey

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

    if lad_details.important_choices.is_unlocked('trust_psychic'):
        $ time_left = 135
        call change_time(8, 45)
    else:
        $ time_left = 45
        call change_time(10, 15)


    call run_menu(lad_details.saved_variables["day3_morning_map_menu"])

    call change_time(11,00)

    $ change_room('tea_room', dissolve)

    if lad_details.saved_variables["day3_morning_captain_found"]:

        """
        I doubt we'll find anyone now.

        So we settled in the tea room to wait for Captain Sinha.
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

        call common_day3_morning_lad_psychic_tea_room_1
        
    call common_day3_morning_lad_psychic_tea_room_2

    call common_day3_morning_lad_psychic_captain_death_manning

    call common_day3_morning_lad_psychic_captain_marsh_empty

    call common_day3_morning_lad_psychic_captain_deaths_end

    pause 1.0

    $ stop_music()

    jump lad_day3_afternoon

    return
