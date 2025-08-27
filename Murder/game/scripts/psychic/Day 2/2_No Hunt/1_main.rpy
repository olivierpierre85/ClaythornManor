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

    call change_time(11, 00, 'Hunt', 'Saturday', hide_minutes=True, chapter='saturday_afternoon')

    $ current_character.add_checkpoint("psychic_day2_no_hunt") 
    
    call black_screen_transition("Amelia Baxter", chapters_names[current_chapter])

    $ change_room('bedroom_psychic')    

    $ play_music('upbeat')

    """
    I let everyone know that I am opting out of the hunt.
    
    It turns out Rosalind Marsh is the only other one who made the same choice.

    We agreed to meet shortly for luncheon in the tea room.

    I should find her there a bit before noon.
    """
    
    $ time_left = 60
    # TODO add (nobody is here yet) WAIT for NURSE !!
    call run_menu(psychic_details.saved_variables["day2_no_hunt_map_menu"])

    if time_left > 55:

        """
        I don't really feel like exploring the Manor, so I decide to wait in the Tea Room.
        """

    elif time_left >= 10:

        """
        I don't really feel like exploring the Manor any further, so I decide to go wait in the Tea Room.
        """

    else:

        """
        It's almost time for lunch, I should go wait in the Tea Room.
        """

    $ time_left = 60

    call psychic_day2_hunt_tea_room

    call change_time(13, 30)

    """
    What should I do know?
    """

    $ time_left += 90
    call run_menu(psychic_details.saved_variables["day2_no_hunt_map_menu"])

    """
    Suddenly, noises from the main entrance catch my attention.

    I should investigate.
    """

    pause 1.0

    $ stop_music()

    jump psychic_day2_evening
    

label psychic_day2_bedroom_broken:

    $ change_room('bedroom_broken')

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

    $ unlock_map('bedroom_broken')

    pause 1.0

    $ play_music('PREVIOUS')

    $ psychic_details.saved_variables['day2_has_seen_bedroom_broken'] = True

    return


label psychic_day2_no_hunt_bedroom_drunk_enter:

    """
    I push the door open quietly, making sure I'm unnoticed.
    """

    play sound door_open

    $ change_room('bedroom_drunk')

    """
    The room is untidy, dim, and reeks of alcohol.

    Clothes are scattered on the floor.

    This must be Samuel Manning's room.
    """

    $ unlock_map('bedroom_drunk')

    """
    I scan the room quickly but only see empty whiskey bottles.

    Honestly, this is just as I expected.

    There's nothing else to do here.
    """

    return


label psychic_day2_no_hunt_bedroom_nurse_busy:
    
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
    
    $ unlock_map('bedroom_nurse')
    
    return


label psychic_day2_no_hunt_cancel:

    $ change_room('bedroom_psychic')

    """
    There's nothing else I want to do right now.

    I should just lie down on my bed for a bit.
    """

    call wait_screen_transition()

    return

