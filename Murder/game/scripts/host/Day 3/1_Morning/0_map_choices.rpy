# Map choices for the Host (Lady Claythorn), Sunday morning
#
# 09:30 -> 12:00, one hundred and fifty minutes on the clock.
#
# She and the Captain go through the house together, to take what they will
# need on the road. Two things can be found:
#   - the garage      : the old tourer, sound but dry (car_checked)
#   - the garden shed : a full tin of petrol, behind the butler's lock (petrol_tin)
# Both are needed for the car at noon. Mr Manning's door can be opened
# here as well (day3_morning_manning_checked), and is opened at noon if not.
#
# Ted Harring and Amelia Baxter are up and walking the house. They are heard
# from the ground floor rooms and avoided (day3_morning_others_heard). Their
# doors, and Miss Marsh's, are never opened: each of those three rooms names
# its door and calls host_day3_morning_bedroom_others, which greys out all
# three on the map.
#
# The Captain carries the master key, so every door in the house opens today,
# including the attic, which was closed to her on Friday.
#
# A room can be picked only once in a chapter, so there are no revisit texts.
# The three saved flags (downstairs, attic, others heard) each span several
# rooms and play their framing on whichever of those rooms comes first.

label host_day3_morning_map_menu:
    python:
        host_day3_morning_map_menu = TimedMenu(
            "host_day3_morning_map_menu",
            [
            # Servants' floor
            map_choice('kitchen', 'host_day3_morning_kitchen', 20),
            map_choice('scullery', 'host_day3_morning_scullery', 10),
            map_choice('garage', 'host_day3_morning_garage', 20),
            map_choice('gun_room', 'host_day3_morning_gun_room', 10),
            # Ground floor
            map_choice('tea_room', 'host_day3_morning_tea_room', 10),
            map_choice('dining_room', 'host_day3_morning_dining_room', 10),
            map_choice('billiard_room', 'host_day3_morning_billiard_room', 10),
            map_choice('entrance_hall', 'host_day3_morning_entrance_hall', 10),
            map_choice('manor_garden', 'host_day3_morning_garden', 20),
            map_choice('servant_stairs', 'host_servant_stairs_default', 10),
            map_choice('portrait_gallery', 'host_day3_morning_portrait_gallery', 10),
            map_choice('library', 'host_day3_morning_library', 10),
            # Bedrooms (her own room is the way out of the map, see below)
            # The three doors she will not knock on, greyed out together
            map_choice('bedroom_lad', 'host_day3_morning_bedroom_lad', 10),
            map_choice('bedroom_nurse', 'host_day3_morning_bedroom_nurse', 10),
            map_choice('bedroom_psychic', 'host_day3_morning_bedroom_psychic', 10),
            map_choice('bedroom_drunk', 'host_day3_morning_bedroom_drunk', 20),
            map_choice('bedroom_captain', 'host_day3_morning_bedroom_captain', 10),
            map_choice('bedroom_doctor', 'host_day3_morning_bedroom_doctor', 10),
            map_choice('bedroom_broken', 'host_day3_morning_bedroom_broken', 10),
            # Attic: empty, and open to the master key
            map_choice('attic_butler_room', 'host_day3_morning_attic_butler_room', 20),
            map_choice('storage', 'host_day3_morning_attic_storage', 10),
            map_choice('males_room', 'host_day3_morning_attic_males_room', 10),
            map_choice('females_room', 'host_day3_morning_attic_females_room', 10),
            # Out of the map: her own room, where she packs what is hers
            # before going down to decide
            TimedMenuChoice(
                'Stop searching and prepare to leave',
                'host_day3_morning_bedroom_host',
                early_exit=True,
                room='bedroom_host',
            ),
        ], is_map = True)

    return


# ------------------------------------
#   The other two are heard, not met
# ------------------------------------
label host_day3_morning_hear_others:

    if not host_details.saved_variables["day3_morning_others_heard"]:

        $ host_details.saved_variables["day3_morning_others_heard"] = True

        """
        Voices, somewhere on the other side of the hall.
        """

        lad """
        Hello? Is anyone there?
        """

        """
        Mr Harring, and Miss Baxter answering him, too low for me to catch the words.

        The Captain's hand closes on my arm, and we stand very still behind the door until the voices go up the stair.
        """

        captain """
        I can hear Ted Harring and Amelia Baxter.

        They are probably trying to understand where everyone is.
        """

        host """
        Maybe, but we should not take any chances.

        Not yet, at least.
        """

        captain """
        You are right, better to avoid them for the time being.
        """

    return


label host_day3_morning_kitchen:

    $ change_room('kitchen')

    """
    The kitchen is empty.

    But the food that was meant to be prepared today is still lying on the counter.
    """

    captain """
    Sunday luncheon, for the whole party.
    """

    host """
    Nobody is going to cook it now.
    """

    """
    We leave it where it lies.
    """

    return


label host_day3_morning_scullery:

    $ change_room('scullery')

    """
    Dirty dishes from Saturday night, and the smell of wet stone.
    """

    if host_details.threads.is_unlocked('found_poison'):

        host """
        Captain, on Friday I noticed a bottle of rat poison standing on that shelf, open.

        I did not think much of it at the time.

        But now, I do not know.
        """

        captain """
        You think it could have been used against Mr Moody?
        """

        host """
        Perhaps.

        I am not sure of anything any more.
        """

        captain """
        If it was, then this weekend was arranged for something terrible.

        That is one more reason to be extremely cautious.
        """

        host """
        Of course.
        """

    """
    There is nothing else for us here.
    """

    return


label host_day3_morning_garage:

    $ change_room('garage')

    """
    The garage holds an assortment of discarded things from the house.
    """

    if host_details.threads.is_unlocked('saw_car'):

        """
        The old tourer is still here, under its dust.
        """

    else:

        """
        At the back, under a sheet, there is an old tourer, thick with dust.
        """

    """
    The Captain lifts the bonnet and puts his head under it.

    I stand back and try to look as though I know what he is doing.
    """

    captain """
    The engine seems to be in order.
    """

    """
    He gets in and tries the starter.
    """

    play sound car_start

    """
    It turns over once and dies.
    """

    captain """
    Dry.

    There is not a drop in the tank.
    """

    $ host_details.observations.unlock('car_checked')

    if host_details.threads.is_unlocked('petrol_tin'):

        captain """
        But the petrol tin from the shed should solve that.
        """

        call host_day3_morning_leave_with_car

    else:

        captain """
        Without petrol it is no use to us.

        But there may be some elsewhere on the estate.
        """

    """
    He closes the bonnet gently, and we leave the car as it was.
    """

    return


label host_day3_morning_gun_room:

    $ change_room('gun_room_empty')

    host """
    It is empty.

    The butler must have taken every weapon he could carry.
    """

    captain """
    No matter.

    I have mine and that is more than enough for us.
    """

    """
    I think I would feel better with a gun of my own.

    But I do not tell him that.
    """

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label host_day3_morning_tea_room:

    $ change_room('tea_room')

    """
    The fire is dead, and there is nothing of interest here.
    """

    call host_day3_morning_hear_others

    return


label host_day3_morning_dining_room:

    $ change_room('dining_room')

    """
    The table is bare, the room empty.
    """

    call host_day3_morning_hear_others

    return


label host_day3_morning_billiard_room:

    $ change_room('billiard_room')

    """
    The billiard room is empty and silent.

    No reason to linger here.
    """

    call host_day3_morning_hear_others

    return


label host_day3_morning_entrance_hall:

    $ change_room('entrance_hall')

    """
    The hall is silent.

    The telephone sits on its table under the stair.

    Captain Sinha picks it up.
    """

    captain """
    The line is dead. It is useless.
    """

    """
    There is nothing else to do here.
    """

    call host_day3_morning_hear_others

    return


label host_day3_morning_garden:

    $ change_room('manor_garden')

    """
    The gravel is empty, and the tracks of the car go off down the drive in the wet.

    At the bottom of the garden stands a small shed.

    We walk down to it.
    """

    $ change_room('toolshed_outside_day')

    play sound door_locked

    """
    I try to open it but it is locked.
    """

    captain """
    Let me try the key the butler gave me yesterday.
    """

    play sound door_open

    $ change_room('toolshed')

    """
    The key turns, and we go in.

    A workbench, a coil of rope, tools that have not been touched in years.

    And in the middle of the floor, a metal petrol tin catches my eye.

    The Captain unscrews the cap and puts his nose to it.
    """

    captain """
    It is petrol, and it is half full.
    """

    if host_details.threads.is_unlocked('car_checked'):

        captain """
        That should help us reach the town with the car from the garage.
        """

        call host_day3_morning_leave_with_car

    else:

        captain """
        If we had a car, there would be more than enough to reach the town.
        """

        host """
        Good, let us keep searching in that case.
        """

    $ host_details.objects.unlock('petrol_tin')

    return


label host_day3_morning_leave_with_car:

    host """
    Great! Now we can finally leave.
    """

    captain """
    Yes, we could actually leave now, but we could also keep searching to make sure we have not forgotten anything.

    It is your decision.
    """

    return


label host_day3_morning_portrait_gallery:

    $ change_room('portrait_gallery')

    """
    A dozen Claythorns in their frames, looking down the gallery at nobody.

    They were here before this weekend, and they will be here when we are gone.

    Not one of them wears my face, and this morning I am glad of it.
    """

    return


label host_day3_morning_library:

    $ change_room('library')

    if host_details.threads.is_unlocked('family_history'):

        """
        The book is still open on the table, at the page I read on Friday.

        Kilbraith.

        I close it. Whoever comes here next need not find it so easily.
        """

    else:

        """
        A heavy book lies open on the table.

        I never did find the time to read it, and it is too late for it to be of any use to me now.
        """

    return


# ------------------------------------
#   BEDROOMS
# ------------------------------------
label host_day3_morning_bedroom_others:

    """
    I raise my hand to knock, but the Captain stops me.
    """

    captain """
    Wait, perhaps we should avoid the risk of meeting anyone else for now.
    """

    host """
    You are right, let us keep it to the two of us. It is safer.
    """

    # Block the other two on the first refusal
    $ all_menus[host_details.saved_variables["day3_morning_map_menu"].id].hide_specific_choice(default_room_text('bedroom_lad'))
    $ all_menus[host_details.saved_variables["day3_morning_map_menu"].id].hide_specific_choice(default_room_text('bedroom_nurse'))
    $ all_menus[host_details.saved_variables["day3_morning_map_menu"].id].hide_specific_choice(default_room_text('bedroom_psychic'))

    return


label host_day3_morning_bedroom_lad:

    $ change_room('bedrooms_hallway')

    host """
    Mr Harring's room.
    """

    call host_day3_morning_bedroom_others

    return


label host_day3_morning_bedroom_nurse:

    $ change_room('bedrooms_hallway')

    host """
    Miss Marsh's room.
    """

    call host_day3_morning_bedroom_others

    return


label host_day3_morning_bedroom_psychic:

    $ change_room('bedrooms_hallway')

    host """
    Miss Baxter's room.
    """

    call host_day3_morning_bedroom_others

    return


label host_day3_morning_bedroom_drunk:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    captain """
    Mr Manning?
    """

    """
    Nothing.
    """

    captain """
    He may still be asleep.

    Stand back a little.
    """

    """
    He turns the key and pushes the door open, and he stops in the doorway.
    """

    call host_day3_morning_manning_body

    return


# --------------------------------------------
#   Mr Manning's body, seen from the doorway.
#   Called from the map, or from host_day3_afternoon at noon if the door
#   was not opened in the morning.
# --------------------------------------------
label host_day3_morning_manning_body:

    $ host_details.saved_variables["day3_morning_manning_checked"] = True

    $ change_room('bedroom_drunk')

    $ play_music('scary', fadeout_val=1)

    """
    Mr Manning lies on his bed with his head turned to the wall.

    The sheet is dark from his chin to his chest, and the dark has run down onto the floor.

    His throat has been cut.
    """

    """
    I do not scream.

    I put my hand over my mouth and I stay where I am, and the Captain takes two steps into the room and no more.
    """

    captain """
    There is no need to go closer.

    He is dead, there is no doubt about it.
    """

    """
    He comes back out and pulls the door to behind him, and for a moment we both stand in the corridor and say nothing.
    """

    $ change_room('bedrooms_hallway')

    captain """
    The door was locked.

    I locked it myself.
    """

    host """
    The butler is the only one with another key.

    But that cannot be. He left yesterday, we watched him go!
    """

    captain """
    Indeed, there is something else at play here.

    I do not understand what has happened, and I do not like it.
    """

    """
    I feel a shiver roll down my spine.
    """

    captain """
    Let us go. There is no reason to stay here any longer.

    And there is nothing we can do for him now.
    """

    $ play_music('PREVIOUS')

    return


label host_day3_morning_bedroom_captain:

    $ change_room('bedroom_captain')

    captain """
    Why do you want to come here?

    Is there something of interest in my room?
    """

    host """
    I do not know.
    """

    """
    I look around and see nothing out of the ordinary.
    """

    captain """
    Well, if you do not know, maybe we should go somewhere else.
    """

    host """
    Yes, of course.
    """

    return


label host_day3_morning_bedroom_doctor:

    $ change_room('bedroom_doctor')

    """
    Doctor Baldwin lies where the Captain and Mr Harring set him down on Saturday.

    The handkerchief is still over his face.

    Nobody has been in here since.
    """

    return


label host_day3_morning_bedroom_broken:

    $ change_room('bedroom_broken')

    """
    Mr Moody, under his sheet, in the cold.

    The first of them.

    On Saturday morning I thought it was the worst thing that could happen to this weekend.
    """

    return


# Early exit of the map: played once, when she stops searching
label host_day3_morning_bedroom_host:

    $ change_room('bedroom_host')

    """
    My own room, where I woke this morning.

    The Captain stays by the door and keeps an eye on the corridor.
    """

    host """
    I shall not be long.
    """

    """
    I open the wardrobe.

    I take my own coat from the back of it, my own shoes, and the handbag with my papers and what little money is mine.
    """

    captain """
    Is that everything?
    """

    host """
    Everything that belongs to me.
    """

    captain """
    Good, then I will fetch my things as well.

    We can meet in the hall afterwards.
    """

    host """
    All right, please do not be long.
    """

    """
    I do not look back at the room.

    Whatever we decide now, I am done with this place.
    """

    return


# ------------------------------------
#   ATTIC
# ------------------------------------
label host_day3_morning_attic_default:

    $ change_room('attic_hallway')

    if not host_details.saved_variables["day3_morning_attic_visited"]:

        $ host_details.saved_variables["day3_morning_attic_visited"] = True

        captain """
        The attic? Are you sure there is something of use up here?
        """

        host """
        I don't know. I assume most of the rooms would be closed.
        """

        captain """
        Maybe, but the key the butler gave me might work here.
        """

        host """
        Let us try, then.
        """

        """
        The Captain inserts the key into the door.

        It opens.
        """

        captain """
        It works, so I assume we can open all of them now.
        """

        host """
        That is good to know.
        """

    return


label host_day3_morning_attic_butler_room:

    call host_day3_morning_attic_default

    play sound door_open

    $ change_room('attic_butler_room')

    """
    The butler's room. It is clear that someone left it in a hurry.

    Against the far wall stands a tall cabinet with glass doors, and the doors are open.

    The shelves behind them are bare.
    """

    captain """
    I would assume the silver was kept in there.

    The candlesticks, the salver...

    It looks like it is gone.
    """

    host """
    I swear, it was never part of the plan to steal anything.
    """

    captain """
    Plan or not, it is clear our friend had few scruples about taking what was not his.
    """

    """
    I stand and look at the empty shelves.

    He gave the orders all weekend, and I took him for an actor.

    But he was a thief as well, it seems.
    """

    return


label host_day3_morning_attic_storage:

    call host_day3_morning_attic_default

    play sound door_open

    $ change_room('attic_storage_room')

    """
    Trunks stacked three deep, furniture under dust sheets, boxes that cannot have been opened in a generation.
    """

    host """
    There could be anything in here.
    """

    captain """
    There could.

    And it would take us the better part of a day to find it.
    """

    host """
    I don't think we have that kind of time.
    """

    captain """
    Nor do I.

    Let us leave it for now.
    """

    """
    I pull the door to behind us, and the dust settles back over the lot of it.
    """

    return


label host_day3_morning_attic_males_room:

    call host_day3_morning_attic_default

    play sound door_open

    $ change_room('attic_males_room')

    """
    Two narrow beds, both stripped to the mattress, and an empty peg behind the door.
    """

    host """
    The footman slept here.

    Thomas, he asked me to call him, which was not his name either.
    """

    captain """
    Whoever he was, he is gone now.

    And he most likely took his belongings with him.

    So there is no need to linger here.
    """

    host """
    You are right.
    """

    return


label host_day3_morning_attic_females_room:

    call host_day3_morning_attic_default

    play sound door_open

    $ change_room('attic_females_room')

    """
    Two beds, a washstand, and the shelf above them swept bare.

    She has left nothing behind at all.
    """

    captain """
    It is empty. I do not think we will find anything here.
    """

    host """
    No.

    Let us look somewhere else.
    """

    return
