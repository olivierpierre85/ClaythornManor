# ------------------------------------
#               LAD/CAPTAIN
# ------------------------------------

label common_day3_morning_lad_psychic_captain_marsh_empty:
    
    """
    He walks back up the stairs and stands in front of another room.
    """

    $ change_room("bedrooms_hallway")

    captain """
    It's Miss Marsh's room.

    It was locked when I tried to open the door earlier.

    At the time, I didn't dare to go further.

    But now, I'm afraid I have to open it by force.
    """

    lad """
    Do you believe she could still be in there?

    Then she would be...
    """

    captain """
    Dead, I'm afraid.

    After what we saw, I think it's a very strong possibility.
    """

    lad """
    Oh my God.
    """

    """
    Captain Sinha draws a deep breath, clenches his fists, and then forcefully kicks the door. 
    
    It bursts open with a deafening crack.
    """

    $ change_room("bedroom_nurse")

    """
    The room is eerily quiet.

    But Rosalind Marsh is not there.

    We look in every corner, but we can't find anything of interest.
    """

    lad """
    What a relief.
    """

    captain """
    Yes, of course. But there's no need to linger here.

    Let's return to the tea room, we need to talk with Miss Baxter to decide our next steps.
    """

    $ change_room("tea_room")

    return

# NOT USED FOR NOW, but maybe later
# label common_day3_morning_lad_psychic_captain_marsh_death:

#     """
#     He walks back up the stairs and stands in front of another room.
#     """

#     $ change_room("bedrooms_hallway")

#     captain """
#     It's Miss Marsh's room.

#     It was locked when I tried to open the door earlier.

#     At the time, I didn't dare to go further.

#     But now, I'm afraid I have to open it by force.
#     """

#     lad """
#     Do you believe she could still be in there?

#     Then she would be...
#     """

#     captain """
#     Dead, I'm afraid.

#     After what we saw, I think it's a very strong possibility.
#     """

#     lad """
#     Oh my God.
#     """

#     """
#     Captain Sinha draws a deep breath, clenches his fists, and then forcefully kicks the door. 
    
#     It bursts open with a deafening crack.
#     """

#     $ change_room("bedroom_nurse")

#     """
#     The room is eerily quiet.
    
#     And there she is—Rosalind Marsh—lying peacefully on her bed.
    
#     There is a trace of blood on the corner of her mouth.
#     """

#     lad """
#     Is she...?
#     """

#     captain """
#     Dead, yes. It appears she was poisoned. 
#     """

#     """
#     My heart pounds in my chest. 
    
#     The reality of two dead bodies sets in, and the room feels like it's closing in on me.
#     """

#     captain """
#     Let's return to the tea room. 
    
#     We need to warn Miss Baxter and decide our next steps.
#     """

#     $ change_room("tea_room")

#     return