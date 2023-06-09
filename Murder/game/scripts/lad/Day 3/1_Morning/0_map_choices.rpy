# Downstairs
label lad_day3_first_downstairs:

    if not lad_details.saved_variables["day3_downstairs_visited"]:

        $ change_room("basement_stairs")

        """
        I take the stairs to the basement, expecting to be stopped at any moment.

        But there is nobody.

        I can safely explore downstairs now.
        """

        $ lad_details.saved_variables["day3_downstairs_visited"] = True

    return


label lad_day3_morning_kitchen:

    call lad_day3_first_downstairs

    $ change_room('kitchen')

    """
    I reach the kitchen.

    I guess it's a regular kitchen for a house of that size.

    There are pots and pans laying around.
    """
        
    psychic """
    You see.

    There is no one here.

    Even though breakfast should be ready soon.
    """

    lad """
    Ok I admit that is very strange indeed.
    """

    """
    We look around a little but can't find anything of interest.
    """
    
    return

label lad_day3_morning_gun_room:

    call lad_day3_first_downstairs

    $ change_room('gun_room')

    """
    The gun room is a bit intimidating.

    So much firepower for just one household.

    It's making me uneasy.
    """

    lad """
    Nobody is here.
    """

    psychic """
    No indeed.

    But it might be useful to get a weapon for protection you don't think?
    """

    """
    Well, I don't have a lot of experience with guns.

    It might be a bad idea.

    But on the other hand, I don't know what we might encounter today.
    """

    call run_menu(TimedMenu([
        TimedMenuChoice('Sure, I need a gun. It doesn\'t matter that I don\'know how to use it', 'lad_day3_take_gun', early_exit=True),
        TimedMenuChoice('I would rather not. I could hurt myself.', 'lad_day3_no_gun', early_exit=True), 
    ]))

    return

label lad_day3_take_gun:

    lad """
    You are right.

    We better get something to defend ourselves.
    """

    """
    Hunting rifles are a bit too large.

    But I spot a revolver that fits my pocket.
    """

    lad """
    Alright, I'll take this with me.

    But there are no bullets in it.
    """

    psychic """
    Sometimes, bullets are being kept separated from the guns.

    It makes it less likely to have an accident.
    """

    lad """
    Where could they be then?
    """

    psychic """
    No idea.

    But even empty, the gun can still scare away someone.
    """

    """
    I guess.

    But it's not very reassuring.
    """

    $ lad_details.objects.unlock('gun')

    return

label lad_day3_no_gun:

    lad """
    No I don't think so.

    We might end up hurting ourselves.
    """

    psychic """
    Alright, if that is what you want.
    """

    return

label lad_day3_morning_scullery:

    call lad_day3_first_downstairs

    $ change_room('scullery')

    """
    Wait, what the hell is a scullery?
    """

    lad """
    Do you know what room this is?
    """

    psychic """
    The scullery.

    That's mainly where they wash the dishes.

    If you look down the sink full, there are a lot of dirty dishes.
    
    It seems nobody cleaned after supper yesterday.
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

    That's where lady Claythorn car should be.

    But instead there is only parts of other cars and an old model in a shabby state.
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
    Yeah me too.
    """

    lad """
    But if everyone has left, we might need it if we want to reach the next town.
    """

    psychic """
    Right. But do you know how to drive that?

    Because I sure can't.
    """

    $ psychic_details.unlock_knowledge('drive')

    lad """
    Not really, no.

    I never learn how to drive.
    """

    """
    It's not like I could afford a car anyway.
    """

    $ lad_details.unlock_knowledge('drive')

    $ lad_details.saved_variables["day3_seen_car"] = True

    return


# First Floor
label lad_day3_morning_library:

    $ change_room("library")
    
    """
    We enter the small library and found it empty.

    There is no room for anyone to hide in here.

    Let's move on.
    """
    
    return

label lad_day3_morning_dining_room:

    $ change_room("dining_room")

    lad """
    Nobody seems to be here.
    """

    psychic """
    And the table is not set for breakfast either.

    That's not normal.
    """

    return

label lad_day3_morning_garden:

    $ change_room('manor_garden')
    
    """
    We go out to explore the garden.

    But there is no trace of anyone.

    Lady Claythorn car is not there either.

    I try to shout to attract attention.
    """

    lad """
    HELLO ! Is anyone here ?

    HELLO !!
    """

    """
    No response.
    """

    psychic """
    I don't think we need to break our lungs.

    If someone is here we will find them.
    """

    """
    Oh, was shouting not appropriate ?

    I guess she will always think about decorum, no matter the situation.

    Let's go back inside then.
    """

    return

label lad_day3_morning_meeting_captain:

    captain """
    At last, living, breathing souls.

    I was starting to feel like I was in a ghost house.
    """

    psychic """
    Same here, you are the first person we've bumped into today too.
    """

    lad """
    Do you have a clue about what's going on?
    """

    captain """
    Nothing solid. All I know is I don't like it.
    
    People don't just up and leave their homes for no reason.
    """

    psychic """
    They sure don't.
    """

    captain """
    And then there's the matter of the suspicious deaths.

    I could have shrugged them off as bad luck yesterday, but now... now I'm not so sure.
    """

    """
    The conversation hangs in the air, a heavy silence stretching between us.
    """

    return

label lad_day3_morning_entrance_hall:

    $ change_room("great_hall")
    
    """
    The entrance hall is usually the heart of the house.

    But there is no any activity today.

    Just in case, I try to call for someone.
    """

    lad """
    Is there anyone here?
    """

    """
    I didn't really expect an answer.

    But an authoritative voice comes from up the stairs.
    """

    captain """
    Who goes there?
    """

    lad """
    It's Ted Harring. I'm down here, and Amelia Baxter's with me.
    """

    captain """
    Understood. I'm making my way down.
    """

    """
    Soon enough, Captain Sinha steps into view, descending the staircase to join us on the ground floor.
    """

    call lad_day3_morning_meeting_captain

    psychic """
    Staying put isn't going to shed any light on this,
    
    We need to keep exploring the house.
    """

    captain """
    Agreed. Now should we keep looking together?
    """

    psychic """
    Thank you, but... maybe it would be better to split up. 
    
    We'd cover more ground that way.
    """

    """
    Amelia seemed nervous when she answered.
    """

    captain """
    Makes sense. Let's venture on our own and meet up later. 

    How about the tea room?
    """

    psychic """
    That's a good spot.

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
    Here I am back in the first room I visited in the manor.

    There is nothing left of the liveliness of that first day.

    Now it stands silent and empty.
    """

    psychic """
    No one is in here.

    Let's look somewhere else.
    """

    lad """
    Right, of course
    """
    
    return

label lad_day3_morning_billiard_room:

    $ change_room("billiard_room")
    
    """
    The billiard room is empty.

    But the drinks are still there.

    Maybe I should have a drink to calm down.
    """

    psychic """
    Mister Harring, you are not thinking of drinking at this hour do you?
    """

    if lad_details.saved_variables["day1_drunk"] and lad_details.saved_variables["day2_drunk"]:
        
        lad """
        I think a bit of sherry would do us good.

        You know,... to settle our nerves.

        Don't you want one?
        """

        psychic """
        Certainly not!
        """

        lad """
        Alright suits yourself.
        """

        """
        She gives me a stare full of anger as I pulling myself a drink.

        I don't want to drink it too fast, so I take it with me.

        Now I will be more relaxed for our exploration.
        """

        # TODO achievement "Biggest drunkard" "You drank every occasion you had"
    
    else:
        lad """
        Hum, no of course not.
        """

        """
        It's probably wiser anyway.

        Let's explore somewhere else
        """
    
    return

# Bedrooms
label lad_day3_morning_lad_room:

    """
    No need to double check my room.

    I know what's there.
    """

    return

label lad_day3_morning_nurse_room:

    $ change_room("bedrooms_hallway")
    
    """ 
    I knock on the door.

    Nobody answers.
    """

    psychic """
    No need for formalities.

    We better just try to enter.
    """

    """
    And before I could say anything, she opens the door.
    """

    $ change_room("nurse_room")

    psychic """
    I believe it's Miss Marsh's Room.
    """

    $ unlock_map("nurse_room")

    psychic """
    She is not here.

    And the room is neatly ordered.

    No sign of struggle or hurry here.
    """

    lad """
    Where could she be?
    """

    psychic """
    I don't know.

    This place is not that big.

    We should have run into her.
    
    In any case, let's look around.

    There might some clue on where she could be.
    """

    pause 1.0
    
    """
    We looked for a while but found nothing of interest.
    """

    return


label lad_day3_morning_captain_room:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    lad """
    No answers.
    """

    """
    Before I could say anything, Amelia was already trying to open it.
    """

    play sound door_rattling

    psychic """
    It's closed.

    I believe it's captain sinha room.
    """

    $ unlock_map('captain_room')

    psychic """
    But he is obviously not here.
    """

    return 

label lad_day3_morning_host_room:

    $ change_room("bedrooms_hallway")

    play sound door_knock

    psychic """
    This is Lady Claythorn's Room.
    """

    $ unlock_map('host_room')

    lad """
    Miss Claythorn?

    Are you there?
    """

    """
    There is no response.
    """

    # psychic """
    # I told you she was not there.
    # """

    """
    Then, she put her on hand on the clutch.

    The door opens.
    """

    lad surprised """
    What are you doing? 

    We can't enter like that!
    """

    """
    But it's too late. She's already rushed inside.

    I have no choice but to follow her.
    """

    $ change_room('host_room')

    """
    It's empty.

    The wardrobe is wide open. There are some clothes on the floor.
    """

    psychic """
    It looks like she left in a hurry.
    """

    """
    We looked for a clue of what happened but found nothing.
    """

    psychic """
    Well, she either have left, or she is still hiding somewhere in the manor.

    There is no need to dwell here any longer.
    """
    
    return 

label lad_day3_morning_drunk_room:

    $ change_room("bedrooms_hallway")

    psychic """
    It's Samuel Manning room.
    """

    $ unlock_map('drunk_room')

    lad """
    Mister Manning?

    Are you alright?
    """

    """
    No answer.
    """

    lad """
    Well the door is closed anyway.

    Mister Sinha has the key.
    """

    return

label lad_day3_morning_psychic_room:

    $ change_room('psychic_room')

    psychic """
    What are you doing in my room?

    You don't think someone is hiding here?
    """

    lad """
    Probably not, but it's better to be thorough.
    """

    """
    But she is right.

    There is nothing or nobody here.
    """

    return

label lad_day3_morning_doctor_room:

    $ change_room('doctor_room')

    """
    I am back in Daniel Baldwin room.

    His body is still on the bed.

    Besides there is nothing else out of the ordinary.

    I don't want to dwell here more then I have to.
    """

    return

label lad_day3_morning_broken_room:

    $ change_room('broken_room')

    $ unlock_map('broken_room')

    """
    Thomas Moody's room.

    He is still lying on the bed.

    But I don't see anyone else here.

    No need to stay longer.
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