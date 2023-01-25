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
    After leaving us in the tea room to gather our strength, Sushil Sinha left to explore the mansion a bit more.

    When he came back, we were starting to feel a bit better.
    """

    $ play_music('mysterious')

    captain """
    I just tried the phone, it's not working.

    So we can't call for help.

    I don't think we have a choice, we have to leave this place.

    The longer we stay here the more we are at risk something will happen to us.
    """

    psychic """
    But,... shouldn't we wait for the police?

    They were supposed to come here today, they might arrive any moment.
    """

    captain """
    I wouldn't count on it.

    For what I understand, there is no proof anyone called the police yesterday.
    """

    psychic """
    But Miss Claythorn she said...
    """

    """
    She stops mid sentence, realizing the implication.
    """

    psychic """
    So you think they never called.

    That the police has no idea what has happened here.

    Those were just lies she told us.
    """

    captain """
    That's the most logical explanation for me.

    Nobody was around when the phone calls were made.

    So there is no way to know if they actually happened.
    """

    lad """
    But why?

    What would they want to do something like this?

    I don't understand what is happening.
    """

    captain """
    Me neither.

    I tried thinking about it an I have no idea why we were all asked to come here.

    But I know that was not to give us any money.

    In any case, all I know is we better leave this place as soon as possible.
    """

    psychic """
    But how?

    We are miles from the next town.

    I can't walk that far. 
    
    And even if I could do it physically, I am not equipped for it.
    """

    """
    Captain Sinha and I consider this for a while.
    """

    captain """
    Maybe you are right.

    It's gonna be a long walk, and the weather could turn any minute.

    We could be caught in an another storm.

    It's probably not safe for you to come with us.
    """

    psychic surprised """
    But you are not gonna leave me alone here?!

    What will happen to me?
    """

    captain """
    We could lock you in a room.

    But that's not ideal of course.

    It might be best that one of us stays with you here.
    """

    psychic """
    Yes !

    Mister Harring can stay here with me right!

    The two of us will be safe until you return with some help.
    """

    captain """
    This is perhaps the wisest choice.

    What do you think Mister Harring?
    """
    
    $ lad_day3_escape_menu = TimedMenu([
        TimedMenuChoice('We could take the old from the garage {{observation}}', 'lad_day3_leave_with_car', condition= 'lad_details.saved_variables["day3_seen_car"]'),
        TimedMenuChoice('Stay here with Amelia Baxter', 'lad_day3_stay', early_exit = True ),
        TimedMenuChoice('Follow Sushil Sinha. Amelia Baxter will {i}probably{/i} be fine on her own', 'lad_day3_escape', early_exit = True)
    ], image_left = "psychic",  image_right = "captain")

    $ time_left = 1

    call run_menu(lad_day3_escape_menu)

    # TODO handle possible endings, add switch on the  more logic in ending names
    if lad_details.saved_variables["day3_ending"] == "gun_downed":

        jump lad_gun_downed_ending

    elif lad_details.saved_variables["day3_ending"] ==  "poisoned":

        jump lad_ending_day3_poisoned
    
    elif lad_details.saved_variables["day3_ending"] == "fell":

        jump lad_ending_day3_fell

    elif lad_details.saved_variables["day3_ending"] == "escape":
        #TODO  IF ALL finished UNLOCK NOT AN ENDING BUT LAST PART     
        jump lad_ending_day3_escape   
    
    elif lad_details.saved_variables["day3_ending"] == "survived":
        #TODO  IF ALL finished UNLOCK NOT AN ENDING BUT LAST PART     
        jump lad_ending_day3_survived    

    return

label lad_day3_leave_with_car:

    lad """
    Wait, there is still a car in the garage.

    We went there earlier and saw an old car.

    Maybe it's still working.

    We don't know how to drive it, but maybe you do?
    """

    captain """
    I can drive yes.

    And I saw the car you mentioned too.

    I even tried to start it.

    No luck.

    I don't think anything is wrong with it. It's probably out of gas.

    But I couldn't find any in the garage.

    So I am afraid this car won't be of any use to us.

    Unless you saw a jerrycan somewhere else in the house?
    """

    lad """
    No. No I didn't.
    """

    psychic """
    Me neither.
    """

    captain """
    Too bad.

    We don't have a choice but to leave on foot then.
    """

    return
