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
#       - Generic psychic OR map
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

    And I could take the opportunity that most people are outside to "look" more intensively into this place.

    Obviously, the priority would be to find the stash of money promised to everyone.

    But, if as I suspect, there isn't any, I am sure I can find other valuables.
    """

    if nurse_details.threads.is_unlocked('steal_cutlery_1') or nurse_details.threads.is_unlocked('steal_cutlery_2'):

        """
        I already secured some silverware.
        
        A rather risky thing to do.

        That may not help me much, but it's still something.
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
    I rested a while, I need to get some strength if I want to get through the day.
    """

    call change_time(14, 0)

    call wait_screen_transition()

    """
    After a little while, I am starting to feel better.

    Perhaps I can use the remaining time productively.
    """

    $ time_left = 60
    call run_menu(nurse_details.saved_variables["day2_no_hunt_map_menu"])

    """
    A commotion from the entrance hall draws my attention.

    It seems the hunting party has returned.
    """

    pause 1.0

    $ stop_music()

    jump nurse_day2_evening


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

    But I'll join you for luncheon.

    Might we speak then?
    """

    nurse """
    Of course.
    """
    
    $ unlock_map('bedroom_psychic')
    
    return

label nurse_search_psychic_caught:

    $ change_room("bedroom_psychic")

    """
    The room has a heavy, sweet scent to it. Something thick, like incense or dried lavender.

    A deck of unusual cards is spread across the dressing table.

    Several books on spiritualism and the occult are stacked carelessly by the bed.

    I look through the drawers, but find only clothes and more peculiar trinkets.

    There is nothing of real value here.
    """

    $ unlock_map('bedroom_psychic')

    """
    I am about to leave when I hear footsteps in the corridor.

    The door opens.
    """

    play sound door_open

    psychic """
    Oh —
    """

    """
    Mrs Baxter stops in the doorway. Her eyes move slowly across the room, then settle on me.
    """

    nurse """
    Mrs Baxter. Forgive me — I have made a dreadful mistake. I thought this was my room.
    """

    """
    A brief silence. I hold her gaze steadily.
    """

    psychic """
    Your room.
    """

    nurse """
    The corridor all looks rather alike at this end. I am sorry to have disturbed you. I shall leave you to rest.
    """

    psychic """
    Yes. I came back to lie down for a short while.
    """

    """
    She does not move from the doorway. Her expression is difficult to read — polite enough on the surface, but there is something watchful underneath.
    """

    psychic """
    It is curious, though.

    I am quite certain I locked the door when I left this morning.
    """

    """
    She says it lightly, almost to herself. But her gaze does not leave me.
    """

    nurse """
    Perhaps the latch did not catch properly. These old doors can be unreliable.
    """

    psychic """
    Perhaps.
    """

    """
    I step past her into the corridor, keeping my pace unhurried.

    She watches me go.

    She is not a fool.

    Whatever she thinks now, she will be watching me more carefully from this moment on.
    """

    $ nurse_details.threads.unlock('spotted_by_psychic')

    return


label nurse_day2_no_hunt_cancel:

    $ change_room('bedroom_nurse')

    """
    I have no desire to wander further for the time being.

    I shall stay in my room and rest until the others return.
    """

    call wait_screen_transition()

    return
