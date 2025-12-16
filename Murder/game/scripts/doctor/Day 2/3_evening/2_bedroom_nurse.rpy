
label doctor_day2_evening_bedroom_nurse_default:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    doctor """
    Hello?
    """

    nurse """
    Yes?

    Is that you Doctor Baldwin?
    """

    doctor """
    Yes, it is.

    Do you mind if I come in for a minute?

    I have something important to discuss.
    """

    nurse """
    I do not know, Doctor. 

    It is late, and that would be rather inappropriate.

    Also, with everything that has happened today, I would prefer to stay alone.

    I hope you understand.
    """

    return


label doctor_day2_evening_bedroom_nurse_do_not_remember:

    call doctor_day2_evening_bedroom_nurse_default

    """
    She is right.

    I cannot simply insist upon entering the room of a woman I scarcely know at this hour.

    I should not press the matter.
    """

    doctor """
    My apologies for disturbing you.

    I shall leave you in peace, Miss Marsh.

    Good night.
    """

    nurse """
    Good night, Doctor.
    """

    return


label doctor_day2_evening_bedroom_nurse_remember:

    call doctor_day2_evening_bedroom_nurse_default

    doctor """
    I do understand, believe me.

    Yet, as you reminded me earlier, you and I have worked side by side in far less proper circumstances than this.

    I would not trouble you now without very good reason.
    """

    """
    There is a brief pause.

    I hear the soft creak of a floorboard, as if she has stepped closer to the door.
    """

    nurse """
    Very well, what is it then?
    """

    doctor """
    It is not something I care to discuss in the hallway.

    May I come in, just for a moment?
    """

    """
    For a few seconds there is only silence, and the faint crackle of a fire from within her room.
    """

    nurse """
    All right.

    Please come in, Doctor.
    """

    play sound door_open

    $ change_room("bedroom_nurse")

    """
    I step into Miss Marsh's room.

    She has not yet undressed, but her shoulders sag with weariness, and there are dark shadows beneath her eyes.
    """

    doctor """
    Thank you.

    I shall be as brief as I can.
    """

    """
    I give her a concise account of the letter I discovered in Samuel Manning's room.
    
    Then I explain how it urged him to provoke me before the hunt, and how it led, step by step, to his death.

    As I speak, the colour drains from her face.
    """

    nurse """
    Good heavens.

    Are you saying someone lured you both into that situation on purpose?
    """

    doctor """
    That is precisely what I fear.

    Whoever wrote that letter knew far too much, and I doubt they are finished.

    I believe they may try again, with me or with someone else in this house.
    """

    nurse """
    And you came to me because we worked together before?

    Because you think you can trust me?
    """

    doctor """
    Indeed, I would rather face this night with an ally than entirely alone.
    """

    nurse """
    I cannot pretend I am not frightened.

    Every sound in this place sets my nerves on edge.

    I am thinking, to be perfectly safe maybe you could ...

    No, never mind, it's probably not a good idea.
    """

    doctor """
    What could be? In these circumstances, we shouldn't be afraid to share what we think.
    """

    nurse """
    All right then, I meant that , if we really are in danger, you should probably ... sleep here tonight.

    Not on the bed I mean, maybe on a chair.

    I know it's very unconventional, but that would make me feel better.
    """

    call run_menu( TimedMenu("broken_generic_other_guests_friday_offense", [
            TimedMenuChoice("I guess it's the safest thing to do", 'doctor_day2_evening_bedroom_nurse_sleep_yes', TIME_MAX, early_exit = True),
            TimedMenuChoice("I'd rather sleep alone", 'doctor_day2_evening_bedroom_nurse_sleep_no', 0, early_exit = True),
        ])
    )

    return


label doctor_day2_evening_bedroom_nurse_sleep_yes:

    doctor """
    Very well.

    If you will permit it, I shall take that chair by the door.

    You may lie down and try to sleep, and I shall keep watch.
    """

    nurse """
    Thank you, Doctor.

    I confess I shall feel safer knowing you are here.

    And I am sorry if I am not good company, but I imagine I shall be asleep in a few moments.
    """

    doctor """
    No worries, please rest.
    """

    """
    I move a straight-backed chair to a position where I can see both the door and the window.

    Miss Marsh sits upon the edge of the bed, then lies down without undressing, her eyes already half closed.
    """

    nurse """
    Wake me if anything seems amiss.

    Otherwise, let us hope the night passes quietly.
    """

    doctor """
    You have my word.

    Try to rest.
    """

    """
    The fire burns low in the grate, filling the room with a dull orange glow.

    I settle into the chair, listening to the ticking of the clock, and the slow deepening of Miss Marsh's breathing as she drifts into sleep.

    Pretty soon it's my turn to doze off.
    """

    call wait_screen_transition

    play sound door_locked

    """
    I am deep asleep when the door suddenly rattles.

    I blink myself awake and see Rosalind Marsh standing close to it, one hand still near the bolt.
    """

    doctor """
    Miss Marsh?

    What are you doing?

    Are you going somewhere?
    """

    nurse """
    Oh, of course not, Doctor.

    I am afraid I am becoming rather paranoid.

    I only wanted to be certain the door was properly fastened.

    But it is, so I can return to bed now.

    I am sorry to have woken you.
    """

    doctor """
    Do not apologise.

    Try to get some rest.

    Good night, Miss Marsh.
    """

    nurse """
    Good night, Doctor Baldwin.
    """

    """
    Strange.

    Still, I cannot blame her for being on edge.
    """

    $ doctor_details.threads.unlock('trust_nurse')

    return


label doctor_day2_evening_bedroom_nurse_sleep_no:

    doctor """
    I am truly sorry but I don'think this would be right.

    I believe it would best if we sleep in our own bed tonight.

    But we can convene first thing in the morning and get ready for whatever awaits us.
    """

    nurse """
    As you wish, Doctor.

    And... thank you for telling me.

    Whatever happens, I am glad you did not keep this to yourself.
    """

    """
    I incline my head and step back into the corridor.

    Miss Marsh follows me to the threshold and closes the door softly behind me.
    """

    $ change_room("bedrooms_hallway")

    """
    The hallway feels colder than before, and the silence of the sleeping house presses in on every side.
    """

    # TODO ending or Possibility to look somewhere else? Ending to mirror captain, but maybe do something to allow start again with captain?
    jump doctor_day2_evening_sleep_alone