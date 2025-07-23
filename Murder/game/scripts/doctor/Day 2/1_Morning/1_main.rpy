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
    "Awake and alive."

    Why am I thinking that?
    
    That's a weird way to start the day.
    """

    jump work_in_progress
