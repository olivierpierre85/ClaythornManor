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
    I wake and stat getting ready for breakfast.

    I realise I have the easy role in all of this.

    The rest of the staff must have been at work a big part of the night.
    
    Then awake sooner than I do.

    I hope they will still be all right today.
    """
    
    call change_time(8, 30)

    $ change_room('dining_room', dissolve)

    # TODO: She is down before any of them, which is deliberate. A hostess is never
    #       seen arriving.
    # TODO: The guests come down in order: the Captain, the Doctor, Miss Baxter and
    #       Miss Marsh, Mr Harring, and finally Mr Manning in a dreadful state.
    # TODO: One place stays empty. Mr Moody does not come down, and she notices it
    #       only as a small failure of her table.
    # TODO: Menu candidate - which of them she works on over breakfast. Needs a menu id
    #       and threads before it can be written.

    call change_time(9, 15)

    $ play_music('mysterious', 2)

    # TODO: The butler comes in and bends to her ear. Whatever face she has on, she
    #       must keep it, with seven people watching her receive the news.
    # TODO: The line the butler gives her, and the effort of standing up calmly.

    call common_day2_morning_host_to_doctor

    # --- Upstairs, which no other character sees ---

    $ change_room('bedrooms_hallway', dissolve)

    # TODO: The walk along the corridor with the two of them behind her. The butler
    #       leads and she follows, which is the wrong way round for a house she owns.

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

    # TODO: The hunt. Cancelling it would be the decent thing, and the butler has made it plain that the weekend goes on. She has to sell it as her own idea.

    call common_day2_morning_host_hunt

    """
    As expected, Miss Marsh and Miss Baxter excuse themselves.

    The men all agree to come.

    Well I should get ready too.
    """

    jump work_in_progress
