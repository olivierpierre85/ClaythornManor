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
            # Attic
            map_choice('attic_butler_room', 'host_day2_evening_attic_butler_room', 20),
            map_choice('storage', 'host_day2_evening_attic_default', 10),
            map_choice('males_room', 'host_day2_evening_attic_default', 10),
            map_choice('females_room', 'host_day2_evening_attic_default', 10),
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

    nurse """
    Who is there?
    """

    host """
    Lady Claythorn.

    I only wished to be sure that you were settled.
    """

    nurse """
    That is very good of you, my lady.

    I am quite settled, thank you. I shall not need anything further tonight.
    """

    """
    She does not open the door, and she has no intention of opening it.

    Her voice comes through two inches of oak perfectly level, which is a great deal more than mine would manage.

    I have spent two days watching that woman miss nothing at all.
    """

    return


label host_day2_evening_bedroom_psychic:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    psychic """
    Come no further, I beg you.

    I have had the most dreadful evening, and I am no fit company for a living soul.
    """

    host """
    Then I shall leave you in peace, Miss Baxter.
    """

    psychic """
    You are kindness itself, my lady.

    Sleep, if you are able. There is a great deal of grief loose in this house tonight, and grief has never cared to be left alone.
    """

    """
    I stand in the corridor a moment after she has stopped speaking.

    That woman has said something to unsettle me every day since Friday, and every time I have decided afterwards that she meant nothing at all by it.

    I am no longer certain that I believe that.
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
# ------------------------------------
label host_day2_evening_attic_default:

    $ change_room('attic_hallway')

    """
    The servants' doors stand open tonight, every one of them, and there is nothing behind any of them but a stripped bed and an empty peg.

    They packed while we were at dinner.

    Every person in this house who was told what we came here to do is ready to leave it.

    I am the only one still asking what it was.
    """

    $ all_menus[host_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[host_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[host_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))

    return


# ------------------------------------
#   THE BUTLER'S ROOM
#
#   The only place she can put the scullery bottle to him before the car goes.
# ------------------------------------
label host_day2_evening_attic_butler_room:

    $ change_room('attic_butler_room')

    """
    His door is open, and his case is shut and standing beside it.

    He has taken the crucifix off the wall and left the nail in the plaster.

    He looks up at me without the smallest sign of surprise, as though he had allowed for this in his arrangements.
    """

    butler """
    The car goes at eleven, my lady.

    Have you decided?
    """

    call run_menu(
        TimedMenu("host_day2_evening_menu_butler_room", [
            TimedMenuChoice(
                'Ask him how the word reached him',
                'host_day2_evening_butler_word',
                0,
            ),
            TimedMenuChoice(
                'Ask him about the bottle in the scullery',
                'host_day2_evening_accuse_butler',
                0,
                condition="host_details.threads.is_unlocked('found_poison') and not host_details.threads.is_unlocked('accused_butler')",
            ),
            TimedMenuChoice(
                'Tell him you have not decided',
                'host_day2_evening_butler_undecided',
                0,
                keep_alive = True,
                early_exit = True,
            ),
        ], image_left = "butler")
    )

    return


# The question the butler left her with at a quarter past nine, and the answer
# he has no intention of giving her.
label host_day2_evening_butler_word:

    host """
    You told me on Friday that the telephone in this house has not worked for years.

    So how does a man in a shut-up manor receive word from London on a Saturday night?
    """

    butler """
    I did not say it came from London.
    """

    host """
    Then where is he?
    """

    """
    He goes on folding a shirt into the case, and he takes his time over the sleeves.
    """

    butler """
    My lady, you have spent two days being told a very little and paid rather well for it.

    That was the arrangement, and it has suited you perfectly until this evening.
    """

    host """
    Two men are dead since that arrangement was made.
    """

    butler """
    Which is precisely why I am not going to add to what you know.

    A woman who knows nothing has nothing to tell anybody, and that is the safest thing you can be tonight.
    """

    """
    He says it without any menace at all, which is what makes it stay with me.

    He is not threatening me. He is telling me the terms.
    """

    return


label host_day2_evening_butler_undecided:

    host """
    I have not.
    """

    butler """
    Then do not be long about it.

    I shall not send anyone up for you, and I shall not sound the horn.

    Eleven o'clock, and the car goes whether you are in it or not.
    """

    """
    He turns back to his case, and I am dismissed in my own house.

    Which is fair enough, since it is not my house and I am not a lady.
    """

    return
