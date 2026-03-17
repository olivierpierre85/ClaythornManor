label common_day3_afternoon_lad_psychic_stay:

    $ stop_music(2)

    if current_character.text_id != "nurse":

        psychic """
        Well, there's no point in waiting around doing nothing.

        We haven't eaten since yesterday.

        I could check the kitchen to see if there's anything I can prepare.
        """

        lad """
        Okay, I'll come with you.
        """

    $ change_room('basement_stairs', dissolve)

    if current_character.text_id == "lad":

        """
        We are heading to the lower floor when we hear a shout.
        """

    elif current_character.text_id == "psychic":

        """
        On our way to the basement, I hear a familiar voice.
        """

    elif current_character.text_id == "nurse":

        """
        I am halfway down the service stairs when I hear voices.

        Two of them, coming from the ground floor.

        My heart lurches.

        The house was supposed to be empty.
        """

        pause 1.0

        """
        I recognise the voices — Ted Harring and Amelia Baxter.

        They are heading this way.

        There is no time to retreat.

        Very well. I shall have to be convincing.
        """

    $ play_music('mysterious', 2)
    
    nurse """
    Hello!
    """

    pause 1.0

    nurse """
    Is there someone here?
    """

    psychic """
    Oh my God, Miss Marsh, you're here!
    """

    nurse """
    Of course I am here. Why do you look so surprised?
    
    I'm afraid I overslept. I don't feel quite like myself today.

    When I woke up, I went to check the dining room but found it empty.

    I wandered in the house for a while but I didn't see anyone until I met you.

    Where is everybody?
    """

    psychic """
    Oh my dear, we don't know.
    """

    if current_character.text_id == "lad":

        """
        We updated her on what happened since this morning.

        When we had finished telling her the story, she remained relatively calm, considering the situation.
        """

    elif current_character.text_id == "psychic":
        # TODO: Add more details or elaborate, since the previous explanation was brief?
        """
        We explained the situation to her as best we could.

        She doesn't appear very alarmed by it.

        I am finding that peculiar.
        """

    elif current_character.text_id == "nurse":

        """
        The lie comes easily enough. I have had practice.

        They tell me what has happened since this morning.

        Mr Manning — dead. The doctor — missing. Lady Claythorn — vanished.

        Captain Sinha has gone to fetch help.

        I keep my expression steady throughout.

        Not too alarmed, not too indifferent.

        Just the right measure of concern.
        """

    nurse """
    Poor Mr Manning, what a terrible fate.

    And what horror that must have been for you, my dear.

    Are you all right?
    """

    psychic """
    I am better now.

    Captain Sinha should be back with help soon, so I'll be fine if I can keep my mind occupied until then.

    Speaking of which, we were heading to the kitchen to see if we can prepare some sort of meal.
    """

    nurse """
    Right, it's a good idea. We might as well keep ourselves busy.
    """

    if current_character.text_id == "lad":
        """
        And just like that, we go downstairs to the kitchen.
        """
    elif current_character.text_id == "psychic":
        """
        So we go downstairs.
        """
    elif current_character.text_id == "nurse":
        """
        Food. Precisely what I came down here for.
        """

    $ change_room('kitchen', dissolve)

    $ stop_music(2)

    """
    We look around for something to eat.
    """

    psychic """
    There isn't much.

    But I think we can manage a light luncheon if you're not picky.
    """

    nurse """
    I'll help you.
    """

    if current_character.text_id == "lad":
        """
        I offer to help as well, but they decline.
        
        So, I take a seat while they prepare the food.   

        That's probably for the best.

        I couldn't do much to help anyway.
        """
        
        $ lad_details.description_hidden.unlock('cook') 

    elif current_character.text_id == "psychic":
        """
        Mr Harring is nice enough to offer his help.

        But I don't think he has much experience in this department.

        So we decide it's best if he doesn't get involved.
        """
    elif current_character.text_id == "nurse":
        """
        Mr Harring offers to assist, but between Miss Baxter and myself we have it well in hand.

        He takes a seat and watches.

        As far as they know, I simply overslept.

        All I need do is eat, wait for the right moment, and slip away.
        """

    pause 1.0

    $ change_room('dining_room', dissolve)

    if current_character.text_id == "lad":
        """
        When everything is ready, I carry the plates to the dining room.

        I set them at our usual places.

        Then I leave the dining room.
        """
    elif current_character.text_id == "psychic":
        """
        When the food is ready, we go to the dining room to eat.

        Ted Harring sets the table and then tries to leave.
        """
    elif current_character.text_id == "nurse":
        """
        We carry the plates to the dining room.

        Mr Harring sets the table and then tries to leave.
        """

    psychic """
    Where are you going, Mr Harring?

    It's better if we stick together at all times.
    """

    lad """
    I understand, but there's something I need to do alone.

    We haven't had a moment apart the entire day and...
    """

    psychic """
    Say no more, I understand.

    I'm in the same situation.

    What about you, Miss Marsh?
    """

    nurse """
    Oh, I'm fine, thank you.

    You both go, I'll finish preparing the table.
    """

    psychic """
    Very well.

    Let's meet back here in a few minutes then.
    """

    lad """
    Of course.
    """

    pause 1.0

    return


label common_day3_afternoon_lad_falls:

    $ stop_music()

    lad surprised """
    What's happening?

    Why am I...
    """

    if current_character.text_id == "lad":
        """
        I try to speak further, but no words come out.
        """
    elif current_character.text_id == "psychic":
        """
        He is unable to say another word before he collapses to the floor.
        """
    elif current_character.text_id == "nurse":
        """
        He cannot finish the sentence.

        His legs give way beneath him.
        """

    play sound body_fall

    return


# Shared scene after Ted collapses: nurse checks pulse, reveals the swap,
# finds the gun, and starts to feel unwell. Used by both psychic and nurse.
label common_day3_afternoon_nurse_revelation:

    if current_character.text_id == "psychic":

        psychic """
        Mr Harring?!
        """

        """
        Rosalind Marsh rushes to his side.

        Her nurse's training kicks in.
        """

    elif current_character.text_id == "nurse":

        """
        He collapses to the floor.

        I rush to his side. My training takes over before my mind catches up.
        """

    nurse """
    Mr Harring, can you hear me?
    """

    psychic """
    What's happened?

    How is he?
    """

    if current_character.text_id == "psychic":

        nurse """
        He's not well, I don't understand.
        """

        """
        She checks his heartbeat.
        """

    elif current_character.text_id == "nurse":

        """
        I check his pulse.

        There is nothing.
        """

    nurse """
    He has no pulse.

    He's dead.
    """

    psychic """
    What?! No, that can't be.

    How is this possible?
    """

    nurse """
    I'm not sure, but I doubt it's a coincidence at this point.

    I believe he's been poisoned.
    """

    if current_character.text_id == "nurse":

        """
        Poisoned.

        From the plate I gave him.

        The plate that was meant for me.

        I was right about the food.

        And now a man is dead because of what I did.
        """

    psychic """
    No, no, no ...

    Mr Harring, why?
    """

    if current_character.text_id == "psychic":

        """
        My hands shake.

        Tears run down my cheeks.

        Rosalind Marsh keeps talking, but I can barely understand what she's saying.
        """

    elif current_character.text_id == "nurse":

        """
        Miss Baxter weeps.
        """

    nurse """
    All I know is that he wasn't the target.

    I switched my plate with his before we started eating.

    I was the one supposed to die, not him.
    """

    psychic """
    You switched plates? Why?
    """

    nurse """
    Why?!

    After all that's happened, weren't you suspecting anything?
    """

    if current_character.text_id == "psychic":

        """
        I try to form a coherent response, but words elude me.
        """

    psychic """
    ...
    """

    nurse """
    When I woke to find this place empty, I knew something was wrong.

    I heard the three of you rummaging around the house and I hid.

    I didn't trust Sushil Sinha, but I should have been more suspicious of Ted Harring.

    After all, he was the least respectable of everyone here.

    Clearly out of place in this environment.

    He...
    """

    if current_character.text_id == "psychic":

        """
        She pauses.
        """

    elif current_character.text_id == "nurse":

        """
        I stop.

        Something is wrong.

        Not with the room. With me.

        A wave of nausea rises from my stomach, sudden and sharp.

        My vision swims.
        """

    nurse """
    I don't know what his motives were, but...
    """

    pause 1.0

    nurse """
    ...it doesn't matter now.
    """

    if current_character.text_id == "psychic":

        """
        She clearly struggles to speak.
        """

    elif current_character.text_id == "nurse":

        """
        My hands tremble.
        """

    nurse """
    Wait, something feels off.
    """

    pause 1.0

    if current_character.text_id == "psychic":

        """
        She grasps the chair next to her for support.
        """

    elif current_character.text_id == "nurse":

        """
        I grasp the chair for support.

        The room tilts.
        """

        $ stop_music(2)

    nurse """
    I think I'm going to faint.
    """

    return


# Shared: nurse accuses psychic after revelation
label common_day3_afternoon_nurse_accuses_psychic:

    pause 1.0

    nurse """
    What have you done?
    """

    if current_character.text_id == "psychic":

        """
        I barely register her words.

        It feels like I'm about to collapse myself.
        """

    elif current_character.text_id == "nurse":

        """
        The words leave my mouth before I can think them through.
        """

    psychic """
    Me? What about me?
    """

    return


# Shared: nurse draws gun on psychic, psychic lunges, gun struggle
label common_day3_afternoon_nurse_gun_confrontation:

    if current_character.text_id == "psychic":

        """
        I turn towards her and see that she is pointing a gun at me.
        """

    elif current_character.text_id == "nurse":

        """
        I pull out the revolver I took from the gun room and level it at her.

        My hand is shaking.
        """

    nurse """
    Don't move.
    """

    return


# Shared: the physical gun struggle between nurse and psychic
label common_day3_afternoon_nurse_gun_fight:

    if current_character.text_id == "psychic":

        """
        Without hesitation, I jump at her.

        It happened so swiftly that she didn't have time to react.
        """

    elif current_character.text_id == "nurse":

        """
        She lunges at me.

        It happens so swiftly that I cannot react.
        """

    nurse surprised """
    Wait! I'll shoot.
    """

    if current_character.text_id == "psychic":

        """
        But I am already upon her, grappling for the gun.
        """

    elif current_character.text_id == "nurse":

        """
        But she is already upon me, grappling for the gun.
        """

    $ stop_music()

    nurse """
    Stop, or I'll ...
    """

    play sound gun

    if current_character.text_id == "psychic":

        """
        The sound of a gunshot pierces the air, ending the fight.

        Silence descends, heavy and suffocating.

        I stand frozen, the nurse's body slumping to the ground.

        The gun, now a cold weight in my hand, drops to the floor alongside her.
        """

    elif current_character.text_id == "nurse":

        """
        The sound of a gunshot pierces the air, ending the fight.

        A sharp, burning pain blooms in my chest.

        The revolver slips from my fingers.

        My legs give way.
        """

    play sound body_fall

    return