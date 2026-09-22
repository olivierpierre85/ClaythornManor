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

    We could still go and tell them what is happening.
    """

    host """
    No.

    I have lied to those people for three days. They would not trust me no matter what I say now.

    Besides, I still do not trust them.
    """

    captain """
    Fine, it is the two of us, then.
    """

    if host_details.threads.is_unlocked('car_checked') and host_details.threads.is_unlocked('petrol_tin'):

        captain """
        The car will run, and the tin in the shed will fill it.

        We can be in town within the hour if we leave now.

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
            But we have no car to leave in.
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
                TimedMenuChoice("Walk out with him", 'host_day3_afternoon_foot', early_exit=True),
                TimedMenuChoice("Let him go alone", 'host_day3_afternoon_attic', early_exit=True),
            ], image_left="captain")
        )

    return

# --------------------------------------------
#   The car, the two of them. She drives.
# --------------------------------------------
label host_day3_afternoon_car:

    host """
    Let us go now, then.

    We can send help from the town.

    It is too risky to trust anyone else in this house.
    """

    captain """
    Very well.
    """

    """
    We go out the main door as quietly as possible, so that the others do not hear us.
    """

    call change_time(12, 15)

    $ change_room('manor_garden', dissolve)

    """
    The Captain goes down to the shed for the tin, and I stand at the garage door and watch the house.

    Nobody comes to a window.
    """

    $ change_room('garage', dissolve)

    """
    We reach the garage from outside.

    He fills the tank and sets the choke and swings the handle.
    """

    play sound car_start

    """
    The engine coughs twice, catches on the third pull, and settles into a rough purr.

    I get into the car, and we are out of the garage and onto the gravel.
    """

    $ change_room('manor_garden')

    play sound car_driving

    """
    We go down the drive, through the gates, and into the trees.

    Soon, the house is behind us, and I can finally feel relieved.
    """

    call change_time(13, 30)

    $ change_room('train_inside_second', dissolve)

    """
    Captain Sinha wanted to go straight to the police station.

    He promised he would vouch for me and help me make the authorities understand that I was innocent in this whole affair.

    But I did not want to take that chance.

    Besides, he does not know my real name, and it is unlikely our paths will cross again.

    So I thought of an excuse to leave him as soon as we reached the town.

    Then I headed for the railway station, where I hopped on the first train going south.

    I am not proud of this, but now I can finally relax and try to put this whole affair behind me.

    I will probably never know exactly what happened at Claythorn Manor, but right now, I am at peace with it.
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
