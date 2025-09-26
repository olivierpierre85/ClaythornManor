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

    call change_time(12,00, "Afternoon", "Sunday", hide_minutes=True, chapter='sunday_afternoon')
    
    $ psychic_details.add_checkpoint("psychic_day3_afternoon") 

    call black_screen_transition("Amelia Baxter", chapters_names[current_chapter])

    $ change_room("tea_room", irisout)

    """
    We waited in the tea room without exchanging any words for a short time.

    Finally, Captain Sinha comes back.
    """

    $ play_music('mysterious')

    call common_day3_afternoon_lad_psychic_captain_discussion_1
    
    if psychic_details.endings.is_unlocked('burned'):

        """
        Leave? I can't leave.

        Yet something doesn't feel right. 
        
        I have a terrible premonition about this place.
        
        I can see it... burning.
        
        Gosh, it's like I can smell it too.

        What's happening to me? Am I losing my mind?

        I know it makes no sense to go out right now, but everything in my body compels me to leave this place as fast as possible.
        """

        $ time_left = 1
        call run_menu( TimedMenu("psychic_day3_stay", [
            TimedMenuChoice("Let's not take any chance and leave this place{{intuition}}", 'psychic_day3_afternoon_escape', early_exit=True),        
            TimedMenuChoice("I am not going out in these clothes", 'common_day3_afternoon_lad_psychic_captain_discussion_2', early_exit=True),
            ])
        )        

    else:
        
        call common_day3_afternoon_lad_psychic_captain_discussion_2

    lad """
    Of course, I'll stay.

    Only a monster would leave you alone here in this condition.
    """

    psychic normal """
    Thank you Mr Haring! 

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

