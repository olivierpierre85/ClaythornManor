 
label doctor_generic():

    if not 'doctor_generic_menu' in locals():
        $ doctor_generic_menu = TimedMenu([
            TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_friday', 5, condition = "current_day == 'Friday'"),
            TimedMenuChoice('What do you think of this weather?', 'doctor_generic_weather_saturday', 5, condition = "current_day == 'Saturday'"),
            TimedMenuChoice('Tell me more about yourself.', 'doctor_generic_background', 20),
            TimedMenuChoice('Why were you invited here?', 'doctor_generic_heroic_act', 20, condition = "doctor_details.check_knowledge_unlocked('background')"),
            TimedMenuChoice('What do you think of this place?', 'doctor_generic_manor', 10),
            TimedMenuChoice('How old are you?', 'doctor_generic_age', 5),
            TimedMenuChoice('What room are you in?', 'doctor_generic_room', 5),
            TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_friday', 5, condition = "current_day == 'Friday'"),
            TimedMenuChoice('What do you think of the other guests?', 'doctor_generic_other_guests_saturday', 5, condition = "current_day == 'Saturday'"),
            TimedMenuChoice('You don\'t have anymore questions for him', 'doctor_generic_cancel', 0, keep_alive = True, early_exit = True)
            ], image_right = "doctor")
    else:
        # Reset if previous early exit
        $ doctor_generic_menu.early_exit = False

    call run_menu(doctor_generic_menu)
    
    return

label doctor_generic_weather_friday:

    doctor """
    A dreadful storm if you ask me.

    I don't know what's planed for tomorrow, but I hope it won't involve getting out this house.
    """

    return

label doctor_generic_weather_saturday:
    
    doctor """
    We are lucky the weather improved greatly today.

    For a while I thought we would be trapped inside the manor the whole weekend.

    But everything seems fine now.
    """

    return

label doctor_generic_background:

    doctor """
    I am the chief physician at St Margaret's Hospital.

    It's a charity hospital for persons in need.

    Before that I worked a bit everywhere.

    I also served in the war twice. 

    In the last one of course, but I was also in China during the insurrection.
    """

    $ doctor_details.add_knowledge('background') 

    return

label doctor_generic_heroic_act:

    doctor """
    Well, I celebrated my ten years at the St Margaret's recently.

    Not a lot of people remains that long at this type of institution.

    Usually, a doctor stays a few year to get a reputation, then moves on to a more luxurious practice.

    Lady Claythorn must have understood how much of a sacrifice I made, hence the reward.

    Not that I consider it a sacrifice of course.

    I love my job and wouldn't change it for the world.

    Still, it's always nice to get some recognition.
    """
    
    return

label doctor_generic_manor:

    doctor """
    It's a nice house.

    But I couldn't say much more about it. 

    I am not used to visit such places.
    
    That's the first time I am invited in a grand mansion as a guest and not as a doctor.

    The truth is my job doesn't pay as much.

    Nevertheless, I am content with my small apartment.

    I wouldn't want anything this big. It must be such a hassle to manage.
    """

    if current_character.text_id == "lad":
        lad "So you are not accustomed to having a butler, and footmen around ?"

        doctor "No, I can't say that I am."

        "Well, that's a bit comforting."

        $ doctor_details.add_knowledge('status') 

    return

label doctor_generic_age:
    doctor "I am 39 nine years. Why do you ask ?"

    if current_character.text_id == "lad":
        lad "Actually I am not sure."

    $ doctor_details.add_knowledge('age') 
    
    return

label doctor_generic_room:
    doctor "I am in the Edward II room."

    $ unlock_map('doctor_room')
    
    return

label doctor_generic_cancel:
    return