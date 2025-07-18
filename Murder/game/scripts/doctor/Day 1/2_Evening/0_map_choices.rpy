# Map choices for Doctor, Friday evening
# Downstairs
label doctor_day1_evening_kitchen:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_scullery:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_garage:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_gun_room:
    call doctor_day1_evening_downstairs_default
    return

label doctor_day1_evening_downstairs_default:

    # Hide all downstairs choices for the current menu
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('gun_room'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('garage'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('scullery'))
    $ doctor_details.saved_variables["day1_evening_map_menu"].hide_specific_choice(default_room_text('kitchen'))
        
    call doctor_downstairs_day1

    return


label doctor_downstairs_day1:

    $ change_room("basement_stairs")

    """
    I ought to have a look downstairs. Might be something of interest there.
    """

    footman """
    Good evening, sir. I'm afraid guests aren't permitted beyond this point.
    """

    """
    I offer him my warmest smile.
    """

    doctor """
    I do apologise. I'm only having a quick look. Could you make an exception?

    I promise I won't be long.
    """

    footman """
    If it were up to me, I'd gladly say yes.

    But Lady Claythorn was quite clear with her instructions.

    I'm sure you understand.

    Please don't take it personally.
    """

    """
    He says it with a warm smile of his own.

    His eyes say sorry, but there's something else there, too.

    I wonder if...
    """

    call run_menu(
        TimedMenu("doctor_has_try_sneaking_downstairs", [
            TimedMenuChoice("Try flirting with him", 'doctor_downstairs_flirt', 15, early_exit=True),
            TimedMenuChoice("No, he clearly won't change his mind", 'doctor_downstairs_apologize', 15, early_exit=True),
        ])
    )

    return


label doctor_downstairs_flirt:
    
    $ doctor_details.important_choices.unlock('flirt')

    doctor """
    That's a shame, but I do understand. Orders are orders.

    Still, I was rather hoping you'd show me around.

    There are a few things I wouldn't mind chatting to you about.
    """

    footman """
    I'm a bit tied up at the moment.

    But I could make time later, if you'd still like to talk.
    """

    doctor """
    I'd like that very much.

    Where shall we meet?
    """

    footman """
    Hard to say when I'll be free.

    But I could pop by your room once I've a moment—if you don't mind.
    """

    """
    Well, that is rather forward.

    I glance around to check we're alone.
    
    We are.

    I give him a meaningful look.
    """

    doctor """
    Are you sure you can't come right now?
    """

    footman """
    No, I really can't.

    Sadly, I have other cats to whip.

    But I'll be done soon.
    """

    """
    Wait, what?
    """

    footman """
    I'll see you later, then.
    """

    doctor """
    Yes... Of course.

    See you later.
    """

    """
    What did he say about cats?

    That's odd.

    I must have misunderstood.
    """

    $ doctor_details.observations.unlock('footman_french_1')

    return


label doctor_downstairs_apologize:

    doctor """ 
    Quite right.

    I'll be off, then.

    Good evening.
    """

    footman """
    Good evening, sir.
    """

    return


# First Floor
label doctor_day1_evening_library:

    $ change_room('library')

    """
    That is a well-furnished library.

    It's been a while since I've seen that many books.

    There is one already opened on a desk.

    "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain."

    That sounds tedious.

    But maybe I can borough something else to read later in my room?

    I'm sure our host won't mind.
    """

    call wait_screen_transition()

    """
    I looked around for a book that might be of interest, and found a couple of options.
    """

    call run_menu(TimedMenu("doctor_library_default", [
        TimedMenuChoice('Take "The Mysterious Affair at Styles" by Agatha Christie', 'doctor_day1_evening_book_mystery', early_exit=True),
        TimedMenuChoice('Take "Confessions of an English Opium-Eater" by Thomas De Quincey', 'doctor_day1_evening_library_book_opium', early_exit=True),
        TimedMenuChoice("On second thought, I'd better not take anything", 'generic_cancel', early_exit=True),
    ]))

    #TODO: Other possibilities OR for someone else (nurse?)

        # 2. "The Tenant of Wildfell Hall" by Anne Brontë (1848)
        # Type: Novel

        # Addiction: Alcoholism

        # Summary: Features a strong female protagonist who flees an abusive, alcoholic husband. The novel critiques the destructive impact of addiction on family life.

        # Significance: Ahead of its time in addressing addiction, women's autonomy, and moral responsibility.

    return


label doctor_day1_evening_book_mystery:

    """
    That appears to be the most recent book they have.
    
    A mystery novel.

    I don't know the author, but a quick look at her biography tells me she was a nurse during the war.
    
    So I feel like I could relate to the her.
    """

    $ doctor_details.objects.unlock('book_mystery')

    return


label doctor_day1_evening_library_book_opium:

    """
    I have been meaning to read this for a long time.

    Maybe now is the time.
    """

    $ doctor_details.objects.unlock('book_opium')

    return

label doctor_day1_evening_tea_room:
    call doctor_tea_room_default
    return

label doctor_day1_evening_dining_room:
    call doctor_dining_room_default
    return

label doctor_day1_evening_garden:

    $ change_room('great_hall')
    
    # """
    # I reach the great hall and prepare to open the door. 

    # However, the weather is so bad that only a madman would venture out now. 

    # I'd be better off doing something else at the moment.
    # """

    return


label doctor_day1_evening_entrance_hall:
    call doctor_entrance_hall_default
    return

label doctor_day1_evening_portrait_gallery:
    call doctor_portrait_gallery_default
    return

# Closed bedrooms
label doctor_bedroom_stay_away:

    """
    Should I try to enter anyway?

    No, that's probably a bad idea.
    """
    
    return

label doctor_day1_evening_bedroom_doctor:

        # TODO do drugs if you chose to go to your room early
    # => Death

    return

label doctor_day1_evening_bedroom_captain:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_host:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_drunk:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_broken:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_nurse:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

# Attic
label doctor_day1_evening_storage:
    call doctor_storage_default
    return

label doctor_day1_evening_males_room:
    call doctor_males_room_default
    return

label doctor_day1_evening_females_room:
    call doctor_females_room_default
    return

label doctor_day1_evening_butler_room:
    call doctor_butler_room_default
    return