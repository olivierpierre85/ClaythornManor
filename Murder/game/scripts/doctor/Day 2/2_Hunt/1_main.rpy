# --------------------------------------------
#   Doctor
#           
#   Saturday - The Hunt
# 
#   11:00 -> 15:00
#
#   Music: upbeat
#
#   Position
#       - House, Tea room : nurse, psychic 
#       - Forest : host, captain, lad, doctor, drunk
#       - Dead : Broken
#
#   Notes : 
#       - Generic lad, 30 minutes
# --------------------------------------------
label doctor_day2_hunt:

    $ current_character.add_checkpoint("doctor_day2_hunt") 

    call change_time(11,00, 'The Hunt', 'Saturday', chapter='saturday_afternoon')

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])
    
    $ change_room("gun_room")

    $ play_music('upbeat', 1, fadein_val=10.0)

    $ change_room('manor_garden')

    """
    Since I could not muster a reason to stay behind, I changed for the hunt.

    Luckily I had thought of taking outdoor close for this week-end.

    It was not hard to imagine a shoot was to be on the agenda.

    It's funny how Lady Claythorn pretends it's for our benefit, when mostly she will enjoy it the most.

    I don't think she can easily find hunting partners here in this isolated place.
    
    Anyway, I have a gun, and even though it's been a while, I think I can still manage how to use it.

    I go outside to join everybody else.

    In addition to our little group, I can spot the butler and the footman.

    They will likely come to help us.
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        d
        """

    jump work_in_progress