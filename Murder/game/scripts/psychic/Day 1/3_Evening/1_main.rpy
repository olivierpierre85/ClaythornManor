# --------------------------------------------
#               Amelia Baxter
#           Friday 21:00 Evening
#   Playtime : about 10 min from start
#
#   Alive: Everyone
label psychic_day1_evening:

    $ lad_details.add_checkpoint("psychic_day1_evening") 

    call change_time(21,00, 'Evening', 'Friday')

    $ change_room('psychic_room')

    """
    Well, I am comfortably settled.

    What should I do now?
    """

    $ play_music('upbeat')

    $ time_left = 120
    call run_menu(psychic_details.saved_variables["map_menu"])

    call change_time(23,00)

    stop music fadeout 5.0

    """
    It's been a long day.

    I can't stay up any longer.

    It's time to go to bed.
    """

    $ change_room('psychic_room')

    

    jump psychic_day2_morning
        


