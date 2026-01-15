# TODO rewrite everything BAD AI JOB
label doctor_day3_morning_nurse:

    $ change_room('bedroom_nurse', irisout)

    """
    I wake up to the soft sound of someone entering the room.
    
    Miss Marsh is coming in.
    """

    nurse """
    I've just come from the dinner room, it's empty.

    In fact I didn't see anyone anywhere.

    No staff at all.
    """

    doctor """
    How is it possible?

    Where could everyone have gone?

    That doesn't make sense.
    """

    nurse """
    I don't know, but it is indeed very suspicious.

    We were right to be cautious, something weird is definitely happening here.
    """

    doctor """
    But what should we do then?

    Should we...
    """

    nurse """
    Shh. I hear someone coming.
    """

    """
    She puts her ear to the door.

    I get up quietly and join her.
    """

    """
    We hear two people walking together, talking in low voices.

    I recognise Ted Harring and Amelia Baxter.

    After they have passed, Rosalind Marsh confirms it.
    """

    nurse """
    Ted Harring and Amelia Baxter.

    What are they doing here? There is no reason for them to pass by my door.

    I don't like this.
    """

    doctor """
    Maybe they're just looking for the staff.

    They must be as surprised as we are.
    """

    nurse """
    Maybe, but I don't know.

    It could be something else entirely.

    I don't really trust those two.
    
    I prefer if we avoided them at the moment.
    """

    doctor """
    If it helps keep your mind at ease, why not.

    But what should we do instead?
    """

    nurse """
    Well, we can't stay in this room.

    They might come looking here eventually.
    """

    doctor """
    So what do you propose?
    """

    nurse """
    I know a place where we can hide for a while until we know more.
    """

    doctor """
    Very well. Where are we heading?
    """

    nurse """
    Come with me, I'll show you.
    """

    """
    Without waiting for an answer she slightly opens the door and takes a peek outside.
    """

    nurse """
    The hallway is clear. Come with me.
    """

    doctor """
    Fine.
    """

    """
    We make it only a few steps before we hear another set of footsteps.

    Miss Marsh pulls me into a narrow recess beside a service door.

    I press my back against the cold wood, holding my breath.

    Captain Sinha appears in the corridor, moving with quiet purpose.

    He pauses for a moment, as if listening, then continues on his way downstairs.

    I glance at Miss Marsh.

    She is perfectly still, her breathing shallow and controlled.

    She knows exactly how to make herself invisible.

    It is impressive, and slightly unsettling.

    It feels like this is not the first time she has had to hide like this.

    When the danger is over, she signals for me to follow her.

    We take a flight of stairs up to the attic.
    """

    $ change_room('attic_hallway')

    nurse """
    Perfect. There is a room here I can lock.

    I don't think they would look here.
    """

    doctor """
    Interesting, how did you get the key to this room?
    """

    """
    She doesn't answer and just turns the key.
    """

    play sound door_open

    nurse """
    Come on in, Doctor, it's empty.
    """

    $ change_room('butler_room')

    """
    I follow her, and she immediately closes the door behind me.
    """

    play sound door_locked

    nurse """
    We should sit tight here for a bit.

    My guess is that they will try to look everywhere but here.

    In a while, either they'll have found someone or realise we are the only ones left in the Manor.

    We can go check again then.
    """

    """
    She thought of everything. I don't think I would have acted that way on my own.

    It's unsettling.
    """

    doctor """
    Excuse me, but you didn't answer. How did you get the key to this room?
    """

    nurse """
    Oh, I found it in the main hall earlier this morning, on a table.

    It's a pass that opens all the doors in the mansion apparently.

    Wherever he went, the butler didn't think he would need his key anymore.
    """

    doctor """
    Right, so he's probably gone for good then.
    """

    nurse """
    That's what I think, and the rest of the staff probably went with him.
    """

    doctor """
    As well as Lady Claythorn.
    """

    nurse """
    Yes, it's very likely.
    """

    call wait_screen_transition

    call doctor_day3_afternoon


