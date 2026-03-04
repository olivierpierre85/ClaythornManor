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

    It will allow me to rest.

    Even though I should at least join Mrs Baxter for lunch.

    And I could take the opportunity that most people are outside to "look" for treasure.

    The priority would be to find the stash of money promised to everyone.

    But, if as I suspect, there isn't any, I am sure I can find other valuables in here.

    Once I feel I have found enough, I might be able to leave early and avoid any suspicion.
    """

    if nurse_details.threads.is_unlocked('steal_cutlery_1') or nurse_details.threads.is_unlocked('steal_cutlery_2'):

        """
        I already secured some silverware.
        
        But that may not help me much, and it was a rather risky thing to do.

        Perhaps I ought to curb such impulsive behaviour if I do not wish to be caught.
        """


    $ time_left = 60
    call run_menu(nurse_details.saved_variables["day2_no_hunt_map_menu"])

    if time_left <= 0:

        """
        I pushed myself again.
        
        No cough this time but I should still be more careful, there is no need to explore until I collapse.
        """

    if not nurse_details.saved_variables.get('day2_hunt_tea_room_early', False):

        """
        It is almost noon. I should not keep Mrs Baxter waiting any longer.
        """

    $ time_left = 60

    call nurse_day2_hunt_tea_room

    $ change_room("bedroom_nurse", dissolve)

    """
    I lay for a bit, I need to get some strength if I want to get through the day.
    """

    call change_time(14, 0)

    call wait_screen_transition()

    """
    After a little while, I am starting to feel better.

    Perhaps I can use the remaining time productively.
    """

    $ time_left += 60
    call run_menu(nurse_details.saved_variables["day2_no_hunt_map_menu"])

    """
    A commotion from the entrance hall draws my attention.

    It seems the hunting party has returned.
    """

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
    Oh, Miss Marsh, I am resting my eyes at present.

    Might we speak a little later?
    """

    nurse """
    Of course. Do not disturb yourself on my account.
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
