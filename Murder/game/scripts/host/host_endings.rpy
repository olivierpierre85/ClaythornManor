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

    $ host_details.endings.unlock('escape')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('escape'))

    """
    You made all the right decisions.

    You trusted the right person.

    You knew where to find everything you needed to escape.

    But then you left people behind.

    And you might never know what happened to them.

    Not quite the right ending, is it?
    """

    $ is_death = False

    jump ending_generic


label host_ending_shot_on_road:

    $ host_details.endings.unlock('shot_on_road')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('shot_on_road'))

    call death_screen_transition

    """
    You set out on foot, on an open road, in the middle of the day.

    Had you looked a little harder, you could have left better prepared, and with a motorcar.

    Perhaps things would have been different then.
    """

    jump ending_generic


label host_ending_burned:

    $ host_details.endings.unlock('burned')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('burned'))

    call death_screen_transition

    """
    You hid, and it worked, for the better part of four hours.

    Then the silence got the better of you, and you came down to see why.

    You found a gun, and you would not believe the one man left who could have told you what happened.

    And when the smoke came, there was nobody left to open a door for you.

    Captain Sinha walked out of that house at a quarter past twelve, and there was no motor to go with him in.

    There is one in the garage. Look harder for what it wants.
    """

    jump ending_generic
