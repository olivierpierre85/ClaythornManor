# --------------------------------------------
#   Psychic
#           
#   Saturday - The Hunt
# 
#   11:00 -> 15:00
#
#   Music: chill
#
#   Position
#       - House, Tea room : nurse, psychic
#       - Forest : host, captain,  doctor, drunk, lad
#       - Dead : Broken
#
#   Notes : 
#       - Generic psychic OR map, 240 minutes,?TODO too long?
#       
# --------------------------------------------
label psychic_day2_no_hunt:

    call change_time(11, 00, 'Hunt', 'Saturday')

    $ current_character.add_checkpoint("psychic_day2_no_hunt") 
    
    call black_screen_transition("Amelia Baxter", "The Hunt")

    $ change_room('psychic_room')    

    $ play_music('upbeat')

    """
    I let everyone know that I'm opting out of the hunt.
    
    It turns out Rosalind Marsh is the only one who made the same choice.

    We've agreed to meet shortly for luncheon in the tea room.

    Before that, I went to my quarters to change.

    Now, what should I do next?
    """

    $ time_left = 240 # TODO: Possibly too long; consider revising.

    call run_menu(psychic_details.saved_variables["day2_no_hunt_map_menu"])

    """
    Suddenly, sounds from the main entrance catch my attention.

    I should investigate.
    """

    pause 1.0

    $ stop_music()

    jump psychic_day2_afternoon
    

label psychic_day2_broken_room:

    $ change_room('broken_room')

    $ play_music('sad', 2)

    """
    The doctor left Thomas Moody's room open.

    I guess he didn't think anyone would come to take a look.

    I know I shouldn't have, but I couldn't resist.

    Maybe I didn't believe it.

    But here he lies, dead in his bed.

    I try to look at him, but the emotion is overwhelming.

    I can't stay here any longer.

    I rush out of the room.
    """

    $ unlock_map('broken_room')

    pause 1.0

    $ play_music('PREVIOUS')

    return


label psychic_day2_no_hunt_drunk_room_enter:

    """
    I push the door open quietly, making sure I'm unnoticed.
    """

    play sound door_open

    $ change_room('drunk_room')

    """
    The room is untidy, dim, and reeks of alcohol.

    Clothes are scattered on the floor.

    This must be Samuel Manning's room.
    """

    $ unlock_map('drunk_room')

    """
    I scan the room quickly but only see empty whiskey bottles.

    Honestly, this is just what I expected.

    There's nothing else to do here.
    """

    return


label psychic_day2_no_hunt_nurse_room_busy:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door.
    """

    nurse """
    Yes? Who's there?
    """

    psychic """
    It's Amelia Baxter.
    """

    nurse """
    Oh, Mrs. Baxter, I'm really tired right now. 

    Can you please come back a bit later?
    """

    psychic """
    Of course, sorry for bothering you.
    """
    
    $ unlock_map('nurse_room')
    
    return


label psychic_day2_no_hunt_cancel:

    $ change_room('psychic_room')

    """
    There's nothing more I can do right now.

    I'll just go lie on my bed for a bit.
    """

    call wait_screen_transition()

    return
