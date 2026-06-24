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

    $ play_music('upbeat', 2)

    """
    I wake to a thin grey light and the unfamiliar weight of a strange bed.

    For a moment I cannot place myself.

    Then it comes back to me. The manor. The mask. Thomas.

    Day two.

    I came through the first night without being found out, but the hardest part is still ahead of me.

    I sit up and reach for the mask on the bedside table.
    """

    """
    The leather is cold against my skin.

    I settle it into place, and Archie disappears beneath Thomas Moody for another day.

    I run through his history once more, the way another man might say his prayers.

    Liverpool. The boot-boy years. The commission. The War.

    When I am word-perfect, I go down.
    """

    call change_time(9, 0)

    $ change_room('dining_room', dissolve)

    """
    The dining room is already half filled.

    Captain Sinha sits at the far end, upright over his plate, eating as though it were a duty.

    Doctor Baldwin is opposite him, his eyes ringed and distant, a man who has slept badly or not at all.

    Miss Baxter and Miss Marsh have their heads bent together over the teapot.

    I take the chair I was given last night, near the head of the table, and help myself to a modest plate.

    Then I let my gaze travel the room as Thomas never would, marking who is present and who is not.
    """

    """
    One place stands empty.

    The young fellow, Harring, who sat beside Miss Baxter at dinner, has not come down.

    A late riser, perhaps. The young so often are.
    """

    """
    Samuel Manning is the last to appear, or rather to fall through the door.

    His colour is dreadful and his hands will not be still.

    He makes for the coffee and nothing else, then drops into the nearest chair without a word to anyone.

    Miss Baxter's mouth thins at the sight of him, though she holds her tongue.
    """

    $ play_music('mysterious', 2)

    """
    I am still taking the measure of them all when the butler slips in and bends to Lady Claythorn's ear.

    Whatever he tells her drains the colour from her face in an instant.

    She rises, gathers her composure back into place with an effort I should not have caught had I not been watching for it, and crosses to the doctor.
    """

    call common_day2_morning_host_to_doctor

    """
    The three of them leave together, the butler leading, the doctor a pace behind.

    The door closes, and the room settles into a silence no one cares to break.
    """

    """
    A summons for the doctor, before the plates are even cleared.

    That is not a thing one does for a guest who has merely overslept.

    Something is wrong in this house this morning.

    I keep my eyes on my plate and my ears open.
    """

    if broken_details.threads.is_unlocked('talked_to_maid'):

        """
        The maid's words come back to me unbidden. A surprise prepared for the guests, she said.

        I begin to wonder what shape that surprise will take.
        """

    call change_time(10, 0)

    $ stop_music()

    """
    A long quarter of an hour passes before Lady Claythorn returns, the doctor a pace behind her.

    She does not sit.

    She stands at the head of the table and folds her hands, and we all know before she speaks that the news is grave.
    """

    host """
    I am so dreadfully sorry to bring you such news.

    It appears that Mr Harring passed away during the night.
    """

    $ play_music('scary')

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

    I will not insult you by pretending I understand it.

    What I am certain of is that the authorities must be sent for.
    """

    host """
    Yes. Of course.

    My butler will see to it at once.
    """

    psychic """
    That poor young man.

    To be taken so early, with all his years still before him.

    It does not bear thinking on.
    """

    """
    We sit a while in a heavy silence.
    """

    """
    A young man, sound as a bell at dinner, dead before breakfast, and no mark upon him.

    I have written up enough inquests to know how seldom the world arranges itself so tidily.

    Men of thirty do not simply stop in the night.
    """

    if broken_details.threads.is_unlocked('found_poison'):

        """
        The bottle from the scullery lies at the bottom of my case, a measure lighter than it ought to be.

        I had put that down to carelessness. I am no longer certain that is what it was.
        """

    """
    And then there is the letter.

    Last night someone laid an old army order upon my pillow, and at the foot of it sat a name. Captain S. Sinha.

    A staff officer who signed better men forward to their deaths, and never once went himself.

    He sits not ten feet from me now, eating his breakfast as though nothing in the world were amiss.

    A man with that upon his conscience would hardly balk at one death more.
    """

    """
    Whatever brought me beneath this roof, I had not reckoned on murder.

    And if it is murder, then no one here is safe, the false Thomas Moody least of all.

    I had best keep my wits about me, and my eyes upon the rest of them.
    """

    call wait_screen_transition()

    $ stop_music()

    """
    When the worst of the murmuring has died away, Lady Claythorn draws breath and speaks again.
    """

    call common_day2_morning_host_hunt

    """
    A man lies dead above our heads, and our hostess speaks of sport as though we had lost no more than an hour to bad weather.

    That composure is a thing worth remembering.

    For my own part, I have no wish to be left behind in this house, picking at cold eggs while I wait to learn who is next.

    Better to be out of doors and among them, where I can watch.

    And a man invited for his soldiering could hardly cry off a morning's shooting without turning every head towards him.

    So I shall go.
    """

    """
    A low murmur of assent runs round the table.

    The Captain accepts at once, and Mr Manning allows that the air may do him some good, though he looks fit for nothing but his bed.

    The two ladies will keep to the house.
    """

    call common_day2_morning_hunt_end

    jump work_in_progress
