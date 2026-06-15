# --------------------------------------------
#   Broken
#
#   Friday - Evening
#
#   14:45 -> ...
#
#   Music: upbeat, chill
#
#   Position
#       - Tea Room : Doctor, then Nurse, Captain, Drunk
#       - Dinner Room : Everyone (seated beside Lady Claythorn)
#
#   Notes :
#       - Tea room: meet Doctor, then Captain, Nurse, Drunk
#       - Dinner: welcome speech, seated next to the host
#       - Generic Host conversation at dinner
#       - Stops at dinner (map choices not yet written)
# --------------------------------------------
label broken_day1_evening:

    call change_time(14, 45, "Evening", "Friday", hide_minutes = True, chapter='friday_evening')

    $ current_character.add_checkpoint("broken_day1_evening")

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room('entrance_hall', dissolve)

    $ play_music('upbeat')

    """
    We step into the hall together, the driver left to wrestle with our luggage.

    The place is handsome enough, but the carpet has worn thin along the line a footman would walk, and the brass wants polishing.

    A house keeping up appearances on a thinning purse.
    """

    call common_day1_evening_doctor_nurse_broken_arrival

    """
    A room to rest in suits me very well.

    It will give me a moment to gather myself.
    """

    $ change_room('bedrooms_hallway', dissolve)

    butler """
    Mr Moody, you are in the 'Richard the Third' room.
    """

    $ change_room('bedroom_broken', dissolve)

    """
    A decent room, if perhaps a bit old-fashioned.

    I sit a while and go over what happened.

    So far, I was able to play the part without nobody noticing.

    But I have only met strangers.

    The real test will come when I will meet the Lady of the house.

    If anyone has any idea who Thomas Moody is, that would be her.
    
    I repeat to myself the details of Thomas's life once more.

    His childhood in Liverpool. The boot-boy years. 
    
    When he joined the army and raised through the ranks.
    
    Until the Great war when he became an officer.
    
    Something his upbringing would have made impossible not so long ago. 

    When I am certain of every line, I go down to join the others.
    """

    $ change_room('tea_room', dissolve)

    call change_time(15, 45)

    """
    The tea room is empty but for one man — the doctor I shared the car with.
    """

    broken """
    Doctor Baldwin, I suppose we are the first ones.
    """

    doctor """
    It seems like it.
    """

    """
    The butler presses a glass of sherry on each of us.

    The doctor makes the usual enquiries. Where I am from, what I do, how I came by my injuries.

    I answer as Thomas would, careful and unhurried, giving each lie the weight of a settled fact.

    It is not the questions that trouble me, but the man asking them.

    He nods at my answers without hearing them.

    His eyes keep drifting to the middle distance, and his fingers worry at the stem of his glass.

    A man waiting for something, or wanting something.

    I have interviewed enough of them to know the look.
    """

    call change_time(16, 30)

    """
    Miss Marsh is the next to arrive.

    She gives a small nod and keeps to herself by the bar.

    Not long after, two more come in together.

    An Indian gentleman in an officer's uniform, upright as a fence-post.

    And behind him an older man who makes straight for the drinks, walking as though the floor could not quite be trusted.

    The older one founders off towards Miss Marsh.

    The officer comes to us.
    """

    call common_day1_evening_tea_room_captain_arrives

    """
    The captain needs little encouragement to talk.

    One tale leads to another. A drunken officer in Calcutta, supply lines in Burma, a skirmish whose name I half recognise.

    I make a show of close attention.

    In truth I am listening for the seams, the small places where a story has been let out or taken in.

    Everyone in this room is performing some version of themselves.

    It is only a question of how well.
    """

    call common_day1_evening_nurse_joins_captain

    """
    He speaks of a battle scar, then catches himself with a glance at my mask, as though weighing his small wound against my supposed ruin.

    I hold his gaze until he looks away.

    It is the one part of the performance I have come to dread. Not the lying, but the pity that comes with it.
    """

    """
    Two more guests slip in while the captain holds court.

    The butler announces the young man.
    """

    butler """
    Mr Ted Harring!
    """

    """
    He is young, and his suit has been brushed once too often.

    A working lad in borrowed feathers, if I am any judge. I should know the look.

    The woman who follows needs no announcement. Her dress sees to that.

    I have no chance to speak to either of them before the gong sounds.
    """

    play sound dinner_gong

    """
    The note rolls through the hall and gathers us up.

    We make our way in to dinner.
    """

    $ stop_music()

    call change_time(18, 30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    Each place is marked with a name card.

    Mine sits near the head of the table, beside the hostess's own chair.

    A better seat than a man like Thomas would expect, which gives me pause.

    Harring is set further down, beside the woman in the fine dress. The officer is across from me, too far off for talk.

    Then the lady of the house makes her entrance.

    She is younger than I had supposed, and carries herself with the easy assurance of someone born to it.

    She takes her place at the head of the table, an arm's length from me.
    """

    call common_day1_evening_host_welcome_speech

    """
    The first course arrives on the heels of her speech.
    """

    pause 1

    """
    I watch her without seeming to.

    It is an old habit, learned below stairs, where one's living depended on reading the family before they had so much as spoken.

    She reaches for her bread roll and takes up the butter knife.

    She cuts the roll clean in two and butters the whole of it.

    The smallest thing.

    But one does not butter a whole roll. One breaks off a single piece and attends to that alone.

    I was corrected on precisely that point more times than I can count, and the lesson never left me.

    A lady raised to this table would not make such a slip.

    Then again, neither would a footman who had spent his life laying it.

    I let the thought settle. Perhaps the manor is not the only thing here wearing a borrowed name.
    """

    $ host_details.description_hidden.unlock('table_manners')

    pause 1.0

    """
    She turns to me with a hostess's practised smile, ready to begin the rounds of polite enquiry.

    I should make the most of it.

    Few here will have a better chance to take her measure than I have now, at her very elbow.
    """

    call change_time(19, 30)

    $ time_left = 90

    call host_generic

    """
    The dinner wears on around us.
    """

    $ stop_music()

    jump work_in_progress
