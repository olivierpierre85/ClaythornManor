# --------------------------------------------
#   Common - Saturday Hunt - The Confrontation in the Woods
#
#   After luncheon, the false Thomas Moody draws Captain Sinha away from the
#   rest of the north-field party on the pretext of his rifle, then confronts
#   him over the forged transfer order and shoots him.
#
#   The spoken dialogue is identical from either side. Only the narration
#   branches on current_character.text_id:
#       - "captain" : the victim's point of view  -> caller jumps to captain_ending_shot_in_woods
#       - "broken"  : the killer's point of view   -> caller continues the chapter
#
#   Callers:
#       - captain_day2_hunt_moody_alive
#       - broken_day2_hunt
# --------------------------------------------
label common_day2_hunt_captain_confrontation:

    broken """
    Captain, a word, if I may.

    My rifle has been pulling to the left all morning.

    I should value a second eye upon it.

    A few paces up the track will do.
    """

    if current_character.text_id == "captain":

        """
        I do not like the idea of following him alone into the trees.

        And it is hard to believe there is anything wrong with his weapon.

        But I cannot find a polite reason to refuse.

        My manners overrule my better judgement.
        """

    elif current_character.text_id == "broken":

        """
        He hesitates, and a wiser man would have refused outright.

        But Captain Sinha is a creature of manners before he is anything else, and manners will not let him deny so small a courtesy.

        I have counted upon that all weekend.

        It is the last thing his breeding will ever cost him.
        """

    captain """
    Very well.

    Lead on, Mr Moody.

    I shall be right behind you.
    """

    $ play_music('danger', 2)

    $ change_room('forest_stream', dissolve)

    if current_character.text_id == "captain":

        """
        I follow him up the track.

        He walks easily, his rifle slung over his shoulder.

        Thirty yards from the clearing, the cover thickens and the track comes down to a shallow stream.

        The voices from the luncheon fall away beneath the sound of water on stone.

        He stops at the water's edge, turns, and lifts the rifle from his shoulder.

        Not to show me.

        To hold.
        """

    elif current_character.text_id == "broken":

        """
        I lead him up the track, my pace unhurried, the very picture of a man with nothing on his mind but a wayward sight.

        He follows a careful step behind, the way a man follows when half of him already knows.

        Thirty yards on, where the cover thickens and a stream swallows the last voices from the luncheon, I judge it far enough.

        I stop. I turn. I bring the rifle down from my shoulder.

        Not to show him.

        To hold.
        """

    broken """
    That is quite far enough, I think, Captain.
    """

    if current_character.text_id == "captain":

        """
        His gun is now pointing directly at my chest.

        My own rifle hangs uselessly at my side.

        There is a yard too many between us for me to raise it in time.
        """

    elif current_character.text_id == "broken":

        """
        I bring the barrel level with his chest.

        His own rifle hangs at his side, a full yard further than his hand can reach in time.

        I watch him understand it. I watch him decide against trying.
        """

    captain """
    Mr Moody.

    What is the meaning of this?
    """

    broken """
    You see, Captain, I found a piece of paper upon my bed yesterday.

    An old army order, written in the autumn of 1917. A transfer.

    Until then, the officer named upon it had held the safest assignment in the whole army.

    Conducting officer to the war correspondents, minding the gentlemen of the press well back of the guns, where no harm could come to him.

    This order pulled him off it and sent him up to the line.

    I assume you can guess his name: Thomas Moody.

    And at the foot of the order, the name of the man who put his signature to it.

    Captain S. Sinha, Staff Officer, General Headquarters.

    A stroke of your pen, and a man was taken from safety and marched into the worst of the war.

    Most who were sent up that season are in the Flanders mud yet.

    And the few who came back were not much luckier.

    They go through life as living monsters, hiding behind a mask such as this.
    """

    if current_character.text_id == "captain":

        """
        He taps the porcelain of his mask with two gloved fingers.
        """

        """
        My mouth is dry.

        I have signed a great many papers in my time.

        Transfers, requisitions, routine dispatches.

        Most of them I could not recall if my life depended upon it.

        It is true that by that autumn, they were combing the soft billets for officers to throw into the thick of battle.

        Yet, that was never my job.
        """

    elif current_character.text_id == "broken":

        """
        I tap the porcelain of my mask with two gloved fingers, as though the lie of it were the proof of everything.

        Beneath it my face is whole. The mask was only ever a borrowed grief.

        But the grief it stands for is mine, and it is real, and it has a name.
        """

        """
        He has gone very still.

        A clever man, weighing the paper against his memory and finding the memory wanting.
        """

    captain """
    You are mistaken, Mr Moody.

    I only ever signed what was laid before me, drafted by other hands.

    I never chose a single name, least of all his.
    """

    broken """
    Ah! How convenient for you, Captain.

    But I have no reason to believe you, in any case.

    Especially since I am now sure that you are not the war hero you claim.

    It was obvious today, when you could not even shoot a bird right under your nose.

    Yet yesterday you were entertaining everyone with tales of Burma and the Boxers, as though you had fought in them yourself.

    You are a fraud, that is clear enough.

    And maybe somebody is using me to hurt you.

    But I am very happy to oblige.
    """

    if current_character.text_id == "captain":

        """
        He does not lower the rifle.

        His gaze is resolute, heavy with hatred.
        """

    elif current_character.text_id == "broken":

        """
        I do not lower the rifle.

        Whatever he reads in my face, let him read it true. I have no wish to disguise it.
        """

    captain """
    Please, Mr Moody, consider what is at stake here.

    Someone here is manufacturing all of this.

    They were likely hoping for precisely this to happen.

    You are being used to their end.

    And you are no safer than I am.
    """

    broken """
    How very considerate of you, Captain.

    But I can quite look after myself, I assure you.
    """

    captain """
    Thomas. Please.

    It is all a mistake.
    """

    broken """
    You will not sway me by using that name.

    You will only anger me the more.
    """

    captain """
    What do you mean?
    """

    broken """
    Well, I suppose there is no reason to hide it anymore.

    Thomas was the name of someone very dear to me.

    I would call him Tom, and he would call me Archie.

    But that is over now.

    All because of you.
    """

    $ broken_details.description_hidden.unlock('lie_name')

    if current_character.text_id == "captain":

        """
        Before I can make sense of what he is saying, he levels the rifle at my head.

        I raise my hands to protect myself.
        """

    elif current_character.text_id == "broken":

        """
        He opens his mouth, to question it or to plead, I neither know nor care.

        I raise the rifle to his head before the words can come.

        His hands fly up, as though flesh and bone could turn a bullet aside.
        """

    broken """
    Ah! Further proof you never saw battle, Captain.

    Well.

    This is as close as it gets.
    """

    play sound gun

    $ stop_music(1)

    pause 1.0

    return
