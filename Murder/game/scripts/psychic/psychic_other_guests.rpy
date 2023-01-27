label psychic_generic_other_guests:

    call run_menu(current_character.saved_variables["psychic_generic_other_guests_menu"])

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

    $ lad_details.saved_variables["psychic_generic_other_guests_saturday_morning_ask"] = True

    return

label psychic_generic_other_guests_saturday_evening:
    # TODO move this to before choices, and leave only thinking about who is involved?
    psychic """
    Good question, we'll be stronger if we know who to be wary of.

    I've thought about it and Samuel Manning of course is the prime suspect.

    But he is locked in his room now, so I wouldn't worry about him too much.

    If what I fear is true, he got help from someone else.
    """

    lad """
    Do you mean a guest? Or someone in the staff could also be involved?
    """

    psychic """
    I wouldn't rule anything, but it's seems less likely that the staff or Lady Claythorn would be involved.

    This would require a tremendous operation.

    No, a more plausible theory is that one or two people heard about the event.
    
    They then stole the place of real guest to infiltrate the place.
    """

    lad """
    But why would they do that?
    """

    psychic """
    Well, it's rather obvious isn't it?

    The price money of course.

    It was mentioned in the invitation letter, the prize will be handed in bearers bond.
    """

    lad """
    Bearers bond? What are those?
    """

    psychic """
    That's a note that you can exchange at the bank without having to prove your identity.

    So it's almost as easy to use as cash.
    """

    lad """
    So you think it could be a simple robbery?
    
    Why not just simply attack the manor?
    """

    psychic """
    It's way easier to enter incognito.

    Observe the castle and then take down potential threat discretely.

    That's the most likely explanation I could come up with.
    """

    return
    

label psychic_generic_other_guests_saturday_hunt:

    if not lad_details.saved_variables["psychic_generic_other_guests_saturday_morning_ask"]:

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

    That's very different that most noble people I've met.
    
    They usually look down on people like you, ...
    
    ... and me.
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

