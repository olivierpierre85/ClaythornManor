
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
    The other guests? You mean Miss Marsh, I assume?
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

    broken """
    There is not much to say I am afraid.

    I am working as mechani

    """


    return

label broken_generic_heroic_act:

    "todo"

    # $ broken_details.description_hidden.unlock('heroic_act')
    
    return

label broken_generic_manor:

    broken """
    It's a decent size house.

    Probably originally for a rich local landowner. 

    Though it's not big enough for a important aristocrat like a Duke or an Earl. 

    I don't know much about this Lady Claythorn but her family are probably squires or baronets.

    Unless there are just rich industrialists and they added the "Lady" to add some prestige to their name.

    That would be quite outrageous if this was the case.
    """

    doctor """
    Really? I wouldn't have thought of that.

    Where do you learn all of this?
    """

    broken """
    Because I was raised in house a bit like this one.

    Then the war happened and everything changed.
    """

    doctor """
    You didn't want to keep doing this after the war?

    Maybe it seemed too trivial for you? Still being a servant after such an horrific experience?
    """

    broken """
    Not really, I don't think there is anything wrong with being a servant.
    
    I would have loved to keep doing this job. 
    
    I even hoped to be a butler someday.

    But it turns out a footman as to fit certain characteristics. 

    For instance, they have to be tall. 
    
    I am not sure why but it's a matter of pride for them to have the tallest servants possible.

    It's all part of us being seen as part of the "image" of their property.

    As can guess, when I returned from the war, I was not considered "footman" material and was relegated to grunt work.

    I decided it was better to leave.

    But it's not easy talking about it.
    """

    doctor """
    I am sorry, I didn't mean to offend you.
    """

    broken """
    Don't worry about it.
    """

    """
    He looks really upset though, I might shouldn't have pushed him like that.
    """

    $ broken_details.description_hidden.unlock('background') 

    return


label broken_generic_age:

    broken """
    27 years old.

    I know it's hard to guess considering.
    """

    doctor """
    I am sorry, I didn't want to imply anything.
    """

    broken """
    Don't worry about it.
    """

    """
    Well I wasn't very polite here. 
    
    I should watch what I am saying.
    """

    $ broken_details.description_hidden.unlock('age') 
    
    return

label broken_generic_room:

    "todo"

    # broken """
    # I'm staying in the Edward II room.
    # """

    # # TODO: Add more dialogue if lad, or broken (invite to room?)
    # $ unlock_map('bedroom_broken')
    
    return
