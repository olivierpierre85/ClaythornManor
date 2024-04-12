label lad_library_default:

    $ change_room('library')

    if not lad_details.saved_variables["library_visited"]:

        """
        It's a very nice library. But what am I doing here? 
        
        I can barely read.
        """

        $ lad_details.description_hidden.unlock('education')

        """
        There is an open book on a small table.

        "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain."

        Yeah, I'm not reading that.

        I should probably look elsewhere.
        """
        # TODO add info on BOOK???
        $ lad_details.saved_variables["library_visited"] = True

    else:

        """
        There is nothing different from the last time I was in here.

        No reason to look further.
        """

    return

label lad_attic_default:

    $ change_room("attic_hallway")

    if not lad_details.saved_variables['attic_visited']:

        """
        I took the stairs to the attic.

        I'm not sure if I should be here.
        """

        $ lad_details.saved_variables["attic_visited"] = True

    return

label lad_downstairs_default:

    $ change_room("basement_stairs")

    if lad_details.saved_variables["has_try_sneaking_downstairs"] == 0:

        """
        I was on my way to the basement when a young maid stopped me.
        """

        maid """
        Hello Sir, may I help you?
        """

        lad """
        Oh, don't mind me. I'm just taking a look around.
        """

        maid """
        I'm sorry, but the basement is off-limits to guests.

        However, there are plenty of rooms upstairs that you can explore.
        """

        lad """
        Of course, thank you.
        """

        $ lad_details.saved_variables["has_met_maid"] = True

        $ lad_details.saved_variables["has_try_sneaking_downstairs"] += 1

    elif lad_details.saved_variables["has_try_sneaking_downstairs"] == 1:

        """
        Let's see if I can check downstairs now.

        I walk down the stairs slowly, being very careful not to attract attention.

        But as I'm stepping down to the basement, the same woman stops me.
        """

        maid """
        You again, Sir? As I already told you, I'm afraid you're not allowed to be here.
        """

        lad """
        Of course, I was just lost. I'm terribly sorry.
        """

        maid """
        It's alright, don't worry about it, sir.
        """

        """
        I'd better be careful. If I'm caught here a third time, it will really start to look suspicious.
        """

        $ lad_details.saved_variables["has_try_sneaking_downstairs"] += 1

    elif lad_details.saved_variables["has_try_sneaking_downstairs"] == 2:

        """
        Maybe I'm pushing my luck, trying to go downstairs, but I feel like I have to go there.
        """

        maid """
        Mister Harring? I thought I made myself clear earlier.

        What are you trying to do here?

        You can't possibly make me believe that you got lost again?
        """

        call run_menu(
            TimedMenu("lad_has_try_sneaking_downstairs", [
                # TimedMenuChoice("I know it sounds ridiculous, but I DID get lost again", 'lad_downstairs_lost', 5, early_exit=True),
                TimedMenuChoice("Zzzzzz (Pretend you're sleepwalking)", 'lad_downstairs_sleepwalk', 10, early_exit=True),
                TimedMenuChoice("Actually, I just wanted to talk to you (flirt your way out)", 'lad_downstairs_flirt', 10, early_exit=True),
            ])
        )

        $ lad_details.saved_variables["has_try_sneaking_downstairs"] += 1

    return

label lad_downstairs_lost:
    # TODO: complicated arc with dead ending:
    # Captain/butler overhears discussion with maid; you are locked in your room for the night.
    # Over the night, somebody opens your door? Who? Psychic? Nurse?
    # But when the captain sees you, he is scared and shoots you?

    lad """
    I'm really sorry. This house is too big.

    I was on my way to the billiard room and I don't know how I ended up here.
    """

    return

label lad_downstairs_sleepwalk:

    play sound snoring_long

    """
    I keep staring in front of me, pretending not to have heard her.

    I add a realistic snore to sell the trick.

    She looks at me, confused.

    She hesitates, uncertain of what to do.
    """

    maid """
    Sir, are you well?

    Are you sleepwalking?
    """

    """
    I keep saying nothing and slowly move back up the stairs.

    She doesn't follow me.

    I think I'm in the clear.
    """

    maid """
    I know you're not asleep.

    First, your snore is obviously fake.

    Second, you're still fully clothed.
    """

    """
    I can't break character.

    I need to commit to the end, so I ignore her and keep moving up the stairs.

    Once I reach the main floor, I look for somewhere else to go.
    """

    stop sound

    # TODO: ALSO get caught here?

    return


label lad_downstairs_flirt:
    
    maid """
    You wanted to see me?

    Why?

    The kitchen is closed, but I can fix you a plate of leftovers if you're still hungry.
    """

    lad """
    Oh, uh, no thank you. I'm not really, um, hungry or anything.
    """

    maid """
    What brings you here so late then?
    """

    lad """
    I was just looking for someone to talk to.
    """

    maid """
    I see. Well, there are many people around if you're looking for company.
    """

    lad """
    Yeah, I know. But I don't think anyone is as interesting as you.
    """

    """
    Okay, that was quite straightforward.

    She seems speechless for a moment.

    When she regains her composure, she appears annoyed.
    """

    maid """
    That's kind of you to say. 
    
    However, I shouldn't have to tell you that it's inappropriate for you to flirt with me in this manner.
    """

    lad """
    Oh, uh, I didn't mean to, um, make you uncomfortable or anything. 
    
    I was just looking for friendly conversation.
    """

    maid """
    I'm afraid I'm too busy for this, sir.

    I must return to my tasks. 
    
    Good night.
    """

    lad """
    Of course. Good night.
    """

    """
    Alright, that was uncomfortable.

    But at least she doesn't think I was sneaking down here; that was a close call.

    Still, I'd better go look somewhere else.
    """

    return


label lad_garden_default:

    $ change_room('manor_garden')

    # TODO: Expand, and add more time to option
    # TODO: Move to no hunt if it's the only time where you can go out
    
    """
    A beautiful garden.

    I wandered in it for a while, enjoying a relaxing walk.

    But in the end, I didn't find anything of interest.
    """

    return

label lad_garage_default:

    call lad_downstairs_default

    return

label lad_tea_room_default:
    
    $ change_room('tea_room')
    
    """
    There is nobody here.

    No need to stay any longer.
    """

    return

label lad_dining_room_default:
    
    $ change_room('dining_room')
    
    """
    The dining room is empty at the moment.
    
    I shouldn't stay here.
    """

    return

label lad_billiard_room_default:
    
    $ change_room('billiard_room')
    
    """
    It's empty.

    "No need to stay here.
    """

    return

label lad_bedroom_default:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door.

    Nobody answers.
    """

    return

label lad_entrance_hall_default:
    
    $ change_room("great_hall")
    
    """
    It's certainly an impressive entrance hall.
    
    Nobody is here.
    """

    return

label lad_portrait_gallery_default:
    
    $ change_room("portrait_gallery")

    if not lad_details.saved_variables["portrait_gallery_visited"]:
    
        """
        That's a creepy portrait gallery.

        I don't recognize anyone, so I guess these are people from the Claythorn family.
        """

        # TODO: Possibility to zoom in on specific members?

        $ lad_details.saved_variables["portrait_gallery_visited"] = True
    
    else:

        """
        Nothing new here.

        It still gives me a weird, creepy feeling.
        """

    return

# Downstairs
label lad_kitchen_default:
    call lad_downstairs_default
    return

label lad_scullery_default:
    call lad_downstairs_default
    return

label lad_gun_room_default:
    call lad_downstairs_default
    return

# Attic
label lad_storage_default:

    call lad_attic_default

    """
    I try to open the attic storage room, but it's closed.
    """
    
    return

label lad_females_room_default:

    call lad_attic_default

    """
    I try to open the room, but it's closed.
    """

    return

label lad_males_room_default:

    call lad_attic_default

    """
    I try to open the room, but it's closed.
    """

    return

label lad_butler_room_default:
    
    call lad_attic_default

    """
    I try to open the room, but it's closed.
    """

    return
