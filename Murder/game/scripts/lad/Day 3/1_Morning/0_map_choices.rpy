# -------------------------
# Sunday Search MAX 250 !
# -------------------------

label lad_day3_morning_map_menu:
    python:    
        lad_day3_morning_map_menu = TimedMenu("lad_day3_morning_map_menu", [
            TimedMenuChoice(default_room_text('library'), 'lad_day3_morning_library', 10, room='library'),
            TimedMenuChoice(default_room_text('tea_room'), 'lad_day3_morning_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'lad_day3_morning_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'lad_day3_morning_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'lad_day3_morning_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'lad_day3_morning_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('billiard_room'), 'lad_day3_morning_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice(default_room_text('storage'), 'lad_day3_morning_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'lad_day3_morning_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'lad_day3_morning_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'lad_day3_morning_butler_room', 10, room='butler_room'),
            TimedMenuChoice(
                default_room_text('bedroom_lad'), 
                'lad_day3_morning_bedroom_lad',
                10,
                room = 'bedroom_lad'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_psychic'), 
                'lad_day3_morning_bedroom_psychic',
                10,
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_drunk'), 
                'lad_day3_morning_bedroom_drunk',
                10,
                room = 'bedroom_drunk'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_doctor'), 
                'lad_day3_morning_bedroom_doctor',
                10,
                room = 'bedroom_doctor'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_broken'), 
                'lad_day3_morning_bedroom_broken',
                10,
                room = 'bedroom_broken'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_captain'), 
                'lad_day3_morning_bedroom_captain',
                10,
                room = 'bedroom_captain'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_host'), 
                'lad_day3_morning_bedroom_host', 
                20, 
                room = 'bedroom_host'
            ),
            TimedMenuChoice(
                default_room_text('bedroom_nurse'), 
                'lad_day3_morning_bedroom_nurse', 
                20, 
                room = 'bedroom_nurse'
            ),                  
            TimedMenuChoice(
                default_room_text('kitchen'), 
                'lad_day3_morning_kitchen', 
                10, 
                room = 'kitchen'
            ),
            TimedMenuChoice(
                default_room_text('scullery'), 
                'lad_day3_morning_scullery', 
                10, 
                room = 'scullery'
            ),
            TimedMenuChoice(
                default_room_text('garage'), 
                'lad_day3_morning_garage', 
                10, 
                room = 'garage'
            ),
            TimedMenuChoice(
                default_room_text('gun_room'), 
                'lad_day3_morning_gun_room', 
                0, 
                room = 'gun_room'
            ),
            TimedMenuChoice(
                'Go wait for Sushil', 
                'generic_cancel', 
                early_exit = True, 
                room = 'tea_room', 
                condition = 'lad_details.saved_variables["day3_morning_captain_found"]'
            ),

        ], is_map = True)

    return



# Downstairs
label lad_day3_first_downstairs:

    if not lad_details.saved_variables["day3_downstairs_visited"]:

        $ change_room("basement_stairs")

        """
        I take the stairs to the basement, expecting to be stopped at any moment.

        But no one is there.

        I can safely explore downstairs now.
        """

        $ lad_details.saved_variables["day3_downstairs_visited"] = True

    return


label lad_day3_morning_kitchen:

    call lad_day3_first_downstairs

    $ change_room('kitchen')

    """
    I reach the kitchen.

    I guess it's a typical kitchen for a house of this size.

    Pots and pans are scattered around.
    """
        
    psychic """
    You see?

    No one is here.

    And yet, breakfast should be ready soon.
    """

    lad """
    Ok, I admit that is very strange indeed.
    """

    """
    We look around a bit but don't find anything of interest.
    """
    
    return

label lad_day3_morning_gun_room:

    call lad_day3_first_downstairs

    $ change_room('gun_room')

    """
    The gun room is a bit intimidating.

    So much firepower for just one household.

    It makes me uneasy.
    """

    lad """
    Nobody is here.
    """

    psychic """
    No, indeed.

    But don't you think it might be useful to get a weapon for protection?
    """

    """
    Well, I don't have much experience with guns.

    It might be a bad idea.

    But then again, I don't know what we might encounter today.
    """

    call run_menu(TimedMenu("lad_day3_morning_gun_room", [
        TimedMenuChoice("Take the gun. It doesn't matter that I don't know how to use it", 'lad_day3_take_gun', 10, early_exit=True),
        TimedMenuChoice("Don't take the gun. You might hurt yourself.", 'lad_day3_no_gun', 10, early_exit=True), 
    ]))

    return

label lad_day3_take_gun:

    lad """
    You are right.

    We should get something to defend ourselves.
    """

    """
    The hunting rifles are a bit too large.

    But I spot a revolver that fits my pocket.
    """

    lad """
    Alright, I'll take this with me.

    However, there are no bullets in it.
    """

    psychic """
    Sometimes, bullets are kept separate from the guns.

    It reduces the likelihood of accidents.
    """

    lad """
    So, where could they be?
    """

    psychic """
    I have no idea.

    Will you still take it?
    """

    lad """
    I think so, even an empty gun can still scare someone away.
    """

    psychic """
    I suppose.
    """

    """
    She doesn't look very convinced. 

    I pocket the gun anyway.
    """

    $ lad_details.objects.unlock('gun')

    return


label lad_day3_no_gun:

    lad """
    No, I don't think so.

    We might end up hurting ourselves.
    """

    psychic """
    Alright, if that's what you want.
    """

    return


label lad_day3_morning_scullery:

    call lad_day3_first_downstairs

    $ change_room('scullery')

    lad """
    Do you know what room this is?
    """

    psychic """
    The scullery.
    """

    """
    Wait, what the hell is a scullery?

    Miss Baxter must have noticed my puzzled look, because she went on explaining.
    """

    psychic """
    It's primarily where they wash dishes.

    If you look in the sink, there are a lot of dirty dishes.

    It seems nobody cleaned up after supper yesterday.
    """

    """
    Right.

    It's empty anyway, no need to linger here.
    """

    return


label lad_day3_morning_garage:

    call lad_day3_first_downstairs

    $ change_room('garage')

    """
    The garage.

    This is where Lady Claythorn's car should be.

    But instead, there are only parts of other cars and an old model in a shabby state.
    """

    lad """
    Did you come here in this car?
    """

    psychic """
    No, of course not.
    
    Lady Claythorn's chauffeur drove us here in a Rolls Royce.

    Not in this old thing.
    """

    lad """
    Me neither.
    """

    lad """
    But if everyone has left, we might need it to reach the next town.
    """

    psychic """
    Right. But do you know how to drive it?

    Because I surely can't.
    """

    $ psychic_details.description_hidden.unlock('drive')

    lad """
    Not really, no.

    I never learned how to drive.
    """

    """
    It's not like I could afford a car anyway.
    """

    $ lad_details.description_hidden.unlock('drive')

    $ lad_details.important_choices.unlock('seen_car')

    return


# First Floor
label lad_day3_morning_library:

    $ change_room("library")
    
    """
    We enter the small library and find it empty.

    There's no room for anyone to hide here.

    Let's move on.
    """
    
    return


label lad_day3_morning_dining_room:

    $ change_room("dining_room")

    lad """
    Nobody seems to be here.
    """

    psychic """
    And the table isn't set for breakfast either.

    That's unusual.
    """

    return


label lad_day3_morning_garden:

    $ change_room('manor_garden')
    
    """
    We venture out to explore the garden.

    But there's no trace of anyone.

    Lady Claythorn's car isn't there either.

    I try shouting to attract attention.
    """

    lad """
    Hello! Is anyone here?

    Hello!!
    """

    """
    No response.
    """

    psychic """
    I don't think shouting will help.

    If someone's here, we'll find them.
    """

    """
    Oh, was shouting inappropriate?

    I guess she'll always prioritize decorum, no matter the situation.

    Let's head back inside then.
    """

    return


label lad_day3_morning_entrance_hall:

    $ change_room("great_hall")
    
    """
    The entrance hall is usually the heart of the house.

    But there's no activity today.

    Just in case, I try to call out for someone.
    """

    lad """
    Is anyone here?
    """

    """
    I didn't really expect an answer.

    But an authoritative voice echoes from up the stairs.
    """

    captain """
    Who goes there?
    """

    lad """
    It's Ted Harring. I'm down here, and Amelia Baxter's with me.
    """

    captain """
    Understood. I'm on my way down.
    """

    """
    Soon enough, Captain Sinha comes into view, descending the staircase to join us on the ground floor.
    """

    call common_day3_morning_meeting_captain

    psychic """
    Staying put won't give us any answers.
    
    We need to continue exploring the house.
    """

    captain """
    Agreed. Should we search together?
    """

    psychic """
    Thank you, but... maybe it's better to split up. 
    
    We'd cover more ground that way.
    """

    """
    Amelia seemed nervous when she answered.
    """

    captain """
    Makes sense. Let's proceed on our own and regroup later. 

    How about the tea room?
    """

    psychic """
    That sounds good.

    See you there.
    """

    $ lad_details.saved_variables["day3_morning_captain_found"] = True

    return


label lad_day3_morning_portrait_gallery:
    
    $ change_room("portrait_gallery")

    """
    The creepy portrait gallery.

    The paintings seem to be looking at me.

    But besides them, no one in here.
    """

    return


label lad_day3_morning_tea_room:

    $ change_room("tea_room")
    
    """
    Here I am, back in the first room I visited in the manor.

    All the liveliness of that first day is gone.

    Now, it stands silent and empty.
    """

    psychic """
    There's no one in here.

    Let's look elsewhere.
    """

    lad """
    Right, of course.
    """
    
    return

label lad_day3_morning_billiard_room:

    $ change_room("billiard_room")
    
    """
    The billiard room is empty.

    But the drinks remain untouched.

    Perhaps I should have a drink to calm my nerves.
    """

    psychic """
    Mister Harring, you aren't considering drinking at this hour, are you?
    """

    if lad_details.important_choices.is_unlocked('day1_drunk') and lad_details.important_choices.is_unlocked('day2_drunk') :
        
        lad """
        I think a bit of sherry might be beneficial.

        You know,... to settle our nerves.

        Don't you want some?
        """

        psychic """
        Absolutely not!
        """

        lad """
        Alright, suit yourself.
        """

        """
        She gives me a disapproving stare as I pour myself a drink.

        Not wanting to down it too quickly, I decide to take it with me.

        It should help relax me during our exploration.
        """

        # TODO achievement "Drink every chance you got."
        # TODO? "Object drink on hand?"
        $ lad_details.important_choices.unlock('day3_drunk')
    
    else:
        lad """
        Uh, no, of course not.
        """

        """
        That's probably wiser.

        Let's explore further.
        """
    
    return

# Bedrooms
label lad_day3_morning_bedroom_lad:

    """
    There's no need to double-check my room.

    I know what's in there.
    """

    return

label lad_day3_morning_bedroom_nurse:

    $ change_room("bedrooms_hallway")

    psychic """
    This is Miss Marsh's room.
    """

    $ unlock_map("bedroom_nurse")
    
    """ 
    I knock on the door.

    There's no response.
    """

    psychic """
    There's no need for formalities now.

    We should just enter.
    """

    """
    Before I can react, she tries to open the door.
    """

    play sound door_rattling

    psychic """
    It's locked.

    She must have gone out.

    Let's try somewhere else.
    """

    stop sound

    return


label lad_day3_morning_bedroom_captain:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    lad """
    I knock on the door.

    There's no response.
    """

    """
    Before I can say anything, Amelia is already trying the handle.
    """

    play sound door_rattling

    psychic """
    It's locked.

    I believe this is Captain Sinha's room.
    """

    $ unlock_map('bedroom_captain')

    lad """
    He doesn't seem to be here.
    """

    psychic """
    We should continue our search elsewhere.
    """

    stop sound

    return 

label lad_day3_morning_bedroom_host:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    psychic """
    This is Lady Claythorn's room.
    """

    $ unlock_map('bedroom_host')

    lad """
    Miss Claythorn?

    Are you there?
    """

    """
    There's no response.
    """

    """
    Amelia places her hand on the latch and gently opens the door.
    """

    lad surprised """
    What are you doing? We can't just barge in like this!
    """

    """
    But it's too late. She has already stepped inside.

    Reluctantly, I follow her.
    """

    $ change_room('bedroom_host')

    """
    The room is empty. 

    The wardrobe stands open, its contents scattered about the floor.
    """

    psychic """
    It appears she left in haste.
    """

    """
    We search for any clues about what might have happened, but come up empty.
    """

    psychic """
    She's either left the manor or is still hidden somewhere within. 
    
    We shouldn't linger here any longer.
    """
    
    return 

label lad_day3_morning_bedroom_drunk:

    $ change_room("bedrooms_hallway")

    psychic """
    This is Samuel Manning's room.
    """

    $ unlock_map('bedroom_drunk')

    lad """
    Mister Manning?

    Are you in there?
    """

    """
    No answer.
    """

    lad """
    The door's locked anyway.

    Mister Sinha has the key.
    """

    return

label lad_day3_morning_bedroom_psychic:

    $ change_room('bedroom_psychic')

    psychic """
    Why are we in my room?

    Surely you don't think someone's hiding here?
    """

    lad """
    Probably not, but it's wise to be thorough.
    """

    """
    But she is right.

    The room is empty.
    """

    return

label lad_day3_morning_bedroom_doctor:

    $ change_room('bedroom_doctor')

    """
    I'm back in Daniel Baldwin's room.

    His lifeless body still lies on the bed.

    Aside from that, everything seems in order.

    I don't wish to linger here any longer than necessary.
    """

    return

label lad_day3_morning_bedroom_broken:

    $ change_room('bedroom_broken')

    $ unlock_map('bedroom_broken')

    """
    I'm in Thomas Moody's room.

    He is still lying on the bed.

    I see no one else around.

    I should move on.
    """

    return

# 
# Attic
# 
label lad_day3_morning_storage:
    call lad_storage_default
    return

label lad_day3_morning_males_room:
    call lad_males_room_default
    return

label lad_day3_morning_females_room:
    call lad_females_room_default
    return

label lad_day3_morning_butler_room:
    call lad_butler_room_default
    return
