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

    $ broken_details.add_checkpoint("broken_day1_evening")

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

    So far, I have been able to play the part without anyone noticing.

    But I have only met strangers.

    The real test will come when I meet the Lady of the house.

    If anyone has any idea who Thomas Moody is, that would be her.
    
    I repeat to myself the details of Thomas's life once more.

    His childhood in Liverpool. The boot-boy years. 
    
    When he joined the army and rose through the ranks, up until the Great War when he became an officer.

    Then the tragedy that changed his life forever.

    When I am certain of every line, I go down to join the others.
    """

    $ change_room('tea_room', dissolve)

    call change_time(15, 45)

    """
    The tea room is empty but for one man — the doctor I shared the car with.
    """

    call common_day1_evening_doctor_broken_introduction

    """
    The doctor makes the usual enquiries. 
    
    Where I am from, what I do, how I came by my injuries.

    I answer as Thomas would have, but I add a brash tone to discourage him from asking too many questions.
    
    It is better to avoid any risk of revealing myself if I can avoid it, and if I sound a bit rude, so be it.

    After a few questions, I realise I should not worry about him.

    The way he nods at my answers without hearing them.

    His eyes drifting to the middle distance, his fingers worrying at the stem of his glass.

    A man waiting for something, or wanting something.

    I have interviewed enough of them to know the look.

    Doctor Baldwin has more pressing things on his mind than trying to find inconsistencies in my story.
    """

    call change_time(16, 30)

    """
    Miss Marsh is the next to arrive.

    She gives a small nod and keeps to herself by the bar.

    Not long after, two more come in together.

    An Indian gentleman in an officer's uniform, upright as a fence-post.

    And behind him an older man who makes straight for the drinks, walking as though the floor could not quite be trusted.

    The older one flounders off towards Miss Marsh.

    The officer comes to us.
    """

    call common_day1_evening_tea_room_captain_arrives

    """
    The captain needs little encouragement to talk.

    One tale leads to another. A drunken officer in Calcutta, supply lines in Burma, a skirmish whose name I half recognise.

    I listen carefully, not that I am really interested. 
    
    But I have learned on the job to never miss a detail when someone is telling a story.
    """

    call common_day1_evening_nurse_joins_captain

    """
    He speaks of a battle scar, then catches himself with a glance at my mask, as though weighing his small wound against my supposed ruin.

    I hold his gaze until he looks away.

    It is the one part of the performance I have come to dread. Not the lying, but the pity that comes with it.
    """

    """
    Two more guests slip in while the captain holds court.

    Ted Harring and Amelia Baxter.

    But I have no time to assess them properly.
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
    Our host turns to me with a hostess's practised smile, ready to begin the rounds of polite enquiry.

    I might not have a better chance to take her measure than I have now.
    """

    call change_time(19, 30)

    $ time_left = 90

    call run_menu(TimedMenu("broken_day1_evening_menu_dinner", [
        TimedMenuChoice("Talk to Lady Claythorn", 'broken_day1_dinner_host', early_exit=True),
        TimedMenuChoice("Keep to yourself", 'generic_cancel', early_exit=True),
    ], image_right = "host"))

    $ stop_music()

    call change_time(21, 00)

    """
    At length the dinner breaks up.

    Lady Claythorn lets it be known that drinks will be laid on in the billiard room for those who care to sit up a while.

    I assume most of the guests will be there, so it is a good opportunity to learn more about them.

    But that also mean there is no better time to explore the house discretely, while the party is gathered in one room and the staff are run off their feet.
    """

    $ change_room('bedroom_broken', dissolve)

    $ unlock_map('bedroom_broken')

    """
    I go back to my room first, to leave my coat and take my bearings.

    Then I set out to see the rest of Claythorn Manor for myself.
    """

    $ play_music('upbeat')

    call change_time(21, 30)

    $ time_left = 90

    call run_menu(broken_details.saved_variables["day1_evening_map_menu"])

    # If the evening ended below stairs, he changes back before retiring.
    call broken_ascend_if_needed

    call change_time(23, 00)

    $ stop_music()

    """
    The hour grows late and the house falls quiet.

    I have seen what there is to see for one night.

    I return to my room.
    """

    $ change_room('bedroom_broken', dissolve)

    """
    I take off the mask and let out a long breath.

    So far, so good. No one has yet seen through Thomas Moody.
    """

    $ play_music('mysterious', 2)

    """
    Then I see it.

    A single sheet of paper, folded once, lying upon my pillow.

    It was not there when I dressed for dinner.

    A cold weight settles behind my ribs.

    Someone has stood in this room while I played the guest below.

    I take up the paper and unfold it beneath the lamp.

    The print faded and the creases gone soft with handling, written in the autumn of 1917.

    It is an old army order, for the transfer of an officer.
    
    One soldier struck off his posting and sent up to a company in Flanders, into the worst of the War. 

    The transferred officer's name: Thomas Moody.
    
    Before that, Thomas, like myself, had the softest billet in the whole Army.

    Minding the gentlemen of the press. Shepherding war correspondents from one safe vantage to the next, well back of the guns, so they might pen their despatches and go home whole.

    When the order came for one of us to go forward, they did not choose me.

    They chose Thomas.

    A boot-boy who had clawed his way to a commission, a temporary gentleman with Liverpool still thick in his vowels. 
    
    Set beside me, he was the cheaper life.

    No one ever writes that reason on an order. But I have always known it, and have never once said it aloud.

    He went forward in my stead, and he came back a ruined man.

    The date of it I have never managed to forget, not for a single day.

    Since then I have carried a press card and taken up the very work we were once only set to guard, as though wearing his trade might settle some part of the debt.

    It never has.

    And at the foot of the order, in a neat staff officer's hand, the name of the man who signed him away.

    Captain S. Sinha, Staff Officer, General Headquarters.

    Sinha.

    The upright officer who held the tea room not five hours ago with his tales of war glory.

    A staff officer at headquarters, for all his soldier's talk. 
    
    A man who never saw battle, yet did not blink at sending others to their deaths.

    And he is sleeping beneath this very roof tonight.
    """

    pause 1.0

    """
    I sit a long while with the paper in my hands.

    Someone wished for Thomas Moody to have this. 

    Was Thomas invited here to exact revenge on Captain Sinha?

    And are the others here for the same purpose?

    The implications ought to frighten me.

    Instead, the image of Tom, dead on his bed, fills me with a mixture of anger and sadness.

    No matter how hard I try, I cannot seem to reason logically.

    Sleep is a long time coming, and when it takes me, I still have no idea of what I am to do tomorrow.
    """

    if broken_details.threads.is_unlocked('butler_surprise'):

        jump broken_ending_day1_throat_cut

    if broken_details.threads.is_unlocked('drink_good_whisky'):

        jump broken_ending_day1_deathbed


    jump broken_day2_morning


# ------------------------------------
#   DINNER SCENES
# ------------------------------------
label broken_day1_dinner_host:

    """
    I should make the most of it.

    I shall conduct the conversation as an interview, and avoid any trivial questions.

    Maybe this way I will learn something useful.
    """

    call host_generic

    return
