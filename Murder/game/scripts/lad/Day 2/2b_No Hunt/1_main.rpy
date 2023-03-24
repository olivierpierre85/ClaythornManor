# --------------------------------------------
#   Lad
#           
#   Saturday - The Hunt
# 
#   11:00 -> 15:00
#
#   Music: chill
#
#   Position
#       - House, Tea room : nurse, psychic, lad
#       - Forest : host, captain,  doctor, drunk
#       - Dead : Broken
#
#   Notes : 
#       - Generic psychic OR map, 120 minutes,?TODO too long?
#       
# --------------------------------------------
label lad_day2_no_hunt:

    call change_time(11,00, 'Hunt', 'Saturday')

    $ current_character.add_checkpoint("lad_day2_no_hunt") 
    
    call black_screen_transition("Ted Harring", "The Hunt")

    $ change_room('lad_room')

    

    $ play_music('upbeat')

    """
    I turned down the invitation for the hunt.

    So I am staying inside with Amelia Baxter and Rosalind Marsh.

    They are in the tea room, waiting for a small luncheon to be served.

    I retreated in my room to change.

    Now what should I do?
    """

    $ time_left = 240 # TODO too long do something

    call run_menu(lad_details.saved_variables["map_menu"])

    """
    Suddenly, I hear noises from the entrance hall.
    
    I decide to go and see what's happening.
    """

    $ stop_music()

    jump lad_day2_afternoon
    

label lad_day2_broken_room:

    $ change_room('broken_room')

    $ play_music('sad', 2)

    if lad_details.saved_variables["day2_breakfast_follow"]:

        """
        The poor man is still there. I don't think he moved.
        """

    else:

        """
        I don't know what kind of macabre feeling made me come here.

        But in case I had doubts, Thomas Moody is there. Not breathing.

        Gosh.
        """

    """
    Well, now that I am here. Maybe I should take a look quickly. 

    Something might help me understand what happened.

    So I look around the room.

    I don't see nothing of the ordinary.

    He seems peaceful in his sleep.

    His mask is still on. 
    
    The doctor didn't even remove it to examine him.

    Well, if the doctor didn't, I certainly won't either.

    On a chair next the the bed are his clothes, meticulously folded.

    There is a whisky flask on the night stand.

    It's on its side, empty.

    Next to it is a stain. 
    
    I suppose it should be whisky, but it has a weird colour.

    A light shade of green.

    That's strange.

    What could it be?

    That's all I could notice in the room.
    """

    $  lad_details.observations.unlock('green_liquid') # TODO link to billiard room option to not drink the whisky?

    pause 1.0
    # TODO add sound for CLUE???
    # TODO FIRST REAL INVESTIGATiON CLUE? ADD INTUITION when come back to 

    $ play_music('PREVIOUS')

    return


label lad_day2_no_hunt_cancel:

    $ change_room('lad_room')

    """
    I don't think there is anything interesting to do now.

    So I will lay on my bed for while.
    """

    call wait_screen_transition()

    return