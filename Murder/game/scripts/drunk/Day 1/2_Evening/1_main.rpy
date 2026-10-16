# --------------------------------------------
#   Drunk
#
#   Friday - Evening
#
#   18:30 -> 23:00
#
#   Music: chill at dinner, upbeat for the billiard room, scary for the letter
#
#   Position
#       - Dining Room : Everyone (he sits on Lady Claythorn's left, Miss Marsh
#         below him, the boy across the table)
#       - Billiard Room : the party, after dinner
#       - Bedroom Drunk : the letter
#
# --------------------------------------------
label drunk_day1_evening:

    call change_time(16, 30, 'Dinner', 'Friday', hide_minutes=True, chapter='friday_evening')

    $ drunk_details.add_checkpoint("drunk_day1_evening")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ change_room('entrance_hall', dissolve)

    $ play_music('upbeat')

    $ set_drunk_mode(2) 

    call common_day1_evening_second_arrival_part_1

    call common_day1_evening_second_arrival_part_2

    $ change_room('tea_room', dissolve)

    call change_time(16, 45)
    
    """
    I spot several people already in the room, and a tray of drinks in a corner.

    I feel too exhausted for small talk, and I should at least get a drink first.

    I pour myself a glass of sherry and notice a couch I can sit on.

    There is nothing wrong with sitting. If anyone wants to talk to me, they can come to me.

    I make myself comfortable in the couch.
    """

    call wait_screen_transition()

    play sound dinner_gong

    # Drunk is between nurse and host. 
    # Focus on the food and ask for more drinks often? NO possibility to say no, he is unredeemable, unlike doctor.

    # "I think our host politely asks me a few questions, that I manage to answer the best I can, but ""

    # Describe the meal, a possible aristocracy meal for the situation

    # VISIT manor MAKE the map choices.
    # Billiard room to drink and sleep.

    jump drunk_day2_morning
