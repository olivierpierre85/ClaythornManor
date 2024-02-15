label lad_day3_stay:

    call change_time(13,00, "Afternoon", "Sunday")

    $ change_room("tea_room")

    """
    I don't feel comfortable leaving Amelia Baxter alone here.

    And in any case, I don't like the idea of being alone with this guy in the forest.

    For all we know, he might very well be the killer.

    Miss Baxter doesn't seem to trusts him either.

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

    $ change_room('basement stairs', dissolve)

    """
    We were heading to the lower floor, when we head a shout.
    """

    nurse """
    Hello ! Hello !

    Is there someone here?
    """

    psychic """
    Oh my god, Miss Mars, you're here!
    """

    nurse """
    Of course I am. I am afraid I over slept.

    I don't feel quite like myself today.

    It's possible I might be sick.

    But where is everybody else?
    """

    psychic """
    Oh my dear we don't know.
    """

    """
    We updated her on what happened since this morning.

    When we had finish told her the story, she remained relatively calm, considering the situation.
    """

    nurse """
    what a tragic story.

    But I believe there's nothing for us to do now but wait.
    """

    psychic """
    We were heading to the kitchen, to see of we can prepare some sort of meal.
    """

    nurse """
    Right, it's a good idea. We might as well keep busy until someone comes back for us.
    """

    $ change_room('kitchen', dissolve)

    """
    We look around for something to eat.
    """

    psychic """
    There isn't much.

    But I think we can manage a light luncheon if you're not picky.
    """

    nurse """
    I'll help you.
    """

    """
    I take a seat while they prepare the food.

    I offer to help, but they decline.

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

    What about you Miss Marsh?
    """

    nurse """
    Oh, I am fine thank you.

    You both go, I'll finish preparing the table.
    """
    

    psychic """
    Very well.

    Let's meet back here in a few minutes then.
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
    
    # Version with only psychic and lad
    # """
    # But when I return, Miss Baxter is already seated at the table.

    # She was even quicker than I was.

    # She must be scared too.

    # I take my seat across from her, and we eat in silence. 

    # There's not much we want to discuss.
    # """

    # pause 2.0

    # """
    # After finishing my meal, I offer to help her with the dishes.

    # Not that it really matters now.

    # It's just something to do while we wait.
    # """

    # $ play_music('danger', fadeout_val=2)

    # """
    # But as soon as I stand up, I realize I can't stay on my feet.

    # My head spins, and I feel faint.

    # I turn to Amelia Baxter.

    # She looks back at me emotionlessly.

    # There's no surprise in her eyes.
    # """

    # lad surprised """
    # What... did you... do to my food?
    # """

    # psychic """
    # Your food? I didn't tamper with it.

    # But I thought you might have.

    # So, I switched our plates before serving.

    # I never really trusted you, Mister Harring.

    # Seems I was right not to.
    # """

    """
    Rosalind Marsh is already at her place.

    I sat down at my seat.

    When Miss Baxter comes back, we start eating in silence.

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
    """

    lad surprised """
    What's happening?
    """

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

    # old version
    # """
    # I try to make sense of the situation.

    # Why am I putting my trust in an eccentric older lady?

    # Because I believe she couldn't harm me?

    # Maybe not directly.

    # But she could be more subtle about it.

    # I inspect our plates; they seem normal.

    # I was with her the entire time, so there's no way she could've tampered with them.

    # At least I think.

    # Perhaps it's nothing, but it's better to be safe than sorry.

    # I discreetly switch my plate with Miss Baxter's.
    
    # I then take my seat, waiting for her to come back.
    # """

    # pause 2.0

    # """
    # She returns rather quickly.

    # She couldn't have spent much time in her room.

    # That's understandable; she must be terrified.

    # Her face certainly shows concern.
    # """

    # psychic """
    # Mister Harring... You were quick.
    # """

    # lad """
    # As were you.
    # """

    # psychic """
    # Indeed.
    # """

    # """
    # She casts a concerned glance my way, then sits.

    # We dine in silence.
    # """
    
    """
    When I return, I see Miss Marsh with my plate in her hands.
    """

    lad """
    Wait, what are you doing?
    """

    """
    She jumps up, visibly startled.
    """

    nurse """
    Oh, nothing special. I just realized the plate set out for me is too full.

    I won't be able to eat that much.

    But you are a strong gentleman; I am sure you won't mind switching with me, right?
    """

    lad """
    I actually do mind.

    Not the quantity, but I already seasoned my plate exactly how I want it.

    I would prefer to keep it that way.
    """

    """
    Not a likely lie, but she doesn't have a response to it.

    She hesitates for a second.
    """

    nurse """
    All right then. I'll switch with Miss Baxter instead.

    I am certain she won't mind.
    """

    """
    Something bothers me about this.

    But I can't quite figure out what.

    She's so quick to exchange the plates that I don't have time for an objection anyway.

    When Miss Baxter comes back, we start eating in silence.
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

    $ play_music("danger")

    """
    Suddenly, she collapses.

    I rush to her side.
    """

    psychic """
    What is happening?

    That doesn't make any sense.

    I thought I...
    """

    """
    She realizes I am holding her hands.
    """

    psychic """
    Oh, Mister Harring, I shouldn't have lied to you.
    """

    lad """
    What do you mean? Are you all right?
    """

    psychic """
    No, I am not, but it's okay.

    I should have been more honest with you.

    You see, I never was a psychic; that was just a lie.

    I...

    I...
    """

    """
    She can't finish her sentence.
    """

    $ psychic_details.unlock_knowledge('lie') 

    $ play_music('scary')

    pause 2.0

    #TODO confrontation between Nurse and lad
    lad """
    Oh my God!!

    What have you done.
    """

    nurse scared """
    Nothing! I swear, I was just

    I was just...
    """

    lad scared """
    Don't try to lie to me.

    I saw you switching plates. What kind of poison have you put in it?
    """

    nurse scared """
    Nothing, you don't understand.

    That means 'my' plate was poisoned.
    """

    """
    I am startled for a second at that response.

    Wait, what about my plate then...

    Have I eaten the same thing as her?

    Now that I think about it, I realize I am suddenly very tired.
    """

    lad scared """
    God, you also poisoned me, didn't you.
    """

    nurse scared """
    No ! I swear.
    """    

    """ 
    My vision is getting blurry.

    I am in danger here.
    """

    nurse scared """
    Mister Harring, are you well?

    You seem weird?"
    """

    """
    She slowly approaches me.
    """

    lad scared """
    Stay where you are!

    Don't move.
    """

    #TODO if gun => point gun at her
    if lad_details.objects.is_unlocked('burned_letter'):
        """
        I point the gun at her.

        It's empty but she doesn't know it.
        """

        lad scared """
        Move back or I'll shoot!
        """

        """
        It seems to work. She jumps back.
        """

        nurse scared """
        Don't shoot ! Please, I won't move.

        I swear.
        """
    else:
        """
        She backs down a little.
        """

        nurse scared """
        Of course.
        """

    """
    I am not safe here.

    I should move.

    Collecting all my strengths I rush to the main staircase.
    """

    # TODO add blurry filter

    # TODO Other ending? Nurse pulls gun out and shot me if I don't have the gun

    $ change_room("great_hall")

    """
    I sprint to the entrance hall and bolt for the door.
    """

    play sound door_locked

    """
    It's locked.

    What the hell?

    My strengths are leaving me slowly.

    I can barely see straight now.

    I have to do something.

    So I rush up the stairs then head to my room.
    """

    $ change_room("lad_room")

    """
    Once inside, I slam the door shut.
    
    My thoughts race.

    I can't stay in here. 

    She probably has a key.

    And I will pass out any seconds now.

    I need to escape.
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
    She's there.

    Time is running out.

    Gripping the window sill, I prepare to jump.

    If I can control my fall, maybe I can...
    """

    $ lad_details.saved_variables["day3_ending"] = "fell"

    stop sound

    $ stop_music()

    return

    # OLD ENDING
    # psychic surprised """
    # Mister Harring...

    # Was it you?
    
    # But why?
    # """

    # lad surprised """
    # What?

    # I don't know what's going on...

    # I had nothing to do with this, I promise...
    # """

    # psychic """
    # Shh... There's no need to feign innocence now.

    # Is it because you discovered the truth?

    # That I'm a fraud...

    # That I could never commune with the dead, that... 

    # Well it doesn't matter anymore.

    # I guess I was wrong to bet on you.

    # I ...
    # """

    # """
    # She can't finish her sentence.
    # """

    # $ psychic_details.unlock_knowledge('lie') 

    # $ play_music('scary')

    # pause 2.0

    # """
    # Oh my god.

    # What just happened?

    # Who did this?
    # """

    # lad """
    # Hey! 

    # Who's there?

    # Show yourself!
    # """

    # pause 1.0

    # """
    # Only silence answers back.

    # I can't stay here.

    # I have to leave. Now.
    # """

    # $ change_room("great_hall")

    # """
    # I sprint to the entrance hall and bolt for the door.
    # """

    # play sound door_locked

    # """
    # It's locked.

    # What the hell?


    # I need to get out.

    # I think I hear footsteps in the distance.
    # """

    # lad surprised """
    # Who's there?
    # """

    # """
    # Panic grips me.

    # I rush to my room.
    # """

    # $ change_room("lad_room")

    # """
    # Once inside, I slam the door shut.
    
    # My thoughts race.

    # The only escape is...
    # """

    # pause 1.0

    # """
    # My gaze lands on the window.

    # The drop isn't too far.

    # I might be able to climb down safely.

    # I throw open the window.

    # Thankfully, it isn't locked.

    # Below, a picket fence lurks.

    # But if I can guide my descent, I might avoid it.

    # I just need to...
    # """

    # play sound door_rattling

    # """
    # Someone's there.

    # Time is running out.

    # Gripping the window sill, I prepare to jump.

    # If I can control my fall, maybe I can...
    # """

    # $ lad_details.saved_variables["day3_ending"] = "fell"

    # stop sound

    # $ stop_music()

    # return
