# --------------------------------------------
#   Psychic
#           
#   Sunday - Morning
# 
#   7:30 / 9:30 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic
#       - Dead : broken, doctor, drunk
#       -? : Host, nurse
#
#   Notes : 
#       - ???
# --------------------------------------------
label psychic_day3_morning:

    $ psychic_details.add_checkpoint("psychic_day3_morning") 

    call black_screen_transition("Amelia Baxter", "Sunday Morning")

    call change_time(7, 0, "Morning", "Sunday", hide_minutes=True)

    $ change_room('psychic_room', irisout)

    """
    I slept terribly last night.

    No wonder why.

    Well, it's the last day at least. It'll be over soon.

    Now I need to get my things ready and head to Ted Harring.
    """

    $ change_room('bedrooms_hallway', dissolve)

    play sound door_knock

    """
    He is not responding.

    I hope he is well.
    """

    play sound door_knock

    psychic """
    Mr Harring, are you there?
    """

    call common_day3_morning_lad_psychic_journey

    """
    And we started to look for others in the manor,

    inspecting every room.

    I let him choose where we were going,

    even though his choices didn't always make much sense.
    """

    $ change_room('tea_room', irisout)

    call change_time(11,00)

    """
    After a long search, we took a break in the tea room.

    We rested there until we heard a familiar voice.
    """

    call common_day3_morning_lad_psychic_tea_room_1

    call common_day3_morning_lad_psychic_tea_room_2

    call common_day3_morning_lad_psychic_captain_death_manning

    """
    I sat there quietly, pondering what had happened, what I should do next.
    """

    pause 1.0

    """
    After some time, they came back.
    """

    call common_day3_morning_lad_psychic_captain_deaths_end

    pause 1.0

    $ stop_music()

    jump psychic_day3_afternoon
