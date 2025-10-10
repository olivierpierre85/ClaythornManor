# ------------------------------------
#               LAD/PSYCHIC
# ------------------------------------
label common_day3_morning_lad_psychic_journey:

    lad """
    I'm coming!
    """

    if current_character.text_id == "lad":
        """
        I quickly get dressed and open the door.

        Amelia Baxter enters, looking visibly nervous.
        """
    else:
        """
        Finally, I was getting worried.

        He opens the door for me and I enter.
        """

        $ change_room('bedroom_lad')

    $ play_music('mysterious', 2)

    psychic """
    Mr Harring, I believe my hunch was right yesterday.

    Something strange is afoot.
    """

    lad """
    What do you mean?
    """

    psychic """
    I haven't seen any staff members on my way here.

    At this hour, they should be busy with lighting fires, cleaning and setting up breakfast.

    Yet, I neither saw nor heard anyone.

    It's as silent as a graveyard in here.
    """

    lad """
    Are you sure it's not just because it's so early?
    """

    psychic """
    I'm certain.

    I was up at the same time yesterday, and the house was bustling with activity.

    Something's not right, I assure you.
    """

    lad """
    Okay, if you say so. 

    But how is that related to a robbery?
    """

    psychic """
    I'm not so sure anymore that this is about a robbery.

    I have a feeling it could be something much worse.
    """

    if current_character.text_id == "lad":
        """
        A chill goes through my body.

        Worse than a robbery? What could she mean?

        But I'm hesitant to ask her.

        Instead, I try to appear confident.
        """
    else: 
        """
        He paused for a second there, he must have realised it's serious.
        """

    lad """
    Alright, we'd better investigate then.
    """

    return


label common_day3_morning_lad_psychic_tea_room_1:

    captain """
    Is anyone here?
    """

    if current_character.text_id == "lad":
        """
        I respond without hesitation.
        """

    lad """
    Yes, Ted Harring. I'm here, and Amelia Baxter's with me.
    """

    if current_character.text_id == "lad":

        """
        Amelia stiffens. I sense her unease, perhaps thinking I replied too quickly.

        It's too late for second thoughts now.

        Captain Sinha soon joins us in the room.
        """
    
    call common_day3_morning_meeting_captain

    return