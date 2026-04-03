label nurse_day2_evening_steal_caught:

    $ play_music('danger', 2)

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
    Every excuse I have ever rehearsed vanishes at once.

    My throat tightens. My hands will not stop trembling.

    No point in denying now.

    I slowly reach inside my bag and place the silver spoon back upon the table.
    """

    host """
    Miss Marsh, I can hardly believe it.
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

    if nurse_details.threads.is_unlocked('steal_pearls'):

        """
        He reaches into the cloth once more and produces a string of pearls, which he sets down beside the cutlery.
        """

        butler """
        And these, my lady.
        """

        host """
        My pearls!

        Good heavens, those are my pearls!

        I was planning to wear them this very evening!
        """

        """
        Lady Claythorn's composure cracks, if only for a moment, before she steadies herself again.
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

    captain """
    We ought to confine her to her room, just as we did with Mr Manning.

    Tomorrow, we shall let the police sort this out.

    Allow me to escort her upstairs, Lady Claythorn.
    """

    host """
    Yes, I think that is wise.

    Thank you, Captain.
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
    His footsteps retreat down the corridor.

    I press my back against the door and sink to the floor.

    I don't think the police will arrest me for this.

    But what will happen if the words go out?

    My reputation could be gone in an instant.

    I sit there for a long while, staring at nothing.
    """

    $ stop_music(2)

    call wait_screen_transition()

    call change_time(23, 30)

    """
    Then something steadies inside me. Self-pity will not help me.

    They believe I am trapped here.

    But a hairpin and a steady hand are all I require to open my door.

    I shall wait until the house is completely silent, and then I will take my leave.

    Certainly, they will not come after me.

    Not for such a minor small crime.

    I could leave and it would be as I've never been here.
    """

    $ play_music('scary', 3)

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

    $ change_room("manor_exterior")

    """
    The night air hits me like a slap.

    I keep to the shadows, moving along the side of the house towards the drive.

    Then I stop.

    Ahead, near the garage, a motorcar stands with its engine running, its headlamps cutting two pale beams into the dark.

    Figures are moving around it — quickly, purposefully.

    I press myself flat against the wall and watch.
    """

    """
    The butler emerges first, carrying two heavy cases which he loads into the boot.

    Behind him, the footman and the maid, each with bags of their own.

    And then Lady Claythorn herself, wrapped in a fur coat, clutching a leather valise to her chest.

    She does not look back at the house. Not once.

    She climbs into the rear of the motorcar without a word.
    """

    """
    The doors close. The engine growls.

    The motorcar pulls away down the drive, its lights shrinking into the darkness until they are gone entirely.

    I stand there for a long moment, pressed against the cold stone, trying to make sense of what I have just seen.

    The lady of the house, fleeing her own estate in the dead of night, with every last member of her staff.

    Whatever is happening in this place, it's better if I don't linger.
    """

    $ change_room("forest_road")

    """
    The road ahead is long, and the air is bitterly cold.

    I walk quickly at first, putting as much distance as I can between myself and the house.

    But the road is dark, and I did not think to bring a lamp.

    The drive gives way to a narrow lane, then to a fork I do not remember from the journey here.

    I choose left. Or perhaps right. I am no longer sure.
    """

    $ change_room("forest")

    """
    The trees press closer.

    The road, if it is still a road, narrows to little more than a track.

    I stumble over a root and catch myself against a trunk, bark scraping my palms.

    I should turn back. But turn back to where?

    I have lost the road entirely.
    """

    """
    The cold settles into me like water filling a glass.

    I keep walking, but my steps grow shorter, slower.

    The trees all look the same.

    Every direction is darkness.
    """

    """
    I sit down against a tree, just for a moment.

    Just to gather my strength.

    The ground is damp and freezing, but my legs will not carry me any further.

    I pull my coat tighter and close my eyes.

    Just for a moment.
    """

    jump nurse_ending_escape_at_night