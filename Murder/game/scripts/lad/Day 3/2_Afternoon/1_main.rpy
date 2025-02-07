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
    We stayed in the tea room and gathered our strength while Sushil Sinha kept searching the manor.

    When he returned, we had started to feel a bit better.
    """

    $ play_music('mysterious')

    call common_day3_afternoon_lad_psychic_captain_discussion_1

    call common_day3_afternoon_lad_psychic_captain_discussion_2
    
    $ lad_day3_escape_menu = TimedMenu("lad_day3_escape_menu", [
        TimedMenuChoice('Propose to use the old car from the garage {{observation}}', 'lad_day3_leave_with_car', condition="lad_details.important_choices.is_unlocked('seen_car')"),
        TimedMenuChoice('Stay here with Amelia Baxter', 'lad_day3_stay', early_exit=True),
        TimedMenuChoice('Follow Sushil Sinha. Amelia Baxter will {i}probably{/i} be fine on her own', 'lad_day3_escape', early_exit=True)
    ], image_left="psychic",  image_right="captain")

    $ time_left = 1

    call run_menu(lad_day3_escape_menu)

    # TODO: Handle possible endings, add more logic for ending names
    if lad_details.saved_variables["day3_ending"] == "gunned_down":
        jump lad_gunned_down_ending

    elif lad_details.saved_variables["day3_ending"] ==  "poisoned":
        jump lad_ending_day3_poisoned
    
    elif lad_details.saved_variables["day3_ending"] == "fell":
        jump lad_ending_day3_fell

    elif lad_details.saved_variables["day3_ending"] == "escape":  
        jump lad_ending_day3_escape   
    
    elif lad_details.saved_variables["day3_ending"] == "survived":
        # TODO: IF ALL finished UNLOCK NOT AN ENDING BUT LAST PART     
        jump lad_ending_day3_survived    

    return

label lad_day3_leave_with_car:

    lad """
    Wait, we saw an old car in the garage earlier.

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
