# --------------------------------------------
#   Common - Saturday Hunt - The doctor's death, seen from the north field
#
#   The north field party takes its luncheon, hears the two shots and the cry,
#   then comes upon the aftermath in the western grove. Shared by both
#   storylines; narration branches on current_character.text_id:
#       - "captain" : the Captain's point of view
#       - "host"    : Lady Claythorn's point of view
#
#   The death itself, seen from inside the grove, is in 2_accident.rpy.
#
#   Callers:
#       - captain_day2_hunt_silent_luncheon
#       - host_day2_hunt
# --------------------------------------------


# The butler serves the luncheon in the clearing, then excuses himself to look
# in upon the other party.
label common_day2_hunt_luncheon_served:

    """
    The butler lays out a modest spread on a linen cloth, pours tea, then steps back with a brief bow.
    """

    butler """
    If you don't mind, my lady. I should like to look in upon the other party, that they might not want for anything.

    I shall be back soon.
    """

    host """
    Very well. Thank you.
    """

    return


# The hunt is taken up again, and the western grove is heard from.
label common_day2_hunt_shots_heard:

    if current_character.text_id == "host":

        """
        In due course the butler returns, composed as ever, and we resume the hunt.
        """

    pause 1.0

    play sound gun

    pause 0.5

    """
    Two shots, close together, from the direction of the western grove.
    """

    if current_character.text_id == "captain":

        """
        Lady Claythorn lifts her head.
        """

    host """
    It seems the others have seen something.
    """

    """
    Then, a moment later, a different sound.

    A cry. Thin and urgent, carried between the trees.
    """

    $ play_music('danger', 2)

    return


# The aftermath in the grove, and the carrying back of the body.
label common_day2_hunt_doctor_aftermath:

    if current_character.text_id == "captain":

        """
        Without time to think it over, I rush in their direction.
        """

    elif current_character.text_id == "host":

        """
        The Captain is already running before I have made sense of what I have heard.

        I gather my skirts and go after him.
        """

    $ change_room('forest_grove')

    if current_character.text_id == "captain":

        """
        When I reach the others, Doctor Baldwin lies on his back in the fern.

        His shirt has been torn open and pressed dark with blood. His bag is open at his side, a pair of emptied vials loose in the moss.

        Mr Harring kneels beside him, white as paper, a useless hand resting on the ruined shirt.

        Samuel Manning stands a few paces off, his rifle at his feet, his whole frame trembling.

        The footman hovers uncertainly, having clearly not known where to place himself.
        """

    elif current_character.text_id == "host":

        """
        Doctor Baldwin lies on his back in the fern, his shirt torn open and dark with blood.

        Mr Harring kneels beside him, white as paper. Samuel Manning stands a few paces off, trembling, his rifle in the moss at his feet.
        """

    drunk """
    A rabbit. It was a rabbit.

    I never saw him. I swear it on my life, I never saw him.
    """

    if current_character.text_id == "captain":

        """
        Lady Claythorn catches up with us.
        """

    host -scared """
    Good God, what has happened?
    """

    footman """
    Mr Manning fired at something in the undergrowth, my lady.

    The doctor was ahead of him, and the bracken was thick between them.

    The bullet took him in the side.
    """

    if current_character.text_id == "captain":

        """
        The doctor's face has already settled into the stillness of the dead.

        A liver shot, from the placement of the blood. Quick enough, though not quickly enough for comfort.
        """

        """
        Lady Claythorn's hand has gone to her throat. She steps back from the body, and back again, until a sapling halts her retreat.

        The colour is gone from her face.
        """


    host -scared """
    He is... he is truly dead?

    But this cannot be. This was meant to be...
    """

    if current_character.text_id == "captain":

        """
        She does not finish the thought. She catches herself mid-breath.

        She closes her mouth and turns her face away from the doctor.
        """

    elif current_character.text_id == "host":

        """
        I stop myself before the rest of it can leave my mouth.

        A pleasant weekend. That is what it was meant to be.

        I turn my face away from the doctor and remember who I am supposed to be.
        """

    host -scared """
    Forgive me. I am being of no use whatsoever.

    Captain, you must... you must tell us what is to be done.
    """

    captain """
    Of course.

    Mr Harring, take the footman. Cut me two straight saplings, the length of a man and as thick as your wrist.

    The doctor's bag will hold a blade.
    """

    captain """
    Mr Manning. Sit down. Head between your knees, and breathe slowly.

    You will be of no use to anyone fainting in the bracken.
    """

    if current_character.text_id == "captain":

        """
        The lad nods and is gone before I have finished speaking.

        Samuel Manning sinks where he stands, his rifle forgotten in the moss.

        The footman lingers a heartbeat, then follows the lad into the trees.
        """

        """
        When they return, I take my own jacket and the footman's, and lay them open upon the ground.

        Sleeves threaded onto the saplings. Buttons fastened beneath. The cloth drawn taut between.

        A makeshift stretcher, rough but serviceable.
        """

        """
        My hands work without instruction.

        The knot at the shoulder. The half-hitch at the foot. The way one tests the give of the cloth before trusting any weight to it.

        I have done this before.

        I may never have seen battle, but overseeing the carrying of the dead and the wounded was often amongst my duties.
        """

    elif current_character.text_id == "host":

        """
        They do as he tells them, every one of them, without a word of complaint.

        He and the footman give up their jackets, and the sleeves are threaded onto two cut saplings to make a stretcher of sorts.

        His hands know the work without being told, and I find myself wondering how many times he has done it before.

        Nobody looks to me at all, and I have never been so grateful for anything in my life.
        """

    captain """
    Mr Harring at the head, the footman at the feet.

    Walk in step. Short paces.

    If you must rest, set him down evenly.

    Mr Manning, follow behind with his bag.
    """

    """
    We begin the slow march back through the ferns.
    """

    return
