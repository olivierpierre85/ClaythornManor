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

    pause 1.0

    """
    As soon as Captain Sinha has left the room, Amelia stands up.
    """

    call common_day3_afternoon_lad_psychic_stay

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
    Oh, nothing special. I just realized the plate set out for me is too full.

    I won't be able to eat that much.

    But you are a strong gentleman.
    
    I am sure you won't mind switching with me, right?
    """

    lad """
    I actually do mind.

    Not the quantity, but I already seasoned my plate exactly how I like it.

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

    I rush to her side.
    """

    psychic """
    What is happening?

    This doesn't make any sense.

    I thought I...
    """

    """
    She realizes I am holding her hand.
    """

    # Important TED or Mr Harring? TED is STROng clue
    psychic """
    Oh, Ted, I shouldn't have lied to you.
    """

    lad """
    What do you mean? Lie about what?
    """

    psychic """
    About everything.

    That... I've never been a psychic, that was just a lie.

    I am just an actress...

    I...
    """

    lad """
    Don't say anything, you need to keep your strength.
    """

    psychic """
    No it's too late for that.

    I need to confess ... now...

    I...

    I...
    """

    """
    She can't finish her sentence.
    """

    $ psychic_details.unlock_knowledge('lie') 

    $ play_music('scary')

    pause 2.0

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

    $ change_room("lad_room")

    """
    Once inside, I slam the door shut.

    Panic floods my mind.

    I can't stay here.

    She likely has a key.

    And I'm on the verge of passing out.

    I need an escape route.
    """

    pause 1.0

    """
    My eyes fix on the window.

    The fall doesn't look too severe.

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
