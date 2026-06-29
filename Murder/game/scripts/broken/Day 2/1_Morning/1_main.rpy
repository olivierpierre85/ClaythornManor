# --------------------------------------------
#   Broken
#
#   Saturday - Morning
#
#   08:30 -> 10:30
#
#   Music: upbeat, mysterious, scary
#
#   Position
#       - Bedroom : Broken
#       - Dining Room : Everyone
#       - Dead : Lad (Ted Harring)
#
#   Notes :
#       - Mirrors the canonical "Moody is found dead" morning, but here Broken
#         lives and Ted Harring is the one found dead in the night.
#       - The guests remark on his youth and good health, the doctor can find no
#         cause, yet the host proposes the hunt all the same.
#       - Straight narration, no menus. Reuses common host-to-doctor / hunt labels.
#       - Stops at the hunt (work_in_progress).
# --------------------------------------------
label broken_day2_morning:

    call change_time(8, 30, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ broken_details.add_checkpoint("broken_day2_morning")

    call black_screen_transition("Thomas Moody", chapters_names[current_chapter])

    $ change_room("bedroom_broken", irisout)

    $ play_music('chill', 3)

    """
    I wake up from a restless sleep.

    For a moment I cannot place myself.

    Then it comes back to me. The manor. The mask. Thomas.

    And then there is the letter.

    The proof that Captain Sinha's orders led Thomas to his injuries, and very likely, to his death.

    Who put it there, and why?

    It is most likely the one who invited us here.
    
    And they want Thomas Moody to harm Sushil Sinha.

    It is an obvious plot, and I am sure Thomas would have jumped at the chance to take revenge.

    And a part of me wants to avenge him as well.
    """
    
    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        But there's also the matter of what the maid told me. 
        
        The surprise prepared for the guests.

        Is the letter part of that surprise?

        If so, I dread what will come next.
        """

    """
    With that in mind, I go down.
    """

    call change_time(9, 0)

    $ change_room('dining_room', dissolve)

    """
    The dining room is already half filled.

    Captain Sinha sits at the far end, upright over his plate, eating as though it were a duty.

    I am surprised at myself for feeling an overwhelming sense of anger towards him.

    I try to remember that in war, terrible things happen no matter what. 

    There is no reason to blame someone who simply signed a piece of paper.

    Yet, that doesn't entirely calm me.

    Doctor Baldwin is opposite him, his eyes ringed and distant, a man who has slept badly or not at all.

    Miss Baxter and Miss Marsh have their heads bent together over the teapot.

    I take the chair I was given last night, near the head of the table, and help myself to a modest plate.

    Samuel Manning is the last to appear, or rather to fall through the door.

    His colour is dreadful and his hands will not be still.

    He makes for the coffee and nothing else, then drops into the nearest chair without a word to anyone.

    Miss Baxter's mouth thins at the sight of him, though she holds her tongue.

    Only one place stands empty.

    The young fellow, Harring, who sat beside Miss Baxter at dinner, has not come down.

    A late riser, perhaps.
    """

    $ play_music('mysterious', 2)

    """
    I am still taking the measure of them all when the butler slips in and bends to Lady Claythorn's ear.

    She rises and crosses to the doctor, and asks him to follow them upstairs.
    """

    pause 1

    """
    The three of them leave together, the butler leading, the doctor a pace behind.

    I resist the urge to follow them, as I have no reason to.

    The door closes, and the room settles into a silence no one cares to break.

    There are no happy reasons to call a doctor for, and everybody here knows it.
    """

    call wait_screen_transition()

    call change_time(10, 0)

    """
    A long quarter of an hour passes before Lady Claythorn returns, the doctor a pace behind her.

    She does not sit.

    She stands at the head of the table and folds her hands, and we all know before she speaks that the news is grave.
    """

    host """
    I am so dreadfully sorry to bring you such news.

    It appears that Mr Harring passed away during the night.
    """

    """
    The room goes very still.
    """

    captain """
    Mr Harring?

    But he was a young man, scarcely more than a boy.
    """

    nurse """
    Are you quite certain, Doctor?

    He seemed in perfect health only last evening.
    """

    doctor """
    I can find no mark upon him, and no cause I am able to point to.

    A man of his years, and sound by every appearance.

    I so not I understand it.

    What I am certain of is that the authorities must be sent for.
    """

    host """
    Yes. Of course.

    My butler will see to it at once.
    """

    """
    We sit a while in a heavy silence.
    """

    if broken_details.threads.is_unlocked('found_poison'):

        """
        The bottle of rat poison I still have in my pocket suddenly comes to mind.

        Why was it so carelessly left there, still open as if someone had just used it?

        But it is too vague an intuition to bring it up.

        Besides, I would have to explain what I was doing downstairs, and I am not ready for that.

        So I say nothing for the moment.
        """

    """
    Whatever brought me beneath this roof, I had not predicted a death would occur.

    And if it is murder, then no one here is safe, the false Thomas Moody least of all.

    I had best keep my wits about me, and my eyes upon the rest of them.
    """

    call wait_screen_transition()

    """
    When the plates are empty and the worst of the murmuring has died away, Lady Claythorn speaks again.
    """

    $ play_music('chill', 3)

    host """
    Now, as I told you all yesterday, there were diversions arranged for this morning.

    A shooting party was to set out after breakfast, for those who cared to join it.

    I know how dreadful this is.

    But I do not believe it would do any good to sit and brood the day away.

    So, if no one objects, I should like us to carry on much as we had planned.
    """

    """
    For a moment no one answers at all.
    """

    nurse """
    Forgive me, Lady Claythorn, but a young man has died in this house not an hour ago.

    Surely you cannot mean for us to go out shooting as though nothing had happened?
    """

    """
    A few quiet voices murmur their agreement with her.
    """

    host """
    I understand you, truly I do.

    But the authorities cannot reach us much before the afternoon, and there is nothing any of us can do for him now.

    I would far sooner keep you all occupied than leave you to dwell upon it.
    """

    """
    The objection falters, less from being really convinced but from the simple fact that Lady Claythorn is our hostess.

    And habit commands us to simply go along with what she is proposing.

    Amelia Baxter and Rosalind Marsh signals they would stay inside, as they would have done anyway.

    For my own part, I weight for a second staying with them.
    
    That would the perfect opportunity to explore the house.
    
    And my injuries would be the perfect cover to explain my reluctance in participating.

    But a hunt is a perfect opportunity to interrogate someone privately.

    And there are a few question I would like to ask Captain Sinha.

    This could be the perfect opportunity to talk to him alone.

    So I shall go.
    """

    jump broken_day2_hunt
