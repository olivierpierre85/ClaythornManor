label nurse_day2_evening_steal_caught:

    $ play_music('scary', 3)

    butler """
    Forgive me, Miss Marsh.

    I believe that item belongs with the service.
    """

    """
    I freeze.

    The butler is standing entirely too close, his expression as impassive as ever.

    He extends an open, expectant hand.
    """

    nurse """
    I can explain.

    I assure you, it is a misunderstanding.
    """

    host """
    Is there a problem?
    """

    """
    Lady Claythorn pauses at the doorway, her sharp eyes taking in the scene.
    """

    butler """
    I observed Miss Marsh securing a piece of the silverware in her bag, my lady.
    """

    host """
    Is this true?
    """

    """
    My face burns as I slowly reach inside and place the silver spoon back upon the table.
    """

    host """
    I can hardly believe my own eyes.
    """

    nurse """
    Lady Claythorn, please...

    I had no intention of keeping it.

    I was only admiring the craftsmanship.
    """

    """
    Lady Claythorn looks straight at me.

    A hard look that says she does not believe me, not a single word.

    But that she also does not quite know what to do.

    That must be a first for her.
    """

    nurse scared """
    Please, believe me.

    This is all a terrible misunderstanding!
    """

    butler """
    Forgive me, my lady, but I am not in the habit of making mistakes.

    I noted several pieces missing after luncheon.

    That is why I took it upon myself to be more watchful this evening.
    """

    """
    This silences everyone in the room.

    All eyes are fixed upon me now.
    """

    captain """
    Several pieces, you say?

    Then we ought to know exactly how far this has gone.
    """

    """
    The Captain turns to the butler without waiting for Lady Claythorn's leave.
    """

    captain """
    Go to Miss Marsh's room and search her belongings.

    If she has taken anything else, bring it here.
    """

    butler """
    At once, sir.
    """

    """
    He leaves without another word.

    I stand rooted to the spot, my heart hammering against my ribs.

    I know precisely what he will find.

    No one speaks. Lady Claythorn remains in the doorway, watching me with that terrible, steady gaze.

    The Captain stands with his arms folded. The others avoid my eyes.

    The minutes stretch unbearably.
    """

    nurse """
    Please, this really is not necessary...
    """

    captain """
    I rather think it is.
    """

    """
    At last, I hear footsteps on the stairs.

    The butler reappears, carrying a small cloth bundle which he sets upon the table.

    He unfolds it carefully, revealing a silver spoon and a fork, identical to the ones we have been using this weekend.
    """

    butler """
    These were in Miss Marsh's travelling case, my lady.

    Concealed beneath her garments.
    """

    """
    The room falls utterly silent.

    There is nothing left to say. The evidence is laid out before them, plain as day.
    """

    captain """
    Given what has just been found, I think we can dispense with any further talk of misunderstandings.

    Miss Marsh is clearly not who she claims to be.
    """

    """
    I try to think of an answer, but words elude me.
    """


    lad """
    What are we going to do then?
    """

    psychic """
    We cannot possibly allow her to roam the house freely.

    I am sorry, Miss Marsh, but I shall not feel safe until you are secured somewhere.
    """

    host """
    Quite right.

    We could confine her to her room, just as we did with Mr Manning.

    Tomorrow, we shall see what the police make of all this.
    """

    captain """
    A sensible precaution.

    Allow me to escort her upstairs, Lady Claythorn.

    Just to be absolutely certain there is no further trouble.
    """

    host """
    Thank you, Captain.

    See to it that she is securely locked in.
    """

    """
    I try to muster some dignity, but with all their eyes upon me, there is none to be found.

    I follow the Captain upstairs with my head bowed.

    He walks closely behind me the whole way, ensuring I do not stray.
    """

    $ change_room("bedroom_nurse", dissolve)

    """
    When I reach my room, I step inside.

    The door closes firmly behind me, followed by the definitive click of a key turning in the lock.
    """

    captain """
    Forgive me, Miss Marsh. I have no choice in the matter.
    """

    """
    They believe I am trapped here.
    
    But they underestimate me.
    
    A hairpin and a steady hand are all I require to open such a simple lock.
    
    I shall wait until the house is completely silent, and then I will take my leave.
    
    It is far from ideal, but it is my only chance.
    """

    call wait_screen_transition()

    call change_time(23, 30)

    $ change_room("bedrooms_hallway")

    """
    I slip out into the hallway undetected.

    Nobody is there.

    I keep close to the walls, hoping I do not run into any servants performing their night duties.

    But the manor is dead silent.
    """

    $ change_room("entrance_hall")

    """
    I reach the entrance hall and look one last time upon the impressive place.

    I force the lock, then quickly make my way outside.
    """

    $ change_room("forest_road")
    
    """
    The road ahead is long, and the air is bitterly cold.
    """

    if nurse_details.threads.is_unlocked('day1_exhaustion'):

        """
        I push myself forward, intending to walk all the way to the next town.
        """

        jump nurse_day2_exhaution

    else:

        """
        I walk through the night until my feet are raw, pushing myself onward until the first light of dawn breaks over the town.

        I have escaped with my life.

        But I am entirely alone, shivering in the morning chill.
        """

        jump nurse_ending_escape_poor