# Map choices for Doctor, Friday evening
label doctor_day1_evening_map_menu:
    python:        
        # Map choices
        doctor_day1_evening_map_menu = TimedMenu(
            "doctor_day1_evening_map_menu", 
            [
            # Default values
            TimedMenuChoice(default_room_text('storage'), 'doctor_day1_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'doctor_day1_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'doctor_day1_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'doctor_day1_evening_butler_room', 10, room='butler_room'),
            #bedroom
            TimedMenuChoice(default_room_text('bedroom_lad'), 'doctor_day1_evening_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'doctor_day1_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'doctor_day1_evening_bedroom_host', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_broken'), 'doctor_day1_evening_bedroom_broken', 10, room='bedroom_broken'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'doctor_day1_evening_bedroom_nurse', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('tea_room'), 'doctor_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'doctor_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'doctor_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'doctor_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'doctor_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'doctor_day1_evening_downstairs_default', 0, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'doctor_day1_evening_downstairs_default', 0, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'doctor_day1_evening_downstairs_default', 0, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'doctor_day1_evening_downstairs_default', 0, room='gun_room'),
            # Specific actions
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'doctor_day1_evening_bedroom_drunk', 10, room='bedroom_drunk', next_menu="doctor_day1_evening_bedroom_drunk"),
            TimedMenuChoice(default_room_text('library'), 'doctor_day1_evening_library', 0, next_menu="doctor_library_default", room='library'),
            TimedMenuChoice(
                default_room_text('bedroom_psychic'), 
                'doctor_day1_evening_bedroom_psychic', 
                10, 
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                'Meet the others in the billiard room', 
                'doctor_day1_evening_billiard_room', 
                0,
                room = 'billiard_room',
                next_menu = 'doctor_day1_evening_billiard_room_menu'
            ), 
            TimedMenuChoice(
                'Go to sleep', 
                'generic_cancel', 
                early_exit = True, 
                room = 'bedroom_doctor'
            )
        ], is_map = True)
    
    return


label doctor_day1_evening_downstairs_default:

    # Hide all downstairs choices for the current menu
    $ all_menus[doctor_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[doctor_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[doctor_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[doctor_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

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
            TimedMenuChoice("Try flirting with him", 'doctor_downstairs_flirt', 30, early_exit=True),
            TimedMenuChoice("No, he clearly won't change his mind", 'doctor_downstairs_apologize', 20, early_exit=True),
        ])
    )

    return


label doctor_downstairs_flirt:

    doctor """
    That's a shame, but I quite understand. Orders are orders.

    Still, I had rather hoped you might show me around.

    There are a few things I'd not mind discussing with you.
    """

    footman """
    I'm a bit tied up at the moment, sir.

    But I could make time later, if you'd still care to talk.
    """

    doctor """
    I'd like that very much.

    Where shall we meet?
    """

    footman """
    Hard to say when I'll be free.

    But I could stop by your room once I've a moment—if you don't mind, that is.
    """

    """
    Well, that is rather forward.

    I glance about to be sure we're alone.

    We are.

    I let my gaze linger a moment longer than necessary.
    """

    doctor """
    Are you certain you can't come now?
    """

    footman """
    No, truly I can't.

    But I'll be done soon enough.

    I'll see you later then, Doctor Baldwin.
    """

    doctor """
    Please—call me Daniel.
    """

    footman """
    Very well, Daniel. I'm Andrew.
    """

    doctor """
    I'll see you later, Andrew.
    """

    $ doctor_details.threads.unlock('flirt')

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

    But maybe I can borrow something else to read later in my room?

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

    #TODO: Other possibilities OR for someone else (nurse?) => GIVE it to drunk

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

    $ doctor_details.threads.unlock('book_mystery')

    return


label doctor_day1_evening_library_book_opium:

    """
    I have been meaning to read this for a long time.

    Maybe now is the time.
    """

    $ doctor_details.threads.unlock('book_opium')

    return


label doctor_day1_evening_tea_room:
    call doctor_tea_room_default
    return


label doctor_day1_evening_dining_room:
    call doctor_dining_room_default
    return


label doctor_day1_evening_garden:

    $ change_room('entrance_hall')

    """
    From the great hall, I am ready to go and have a look outside.

    But the weather has worsened, I do not think it is safe to go out tonight.
    """

    return


label doctor_day1_evening_entrance_hall:
    call doctor_entrance_hall_default
    return

label doctor_day1_evening_portrait_gallery:
    call doctor_portrait_gallery_default
    return

# First Floor
label doctor_day1_evening_bedroom_drunk:
    
    call doctor_bedroom_default

    play sound door_open

    """
    My knocking slightly opens the door.

    From the hallway, I can see part of the room.

    It is in a dreadful state.

    Should I take a peek?
    """

    if doctor_details.endings.is_unlocked('shot_by_drunk'):
        
        """
        I know and it's probably a bad idea and that I should close this door.

        But I've got an intrusive feeling that if don't enter, something bad will happen.

        That is obviously silly, but...
        """
        
        call run_menu( 
            TimedMenu("doctor_day1_evening_bedroom_drunk", [
                TimedMenuChoice("Follow your intuition, they exist for a reason{{intuition}}", "doctor_day1_evening_bedroom_drunk_enter", 20, next_menu="doctor_day1_evening_bedroom_drunk_enter", early_exit=True),
                TimedMenuChoice("Don't be ridiculous, there is no such thing as premonition", "doctor_day1_evening_bedroom_drunk_not_enter", early_exit=True),
            ])
        )

    else:

        pause 1.0

        call doctor_day1_evening_bedroom_drunk_not_enter

    return


label doctor_day1_evening_bedroom_drunk_not_enter:

    """
    Why am I thinking, there is no reason for me to intrude.

    I close the door and leave.
    """

    return


label doctor_day1_evening_bedroom_psychic:
  
    call doctor_bedroom_psychic_evening

    return


label doctor_bedroom_psychic_evening:

    call doctor_bedroom_default

    psychic """
    Yes? Who is it?
    """ 

    doctor """
    It's Doctor Baldwin.
    """

    psychic """
    Yes, Doctor, what can I do for you?
    """
    
    doctor """
    I just wanted to have chat. Do you have time?
    """

    psychic """
    I'm afraid It's a bit too late for me.

    But we can speak again tomorrow.
    """

    doctor """
    Of course, I am sorry.
    """
    
    $ unlock_map('bedroom_psychic')

    return

# Closed bedrooms
label doctor_bedroom_stay_away:

    """
    Should I try to see what's inside?

    No, of course not. 

    Most people are downstairs now, but they could come back anytime.

    Also, that's wildly inappropriate.
    """
    
    return


label doctor_day1_evening_bedroom_captain:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_host:
    call doctor_bedroom_default
    call doctor_bedroom_stay_away
    return

label doctor_day1_evening_bedroom_lad:
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