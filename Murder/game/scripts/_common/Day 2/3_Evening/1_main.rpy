label common_day2_evening_entrance_dialog:

    psychic surprised """
    Good heavens! What happened!?

    Is that Doctor Baldwin? Is he injured?

    Oh no! Is he... dead?
    """

    captain """
    I'm sorry, dear, but he is.
    """

    psychic """
    But... what happened?
    """

    captain """
    A terrible thing. 

    Samuel Manning missed his target and hit Doctor Baldwin instead.
    """

    drunk sad """
    It was an accident, I swear! I have no idea how I could have hit him.
    
    I was aiming at a rabbit. I didn't even see him.
    """
        
    psychic angry """
    You fool! You were probably too drunk, and that's why you hit him.

    You could barely walk this morning. Who gave you a gun?
    """

    captain """
    Please, there's no need to point fingers now. It's done.

    The police will handle it.

    Speaking of which, has anyone from the city arrived yet?
    """

    psychic """
    No, not yet.

    We're still waiting for them.
    """

    captain """
    We should tell them to hurry.

    There are now two bodies to inspect, that will make matters even more complicated.

    Lady Claythorn, where's the telephone?
    """

    host """
    I'll handle it.
    """

    if current_character == lad_details:

        """
        The hostess and her butler clear off down the corridor.

        Then the room goes dead quiet.

        All eyes are on Sam Manning. He doesn't see them.

        He's somewhere else entirely, staring at his own hands as if he's only just realised they're his.

        Best to keep my mouth shut.

        When the hostess comes back, no one has moved an inch.
        """

    elif current_character == psychic_details:

        """
        Our hostess exits the hall, her butler trailing in her wake.

        I look upon Mr Manning.

        The drunkard is altogether elsewhere. His eyes have gone soft as mist, his hands trembling upon his knees.

        No one utters a word until Lady Claythorn has returned.
        """

    elif current_character == nurse_details:

        """
        Lady Claythorn leaves with the butler.

        I keep my hands folded before me. It is what one is taught to do, when there is nothing useful left to be done.

        Mr Manning sits upon the bottom stair, drained of whatever spirit he had this morning.

        He looks rather pitiable, though I doubt anyone here would thank me for saying so.

        I hold my peace.

        The hostess returns presently.
        """

    host """
    I just spoke with the police. They aren't coming today.
    """

    captain """
    What!? Why not?
    """

    host """
    They were on their way but encountered a huge tree blocking the road.
    
    They couldn't get past it.
    
    They said they'll be back tomorrow with assistance.
    """

    psychic -angry """
    But... what are we going to do with him until then?
    """

    captain """
    We'll move him to his bed for now. 
    
    It's the best we can do under the circumstances.

    Anyone willing to help?
    """

    lad """
    I will.
    """

    return

label common_day2_evening_bedroom_doctor_dialogue:

    captain """
    It's the best we can do at the moment.

    We shouldn't linger here.

    I want to keep an eye on Samuel Manning.
    """

    lad """
    Of course.
    """

    captain """
    Also Mr Harring, you might want to change before rejoining us.
    """

    return


label common_day2_evening_samuel_manning_discussion_part_1:

    # Present: psychic, host, drunk, nurse, butler
    # Later Captain
    """
    Lady Claythorn discreetly approaches her butler to converse with him, almost whispering.
    """

    host """
    What should we do about him?

    We certainly can't allow him to wander freely.
    """

    butler """
    It's difficult to say.

    Ordinarily, this would be a matter for the police.

    However, these are extraordinary circumstances, which leave me at a loss.
    """

    psychic """
    Indeed, but that shouldn't stop us from taking measures.

    Our safety must be a priority.

    While he may appear harmless now, it's uncertain if that will remain so.

    Once the effect of the alcohol wanes and he grasps his situation, who knows how he'll respond.

    There's a risk he could attempt to escape.
    """

    nurse """
    Or, he might lash out and harm someone.
    """

    psychic """
    Precisely.

    So we are in agreement, something needs to be done?
    """

    """
    Everyone agrees, albeit silently.
    """

    butler """
    The most sensible course would be confining him to his room.

    The doors are sufficiently robust, and considering his current condition, it's unlikely he'd manage to break free even if he tried.
    """

    host """
    Yes, that seems like a prudent measure.
    """

    """
    At that moment, Sushil Sinha makes his return from upstairs.

    Ted Harring is not with him.
    """

    return


label common_day2_evening_samuel_manning_discussion_part_2:
    
    captain """
    Mr Harring needed to change, he'll join us shortly.
    """

    host """
    Ah, Captain! It's good you're here.

    We've been deliberating over what action to take concerning Samuel Manning.
    """

    captain """
    I see.

    And what is your plan?
    """

    host """
    We've decided to confine him to his chamber.

    At least until the authorities can take over.
    """

    captain """
    That does seem like the wisest approach.
    """

    """
    He shifts his attention towards Samuel Manning.
    """

    captain """
    I hope you understand we're left with little choice right now.
    """

    """ 
    Samuel Manning gives no sign of comprehension.
    """

    drunk """
    Choice? What choice?

    What do you mean?
    """

    captain """
    You have to retire to your room for now.

    The door will be locked from the outside to ensure you don't get out.

    Is that clear?
    """

    drunk """
    Yes, of course...

    I understand.
    """

    captain """
    Good, come with me, please.
    """

    """
    The butler retrieves a set of keys from his pocket.

    After sifting through them, he presents one to Mr Sinha.
    """

    butler """
    Use this key to lock his room.
    """

    captain """
    Excellent, thank you.

    Now, Mr Manning, let's go shall we?
    """

    """
    Samuel Manning offers a silent nod, rises, and follows Captain Sinha up the staircase.

    His gaze betrays a mix of resignation and confusion.
    """
    
    return


label common_day2_evening_samuel_manning_discussion_part_3:

    host """
    What a sad business.

    But, sadly, there is nothing else to be done at the moment.

    I suggest you all return to your rooms for now.

    You'll hear the gong when dinner is ready.
    """
    
    return

label common_day2_evening_dinner_host:

    host """
    Now that everyone is here, I want to express my deepest regret for what happened today.

    This isn't how I imagined our weekend.

    I don't believe any of us are in the mood for more entertainment.

    So, tomorrow morning, you'll receive your rewards.
    
    Afterward, we'll wait for the police to arrive.

    You're free to head home as soon as the officers give the all-clear.

    For now, enjoy your dinner.

    Drinks will be available in the billiard room afterwards, as they were yesterday.
    """

    return


label common_day2_evening_dinner_lad_psychic_talk:

    lad """
    Miss Baxter, I don't see Samuel Manning. 

    Do you know where he might be?
    """

    psychic """
    He's locked in his room.

    After you left, there was a debate about how to handle him.
    
    Ultimately, we decided it best to confine him to his room.

    He didn't resist.

    That's where he is now. 

    It was agreed that his dinner would be served there.
    """

    return