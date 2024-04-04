label psychic_day3_afternoon_escape:

    psychic """
    You are right.

    I can't stay one minute more in this cursed place.
    """

    captain """
    Are you sure?

    It's not going to be an easy walk.
    """

    psychic """
    I am certain.
    """

    captain """
    Very well, let's get ready before leaving then.

    I suggest we all get our more comfortable shoes, warm clothes and leave everything else here.

    No need to be ecombered by our luggages. Hopefully we will come back to get them soon enough.

    Let's get ready and meet in the main hall in 15 minutes then.

    Do you agree?
    """

    psychic """
    Of course.
    """

    lad """
    Sounds good to me.
    """

    pause 1.0

    $ change_room('great_hall', dissolve)

    """
    I rush to my room, take back what I need and go down the hall as fast as possible.

    The other are already there.
    
    Captain Sinha has a large coat and big boots with him.

    Ted Harring on the other hand doesn't seem to have changed clothes at all.
    """

    captain """
    All right, if every one is ready, let's leave then.
    """

    """
    We then proceed to exit the house, leaving it's sinister shade behind us.
    """

    $ change_room('forest_road', dissolve)

    $ stop_music()

    """
    We have been walking a couple of miles already and everything is going smoothly, maybe too smoothly.

    Except for the fact that I am trailing behind Ted Harring and Sushil Sinha.

    I am clearly not build for this kind of activity

    I stop for a while to take a little break.
    
    As I catching my break, look at the forest surrounding us.

    Then...
    """

    $ play_music('danger', 2)

    psychic """
    Captain, could come and see something?
    """

    captain """
    Of course, what is it?
    """

    """
    He retrace his steps to me level, while Ted Harring keeps on walking ahead.
    """

    psychic """
    Can you look this way, behind that huge oak tree.

    I believe I saw something.

    I might be imagining things but it looked like a person.
    """

    captain """
    I can spot the tree, but see no one.
    """

    psychic """
    I don't see it anymore, but it was there a second ago.

    I am certain of it.
    """

    captain """
    All right, I will go and check quickly.
    """

    """
    Without hesitation, he rush towards the large tree ahead.
    """

    play sound gun 


    psychic """
    Captain !!
    """

    """
    He stops right in his tracks.

    Looks like he is gonna collapsed but then comes back towards.
    """

    # I barely have the time to hide the smoking gun in my right hand.

    captain """
    Damn, I didn't see this one coming.

    Somebody his shot at us.

    Run!
    """

    """
    He then began to limp as fast as he could.

    I try to help him be carrying him.
    """

    captain """
    Stops this nonsense,

    Run to safety.
    """

    psychic """
    I can't leave you, you are injured, you need help.
    """

    captain """
    It's probably too late for that anyway.

    I think the bullet hit an artery.
    """

    """
    I looked down and see that his shirt is bright red.

    He is right, the wound looks fatal.

    But I try not to alarm him.
    """

    psychic """
    It's not so bad.

    I am sure you've had worst that this.
    """

    captain """
    Yeah right.

    This weekend is the most action I've seen in my entire life.    
    """

    psychic """
    What do you mean?
    """

    captain """
    Well there is no need to hide it now.

    I only fought one battle, and left in the middle of it.

    I was never a captain.

    I only pretented when I arrived to London because it was the only way to be treated decently.

    I should ..

    .. not have come here.
    """

    # REjoin ted harring

    # Escape TWO, rest is dead


    jump work_in_progress