# --------------------------------------------
#   Lad
#           
#   Sunday - Afternoon
# 
#   12:00 -> Ending
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic
#       - Dead : broken, doctor, drunk
#       -? : Host, nurse
#
#   Notes : 
#       - 
# --------------------------------------------
label lad_day3_afternoon:

    call change_time(12,00, "Afternoon", "Sunday")
    
    $ lad_details.add_checkpoint("lad_day3_afternoon") 

    call black_screen_transition("Ted Harring", "Sunday Afternoon")

    $ change_room("tea_room", irisout)

    """
    After leaving us in the tea room to gather our strength, Sushil Sinha left to explore the mansion further.

    When he returned, we were starting to feel a bit better.
    """

    $ play_music('mysterious')

    captain """
    I just tried the phone, and it's not working.

    We can't call for help.

    I believe we don't have a choice but to leave this place.

    The longer we stay, the more at risk we are.
    """

    psychic """
    But... shouldn't we wait for the police?

    They were expected today. They could arrive any moment.
    """

    captain """
    I wouldn't count on it.

    From what I gather, there's no evidence that the police were called yesterday.
    """

    psychic """
    But Miss Claythorn said...
    """

    """
    She stops mid-sentence, realizing the implication.
    """

    psychic """
    So you believe they never called.

    That the police have no idea about what's happened here.

    She lied to us.
    """

    captain """
    That's the most logical explanation.

    No one was around when the phone calls were supposedly made.

    So, there's no way to verify if they actually happened.
    """

    lad """
    But why?

    Why would anyone do this?

    I don't understand what's happening.
    """

    captain """
    Neither do I.

    I've thought about it, and I have no clue why we were all invited here.

    I'm sure it wasn't to give us any money.

    In any case, all I know is we need to leave as soon as possible.
    """

    psychic """
    But how?

    The nearest town is miles away.

    I can't walk that far. 

    And even if I could, I'm not prepared for such a journey.
    """

    """
    Captain Sinha and I consider this for a moment.
    """

    captain """
    You might be right.

    It would be a long walk, and the weather might turn at any moment.

    We could get caught in another storm.

    It's probably unsafe for you to join us.
    """

    psychic surprised """
    But you're not going to leave me here alone, are you?

    What would become of me?
    """

    captain """
    We could lock you in a room.

    Though, that's far from ideal.

    Maybe one of us should stay with you.
    """

    psychic """
    Yes!

    Mister Harring can stay with me, right?

    The two of us should be safe until you return with help.
    """

    captain """
    That seems to be the wisest choice.

    What do you think, Mister Harring?
    """
    
    $ lad_day3_escape_menu = TimedMenu("lad_day3_escape_menu", [
        TimedMenuChoice('We could use the old car from the garage {{observation}}', 'lad_day3_leave_with_car', condition='lad_details.saved_variables["day3_seen_car"]'),
        TimedMenuChoice('Stay here with Amelia Baxter', 'lad_day3_stay', early_exit=True),
        TimedMenuChoice('Follow Sushil Sinha. Amelia Baxter will {i}probably{/i} be fine on her own', 'lad_day3_escape', early_exit=True)
    ], image_left="psychic",  image_right="captain")

    $ time_left = 1

    call run_menu(lad_day3_escape_menu)

    # TODO: Handle possible endings, add more logic for ending names
    if lad_details.saved_variables["day3_ending"] == "gun_downed":
        jump lad_gun_downed_ending

    elif lad_details.saved_variables["day3_ending"] ==  "poisoned":
        jump lad_ending_day3_poisoned
    
    elif lad_details.saved_variables["day3_ending"] == "fell":
        jump lad_ending_day3_fell

    elif lad_details.saved_variables["day3_ending"] == "escape":
        # TODO: IF ALL finished UNLOCK NOT AN ENDING BUT LAST PART     
        jump lad_ending_day3_escape   
    
    elif lad_details.saved_variables["day3_ending"] == "survived":
        # TODO: IF ALL finished UNLOCK NOT AN ENDING BUT LAST PART     
        jump lad_ending_day3_survived    

    return

label lad_day3_leave_with_car:

    lad """
    Wait, there's still a car in the garage.

    We saw it earlier. It's an old model.

    We don't know how to drive it, but perhaps you do?
    """

    captain """
    I can drive, yes.

    I saw the car you're talking about.

    I even tried to start it, but no luck.

    I don't think it's broken; it's probably just out of gas.

    I couldn't find any in the garage.

    So, I'm afraid that car won't be much help.

    Unless either of you spotted a jerrycan somewhere in the mansion?
    """

    lad """
    No, I haven't.
    """

    psychic """
    Neither have I.
    """

    captain """
    That's unfortunate.

    It seems we have no choice but to proceed on foot.
    """

    return
