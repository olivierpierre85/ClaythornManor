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


label common_day3_morning_entrance_hall_meeting:

    if current_character.text_id == "captain":

        """
        Suddenly, I hear a voice rising.
        """

    elif current_character.text_id == "lad":

        """
        Just in case, I try calling out one more time.
        """

    else:

        """
        Mr Harring tries calling out one last time.
        """

    lad """
    Hello? Is anyone there?
    """

    captain """
    Mr Harring. I am here.
    """

    if current_character.text_id == "captain":

        """
        Ted Harring appears at the bottom of the stair, with Miss Baxter just behind him.

        Some of the colour comes back into his face when he sees me.
        """

    elif current_character.text_id == "lad":

        """
        Captain Sinha appears at the top of the stairs and comes down to join us.

        I didn't expect to be this relieved to see him.
        """

    else:

        """
        Captain Sinha appears at the top of the stairs and descends to join us.

        Mr Harring's face brightens at the sight of him.
        """

    call common_day3_morning_meeting_captain

    captain """
    We have got a lot to talk about, maybe we should settle somewhere more comfortable.
    """

    psychic """
    The tea room perhaps?
    """

    captain """
    Perfect.
    """

    $ change_room("tea_room")

    """
    Everyone finds a chair before we can continue our conversation.
    """

    return