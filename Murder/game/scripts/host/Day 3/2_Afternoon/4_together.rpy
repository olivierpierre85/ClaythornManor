# --------------------------------------------
#   Host - Sunday afternoon, the car, all of them
#
#   She has the car and the petrol and she will not leave without the
#   others. She and the Captain go in to Ted Harring and Amelia Baxter,
#   the Captain brings the car round, and Miss Marsh comes out of the
#   front door as they are getting in.
#
#   Lady Claythorn does not drive a motor car in front of three guests,
#   so the Captain drives. The engine dies a mile into the wood, he gets
#   out to look at it, and the shooting starts behind her.
#
#   Same road, same stalled engine, as captain_day3_afternoon_car_together.
# --------------------------------------------
label host_day3_afternoon_together:

    if host_details.endings.is_unlocked('shot_by_butler'):

        # Intuition, and she goes in anyway
        """
        Whatever that was, it has passed.

        Nerves, and two bad nights. I have gone on with worse.
        """

    """
    I have lied to those two for three days, and I have left them to themselves for three nights.

    I am not driving out of this house without so much as a word to them.
    """

    host """
    We go in to them.

    All of us, in the car.
    """

    captain """
    Very well.

    But we keep to what we agreed. We say nothing of what you told me.
    """

    host """
    Nothing.
    """

    call change_time(12, 15)

    call host_day3_afternoon_tea_room_talk(True)

    captain """
    We are not waiting.

    There is a motor in the garage, and petrol for it, and it will take the four of us.

    Get your coats. I will bring it round to the front.
    """

    lad """
    You can drive?
    """

    captain """
    Well enough.
    """

    """
    He does not look at me, and I do not look at him.

    Lady Claythorn does not drive a motor car, any more than she goes below stairs.

    I have kept to that for three days, and I keep to it now, with two people watching.
    """

    call change_time(12, 45)

    $ change_room('manor_exterior', dissolve)

    """
    A quarter of an hour on the front steps, and the car comes round the side of the house, coughing, with the Captain hunched over the wheel.

    Mr Harring hands Miss Baxter up into the back, and I am half way in after her when the front door opens behind us.
    """

    nurse """
    You were going to leave without me.
    """

    """
    Miss Marsh, in the same dress as Saturday, and looking as though she has slept in it.
    """

    if host_details.saved_variables["day3_morning_nurse_checked"]:

        """
        The Captain and I opened her door this morning, and her bed had not been slept in.

        I say nothing. He says nothing.
        """

    captain """
    We did not know you were alive, Miss Marsh.

    Get in.
    """

    """
    She climbs in beside Miss Baxter without another word, and the boy takes the seat by the Captain.

    So I am in the back, between two women I do not trust, with my hands in my lap.

    Nobody is at any window to see us go.
    """

    play sound car_driving

    $ change_room('forest_road', dissolve)

    """
    Down the drive, through the gates, and into the trees.

    The Captain drives with one hand and keeps the other near his pocket, and his eyes are on the verges.

    Nobody speaks. For a mile, it is almost easy.
    """

    call change_time(13, 00)

    $ play_music('danger', 2)

    """
    Then the engine coughs.

    It catches, and falters, and dies, and we roll to a stop in the middle of the empty road.
    """

    stop sound

    captain """
    Stay in the car.

    All of you.
    """

    """
    He gets out and lifts the bonnet, and the wood on either side of us is very still.

    Behind me, a door opens.
    """

    play sound door_open

    captain """
    Stay inside!

    We do not know if it is safe here.
    """

    """
    Footsteps on the road, going towards him, unhurried.

    The Captain straightens up from the engine with his hand going to his pocket.
    """

    play sound gun

    """
    He goes down without a sound.

    I have my hand on the door, and the footsteps turn, and come back towards the car.
    """

    play sound gun

    jump host_ending_car_ambush
