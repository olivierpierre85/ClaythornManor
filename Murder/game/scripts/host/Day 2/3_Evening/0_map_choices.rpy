# Map choices for the Host (Lady Claythorn), Saturday night
#
# 21:30 -> 23:00, ninety minutes on the clock.
#
# The butler's car stands in the garden with its lamps lit, and it leaves at
# eleven whether she is in it or not. Two destinations decide how her night
# ends:
#   - the garden        : she takes the seat she was offered
#   - the billiard room : she may tell Captain Sinha what she really is,
#                         or keep the mask on and sleep alone
#
# The Captain only sits up if she has not already humiliated him in the tea
# room, so 'bested_captain' shuts that door for good and leaves her alone.
#
# The butler cannot be reached tonight. He is out on the gravel loading the car
# from a quarter past nine, so the attic holds nothing but the staff packing.

label host_day2_evening_map_menu:
    python:
        host_day2_evening_map_menu = TimedMenu(
            "host_day2_evening_map_menu",
            [
            # Servants' floor
            map_choice('kitchen', 'host_day2_evening_kitchen', 10),
            map_choice('scullery', 'host_day2_evening_scullery', 10),
            map_choice('garage', 'host_day2_evening_garage', 10),
            map_choice('gun_room', 'host_day2_evening_gun_room', 10),
            # Ground floor
            map_choice('tea_room', 'host_day2_evening_tea_room', 10),
            map_choice('dining_room', 'host_day2_evening_dining_room', 10),
            map_choice('entrance_hall', 'host_day2_evening_entrance_hall', 10),
            map_choice('servant_stairs', 'host_servant_stairs_default', 10),
            map_choice('portrait_gallery', 'host_day2_evening_portrait_gallery', 20),
            map_choice('library', 'host_day2_evening_library', 20),
            # Bedrooms (her own room is the retire exit, so it is not listed here)
            map_choice('bedroom_lad', 'host_day2_evening_bedroom_lad', 10),
            map_choice('bedroom_nurse', 'host_day2_evening_bedroom_nurse', 10),
            map_choice('bedroom_psychic', 'host_day2_evening_bedroom_psychic', 10),
            map_choice('bedroom_drunk', 'host_day2_evening_bedroom_drunk', 20),
            map_choice('bedroom_captain', 'host_day2_evening_bedroom_captain', 10),
            map_choice('bedroom_doctor', 'host_day2_evening_bedroom_doctor', 10),
            map_choice('bedroom_broken', 'host_day2_evening_bedroom_broken', 10),
            # Attic: the staff are packing, and the butler is already outside
            map_choice('attic_butler_room', 'host_day2_evening_attic_butler_room', 10),
            map_choice('storage', 'host_day2_evening_attic_storage', 10),
            map_choice('males_room', 'host_day2_evening_attic_males_room', 10),
            map_choice('females_room', 'host_day2_evening_attic_females_room', 20),
            # The Captain sits up alone, unless she made an enemy of him this afternoon
            TimedMenuChoice(
                'Sit up with Captain Sinha in the billiard room',
                'host_day2_evening_billiard_room',
                20,
                room='billiard_room',
                condition="not host_details.threads.is_unlocked('bested_captain')",
            ),
            TimedMenuChoice(
                'Look into the billiard room',
                'host_day2_evening_billiard_room_empty',
                10,
                room='billiard_room',
                condition="host_details.threads.is_unlocked('bested_captain')",
            ),
            # The two ways out of the night
            TimedMenuChoice(
                'Go to the car and leave with the staff',
                'host_day2_evening_leave_with_butler',
                early_exit=True,
                room='manor_garden',
            ),
            TimedMenuChoice(
                'Lock your door and try to sleep',
                'generic_cancel',
                early_exit=True,
                room='bedroom_host',
            ),
        ], is_map = True)

    return


label host_day2_evening_kitchen:

    $ change_room('kitchen')

    """
    The kitchen is empty.

    Nobody will bother preparing anything for tomorrow.

    The guests will have to fend for themselves if they want something to eat in the morning.
    """

    return


label host_day2_evening_scullery:

    $ change_room('scullery')

    """
    The scullery is filled with dirty dishes.

    I assume nobody will bother cleaning them now.
    """

    if host_details.threads.is_unlocked('found_poison'):

        """
        I also notice that the bottle of rat poison that was here yesterday has gone.

        Strange.
        """

    return


label host_day2_evening_garage:

    call host_garage_default

    return


label host_day2_evening_gun_room:

    $ change_room('gun_room_empty')

    """
    The gun room is empty.

    Not a single weapon in sight.

    It was probably one of the few things we brought specifically for this weekend.

    I assume they are already packed in the car with the luggage.
    """

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label host_day2_evening_tea_room:

    $ change_room('tea_room')

    """
    The room is empty.

    The fire has gone out and nobody has laid it again.
    """

    return


label host_day2_evening_dining_room:

    $ change_room('dining_room')

    """
    The plates have been removed from the table.

    It gives at least the pretence that things are carrying on as normal.
    """

    return


label host_day2_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The entrance hall is empty.

    But I know that outside there is a car waiting for me.

    If I want, I could go right now and never look back.
    """

    return


label host_day2_evening_portrait_gallery:

    $ change_room('portrait_gallery')

    if host_details.threads.is_unlocked('no_portrait'):

        """
        The Claythorns are still on their walls, and not one of them wears my face.

        Nothing about that has changed.
        """

    else:

        """
        A dozen Claythorns in gilt frames, looking down the gallery.

        Many generations of people who have lived and died at Claythorn Manor.

        Whoever they were, it is no longer any concern of mine.
        """

    return


label host_day2_evening_library:

    $ change_room('library')

    if host_details.threads.is_unlocked('family_history'):

        """
        I have learned all I needed from the book on the table.

        There is nothing more for me here.
        """

    else:

        """
        A better library than I expected.

        A heavy book lies open on the table.

        But there is no point in reading it now.
        """

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label host_day2_evening_bedroom_lad:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    Nobody answers, but something heavy is being dragged across the boards on the other side of the door.
    """

    play sound moving_furniture

    host """
    It is only me, Mr Harring.
    """

    """
    The dragging stops.

    It does not begin again, and he does not come to the door.

    I have no argument to make against a young man who has decided to trust nobody in this house tonight.

    He is quite right, and I am one of the people he is right about.
    """

    return


label host_day2_evening_bedroom_nurse:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    No answer.

    I suppose she is either asleep or too frightened to answer.
    """

    return


label host_day2_evening_bedroom_psychic:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    """
    I hear movement but nobody answers.

    She is probably too afraid to open the door, and I do not have the strength to insist.
    """

    return


label host_day2_evening_bedroom_drunk:

    $ change_room('bedrooms_hallway')

    """
    I stand in front of Mr Manning's door and knock.
    """

    play sound door_knock

    """
    No answer.

    I guess he is already asleep.

    There is no reason for me to insist.
    """

    return


label host_day2_evening_bedroom_captain:

    $ change_room('bedrooms_hallway')

    play sound door_knock


    if host_details.threads.is_unlocked('bested_captain'):

        """
        No answer.

        There is a line of lamplight beneath the door, so I know he is awake.

        But he is probably too ashamed of what he did earlier to face anybody tonight.

        I leave him be.
        """

    else:

        """
        No answer, and no light beneath the door.

        He is probably not in his room tonight.
        """

    return


label host_day2_evening_bedroom_doctor:

    $ change_room('bedroom_doctor')

    """
    The door stands open and the lamp has been left burning at the bedside.

    Doctor Baldwin lies where the Captain and Mr Harring set him down, still in the coat he was shot in.

    Somebody has laid a handkerchief over his face.

    I cannot stay here long, so I leave quickly.
    """


    return


label host_day2_evening_bedroom_broken:

    $ change_room('bedroom_broken')

    """
    Mr Moody has been left as he was found this morning, with the sheet drawn up over him.

    The room is very cold.

    I do not have the strength to remain here for long, so I leave.
    """

    return


label host_day2_evening_attic_butler_room:

    $ change_room('attic_hallway')

    play sound door_knock

    """
    Nothing answers me, and there is no sound at all behind the door.

    He must be at the car already, loading it himself rather than trust any of it to the footman.

    I try the handle out of habit.

    Locked, of course.

    There is nothing up here he has not decided to leave behind.
    """

    return


label host_day2_evening_attic_males_room:

    $ change_room('attic_hallway')

    play sound door_knock

    """
    Nobody answers.

    He has probably gone down already.
    """

    return


label host_day2_evening_attic_females_room:

    $ change_room('attic_hallway')

    play sound door_knock

    """
    No answer, and no sound behind the door.

    But I notice a ray of light coming from beneath the door.
    """

    host """
    It is only Lady Claythorn.

    You may open the door, it is quite safe.
    """

    maid """
    Ma'am.

    I am nearly ready, I promise.
    """

    """
    As she says this, she opens the door and lets me in.
    """

    $ change_room('attic_females_room')

    host """
    No need to apologise.

    I just wanted to see how you were holding up.

    We were not expecting this weekend to end so terribly.
    """

    maid """
    Well, to be honest, I rather feel like a thief.

    Leaving like this in the dark, and the guests not knowing a thing about it.

    I have been wondering, have we done something wrong, ma'am?
    """

    host """
    Listen to me.

    One of them was shot in the woods by a man who could not hold a gun properly, and the other went in his sleep.

    Both of them accidents.

    Our part in this had nothing to do with either of them.

    It was a piece of theatre, a joke of a sort, that has gone wrong.
    """

    maid """
    Then if we have done nothing wrong, why are we not telling this to the guests?
    """

    host """
    Because whatever we were doing here will attract suspicion.

    We ought to have called the police this morning.

    We might be blamed for that, even if we have done nothing wrong.
    """

    maid """
    Maybe.

    I should finish my packing, then.
    """

    """
    I do not think she believes me entirely, but she does not want to press the matter further.

    I cannot blame her.
    """

    host """
    Of course. I shall leave you to it.
    """

    return


label host_day2_evening_attic_storage:

    $ change_room('attic_hallway')

    play sound door_knock

    """
    No answer, as I expected.
    """

    """
    I try the handle.
    """

    play sound door_locked

    """
    Locked.
    """

    return
