label doctor_day3_afternoon_captain:

    $ change_room("tea_room", irisout)

    """
    We are all seated in the tea room, Captain Sinha, Ted Harring, Amelia Baxter and me.

    Each of us is deep in thought.

    The manor feels hollow now, stripped of its usual life.

    Captain Sinha breaks the silence.
    """

    captain """
    Whatever happened here was coordinated.

    Staff and guests alike did not simply wander off.
    """

    lad """
    But why?
    """

    """
    Captain Sinha leans towards me and whispers in my ear.
    """

    captain """
    Perhaps it is better to tell them everything.

    We might need their help if we are to get out of here intact.

    What do you think, Doctor?
    """

    psychic """
    Excuse me, what are you two whispering about?

    Is there something we should know?
    """

    $ time_left = 1
    call run_menu( TimedMenu("doctor_day3_afternoon_captain_choice", [
            TimedMenuChoice("Share what you know with the others", "doctor_day3_afternoon_captain_share", 0, early_exit=True),
            TimedMenuChoice("No, do not trust them.", "doctor_day3_afternoon_captain_do_not_share", 0, early_exit=True),
        ])
    )

    call change_time(14, 00)

    """
    Once again, we all fall silent.

    Trying to make sense of what is happening to us.
    """

    lad """
    Right, as I see it, we don't know much more that this morning.
    
    So what now?

    I feel like we've explore the whole place already.

    And we can't just sit around waiting for answers.
    """

    captain """
    No.

    We must act sensibly.

    It's obvious now that we have to leave.
    """

    psychic """
    Of course, but how?

    The nearest town is miles away.

    I can't walk that far. 

    And even if I could, I'm not prepared for such a journey.
    """

    captain """
    You might be right.

    It would be a long walk, and the weather might turn at any moment.

    We could get caught in another storm.

    It's probably unsafe for you to join us.
    """

    psychic surprised """
    But you're not going to leave me here alone, are you?

    What would become of me?
    """

    captain """
    We could lock you in a room.

    Though, that's far from ideal.

    Perhaps one of us should stay with you.
    """

    psychic """
    Yes!

    Mr Harring can stay with me, right?

    The two of us should be safe until you return with help.
    """

    captain """
    That seems to be the wisest choice.

    What do you think, Mr Harring?
    """

    if doctor_details.saved_variables['doctor_day3_afternoon_captain_share'] > 2:

        lad """
        I don't know, with everything they just told us, I don't believe we are safe, even the two of us staying here.
        """

        psychic """
        But I can't really travel.
        """

        """
        Ted Harring is looking to the floor, ashamed.
        """

        lad """
        I am sorry, I can't stay here any longer I can't.
        """

        psychic """
        What? Are you really gonna abandonned me?

        And you doctor? Or you Captain? Can't one of you stay with me?
        """

        """
        There is an akward silence.

        None of use reply.
        """

        psychic """
        Oh I see, so there is no chance to convince you is there?
        """

        captain """
        I would stay of course, but I am afraid they will need my military skills to make the trip.

        ....
        """

    else:

        lad """
        Of course, I'll stay.

        Only a monster would leave you alone here in this condition.
        """

        psychic normal """
        Thank you Mr Harring! 

        That means the world to me.
        """

        captain """
        Very well.

        Doctor Baldwin and I will go right now then. I don't want to lose time.

        Hopefully, I'll be back with help before nightfall.
        """

    # TODO what are the options

    # Doctor leaves with captain, ted harring stays there
    # Doctor stays??? No way too stressfull

    # Everyone leaves => If you have Told all the information, TED harring DOESN't want to stay with Amelia
    # She is reluctant but end up accepting, realising that everyone is against us, ending at 4 Lives saved BETTER

    # OR Ted Harring stays, the doctor exit with the captain, noone shots at them. TWO saved

    jump work_in_progress



label doctor_day3_afternoon_captain_do_not_share:

    doctor """
    No, it is nothing.

    Captain Sinha merely noticed that my shirt was not sitting properly.

    It is fixed now.
    """

    """
    I quickly tuck my shirt in.

    Captain Sinha gives me a disapproving look. He would have preferred to explain everything.

    But I do not know that I can trust those two just yet.

    In any case, Amelia Baxter seems reassured by my very plausible answer.
    """

    psychic """
    All right, but please, no whispering.

    We are already tense as it is.
    """

    captain """
    Of course. My apologies.
    """

    return


label doctor_day3_afternoon_captain_share:

    doctor """
    I believe you are right, Captain.

    We might as well tell you everything we know.
    """

    """
    So I tell them about the letter we found in Samuel Manning's room, and how it lead to our fight, and his death.

    They look at me puzzled at first, taking it in.

    When the implications are clear to them, they look frightened.
    """

    psychic """
    How terrible.

    But who could be behind this?
    """

    captain """
    That's what we've been trying to figure out, without success.
    """

    """
    Of course, we are not saying what everyone is thinking.

    We are all suspects to the others. 
    
    We may have made a choice to trust them, but deep down we'll stay watchful.
    """

    psychic """
    Right, so right now you don't have more idea than we do.
    """

    captain """
    That is correct. 
    
    We only believe that the obvious suspect is Lady Claythorn.
    """

    psychic """
    Of course, but we don't know enough to be sure are we?

    We need more information to really know what's happening.
    """

    call run_menu( TimedMenu("doctor_day3_afternoon_captain_share", [
            TimedMenuChoice("Tell them about the footman{{observation}}", 'doctor_day3_afternoon_captain_share_footman', condition="doctor_details.threads.is_unlocked('footman_actor')"),
            TimedMenuChoice("Tell them about Rosalind Marsh{{observation}}", 'doctor_day3_afternoon_captain_share_nurse', condition="doctor_details.threads.is_unlocked('remember_nurse')"),
            TimedMenuChoice("Tell them about Thomas Moody{{observation}}", 'doctor_day3_afternoon_captain_share_broken', condition="doctor_details.threads.is_unlocked('broken_unmasked')"),
            TimedMenuChoice("Do not tell them anything more", 'generic_cancel', early_exit=True),
        ])
    )

    return


label doctor_day3_afternoon_captain_share_footman:

    doctor """
    There is something else you should know.

    The footman was not who he claimed to be.

    He told me he was an actor.
    """

    captain """
    An actor?

    Now that you mention it, I remember he made a few mistakes during dinner.

    I assumed he was new to the job.
    """

    psychic """
    It is true, he was a bit inexperienced.
    """

    captain """
    And now that you mention it, so were the others.
    """

    psychic """
    Right, and there were not many of them either.

    A house this big should have twice the staff, at least, compared to what I have seen.

    I simply thought it was due to a labour shortage.
    """

    """
    Ted Harring remains silent through the whole exchange.

    He clearly did not notice anything out of place.

    I must admit I did not either.
    """

    doctor """
    So, in your view, the staff was not what you expected.
    """

    psychic """
    Perhaps not.
    """

    captain """
    Not at all, in my opinion.

    But that doesn't say much.

    I assume a lot of struggling artist end up doing this kind of work.

    The times have changed, it is no longer the case that you were born in service and stay in it your whole life.
    """

    psychic """
    Sadly.
    """

    captain """
    On the other hand, it could also mean they were part of whatever is happening here.

    It would explain why we cannot see any of them here today.
    """

    psychic """
    Maybe, but again, there is no way to know for sure.
    """

    captain """
    Of course.
    """

    """
    I do not believe Andrew was involved, at least not in anything that would harm us.

    But I cannot tell them why.

    Besides, I did not know him all that well.
    """

    $ doctor_details.saved_variables['doctor_day3_afternoon_captain_share'] += 1

    return

# TODO last TWO should be longer have more impact on the story
label doctor_day3_afternoon_captain_share_nurse:

    doctor """
    I am not sure if it is relevant, but I realised earlier that Miss Marsh and I were already acquainted.

    I don't know if it is relevant or if it just a coincidence.
    """

    captain """
    It would be a very improbable coincidence indeed.

    That out of the millions of people in the realm, Lady Claythorn chose two that know each other.

    You could be onto something doctor.

    How well did you know her?
    """

    doctor """
    Not very well of course, I didn't even recognize her at first.

    We met a very long time ago, during the Boxer's rebellion, you see we...
    """

    captain """
    Wait, Doctor. You were in China during the Boxer's Rebellion?
    """

    doctor """
    Yes, as was miss Marsh apparently.
    """

    captain """
    In that case, that can't be a coincidence Doctor.

    You see, I was there myself.
    """

    $ captain_details.description_hidden.unlock('wars')

    doctor """
    You were?

    I don't remember you.
    """

    captain """
    Well, there was a vast among of Indian soldiers fighting for the country.

    It may have been different for you to tell us apart.

    In any case, we didn't associate a lot with people from the metropolis.

    But know that I try to remember, I think I can see talking to a young doctor looking a bit like yourself.
    """

    doctor """
    Well, right.

    It's possible we've met before as well, then.
    """

    lad """
    How queer.

    What are the chances of that?
    """

    captain """
    That it happened by chance that at least three people present here tonight met before?

    I would say close to to zero Mr Harring.

    I would even dare to say that what happened in China could be the reason we are all here this weekend.
    """

    """
    Everybody pounders that for a second.
    """

    lad """
    But I'be never been to China.
    """

    psychic """
    Neither have I.

    And I am confident I never met anyone here before as well.
    """

    captain """
    Right, still this a very weird coincidence, we shouldn't overlook it.
    """

    $ doctor_details.saved_variables['doctor_day3_afternoon_captain_share'] += 1

    return


label doctor_day3_afternoon_captain_share_broken:

    doctor """
    There was something else that struck me as strange, though I do not yet see how it helps us make sense of our situation.

    It concerns Thomas Moody.
    """

    psychic """
    What about him?
    """

    doctor """
    You all noticed the mask he wore to hide his war injuries, I presume.
    """

    psychic """
    Of course.
    """

    lad """
    How could we miss it?
    """

    doctor """
    When I examined him, I had to remove the mask to determine the cause of death.

    I confess I was apprehensive about what I might find.

    But behind it, there were no injuries at all.
    """

    lad """
    No injuries?

    Then why wear the bloody thing?
    """

    doctor """
    Honestly, I cannot offer a logical explanation.

    It was so unsettling that I kept it to myself, as I wished to understand more before speaking of it.

    When I shared what I knew with Captain Sinha, he helped me realise something else.

    That Thomas Moody may have been poisoned.
    """

    psychic surprised """
    Poisoned?!

    And you did not think you ought to have told us?
    """

    captain """
    At the time, we realised something was terribly wrong in the manor.

    But we did not know whom we could trust.

    So we kept it to ourselves.
    """

    psychic -surprised """
    Right.

    I am not sure how that helps us just now.

    It is one more reason to worry, and nothing that truly helps us.

    Still, at least you have told us.
    """

    doctor """
    I am sorry.
    """

    $ doctor_details.saved_variables['doctor_day3_afternoon_captain_share'] += 1

    return
