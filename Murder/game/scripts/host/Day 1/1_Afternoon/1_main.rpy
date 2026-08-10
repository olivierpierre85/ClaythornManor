# --------------------------------------------
#   Host
#           
#   Friday - Afternoon
#   
#   10:00 -> 16:30
#
#   Music: Elegant, slightly mysterious
#
#   Alive: Everyone
#
# --------------------------------------------
label host_introduction:

    call change_time(12, 0, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    call black_screen_transition("", "Lady Claythorn")

    $ play_music('chill')

    $ change_room("train_inside_first")

    """
    The journey from London is finally coming to a close.

    I am eager, but also nervous, about the most unusual role I have ever been hired to play.

    The hostess of a Scottish manor.

    A prominent lady.

    All of it to entertain a group of unlikely people.

    I received only the barest information about the reason behind the whole thing.

    I was told I would learn more once I was there.

    Well, here I am.

    Let's make the most of it.
    """

    $ change_room("train_station", irisout)

    """
    I have barely stepped down from the carriage when an old acquaintance in a butler's uniform approaches me.
    """

    butler """
    Good, you made it on time.

    Please come this way.
    """

    """
    Without ceremony, he guides me into a car.
    """

    $ change_room("inside_car")

    butler """
    We will be there soon.

    Claythorn Manor.

    From now on you are the lady of this place.

    Don't forget it.
    """

    host """
    I don't understand why you can't be the lord.

    You would clearly be better at it than I.
    """

    butler """
    You mean because I am the better actor?
    """

    host """
    I didn't say that.

    And you are not.

    But I know you are familiar with that type of house.
    """

    butler """
    True, I was a footman when I was younger.
    
    A very long time ago.
    """

    $ butler_details.description_hidden.unlock('job')

    butler """
    But that's precisely why I should be the butler.

    You see, in this kind of environment, the staff are scrutinised more than the host.

    That's a rule.

    As the lady of the house, you can do almost anything.

    At worst you will be labelled as eccentric.

    But to maintain the illusion, the staff can't afford a mistake.

    That's why I have to be in charge of them.

    Besides, a butler must always be a man.
    """

    host """
    Right.

    But I've been assured that the guests we are receiving won't be accustomed to all this.

    None of them is of a standing important enough to notice little mistakes in the service.
    """

    butler """
    Maybe so, but the rest of our staff are all actors too.
    
    They have very little domestic experience, if any.

    So we shouldn't take any chances.
    """

    $ change_room("manor_exterior", irisout)

    call change_time(12, 30)

    """
    Finally, I can spot the Manor from afar.

    This is becoming real now.
    
    I feel a knot inside my stomach and wonder what I have got myself into.
    """

    butler """
    All right, the others are already there to prepare the house.
    
    Let us not waste any time.
    """

    $ change_room("entrance_hall")

    """
    Two other people are gathered in the entrance hall.

    A young man, rather dashing, and a girl who cannot look more than eighteen years old.
    """

    host """
    Is that everyone?
    """

    butler """
    I am afraid so.

    It would have been dangerous to bring more people in.
    """

    host """
    Is that enough for a house this size?
    """

    butler """
    Normally no, but for the weekend we shall have to make it work.

    I have already briefed them, so they know what their roles are.

    This gentleman will be acting as footman and driver.
    """

    footman """
    Nice to meet you, ma'am.
    """

    """
    He says it with deference, as though he is already in character.

    Good.
    """

    host """
    Hello.

    What should I call you?
    """

    footman """
    Thomas, my lady.
    """

    butler """
    And this is Elsie, our cook and maid for the weekend.
    """

    maid """
    Hello, ma'am.
    """

    butler """
    Those are not their real names, of course.
    """

    host """
    Of course.
    """

    """
    I will not know their names, and they won't know mine.

    And if I run into them on a stage in the future, we will act as if we were meeting for the first time.

    Those were the terms we agreed on.
    """

    host """
    And what should I call you?
    """

    butler """
    Hmm, with any luck you won't have to call me at all, since I'll be the one managing everything this weekend.

    But if you must, call me 'Barrow'.
    """

    $ butler_details.description_hidden.unlock('name')

    host """
    Barrow it is, then.
    """

    butler """
    Very well, now that the introductions have been made, I believe everybody knows what their role will be this weekend.

    Now let's get to it.
    """

    footman """
    Yes, sir!
    """

    maid """
    Very well.
    """

    """
    They both head downstairs.

    As for me, I go to my room to settle in and get ready for the evening.
    """

    jump host_day1_evening
