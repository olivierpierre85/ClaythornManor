# Map choices for Doctor, SATURDAY EVENING
label doctor_day2_evening_map_menu:
    python:        
        # Map choices
        doctor_day2_evening_map_menu = TimedMenu(
            "doctor_day2_evening_map_menu", 
            [
            # Downstairs
            TimedMenuChoice(default_room_text('kitchen'), 'doctor_day2_evening_downstairs_default', 0, room='kitchen'),
            TimedMenuChoice(default_room_text('scullery'), 'doctor_day2_evening_downstairs_default', 0, room='scullery'),
            TimedMenuChoice(default_room_text('garage'), 'doctor_day2_evening_downstairs_default', 0, room='garage'),
            TimedMenuChoice(default_room_text('gun_room'), 'doctor_day2_evening_downstairs_default', 0, room='gun_room'),
            # First floor
            TimedMenuChoice(default_room_text('tea_room'), 'doctor_day2_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'doctor_day2_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'doctor_day2_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'doctor_day2_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'doctor_day2_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(
                'Check who is in the billiard room', 
                'doctor_day2_evening_billiard_room', 
                0,
                room = 'billiard_room',
                next_menu = 'doctor_day2_evening_billiard_room_menu',
                keep_alive = True, 
            ), 
            #bedroom
            # Weird talk with lad who is scared 
            TimedMenuChoice(default_room_text('bedroom_lad'), 'doctor_day2_evening_bedroom_lad', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'doctor_day2_evening_bedroom_captain', 10, room='bedroom_captain'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'doctor_day2_evening_bedroom_host', 10, room='bedroom_host'),
            # Allow to see face a second time if not done on first day
            TimedMenuChoice(default_room_text('bedroom_broken'), 'doctor_day2_evening_bedroom_broken', 10, room='bedroom_broken'),
            # Nurse path
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'doctor_day2_evening_bedroom_nurse', 0, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'doctor_day2_evening_bedroom_drunk', 10, room='bedroom_drunk', next_menu="doctor_day2_evening_bedroom_drunk"),
            TimedMenuChoice(default_room_text('library'), 'doctor_day2_evening_library', 0, next_menu="doctor_library_default", room='library'),
            TimedMenuChoice(
                default_room_text('bedroom_psychic'), 
                'doctor_day2_evening_bedroom_psychic', 
                10, 
                room = 'bedroom_psychic'
            ),
            TimedMenuChoice(
                'Go to sleep', 
                'generic_cancel', 
                early_exit = True, 
                room = 'bedroom_doctor'
            ),
            # Attic
            TimedMenuChoice(default_room_text('storage'), 'doctor_day2_evening_storage', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'doctor_day2_evening_males_room', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'doctor_day2_evening_females_room', 10, room='females_room'),
            TimedMenuChoice(default_room_text('butler_room'), 'doctor_day2_evening_butler_room', 10, room='butler_room'),
        ], is_map = True)
    
    return


label doctor_day2_evening_downstairs_default:

    # Hide all downstairs choices for the current menu
    $ all_menus[doctor_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('gun_room'))
    $ all_menus[doctor_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('garage'))
    $ all_menus[doctor_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('scullery'))
    $ all_menus[doctor_details.saved_variables["day2_evening_map_menu"].id].hide_specific_choice(default_room_text('kitchen'))

    call doctor_downstairs_day2_evening 

    return


label doctor_downstairs_day2_evening:

    $ change_room("basement_stairs")

    """
    I am about to go downstairs when someone stops me.
    """

    maid """
    Good evening, sir. 

    May I help you?
    """

    if doctor_details.threads.is_unlocked('flirt'):

        doctor """
        Well, perhaps. 

        I am looking for someone.
        
        I would like to have a word with your footman. 

        I believe he is called Andrew.
        """

        maid """
        I am sorry, sir, but Andrew is not here any longer. 

        I believe you will find him in his room.
        """

        doctor """
        Very good. 

        And where is that, exactly?
        """

        maid """
        In the attic, sir. 

        The first room to your left after the stairs.
        """

        doctor """
        Perfect, thank you.
        """

        $ unlock_map('bedroom_footman')

    else:

        doctor """
        I was just hoping to have a look downstairs, if you do not mind.
        """

        maid """
        I am sorry, sir, but Lady Claythorn left very strict instructions. 

        No guest is to be allowed downstairs. 

        You may freely visit the rest of the manor, of course.
        """

        doctor """
        I understand.
        """

        """
        Specific instructions forbidding guests to go downstairs do not sit well with me. 

        Still, I do not wish to risk alienating our hostess by forcing my way there. 

        I shall avoid the downstairs rooms, for the moment.
        """

    return


# First Floor
label doctor_day2_evening_library:

    $ change_room("library")

    """
    The library.

    At another time I would gladly have taken a book and settled in to read.

    Tonight however, I feel it is too dangerous to waste time reading.

    I should look elsewhere.
    """

    return


label doctor_day2_evening_tea_room:
    call doctor_tea_room_default
    return


label doctor_day2_evening_dining_room:
    call doctor_dining_room_default
    return


label doctor_day2_evening_garden:

    $ change_room('great_hall')

    """
    I walk to the door that opens on to the garden.

    When I pull it ajar, I find nothing but a wall of darkness beyond.

    It would be far too dangerous to waste time out there at this hour.

    I should turn my attention somewhere else.
    """
    
    return


label doctor_day2_evening_entrance_hall:
    call doctor_entrance_hall_default
    return

label doctor_day2_evening_portrait_gallery:
    call doctor_portrait_gallery_default
    return

# Second Floor
# Closed bedrooms
label doctor_day2_evening_bedroom_closed:

    if not doctor_details.saved_variables["day2_evening_bedroom_closed"]:

        $ doctor_details.saved_variables["day2_evening_bedroom_closed"] = True

        """
        I could try to enter but they might be there and not want to answer.

        So I would look too suspicious now, I should just try somewhere else.
        """
    
    else:

        """
        Nobody is here either.

        I should move on.
        """
    
    return


label doctor_day2_evening_bedroom_captain:
    
    call doctor_bedroom_default
    call doctor_day2_evening_bedroom_closed

    return


label doctor_day2_evening_bedroom_host:

    call doctor_bedroom_default
    call doctor_day2_evening_bedroom_closed

    return

# label doctor_day2_evening_bedroom_drunk:
    
#     call doctor_bedroom_default

#     play sound door_open

#     """
#     My knocking slightly opens the door.

#     From the hallway, I can see part of the room.

#     It is in a dreadful state.

#     Should I take a peek?
#     """

#     if doctor_details.endings.is_unlocked('shot_by_drunk'):
        
#         """
#         I know and it's probably a bad idea and that I should close this door.

#         But I've got an intrusive feeling that if don't enter, something bad will happen.

#         That is obviously silly, but...
#         """
        
#         call run_menu( 
#             TimedMenu("doctor_day2_evening_bedroom_drunk", [
#                 TimedMenuChoice("Follow your intuition, they exist for a reason{{intuition}}", "doctor_day2_evening_bedroom_drunk_enter", 20, next_menu="doctor_day2_evening_bedroom_drunk_enter", early_exit=True),
#                 TimedMenuChoice("Don't be ridiculous, there is no such thing as premonition", "doctor_day2_evening_bedroom_drunk_not_enter", early_exit=True),
#             ])
#         )

#     else:

#         pause 1.0

#         call doctor_day2_evening_bedroom_drunk_not_enter

#     return


# label doctor_day2_evening_bedroom_drunk_not_enter:

#     """
#     Why am I thinking, there is no reason for me to intrude.

#     I close the door and leave.
#     """

#     return


# label doctor_day2_evening_bedroom_psychic:
  
#     call doctor_bedroom_default

#     psychic """
#     Yes? Who is it?
#     """ 

#     doctor """
#     It's Doctor Baldwin.
#     """

#     psychic """
#     Yes, Doctor, what can I do for you?
#     """
    
#     doctor """
#     I just wanted to have chat. Do you have time?
#     """

#     psychic """
#     I'm afraid It's a bit too late for me.

#     But we can speak again tomorrow.
#     """

#     doctor """
#     Of course, I am sorry.
#     """

#     $ unlock_map('bedroom_psychic')

#     return


# # Attic
# label doctor_day2_evening_storage:
#     call doctor_storage_default
#     return

# label doctor_day2_evening_males_room:
#     call doctor_males_room_default
#     return

# label doctor_day2_evening_females_room:
#     call doctor_females_room_default
#     return

# label doctor_day2_evening_butler_room:
#     call doctor_butler_room_default
#     return