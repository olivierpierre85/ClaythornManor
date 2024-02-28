# --------------------------------------------
#   Psychic
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
label psychic_day2_morning:

    $ current_character.add_checkpoint("psychic_day2_morning")

    call black_screen_transition("Amelia Baxter", "Saturday")

    scene psychic_room with irisout

    $ change_room('psychic_room')

    call change_time(8, 30, 'Morning', 'Saturday', hide_minutes=True)

    """
    Despite the storm that raged all night, I managed to sleep relatively well.

    So, I take my time getting ready and then head downstairs to the dining room.
    """

    $ change_room('dining_room')

    call change_time(9, 20)

    """
    Some of the guests are already eating.

    I grab a plate at the breakfast buffet and then sit down at the same spot on the table as yesterday.

    Captain Sinha is there, but I don't feel like engaging in conversation with him.

    It's too soon for that.

    After a while, Ted Harring joins me at the table.
    """

    call change_time(9, 30)

    call common_day2_morning_lad_psychic

    """
    For some reason, Ted Harring also stands up and follows them.

    It seems I am stuck with Sushil Sinha.
    """

    psychic """
    Good morning, Mister Sinha.
    """

    captain """
    Miss Baxter.
    """

    $ time_left = 30

    call captain_generic

    call change_time(10, 00)

    call common_day2_morning_host_death

    call common_day2_morning_host_death_doctor

    $ stop_music()

    call common_day2_morning_host_hunt

    """
    That's impressive.

    People seem eager to move on really quickly.

    Well, let them enjoy their game.

    Obviously, I'll stay here this afternoon.
    """
    
    jump psychic_day2_no_hunt


    