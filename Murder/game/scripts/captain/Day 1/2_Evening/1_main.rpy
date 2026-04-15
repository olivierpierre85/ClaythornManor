# --------------------------------------------
#   Captain
#
#   Friday - Evening
#
#   16:30 -> 23:00
#
#   Music: chill
#
#   Position
#       - Tea Room : Doctor, Broken, Nurse, Drunk
#       - Dinner Room : Everyone
#
#   Notes :
#       - Tea room: meet Doctor, Broken, Nurse
#       - Dinner: Psychic (on his right), Broken across (no talk)
#       - Map visit, 90 minutes
#       - Billiard room: tell Boxer story
# --------------------------------------------
label captain_day1_evening:

    call change_time(16, 30, "Evening", "Friday", hide_minutes = True, chapter='friday_evening')

    $ current_character.add_checkpoint("captain_day1_evening")

    call black_screen_transition("Sushil Sinha", chapters_names[current_chapter])

    $ change_room('entrance_hall', dissolve)

    $ play_music('upbeat')

    """
    We arrive at the manor.

    It is an imposing house. Not the grandest I have seen, but respectable.

    The kind of place I should have been invited to years ago.

    I straighten my jacket and step inside.
    """

    call common_day1_evening_second_arrival_part_1

    """
    Manning is already demanding a drink. The man has no shame.

    But at least he draws attention away from me.
    """

    call common_day1_evening_second_arrival_part_2

    """
    Miss Baxter excuses herself to freshen up in her room.

    Good. I have had quite enough of her questions for now.

    The tea room it is.
    """

    $ change_room('tea_room', dissolve)

    call change_time(16, 45)

    """
    As soon as we enter, Samuel Manning rushes to the tray of drinks.

    There is a woman there already. And Samuel Manning seems to be trying to engage in conversation with her.

    I could go and rescue her, but I do not really feel like dealing with that right now.

    I also spot two men in quiet conversation.

    That seems like a better alternative.

    Time to introduce myself.
    """
    
    call common_day1_evening_tea_room_captain_arrives

    """
    That part, at least, is true.

    I carry on from there. A story about a drunkard officer in Calcutta.

    Then another about the supply lines in Burma.

    And another.

    I can tell the doctor has stopped listening after a while, but Mr Moody seems genuinely interested.

    Then, the woman approaches our group.
    """

    call common_day1_evening_nurse_joins_captain

    """
    That particular scar is from falling off a chair in my office in Calcutta.

    But they do not need to know that.
    """

    $ captain_details.description_hidden.unlock('embellishment')

    """
    I carry on. Miss Marsh listens attentively.

    The doctor, on the other hand, has drifted off entirely. He nods, but his mind is elsewhere.

    Two more guests slip into the room. The butler announces the young man.
    """

    butler """
    Mr Ted Harring!
    """

    """
    He looks out of place. Young, nervous, dressed in clothes that have seen better days.

    I pay him little mind and continue my story.
    """

    $ lad_details.description_hidden.unlock('poor')

    """
    I am in the middle of a rather good tale when the gong interrupts me.
    """

    play sound dinner_gong

    """
    A pity. I was just getting to the best part.
    """

    $ stop_music()

    call change_time(18, 30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    We file into the dining room. Each place is marked with a name card.

    I find mine near the head of the table. A good position.

    Miss Baxter is on my right. Mr Moody sits across from me, but far too distant for conversation.

    Then, our host makes her entrance.

    She is rather young, elegantly dressed, with the quiet confidence of old money.

    She takes her seat at the head of the table.
    """

    call common_day1_evening_host_welcome_speech

    """
    After the speech, I cannot help but notice a tightness in my stomach.

    It reminds me that I am an impostor here, not worthy of any award.

    If I am discovered, not only will I lose the money, but there will certainly be talk about what I have done.

    That could hurt my reputation.

    So I should watch what I am saying carefully.

    As we begin to eat, I notice Miss Baxter turning to her right.

    She has struck up a conversation with Mr Harring.

    That is unusual. In a formal setting, one addresses the person on one's left first.

    So she ought to have spoken to me.

    Either she is unaware of the convention, or she is deliberately avoiding me.

    It could be the latter. But as I examine the other guests, small lapses begin to reveal themselves.

    Mr Manning holds his wine glass by the bowl, not the stem.

    Mr Harring hesitates over his cutlery, glancing at his neighbour before choosing a fork.

    Dr Baldwin has not touched his napkin at all. It lies folded beside his plate, forgotten.

    Small things. The sort a man like me has trained himself to notice in others.

    None of them are accustomed to proper company. That much is plain enough.

    Then my gaze drifts to the head of the table, and I pause.

    Lady Claythorn reaches for her bread roll and picks up the butter knife.

    She cuts the roll in half and butters it whole.

    A small thing. Invisible to most at this table.

    But one does not butter an entire roll. One breaks off a single piece and attends to that alone.

    I have been told that so many times I cannot fail to notice it.

    Of all the people at this table, I did not expect that from her.

    Then again, this alone probably means nothing. 
    
    With a manor this remote, perhaps she has simply not had occasion for proper company in some time, so she has forfeited some of the usual habits.
    """
    
    pause 1.0

    """
    After a while Miss Baxter seems to have exhausted her conversation with the young man.

    I can talk to her now if I please.
    """

    call change_time(19, 30)

    $ time_left = 1
    call run_menu(TimedMenu("captain_day1_evening", [
        TimedMenuChoice("Talk to Amelia Baxter", 'captain_day1_dinner_psychic', early_exit=True),
        TimedMenuChoice("Ignore her", 'captain_day1_dinner_no_talk', early_exit=True),
    ], image_left = "psychic"))

    call change_time(21, 00)

    """
    The dinner reaches its conclusion.

    Lady Claythorn mentions that drinks will be available in the billiard room for those who wish to continue the evening.

    First, I should like to see my room. I have not yet had the chance to settle in.

    I ask the footman to show me the way.
    """

    $ change_room('bedrooms_hallway', dissolve)

    footman """
    Here you are, Captain.

    You've been assigned the 'George I' room.
    """

    $ change_room('bedroom_captain', dissolve)
    
    $ unlock_map('bedroom_captain')

    """
    The room is adequate. Not extravagant, but respectable.

    Still, it is more comfortable than my lodgings in London.

    I unpack quickly and consider my options.
    """

    $ play_music('upbeat')

    call change_time(21, 30)

    $ time_left = 90

    call run_menu(captain_details.saved_variables["day1_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    """
    The hour is late and the house has grown quiet.

    I return to my room.
    """

    $ change_room('bedroom_captain', dissolve)

    """
    I change and prepare for bed while I review the evening in my head.

    I have done well. Nobody suspects a thing.

    My stories have held their attention, and I have avoided any question that might have caught me out.

    If I can keep doing this, I might be able to get out of here with the reward without anyone the wiser.

    I turn back the covers and find a folded sheet of paper resting on the pillow.

    Plain. Unmarked.

    I pick it up and unfold it.
    """

    $ play_music('scary')

    letter """
    You are a fraud.
    """

    """
    My hand stills.

    For a moment, I am frozen, unable to react.

    I gather all my strength not to panic.

    I breathe. I think.
    
    I set the paper down. 

    Someone in this house knows. Someone has been in this very room tonight and placed this where I could not miss it.

    But why?

    Is it a threat? A warning?

    And from whom? 

    From the Mistress of this place? Then this whole weekend could be designed just to torture me?

    But I cannot see a reason why — I have no enemies, not real ones at least.

    It could also come from a guest. 
    
    Someone who knows me, and realised I do not belong here.

    But then, why not say it in front of everybody?

    To torture me?

    I sit on the edge of the bed. I go through every face at dinner, trying to remember someone.

    I find nothing.

    Unless, of course, the culprit is the person behind the mask.

    The other military man in the house.

    Thomas Moody is the most likely to have recognised me, realised I am not who I claim to be, and decided to make me pay for it.

    Still, he did not show it at all tonight.

    I stay still for a while, trying to make sense of this, but cannot.
    """

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        And the letter is not the only thing weighing on my mind.

        Lady Claythorn, from what I have learnt tonight, could be an impostor too.
        
        No more the mistress of this manor than I am a decorated war hero.

        Perhaps we all are. 
        
        Perhaps this whole weekend is some elaborate piece of theatre, and each of us has been handed a part to play.
        """

    $ stop_music()

    """
    The question now is what to do.

    I could flee. Leave this place and everyone behind.

    But then I would give up the money.

    The letter's goal could be to make me do just that.

    But I cannot. I will not.

    I have come too far, put too much hope in this journey to give up now.

    Whatever is at play here, I will stay at least until tomorrow, and decide accordingly.    

    I lie back, but sleep does not come easily.
    """

    $ stop_music()

    jump captain_day2_morning


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label captain_day1_dinner_no_talk:

    """
    I decide that the best way not to be discovered is to simply keep to myself.

    So I do not engage with Miss Baxter.

    She does not seem to mind.

    We eat in silence until the end of dinner.
    """

    return


label captain_day1_dinner_psychic:

    captain """
    Miss Baxter.
    """

    call captain_psychic_should_talk_to_captain_first

    """
    She gives me an annoyed look. I do not think she was expecting to be put back in her place by someone like me.

    That gives me a small feeling of satisfaction.

    She then proceeds to ask me questions about myself, and I make sure each answer is filled with inconsequential details.

    Hopefully, if I drown her in information, she might not notice any inconsistencies.

    When the dinner reaches its conclusion, I realise I have not even asked her anything about herself.
    """

    return
