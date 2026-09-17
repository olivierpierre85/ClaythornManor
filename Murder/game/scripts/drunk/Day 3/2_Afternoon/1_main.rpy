# --------------------------------------------
#   Drunk
#
#   Sunday - Afternoon
#
#   12:00 -> Ending
#
#   Music: mysterious, danger for the table, scary for the butler
#
#   Position
#       - Service passage : drunk, hidden
#       - Kitchen / Dining Room : lad, psychic, nurse
#       - Dead : broken, doctor
#       - Gone, then back : butler
#
#   Notes :
#       - He is a dead man loose in a house of three living ones. He gets
#         down the servant stair and into the passage behind the dining
#         room, and he watches the last act of the weekend through the
#         serving hatch.
#       - The plates, from day3_poisoning_chart.md: the nurse's place is
#         poisoned, the boy's is sedated, Miss Baxter's is clean. Miss Marsh,
#         paranoid, swaps her plate with the boy's - which would put the
#         poison in front of the boy. Manning, who has understood everything,
#         can slip in and put them back (swapped_back), so the poison returns
#         to the woman it was meant for and the boy only sleeps.
#       - Swap them back, and the boy lives, and Manning has the wit to be
#         gone before the butler's car returns (survived), witnessing the
#         butler greet the waking boy on his way out.
#       - Do nothing, and the boy dies, and Manning stays frozen at the
#         hatch to watch it, and the returning butler checks the bed the
#         Captain did not (found_out).
#       - He recognises Miss Baxter at the end either way: she is the client
#         he was too drunk to defend, years ago (lost_case). That is why he
#         was on the list.
#
#   Unlocks : drunk 'swapped_back', 'lost_case'
#             butler 'manages_weekend', 'job', 'mob', 'took_valuables'
#                    (survived only)
# --------------------------------------------
label drunk_day3_afternoon:

    call change_time(12, 00, 'Afternoon', 'Sunday', hide_minutes = True, chapter = 'sunday_afternoon')

    $ drunk_details.add_checkpoint("drunk_day3_afternoon")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ change_room('basement_stairs', irisout)

    $ play_music('mysterious', 2)

    """
    Down the drainpipe and along the scullery roof and in at a pantry window, the way I have not moved in forty years, and my knees will have something to say about it tomorrow, if there is a tomorrow.

    The below-stairs of Claythorn Manor is empty. No cook, no maid, no footman. The staff have gone, and I know now they were never staff at all.

    There is a passage behind the dining room, where the plates go in and the empties come out, with a hatch in the wall the width of a serving dish.

    I fold myself into it, and I put my eye to the crack of the hatch, and I wait for the last act.
    """

    call change_time(12, 45)

    """
    They come down together. The boy, the hat, the thin woman who is not dead.

    So the thin woman lied about something to somebody, but then everyone in this house has, myself the most of all.

    They have made a luncheon of what the kitchen had. The boy carries the plates in and sets them at their places, three of them, at the near end of the long table with all its empty chairs.

    Then he says he has something he must do alone, and the hat says she has the same, and the two of them go up, and the thin woman is left to lay the last of the table.

    Alone.
    """

    $ play_music('danger', 3)

    """
    The moment they are gone, she moves.

    Quick, and sure, and not at all the frightened invalid she has played all weekend. She takes up her own plate and the boy's, one in each hand, and she sets her own down at his place, and his down at hers.

    She swaps them.

    A nurse does not fuss over which plate is which. A nurse who swaps her dinner with a strong young man's is a nurse who is afraid of her own dinner.

    She is afraid of the food. She has been afraid of it since she sat down, and she is right to be, and she has just moved whatever is in it in front of that boy.
    """

    """
    And I understand it whole, from the hatch, the way I understood the rest of it in the locked room.

    Somebody meant the poison for her. She has smelt it, or guessed it, and passed it to the boy, and gone back to eating like a woman who has saved her own life.

    In a minute the boy will come down and eat what was meant for her, and die of it, and she will live.

    Unless a dead man does something about it.
    """

    """
    She sets the last fork straight and goes out to the kitchen for the bread.

    The room is empty. The plates are on the table. The hatch is at my shoulder.

    I have perhaps a minute.
    """

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day3_afternoon_menu_plates", [
        TimedMenuChoice('Slip in and put the plates back where they were', 'drunk_day3_afternoon_swap', early_exit=True),
        TimedMenuChoice('Stay in the hatch. It is not your business. It never was', 'drunk_day3_afternoon_watch', early_exit=True),
    ]))

    return


# ------------------------------------
#   He puts them back. -> swapped_back, the boy lives
# ------------------------------------
label drunk_day3_afternoon_swap:

    $ drunk_details.threads.unlock('swapped_back')

    $ change_room('dining_room')

    """
    Fifty-five years old, dead since last night, and I come out of a serving hatch like a stagehand between the acts.

    The boy's plate to the boy's place. The thin woman's plate back to the thin woman's place. Exactly as they were laid.

    I have moved evidence before, God forgive me, in courtrooms, for money. This is the first time I have moved it to save a life instead of end one.

    My hands do not shake at all.

    Then I am back in the wall, with the hatch drawn to, and the port stiff on my collar, and my heart going like a boy's, before the kitchen door has even opened.
    """

    call change_time(13, 15)

    """
    They come back. The boy, then the hat, and the thin woman with the bread.

    They sit at their proper places, in front of their proper plates, and they eat in the silence of people with nothing left to say to one another.

    The thin woman eats a little. She does not know she is eating what she was so careful to give away.

    The boy eats like a boy.
    """

    call change_time(13, 30)

    pause 1.0

    $ play_music('danger', fadeout_val=2)

    """
    It is the thin woman who goes first.

    She sets her fork down very carefully, and puts a flat hand on the cloth, and goes the colour of it.
    """

    nurse """
    The food.

    It was...
    """

    play sound body_fall

    """
    She goes sideways out of her chair, and she does not get up.

    The hat is on her feet. The boy is on his, swaying, a hand to his own head.
    """

    lad """
    I feel... something is wrong. I feel...
    """

    """
    And then the boy folds up too, gently, almost slowly, and lies down on the floor of the dining room as though he has decided to sleep there.

    But he is breathing.

    From the hatch, in the dark, I watch his chest go up and down, and up, and down, and I could weep.

    Sleeping. Only sleeping. Whatever was in that plate meant to send a man to sleep, and it has, and it will wear off, and he will wake.

    I have never in my life been paid to do a thing as well as I have just done this thing for nothing.
    """

    call drunk_day3_afternoon_recognition

    call drunk_day3_afternoon_butler_returns

    jump drunk_ending_survived


# ------------------------------------
#   He does nothing. -> the boy dies
# ------------------------------------
label drunk_day3_afternoon_watch:

    """
    No.

    It is not my business. It never was. I am a dead man in a wall, and dead men do not reach out of the dark and rearrange the world.

    That is what I tell myself, and it is what I have told myself at every hatch I have ever stood behind, and the words are as thin now as they have always been.

    I stay where I am.
    """

    call change_time(13, 15)

    """
    They come back and they sit and they eat.

    The boy eats what the thin woman put in front of him. What was meant for her.
    """

    call change_time(13, 30)

    pause 1.0

    $ play_music('danger', fadeout_val=2)

    """
    He is the one who goes.

    He stands up to help with the plates, like the decent boy he is, and the room takes him, and he goes down.
    """

    play sound body_fall

    lad """
    What's happening? Why am I...
    """

    """
    The thin woman is at his side, her hands doing their old trained work, and then they stop.
    """

    nurse """
    He has no pulse.

    He's dead.
    """

    """
    Dead.

    I had a minute, and a serving hatch, and a whole life of standing behind them doing nothing, and I did the thing I have always done.

    He is on the floor a yard from me with the sleep he was never given, and I gave him the poison instead, by holding still.
    """

    $ stop_music()

    call drunk_day3_afternoon_recognition

    call drunk_day3_afternoon_butler_returns_found

    jump drunk_ending_found_out


# ------------------------------------
#   He recognises Miss Baxter. -> lost_case
# ------------------------------------
label drunk_day3_afternoon_recognition:

    $ play_music('sad', 2)

    """
    The hat is on the floor now beside the boy, and she has him gathered up against her, and she is making a sound I have heard before, in cells, and in the corridors outside courtrooms, from women who have lost everything the law was supposed to keep for them.

    And in the making of that sound her face comes apart, and the powder cracks at the eyes, and under the eccentric hat and the séance manner there is a face I know.

    I know it.

    Not from this weekend. From years back, from the north, from the worst season of my whole disgraceful practice.

    A woman in the dock, plainer then, and younger, up for breaking into a place she should not have been. An orphanage, of all things. She would not say why, only that she had to know something that was kept there.

    And they gave her Samuel Manning, because Samuel Manning was cheap and could be had at short notice and no better man would take a case with no fee in it.

    And Samuel Manning came to court with the smell of last night on him and lost it in an afternoon, and she was sent down, and she looked at me across that court exactly as she is not looking at me now, because she does not know I am here.

    She remembered me. Of course she remembered me.

    That is why I am on the list. Not for Eleanor. Eleanor was the bait. I am on the list because I failed this woman, years ago, when she needed me, and she has waited all this time to gather up everyone who failed her in one house and watch them destroy each other.

    And the boy she is holding.

    The boy she counted the fingers of, at dinner, the first night.

    Oh.

    Oh, you poor woman. That is what was kept at the orphanage.
    """

    $ drunk_details.description_hidden.unlock('lost_case')

    return


# ------------------------------------
#   The butler returns, and Manning has the wit to be gone. (survived)
# ------------------------------------
label drunk_day3_afternoon_butler_returns:

    """
    Then, from the drive, an engine.
    """

    play sound car_driving fadein 3

    $ play_music('scary', 2)

    """
    A motor on the gravel, and it stops, and the engine dies.

    His.

    I know the sound of it. I sat in front of it, drunk, all the way from the station, a hundred years ago on Friday.

    He has come back for something. Men like that always come back for something.
    """

    stop sound

    play sound door_open

    """
    The front door, and feet in the hall, unhurried, the way they always were.

    I draw back off the hatch into the dark of the passage, and I make myself smaller than a man my age has any right to be.

    Through the crack I watch him come into the dining room and stand over it all, and take it in with one glance, the way he took in the tea room on Saturday night.

    He is out of his livery. He looks like what he is now, and what he is, is the man I saw walk out of a dock in the north a dozen years ago.
    """

    """
    He goes to the sideboard, and to the cabinet in the hall, and I hear the chime of silver going into a bag, unhurried, a man collecting a debt.

    He was promised money for this weekend, and he has not been paid, and he is paying himself out of the house.
    """

    $ butler_details.description_hidden.unlock('manages_weekend')
    $ butler_details.description_hidden.unlock('job')
    $ butler_details.description_hidden.unlock('mob')
    $ butler_details.description_hidden.unlock('took_valuables')

    """
    And then the boy on the floor stirs.

    A hand first, and then a knee, the sleep letting go of him exactly as I knew it would.

    The butler hears it. He crosses the room and crouches by the boy, and the bag of silver settles against his leg, and he looks into the boy's face with something on his own that is almost gentle.
    """

    butler """
    Hello, Mr Harring.

    How are you feeling?
    """

    """
    The boy does not answer. He is not properly back yet.

    And I understand, from the wall, that whatever this whole weekend was, this is what it was for. This man, and this boy, and the woman weeping between them.

    There is a whole other story in this house, and it is ending now, in front of me, and I am the only living soul who will ever have seen it.

    If I stay to see the end of it, I will be the only living soul in this house who did, and he will not allow that.

    I have watched enough. It is the one thing I have always been good at.

    Now, for once, I am going to do the other thing. I am going to leave before the ending finds me.
    """

    $ change_room('basement_stairs', dissolve)

    """
    Back along the passage, out at the pantry window, over the scullery roof and down.

    An old drunk, going out of a house by a window, with a dead man's blood dried on his collar and a boy's sleeping face behind him, alive.

    I do not look back.

    A road is a dangerous thing, when the people you are running from use it. So I do not take the road.

    I take the woods, the way a poacher would, and I have all afternoon, and I am, against every expectation of the last thirty years, in no hurry at all to have a drink.
    """

    return


# ------------------------------------
#   The butler returns, and Manning is still at the hatch. (found_out)
# ------------------------------------
label drunk_day3_afternoon_butler_returns_found:

    """
    Then, from the drive, an engine.
    """

    play sound car_driving fadein 3

    $ play_music('scary', 2)

    """
    A motor on the gravel. It stops. His.

    I know the sound of it, and I do not move, because I cannot. I am fixed to the hatch, watching the hat weep over the boy she killed by trusting the wrong plate, and I cannot make myself let go of the sight of it.

    That has always been my trouble. I can watch anything. I cannot leave.
    """

    stop sound

    play sound door_open

    """
    He comes in unhurried, out of his livery, and he takes it all in with one glance, and he does not weep and he does not blink.

    He is a careful man. He was always the careful one.

    And a careful man, before he leaves a house full of the dead, goes up to be sure they are all where he left them.
    """

    call change_time(15, 00)

    $ change_room('bedrooms_hallway', dissolve)

    """
    I hear him on the stair. I hear the key in my own door, the door that was locked on a dead man.

    I hear the door open on an empty bed, with the port dried into the shape of a man who is no longer in it.

    The Captain saw a cut throat and did not come close. The butler comes close. The butler puts his hand flat on the cold sheet, and finds it cold the wrong way, and understands in one second what took me a whole locked night to think of.

    Then his feet come back to the stair. Unhurried.

    Looking for the dead man who got up.
    """

    $ butler_details.description_hidden.unlock('manages_weekend')

    """
    I am below, in the passage, with nowhere left to be small.

    I could have been in the woods an hour ago.

    I stayed to watch. I always stay to watch.
    """

    return
