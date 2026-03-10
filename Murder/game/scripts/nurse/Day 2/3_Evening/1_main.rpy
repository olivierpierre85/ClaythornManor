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
        TimedMenuChoice("Pocket some silverware discretely", 'nurse_day2_evening_steal_caught', early_exit=True),
        TimedMenuChoice("It is not worth the risk", 'nurse_day2_evening_do_not_steal', early_exit=True),
    ]))

    """
    I do not feel ready to sleep just yet.

    The manor is quiet, but that is not the same as saying it is safe.

    Perhaps I ought to make a brief survey before I retire.
    """

    $ time_left = 90
    call run_menu(nurse_details.saved_variables["day2_evening_map_menu"])

    call change_time(22, 00)

    if time_left <= 0:

        if nurse_details.threads.is_unlocked('day1_exhaustion'):

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

        else:

            play sound woman_cough

            """
            A cough catches me in the corridor.

            I stop and press a hand against the wall until it passes.
            """

            """
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

    I need tto rest.
    """

    $ stop_music()

    jump work_in_progress


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


label nurse_day2_evening_steal_caught:

    """
    A quick glance to either side.

    No one seems to be paying the slightest attention.

    My hand moves to slide a silver spoon into my bag with the faintest clink.
    """

    host """
    Miss Marsh. What exactly do you think you are doing?
    """

    """
    I freeze.

    Lady Claythorn is standing by the doorway, her eyes fixed upon my bag.
    """

    nurse """
    I... I am just gathering my things, Lady Claythorn.
    """

    host """
    Do not insult my intelligence.

    Empty your bag at once.
    """

    """
    My face burns as I slowly reach inside and pull out the silver spoon.

    I place it on the table.
    """

    host """
    I had my suspicions.

    But to see it with my own eyes... It is beyond belief.
    """

    nurse """
    Lady Claythorn, please, I can explain...

    I was only admiring the craftsmanship. I had no intention of keeping it.
    """

    host """
    Do you take me for a fool?

    We have a dead man in the house, and you use the opportunity to pilfer my silver.
    """

    lad """
    Blimey, right out of the dining room! Who'd have thought it of a nurse?
    """

    psychic """
    I sensed a darkness in her aura the moment she arrived. A shadow of deceit.
    """

    nurse """
    That is not true! I am a respectable professional. I have served in hospitals across the country.

    This is all a terrible misunderstanding!
    """

    captain """
    Professional or not, Miss Marsh, the evidence is rather plainly on the table.

    Given the circumstances, Lady Claythorn is entirely justified in her concern.
    """

    host """
    Indeed. You will confine yourself to your room immediately.

    And I shall lock the door to ensure you stay there.

    Tomorrow, we shall see what the police have to say about this.
    """

    captain """
    Allow me to escort her upstairs, Lady Claythorn. Just to be absolutely certain there is no further... trouble.
    """

    host """
    Thank you, Captain. See to it that she is securely locked in.
    """

    """
    I try to muster some dignity, but with all their eyes upon me, there is none to be had.

    I follow the Captain upstairs with my head bowed.

    He walks closely behind me the whole way, ensuring I do not stray.
    """

    $ change_room("bedroom_nurse", dissolve)

    """
    When I reach my room, I step inside.

    The door closes firmly behind me, followed by the definitive click of a key turning in the lock.
    """

    call change_time(22, 00)
    
    """
    I am trapped here now.

    There is nothing left to do tonight but sleep.
    """

    $ stop_music()

    jump work_in_progress


label nurse_day2_evening_do_not_steal:

    """
    I look at the silverware for a moment longer than I ought.

    Then I push the thought aside.

    It is not worth the risk.
    """

    return
