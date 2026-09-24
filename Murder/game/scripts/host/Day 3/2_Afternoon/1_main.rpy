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
#         she slips away from him in the town (escape).
#       - Otherwise it is the road on foot, and she chooses:
#           * shot_on_road   - she walks out with him, and the butler, walking
#                              back from the town, meets them on the forest road.
#                              The Captain fires and misses, the butler does not
#           * burned         - she cannot face the walk, sends him alone and
#                              keeps the butler's key, hides in the attic,
#                              and comes down to Harring poisoned and the two
#                              women shot. She does not believe Samuel Manning,
#                              shoots him, and is trapped in the dining room
#                              when the house burns (2_attic.rpy)
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

    I have lied to those people all weekend. They would not trust me no matter what I say now.

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
    We reach the garage from outside.

    The Captain goes down to the shed for the tin, and I stand at the garage door and watch the house.

    Nobody comes to a window.
    """

    $ change_room('garage', dissolve)

    """
    He comes back with the tin and fills the tank.

    By then, I am already behind the wheel.
    """

    captain """
    You drive, Lady Claythorn?
    """

    host """
    Better than I shoot, Captain.
    """

    """
    I set the choke, and he goes round to the front and swings the handle.
    """

    play sound car_start

    """
    The engine coughs twice, catches on the third pull, and settles into a rough purr.

    He climbs in beside me, and I take us out of the garage and onto the gravel.
    """

    $ host_details.description_hidden.unlock('car')

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

    Then I headed for the railway station, where I caught the first train south.

    I am not proud of this, but now I can finally relax and try to put this whole affair behind me.

    I will probably never know exactly what happened at Claythorn Manor, but right now, I am at peace with it.
    """

    jump host_ending_escape


# --------------------------------------------
#   On foot, the two of them. The butler meets them on the road.
# --------------------------------------------
label host_day3_afternoon_foot:

    host """
    Then we walk.

    It will not be pleasant, but I prefer that to staying one more second in this place.
    """

    captain """
    Very well, let us leave, then.
    """

    """
    We go out quietly, so that nobody at the tea room window hears us.
    """

    call change_time(12, 15)

    $ change_room('manor_garden', dissolve)

    """
    We walk on the gravel slowly at first, so as not to attract attention.

    Then faster as we leave the driveway.

    We reach the road without so much as a glance back towards the house.
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
    Then, where the road comes out of the trees ahead, a man.
    """

    $ play_music('danger', 2)

    """
    He is on foot, coming up from the town.

    The Captain slows, and puts up a hand, and for one moment his face is the face of a man who thinks help has come.

    But I recognise him at once.
    """

    host """
    Captain. It is him.
    """

    """
    His attitude changes in an instant.

    His hand comes out of his pocket with the revolver in it, and his other hand takes me by the arm and puts me behind him.

    The butler does not stop, and he does not hurry.

    Captain Sinha shouts at him.
    """

    captain """
    Stop right there!

    I have a weapon and will not hesitate to use it.
    """

    """
    He stops.

    Twenty yards, perhaps less. Close enough that I can see the mud on his boots, and that his own hand is in his coat.
    """

    butler """
    My lady. Captain.

    I had hoped you would have the sense to stay in the house.

    It would have been simpler for everyone.
    """

    captain """
    Take your hand out of your coat, slowly, and step off the road.

    I will not ask twice.
    """

    butler """
    No. I do not suppose you will.
    """

    host """
    What are you doing back here?

    You were supposed to leave and never come back.
    """

    """
    He does not answer.

    Instead, his hand comes quickly out of his coat.
    """

    play sound gun

    """
    The Captain fires first.

    The butler steps to one side as the shot goes off.

    The bark jumps off a tree a yard behind him.
    """

    play sound gun

    """
    The Captain fires again.

    He misses again, and this time the butler fires back.
    """

    play sound gun

    play sound body_fall

    """
    The Captain goes down on the road beside me, without a word.

    The butler walks the rest of the way to us, and looks down at the Captain, and then at me.
    """

    play sound gun

    jump host_ending_shot_on_road
