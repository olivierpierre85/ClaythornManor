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

    call common_day3_afternoon_lad_psychic_captain_discussion_1
    
    """
    WHATTTTT
    """
    
    if psychic_details.intuitions.is_unlocked('leave_castle'):

        """
        Something isn't right.

        I can feel it.

        I know it makes no sense to go out right now, but something compels me to get out of here immediately.
        """

        $ time_left = 1
        call run_menu( TimedMenu("psychic_day3_stay", [
            TimedMenuChoice("Let's not take anymore risk and leave this place", 'psychic_day3_afternoon_escape', early_exit=True),        
            TimedMenuChoice("I am not going out in this weather", 'common_day3_afternoon_lad_psychic_captain_discussion_2', early_exit=True),
            ])
        )        

    else:
        call common_day3_afternoon_lad_psychic_captain_discussion_2

    lad """
    Of course, I'll stay.

    Only a monster would leave you alone here in this condition.
    """

    psychic normal """
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
    And then he is on his way.
    """

    jump psychic_day3_afternoon_stay

