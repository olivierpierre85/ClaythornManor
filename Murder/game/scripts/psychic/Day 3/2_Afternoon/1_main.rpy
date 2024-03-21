# --------------------------------------------
#   Psychic
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
label psychic_day3_afternoon:

    call change_time(12,00, "Afternoon", "Sunday")
    
    $ lad_details.add_checkpoint("psychic_day3_afternoon") 

    call black_screen_transition("Amelia Baxter", "Sunday Afternoon")

    $ change_room("tea_room", irisout)

    """
    We waited in the tea room without exchanging any words for a short time.

    Finally, Captain Sinha comes back.
    """

    $ play_music('mysterious')

    call common_day3_afternoon_lad_psychic_captain_discussion

    lad """
    Of course, I'll stay.

    Only a monster would leave you alone here in this condition.
    """

    psychic """
    Thank you Mister Haring! 

    That means the world to me.
    """

    captain """
    Very well.

    I will go right now then. I don't want to lose time.

    Hopefully, I'll be back with help before nightfall.
    """

    psychic """
    Thank you captain.

    I hope you'll be safe.
    """

    lad """
    Yes, thank you.
    """

    """
    And then he was on his way.
    """

    jump work_in_progress
