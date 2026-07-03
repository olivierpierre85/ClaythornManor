# --------------------------------------------
#   Captain - Saturday Hunt - V2 (Moody alive)
#
#   Grouping:
#       - Captain + Lady Claythorn + Thomas Moody + butler
#       - Doctor + Drunk + Lad + footman
#
#   Linear path: Moody isolates the Captain after luncheon
#                 and shoots him in the woods.
#
#   The north-field hunt and the confrontation are both shared with the Broken
#   storyline:
#       - common_day2_hunt_north_field
#       - common_day2_hunt_captain_confrontation
# --------------------------------------------

label captain_day2_hunt_moody_alive:

    broken """
    Doctor Baldwin's party is already three guns strong.

    I shall round out your own, if my lady will have me.
    """

    host """
    Why, Mr Moody, of course.

    The more the merrier.
    """

    """
    A chill passes through me.

    I would rather have avoided him this afternoon.

    But, I cannot object without drawing attention to myself.
    """

    captain """
    A pleasure, Mr Moody.
    """

    broken """
    The pleasure is entirely mine, Captain.
    """

    """
    The butler steps forward.
    """

    butler """
    Very good. Doctor Baldwin and Mr Manning to the western grove, with Mr Harring.

    The footman will go along with them.

    My lady, Captain Sinha and Mr Moody to the north field, and I shall attend.
    """

    call common_day2_hunt_north_field

    """
    He says it politely enough, but I feel the mockery in his tone.

    I force a thin smile and say no more.

    We settle for luncheon in a clearing bordered by birches.

    The butler lays out a spread upon a linen cloth and serves the tea with his customary care.

    Lady Claythorn ask me to tell them a story of one of my campaigns.

    Mr Moody comments have shaken me and I would prefer to eat in silence.

    But I cannot think of a reason to refuse her.

    While I am talking, Thomas Moody gaze is on me.

    Like he is seeing me for who I really am.
    """
    
    call change_time(13, 0)

    """
    When the story is over, he turns to me.
    """

    call common_day2_hunt_captain_confrontation

    jump captain_ending_shot_in_woods
