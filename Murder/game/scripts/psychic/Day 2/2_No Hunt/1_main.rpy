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
#       - Generic psychic OR map, 120 minutes,?TODO too long?
#       
# --------------------------------------------
label psychic_day2_no_hunt:

    call change_time(11,00, 'Hunt', 'Saturday')

    $ current_character.add_checkpoint("psychic_day2_no_hunt") 
    
    call black_screen_transition("Amelia Baxter", "The Hunt")

    $ change_room('psychic_room')    

    $ play_music('upbeat')

    """
    I explained to everyone I wouldn't go on the hunt with them.
    
    Only Rosalind Marsh made the same choice.

    We are supposed to meet in a little while for a luncheon in the tea room.

    I went to my room to change.

    What should I do next?
    """

    $ time_left = 240 # TODO: Possibly too long; consider revising.

    call run_menu(psychic_details.saved_variables["day2_no_hunt_map_menu"])

    """
    I hear sounds from the entrance.

    I decide to check it out.
    """

    $ stop_music()

    jump psychic_day2_afternoon
    

label psychic_day2_broken_room:

    $ change_room('broken_room')

    $ play_music('sad', 2)

    # """
    # I don't know what morbid curiosity led me here.

    # But, if I had any doubts, Thomas Moody is there, lifeless.

    # Gosh.
    # """

    # """
    # Now that I'm here, perhaps I should take a quick look.

    # There might be something that helps me understand what happened.

    # I look around the room.

    # Nothing seems out of the ordinary.

    # He looks peaceful.

    # His mask is still on. 
    
    # The doctor didn't even remove it for the examination.

    # Well, if the doctor didn't, I certainly won't either.

    # On a chair next to the bed, his clothes are meticulously folded.

    # There's a whiskey flask on the nightstand.

    # It's on its side, empty.

    # Next to it is a stain. 
    
    # I suppose it's whiskey, but it's an odd shade of green.

    # That's peculiar.

    # What could it be?

    # That's all I notice in the room.
    # """

    # $ psychic_details.observations.unlock('green_liquid') # TODO: Link to billiard room option not to drink the whiskey?

    # pause 1.0

    $ play_music('PREVIOUS')

    return

label psychic_day2_no_hunt_cancel:

    $ change_room('psychic_room')

    """
    There's nothing more I can do right now.

    I'll just go lie on my bed for a bit.
    """


    call wait_screen_transition()

    return