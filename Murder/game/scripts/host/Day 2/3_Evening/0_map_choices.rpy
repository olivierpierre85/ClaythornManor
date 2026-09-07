# Map choices for the Host (Lady Claythorn), Saturday night
#
# 21:30 -> 23:00, ninety minutes on the clock.
#
# The butler's car stands in the garden with its lamps lit, and it leaves at
# eleven whether she is in it or not. Two destinations decide how her night
# ends:
#   - the garden        : she takes the seat she was offered
#   - the billiard room : she tells Captain Sinha what she really is
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
                90,
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


label host_day2_evening_billiard_room_empty:

    $ change_room('billiard_room')

    """
    The decanters have been set out on the side table, the lamps are lit, but there is not a soul in the room.

    It is not really surprising, though.

    Two deaths in the same weekend are enough to scare just about anybody.

    I do not think anyone will show up here tonight.

    I leave the room.
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


# ------------------------------------
#   ATTIC
#
#   The staff are packing. The butler is already down at the car, the footman
#   will not be drawn, and only the girl says what she is afraid of.
# ------------------------------------
label host_day2_evening_attic_butler_room:

    $ change_room('attic_butler_room')

    """
    His door stands open and the room has already been stripped.

    The crucifix has come off the wall and the nail has been left in the plaster.

    No case, no coat, nothing of his at all.

    He will be down at the car with the lamps lit, loading it himself rather than trust any of it to the footman.

    There is nothing left up here that he has not decided to leave behind.
    """

    return


label host_day2_evening_attic_males_room:

    $ change_room('attic_males_room')

    """
    The footman has his bag open on the bed and he is filling it as fast as his hands will go.

    He does not stop when I come in, and he barely looks up.
    """

    host """
    You are in a great hurry.
    """

    footman """
    Car goes at eleven, my lady.
    """

    """
    He folds nothing.

    He pushes it all in and presses it down with the flat of his hand.
    """

    host """
    Are you quite all right?
    """

    footman """
    I was engaged for a weekend and I have done the weekend.

    That is all there is to it.
    """

    """
    That is not what I asked him, and he knows it.
    """

    host """
    If something has happened that I ought to know about, you may tell me.
    """

    footman """
    Nothing has happened, my lady.

    And if it had, it would be no business of mine.
    """

    """
    He pulls the strap through the buckle and drags it tight.

    He has not once looked at me straight, and he will not while I am standing here.

    Whatever he thinks of this weekend, he means to carry it down the stairs with him and out through the gate.
    """

    return


label host_day2_evening_attic_females_room:

    $ change_room('attic_females_room')

    """
    The girl has her things laid out on the bed in a neat square, and she is folding each piece as though somebody will inspect it.

    Her hands are not steady.
    """

    maid """
    Ma'am.

    I am nearly ready, I promise.
    """

    host """
    Nobody is timing you, Elsie.
    """

    """
    She puts a folded apron into the bag, takes it out again, and puts it back in the very same place.
    """

    maid """
    May I say something, ma'am?

    It will sound foolish.
    """

    host """
    You may.
    """

    maid """
    I feel like a thief.

    Creeping down the back stairs in the dark with my bag, and the gentlemen upstairs not knowing a thing about it.

    And I have not stolen anything.

    Not so much as a spoon.

    You may look in my bag if you care to, ma'am, I would rather you did.
    """

    host """
    I shall do nothing of the kind.
    """

    """
    She stops folding, and now she does look at me.
    """

    maid """
    Then tell me something else instead.

    Have we done wrong, ma'am?

    Two gentlemen are dead in this house and we are going out of it at eleven at night, and I cannot make those two things sit quietly together.
    """

    """
    She has asked me the question I have been carrying about the house all evening, and she has asked it far better than I could.
    """

    host """
    Listen to me.

    One of them was shot in the woods by a man who could not hold a gun properly, and the other went in his sleep.

    Both of them accidents, and neither of them anything to do with you.

    The rest of it was a piece of theatre got up by people with more money than sense.

    A joke, of a sort, that has ended a great deal worse than any of them intended.
    """

    maid """
    Then why are we not going in the morning, in the daylight, like honest people?
    """

    host """
    Because honest people spend a fortnight answering a policeman's questions in a village hall.

    You cooked and you carried, and that is the whole of what you did.

    But you would still be a young woman in a house where two gentlemen died, and they would put the same question to you forty times over to see whether you changed your answer.

    Far better to be well away before anybody thinks to ask it.
    """

    maid """
    Yes, ma'am.

    Thank you.

    I did not like to ask Mr Barrow.
    """

    """
    She goes back to her folding, and her hands are steadier for it.

    It is the only useful thing I have done all day.

    I have told a frightened girl that leaving in the dark is the sensible course, and I told it well, because telling things well is the one trade I have.

    I only wish I believed a word of it.
    """

    return


label host_day2_evening_attic_storage:

    $ change_room('attic_hallway')

    """
    The servants' doors stand open tonight, every one of them.

    The storage room does not.
    """

    play sound door_locked

    """
    I try the handle twice, which is twice more than there is any sense in.

    Locked on Friday, and locked still.

    It is the one door in this house that has never been open to me, and he will have the key in his pocket, down on the gravel, packing the car.
    """

    return
