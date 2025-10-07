label common_day3_morning_meeting_captain:

    captain """
    At last, living, breathing souls.

    I was starting to feel like I was in a ghost house.
    """

    psychic """
    We feel the same. You're the first person we've encountered today as well.
    """

    lad """
    Do you have any idea what's going on?
    """

    captain """
    Nothing concrete. All I know is, I don't like it.
    
    People don't just vanish from their homes without reason.
    """

    psychic """
    They certainly don't.
    """

    captain """
    And then there's the matter of the suspicious deaths.

    I could've dismissed them as bad luck yesterday, but now... I'm not so certain.
    """

    if current_character.text_id == "lad":
        """
        The conversation lingers in the air, a heavy silence stretching between us.
        """
    else:
        """
        There is an awkward silence.
        """

    return

label common_day3_morning_lad_psychic_tea_room_2:
    
    lad """
    By the way, did you check on Samuel Manning?

    You're the only one with the key to his room.
    """

    captain """
    No, not yet. I assumed he couldn't have gone far.

    But you're right, we should check on him.
    """

    lad """
    I think so too.

    We'll follow you.
    """

    if current_character.text_id == "lad":
        """
        Amelia shoots me a concerned look but remains silent.

        She follows us nonetheless.
        """

    return


label common_day3_morning_lad_psychic_captain_death_manning:

    $ change_room("bedrooms_hallway")

    $ unlock_map('bedroom_drunk')

    play sound door_knock

    captain """
    Mr Manning, are you there?
    """

    """
    No response.
    """

    captain """
    Alright, I'm going in.
    """

    if current_character.text_id == "lad":
        """
        He unlocks the door, and we trail behind him.

        But as I step inside, Captain Sinha tries to halt us.
        """
    else:
        """
        Without warning, he opens the door and enters.

        We quickly follow him, but he attempts to stop us. 
        """

    captain """
    Wait! Don't come in.
    """

    if current_character.text_id == "lad":
        """
        But it's already too late.
        """
    else:
        """
        But we are already in.
        """

    $ change_room('bedroom_drunk')
    
    $ play_music('scary', fadeout_val=1)

    if current_character.text_id == "lad":
        """
        The sight inside is beyond horrifying.

        Samuel Manning lies in his bed, drenched in blood, his throat slashed multiple times.

        Pale as a sheet, his eyes frozen in a blank stare.

        Miss Baxter almost screams.
        """
    else:
        """
        There lies Samuel Manning, dead in his bed.

        Blood is all over him.

        I let out a gasp.
        """

    captain """
    Miss Baxter, please don't stay here.
    """

    if current_character.text_id == "lad":
        """
        She's speechless, her gaze fixed on the horrifying scene.

        Sushil Sinha gently pulls her arm, leading her out. I quickly follow.
        """
    else:
        """
        Without a word, Sushil Sinha drags me out of the room.
        """

    $ change_room("bedrooms_hallway")

    captain """
    I regret letting you see that.

    You shouldn't have entered.
    """

    psychic surprised """
    Is... is he... dead?
    """

    captain """
    I'm afraid so.
    """

    lad surprised """
    Are you certain?

    Shouldn't we check his pulse?

    Maybe... just maybe, there's a chance he's alive.
    """
    
    if current_character.text_id == "lad":
        """
        My voice trembles as I speak, realisation dawning on me.
        """

    captain """
    I'm sorry, but it's too late.

    I've seen enough dead people to know. He's been gone for a long time.

    Likely since last night.
    """

    psychic """
    Oh my God.
    """

    if current_character.text_id == "lad":
        """
        The weight of shock renders me motionless.

        To help us recover, Sushil guides us back to the tea room.
        """
    else:
        """
        Ted Harring looks terribly distraught.

        Looking less affected, Captain Sinha guides us back to the tea room.
        """

    $ change_room("tea_room")

    captain """
    Miss Baxter, you should probably rest here for a little bit.

    I have something to check out, and I'll be back soon.

    Mr Harring, would you mind coming with me?
    """

    if current_character.text_id == "lad":
        """
        I'm still shaken from what we saw, but doing something might help me recover my senses.
        """

    lad """
    Well, sure.

    I'll follow you.
    """

    psychic """
    Please don't be long.
    """

    captain """
    Don't worry, this should only take a few minutes.
    """ 

    return


label common_day3_morning_lad_psychic_captain_deaths_end:

    psychic """
    You've been gone for a while. What happened?
    """

    # TODO Marsh dead or alive??? NOW alive, but maybe add later a branch where she died
    # captain """
    # I'm afraid we've found Miss Marsh. She has also passed away.
    # """

    # psychic """
    # No... Not another one...
    # """

    # if current_character.text_id == "lad":
    #     """
    #     Our eyes met, and although no words were spoken, the gravity of the situation was understood by all.
    #     """

    captain """
    I'm afraid we haven't been able to find Miss Marsh.

    We searched her room but it was empty.
    """

    psychic """
    Well, what should we do now?
    """

    captain """
    You both seem a bit shaken up.

    That's not surprising, given what you've witnessed.

    It's easier for me. 
    
    Sadly, I've seen my share of dead people.

    So I suggest you two rest for a bit while I continue to explore the manor.

    I'll be back soon.
    """

    if current_character.text_id == "lad":
        """
        I feel like I should accompany him.

        But he is right, I am exhausted and overwhelmed.

        So I just agree with a nod and sit down.
        """

    else:
        """
        I have no objection to that.

        Ted Harring seems to want to say something, then changes his mind.
        """

    return
