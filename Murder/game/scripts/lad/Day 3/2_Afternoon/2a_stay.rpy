label lad_day3_stay:

    call change_time(13,00, "Afternoon", "Sunday")

    $ change_room("tea_room")

    """
    I don't feel comfortable leaving Amelia Baxter alone in here.

    And in any case, I don't like the idea to be alone with this guy in the forest.

    For whole all know, he very well might be the killer.

    Miss Baxter doesn't seem to trust him anyway.

    So I figure it's best we stay there, and be on our guards.

    If we are lucky, the captain will come back with reinforcements and everything will be fine.
    """

    pause 2.0

    """
    After a while sitting anxiously, Amelia stands up.
    """

    psychic """
    Well, no point in waiting doing nothing.

    We haven't eaten anything since yesterday.

    I could check the kitchen to see if there is anything I could prepare.
    """

    lad """
    Okay, I am coming with you.
    """

    $ change_room('kitchen', dissolve)

    """
    We looked around to find something.
    """

    psychic """
    There is not much.

    But I think I can manage a light luncheon if you are not picky.
    """

    """
    I take a seat while she prepares the food.

    I offer to help but she declines.

    That's probably for the best.

    It's not like I could do much anyway.
    """

    $ lad_details.unlock_knowledge('cook') 

    $ change_room('dining_room', dissolve)

    """
    When everything is ready I offer to carry the plates to the dining room.

    I put them on the table at our usuals places.

    Then I excuse myself.
    """

    psychic """
    Where are you going mister Harring?

    It's better that we stick together at all time.
    """

    lad """
    I understand, but there is one thing I need to do alone.

    You see, we haven't left each other company the whole day and...
    """

    psychic """
    Say no more, I understand.

    I guess this was inevitable. 

    I would like to go too actually.

    Let's meet here in a few minutes.
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
    That is where we split up.

    We can meet again in the dining room in a few minutes.
    """


    if lad_details.intuitions.is_unlocked('psychic_poisons'):

        """
        I see her enter her room but as I was supposed to leave for mine, some weird feeling overwhelms me. 

        I don't know what it is but it tells me to not go to my room.

        That I should go back to the dining room, now.

        What should I do?
        """

        $ time_left = 1
        call run_menu( TimedMenu("lad_day3_stay", [
            TimedMenuChoice('I am being paranoid. Besides I can\'t hold it any longer', 'lad_day3_afternoon_toilet', early_exit = True ),
            TimedMenuChoice('Go back downstairs{{intuition}}', 'lad_day3_afternoon_no_toilet', early_exit = True)
            ])
        )
    else:

        call lad_day3_afternoon_toilet

    return

label lad_day3_afternoon_toilet:

    """
    I see her enter her room then I head to mine.
    """

    $ change_room('lad_room')

    """
    As I walked in the hallway, I was looking frenetically around me.

    It felt like someone could jump from a corner at any moment.

    I better not waste any time.
    """       

    pause 2.0

    """
    Once I am done, I try to hurry back as fast as I could, almost running down the stairs. 
    """

    $ change_room('dining_room')
    
    """
    But when I came back, Miss Baxter is already seated at the table.

    She was even faster than I was.

    She must be scared too.

    I take my place in front of her and we start eating in silence. 
    
    There is not much we want to talk about.
    """

    pause 2.0

    """
    After I finished my plate, I offer to help her do the dishes.

    Not that it really matters now.

    It's just something more to do while waiting.
    """

    $ play_music('danger', fadeout_val=2)

    """
    But as soon I stand up, I realize I can't stay on my feet.

    My head is dizzy. 

    I feel that I am about to faint.

    I look to Amelia Baxter.

    She looks back at me with a blank stare. 
    
    There is no sign of surprise in her look.
    """

    lad surprised """
    What... did ... you do ... to my food?
    """

    # psychic """
    # Your food? I did nothing with it.

    # But I taught you might have.

    # So I switched our plates before handing them to you.

    # You see, I never really trusted you Mister Harring.

    # It looks like I was right to do so.
    # """

    """
    I try to keep on talking. But no sound comes out of my mouth.
    """

    play sound body_fall

    $ stop_music(2)

    """
    I fall on the ground.
    """

    $ lad_details.saved_variables["day3_ending"] = "poisoned"

    

    return

label lad_day3_afternoon_no_toilet:
    
    """
    Instead of going to my room, I go down the stairs and back into the dining room.
    """

    $ change_room('dining_room')

    """
    Then, I try to make sense of what is happening.

    I am putting my trust in a eccentric older lady, why?
    
    Because I don't think she could hurt me?

    Not directly at least.

    But she could do it in a more subtle way.

    I look at our plates, they look normal to me.

    And I was with her the whole time, so there is no way she could have tampered with them.

    At least I think.

    I am not so sure now.

    It's probably for nothing, but it's better to be safe than sorry.

    So I switch my plate with Miss Baxter's.
    
    Then I sat down at my place, waiting for her to return.
    """

    pause 2.0

    """
    She comes back, very soon herself.

    She couldn't have stayed very long in her room.

    But that make sense, she must be terrified.

    There is indeed a worried look on her face.
    """

    psychic """
    Mister Harring... You were fast.
    """

    lad """
    So were you.
    """

    psychic """
    Right.
    """

    """
    She gave me a concerned look, then sits down at her place.
    
    We start eating in silence. 
    """

    pause 2.0

    """
    After we are finished, I stand up and offer to make the dishes.
    """

    psychic """
    No don't worry, I can do it myself.
    """

    """
    She stands up, but seems a bit disoriented.
    """

    psychic """
    I feel woozy.

    What's happening to me?
    """

    play sound body_fall

    $ play_music('danger')

    """
    Then she suddenly fells on the ground.

    I rush next to her.
    """

    psychic surprised """
    Mister Harring.

    So it was you.
    
    But why?
    """

    lad surprised """
    What?

    No, I don't understand what's happening...

    I have nothing to do with this I,...
    """

    psychic """
    Shhh, there is no need to pretend now.

    Is it because you found out the truth about me?
    
    That I was a fraud...

    That I could never talk with the dead... 

    Well it doesn't matter anymore.

    I guess I was wrong to bet on you.

    I ...
    """

    """
    But she can't finish her sentence.
    """

    $ psychic_details.unlock_knowledge('lie') 

    $ play_music('scary')

    pause 2.0

    """
    Oh my god.

    What's happening?

    Who did this to her?
    """

    """
    TODO footsteps?
    Paranoid?
    """
    
    lad """
    Hey!!! 

    Who is here !?

    Where are you !?

    Show Yourself!!!
    """

    pause 1.0

    """
    No answers.

    I can't stay here.

    I need to go out fast.
    """

    $ change_room("great_hall")

    """
    I run to the entrance hall and rush to the door.
    """

    play sound door_locked

    """
    It's locked.

    What the hell.

    Who did this?

    I need to get out.

    I think I hear footsteps in the distance.
    """

    lad surprised """
    Who is it?
    """

    """
    I don't know what to do.
    
    In a state of panic I run to my room.
    """

    $ change_room("lad_room")

    """
    I close the door right after I enter.
    
    Oh my god.
    
    How will I get out now?
    
    The only way out is ...
    """

    pause 1.0

    """
    I look at my window.

    It is not too high.

    Maybe I can safely go down there.

    I open the window.

    At least it is not locked.

    Down there I can see a picked fence.
    
    But if I can control my fall, I should be able to avoid it.

    All I have to do ...
    """

    play sound door_rattling

    """
    Someone is coming.

    I don't have time.

    I grab the window sill.

    If I can fell slowly I can ...
    """

    $ lad_details.saved_variables["day3_ending"] = "fell"

    stop sound

    $ stop_music()

    return