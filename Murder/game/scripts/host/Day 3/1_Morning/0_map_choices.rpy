# Map choices for the Host (Lady Claythorn), Sunday morning
#
# 09:30 -> 12:00, one hundred and fifty minutes on the clock.
#
# She and the Captain go through the house together, to take what they will
# need on the road. Three things can be found:
#   - the garage      : the old tourer, sound but dry (seen_car)
#   - the garden shed : a full tin of petrol, behind the butler's lock (petrol_tin)
#   - the kitchen     : what food is left, packed for the road (provisions)
# All three are needed for the car at noon. Mr Manning's door can be opened
# here as well (day3_morning_manning_checked), and is opened at noon if not.
#
# Ted Harring and Amelia Baxter are up and walking the house. They are heard
# from the ground floor rooms and avoided (day3_morning_others_heard).
#
# The Captain carries the master key, so every door in the house opens today,
# including the attic, which was closed to her on Friday.

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
            # Bedrooms (her own room holds nothing she wants, so it is not listed)
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
            # Out of the map: back to the hall to decide
            TimedMenuChoice(
                'Stop searching and decide what to do',
                'generic_cancel',
                early_exit=True,
                room='entrance_hall',
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
        They are looking for people.
        """

        host """
        Or for a way out.
        """

        captain """
        Either way, not for us.

        Not yet.
        """

    else:

        """
        Their voices again, further off this time.

        We keep to the far side of the house from them.
        """

    return


# ------------------------------------
#   SERVANTS' FLOOR
# ------------------------------------
label host_day3_morning_first_downstairs:

    if not host_details.saved_variables["day3_morning_downstairs_visited"]:

        $ host_details.saved_variables["day3_morning_downstairs_visited"] = True

        $ change_room('basement_stairs')

        """
        The narrow stair down.

        On Friday I stood here and told myself a lady does not go below.

        This morning there is nobody left below to see her do it.

        The Captain goes first.
        """

    return


label host_day3_morning_kitchen:

    call host_day3_morning_first_downstairs

    $ change_room('kitchen')

    if host_details.threads.is_unlocked('provisions'):

        """
        The basket is where we left it, at the foot of the stair.

        There is nothing more to take from here.
        """

        return

    """
    The range is cold, and the pans from Saturday night are still on it.

    The girl was a fine cook, for an actress. It is a pity nobody will ever know it.

    I open the larder.

    Half a loaf, the end of a ham, a piece of cheese in its cloth, and a few apples.

    Not a feast. Enough for a road.
    """

    captain """
    Take all of it.

    Whoever is left in this house can find their own.
    """

    """
    I put it into a basket with a bottle of water, and we set the basket at the foot of the stair, to be picked up on our way out.
    """

    $ host_details.objects.unlock('provisions')

    return


label host_day3_morning_scullery:

    call host_day3_morning_first_downstairs

    $ change_room('scullery')

    """
    Dirty dishes from Saturday night, and the smell of wet stone.
    """

    if host_details.threads.is_unlocked('found_poison'):

        """
        My eyes go to the shelf above the sink before I can stop them.

        The rat poison stood there on Friday, open. It was gone last night, and it has not come back.
        """

        captain """
        What are you looking for?
        """

        host """
        A bottle of rat poison.

        It was on that shelf on Friday. I did not think much of it then.
        """

        captain """
        And now it is not.
        """

        host """
        No.
        """

        captain """
        Then it is in somebody's pocket.
        """

        """
        He does not say whose. Neither do I.
        """

    else:

        """
        Nobody will wash them now.

        There is nothing here for us.
        """

    return


label host_day3_morning_garage:

    call host_day3_morning_first_downstairs

    $ change_room('garage')

    if host_details.threads.is_unlocked('seen_car'):

        """
        The tourer stands where it stood.
        """

        if host_details.threads.is_unlocked('petrol_tin'):

            """
            With the tin from the shed, the Captain says it will run.

            There is nothing more to do here until we are ready to go.
            """

        else:

            """
            It will not move an inch until we find it something to drink.
            """

        return

    """
    Petrol and cold iron.

    The good car is gone, of course. The old tourer is still here, under its dust.

    The Captain lifts the bonnet and puts his head under it.

    I stand back and try to look as though I know what he is doing.
    """

    captain """
    The engine is in order.

    Better than I expected.
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

    $ host_details.observations.unlock('seen_car')

    if host_details.threads.is_unlocked('petrol_tin'):

        captain """
        The tin from the shed will see to that.

        I will not fill it now. If anybody comes down here, I want it to look exactly as it did.
        """

        host """
        You think somebody would tamper with it?
        """

        captain """
        I think I have stopped assuming anything about this house.
        """

    else:

        captain """
        Without petrol it is a dead weight.

        If there is any on the estate, it is not in here.
        """

        host """
        The shed in the garden.
        """

        captain """
        Yes. Let us hope so.
        """

    """
    He closes the bonnet gently, and we leave the car as it was.
    """

    return


label host_day3_morning_gun_room:

    call host_day3_morning_first_downstairs

    $ change_room('gun_room_empty')

    """
    Still empty.

    Whatever was in here went into the car last night, with the luggage.
    """

    captain """
    No matter.

    I have mine.
    """

    """
    He does not take it out to show me, and I am glad of it.
    """

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label host_day3_morning_tea_room:

    $ change_room('tea_room')

    """
    The fire is dead, and the cushions are as the girl left them on Saturday.
    """

    call host_day3_morning_hear_others

    return


label host_day3_morning_dining_room:

    $ change_room('dining_room')

    """
    The table is bare.

    My chair at the head of it, and the three empty ones, and the rest.

    I said a line from a piece of paper at that table last night, and I hope it is the last line of his I ever say.
    """

    call host_day3_morning_hear_others

    return


label host_day3_morning_billiard_room:

    $ change_room('billiard_room')

    """
    The decanters stand on the side table, where the butler set them out on Friday.

    All but one.

    There was a decanter of port here on the first night, and it was gone by Saturday morning.

    The butler put it down to Mr Manning, and I did not doubt him for a second.
    """

    captain """
    This is where you found me last night.

    It seems a long time ago.
    """

    host """
    It does.
    """

    return


label host_day3_morning_entrance_hall:

    $ change_room('entrance_hall')

    """
    The hall, with the lamps out.

    The telephone sits on its table under the stair, as dead as it was on Friday.

    On the side table by the door, something small catches the light.

    A key on a plain chain.
    """

    """
    The Captain takes it up and lays it beside his own.

    They are the same.
    """

    captain """
    A master key.

    The butler gave me one. He did not mention a third.
    """

    host """
    It was not there last night. I would have seen it.
    """

    captain """
    Then somebody wants it found.
    """

    """
    He puts it in his pocket with the other.
    """

    call host_day3_morning_hear_others

    return


label host_day3_morning_garden:

    $ change_room('manor_garden')

    if host_details.threads.is_unlocked('petrol_tin'):

        """
        The gravel, the wet grass, and the tracks of the car that left last night.

        The tin waits in the shed. There is no need to go down to it again.
        """

        return

    """
    The gravel is empty, and the tracks of the car go off down the drive in the wet.

    A mist hangs over the lawn.

    At the bottom of the garden stands the squat timber shed the butler kept locked all weekend.

    We walk down to it.
    """

    # TODO add this image
    $ change_room('toolshed_outside_day')

    play sound door_locked

    """
    Locked, as it has been since Friday.
    """

    captain """
    Not to this.
    """

    play sound door_open

    $ change_room('toolshed')

    """
    A workbench, a coil of rope, tools that have not been touched in years.

    And in the middle of the floor, set down as neatly as a parcel, a metal petrol tin.

    The Captain unscrews the cap and puts his nose to it.
    """

    captain """
    Full.

    That is more than enough to reach the town.
    """

    host """
    Why would he lock away a tin of petrol?
    """

    captain """
    So that nobody could leave without asking him.

    He did not expect anybody else to have a key.
    """

    """
    He leaves the tin where it is, and locks the door behind us as carefully as he opened it.
    """

    $ host_details.objects.unlock('petrol_tin')

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
label host_day3_morning_bedroom_knock:

    $ change_room('bedrooms_hallway')

    play sound door_knock

    return


label host_day3_morning_bedroom_lad:

    call host_day3_morning_bedroom_knock

    host """
    Mr Harring?
    """

    """
    No answer.

    The Captain tries the handle, and the door is not locked.
    """

    $ change_room('bedroom_lad')

    """
    The bed has been slept in.

    The chest of drawers stands a yard from the door, where he dragged it on Saturday night.

    He moved it back this morning to get out.

    Wherever he is now, he is not hiding any more.
    """

    return


label host_day3_morning_bedroom_nurse:

    call host_day3_morning_bedroom_knock

    host """
    Miss Marsh?
    """

    """
    Nothing.

    The door is locked, and the Captain fits the key.
    """

    play sound door_open

    $ change_room('bedroom_nurse')

    $ host_details.saved_variables["day3_morning_nurse_checked"] = True

    """
    Empty.

    The bed is made, and it has not been slept in.

    Miss Marsh is somewhere in this house, or she is not, and there is nothing in these four walls to say which.
    """

    """
    The Captain locks the door again behind us.
    """

    return


label host_day3_morning_bedroom_psychic:

    call host_day3_morning_bedroom_knock

    host """
    Miss Baxter?
    """

    """
    No answer.

    The door swings open at the Captain's touch.
    """

    $ change_room('bedroom_psychic')

    """
    The bed has been slept in, and her things are laid out as neatly as on the day she arrived.

    Everything in its place.

    She is not here, and she has not packed.
    """

    return


label host_day3_morning_bedroom_drunk:

    call host_day3_morning_bedroom_knock

    if host_details.saved_variables["day3_morning_manning_checked"]:

        """
        We have opened this door once this morning.

        Neither of us has any wish to open it again.
        """

        return

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

    Nobody survives that.
    """

    """
    He comes back out and pulls the door to behind him, and for a moment we both stand in the corridor and say nothing.
    """

    $ change_room('bedrooms_hallway')

    host """
    The door was locked.

    It was locked from the outside, Captain. I saw you turn the key.
    """

    captain """
    And I have had that key in my pocket since.

    The butler had the other.
    """

    host """
    He left at eleven. We watched him go.
    """

    captain """
    Then either he came back in the night, or there is another key in this house.

    A locked door means nothing here.
    """

    """
    I slept behind one last night.

    I do not want to think about how easily it might have been mine.
    """

    captain """
    Come.

    There is nothing we can do for him, and I do not want to be found standing here.
    """

    $ play_music('PREVIOUS')

    return


label host_day3_morning_bedroom_captain:

    $ change_room('bedroom_captain')

    """
    His own room.

    He takes his greatcoat from the wardrobe and a few things from the drawer, and he does not linger.
    """

    captain """
    Whatever happens at noon, I shall not be coming back up here.
    """

    """
    I think of my own room, and the clothes I brought for a part.

    There is nothing in it I want.
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


# ------------------------------------
#   ATTIC
# ------------------------------------
label host_day3_morning_attic_default:

    $ change_room('attic_hallway')

    if not host_details.saved_variables["day3_morning_attic_visited"]:

        $ host_details.saved_variables["day3_morning_attic_visited"] = True

        """
        The attic stair.

        On Friday every door up here was locked against me, and I had no key.

        This morning the Captain has two.
        """

    return


label host_day3_morning_attic_butler_room:

    call host_day3_morning_attic_default

    play sound door_open

    $ change_room('attic_butler_room')

    """
    His room.

    The bed is stripped and the wardrobe is empty. He took his own things, at least.

    Against the far wall stands a cabinet with an iron band across its doors.

    The master key opens it.
    """

    """
    The candlesticks from the dining table. The salver. The good spoons.

    A flat case, and inside it the pearls I wore on Friday night.

    Everything the house was dressed with for this weekend, packed and ready, and left behind.
    """

    captain """
    He left in a hurry.
    """

    host """
    No.

    He had the whole evening to load that car, and he had this key.

    He did not leave it. He means to come back for it.
    """

    """
    The Captain closes the cabinet and turns the key in it again.
    """

    captain """
    Then we had better not be here when he does.
    """

    return


label host_day3_morning_attic_storage:

    call host_day3_morning_attic_default

    play sound door_open

    $ change_room('attic_storage_room')

    """
    Trunks, mostly empty.

    A spare livery on a hanger, and a hamper with the name of a London theatrical supplier on the lid.

    The whole weekend came up here in these boxes, and it will not be going back in them.
    """

    return


label host_day3_morning_attic_males_room:

    call host_day3_morning_attic_default

    play sound door_open

    $ change_room('attic_males_room')

    """
    The footman's room, stripped to the bed frame.

    He was the best of us, I think. Not one word out of place all weekend.

    I hope he is a long way from here.
    """

    return


label host_day3_morning_attic_females_room:

    call host_day3_morning_attic_default

    play sound door_open

    $ change_room('attic_females_room')

    """
    The girl's room.

    A hairbrush on the washstand, forgotten in the hurry.

    She was the youngest of us, and the most frightened, and she had the least to be frightened of.

    I hope she is a long way from here too.
    """

    return
