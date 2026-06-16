# --------------------------------------------
#   Captain — Sunday morning, nurse path
#
#   The captain confided in Miss Marsh last night, and she comes for him at
#   first light. While they take stock in his room, she admits she could not
#   manage the walk to town, so the captain proposes to fetch help alone
#   while she hides. Before they can move, they hear others going through
#   the house (the lad and the psychic, searching — never named). Miss Marsh
#   persuades the captain not to show himself, and they hide together in the
#   butler's attic room.
#
#   While they wait for quiet, a single hub menu lets the captain draw her
#   out (her health, the prize letters, then China once the letters have
#   been discussed). Flavour and player insight only — no unlocks.
#
#   When the house falls silent he leaves alone on foot to fetch help,
#   leaving her his pistol and the master key, and is shot on the road
#   (captain_ending_shot_fleeing). This path does not reach the afternoon.
# --------------------------------------------

label captain_day3_morning_nurse:

    $ change_room('bedroom_captain', irisout)

    """
    I sleep poorly, and only in patches.

    The house stays quiet through the night.

    A little before half past eight, I dress and sit on the edge of the bed.
    """

    play sound door_knock

    """
    There is a soft, quick knock at the door.
    """

    nurse """
    Captain. It's me.
    """

    """
    I unlock the door.

    Miss Marsh slips inside without a word and closes it behind her.

    She is pale, but quite collected.
    """

    captain """
    Miss Marsh.

    Are you all right?
    """

    nurse """
    I am, but there is something wrong with the house.
    """

    captain """
    What do you mean?
    """

    nurse """
    There are no staff. No fires lit. No breakfast laid.

    I have walked the dining room, the kitchen, the back corridor.

    Not a soul.
    """

    captain """
    So I was right, something strange is happening here.

    Have you checked any of the other rooms?
    """

    nurse """
    No, I came straight to you.
    """

    captain """
    A sound choice.

    It might not be safe for you to just roam around the house.
    """

    nurse """
    I believe you are right.

    I was thinking we might hide for a while, at least until the police come.
    """

    captain """
    Right, the police.

    I do not know for sure they will come, Miss Marsh.

    There is a good chance they were never called in the first place.
    """

    nurse """
    Never called, but Lady Claythorn...
    """

    captain """
    Lady Claythorn might be behind this masquerade, so there was no reason for her to call the police.

    We could wait here indefinitely.
    """

    nurse """
    Oh... you are right of course.

    We really shouldn't trust anything that she said, should we?

    What can we do then?
    """

    captain """
    The way I see it, we have two choices.

    We can search the house and try to make sense of what is happening, or we can leave at once and make for the town.
    """

    nurse """
    I do not like the idea of roaming around the house, even with you to protect me.

    But leave, Captain? On foot?
    """

    captain """
    I am afraid so.

    Lady Claythorn and her staff most likely left with the motor car.

    It is a fairly long walk to the town, but it is still early. I am sure we can make it.
    """

    nurse """
    Oh, I am sure you could, Captain.

    Sadly I can't.
    """

    """
    She says it quietly, and I see now what I was too preoccupied to mark before.

    The pallor that is not only fear.

    The careful way she holds herself.
    """

    nurse """
    I am not a healthy woman, Captain.

    There is a good chance my body will not hold for such a long journey.
    """

    captain """
    I see.
    """

    """
    I think her condition might be worse than her quiet behaviour shows.

    But this is not the moment to press her on it.
    """

    captain """
    In that case, I believe the safer bet is for me to leave alone.

    And I should go as soon as possible then. This way there is a very good chance that I can come back for you before the end of the day.

    You could hide until then.
    """

    play sound door_shut

    """
    Somewhere below us, a door bangs.

    Then footsteps. More than one set, moving fast.
    """

    nurse """
    Captain...
    """

    """
    I raise a hand for silence and listen.

    Floorboards along the corridor below. A voice, too muffled to make out. Another door.

    Whoever they are, they are going through the house room by room.
    """

    captain """
    Someone is searching the house.

    I should go out and meet them. Better to face a man than be cornered by one.
    """

    nurse """
    Captain, no.

    We do not know who is out there.

    It might be one of the guests. It might be whoever did away with the staff.

    If you open that door, you will find out which only when it is too late.
    """

    """
    I weigh it.

    I have one revolver, six rounds, and no notion of their numbers or their intent.

    She is right. This is probably dangerous.
    """

    captain """
    Very well, we stay out of sight.

    But not here.

    If they are opening doors, they will reach this room sooner or later.
    """

    nurse """
    The attic.

    The staff are gone, and no guest has any business up there.

    Nobody will think to look for us amongst empty servants' rooms.
    """

    captain """
    The attic, good.

    I have the butler's master key, so the locked doors up there are no obstacle.

    We wait for the corridor to clear, then we move. Quickly and quietly.
    """

    """
    We stand on either side of the door and listen.

    The footsteps pass along the corridor, pause somewhere at the far end, and fade towards the stairs.

    I ease the door open.
    """

    call change_time(9, 0)

    $ change_room('bedrooms_hallway', dissolve)

    """
    The corridor is empty.

    We make for the attic stair, Miss Marsh ahead, my eyes on the landing behind us.
    """

    $ change_room('attic_hallway', dissolve)

    """
    The narrow stair creaks under our weight, and then we are up amongst the servants' doors.

    I fit the master key to the butler's room. It belonged to the head man of the house, and it has the soundest door up here.
    """

    play sound door_open

    $ change_room('attic_butler_room')

    """
    I lock the door behind us.

    A narrow bed, a washstand, a single chair. Against the far wall, a heavy glass-panelled cabinet with the household silver asleep inside it.

    Miss Marsh takes the chair. I set my back against the wall where I can watch the door.
    """

    captain """
    Now we wait until the house is quieter. 
    
    Then, we will decide our next move.
    """

    nurse """
    Very well, Captain.
    """

    """
    Miss Marsh sits in the chair, her hands folded in her lap.
    
    I keep my place by the wall and listen to what is happening downstairs.

    This might take a while. Maybe now is a good opportunity to ask Miss Marsh some questions.
    """

    $ time_left = 120
    call run_menu(TimedMenu("captain_day3_attic_wait_menu", [
        TimedMenuChoice("Ask her about her health", 'captain_day3_attic_ask_health', 30),
        TimedMenuChoice("Ask her what brought her here", 'captain_day3_attic_ask_prize', 30, linked_choice='captain_day3_attic_ask_china'),
        TimedMenuChoice("Ask her about the Boxer Rebellion", 'captain_day3_attic_ask_china', 30, condition="is_linked_choice_hidden('captain_day3_attic_wait_menu', 'captain_day3_attic_ask_china')"),
        TimedMenuChoice("Say nothing", 'captain_day3_attic_wait_silence', 0, early_exit=True, keep_alive=True),
    ]))

    call wait_screen_transition()

    call change_time(11, 30)

    """
    The footsteps below stopped a long while ago, and the house has gone back to its heavy silence.

    No one has tried the attic stair.
    """

    captain """
    The house has been quiet for a long while now.

    If I am to reach the town and come back with help before nightfall, I should leave now.

    You will stay here, as we agreed.

    This room has a sound door and a sound lock.
    """

    nurse """
    I see.

    If I am being honest, I do not like this, Captain.

    It feels extremely dangerous for me.
    """

    captain """
    I know and I am sorry, but I still believe it is our best chance.

    And if it can ease your mind, you can take this pistol.

    I try always to keep it on me. One never knows when one might need protection.

    Do you know how to use one?
    """

    nurse """
    I can manage, I believe.

    But I really hope I won't have to use it.
    """

    captain """
    You probably won't.

    Lock the door behind me and do not open it to anybody.

    It is safe to say that everyone is a suspect at this point.
    """

    """
    I hand her the pistol, and the master key with it.

    I do not need the key any more, anyway.
    """

    nurse """
    All right, I think I can manage that.

    Thank you, Captain.
    """

    captain """
    Good, in that case I see no reason to linger.

    I will go straight away and come back as soon as possible.

    Good luck, Miss Marsh.
    """

    nurse """
    Good luck, Captain.
    """

    call change_time(12, 00)

    call captain_day3_leave_alone_introduction
    
    """
    Then, away to my right, I notice something.

    Something in the wood is the wrong colour.

    I watch its shape with care.

    From that shape, I can spot something shining, metal.

    It takes me a moment to understand what it is.
    
    The barrel of a rifle.

    And it is pointing right at me.

    I quickly grab for my own gun but come up empty.

    Miss Marsh has it.

    I am defenceless.
    """

    play sound gun

    jump captain_ending_shot_fleeing


# ------------------------------------
#   THE WAIT — attic hub menu
# ------------------------------------

label captain_day3_attic_ask_health:

    captain """
    You said the walk to the town would be more than your body could bear.

    Forgive my asking plainly, Miss Marsh, but what ails you?
    """

    nurse """
    You are direct, Captain.
    """

    captain """
    I believe that, given the circumstances, it is best to be.
    """

    nurse """
    Fine then, I suppose there is no reason to hide this from you.

    I have been diagnosed with consumption.

    Because of it, I have not been strong for some years.

    This weekend has asked more of me than I expected, that is all.
    """

    """
    She folds her hands again, and that is plainly the end of the matter.

    Consumption. I know how serious that is.

    She is right to believe she will not be able to leave on foot.

    No, if she wants to leave safely, she will need a motor car, that is certain.
    """

    return


label captain_day3_attic_ask_prize:

    captain """
    May I ask what brought you here, Miss Marsh?

    The reason for your award, I mean.
    """

    nurse """
    Well, the letter mentioned an award for distinguished service.

    Something about having served in more wars than any other nurse.
    """

    captain """
    Really, that is impressive.
    """

    nurse """
    Yes. But also a little vague.

    It is hard to imagine that there are not hundreds of nurses as distinguished as myself, maybe more so.

    From the day I received that letter I have been suspicious.
    """

    captain """
    Yet you came anyway.
    """

    nurse """
    I did.

    I need the money, you see.

    A thousand pounds is not something you can just turn down.

    Now, I regret I did not stay at home.
    """

    """
    I could let it pass with a polite word.

    Instead I find myself answering her honestly.
    """

    captain """
    My letter spoke of an impressive military career.

    Medals, campaigns, acts of courage in the field.
    """

    nurse """
    And?
    """

    captain """
    Unlike yours, it was plain to see mine was pure fabrication from the start.

    The name was correct, the battles, the places.

    But my role in those battles was clearly exaggerated.

    I assumed it was a mix-up due to my origins.

    I could have written back to correct it, but I did not.

    I suppose you are right. We are willing to do an impressive number of things for the right amount of money.
    """

    nurse """
    Thank you for your honesty, Captain.

    Then we are the same.

    Two impostors, invited under false pretences.

    And I would wager the others are too.

    A houseful of guests, every one of them honoured for something they know, in their hearts, they did not quite do.

    Maybe this was just a test, to see who would be dishonest enough to come.

    And to make us pay dearly for it.
    """

    captain """
    If that is true, then we are in even more danger than I thought.
    """

    """
    I ponder this for a few seconds.

    Is this just an elaborate way to torture us?

    But for what motive?
    """

    captain """
    Something is troubling me.

    The letters were not invented entirely out of nothing.

    As I said, mine had the regiments right, the postings, the dates.

    Battles I actually participated in, even if it was from afar.

    It would have been very hard to just fabricate those things.
    """

    nurse """
    Now that you mention it, mine had very precise information too.

    It had most of my postings right. It even knew I had served abroad — for instance, that I was in China during the Boxer Rebellion.

    Whoever wrote those letters knew us, Captain. Well enough to know which truth would bring us here.
    """

    """
    China, during the Rebellion.

    The detail lodges itself at the back of my mind.
    """

    return


label captain_day3_attic_ask_china:

    captain """
    You said you were in China earlier, Miss Marsh.

    During the Rebellion?
    """

    nurse """
    Yes.

    With the field hospitals, nursing the wounded out of the legations.

    I know you were there too, Captain. We all heard your story on Friday evening.
    """

    captain """
    Interesting, that is a strange coincidence.
    """

    nurse """
    If it is one at all.

    There is a curious thing I have been turning over since your speech.

    Doctor Baldwin was in China in those years as well, I am almost sure of that.
    """

    captain """
    The doctor?

    How do you know that?
    """

    nurse """
    I recognised him.

    It was a long time ago, and of course he must have changed quite a bit.

    I wanted to ask him about it, but did not have the time.
    """

    captain """
    Yes, what a sad end for Doctor Baldwin.
    """

    """
    I weigh the implications of that information.
    """

    captain """
    Yourself, myself, Doctor Baldwin.

    Three guests out of seven, all in China a quarter of a century ago.
    """

    nurse """
    It may be nothing.
    """

    captain """
    Perhaps.

    But the letters knew us, Miss Marsh. You said it yourself.

    If our host went digging into our pasts, China is where three of those pasts cross.
    """

    """
    I turn it over and can make nothing more of it.

    Whatever happened out there, it was a long time ago, and half a world away.
    """

    return


label captain_day3_attic_wait_silence:

    if is_choice_already_chosen('captain_day3_attic_wait_menu', 'captain_day3_attic_ask_health') or is_choice_already_chosen('captain_day3_attic_wait_menu', 'captain_day3_attic_ask_prize'):

        """
        We have said what there is to say.

        Miss Marsh seems content to keep her own counsel, and I keep mine.
        """

    else:

        """
        I find I have no appetite for conversation, and Miss Marsh does not press me.
        """

    """
    We sit in silence and listen to the house below.
    """

    return


label captain_day3_leave_alone_introduction:

    # Same leaving introduction for both paths
    $ change_room('entrance_hall', dissolve)

    """
    I do not waste time and go down fast to the entrance hall.

    It is still empty, so I make it outside.
    """

    $ change_room('forest_road', dissolve)

    """
    I take only my coat and what will fit in its pockets.

    The drive gives way to a rough road, and the road to open country between the trees.
    """
    
    $ play_music('danger')

    """
    I keep a steady pace for an hour.
    
    Fear is slowly being replaced by hope, and I start to think I might get away.
    """

    return
