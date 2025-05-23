label lad_day3_stay:

    call change_time(13, 00, "Afternoon", "Sunday")

    $ change_room("tea_room")

    """
    I don't feel comfortable leaving Amelia Baxter alone here.

    And in any case, I don't like the idea of being alone with this guy in the forest.

    For all we know, he might very well be the killer.

    Miss Baxter doesn't seem to trust him either.

    So I figure it's best for us to stay here and be on our guard.

    If we're lucky, the captain will return with reinforcements, and everything will be fine.
    """

    pause 1.0

    lad """
    I think I should stay here.
    """

    psychic """
    Yes! Thank you, Mister Harring.
    """

    captain """
    It's decided then, I'll go alone.

    And there is no time to lose, so I better leave immediately.
    """

    psychic """
    Good thinking. And don't worry about us, we'll be fine here.

    Be careful.
    """

    lad """
    Good luck, Captain.
    """

    captain """
    Thank you both. I will be back soon.
    """

    """
    We watched him leave the room, and I can sense relief in Miss Baxter's eyes.

    As soon as Captain Sinha is out of sight, she stands up.
    """

    call common_day3_afternoon_lad_psychic_stay

    $ change_room("bedrooms_hallway", dissolve)

    """
    I accompany Miss Baxter to her room.
    """

    psychic """
    This is where we part.

    We'll meet again in the dining room in a few minutes.
    """

    lad """
    Alright, see you soon.
    """

    pause 1.0

    if lad_details.endings.is_unlocked('poisoned'):

        """
        I see her enter her room, but as I'm about to leave for mine, a strange feeling overwhelms me.

        Something tells me not to go to my room.

        That I should return to the dining room immediately.

        What should I do?
        """

        $ time_left = 1
        call run_menu( TimedMenu("lad_day3_stay", [
            TimedMenuChoice('I\'m being paranoid. Besides, I really need to go', 'lad_day3_afternoon_toilet', early_exit = True ),
            TimedMenuChoice('Hold it in and go back downstairs{{intuition}}', 'lad_day3_afternoon_no_toilet', early_exit = True)
            ])
        )
    else:

        call lad_day3_afternoon_toilet

    return

label lad_day3_afternoon_toilet:

    """
    After seeing her enter her room, I head to mine.

    As I walk down the hallway, I constantly look around.

    It feels like someone might jump out at me any moment.
    """

    $ change_room('bedroom_lad')

    """
    Once I reached my room, I try not to waste any time. 
    
    First things first, I spend a penny.
    """       

    pause 2.0

    """
    Once I'm done, I rush back as quickly as possible, nearly running down the stairs. 
    """

    $ change_room('dining_room')

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

    call common_day3_afternoon_lad_falls

    $ stop_music(2)

    """
    I collapse to the ground.
    """

    $ lad_details.saved_variables["day3_ending"] = "poisoned"

    return


label lad_day3_afternoon_no_toilet:

    $ lad_details.important_choices.unlock('protect_food')

    """
    Instead of going to my room, I go down the stairs and return to the dining room.
    """

    $ change_room('dining_room')

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
    Oh, nothing special. I just realised the plate set out for me is too full.

    I won't be able to eat that much.

    But you are a strong gentleman.
    
    I am sure you won't mind switching with me, right?
    """

    lad """
    I actually do mind.

    Not the quantity, but I have already seasoned my plate exactly how I like it.

    I would prefer to keep it that way.
    """

    """
    It's not a likely lie, but she doesn't have a response to it.

    She hesitates for a moment.
    """

    nurse """
    All right then. I'll swap with Miss Baxter instead.

    I'm certain she won't mind.
    """

    """
    Something bothers me about this.

    But I can't quite figure out what it is.

    She's so quick to exchange the plates that I don't have time to raise an objection anyway.

    When Miss Baxter comes back, we start eating in silence.
    """

    pause 2.0

    call wait_screen_transition()

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
    """

    play sound body_fall

    $ play_music("danger")

    """
    Suddenly, she collapses.
    """

    psychic """
    What is happening?

    This doesn't make any sense.

    I thought I...
    """

    """
    I rush to her side.
    """

    lad """
    Are you alright?

    Do you need a glass of water?
    """

    psychic """
    No no, I don't need anything thank you.
    """

    """
    Her expression subtly changes, from fright to resignation.
    """

    psychic """
    I feel... I feel I made a huge mistake.
    """

    lad """
    What do you mean?
    """

    # TOO obvious
    # psychic """
    # It doesn't matter now.

    # It's too late it appears.
    
    # Oh, Ted, I shouldn't have lied to you.
    # """

    psychic """
    It doesn't matter now.

    It's too late.
    
    I am sorry, I shouldn't have lied.
    """

    lad """
    What are you talking about? Lie about what?
    """

    psychic """
    About everything.

    That... I was never a psychic...

    I am... a fraud... 
    
    A con artist...

    I...
    """

    lad """
    Don't say anything, you need to keep your strength.
    """

    psychic """
    No it's too late for that.

    I need to... now...

    I...

    I...
    """

    """
    She can't finish her sentence.
    """

    $ stop_music(1)

    $ psychic_details.description_hidden.unlock('lie') 

    $ play_music('scary')

    pause 2.0

    """
    As I watch Amelia Baxter's life slowing leaving her body, 
    
    I turn towards Rosalind Marsh.
    """

    lad """
    Oh my God!

    What have you done?
    """

    nurse scared """
    Nothing! I swear, I was just...

    trying to...
    """

    lad scared """
    Don't try to lie to me.

    I saw you swapping plates. What kind of poison did you put in there?
    """

    nurse scared """
    Nothing, you don't understand.

    That means 'my' plate was poisoned.
    """

    """
    I am startled for a moment by that response.

    Then I think, wait, what about my plate then...

    Have I eaten the same thing as her?

    Now that I think about it, I realize I am suddenly very tired.
    """

    lad scared """
    God, you also poisoned me, didn't you?
    """

    nurse scared """
    No! I swear.
    """    

    #TODO Add blurry filter
    """ 
    My vision is getting blurry.

    I am in danger here.
    """

    nurse scared """
    Mister Harring, are you all right?

    You look unwell.
    """

    """
    She slowly approaches me.
    """

    lad scared """
    Stay where you are!

    Don't come any closer.
    """

    # TODO: if gun => point the gun at her
    if lad_details.objects.is_unlocked('gun'):
        """
        I point the gun at her.

        It's empty, but she doesn't know that.
        """

        lad scared """
        Move back, or I'll shoot!
        """

        """
        It seems to work. She jumps back.
        """

        nurse scared """
        Don't shoot! Please, I won't move.

        I swear.
        """
    else:
        """
        She backs down a little.
        """

        nurse scared """
        Alright, alright.
        """

    """
    I'm not safe here.

    I need to move.

    Gathering all my strength, I rush to the main staircase.
    """

    # TODO: Consider other ending? If the nurse has a gun and I don't, she shoots me

    $ change_room("great_hall")

    """
    I sprint to the entrance hall and make a break for the door.
    """

    play sound door_locked

    """
    It's locked.

    How can this be?

    My strength is fading slowly.

    I must do something.

    So, with the last of my energy, I go up the stairs and head to my room.
    """

    $ change_room("bedroom_lad")

    """
    Once inside, I slam the door shut.
    """
    
    play sound door_shut

    """
    Panic floods my mind.

    I can't stay here.

    She likely has a key.

    And I'm on the verge of passing out.

    I need an escape route.
    """

    pause 1.0

    """
    My eyes fix on the window.

    This bedroom is not too high.

    I might be able to climb down safely.

    I throw open the window.

    Thankfully, it isn't locked.

    Below, there is a picket fence.

    But if I can guide my descent, I might avoid it.

    I just need to...
    """

    play sound door_rattling

    """
    She's right outside.

    Time is running out.

    Gripping the window sill, I prepare to jump.

    If I can control my fall, maybe I can...
    """

    $ lad_details.saved_variables["day3_ending"] = "fell"

    stop sound

    $ stop_music()

    return
