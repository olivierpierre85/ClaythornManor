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
    Four people are already here.

    I am not surprised to see Samuel Manning next to the tray of drinks.

    He is trying to engage in conversation with a woman who seems rather embarrassed.

    I could go and rescue her, but I don't really feel like dealing with Mr Manning right now.

    I also spot two men in quiet conversation.

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

    The Anglo-Zanzibar War. The shortest war in the history of Great Britain.

    Not that anyone here is likely to remember that detail.
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
    """

    """
    Then, our host makes her entrance.

    She is younger than I expected. Elegantly dressed, with the quiet confidence of old money.

    She takes her seat at the head of the table.
    """

    """
    I watch her closely as she settles in.

    Her posture is excellent. Her gestures are graceful.

    And yet there is something oddly deliberate about every movement.

    It is not the ease of someone born into this. It is the precision of someone who has studied it.

    Like an actress performing a part she has rehearsed too many times.
    """

    call common_day1_evening_host_welcome_speech

    """
    One thousand pounds, shared among seven guests. Roughly one hundred and forty each.

    Not as much as I had hoped, but still a significant sum.

    If used wisely, it could open the right doors.

    The first course is served shortly after.
    """

    $ captain_details.description_hidden.unlock('heroic_act')

    """
    As we begin to eat, I notice Miss Baxter turning to her right.

    She has struck up a conversation with Mr Harring.

    That is unusual. In a formal setting, one addresses the person on one's left first.

    I am on her left. She ought to have spoken to me.

    Either she is unaware of the convention, or she is deliberately avoiding me.

    Given our car ride, I suspect the latter.
    """

    $ captain_details.description_hidden.unlock('table')

    """
    After a while, she seems to have exhausted her conversation with the young man.

    She turns to me at last.
    """

    call change_time(19, 30)

    $ time_left = 90
    call run_menu(TimedMenu("captain_day1_evening", [
        TimedMenuChoice("Talk to Amelia Baxter", 'captain_day1_dinner_psychic', early_exit=True),
        TimedMenuChoice("Eat in dignified silence", 'generic_cancel', early_exit=True),
    ], image_left = "psychic"))

    call change_time(21, 00)

    """
    The dinner draws to a close.

    Lady Claythorn mentions that drinks will be available in the billiard room for those who wish to continue the evening.

    First, I should like to see my room. I have not yet had the chance to settle in.

    I ask the footman to show me the way.
    """

    $ change_room('bedrooms_hallway', dissolve)

    footman """
    Here you are, Captain.

    You've been assigned the 'George I' room.
    """

    $ unlock_map('bedroom_captain')

    $ change_room('bedroom_captain', dissolve)

    """
    The room is adequate. Not extravagant, but respectable.

    'George I.' An ordinary room named after an ordinary King.

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
    I change and prepare for bed with military efficiency.

    As I lie down, I review the evening.

    I have done well. Nobody suspects a thing.

    My stories held their attention, and I avoided any question that might have caught me out.

    Tomorrow, I shall do the same.

    With that thought, I close my eyes.
    """

    $ stop_music()

    jump work_in_progress


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label captain_day1_dinner_psychic:

    psychic """
    Well, Mr Sinha. It seems we are neighbours again.
    """

    """
    She smiles. But I know what comes next. Questions.

    Questions about where I am really from. About my rank. About my service.

    I have learnt that the best defence against questions is to leave no room for them.
    """

    captain """
    Indeed, Miss Baxter. And I must say, this is a remarkable setting.

    It reminds me of the officers' mess in Calcutta. Not in style, of course, but in atmosphere.

    There was a hall there, built during the time of Lord Wellesley, with the most extraordinary ceiling.

    Painted by an Italian artist whose name escapes me now, but the detail was remarkable.

    Every panel depicted a different campaign of the East India Company.

    I used to stand beneath it and study the brushwork during long evenings when the heat made sleep impossible.
    """

    psychic """
    How fascinating. But I was merely asking—
    """

    captain """
    And speaking of ceilings, have you noticed the plasterwork in this dining room?

    It is Georgian, if I am not mistaken. The acanthus motifs along the cornice are quite distinctive.

    In London, one sees a great deal of Adam-style ornamentation, but this is earlier.

    More restrained, if you will. Quite tasteful.
    """

    """
    She has stopped trying to interject.

    Good. That is precisely the effect I was hoping for.

    The key is to sound knowledgeable without saying anything of substance.

    It is a skill I have perfected over many years.
    """

    psychic """
    You are certainly well-informed, Captain.
    """

    captain """
    One picks things up. The army takes you to a great many places.

    Have I told you about the time I was stationed near the Khyber Pass?

    The light there in the early morning is unlike anything you have ever seen.

    It catches the mountains in such a way that—
    """

    psychic """
    I think the next course is arriving.
    """

    """
    She turns back to her plate with a tight smile.

    Excellent. Another conversation in which I have said a great deal and revealed nothing.

    She is sharp, this Miss Baxter, but she will not catch me out so easily.
    """

    return
