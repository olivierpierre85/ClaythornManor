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
#       - Generic psychic OR map, 240 minutes,?TODO too long?
#       
# --------------------------------------------
label lad_day2_no_hunt:

    call change_time(11,00, 'No Hunt', 'Saturday', chapter='saturday_afternoon_no_hunt')

    $ current_character.add_checkpoint("lad_day2_no_hunt") 
    
    call black_screen_transition("Ted Harring", chapters_names[current_chapter])

    $ change_room('bedroom_lad')    

    $ play_music('upbeat')

    """
    I turned down the invitation for the hunt.

    So, I'm staying inside with Amelia Baxter and Rosalind Marsh.

    They are in the tea room, waiting for a small luncheon to be served.

    Now, what should I do?
    """

    $ time_left = 240 # TODO: Possibly too long; consider revising.

    call run_menu(lad_details.saved_variables["day2_no_hunt_map_menu"])

    """
    Suddenly, I hear noises from the entrance hall.
    
    I decide to see what's happening.
    """

    $ stop_music()

    jump lad_day2_evening
    

label lad_day2_bedroom_broken:

    $ change_room('bedroom_broken')

    $ play_music('sad', 2)

    if lad_details.saved_variables["day2_breakfast_follow"]:

        """
        The poor man is still there. I don't think he's moved.
        """

    else:

        """
        I slowly enter the unlocked door.

        It's Thomas Moody's.

        His lifeless body lies on the bed.

        I don't know what morbid curiosity led me here.

        Gosh.
        """

        $ unlock_map('bedroom_broken')

    """
    Now that I'm here, perhaps I should take a quick look.

    There might be something that helps me understand what happened.

    I look around the room.

    Nothing seems out of the ordinary.

    He looks peaceful.

    His mask is still on. 
    
    The doctor didn't even remove it for the examination.

    Well, if the doctor didn't, I certainly won't either.

    On a chair next to the bed, his clothes are meticulously folded.

    There's a whiskey flask on the nightstand.

    It's on its side, empty.

    Next to it is a stain. 
    
    I suppose it's whiskey, but it's an odd shade of green.

    That's peculiar.

    What could it be?

    That's all I notice in the room.
    """

    $ lad_details.observations.unlock('green_liquid') # TODO: Link to billiard room option not to drink the whiskey?

    pause 1.0
    # TODO: Add sound effect for discovering a clue?
    # TODO: FIRST REAL INVESTIGATION CLUE? Add intuition when returning to...

    $ play_music('PREVIOUS')

    return

label lad_day2_no_hunt_cancel:

    $ change_room('bedroom_lad')

    """
    I don't think there's anything interesting to do now.

    So, I'll just lie down on my bed for a while.
    """

    call wait_screen_transition()

    return

label lad_day2_no_hunt_bedroom_nurse_busy:
        
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
    Ah, Mr. Harring, I'm quite exhausted at the moment. 
    
    Would you mind coming back later?
    """

    lad """
    Of course, sorry for bothering you.
    """

    $ unlock_map('bedroom_nurse')

    return

label lad_day2_no_hunt_bedroom_captain_enter:

    """
    Ensuring no one's watching, I gently nudge the door open.
    """

    play sound door_open

    $ change_room('bedroom_captain')

    """ 
    The door opens smoothly, and I step inside.

    The room is impeccably neat.

    In one corner, a valet stand holds a military uniform.

    This must be Sushil Sinha's room.
    """
    
    $ unlock_map('bedroom_captain')

    """
    Now that I'm here, I should take a look around.
    """

    play sound searching

    $ renpy.pause(5, hard=True)

    $ change_room('bedroom_captain') # TODO: Add visual effect for the same room?
    
    """
    I searched for quite a while.

    I thought I'd found nothing until I opened the bed drawers.

    Inside is a gun and a few bullets.

    It's unusual, but not surprising for someone in the military.

    The rest of the room is unremarkable.

    I put everything back like it was and leave.
    """

    return

label lad_day2_no_hunt_bedroom_drunk_enter:

    """
    I cautiously push the door open, ensuring no one sees me.
    """

    play sound door_open

    $ change_room('bedroom_drunk')

    """
    The bedroom is messy and dimly lit and the smell of alcohol fills the air.

    There are clothes all over the floor.

    I think I can safely say it's Samuel Manning's room.
    """

    $ unlock_map('bedroom_drunk')

    """
    I quickly scan the room but only find empty whiskey bottles.

    As I'm about to leave, a piece of white paper in the fireplace catches my eye.

    Driven by curiosity, I pick it up.

    The writing on the paper is almost entirely burned. 
    
    I can only read some of it.

    There is a first part, written with an impeccable style.   
    """

    call drunk_letter_first_part_burned

    """
    Below, another message is scribbled in a barely legible hand:
    """

    call drunk_letter_second_part_burned

    """
    Even though its meaning eludes me, this letter seems significant.
    
    I decide to keep it, just in case.
    """

    $ lad_details.objects.unlock('burned_letter')

    return
