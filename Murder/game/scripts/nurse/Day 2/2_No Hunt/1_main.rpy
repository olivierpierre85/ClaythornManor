# --------------------------------------------
#   Nurse
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
#       - Generic nurse OR map, 240 minutes,?TODO too long?
#       
# --------------------------------------------
label nurse_day2_hunt:

    call change_time(11, 00, 'The Hunt', 'Saturday', hide_minutes=True, chapter='saturday_afternoon')

    $ current_character.add_checkpoint("nurse_day2_hunt") 
    
    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room('bedroom_nurse')

    $ play_music('chill')

    """
    I am quite content to remain behind.

    A trudge across broken ground in the damp is precisely what I must avoid.

    I should perhaps rest, or find a quiet corner of the house to sit.
    """

    $ time_left = 60
    call run_menu(nurse_details.saved_variables["day2_no_hunt_map_menu"])

    pause 1.0

    $ stop_music()

    jump nurse_day2_evening


label nurse_day2_bedroom_broken:

    $ change_room('bedroom_broken')

    $ play_music('sad', 2)

    """
    Mr Moody's room.

    There is a distinct finality to a room once its occupant is gone.

    I have seen it many times before.

    I should not linger here. It serves no purpose.
    """

    $ unlock_map('bedroom_broken')

    pause 1.0

    $ play_music('PREVIOUS')

    $ nurse_details.saved_variables['day2_has_seen_bedroom_broken'] = True

    return


label nurse_day2_no_hunt_bedroom_psychic_busy:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock politely on the door.
    """

    psychic """
    Yes? Who is there?
    """

    nurse """
    It is Rosalind Marsh.
    """

    psychic """
    Oh, Miss Marsh, I am resting my eyes just now. 

    Could we perhaps speak later?
    """

    nurse """
    Certainly. I shall leave you to it.
    """
    
    $ unlock_map('bedroom_psychic')
    
    return


label nurse_day2_no_hunt_cancel:

    $ change_room('bedroom_nurse')

    """
    I have no desire to wander further for the time being.

    I shall stay in my room and rest until the others return.
    """

    call wait_screen_transition()

    return
