label nurse_bedroom_default:

    call nurse_bedroom_default_intro

    """
    No answer.
    """

    return


label nurse_bedroom_default_intro:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    nurse """
    Hello? Is anyone there?
    """

    return

label nurse_bedroom_lockpick_choice(search_label):

    call nurse_lockpick_door

    call expression search_label

    return

label nurse_lockpick_door:

    play sound door_locked

    """
    The door is locked.
    """

    if not nurse_details.saved_variables["lockpick_seen"]:

        $ nurse_details.saved_variables["lockpick_seen"] = True

        """
        But it would take me very little effort to open it.

        In my years of nursing, I have become acquainted with all manner of locks — on medicine cabinets, ward doors, and supply rooms.

        And I quickly realised how convenient it is to be able to open them all.

        That is why I learned to pick locks.

        A most useful skill.

        So, I easily make my way inside.
        """

    else:

        """
        I easily make my way inside.
        """

    return

# Possible searches for treasure => Only after day 2 (during the hunt there is nobody)

label nurse_search_captain_default:

    $ nurse_details.saved_variables["visited_bedroom_captain"] = True
    $ change_room("bedroom_captain")

    play sound door_locked

    """
    The room is neat to the point of severity.

    A coat hangs straight on its hook.

    A leather case sits packed on the stand, its straps buckled precisely.

    Nothing is left in reach.

    Military discipline of this kind belongs to one man in this house.

    I search thoroughly, but find nothing of use.

    Whatever the Captain values, he keeps it close to his person.
    """

    $ unlock_map('bedroom_captain')

    return


label nurse_search_captain_again:

    $ change_room("bedroom_captain")

    """
    I look over the Captain's immaculate room one last time.

    Everything remains exactly as I found it earlier.

    If there is a secret here, it is too well hidden for me to find now.

    I should not linger and press my luck.
    """

    return


label nurse_search_captain_master_key:

    """
    I turn to the jacket on the hook by the door.

    The hunting jacket — heavier than the dinner jacket, rougher cloth.

    I slip my hand into the right pocket.

    Nothing.

    The left.

    My fingers close around cold metal.

    A key, heavy and old, with a long shaft and an open bit at the end.

    It doesn't look like a normal bedroom key.

    That must be the butler's master key.

    This might come in handy.
    """

    $ nurse_details.threads.unlock('master_key')

    return


label nurse_search_host_default:

    $ nurse_details.saved_variables["visited_bedroom_host"] = True
    $ change_room("bedroom_host")

    """
    The room is larger than mine, dressed in pale silks and heavy curtains.

    This is unquestionably the lady of the house's own chamber.

    I look quickly through the dressing table.

    A jet brooch, a few hairpins, a string of pearls in a velvet case.

    They catch my eye for a moment — but only for a moment.
    """

    $ unlock_map('bedroom_host')

    """
    This is not much for a woman of Lady Claythorn's standing.

    Pearls and jet are for show — for evenings and guests.

    There should be more.

    I also don't see the prize money anywhere. That's the real reason I am in this room.

    One thousand pounds each. Seven guests. Seven thousand pounds in bearer bonds.

    Whoever holds bearer bonds holds the money. There are no names on them. No register.

    They could walk out of this house in anyone's pocket.

    But that is if they exist at all.

    It would not surprise me greatly if there were no bonds. No ceremony. Nothing.

    But if they are real, they are here somewhere.

    I look more carefully. Behind the curtain, beneath the floorboards, behind a picture — it could be anywhere.

    But I find nothing.

    There is a safe somewhere. There must be.

    Though perhaps not here. A woman like Lady Claythorn may well keep it in a study, or some other room she considers entirely her own.

    I simply have not found it yet.

    Before I leave, I look over what might be worth taking.

    The pearls are the only items of any real value.
    """

    call run_menu(TimedMenu("nurse_search_host_choice_default", [
        TimedMenuChoice("Take the pearls.", 'nurse_take_pearls', 5, early_exit=True),
        TimedMenuChoice("Leave them. It's not worth the risk.", 'generic_cancel', early_exit=True),
    ]))

    return


label nurse_search_host_again:

    $ change_room("bedroom_host")

    """
    I carefully search Lady Claythorn's room once more.

    The heavy curtains, the dressing table, the floorboards... I check it all again.

    But there is simply nothing else to be found. 

    If the bearer bonds are here, they are in a safe I cannot locate.
    """

    if not nurse_details.threads.is_unlocked('steal_pearls'):
        
        """
        The string of pearls still sits in its velvet case on the dressing table.

        I left them earlier, but they remain the only transportable item of value in the room.
        """

        call run_menu(TimedMenu("nurse_search_host_choice_again", [
            TimedMenuChoice("Take the pearls.", 'nurse_take_pearls', 5, early_exit=True),
            TimedMenuChoice("Leave them. It's not worth the risk.", 'generic_cancel', early_exit=True),
        ]))

    return


label nurse_take_pearls:

    """
    Not first-rate, but they will fetch something.

    I slip them into my bag and leave.
    """

    $ nurse_details.threads.unlock('steal_pearls')

    return


label nurse_search_lad_default:

    $ change_room("bedroom_lad")

    """
    There isn't much in here.

    A jacket thrown over the chair, a battered holdall on the floor.

    There is nothing here worth taking.

    But it should not be a surprise.

    Anyone looking more than a few seconds at Ted Harring would see he is not a man of means.
    """

    return


label nurse_search_broken_default:

    $ change_room("bedroom_broken")

    $ play_music('sad', 2)

    """
    Mr Moody's room.

    His body settled on the bed, hidden underneath the bed sheets.

    One could be easily frightened, but I am used to this.

    Usually, a dead body doesn't cause me anguish, only respect and sadness.

    And yet here I am, with the purpose of stealing from a man who can't defend himself anymore.

    I should feel bad, but I know I need the money more than he does now.

    So I start looking.

    But the bounty is meager.

    Nothing on the dressing table.

    A small case with his clothes under the bed.

    That's it.

    I could also search his body, but that would be going too far, even for me.

    I close the door softly and leave.
    """

    $ unlock_map('bedroom_broken')

    $ nurse_details.saved_variables['day2_has_seen_bedroom_broken'] = True

    $ play_music('PREVIOUS')

    return


label nurse_search_doctor_default:

    $ change_room("bedroom_doctor")

    """
    A doctor's bag sits open on the small writing desk.

    Instruments, a bottle of laudanum, a notebook with the clasp shut.

    There is no mistaking whose room this is.

    I know better than to disturb another's bag.

    Partly professional courtesy.

    Partly because there is nothing in there I could make use of.
    """

    $ unlock_map('bedroom_doctor')

    return


label nurse_garage_default:

    if nurse_details.saved_variables.get("visited_garage"):

        $ change_room("garage")

        """
        It looks exactly the same as before.

        No need to search any further.
        """

    else:

        $ nurse_details.saved_variables["visited_garage"] = True

        $ change_room("garage")

        """
        I reach the garage, making sure I should not encounter anyone.

        It is a cold, oil-smelling place.

        There is an old car; it does not look as though it is working any more.

        Tools hang neatly along one wall, and a bicycle leans against another.

        Nothing here that is of any use to me.
        """

    return


label nurse_gun_room_default:

    if nurse_details.saved_variables.get("visited_gun_room"):

        $ change_room("gun_room")

        if nurse_details.threads.is_unlocked('take_gun'):

            """
            There is nothing new in here.

            I search a bit more for bullets, but still cannot find any.

            So there is no reason to stay here.
            """

            # We still have to remove some time, even if we've been here before
            $ time_left = time_left - 10

            return

        else:

            """
            The rows of weapons remain exactly as they were.

            The small pistols are still available if I so desire.
            """

    else:

        $ nurse_details.saved_variables["visited_gun_room"] = True

        $ change_room("gun_room")

        """
        The gun room.
        
        I am confident that I should not be here, so I made sure no one noticed me.

        Shotguns and hunting rifles line three walls, arranged on open racks.

        The smell of gun oil is sharp.

        Everything is laid out as though ready for use — nothing locked away.

        There are even a few small handguns lying on a table.

        It looks like something I could use.
        """

    if not nurse_details.threads.is_unlocked('take_gun'):
        call run_menu(TimedMenu("nurse_gun_room_choice", [
            TimedMenuChoice("Take a pistol", 'nurse_take_gun', 20, early_exit=True),
            TimedMenuChoice("Leave it. Too dangerous to carry.", 'generic_cancel', 20, early_exit=True),
        ]))

    return


label nurse_take_gun:

    """
    My hand closes around the grip of a small revolver.

    It is not loaded.
    """

    if nurse_details.threads.is_unlocked('find_bullets'):

        """
        But I already have the bullets I found in the attic.

        I take them out and carefully load the weapon.

        It is good to be prepared.
        """

    else:

        """
        And I have not seen any bullets lying about.

        Nevertheless, it could prove useful.
        """

    """
    I slip it into my bag.

    Nobody will notice. Not for a while, at any rate.
    """

    $ nurse_details.threads.unlock('take_gun')

    return


label nurse_tea_room_default:

    $ change_room('tea_room')

    """
    The room is quite empty.

    The teapot has gone cold.

    There is nothing to keep me here.
    """

    return


label nurse_billiard_room_default:

    $ change_room('billiard_room')

    """
    The billiard room is empty, the table undisturbed.

    There is nothing here for me.
    """

    return


label nurse_entrance_hall_default:

    $ change_room('entrance_hall')

    """
    The great hall is quiet.

    The chandelier has been turned down low.

    I stand beneath it for a moment, listening.

    The house settles around me.

    There is something watchful about the place at this hour.
    """

    return


label nurse_downstairs_approach:

    """
    I move quietly through the back passage.

    Years of moving through dark passages in hospitals and large houses have taught me how to remain unseen.

    I reach the kitchen door and ease it open an inch.
    """

    return


label nurse_library_default:

    if nurse_details.saved_variables.get("visited_library"):

        $ change_room("library")

        if nurse_details.threads.is_unlocked('captain_lie_zanzibar'):

            """
            There is nothing more for me to find here.

            I already know what I need to know about Zanzibar.
            """

            return

        else:

            """
            The library remains as it was.

            The volumes of "A History of the British Army" are still on the shelf.
            """

    else:

        $ nurse_details.saved_variables["visited_library"] = True

        $ change_room("library")

        """
        A well-appointed library.

        "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain" lies open on a table.

        I cast my eye along the shelves.

        Mostly heraldry, county histories, and bound journals.

        Nothing worth taking — far too heavy, and of no particular value.

        I am about to leave when a title catches my attention.

        "A History of the British Army" — Fortescue.

        Fourteen volumes.

        I have seen this set before, in the officers' mess at Netley.

        The Captain mentioned Zanzibar at some point, I remember.

        Something in the way he spoke of it nagged at me, though I could not quite place it at the time.

        I could try to learn more about that conflict, though it may take some time.
        """

    if not nurse_details.threads.is_unlocked('captain_lie_zanzibar'):
        call run_menu(TimedMenu("nurse_library_choice", [
            TimedMenuChoice("Look it up. It may be useful.", 'nurse_library_war_book', 30, early_exit=True),
            TimedMenuChoice("Leave it. I am too tired for reading.", 'generic_cancel', 20, early_exit=True),
        ]))

    return


label nurse_library_war_book:

    """
    I take down the volume covering the latter campaigns in India and East Africa.

    I find the index and look up Zanzibar.

    A single page.

    The engagement lasted thirty-eight minutes.

    The shortest war in recorded history, apparently.

    The British bombardment was overwhelming.

    Casualties on the British side were minimal — one man, lightly wounded.

    If what the Captain said is true, he would be the only injured soldier from the entire war.

    That seems most unlikely.

    He may well have invented the whole story — but to what end?
    """

    $ nurse_details.threads.unlock('captain_lie_zanzibar')

    return


label nurse_portrait_gallery_default:

    if nurse_details.saved_variables.get("visited_portrait_gallery"):

        $ change_room('portrait_gallery')

        """
        The portraits remain as they were, their silent judgement unchanged.

        There is nothing here for me.
        """

    else:

        $ nurse_details.saved_variables["visited_portrait_gallery"] = True

        $ change_room('portrait_gallery')

        """
        The gallery is lit by a single gas lamp.

        The Claythorn ancestors gaze down from their frames with an air of collective disapproval.

        I feel rather as though I am being assessed.

        I do not linger.
        """

    return


# Attic
label nurse_attic_approach:

    
    $ change_room("attic_hallway")

    if not nurse_details.saved_variables.get("generic_attic_visited", False):

        $ nurse_details.saved_variables["generic_attic_visited"] = True

        """
        The attic staircase creaks with every step.

        Up here, the air is close and smells of dust and old timber.

        The corridor runs the length of the house, doors on either side.

        With the servants all occupied below, there is no one to question what I am doing up here.
        """

    call nurse_lockpick_door

    return


label nurse_attic_females_room:

    call nurse_attic_approach

    if nurse_details.saved_variables.get("visited_attic_females_room"):

        $ change_room("attic_females_room")

        """
        It looks exactly the same as before.

        No need to search any further.
        """

    else:

        $ nurse_details.saved_variables["visited_attic_females_room"] = True

        $ change_room("attic_females_room")

        """
        It is a small, spare space — two narrow beds, a washstand, a single trunk between them.

        On the shelf above one of the beds, a small collection of things: a dog-eared playbill from a London theatre, another from a touring company. 
        
        A faded photograph is tucked behind them.

        I take the photograph down.

        A young woman in stage dress, posed with a man I do not recognise.

        She is smiling broadly. I recognise the young maid working here.

        So she is, or was, an aspiring actress.

        How peculiar for her to end up here.

        I wonder what her story is.

        I replace everything as it was and step back out.
        """

        $ nurse_details.threads.unlock('maid_actress')

    return


label nurse_attic_butler_room:

    call nurse_attic_approach

    if nurse_details.saved_variables.get("visited_attic_butler_room"):

        $ change_room("butler_room")

        if nurse_details.threads.is_unlocked('silverware_big'):

            """
            The cabinet stands open, emptied of anything worth taking.

            There is nothing more for me here.
            """

        elif nurse_details.saved_variables.get("tried_butler_cabinet"):

            if nurse_details.threads.is_unlocked('master_key'):

                """
                The reinforced cabinet still stands against the far wall.

                But this time, I have the master key.
                """

                call nurse_butler_cabinet_open_with_master_key

            else:

                """
                The reinforced cabinet still stands against the far wall.

                Without the butler's key, there is nothing I can do here.
                """

        else:

            """
            The room itself is surprisingly ordinary.

            However, standing against the far wall is a large, reinforced cabinet.
            """

    else:

        $ nurse_details.saved_variables["visited_attic_butler_room"] = True

        $ change_room("butler_room")

        call nurse_butler_room_first_visit

    if not nurse_details.saved_variables.get("tried_butler_cabinet") and not nurse_details.threads.is_unlocked('silverware_big'):

        call run_menu(TimedMenu("nurse_attic_butler_cabinet_choice", [
            TimedMenuChoice("Try to open the cabinet", 'nurse_butler_cabinet_lockpick', 20, early_exit=True),
            TimedMenuChoice("Leave it for now", 'generic_cancel', 10, early_exit=True),
        ]))

    return


label nurse_butler_cabinet_lockpick:

    $ nurse_details.saved_variables["tried_butler_cabinet"] = True

    if nurse_details.threads.is_unlocked('master_key'):

        call nurse_butler_cabinet_open_with_master_key

    else:

        """
        I approach the cabinet and attempt to pick the lock.

        But this is no ordinary lock.

        The mechanism inside is far more intricate than those I am used to.

        After a few moments of fruitless effort, I am forced to admit defeat.

        I shall not be able to open this by force or skill alone.

        I will need the butler's key.
        """

    return


label nurse_butler_cabinet_open_with_master_key:

    """
    I approach the cabinet.

    But before I waste time with my lockpicks, I remember the master key.

    I take it from my pocket and fit it into the lock.

    It turns with a satisfying click.

    The cabinet doors swing open.

    No bearer bonds.

    Disappointing, but I was expecting it.

    Luckily, the cabinet is not empty.

    A pair of candlesticks, a salver, a set of heavy serving spoons — all solid, all worth a good deal more than sentiment.

    I take what I can fit in my bag.

    Then I close the cabinet and step back.

    This changes everything.

    This might actually be enough.

    Enough to matter.
    """

    $ nurse_details.objects.unlock('silverware_big')

    return


label nurse_attic_males_room:

    call nurse_attic_approach

    if nurse_details.saved_variables.get("visited_attic_males_room"):

        $ change_room("attic_males_room")

        """
        It looks exactly the same as before.

        No need to search any further.
        """

    else:

        $ nurse_details.saved_variables["visited_attic_males_room"] = True

        $ change_room("attic_males_room")

        """
        Two beds, a chest of drawers, a peg for each man's jacket.

        I check the drawers quickly — folded shirts, a penknife, a few coins.

        No valuables here.

        Tucked at the very back of the bottom drawer, I find a passport. Belgian.

        I open it carefully.

        On the photograph inside I recognize Lady Claythorn's footman.

        But his name is indeed not british at all. "André De Prei"

        That is very peculiar.

        I close it and replace it exactly as I found it.
        """

        $ nurse_details.threads.unlock('footman_belgian')

    return


label nurse_attic_storage:

    call nurse_attic_approach

    if nurse_details.saved_variables.get("visited_attic_storage"):

        $ change_room("attic_storage_room")

        if nurse_details.threads.is_unlocked('find_bullets'):

            """
            There is nothing more for me to find here.

            I have already gone through the important items.
            """

        else:

            """
            The storage room remains a jumble of trunks and boxes.

            I still have not searched it thoroughly.
            """

    else:

        $ nurse_details.saved_variables["visited_attic_storage"] = True

        $ change_room("attic_storage_room")

        """
        The storage room is vast.

        Trunks stacked three deep, old furniture draped in dust sheets, boxes of every shape and size.

        I barely know where to begin.
        """

    if not nurse_details.threads.is_unlocked('find_bullets'):

        call run_menu(
            TimedMenu(
                id='nurse_attic_storage_search',
                choices=[
                    TimedMenuChoice('Search everything carefully', 'nurse_attic_storage_search_all', 60, early_exit=True),
                    TimedMenuChoice('Give up. This will take all day.', 'nurse_attic_storage_give_up', 10, early_exit=True),
                ]
            )
        )

    return


label nurse_attic_storage_search_all:

    """
    The trunks are packed tightly and most of them are locked.

    I manage to open one — old curtains, heavy and mildewed.

    Another: crockery wrapped in cloth.

    I lift a dust sheet from what turns out to be an old escritoire.

    The drawers are empty save for a few dried-up pen nibs and a folded invoice from eighteen ninety.

    The shelves near the door hold rows of old tins and jars, most unlabelled.

    I move some aside — and then I stop.

    Behind a row of old paint tins, stacked neatly and deliberately out of sight:

    Bullets.

    A good number of them. 

    Someone has gone to some trouble to hide these.
    """

    $ nurse_details.threads.unlock('find_bullets')

    if nurse_details.threads.is_unlocked('take_gun'):

        """
        I take them out and carefully load the small revolver I took from the gun room.

        It is good to be prepared.
        """

    else:

        """
        I shall need a gun to use these, but I take them regardless.
        """

    """
    Then I replace the tins exactly as they were, and leave the room as quietly as I came.
    """


    return


label nurse_attic_storage_give_up:

    """
    I have been in here long enough.

    There is too much to search properly, and I am beginning to feel uneasy.

    I leave without having found anything of note.
    """

    return


label nurse_butler_room_first_visit:

    """
    The room itself is surprisingly ordinary — a head servant's quarters.

    A neat bed, a small washstand, and a plain wooden chair.

    However, standing against the far wall is a large, reinforced cabinet.

    Through its glass panes, I can see the household silver and other valuables gleaming in the dim light.

    This must be where the true wealth of the house is kept.
    """

    return