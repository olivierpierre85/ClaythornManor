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
#       - Whether she knows about the old tourer depends on 'saw_car', set by
#         a garage visit on the Friday or Saturday evening. If she does, she
#         brings it up herself. If not, the Captain asks and the garage goes
#         on the list as a place to look.
#       - The morning map (0_map_choices.rpy) is where the three things they
#         need are found: the car (car_checked), the petrol (petrol_tin) and
#         the food (provisions). Mr Manning's door can be opened there as well
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

    """
    I wake in my clothes, with the light already coming through the curtains.

    The house is eerly quiet.

    No footsteps below. No fires being laid. No trays.

    For a brief moment that seems odd to me, then I remember.

    The staff is gone, we are on our own.

    Captain Sinha is in the chair by the door.

    His chin is on his chest, the revolver lies in his lap, and he is fast asleep.

    So much for the watch.

    I stand up, and the noise wakes him up.
    """

    captain """
    Forgive me.

    I closed my eyes for a moment.
    """

    """
    He puts the revolver back into his pocket without looking at it, and he straightens his coat.
    """

    host """
    Do not worry.

    Nobody came to my door in the night.

    That is all that matters.
    """

    captain """
    Right.

    Well, I guess now there is daylight, we can leave.

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

    We could do it, though it is not ideal.
    """

    if host_details.threads.is_unlocked('saw_car'):

        host """
        There is an old tourer in the garage. 
        
        But  I have no idea if it is still working.

        I know nothing about motors.
        """

        captain """
        I know a little.
        
        We could check it then, see if we can start it.
        """

    else:

        captain """
        It would be easier if we had a car.

        Do you know if there is another one on the estate?
        """

        host """
        I am not sure.
        """

        captain """
        Well, it is worth looking for one then.
        """


    host """
    Another thing.

    What shall we do about Mr Manning?
    """

    captain """
    Right.

    I locked him up in his room last night.

    It would not be fair to let him in there.
    
    We should at least open his door before we go.
    """

    host """
    Alright, so we can sort those things out before deciding on our next move.
    """

    captain """
    Ver well.

    One more note, we shouldn't say anything to anybody until we are out of this house.

    If one of them is behind this, I do not want to see their face when they learn what we know.
    """

    host """
    Then we keep away from them.
    """

    captain """
    As long as we can.
    """

    """
    So that is the plan.

    A few things to check and then we are out of here.

    I put my shoes on, and we go out into the corridor together.
    """

    $ change_room('bedrooms_hallway', dissolve)

    """
    The doors are all shut.

    Nothing moves.
    """

    captain """
    Please, lead the way.
    """

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