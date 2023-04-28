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

    call run_menu(lad_details.saved_variables["day2_no_hunt_map_menu"])

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

label lad_day2_no_hunt_nurse_room_busy:
        
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door.
    """

    nurse """
    Yes? Who is it?
    """

    lad """
    It's Ted Harring.
    """

    nurse """
    Ah, Mr. Harring, I'm afraid I'm quite exhausted at the moment. 
    
    Would you mind coming back later?
    """

    lad """
    Of course not, sorry for bothering you.
    """

    return

label lad_day2_no_hunt_captain_room_enter:

    """
    Making sure no one's watching, I carefully nudge the door open.
    """

    play sound door_open

    $ change_room('captain_room')

    """ 
    The door opens smoothly, allowing me to step inside the room.

    It is extremely neat, with everything in its place.

    Over in a corner, there's a valet stand holding a military uniform.

    It's gotta be Sushil Sinha's room.
    """
    
    $ unlock_map('captain_room')

    """
    Well, since I'm here, I might as well search around a little.
    """

    play sound searching

    $ renpy.pause(5, hard=True)

    $ change_room('captain_room') # TODO add effect same room
    
    """
    I looked around for quite some time.

    I thought I wouldn't find anything until I pulled open the bed drawers.

    There is a gun and a few bullets inside.

    It's not something most people carry, but I guess it's pretty usual for a military person.

    The rest of the room is just plain ordinary.

    I put everything in order and leave.
    """

    return

label lad_day2_no_hunt_drunk_room_enter:

    """
    I sneakily push the door open, making sure nobody is watching me.
    """

    play sound door_open

    $ change_room('drunk_room')

    """
    The bedroom is messy and dimly lit and the smell of alcohol fills the air.

    There are clothes all over the floor.

    I think I can safely say it's Samuel Manning's room.
    """

    $ unlock_map('drunk_room')

    """
    I quickly scan the place but only find empty bottles of whisky.

    Just as I am about to leave, something catches my eye in the fireplace.

    A piece of white paper.

    Curiosity gets the better of me, and I pick it up.

    The writing on the paper is almost entirely burned. 
    
    I can only read some of it.

    There is a first part, written with an impeccable style.    
    """

    call drunk_letter_first_part_burned

    """
    Below that, there is an addition written in an almost indecipherable style:
    """

    call drunk_letter_second_part_burned

    """
    Although I don't understand the meaning behind it, this letter must be important. 
    
    I decide to pocket it just in case.
    """

    $ lad_details.objects.unlock('burned_letter')


    return