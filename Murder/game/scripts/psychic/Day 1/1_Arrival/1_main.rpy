# --------------------------------------------
#               Ted Harring
#           Friday 17:30 Arrival
#
#   Alive: Everyone
label psychic_day1_arrival:

    $ psychic_details.add_checkpoint("psychic_day1_arrival") 
    
    call black_screen_transition("Amalia Baxter", "Friday")

    $ change_room('great_hall', irisout)
    
    call change_time(17,30, 'Arrival', 'Friday')

    $ play_music('upbeat')

    butler """
    Good afternoon Sir.
    """