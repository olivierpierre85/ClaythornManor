label psychic_generic_other_guests:

    $ condition_saturday_morning = "(current_day == 'Saturday' and current_phase == 'Morning')"
    $ condition_saturday_morning_or_hunt = "(current_day == 'Saturday' and (current_phase == 'Morning' or current_phase == 'Hunt'))"
    $ condition_saturday_hunt = "(current_day == 'Saturday' and current_phase == 'Hunt')"

    if not 'psychic_generic_other_guests_menu' in locals():
        $ psychic_generic_other_guests_menu = TimedMenu([
            # Saturday Morning
            TimedMenuChoice('Ask about Samuel Manning', 'psychic_generic_drunk_saturday_morning', 5, condition = condition_saturday_morning_or_hunt ),
            TimedMenuChoice('Ask about Sushil Sinha', 'psychic_generic_captain_saturday_morning', 5, condition = condition_saturday_morning_or_hunt),
            TimedMenuChoice('Ask about Lady Claythorn', 'psychic_generic_host_saturday_morning', 5, condition = condition_saturday_morning_or_hunt),
            TimedMenuChoice('Ask about Rosalind Marsh', 'psychic_generic_nurse_saturday_hunt', 5, condition = condition_saturday_hunt),

            # TimedMenuChoice('Ask about Thomas Moody', 'psychic_generic_broken_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
            # TimedMenuChoice('Ask about Rosalind Marsh', 'psychic_generic_nurse_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
            # TimedMenuChoice('Ask about Daniel Baldwin', 'psychic_generic_doctor_saturday_morning', 5, condition = "current_day == 'Saturday' and current_phase=='Morning'"),
            # Always Generic 
            TimedMenuChoice('Talk about something else', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
        ], image_right = "psychic")

    call run_menu(psychic_generic_other_guests_menu)

    return

label psychic_generic_other_guests_saturday:

    psychic """
    I haven't had time to make an opinion everyone yet.

    I was just able to get to know Captain Sinha, the sorry drunk that is Samuel Manning.

    And I could also exchange a few words with our hostess, Lady Claythorn.
    """

    return

label psychic_generic_other_guests_saturday_morning:

    call psychic_generic_other_guests_saturday

    call psychic_generic_other_guests

    $ psychic_generic_other_guests_saturday_morning_ask = True

    return

label psychic_generic_other_guests_saturday_hunt:

    if not psychic_generic_other_guests_saturday_morning_ask:

        call psychic_generic_other_guests_saturday

    else:

        psychic """
        You know that I already talked with Samuel Manning, Captain Sinha and our host.
        """

    psychic """
    Now, I also have talked a little with Miss Marsh.
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

    $ captain_details.unlock_knowledge('talker') 

    return

label psychic_generic_drunk_saturday_morning:

    psychic """
    Well, I think by now you can tell as well as I that he is a dangerous drunk.

    We better stay away from him.
    """

    $ drunk_details.unlock_knowledge('addict') 

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

    $ captain_details.unlock_knowledge('talker') 

    return


label psychic_generic_host_saturday_morning:

    psychic """
    I could only exchange a few pleasantries with the Lady of the house.

    She seems delightful to me.

    What was event better, is that she addressed me as an equal.

    That's very different that most noble people I've met, who would look down on people like you, ..., and me.
    """

    """
    She paused a little too long before adding \"and me\".

    I don't like that.
    """

    $ host_details.unlock_knowledge('down_to_earth') 

    return

label psychic_generic_nurse_saturday_hunt:

    psychic """
    For what I've seen, I believe she is a very respectable woman.

    She worked most of her life as a nurse.

    So I believe the prize money could help her retire.
    """

    $ nurse_details.unlock_knowledge('job') 

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

