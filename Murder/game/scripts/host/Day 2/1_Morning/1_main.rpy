# --------------------------------------------
#   Host
#
#   Saturday - Morning
#
#   07:30 -> 10:30
#
#   Music: chill for the waking, mysterious upstairs, scary for the announcement,
#          upbeat for the hunt (played by the common labels)
#
#   Position
#       - Bedroom : Host
#       - Dining Room : Everyone
#       - Dead : Broken (Thomas Moody), found in his bed
# --------------------------------------------
label host_day2_morning:

    call change_time(7, 30, 'Morning', 'Saturday', hide_minutes = True, chapter='saturday_morning')

    $ current_character.add_checkpoint("host_day2_morning")

    call black_screen_transition("Lady Claythorn", chapters_names[current_chapter])

    $ change_room('bedroom_host', irisout)

    $ play_music('chill', 3)

    """
    I wake and start getting ready for breakfast.

    I realise I have the easy role in all of this.

    The rest of the staff must have been at work a big part of the night.
    
    Then awake sooner than I do.

    I hope they will still be all right today.
    """
    
    call change_time(8, 30)

    $ change_room('dining_room', dissolve)


    """
    I reach the dining room hoping to be the first one there.

    To my surprise, Captain Sinha is already seated, enjoy a light breakfast.
    """

    captain """
    Good morning, I am sorry, I am already.

    It is a soldier's habit, I am afraid.
    """

    host """
    Do not worry Captain.

    I will fix myself a plate and join you soon.
    """

    """
    I take my place at the table and the guests arrive one by one.
    """

    call change_time(9, 15)

    $ play_music('mysterious', 2)

    call common_day2_morning_host_to_doctor

    # --- Upstairs, which no other character sees ---

    $ change_room('bedrooms_hallway', dissolve)

    """
    todo
    """

    $ change_room('bedroom_broken', dissolve)

    # TODO: Mr Moody dead in his bed. Her first corpse, and she has played a dozen.
    # TODO: The doctor examines him and speaks of old wounds and natural failure.
    # TODO: The butler is entirely unmoved, and that is what frightens her, not the body.
    # TODO: The authorities. The doctor asks for them to be sent for, the butler
    #       undertakes to see to it, and she is the only one in the room who knows
    #       what his undertakings are worth.
    # TODO: Menu candidate - press the butler about the telephone or the car now, or
    #       hold her tongue until the guests are out of the house. Needs threads.

    call change_time(10, 00)

    $ change_room('dining_room', dissolve)

    # TODO: Going back in. The whole table turns, and she has to say it out loud.

    call common_day2_morning_host_death

    call common_day2_morning_host_death_doctor

    # TODO: Sitting through the silence afterwards, counting how many of them are
    #       looking at her rather than at their plates.
    # TODO: And the thing she cannot say: a man is dead in a house that was opened for
    #       three days by a gentleman neither she nor the butler has ever met.

    call change_time(10, 15)

    $ stop_music()

    """
    What now?
    """

    call common_day2_morning_host_hunt

    """
    As expected, Miss Marsh and Miss Baxter excuse themselves.

    The men all agree to come.

    Well I should get ready too.
    """

    jump host_day2_hunt
