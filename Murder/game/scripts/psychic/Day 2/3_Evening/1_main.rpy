# --------------------------------------------
#   Psychic
#           
#   Saturday - Evening
# 
#   15:00 -> 23h
#
#   Music: sad
#
#   Position
#       - House: Everyone else
#       - Dead : broken, doctor
#
#   Notes : 
#       -  captain generic, lad generic
# --------------------------------------------
label psychic_day2_evening:

    call change_time(15, 00, "Evening", "Saturday", hide_minutes=True, chapter='saturday_evening')

    $ psychic_details.add_checkpoint("psychic_day2_evening") 
    
    call black_screen_transition("Amelia Baxter", chapters_names[current_chapter])

    $ change_room("great_hall", irisout)
    
    """
    I observe the hunting party as they make their way into the house.

    Rosalind was already by the entrance.

    Lady Claythorn steps through the doorway first, her expression one of sheer disbelief.

    Following close behind are the butler and footman.

    They carefully carry someone on an improvised stretcher.
    """

    $ play_music('sad')

    call common_day2_evening_entrance_dialog

    """
    I watch Captain Sinha and Ted Harring carry Doctor Baldwin to his room.

    Now, the attention of everyone turns to Samuel Manning.

    I realize no one has thought about restraining him in any way.

    But it seems unnecessary as he is sitting on the stairs,

    his gaze empty, apparently unaware of what is happening around him.
    """

    call common_day2_evening_samuel_manning_discussion_part_1

    call common_day2_evening_samuel_manning_discussion_part_2

    """
    We all watch the two men leave down the stairs.

    Then an awkward silence fills the room.
    """

    call common_day2_evening_samuel_manning_discussion_part_3

    """
    Before heading to my room, there is something I would like to understand.

    I approach the butler.
    """

    butler """
    Yes, Miss Baxter?
    """

    psychic """
    I don't understand; how could you give a gun to someone so drunk?
    """

    butler """
    I am so sorry, but he wasn't drunk when we talked this morning.

    He was acting totally normally.

    He probably got drunk during the day.

    There was nothing I could have done.
    """

    psychic """
    Right.
    """

    """
    He did seem very drunk to me during breakfast though.
    """

    call psychic_day2_afternoon_bedroom

    call change_time(18,30)

    $ change_room("dining_room", irisout)
    
    $ play_music('sad', 3)

    """
    As I step into the dining room, a sombre ambience surrounds me.

    The chairs where Daniel Baldwin and Thomas Moody usually sit are empty.

    Samuel Manning is not here either, obviously.

    I settle into my familiar spot, with Ted Harring to my right.

    Lady Claythorn stands up to speak.
    """

    call common_day2_evening_dinner

    call change_time(21, 00)

    """
    We ate in silence.

    After dinner, most people retired to their rooms.

    I don't think many will join for a drink afterwards.

    So I could also take advantage of the fact that the Manor is almost empty.
    """

    if psychic_details.important_choices.is_unlocked('visit_lad'):
        
        """
        Or I could wait in my room for Ted Harring. 
        """

    else:
        
        """
        Or maybe it's safer to just wait in my room.
        """

    """
    What should I do?
    """

    $ time_left = 60

    call run_menu(psychic_details.saved_variables["day2_evening_map_menu"])

    call change_time(22, 00)

    if time_left <= 0:
        """
        There's no need to wander the house further.

        I should return to my room.
        """

    if psychic_details.important_choices.is_unlocked('visit_lad'):
        
        call psychic_day2_evening_lad_discussion_2

    else:
        
        """
        With nothing more to do, I quickly fall asleep.
        """

    jump psychic_day3_morning


label psychic_day2_evening_cancel:

    $ change_room('bedroom_psychic')

    """
    There's nothing more I can do right now.

    I'll just go and lie on my bed for a bit.
    """

    call wait_screen_transition()

    return

