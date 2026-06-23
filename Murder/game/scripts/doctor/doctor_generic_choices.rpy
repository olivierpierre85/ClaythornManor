
# Generic Doctor Dialogs.
# Accessible from :
#                   - Psychic
#                   - Lad
#                   - Broken (via the _broken wrappers below, which call the
#                     generic label and then add Moody's own insight)


label doctor_generic:

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

    # TODO add city for the hospital (when i decide where he is from)
    doctor """
    I am the chief physician at St. Margaret's Hospital.

    It's a charity hospital for those in need.

    Before that, I worked a bit all over the place.

    I also served in the army several times, including the last one. 

    That one was the worst, of course.
    """

    $ doctor_details.description_hidden.unlock('background')
     

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
    
    $ doctor_details.description_hidden.unlock('heroic_act')

    return


# ---------------------------------------------------------------------------
# BROKEN (Thomas Moody) variants
# Each wraps the generic answer and then adds Moody's own observation. Moody is
# an amateur sleuth posing as a maimed war hero, so a fellow veteran draws his
# particular attention.
# ---------------------------------------------------------------------------

label doctor_generic_background_broken:

    call doctor_generic_background

    """
    Several turns with the army, and he lets them pass as plainly as the weather.

    A man who has seen a good deal, then, and learned to keep most of it behind his teeth.

    I know the habit well enough. I wear it myself.
    """

    return


label doctor_generic_heroic_act_broken:

    call doctor_generic_heroic_act

    """
    Ten years at a charity hospital. A worthy thing, no doubt.

    Yet one does not earn a lady's prize for it, and I half expected him to speak of the war instead.

    He served more than once, by his own account. There may be a story there he would sooner not tell.
    """

    return


label doctor_generic_heroic_act_war:

    broken """
    Forgive me, Doctor, but from the way you spoke I had half a mind you were some sort of war hero.
    """

    doctor """
    A hero? No, nothing so grand.

    I served in a few campaigns, that is all. A field surgeon, for the most part.

    The Boxer Rebellion was the first of them. China, the year nineteen hundred.

    I patched up rather more men than I should care to count.
    """

    broken """
    The Boxer Rebellion. That was a hard posting, by all accounts.
    """

    doctor """
    It was. But the prize I am here for has nothing to do with any of that.

    It is the hospital they wished to reward, not the soldier.
    """

    """
    The Boxer Rebellion. I shall keep that in mind.

    A surgeon out in China, all those years ago. One never knows which old thread will prove worth the pulling.
    """

    $ broken_details.threads.unlock('doctor_boxer')

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
        Well, that's rather comforting.
        """

        $ doctor_details.description_hidden.unlock('status') 

    return

label doctor_generic_age:

    doctor """
    I'm 39 years old. Why do you ask?
    """

    if current_character.text_id == "lad":
        lad """
        Actually, I'm not sure.
        """

    $ doctor_details.description_hidden.unlock('age') 
    
    return

label doctor_generic_room:

    doctor """
    I'm staying in the Edward II room.
    """

    # TODO: Add more dialogue if lad, or broken (invite to room?)
    $ unlock_map('bedroom_doctor')
    
    return
