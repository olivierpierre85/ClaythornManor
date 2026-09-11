# --------------------------------------------
#   Host - Sunday afternoon, she stays
#
#   She and the Captain go in to Ted Harring and Amelia Baxter, and Miss
#   Marsh comes down the stair to join them. Lunch is prepared by the two
#   women, the boy sets the table, and the hostess moves the plates.
#
#   Plates, as Ted Harring sets them down (see day3_poisoning_chart.md):
#       A - Miss Marsh's place, poisoned
#       B - Mr Harring's place, a sedative
#       C, D, E - Miss Baxter, the host, the Captain, clean
#   Miss Marsh, alone with the table, swaps A and B.
#   The host, who saw it, gives Ted her own plate, gives A back to Miss
#   Marsh, and keeps B for herself.
#   So Miss Marsh dies at the table, the host goes to sleep, and the other
#   three are left alone with a dead woman and a loaded revolver.
#
#   She wakes at three, with Samuel Manning shaking her, everyone else dead,
#   and the butler's car on the gravel.
#
#   Unlocks : drunk 'faked_death' and 'lie', butler 'took_valuables'
# --------------------------------------------
label host_day3_afternoon_stay:

    host """
    No.

    I have lied to those two for three days, and I have left them to themselves for three nights.

    I am not walking out of this house without so much as a word to them.
    """

    captain """
    Very well.

    But we keep to what we agreed. We say nothing of what you told me.
    """

    host """
    Nothing.
    """

    call change_time(12, 15)

    $ change_room('tea_room', dissolve)

    """
    Mr Harring is at the window, and Miss Baxter is in the chair by the dead fire.

    They both turn when the door opens, and the boy's face goes through three things at once before it settles on relief.
    """

    lad """
    Captain! Lady Claythorn!

    We've been over the whole house. We thought...
    """

    psychic """
    We thought we were the only ones left.

    Where is everybody? Where are the servants?
    """

    captain """
    Gone.

    The car went in the night, and the staff with it. Every one of them.
    """

    psychic surprised """
    Gone? But why?
    """

    captain """
    That I cannot tell you.
    """

    """
    He does not look at me as he says it, and I am grateful.
    """

    lad """
    And Mr Manning?

    You had his key.
    """

    captain """
    I opened his door this morning.

    He is dead. Killed in his bed, some time in the night.
    """

    psychic surprised """
    Oh dear God.
    """

    lad -scared """
    Killed? You mean somebody...
    """

    captain """
    His throat was cut.

    Whoever did it had a key to that door.
    """

    """
    Miss Baxter sinks back into her chair, and the boy has to find his voice before he can go on.
    """

    lad """
    What about the police, then?

    Lady Claythorn, you spoke to them yesterday. They're coming today, aren't they?
    """

    """
    Here it is.

    The Captain does not look at me. He is looking at the fire.
    """

    host """
    They said today, Mr Harring.

    The road was blocked. They will come as soon as it is clear.
    """

    """
    It comes out of my mouth as smoothly as it did on Saturday, and I hate the sound of it.

    The boy nods. Miss Baxter does not.
    """

    psychic """
    Then we wait for them.

    There is nothing else we can do, is there?
    """

    captain """
    We can leave.

    But not without something in our stomachs. None of us has eaten since dinner.
    """

    psychic """
    The kitchen.

    I could see what there is, if somebody will come down with me. I do not much care to go alone.
    """

    """
    I open my mouth to say I will, and close it again.

    Lady Claythorn does not go below stairs.

    I have kept to that for three days, and the habit is stronger than I am.
    """

    lad """
    I'll come.
    """

    """
    Then, from the hall, the sound of the stair, and a voice.
    """

    nurse """
    Hello?

    Is there somebody there?
    """

    """
    Miss Marsh, in the doorway, in the same dress as Saturday, and looking as though she has slept in it.
    """

    psychic """
    Miss Marsh! Good heavens, we thought...
    """

    nurse """
    I overslept.

    I am afraid I have not felt at all well, and I did not hear the gong.

    I came down and found the house empty. I have been looking for somebody for an hour.
    """

    if host_details.saved_variables["day3_morning_nurse_checked"]:

        """
        The Captain and I opened her door this morning, and her bed had not been slept in.

        I say nothing. He says nothing.
        """

    """
    She tells her story, and it is a fair performance.

    I have given worse.
    """

    nurse """
    Poor Mr Manning. What a dreadful thing.
    """

    """
    They tell her the rest, and she takes it as a nurse takes things, with her hands folded.
    """

    psychic """
    We were about to see what the kitchen has to offer. Will you help me, Miss Marsh?
    """

    nurse """
    Of course.
    """

    """
    And so they go down, the two women and the boy, and the Captain and I are left with the dead fire.
    """

    captain """
    We could still go.
    """

    host """
    I know.
    """

    """
    Neither of us moves.
    """

    call change_time(13, 00)

    call wait_screen_transition()

    """
    It is the boy who comes to fetch us, three quarters of an hour later.
    """

    lad """
    It's ready.

    It's not much, but Miss Baxter says it'll do.
    """

    call host_day3_afternoon_stay_lunch

    call host_day3_afternoon_stay_wake

    call host_day3_afternoon_stay_butler

    jump host_ending_shot_by_butler


# --------------------------------------------
#   The plates
# --------------------------------------------
label host_day3_afternoon_stay_lunch:

    $ change_room('dining_room', dissolve)

    """
    Five plates on the long table, at the same five places as on Saturday night, with the three empty chairs between them.

    Miss Marsh is alone in the room, standing at the boy's place with a plate in each hand.

    She sets one down in front of his chair as we come in, and carries the other back to her own.
    """

    nurse """
    The portions were uneven.

    Mr Harring is a growing boy, and I have no appetite to speak of.
    """

    """
    A nurse does not fuss over portions. I have watched her for three days, and she does not fuss over anything.
    """

    if host_details.threads.is_unlocked('found_poison'):

        """
        And there is a bottle missing from a shelf in the scullery, and it is in somebody's pocket.

        I look at the plate in front of the boy's chair, and I look at the one in front of hers, and I decide that I know which is which.
        """

    else:

        """
        I look at the plate in front of the boy's chair, and I look at the one in front of hers.

        She wanted his. She did not want her own.

        I decide that I know which is which.
        """

    """
    Miss Baxter comes in with the bread, and the boy behind her, and the Captain takes the chair nearest the door without being asked.

    I take my place at the head of the table.

    One last time.
    """

    """
    On Friday, in the car, the butler told me that the lady of the house could do almost anything, and that at worst she would be called eccentric.

    I have been very careful with that all weekend.

    I am going to spend the whole of it now.
    """

    host """
    Mr Harring.

    Miss Marsh has been generous with you, and I will not have a guest at my table served better than I am.

    You shall take my plate, and I shall take yours.
    """

    """
    I do not wait for an answer.

    I set my own plate in front of him, and I lift his, and it is heavy in my hands.
    """

    nurse """
    Lady Claythorn, really, there is no need...
    """

    host """
    And you, Miss Marsh, shall have back what you gave away.

    I insist. It is a poor hostess who lets a guest go without.
    """

    """
    I put the boy's plate in front of her, and I take hers for myself, and I sit down.

    Three plates, moved twice.

    Miss Marsh has gone the colour of the tablecloth, and she cannot say a word against it without saying why.
    """

    psychic """
    What a curious custom.
    """

    host """
    An old one.

    My father was very particular about it.
    """

    """
    The Captain has watched every plate go round, and he says nothing.

    He picks up his fork, and so does the boy, and so, after a moment, does Miss Marsh.

    She eats a little. She does not look at me.

    I eat.

    It is plain food, and it is not bad, and I am hungrier than I knew.
    """

    call change_time(13, 30)

    pause 1.0

    """
    She goes grey first.

    She sets her fork down very carefully, as though it might break, and she puts a hand flat on the table.
    """

    psychic """
    Miss Marsh? Are you quite all right?
    """

    nurse """
    The food.

    It was...
    """

    $ play_music('danger', fadeout_val=2)

    """
    She looks at me, and there is no anger in it, only a kind of terrible understanding.
    """

    nurse """
    You knew.
    """

    """
    Then she goes sideways out of her chair.
    """

    play sound body_fall

    """
    The boy is up. The Captain is up, with his hand in his coat.

    I stand too, to go to her, because somebody must.

    And the room goes over on its side.
    """

    """
    I have my hand on the back of my chair and I cannot feel it.

    The Captain is saying my name. Not my name. Her name.

    I got the plates right. I am certain of it. I got every one of them right.

    So why...
    """

    $ stop_music()

    scene black_background with dissolve

    pause 2.0

    """
    Nothing.
    """

    return


# --------------------------------------------
#   She wakes. Samuel Manning.
# --------------------------------------------
label host_day3_afternoon_stay_wake:

    call change_time(15, 00)

    """
    A hand on my shoulder, shaking it.

    A voice, a long way off, saying 'my lady' over and over.
    """

    $ change_room('dining_room', dissolve)

    $ play_music('scary', 2)

    """
    I open my eyes, and I am on the floor of the dining room with my cheek on the carpet and the legs of my own chair in front of my face.

    Somebody is crouched over me.

    I turn my head, and I see who it is, and I scream.
    """

    """
    Samuel Manning.

    Samuel Manning, whose throat I saw cut this morning, with his hand coming down over my mouth.
    """

    drunk """
    Quiet.

    For God's sake, woman, quiet.
    """

    """
    I bite him.

    He swears and lets go, and I get as far as the wall on my hands and knees before my legs tell me that is all they will do.

    He stays where he is, with his hand in his mouth, and he does not come after me.
    """

    drunk """
    I am not going to hurt you.

    Look at me. Look.

    I am not one of them.
    """

    host """
    You were dead.

    I saw you. Your throat...
    """

    drunk """
    Port.

    A decent one, from the billiard room. And a razor, for the edge of it. Not deep. It did not need to be.
    """

    """
    He pulls his collar down.

    Under it, a line of scab from one side of his neck to the other, shallow as a cat's scratch and black with dried wine.
    """

    drunk """
    Nobody checks a cut throat, my lady.

    That was the whole of my case.
    """

    """
    And then, because I have not looked anywhere else yet, I look.
    """

    """
    Miss Marsh is where she fell, on her side by her chair, with her eyes open.

    The Captain is across the doorway on his face, with the revolver still in his hand.

    Mr Harring is by the window, half under the curtain, as though he had tried to get behind it.

    And Miss Baxter lies across the far end of the table with her hair in the plates.
    """

    host """
    Are they...
    """

    drunk """
    All of them.

    I have looked. I did not want to.
    """

    host """
    What happened?

    What happened here?
    """

    drunk """
    I do not know.

    I was upstairs, in my bed, being dead.

    There was shouting. The Captain, and then the boy. A woman screaming, I could not say which.

    Then the shots. Three, or four. I did not count.

    Then nothing, for a very long time.

    I waited an hour after the nothing before I came down.
    """

    """
    He sits down on the floor, with his back to the sideboard, and looks at his bitten hand.
    """

    host """
    Why?

    Why would you do such a thing?
    """

    drunk """
    Because I was going to be next.

    I worked that out on Saturday, in that room, with the door locked on me and a tray coming up the back stair.

    Two men dead in two days, and both of them accidents, and the whole house nodding along.

    I have stood up in court for twenty years and watched juries nod like that.

    It is what people do when they have decided not to see something.
    """

    host """
    But to cut yourself...
    """

    drunk """
    A locked door is nothing to whoever has been walking this house at night.

    I could not get out, and I could not fight. I am not built for either.

    But I could be no longer worth the trouble.

    So I took the bottle I had put by, and I made a mess of the bed, and I lay down in it and waited for somebody to open the door and decide I was finished.

    It was the Captain who did, and I heard him tell you not to come closer.

    I could have kissed him.
    """

    $ drunk_details.description_hidden.unlock('faked_death')

    """
    I look at him.

    Samuel Manning, who could not find his own chair at dinner on Friday, sitting on the floor of this dining room stone cold sober and telling me how he outlived the whole house.

    I do not know whether to laugh or to be sick.
    """

    host """
    You were never as drunk as you let us think.
    """

    drunk """
    I was every bit as drunk as I let you think.

    I was simply not drunk the whole time.

    It is a useful thing to be thought, my lady. People stop watching you.
    """

    $ drunk_details.description_hidden.unlock('lie')

    return


# --------------------------------------------
#   The butler comes back
# --------------------------------------------
label host_day3_afternoon_stay_butler:

    """
    And then we both hear it.
    """

    play sound car_driving fadein 3

    """
    An engine on the drive, and tyres on the gravel, and then nothing.

    The engine stops.
    """

    stop sound

    $ play_music('danger', 2)

    drunk """
    That is a motor.
    """

    host """
    It is his.

    The butler. He has come back.
    """

    """
    Mr Manning is on his feet faster than a man of his years has any right to be.
    """

    drunk """
    Then I am going back to bed.

    It has served me well for a day. It can serve me a while longer.

    Come. Can you stand?
    """

    """
    I try.

    My legs are water, and the floor comes up to meet me, and I am on my knees again with the chair leg in my hand.
    """

    host """
    Go.
    """

    drunk """
    My lady...
    """

    host """
    Go. He does not know about you.

    He knows about me.
    """

    """
    He looks at me for one second longer, and then he goes, quickly and quietly, by the service door.

    I do not blame him.

    I would have gone.
    """

    play sound door_open

    """
    The front door.

    Footsteps in the hall, unhurried, the way they always were.

    He was the best butler I ever saw, and he was never a butler at all.
    """

    """
    He stops in the dining room doorway and steps over the Captain's legs, and he looks round the room the way he looked round the tea room on Saturday night.

    All of it, in one glance.

    He is out of livery. He looks like what he is.
    """

    butler """
    Well.

    You are awake.
    """

    host """
    You came back.
    """

    butler """
    I was owed a great deal of money for this weekend, and I have seen nothing of it since the advance.

    I do not think our patron will be paying now.

    So I have come to pay myself, with what the house has to offer.
    """

    host """
    The silver.

    The pearls.
    """

    butler """
    It is not what I was promised.

    It is what there is.
    """

    $ butler_details.description_hidden.unlock('took_valuables')

    host """
    And them?
    """

    """
    I do not look at the floor. He does.
    """

    butler """
    None of my doing.

    I have been on the road since eleven last night, and I have the mud to prove it.

    They did this to each other, or somebody did it for them. I was not here.
    """

    host """
    Then who?

    You said nobody was supposed to be hurt.
    """

    butler """
    Nobody was.

    I did not think it would end like this. I am not sure I was meant to think at all.
    """

    """
    He takes his hand out of his coat, and the revolver is in it, and it is pointed at the floor.

    For now.
    """

    butler """
    You told the Captain.

    I saw his face last night, on the gravel. He knew what I was, and there is only one way he could have known it.

    Who else?
    """

    host """
    Nobody.
    """

    butler """
    I should like to believe that.

    It is not enough.
    """

    host """
    Manning...
    """

    """
    It is out before I can stop it.

    His eyes go to the ceiling for a moment, and come back.
    """

    butler """
    Mr Manning is upstairs with his throat cut, where the Captain found him.

    You are not going to confuse me at this hour of the day, my lady.
    """

    """
    I do not correct him.

    It is the last thing I have to give anybody, and I give it to Samuel Manning.
    """

    butler """
    You know my face. You know my name.

    You are the only one left in this house who does.
    """

    host """
    You said nobody was supposed to get hurt.
    """

    butler """
    I am sorry.
    """

    play sound gun

    return
