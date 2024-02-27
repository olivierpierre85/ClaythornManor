label nurse_generic_other_guests_saturday:

    nurse """
    Oh, up until now, I've mostly kept to myself.

    I haven't talked to many people.

    I am seated next to Samuel Manning, but we haven't had a very deep conversation yet.

    Our host is the only other person I've had any real exchange with.

    But we stuck mostly to simple pleasantries.
    """

    call run_menu(current_character.saved_variables["nurse_generic_other_guests_menu"])

    return



label nurse_generic_drunk_saturday_morning:

    nurse """
    I usually don't like to spread gossip.

    But in this case, I don't think it's a big secret.

    I believe Samuel Manning is an alcoholic.

    He was barely intelligible both at dinner yesterday and this morning.

    Those were two pretty unpleasant meals for me.
    """

    if current_character.text_id == "psychic":

        """
        Well, that's nothing I didn't already know.
        """


    $ drunk_details.unlock_knowledge('addict') 

    return


label nurse_generic_host_saturday_morning:

    nurse """
    I only share a few words with the Lady of the house.

    I tried to know more about the details of the Manor, the staff, that sort of things.
    
    She was quite polite, but her responses were short and not very informative.

    I hope I wasn't rude to her.
    """

    return

# label nurse_generic_other_guests_saturday_morning:

#     call nurse_generic_other_guests_saturday

#     call nurse_generic_other_guests

#     $ lad_details.saved_variables["psychic_generic_other_guests_saturday_morning_ask"] = True

#     return
    

# label nurse_generic_other_guests_saturday_hunt:

#     if not lad_details.saved_variables["psychic_generic_other_guests_saturday_morning_ask"]:

#         call nurse_generic_other_guests_saturday

#     else:

#         psychic """
#         You know that I already talked with Samuel Manning, Captain Sinha and our host.
#         """

#     psychic """
#     Now, I also have talked a little with Miss Marsh.
#     """

#     call nurse_generic_other_guests

#     return

# label nurse_generic_other_guests_friday:
#     # DRINKS AND DINNER
#     psychic """
#     I've just met them. So I can't say to know a lot yet.

#     All I know is that this guy over there ...
#     """

#     """
#     She points at Sushil Sinha.
#     """

#     psychic """
#     ... is monopolizing the conversation.

#     And he is very noisy too.

#     It's not very tactful if you ask me.
#     """

#     $ captain_details.unlock_knowledge('talker') 

#     return

# label nurse_generic_drunk_saturday_morning:

#     psychic """
#     Well, I think by now you can tell as well as I that he is a dangerous drunk.

#     We better stay away from him.
#     """

#     $ drunk_details.unlock_knowledge('addict') 

#     return

# label nurse_generic_captain_saturday_morning:

#     psychic """
#     He looks to me like the typical military man.

#     Except for, you know, his origin.

#     I didn't think they would accept indigenous people in the British Army.

#     But beside that, he is exactly like other officer I met.

#     Bold, sure of himself, and not ashamed to talk about himself.

#     I bet he will keep on telling stories about his \"Glorious Days\" during one war or another.

#     I think is in bad taste, so I will try to avoid him in the coming days.

#     I suggest you do the same, unless you want to be bored to death.
#     """

#     $ captain_details.unlock_knowledge('talker') 

#     return


# label nurse_generic_host_saturday_morning:

#     psychic """
#     I could only exchange a few pleasantries with the Lady of the house.

#     She seems delightful to me.

#     What was event better, is that she addressed me as an equal.

#     That's very different that most noble people I've met.
    
#     They usually look down on people like you, ...
    
#     ... and me.
#     """

#     """
#     She paused a little too long before adding \"and me\".

#     I don't like that.
#     """

#     $ host_details.unlock_knowledge('down_to_earth') 

#     return

# label nurse_generic_nurse_saturday_hunt:

#     psychic """
#     For what I've seen, I believe she is a very respectable woman.

#     She worked most of her life as a nurse.

#     So I believe the prize money could help her retire.
#     """

#     $ nurse_details.unlock_knowledge('job') 

#     return

# label nurse_generic_other_guests_saturday_evening:

#     psychic """
#     Good question, we'll be stronger if we know who to be wary of.

#     I've thought about it and Samuel Manning of course is the prime suspect.

#     But he is locked in his room now, so I wouldn't worry about him too much.

#     The other obvious suspect is Thomas Moody. 
    
#     The fact that he wears a mask is the perfect way to hide his true identity.

#     But it was obviously not him.

#     So that leaves us three persons to worry about : Sushil Sinha, Lady Claythorn and Rosalind Marsh.
#     """
    
#     call nurse_generic_other_guests

#     return

# label nurse_generic_captain_saturday_evening:

#     psychic """
#     Captain Sinha is the one I am the most worried about.

#     He the strongest of us, has military experience.
    
#     And he often took command during dramatic moments.

#     Which means he can try to drive us where he wants.

#     But he is also the one that locked Samuel Manning, so I am not sure.
#     """

#     return


# label nurse_generic_host_saturday_evening:

#     psychic """
#     If the money is not the reason behind the murders, then I suppose she would be suspicious.

#     After all, she is the one who called all of us here.

#     But as I said, it would be a lot of work to organize all this, and for what?

#     To kill a few of her enemies?

#     That seem a bit far fetched.

#     Also, she seemed very nice to me. 

#     But of course that doesn't mean much.
#     """

#     return

# label nurse_generic_nurse_saturday_evening:

#     psychic """
#     Miss Marsh definitely doesn't have the type of a killer.

#     But that's not a reason enough to think she couldn't be.

#     She is very discreet.

#     That could be a way to be able to search the manor while she relies on an accomplice for the more \"physical\" part of the robbery.
#     """

#     return