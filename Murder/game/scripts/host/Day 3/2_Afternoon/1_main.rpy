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
#       - She and the Captain keep to what they agreed in the morning:
#         nothing is said to the others, and they do not go in to them. She
#         has lied to those people for three days and they would not take
#         the truth from her now. So it is the two of them, and the only
#         question is how.
#       - Car and petrol found in the morning: no menu. They go now, and
#         she drives (escape).
#       - Otherwise it is the road on foot, and she chooses:
#           * run_over       - she walks out with him, and the butler's car
#                              meets them on the forest road
#           * shot_by_butler - she cannot face the walk, sends him alone and
#                              keeps the butler's key, hides in the attic,
#                              and comes down to Samuel Manning alive among
#                              the dead and the butler's car on the gravel
#                              (2_attic.rpy)
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

    We keep to what we agreed. Nothing is said to the three of them, and we do not go in to them.
    """

    host """
    No.

    I have lied to those people for three days. They would not take the truth from me now, and I would not blame them.
    """

    """
    It is the two of us, then.

    The only question is how.
    """

    if host_details.threads.is_unlocked('car_checked') and host_details.threads.is_unlocked('petrol_tin'):

        captain """
        The car will run, and the tin in the shed will fill it.

        We can be on the road in a quarter of an hour, and in the town within the hour.

        I see nothing to keep us here.
        """

        jump host_day3_afternoon_car

    else:

        if host_details.threads.is_unlocked('car_checked'):

            captain """
            The car is sound, but there is not a drop of petrol in it, and we found none.

            It is a dead weight.
            """

        else:

            captain """
            We have no car to leave in.
            """

        captain """
        So we have to leave on foot.

        It is at least ten miles, but we have the whole of the afternoon to do it.
        """

        """
        I look out of the windows.

        The weather is uncertain. It could rain any minute now.

        The idea of walking in the rain for hours, in these shoes, fills me with dread.

        So does the idea of staying behind, alone in this house.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("host_day3_afternoon_menu_foot", [
                TimedMenuChoice("Walk out with him, now", 'host_day3_afternoon_foot', early_exit=True),
                TimedMenuChoice("Let him go alone, and hide in the attic", 'host_day3_afternoon_attic', early_exit=True),
            ], image_left="captain")
        )

    return

# --------------------------------------------
#   The car, the two of them. She drives.
# --------------------------------------------
label host_day3_afternoon_car:

    host """
    We go now, and alone.

    We can send help from the town.

    It is too risky to trust anyone else in this house.
    """

    captain """
    I agree.

    So let us waste no time.
    """

    """
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
#   On foot, the two of them. The butler's car meets them on the road.
# --------------------------------------------
label host_day3_afternoon_foot:

    host """
    Then we walk.

    Now, before I think better of it.
    """

    captain """
    Now.
    """

    """
    We go out the back way, so that nobody at the tea room window sees us cross the gravel.
    """

    call change_time(12, 15)

    $ change_room('manor_garden', dissolve)

    """
    The gravel, the wet lawn, the drive going off into the trees.

    I have walked out of a great many houses in my life, most of them with my wages unpaid.

    This is the first one I have been afraid to look back at.
    """

    $ change_room('forest_road', dissolve)

    """
    The road is mud from Saturday's rain, and my shoes were made for a drawing room.

    The Captain sets a pace I can keep, and keeps his hand in his coat pocket, and says very little.

    We go a mile, and another.
    """

    call change_time(13, 15)

    call wait_screen_transition()

    """
    Then, from the trees ahead, an engine.
    """

    play sound car_driving fadein 4 loop

    $ play_music('danger', 2)

    """
    A motor, coming up the road from the town.

    The Captain stops, and puts up a hand, and for one moment his face is the face of a man who thinks help has come.
    """

    """
    I know the sound of that engine.

    I sat behind it on Friday, all the way from the station.
    """

    host """
    Captain. It is his.
    """

    """
    He understands me at once.

    His hand comes out of his pocket with the revolver in it, and his other hand takes me by the arm and pulls me towards the ditch.

    The car does not slow.

    It comes off the crown of the road, straight for us, and there is nowhere on that road to go.
    """

    play sound gun

    """
    The Captain fires once.

    It makes no difference at all.
    """

    play sound body_fall

    jump host_ending_run_over
