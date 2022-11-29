label psychic_generic_other_guests:

    if not 'psychic_generic_other_guests_menu' in locals():
        $ psychic_generic_other_guests_menu = TimedMenu([
            # Saturday Morning
            TimedMenuChoice('Ask about Samuel Manning', 'psychic_generic_drunk_saturday_morning', 5, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
            TimedMenuChoice('Ask about Sushil Sinha', 'psychic_generic_captain_saturday_morning', 5, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
            TimedMenuChoice('Ask about Lady Claythorn', 'psychic_generic_host_saturday_morning', 5, condition = "(current_day == 'Saturday' and current_phase == 'Morning')"),
            
            # TimedMenuChoice('Ask about Thomas Moody', 'psychic_generic_broken_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
            # TimedMenuChoice('Ask about Rosalind Marsh', 'psychic_generic_nurse_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
            # TimedMenuChoice('Ask about Daniel Baldwin', 'psychic_generic_doctor_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
            # Always Generic 
            TimedMenuChoice('Talk about something else', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
        ], image_right = "psychic")

    call run_menu(psychic_generic_other_guests_menu)

    return

label psychic_generic_other_guests_saturday_morning:
    psychic """
    I haven't had time to make an opinion everyone yet.

    I was just able to get to know Captain Sinha, our host and the sorry drunk there.

    And I could only exchange a few words with our hostess, Lady Claythorn.
    """

    call psychic_generic_other_guests

    return

label psychic_generic_other_guests_friday:
    # DRINKS AND DINNER
    psychic """
    I've just met them. So I can't say to know a lot yet.

    All I know is that this guy over there ...
    """

    """
    She points at Sushil Sinha.
    """

    psychic """
    ... is monopolizing the conversation.

    And he is very noisy too.

    It's not very tactful if you ask me.
    """

    $ captain_details.add_knowledge('talker') 

    return

label psychic_generic_drunk_saturday_morning:

    psychic """
    Well, I think by now you can tell as well as I that he is a dangerous drunk.

    We better stay away from him.
    """

    $ drunk_details.add_knowledge('addict') 

    return

label psychic_generic_captain_saturday_morning:

    psychic """
    He looks to me like the typical military man.

    Except for, you know, his origin.

    I didn't think they would accept indigenous people in the British Army.

    But beside that, he is exactly like other officer I met.

    Bold, sure of himself, and not ashamed to talk about himself.

    I bet he will keep on telling stories about his \"Glorious Days\" during one war or another.

    I think is in bad taste, so I will try to avoid him in the coming days.

    I suggest you do the same, unless you want to be bored to death.
    """

    $ captain_details.add_knowledge('talker') 

    return

label psychic_generic_host_saturday_morning:

    psychic """
    I could only exchange a few pleasantries with the Lady of the house.

    She seems delightful to me.

    She addressed me as an equal, unlike some stuffed people in the gentry would do.
    """

    return

# label psychic_generic_broken_saturday_morning:

#     psychic """
#     broken
#     """

#     return

# label psychic_generic_doctor_saturday_morning:

#     psychic """
#     doctor
#     """

#     return

# label psychic_generic_nurse_saturday_morning:

#     psychic """
#     nurse
#     """

#     return

