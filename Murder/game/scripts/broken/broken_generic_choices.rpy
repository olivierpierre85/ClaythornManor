
# Generic Broken Dialogs.
# Accessible from :
#                   - Doctor
#                   - ?


label broken_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["broken_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["broken_generic_menu"])
    
    return

label broken_generic_other_guests_friday:

    broken """
    Another guest? You mean Miss Marsh, I assume?
    """

    doctor """
    Well, yes, of course. We haven't met anyone else yet, have we?
    """

    broken """
    Right.

    I am not sure. She was very quiet during our trip.

    But being alone with men around her must have made her uneasy.
    """

    """
    Yes, that or something else must have scared her.

    But there is no reason to point it out.
    """

    return

label broken_generic_weather_friday:

    broken """
    It's not the ideal weather, but there's no reason to lose sleep over it.
    """

    return


label broken_generic_background:

    "todo"

    # # TODO add city for the hospital (when i decide where he is from)
    # broken """
    # I am the chief physician at St. Margaret's Hospital.

    # It's a charity hospital for those in need.

    # Before that, I worked a bit all over the place.

    # I also served in the army several times, including the last one. 

    # That one was the worst, of course.
    # """

    # $ broken_details.description_hidden.unlock('background')
     
    # $ current_character.saved_variables["knows_broken_background"] = True

    return

label broken_generic_heroic_act:

    "todo"

    # broken """
    # Well, I recently celebrated my ten years at St. Margaret's.

    # Not many people stay that long at this type of institution.

    # Usually, brokens stay for a few years to build a reputation, then move on to a more luxurious practice.

    # Lady Claythorn must have understood the sacrifice I've made, hence the reward.

    # Not that I consider it a sacrifice, of course.

    # I love my job and wouldn't change it for the world.

    # Still, it's always nice to receive some recognition.
    # """
    
    # $ broken_details.description_hidden.unlock('heroic_act')
    
    return

label broken_generic_manor:

    "todo"

    # broken """
    # It's a nice house.

    # But I can't say much more about it. 

    # I'm not used to visiting such places.

    # This is the first time I've been invited to a grand mansion as a guest and not as a broken.

    # The truth is, my job doesn't pay that much.

    # Nevertheless, I'm content with my small apartment.

    # I wouldn't want anything this big; it must be such a hassle to manage.
    # """

    # if current_character.text_id == "lad":
    #     lad """
    #     So you're not accustomed to having a butler and footmen around?
    #     """

    #     broken """
    #     No, I can't say that I am.
    #     """

    #     """
    #     Well, that's somewhat comforting.
    #     """

    #     $ broken_details.description_hidden.unlock('status') 

    return

label broken_generic_age:

    "todo"

    # broken """
    # I'm 39 years old. Why do you ask?
    # """

    # if current_character.text_id == "lad":
    #     lad """
    #     Actually, I'm not sure.
    #     """

    # $ broken_details.description_hidden.unlock('age') 
    
    return

label broken_generic_room:

    "todo"

    # broken """
    # I'm staying in the Edward II room.
    # """

    # # TODO: Add more dialogue if lad, or broken (invite to room?)
    # $ unlock_map('bedroom_broken')
    
    return
