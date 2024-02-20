label doctor_generic():

    # Reset if previous early exit
    $ current_character.saved_variables["doctor_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["doctor_generic_menu"])
    
    return

label doctor_generic_weather_friday:

    doctor """
    A dreadful storm, if you ask me.

    I don't know what's planned for tomorrow, but I hope it doesn't involve leaving this house.
    """

    return

label doctor_generic_weather_saturday:
    
    doctor """
    We are lucky that the weather improved greatly today.

    For a while, I thought we would be trapped inside the manor all weekend.

    But everything seems fine now.
    """

    return

label doctor_generic_background:

    doctor """
    I am the chief physician at St. Margaret's Hospital.

    It's a charity hospital for those in need.

    Before that, I worked a bit all over the place.

    I also served in the army several times, including the last one. 

    That one was the worst, of course.
    """

    $ doctor_details.unlock_knowledge('background')
     
    $ current_character.saved_variables["knows_doctor_background"] = True

    return

label doctor_generic_heroic_act:

    doctor """
    Well, I recently celebrated my ten years at St. Margaret's.

    Not many people stay that long at this type of institution.

    Usually, doctors stay for a few years to build a reputation, then move on to a more luxurious practice.

    Lady Claythorn must have understood the sacrifice I've made, hence the reward.

    Not that I consider it a sacrifice, of course.

    I love my job and wouldn't change it for the world.

    Still, it's always nice to receive some recognition.
    """
    
    #TODO: Unlock heroic act knowledge
    return

label doctor_generic_manor:

    doctor """
    It's a nice house.

    But I can't say much more about it. 

    I'm not used to visiting such places.

    This is the first time I've been invited to a grand mansion as a guest and not as a doctor.

    The truth is, my job doesn't pay that much.

    Nevertheless, I'm content with my small apartment.

    I wouldn't want anything this big; it must be such a hassle to manage.
    """

    if current_character.text_id == "lad":
        lad """
        So you're not accustomed to having a butler and footmen around?
        """

        doctor """
        No, I can't say that I am.
        """

        """
        Well, that's somewhat comforting.
        """

        $ doctor_details.unlock_knowledge('status') 

    return

label doctor_generic_age:

    doctor """
    I'm 39 years old. Why do you ask?
    """

    if current_character.text_id == "lad":
        lad """
        Actually, I'm not sure.
        """

    $ doctor_details.unlock_knowledge('age') 
    
    return

label doctor_generic_room:

    doctor """
    I'm staying in the Edward II room.
    """

    # TODO: Add more dialogue if lad, or broken (invite to room?)
    $ unlock_map('doctor_room')
    
    return
