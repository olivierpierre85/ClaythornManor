# --------------------------------------------
#   Nurse
#
#   Saturday - Evening
#
#   15:00 -> 23h
#
#   Music: sad
#
#   Position
#       - House: nurse, psychic, host, butler
#       - Forest: captain, doctor, drunk, lad
#       - Dead: broken
#
#   Notes :
#       - Nurse stays in the house during the hunt
#       - Witnesses the return of the hunting party
#       - Manning discussion (common text), nurse has lines in it
#       - Dinner with remaining guests
#       - Evening map, 90 minutes
# --------------------------------------------
label nurse_day2_evening:

    call change_time(15, 00, 'Evening', 'Saturday', hide_minutes=True, chapter='saturday_evening')

    $ nurse_details.add_checkpoint("nurse_day2_evening")

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("entrance_hall", irisout)

    $ play_music('sad')

    """
    I hear them before I see them.

    There is a commotion at the front door, a confusion of voices.

    Then the door swings wide and the hunting party files in.

    Something is wrong.

    Lady Claythorn's face is ashen.

    Two of the men are carrying someone between them.

    I step forward at once.
    """

    call common_day2_evening_entrance_dialog

    """
    The Captain takes charge with admirable promptness.

    I watch as Ted Harring helps carry the body up the stairs.

    I keep to one side.

    There is nothing more for me to do for Doctor Baldwin now.
    """

    call common_day2_evening_samuel_manning_discussion_part_1

    call common_day2_evening_samuel_manning_discussion_part_2

    """
    I watch the Captain lead Samuel Manning away.

    The man goes quietly, which surprises me.

    He seems to have only a dim sense of what has happened.
    """

    call common_day2_evening_samuel_manning_discussion_part_3

    $ change_room("bedroom_nurse")

    call change_time(16, 00)

    """
    I return to my room.

    I sit on the edge of the bed and press my fingers together.

    A man is dead.

    I have seen men die before, many of them, at far closer quarters than this.

    Yet there is something particular about a death in a house.

    It leaves a stillness in the air that does not belong there.
    """

    if nurse_details.threads.is_unlocked('captain_zanzibar'):

        """
        I think of the Captain and what I found in the library.

        His account of his wound at Zanzibar seemed improbable to me from the start.

        After today, I am no longer sure what to make of him.

        He acted with authority and presence of mind.

        But that, in itself, proves nothing.
        """

    """
    I decide I should rest before dinner.
    """

    call wait_screen_transition()

    call change_time(18, 30)

    play sound dinner_gong

    """
    The gong sounds.

    I would prefer to stay in my room, but that would raise questions.
    """

    $ change_room("dining_room", irisout)

    $ play_music('sad', 3)

    """
    The dining room is noticeably quieter than it was last night.

    Three chairs sit empty.

    I take my usual place and look around the table.

    But I realise that I have no one in front of me, nor to my side.

    Lady Claythorn observes my awkward position.
    """

    host """
    I think it's better if you come sit next to me tonight.

    No reason to leave you alone at the end of the table.
    """

    nurse """
    Thank you.
    """

    """
    Everyone is subdued.

    Lady Claythorn stands.
    """

    call common_day2_evening_dinner_host

    """
    A measured speech.

    She holds herself well.

    I find myself wondering what she is actually feeling beneath that composed exterior.

    Now that she is sitting to my right, I have the opportunity to question her.
    """

    $ time_left = 90
    call run_menu(TimedMenu("nurse_day2_evening_dinner", [
        TimedMenuChoice("Speak to Lady Claythorn", 'nurse_day2_dinner_host'),
        TimedMenuChoice("Say nothing, eat your dinner", 'generic_cancel', early_exit=True),
    ], image_right = "host"))

    call change_time(21, 00)

    """
    Dinner ends.

    Very few words were exchanged.

    The butler sees the guests out of the room with quiet efficiency.

    Most of the others drift away towards their rooms.

    Before they all leave, my eyes settle on the silverware scattered about the table.

    It would be so easy to slide a piece into my bag undetected.

    The others are distracted by the evening's events.
    """


    $ time_left = 1 
    call run_menu(TimedMenu("nurse_day2_evening_steal", [
        TimedMenuChoice("Pocket some silverware discretely", 'nurse_day2_evening_steal', early_exit=True),
        TimedMenuChoice("It is not worth the risk", 'nurse_day2_evening_do_not_steal', early_exit=True),
    ]))

    $ change_room("bedroom_nurse", dissolve)

    """
    I do not feel ready to sleep just yet.

    The manor is quiet, but that is not the same as saying it is safe.

    Perhaps I ought to make a brief exploration before I retire.
    """

    $ time_left = 90
    call run_menu(nurse_details.saved_variables["day2_evening_map_menu"])

    call change_time(22, 00)

    if time_left <= 0:

        if nurse_details.threads.is_unlocked('day1_exhaustion'):

            call nurse_day2_exhaution

        else:

            play sound woman_cough

            """
            A cough catches me in the corridor.

            I stop and press a hand against the wall until it passes.

            When it does, I become suddenly aware of how late it must be.

            I have been wandering this house for the better part of an hour.

            That was not wise of me.

            There are some indulgences I cannot afford, and pushing myself through the small hours of the night is one of them.

            I shall not press my luck further tonight.
            """

    """
    It is time to sleep.

    I return to my room and lock the door behind me.

    It has been a long day.

    I need to rest.
    """

    $ stop_music()

    jump nurse_day3_morning


label nurse_day2_dinner_host:

    nurse """
    It has been a dreadful day, has it not, Lady Claythorn?

    To lose such a man as Doctor Baldwin in such a manner...
    """

    host """
    It is indeed a tragedy.
    """

    nurse """
    And poor Mr Manning.

    One can only hope the authorities arrive soon to settle this matter.
    """

    host """
    Indeed.
    
    But please, let us not dwell on such dark matters while we eat, my dear.
    """

    nurse """
    Of course.
    """

    call host_generic

    return


label nurse_day2_exhaution:

    $ play_music('mysterious', 3)

    play sound woman_cough

    """
    A cough takes me without warning.

    Harder than the ones before.

    I press my handkerchief to my lips.
    """

    play sound woman_cough

    """
    A second.

    My knees feel uncertain beneath me.

    I find the wall and lean against it.
    """

    play sound woman_cough

    """
    A third, and I cannot check it.

    I sink down.

    The handkerchief, when I pull it away, tells me everything I already knew.

    The walls are very cold.

    I cannot seem to rise.
    """

    jump nurse_ending_exhausted


label nurse_day2_evening_steal:

    """
    A quick glance to either side.

    The others are moving towards the door, their backs turned.

    My hand moves, sliding a silver spoon into my bag with the faintest clink.
    """

    if nurse_details.threads.is_unlocked('steal_cutlery_1') and nurse_details.threads.is_unlocked('steal_cutlery_2'):

        call nurse_day2_evening_steal_caught

    else:

        """
        Nobody seems to notice.
        """

    return


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
    Given the circumstances of this weekend, I am inclined to think there might be more to this than simple pilfering.
    """

    host """
    Whatever do you mean, Captain?
    """

    captain """
    I mean that Miss Marsh might not be who she claims to be.
    """

    nurse """
    What? No, that is ridiculous!

    It is a misunderstanding!
    """

    captain """
    So you continue to say.

    But you must admit, it is rather difficult to take you at your word just now.
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

    We shall confine her to her room, just as we did with Mr Manning.

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
    Sorry Miss Marsh, but I don't have a choice.
    """

    """
    They believe I am trapped here.
    
    But they underestimate me.
    
    A hairpin and a steady hand are all I require to open such a simple lock.
    
    I shall wait until the house is completely silent, and then I will take my leave.
    
    It is far from ideal, but it is my only chance.
    """

    call black_screen_transition()

    call change_time(23, 30)

    $ change_room("bedrooms_hallway")

    """
    I slip out into the hallway undetected.

    Nobody is there.
    """

    $ change_room("entrance_hall")

    """
    I reach the entrance hall, then quickly make my way outside.
    """

    # TODO finish from here
    
    """
    The road ahead is long, and the air is bitterly cold.
    """

    if nurse_details.threads.is_unlocked('day1_exhaustion'):

        """
        I push myself forward, intending to walk all the way to the village.
        """

        jump nurse_day2_exhaution

    else:

        """
        I walk through the night until my feet are raw, pushing myself onward until the first light of dawn breaks over the village.

        I have escaped with my life.

        But I am entirely alone, shivering in the morning chill.

        I have no money, no position, and I am no better off than when I first arrived at Claythorn Manor.
        
        Still, I have my freedom. And for now, that must suffice.
        """

        jump nurse_ending_escaped_alone


label nurse_day2_evening_do_not_steal:

    """
    I look at the silverware for a moment longer than I ought.

    Then I push the thought aside.

    It is not worth the risk.
    """

    return
