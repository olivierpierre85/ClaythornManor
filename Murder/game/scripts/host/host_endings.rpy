# --------------------------------------------
#   Host endings
# --------------------------------------------

label host_ending_shot_tea_room:

    $ host_details.endings.unlock('shot_tea_room')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('shot_tea_room'))

    call death_screen_transition

    """
    Captain Sinha asked you for one simple thing, and you could not give it to him.

    That was one mistake too many, and it led to this unfortunate end.

    You are getting closer to the truth.

    If you want to reach the end of this story, you should stop making bad decisions like this.
    """

    jump ending_generic


label host_ending_die_in_sleep:

    $ host_details.endings.unlock('die_in_sleep')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('die_in_sleep'))

    call death_screen_transition

    """
    You do not wake up.

    You died in the night, in your clothes, behind a locked door with a chair wedged beneath the handle.

    You told nobody in that house what you truly were, so you were entirely alone in the night.

    In dangerous situations, it is sometimes best to have an ally to rely on.
    """

    jump ending_generic


label host_ending_shot_in_car:

    $ host_details.endings.unlock('shot_in_car')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('shot_in_car'))

    call death_screen_transition

    """
    You got into a car in the dark with a man you barely knew.

    There were plenty of signs that could have warned you about the risk, but you ignored them.
    """

    jump ending_generic


label host_ending_escape:

    call survive_screen_transition

    $ play_music('end_credits')

    $ host_details.endings.unlock('escape')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('escape'))

    """
    You told one man the truth, and you spent a morning preparing instead of running.

    A car, a tin of petrol, and a locked door opened out of conscience.

    Then you left three people behind in that house, and you sent help from the town.

    You will never know whether it arrived in time, and you will have a great deal to explain.

    But you are alive to explain it.
    """

    $ is_death = False

    jump ending_generic


label host_ending_car_ambush:

    $ host_details.endings.unlock('car_ambush')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('car_ambush'))

    call death_screen_transition

    """
    You would not leave without them, so you took them all, and the car never got past the wood.

    Somebody had seen to that engine before it left the garage, and you never saw who fired.

    Captain Sinha knew what you were, and he would have let you drive. In front of the others you kept to the part, and the part put you in the back seat with your hands in your lap.

    Two people in a motor get through. Five do not.
    """

    jump ending_generic


label host_ending_poisoned:

    $ host_details.endings.unlock('poisoned')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('poisoned'))

    call death_screen_transition

    """
    Three people have died in that house since Friday, and you sat down at its table with nobody at your back and ate what was put in front of you.

    Captain Sinha asked you for one thing before he went. Lock yourself in.

    You had the key to every door in the house in your pocket, and you used it on none of them.
    """

    jump ending_generic


label host_ending_shot_by_butler:

    $ host_details.endings.unlock('shot_by_butler')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('shot_by_butler'))

    call death_screen_transition

    """
    You hid, and it worked, for the better part of three hours.

    Then the house went quiet, and you came down to see why, and you were sitting at your own table when the car came up the drive.

    He came back for what he was owed, and you were the one person left in that house who could put a name to him.

    Captain Sinha walked out of that house at a quarter past twelve, and there was no motor to go with him in.

    There is one in the garage. Look harder for what it wants.
    """

    jump ending_generic
