# --------------------------------------------
#   Psychic
#           
#   Saturday - Evening
# 
#   18:30 -> 23h
#
#   Music: sad
#
#   Position
#       - House: Everyone else
#       - Dead : broken, doctor
#
#   Notes : 
#       -  captain generic, lad generic
# --------------------------------------------
label psychic_day2_evening:

    call change_time(18, 30, "Evening", "Saturday")

    $ psychic_details.add_checkpoint("psychic_day2_evening") 

    call black_screen_transition("Amelia Baxter", "Saturday Evening")

    $ change_room("dining_room", irisout)
    
    $ play_music('sad', 3)

    """
    As I step into the dining room, a sombre ambience surrounds me.

    The chairs where Daniel Baldwin and Thomas Moody usually sit are empty.

    Samuel Manning is not here either, obviously.

    I settle into my familiar spot, with Ted Harring to my right.

    Lady Claythorn stands up to speak.
    """

    call common_day2_evening_dinner

    call change_time(21, 00)

    """
    We ate in silence.

    After dinner, most people retired to their rooms.

    I don't think many will join for a drink afterwards.

    So I could also take advantage of the fact that the Manor is almost empty.
    """

    if psychic_details.important_choices.is_unlocked('visit_lad'):
        
        """
        Or I could wait in my room for Ted Harring. 
        """

    else:
        
        """
        Or maybe it's safer to just wait in my room.
        """

    """
    What should I do?
    """

    $ time_left = 60

    call run_menu(psychic_details.saved_variables["day2_evening_map_menu"])

    call change_time(22, 00)

    if time_left <= 0:
        """
        There's no need to wander the house further.

        I should return to my room.
        """

    if psychic_details.important_choices.is_unlocked('visit_lad'):
        
        call psychic_day2_evening_lad_discussion

    else:
        
        """
        With nothing more to do, I quickly fall asleep.
        """

    jump psychic_day3_morning


label psychic_day2_evening_cancel:

    $ change_room('bedroom_psychic')

    """
    There's nothing more I can do right now.

    I'll just go and lie on my bed for a bit.
    """

    call wait_screen_transition()

    return

