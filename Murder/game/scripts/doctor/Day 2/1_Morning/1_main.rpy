# --------------------------------------------
#   Doctor
#           
#   Saturday - Morning
#   
#   08:30 -> 11:00
#
#   Music: chill
#
#   Alive: Everyone but Broken
#
#   Notes : 
#       - Generic Lad ?
# --------------------------------------------
label doctor_day2_morning:

    call change_time(8, 30, 'Morning', 'Saturday', hide_minutes=True, chapter='saturday_morning')

    $ current_character.add_checkpoint("doctor_day2_morning")

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ change_room("bedroom_doctor", irisout)

    """
    Awake and alive.
    Why am I thinking that?
    That is a peculiar way to commence the day.
    """

    lad """
    Hello Doctor Baldwin.
    Did you sleep well?
    """

    doctor """
    I did, thank you. I find the morning agreeable.
    """

    jump work_in_progress
