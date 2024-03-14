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
    TODO
    """

    jump work_in_progress
