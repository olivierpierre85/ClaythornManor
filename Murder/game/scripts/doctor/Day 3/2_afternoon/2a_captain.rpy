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

    lad """
    So what now?

    We can't just sit around waiting for answers.
    """

    captain """
    No.

    We must act sensibly.
    """

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
    So I tell them about the letter we found in Samuel Manning's room.
    """

    psychic """
    How peculiar.

    Who could have done such a thing, and why?

    It is very strange, but it does not explain much.

    Is there anything else we should know, Doctor?
    """

    call run_menu( TimedMenu("doctor_day3_afternoon_captain_share", [
            TimedMenuChoice("Tell them about the footman", 'doctor_day3_afternoon_captain_share_footman', condition="doctor_details.threads.is_unlocked('footman_actor')"),
            TimedMenuChoice("Tell them about Rosalind Marsh", 'doctor_day3_afternoon_captain_share_nurse', condition="doctor_details.threads.is_unlocked('remember_nurse')"),
            TimedMenuChoice("Tell them about Thomas Moody", 'doctor_day3_afternoon_captain_share_broken', condition="doctor_details.threads.is_unlocked('broken_unmasked')"),
            TimedMenuChoice("Do not tell them anything more", 'generic_cancel', early_exit=True),
        ])
    )
    # TODO: If you have said all options: Psychic don't let you leave?

    call change_time(13, 00)

    doctor """
    There you have it.

    It is everything I know.
    """

    return


label doctor_day3_afternoon_captain_share_footman:

    doctor """
    There is something else you should know.

    The footman was not who he claimed to be.

    He was an actor.
    """

    captain """
    An actor?

    That would explain a great deal.

    He made a few mistakes during dinner.

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

    We could assume they were part of it, then.

    I do not know what 'it' is meant to be.

    But it would explain why we cannot see any of them here today.
    """

    """
    I do not believe Andrew was involved, at least not in anything that would harm us.

    But I cannot tell them why.

    Besides, I did not know him all that well.
    """

    return

# TODO last TWO should be longer have more impact on the story
label doctor_day3_afternoon_captain_share_nurse:

    doctor """
    I am not sure if it is relevant, but I realized earlier that Miss Marsh and I were already acquainted.

    I don't know if it is relevant or if it just a coincidence.
    """

    captain """
    It would be a very improbable coincidence indeed.

    That out of the millions of people in the realm, Lady Claythorn chose two that know each other.

    You could be onto something doctor.

    How well did you know her.
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
    THat it happened by chance that at least three people present here tonight met before?

    I would say close to to zero Mr Harring.

    I would even dare to say that what happened in China could be the reason we are all here this weekend.
    """

    """
    Everybody pounders that for a second.
    """

    lad """
    But I never been to China.
    """

    psychic """
    And neither have I.

    And I am confident I never met anyone here before as well.
    """

    # TODO more talk? or 

    return


label doctor_day3_afternoon_captain_share_broken:

    doctor """
    There was something else that was strange, but I don't how it could help us understand our situation.  

    It's about Thomas Moody.      
    """

    psychic """
    What about him?
    """

    doctor """
    Well, you've all noticed the mask he used to hide his war injuries I presume.
    """

    psychic """
    Of course.
    """

    lad """
    How could we have missed it?
    """

    doctor """
    Right, well, I had to remove his mask to determine the cause of death.

    Turns out there wasn't any.
    """

    lad """
    What do you mean? Why wear a mask then?
    """

    doctor """
    That's the question Mr Harring, I have no idea.

    But what I saw behind his mask, is that he was probably poisoned.
    """

    lad """
    Poisoned?

    But you didn't say anything?

    Why?
    """

    # FAir question, why?
    # Then, nobody can trust him after saying that I assume => What impact?



    return