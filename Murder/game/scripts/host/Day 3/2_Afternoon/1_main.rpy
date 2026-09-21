# --------------------------------------------
#   Host
#
#   Sunday - Afternoon
#
#   12:00 -> Ending
#
#   Music: mysterious, danger on the road, scary for the dining room
#
#   Position
#       - House : host, captain, lad, psychic, nurse (out of sight)
#       - Dead  : broken, doctor, drunk (or so everyone believes)
#       - Gone  : butler and the staff, and the butler on his way back
#
#   Notes :
#       - She cannot walk ten miles of that road, so there is no going out
#         on foot. What she found in the morning decides the noon menu.
#       - No car, or no petrol (Case A): the Captain goes for the town alone
#         and leaves her the butler's key. Then she chooses:
#           * poisoned       - she goes in to Mr Harring and Miss Baxter,
#                              sits down to lunch with them, and Miss Marsh
#                              never comes down (2_stay.rpy)
#           * shot_by_butler - she locks herself into the attic, the house
#                              goes quiet under her, and she comes down to
#                              Samuel Manning alive among the dead and the
#                              butler's car on the gravel (3_attic.rpy)
#       - Car and petrol (Case B):
#           * car_ambush     - she will not leave without the others, so the
#                              Captain drives all five of them, and the car
#                              is stopped in the wood (4_together.rpy)
#           * escape         - INTUITION, unlocked by shot_by_butler. The two
#                              of them go now, and she drives.
#         Without the intuition there is no menu in Case B, the same as the
#         Captain's Sunday.
# --------------------------------------------
label host_day3_afternoon:

    call change_time(12, 00, 'Afternoon', 'Sunday', hide_minutes = True, chapter = 'sunday_afternoon')

    $ host_details.add_checkpoint("host_day3_afternoon")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('entrance_hall', irisout)

    $ play_music('mysterious', 2)

    """
    We stand in the hall with the morning behind us and nobody in sight.

    Somewhere on the other side of the house a door closes, and there are voices in the tea room.

    Mr Harring, and Miss Baxter.

    They have stopped searching, then, and they are waiting for something to happen.
    """

    captain """
    Well.

    Here is where we stand.
    """


    if host_details.threads.is_unlocked('car_checked') and host_details.threads.is_unlocked('petrol_tin'):

        captain """
        The car will run, and the tin in the shed will fill it.

        We can be on the road in a quarter of an hour, and in the town within the hour.

        I see nothing to keep us here.
        """

        host """
        Nothing, except the three of them.
        """

        captain """
        Yes.

        We could go in to them. Tell them what we know, and take them with us.

        Or we could go now, and send help from the town.
        """

        """
        He does not say which he would choose.

        I think he has decided it is mine to make.

        I look at the tea room door, and then at the front door.
        """

        if host_details.endings.is_unlocked('shot_by_butler'):

            # Intuition. She has stood in that dining room before, with the
            # butler in the doorway.
            """
            And then, with my hand almost on the tea room door, it comes.

            A room full of the dead and the smell of cold food, and a man in the doorway with his coat open and a revolver pointed at the floor, telling me he is sorry.

            I have never seen it. I know it the way I know my own lines.

            If I go through that door, I shall not come out of this house alive.
            """

            $ time_left = 1
            call run_menu(
                TimedMenu("host_day3_afternoon_menu_car", [
                    TimedMenuChoice("Take the car, and go now{{intuition}}", 'host_day3_afternoon_car', early_exit=True),
                    TimedMenuChoice("We cannot leave them. Go in to the others", 'host_day3_afternoon_together', early_exit=True),
                ], image_left="captain")
            )

        else:

            jump host_day3_afternoon_together

    else:

        if host_details.threads.is_unlocked('car_checked'):

            captain """
            The car is sound, but there is not a drop of petrol in it, and we found none.

            It is a dead weight.
            """

        elif host_details.threads.is_unlocked('petrol_tin'):

            captain """
            We have a full tin of petrol and nothing to put it in.

            I never got as far as the garage.
            """

        else:

            captain """
            We have no motor and no petrol.
            """

        captain """
        So it is the road, on foot, this afternoon.

        Ten miles of it, and the whole of the afternoon to do it in.
        """

        """
        I look at the front door, and I do the sum.

        Ten miles of mud, in these shoes, at my age.

        I have walked out of a great many houses in my life, and never one that was ten miles from anywhere.
        """

        host """
        I cannot walk it, Captain.

        I should not get as far as the gates before you had to carry me.
        """

        captain """
        Then I will not go.
        """

        host """
        You will.

        One of us must reach the town, and it cannot be me.

        Go now, while there is daylight, and send them up here as fast as they will come.
        """

        """
        He does not like it.

        He looks at the tea room door, and at me, and at the tea room door again, and then he takes the key out of his pocket.
        """

        captain """
        The butler's key.

        It opens every door in this house. Lock yourself in somewhere, and open to nobody but me.
        """

        """
        I take it. It is still warm from his pocket.
        """

        captain """
        I will be back before dark, with the police or without them.
        """

        host """
        I know you will.
        """

        """
        Neither of us believes it, and neither of us says so.

        He goes out by the back way, so that nobody at the tea room window sees him cross the gravel, and I stand in the hall and listen to his feet on the path until I cannot hear them any more.
        """

        call change_time(12, 15)

        """
        Then it is very quiet.

        Voices in the tea room, and the stair going up into the dark, and the key in my hand.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("host_day3_afternoon_menu_alone", [
                TimedMenuChoice("Go in to the others", 'host_day3_afternoon_stay', early_exit=True),
                TimedMenuChoice("Hide in the attic, and wait", 'host_day3_afternoon_attic', early_exit=True),
            ])
        )

    return

# --------------------------------------------
#   The car, the two of them. She drives.
# --------------------------------------------
label host_day3_afternoon_car:

    host """
    We go now.

    We send help from the town. It is the best we can do for them.
    """

    captain """
    Agreed.
    """

    """
    He does not argue, and I am grateful for that too.

    We go out the back way, so that nobody at the tea room window sees us cross the gravel.
    """

    call change_time(12, 15)

    $ change_room('manor_garden', dissolve)

    """
    The Captain goes down to the shed for the tin, and I stand at the garage door and watch the house.

    Nobody comes to a window.
    """

    $ change_room('garage', dissolve)

    """
    He fills the tank and sets the choke and swings the handle.
    """

    play sound car_start

    """
    The engine coughs twice, catches on the third pull, and settles into a rough idle.

    The Captain looks at the wheel, and then at the revolver in his pocket, and then at me.
    """

    captain """
    I would rather have my hands free on that road.

    I do not suppose you...
    """

    host """
    I can drive.
    """

    """
    He does not hide his surprise, and I do not blame him.
    """

    host """
    I learnt it for a part, years ago. A modern girl in a modern play.

    The play closed inside a week. The lessons stayed.
    """

    $ host_details.description_hidden.unlock('car')

    captain """
    Then you drive, and I shall watch the road.
    """

    """
    I take the wheel.

    It is heavier than I remember, and the gears fight me on the first change.

    Then we are out of the garage and onto the gravel, and the house is behind us.
    """

    play sound car_driving

    $ change_room('forest_road', dissolve)

    """
    Down the drive, through the gates, and into the trees.

    The Captain sits with his hand in his coat pocket and his eyes on the verges.

    I keep my eyes on the road and my hands on the wheel, and I do not look back once.
    """

    call change_time(12, 45)

    """
    A mile past the gates the trees open out, and there is another motor on the road ahead, coming up towards us.
    """

    $ play_music('danger', 2)

    """
    I know it before I can see who is in it.

    I sat in the back of that car on Friday.
    """

    host """
    It is his.
    """

    captain """
    Do not slow down.

    Keep your head down, and do not look at him.
    """

    """
    The road is barely wide enough for two.

    I put our wheels on the grass and I hold the speed, and for one second there is nothing between us but a foot of air and his face at the window.

    Then he is past.
    """

    """
    I watch him in the mirror until the bend takes him.

    He does not turn round.

    I do not know whether he saw my face. I shall never know.

    Whatever he has come back for, it is not us.
    """

    call wait_screen_transition()

    $ stop_music()

    $ change_room('police_station', dissolve)

    call change_time(13, 30)

    $ play_music('end_credits')

    """
    The town, and the police station, and a sergeant who does not believe a word of it until the Captain gives his name and his rank.

    They go up to the manor that afternoon.

    I am not there to see what they find, and I do not ask.

    I shall have a great deal to explain in the days to come, and I shall explain it.

    I will do it alive.
    """

    jump host_ending_escape


# --------------------------------------------
#   The tea room. Mr Harring and Miss Baxter get the news, with or
#   without the Captain in the room to give it.
# --------------------------------------------
label host_day3_afternoon_tea_room_talk(with_captain):

    $ change_room('tea_room', dissolve)

    """
    Mr Harring is at the window, and Miss Baxter is in the chair by the dead fire.

    They both turn when the door opens, and the boy's face goes through three things at once before it settles on relief.
    """

    if with_captain:

        lad """
        Captain! Lady Claythorn!

        We've been over the whole house. We thought...
        """

    else:

        lad """
        Lady Claythorn!

        We've been over the whole house. We thought...
        """

    psychic """
    We thought we were the only ones left.

    Where is everybody? Where are the servants?
    """

    if with_captain:

        captain """
        Gone.

        The car went in the night, and the staff with it. Every one of them.
        """

        psychic surprised """
        Gone? But why?
        """

        captain """
        That I cannot tell you.
        """

        """
        He does not look at me as he says it, and I am grateful.
        """

        lad """
        And Mr Manning?

        You had his key.
        """

        captain """
        I opened his door this morning.

        He is dead. Killed in his bed, some time in the night.
        """

    else:

        host """
        Gone.

        The car went in the night, and the staff with it. Every one of them.
        """

        psychic surprised """
        Gone? But why?
        """

        host """
        I cannot tell you.
        """

        """
        It is not even a lie. I know who. I have never known why.
        """

        lad """
        And the Captain? Where is he?
        """

        host """
        Gone for help. On foot, to the town, a quarter of an hour ago.
        """

        psychic """
        On foot? Alone?
        """

        host """
        He would not wait.

        He will send help up the moment he reaches the town.
        """

        lad """
        And Mr Manning?

        The Captain had his key.
        """

        host """
        He opened his door this morning.

        Mr Manning is dead. Killed in his bed, some time in the night.
        """

    psychic surprised """
    Oh dear God.
    """

    lad -scared """
    Killed? You mean somebody...
    """

    if with_captain:

        captain """
        His throat was cut.

        Whoever did it had a key to that door.
        """

    else:

        host """
        His throat was cut.

        Whoever did it had a key to that door.
        """

    """
    Miss Baxter sinks back into her chair, and the boy has to find his voice before he can go on.
    """

    lad """
    What about the police, then?

    Lady Claythorn, you spoke to them yesterday. They're coming today, aren't they?
    """

    """
    Here it is.
    """

    if with_captain:

        """
        The Captain does not look at me. He is looking at the fire.
        """

    host """
    They said today, Mr Harring.

    The road was blocked. They will come as soon as it is clear.
    """

    """
    It comes out of my mouth as smoothly as it did on Saturday, and I hate the sound of it.

    The boy nods. Miss Baxter does not.
    """

    psychic """
    Then we wait for them.

    There is nothing else we can do, is there?
    """

    return
