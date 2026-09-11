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

    A car, a tin of petrol, a basket of food, and a locked door opened out of conscience.

    Then you left three people behind in that house, and you sent help from the town.

    You will never know whether it arrived in time, and you will have a great deal to explain.

    But you are alive to explain it.
    """

    $ is_death = False

    jump ending_generic


label host_ending_run_over:

    $ host_details.endings.unlock('run_over')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('run_over'))

    call death_screen_transition

    """
    You set out on foot, on an open road, in the middle of the day.

    You knew the sound of that engine before you saw the car, and there was nowhere to go.

    A road is not a way out when the people you are running from are the only ones who use it.

    There was a motor in the garage. It only wanted a little more preparation.
    """

    jump ending_generic


label host_ending_shot_by_butler:

    $ host_details.endings.unlock('shot_by_butler')
    $ host_details.add_ending_checkpoint(ending=host_details.endings.get_item('shot_by_butler'))

    call death_screen_transition

    """
    You read that table rightly.

    The plate Miss Marsh got rid of was meant to kill her, and the one she wanted was only meant to make a young man sleep.

    You gave the poison back to the woman it was meant for, and you took the sleep for yourself.

    It was the cleverest thing anybody did in that house all weekend, and you were unconscious for everything that came of it.

    Samuel Manning had the better idea. He had it on Saturday, and it worked.
    """

    jump ending_generic
