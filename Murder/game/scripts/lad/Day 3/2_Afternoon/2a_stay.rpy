label lad_day3_stay:

    call change_time(13,00, "Afternoon", "Sunday")

    $ change_room("tea_room")

    """
    I don't feel comfortable leaving Amelia Baxter alone here.

    And in any case, I don't like the idea of being alone with this guy in the forest.

    For all we know, he might very well be the killer.

    Miss Baxter doesn't seem to trust him either.

    So I figure it's best for us to stay here and be on our guard.

    If we're lucky, the captain will return with reinforcements, and everything will be fine.
    """

    pause 2.0

    """
    After waiting anxiously for a while, Amelia stands up.
    """

    psychic """
    Well, there's no point in waiting around doing nothing.

    We haven't eaten since yesterday.

    I could check the kitchen to see if there's anything I can prepare.
    """

    lad """
    Okay, I'll come with you.
    """

    $ change_room('kitchen', dissolve)

    """
    We look around for something to eat.
    """

    psychic """
    There isn't much.

    But I think I can manage a light luncheon if you're not picky.
    """

    """
    I take a seat while she prepares the food.

    I offer to help, but she declines.

    That's probably for the best.

    I couldn't do much to help anyway.
    """

    $ lad_details.unlock_knowledge('cook') 

    $ change_room('dining_room', dissolve)

    """
    When everything is ready, I offer to carry the plates to the dining room.

    I set them at our usual places.

    Then I excuse myself.
    """

    psychic """
    Where are you going, Mister Harring?

    It's better if we stick together at all times.
    """

    lad """
    I understand, but there's something I need to do alone.

    We haven't had a moment apart the entire day and...
    """

    psychic """
    Say no more, I understand.

    I've been feeling the same. 

    Let's meet back here in a few minutes.
    """

    lad """
    Of course.
    """

    pause 1.0

    $ change_room("bedrooms_hallway")

    """
    I accompany Miss Baxter to her room.
    """

    psychic """
    This is where we part.

    We'll meet again in the dining room in a few minutes.
    """

    if lad_details.intuitions.is_unlocked('psychic_poisons'):

        """
        I see her enter her room, but as I'm about to leave for mine, a strange feeling overwhelms me.

        Something tells me not to go to my room.

        That I should return to the dining room immediately.

        What should I do?
        """

        $ time_left = 1
        call run_menu( TimedMenu("lad_day3_stay", [
            TimedMenuChoice('I\'m being paranoid. Besides, I really need to go', 'lad_day3_afternoon_toilet', early_exit = True ),
            TimedMenuChoice('Go back downstairs{{intuition}}', 'lad_day3_afternoon_no_toilet', early_exit = True)
            ])
        )
    else:

        call lad_day3_afternoon_toilet

    return

label lad_day3_afternoon_toilet:

    """
    After seeing her enter her room, I head to mine.
    """

    $ change_room('lad_room')

    """
    As I walk down the hallway, I constantly look around.

    It feels like someone might jump out at me any moment.

    I shouldn't waste any time.
    """       

    pause 2.0

    """
    Once I'm done, I rush back as quickly as possible, nearly running down the stairs. 
    """

    $ change_room('dining_room')
    
    """
    But when I return, Miss Baxter is already seated at the table.

    She was even quicker than I was.

    She must be scared too.

    I take my seat across from her, and we eat in silence. 

    There's not much we want to discuss.
    """

    pause 2.0

    """
    After finishing my meal, I offer to help her with the dishes.

    Not that it really matters now.

    It's just something to do while we wait.
    """

    $ play_music('danger', fadeout_val=2)

    """
    But as soon as I stand up, I realize I can't stay on my feet.

    My head spins, and I feel faint.

    I turn to Amelia Baxter.

    She looks back at me emotionlessly.

    There's no surprise in her eyes.
    """

    lad surprised """
    What... did you... do to my food?
    """

    # psychic """
    # Your food? I didn't tamper with it.

    # But I thought you might have.

    # So, I switched our plates before serving.

    # I never really trusted you, Mister Harring.

    # Seems I was right not to.
    # """

    """
    I try to speak further, but no words come out.
    """

    play sound body_fall

    $ stop_music(2)

    """
    I collapse to the ground.
    """

    $ lad_details.saved_variables["day3_ending"] = "poisoned"

    return


label lad_day3_afternoon_no_toilet:

    """
    Instead of going to my room, I go down the stairs and return to the dining room.
    """

    $ change_room('dining_room')

    """
    I try to make sense of the situation.

    Why am I putting my trust in an eccentric older lady?

    Because I believe she couldn't harm me?

    Maybe not directly.

    But she could be more subtle about it.

    I inspect our plates; they seem normal.

    I was with her the entire time, so there's no way she could've tampered with them.

    At least I think.

    Perhaps it's nothing, but it's better to be safe than sorry.

    I discreetly switch my plate with Miss Baxter's.
    
    I then take my seat, waiting for her to come back.
    """

    pause 2.0

    """
    She returns rather quickly.

    She couldn't have spent much time in her room.

    That's understandable; she must be terrified.

    Her face certainly shows concern.
    """

    psychic """
    Mister Harring... You were quick.
    """

    lad """
    As were you.
    """

    psychic """
    Indeed.
    """

    """
    She casts a concerned glance my way, then sits.

    We dine in silence.
    """

    pause 2.0

    """
    After finishing, I rise and offer to wash the dishes.
    """

    psychic """
    No, don't worry. I'll handle it.
    """

    """
    She stands but appears slightly off-balance.
    """

    psychic """
    I feel faint...

    What's happening?
    """

    play sound body_fall

    $ play_music('danger')

    """
    Suddenly, she collapses.

    I rush to her side.
    """

    psychic surprised """
    Mister Harring...

    Was it you?
    
    But why?
    """

    lad surprised """
    What?

    I don't know what's going on...

    I had nothing to do with this, I promise...
    """

    psychic """
    Shh... There's no need to feign innocence now.

    Is it because you discovered the truth?

    That I'm a fraud...

    That I could never commune with the dead, that... 

    Well it doesn't matter anymore.

    I guess I was wrong to bet on you.

    I ...
    """

    """
    She can't finish her sentence.
    """

    $ psychic_details.unlock_knowledge('lie') 

    $ play_music('scary')

    pause 2.0

    """
    Oh my god.

    What just happened?

    Who did this?
    """

    lad """
    Hey! 

    Who's there?

    Show yourself!
    """

    pause 1.0

    """
    Only silence answers back.

    I can't stay here.

    I have to leave. Now.
    """

    $ change_room("great_hall")

    """
    I sprint to the entrance hall and bolt for the door.
    """

    play sound door_locked

    """
    It's locked.

    What the hell?


    I need to get out.

    I think I hear footsteps in the distance.
    """

    lad surprised """
    Who's there?
    """

    """
    Panic grips me.

    I rush to my room.
    """

    $ change_room("lad_room")

    """
    Once inside, I slam the door shut.
    
    My thoughts race.

    The only escape is...
    """

    pause 1.0

    """
    My gaze lands on the window.

    The drop isn't too far.

    I might be able to climb down safely.

    I throw open the window.

    Thankfully, it isn't locked.

    Below, a picket fence lurks.

    But if I can guide my descent, I might avoid it.

    I just need to...
    """

    play sound door_rattling

    """
    Someone's there.

    Time is running out.

    Gripping the window sill, I prepare to jump.

    If I can control my fall, maybe I can...
    """

    $ lad_details.saved_variables["day3_ending"] = "fell"

    stop sound

    $ stop_music()

    return
