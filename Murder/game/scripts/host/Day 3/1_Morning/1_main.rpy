# --------------------------------------------
#   Host
#
#   Sunday - Morning
#
#   08:00 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - Bedroom Host : host, captain (he sat up in her room all night)
#       - House        : lad, psychic, nurse (Miss Marsh keeps out of sight)
#       - Confined     : drunk, locked in his room
#       - Dead         : broken (Thomas Moody), doctor (Daniel Baldwin)
#       - Gone         : butler and the rest of the staff, in the car since eleven
#
#   Notes :
#       - Only reachable through the 'trust_captain' branch of Saturday night.
#         Every other Saturday evening path ends in a death.
#       - She wakes to find the Captain asleep in his chair. They agree to
#         leave, but to prepare first, and they go through the house together.
#       - The morning map (0_map_choices.rpy) is where the three things they
#         need are found: the car (seen_car), the petrol (petrol_tin) and the
#         food (provisions). Mr Manning's door can be opened there as well
#         (day3_morning_manning_checked). If it is not, the Captain opens it
#         at noon before anything is decided (host_day3_afternoon).
#       - Ted Harring and Amelia Baxter are walking the house all morning.
#         They are heard and avoided, never met.
# --------------------------------------------
label host_day3_morning:

    call change_time(8, 00, 'Morning', 'Sunday', hide_minutes = True, chapter = 'sunday_morning')

    $ host_details.add_checkpoint("host_day3_morning")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('bedroom_host', irisout)

    $ play_music('mysterious', 2)

    call host_day3_morning_wake

    call change_time(9, 30)

    $ time_left = 150

    call run_menu(host_details.saved_variables["day3_morning_map_menu"])

    if time_left <= 0:

        $ change_room('entrance_hall', dissolve)

        """
        We have been through the house for the better part of the morning.

        The Captain looks at his watch, and we go back to the hall.

        There is no time left for anything else.
        """

    call change_time(12, 00)

    $ stop_music()

    jump host_day3_afternoon


# ------------------------------------
#   Waking with the Captain
# ------------------------------------
label host_day3_morning_wake:

    """
    I wake in my clothes, with the light already coming through the curtains.

    For a moment I do not know where I am.

    Then I see him.

    Captain Sinha is in the chair by the door, exactly where he said he would be.

    His chin is on his chest, the revolver lies in his lap, and he is fast asleep.

    So much for the watch.
    """

    """
    I do not wake him at once.

    I lie still and listen to the house instead.

    No footsteps below. No fires being laid. No trays.

    On Friday, at this hour, the girl was already at the range and the footman was polishing the brass in the hall.

    They are miles away by now, and I am the only member of staff left at Claythorn Manor.

    It is an odd thought.

    For the first time since I stepped down from the train, nobody expects me to be anybody at all.
    """

    """
    I sit up, and the bed creaks, and the Captain is on his feet before I have finished the movement.
    """

    captain """
    Forgive me.

    I closed my eyes for a moment.
    """

    host """
    It was rather more than a moment, Captain.

    It is morning.
    """

    captain """
    So it is.
    """

    """
    He puts the revolver back into his pocket without looking at it, and he straightens his coat.

    He is embarrassed, and I find I do not mind in the least.

    Nobody came to my door in the night.

    That is all that matters.
    """

    host """
    Well, Captain.

    It is daylight, as you said.

    What do we do now?
    """

    captain """
    We leave.

    That has not changed since last night.

    The question is how.
    """

    host """
    The town is a long way.

    We came up from the station on Friday, and it took the car the better part of an hour.
    """

    captain """
    Ten miles, then. Perhaps more.

    On foot, and on that road, it is the whole of the afternoon.

    We could do it. I would rather not.
    """

    host """
    There is a car.
    """

    """
    He looks at me.
    """

    host """
    Not the one we came up in. That one is gone.

    There is an old tourer in the garage. It was here when we arrived.

    I have looked at it twice this weekend and thought it would never start.

    But I am no judge of motors.
    """

    captain """
    I am.

    If the engine is sound, it will want petrol, and the chauffeur will not have left any lying about.
    """

    host """
    There is a shed at the bottom of the garden.

    The butler kept it locked all weekend, and I never asked him why.
    """

    captain """
    Then I shall ask the master key.
    """

    """
    He pats his waistcoat pocket, where the key has been since Saturday afternoon.
    """

    captain """
    Something to eat, as well.

    Nothing will be served in this house today, and nothing has been since dinner.

    If the car fails us on the road, we finish on foot, and I would rather not do that hungry.
    """

    host """
    The kitchen, then.

    And there is Mr Manning.
    """

    captain """
    Yes.

    I locked that door myself. I shall open it before we go, whatever else we do.
    """

    host """
    And the other three?
    """

    captain """
    We agreed last night.

    We say nothing to anybody until we are out of this house.

    If one of them is behind this, I do not want to see their face when they learn what we know.
    """

    host """
    Then we keep away from them.
    """

    captain """
    As long as we can.

    And we do not separate. I am not letting you out of my sight this morning.
    """

    host """
    I was going to insist on it.
    """

    """
    So that is the plan.

    A car, petrol, food, and a locked door to open.

    Two hours, perhaps a little more, before the others come looking for us.

    I put my shoes on, and we go out into the corridor together.
    """

    $ change_room('bedrooms_hallway', dissolve)

    """
    The doors are all shut.

    Nothing moves.

    We go down.
    """

    return
