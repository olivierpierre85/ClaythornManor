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
            map_choice('portrait_gallery', 'host_portrait_gallery_default', 20),
            map_choice('library', 'host_library_default', 20),
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
                'Take your seat in the car and leave with them',
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


# ------------------------------------
#   SERVANTS' FLOOR
#
#   Everyone below stairs was told before she was, which is the whole of what
#   she learns down here.
# ------------------------------------
label host_day2_evening_kitchen:

    $ change_room('kitchen')

    """
    The range is still warm, and not one plate has been washed.

    The girl is kneeling on the flags with a carpet bag open in front of her, folding her things into it.

    She is on her feet the moment she sees me, and she cannot look at me at all.
    """

    maid """
    M'lady.

    We were told to be ready by eleven.

    I thought you knew, ma'am, or I would not have started.
    """

    host """
    I do know.

    Finish your packing.
    """

    """
    She is nineteen at the most, and she has had her orders from the same man who gave me mine.

    I go back up the stair before she can see what my face is doing.
    """

    return


label host_day2_evening_scullery:

    $ change_room('scullery')

    if host_details.threads.is_unlocked('found_poison'):

        """
        The shelf above the sink is bare.

        The bottle has gone, and somebody has wiped the ring it left in the dust.

        A man who takes a bottle away has merely tidied up.

        A man who wipes the shelf afterwards knew there was a mark worth wiping.
        """

    else:

        """
        The scullery is cold and smells of soda and wet stone.

        There is a clean ring in the dust on the shelf above the sink, where something round stood for a long while and was taken away this evening.

        I have no notion what it was, and I find I would rather not have one.
        """

    return


label host_day2_evening_garage:

    $ change_room('garage')

    """
    The old tourer sits under its sheet, exactly as it has done since Friday.

    The other bay is empty, and two wet tracks run out of it and round towards the garden.

    So he brought the car round before he ever came up to ask me.

    He was very sure of my answer.
    """

    return


label host_day2_evening_gun_room:

    $ change_room('gun_room')

    """
    The sporting guns are still behind their glass.

    The handgun that lay out on the table on Friday night is not.

    There is a clean patch on the baize where it was, and nothing else in the room has been touched.

    On Friday I stood here and thought of a play I had once seen, and could not think why.

    I know why now.
    """

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label host_day2_evening_tea_room:

    $ change_room('tea_room')

    if host_details.threads.is_unlocked('bested_captain'):

        """
        The chairs are still drawn into the half circle the Captain made of them when he put his question to me.

        Nobody has thought to set the room straight, because there is nobody left in this house who thinks of such things.

        I stand where I stood and I say my answer over again in my head, and it is still a very good answer.

        It has cost me the only man under this roof who might have stood beside me tonight, but it was a good answer.
        """

    else:

        """
        The fire has gone out and nobody has laid it again.

        A room left cold at this hour looks like a room in a house that has been shut up.

        Which, by tomorrow, is what it will be.
        """

    return


label host_day2_evening_dining_room:

    $ change_room('dining_room')

    """
    The cloth has been taken off and the chairs pushed in, and the table is bare wood again.

    Eight places were laid here on Friday.

    I count the empty ones out on the wood, the way one counts a cast at the end of a run, and I stop when I reach three.
    """

    return


label host_day2_evening_entrance_hall:

    $ change_room('entrance_hall')

    """
    The front door has been left on the latch, and there is cold air coming across the flags from it.

    Two cases stand against the wall beside it, and neither of them is mine.

    Beyond the door a pair of lamps burn out on the gravel, and the engine has been left running so that nobody will have to start it again in the cold.

    They are only waiting for the hour now.
    """

    """
    The telephone sits on its table at the back of the hall, beneath the stair, where he told me on Friday that it had been dead for years.

    I lift the receiver and hold it against my ear for a long moment.
    """

    """
    Nothing at all.

    Not a click, not a hum, not so much as the sound of a wire with weather on it.

    So no word came into this house that way tonight, and somebody carried it up the drive instead.

    I put the receiver back very quietly, as though the thing could hear me.
    """

    return


label host_day2_evening_billiard_room_empty:

    $ change_room('billiard_room')

    """
    The decanters have been set out on the side table, the lamps are lit, and there is not a soul in the room.

    That surprises me more than it ought to.

    A man who does not trust a house does not go to bed in it, and Captain Sinha trusts nothing here.

    Then I remember the tea room, and how very well I did in it, and I understand that he would sooner sit alone upstairs than pass an evening in a room with me.

    I turn the lamps down and leave the drink where it stands.
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
    The key stands in the outside of Mr Manning's door, where the Captain had it put.

    His supper tray is on the floor beside it.

    The cover is still on the plate, and the plate has not been touched.
    """

    if host_details.threads.is_unlocked('accused_butler'):

        """
        Nobody at that table has come to any harm.

        He chose those words with a great deal of care, and the man behind this door was not at that table.

        I crouch down and lift the cover, and there is nothing whatever to see, because there never is.
        """

    elif host_details.threads.is_unlocked('found_poison'):

        """
        A man who has been drinking since Friday has not touched his dinner.

        There is an open bottle of rat poison somewhere in this house, or there was this morning, and I cannot make those two thoughts sit apart from one another.
        """

    play sound snoring

    """
    Then a sound from inside, coarse and regular.

    He is asleep, and he is breathing, and there is nothing further I can do for him tonight.
    """

    return


label host_day2_evening_bedroom_captain:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    if host_details.threads.is_unlocked('bested_captain'):

        """
        There is a line of lamplight beneath Captain Sinha's door, so he is awake and he has heard me.

        He does not answer, and he is not going to.

        I made that man apologise to me in front of the whole house this afternoon, and I was rather pleased with myself at the time.
        """

    else:

        """
        No answer, and no light beneath the door.

        He is not in his room at all.

        A man who means to sleep tonight would be in it, which tells me he does not mean to sleep.
        """

    return


label host_day2_evening_bedroom_doctor:

    $ change_room('bedroom_doctor')

    """
    The door stands open and the lamp has been left burning at the bedside.

    Doctor Baldwin lies where the Captain and Mr Harring set him down, still in the coat he was shot in.

    Somebody has laid a handkerchief over his face.
    """

    call host_day2_evening_dead_man_thought

    return


label host_day2_evening_bedroom_broken:

    $ change_room('bedroom_broken')

    """
    Mr Moody has been left as he was found this morning, with the sheet drawn up over him.

    The room is very cold. Somebody has opened the window a hand's breadth, because somebody believed that was the proper thing to do.
    """

    call host_day2_evening_dead_man_thought

    return


# Both dead men get the same thought from her, so it lives in one place.
label host_day2_evening_dead_man_thought:

    """
    I ought to say something over him.

    The lady of the house would, and there is nobody here to judge whether I do it well or badly.

    I find that I cannot, and that frightens me rather more than the room does.
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
