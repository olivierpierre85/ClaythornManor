# --------------------------------------------
#   Drunk
#
#   Friday - Evening
#
#   16:30 -> 23:45
#
#   Music: chill at dinner, scary for the letter, upbeat for the house and the billiard room
#
#   Position
#       - Dining Room : Everyone (he sits on Lady Claythorn's left, Miss Marsh
#         below him, the boy across the table)
#       - Bedroom Drunk : the letter, straight after dinner
#       - Billiard Room : the party, then alone once he wakes
#
#   Notes :
#       - Dinner: one person to turn to (or none), then the meal (food)
#       - The letter comes BEFORE the map: in the doctor's path the letter,
#         second half included, is already on the desk while the party is in
#         the billiard room (doctor_day1_evening_bedroom_drunk_enter)
#       - Letter: drink (day1_drink), or put the bottle down (intuition,
#         after the 'despair' ending)
#       - Map (0_map_choices.rpy), then the billiard room to drink and sleep.
#         He wakes alone: carry the bottles up (raided_bar, port) or not
#         (2_billiard_room.rpy)
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

    There is nothing wrong with sitting.

    If anyone wants to talk to me, they can come to me.

    I make myself comfortable on the couch.
    """

    $ drunk_details.saved_variables["day1_drinks"] += 1

    $ stop_music()

    call wait_screen_transition()

    play sound dinner_gong

    """
    What in the devil?

    What was that, a gong?

    I must have dozed off a little.

    Around me the rest of the guests head to the dining room, so I follow suit.
    """

    call change_time(18, 30, 'Dinner', 'Friday')

    $ change_room('dining_room', irisout)

    $ play_music('chill', 2)

    """
    Every place is marked with a card.

    I go round half the table before I find mine, near the head.

    The chair at the head is still empty, so Lady Claythorn will be on my right.

    On my left sits a lady whose card says Miss Marsh.

    Lady Claythorn comes in last.

    She walks the length of the room, takes her place at the head of the table, and waits for silence before she speaks.

    Then she begins, and I try to focus on what she is saying.
    """

    host """
    Welcome, everyone...

    ... my gratitude once more...

    ... the heroic acts you've committed in the past...
    """

    """
    The speech ends, and there is a murmur of thanks round the table.

    I wake up from my own thoughts and add mine, a little late.

    The first course is a clear soup.

    It smells very good, but before I take a sip, I notice that the staff are coming round with the wine.
    """

    drunk """
    To the top, if you please.

    Don't be stingy with it.
    """

    """
    I empty the glass before the man has taken two steps, and hold it out again.

    He fills it without a word.

    Miss Marsh looks at my glass, then at me, then at her soup.

    Lady Claythorn on one side, Miss Marsh on the other.

    I suppose I ought to say something to one of them.

    Or I could simply eat.
    """

    $ drunk_details.saved_variables["day1_drinks"] += 1

    call change_time(19, 30)

    $ time_left = 90

    call run_menu(TimedMenu("drunk_day1_evening_menu_dinner", [
        TimedMenuChoice("Tell Lady Claythorn what you think of the food", 'drunk_day1_dinner_host', early_exit=True),
        TimedMenuChoice("Tell Miss Marsh what you think of the wine", 'drunk_day1_dinner_nurse', early_exit=True),
        TimedMenuChoice("Keep to yourself", 'generic_cancel', early_exit=True),
    ], image_left = "nurse", image_right = "host"))

    """
    After that, I keep to my plate and my glass.

    Whenever the glass runs low, I ask for more.

    They never say no.

    That tells me they follow proper etiquette. Good.
    """

    $ drunk_details.saved_variables["day1_drinks"] += 1

    """
    Our host politely asks me a few questions, which I manage to answer as best I can, but then the conversation dies out...
    """

    """
    It does not matter much.

    The food deserves my full attention anyway.

    After the fish come lamb cutlets, still pink at the bone, in a sauce made from their own juices with a spoonful of redcurrant jelly.

    Simple, but delicious nonetheless.

    The pudding is a charlotte russe, and it holds its shape when the spoon goes in.

    I have not eaten like this in years.

    Yet I remember other suppers I have shared with members of the aristocracy.

    In comparison, this meal is simpler, smaller.

    I was expecting more. A joint of beef, perhaps, carved at the sideboard. Or shallots cooked slowly in butter.

    Well, at least there is enough wine.
    """

    $ drunk_details.description_hidden.unlock('food')

    $ stop_music()

    call change_time(21, 00)

    """
    The last plates go out.

    Lady Claythorn looks round the table and addresses us once more.
    
    I understand that there will be drinks in the billiard room.

    That is good news.

    But I supposed I should head to my room first.

    I have not even seen it yet, and my bag is up there.

    A footman shows me the way.
    """

    call drunk_day1_evening_letter

    call change_time(21, 30)

    $ play_music('upbeat')

    # TODO add dialogs
    #   - He leaves his room with the door ajar (the doctor finds it that way,
    #     doctor_day1_evening_bedroom_drunk)
    #   - The billiard room can wait. Or can it?

    $ time_left = 90

    call run_menu(drunk_details.saved_variables["day1_evening_map_menu"])

    $ stop_music()

    if not drunk_details.saved_variables["day1_evening_billiard_room_visited"]:

        call change_time(23, 00)

        # TODO add dialogs
        #   - He never made it to the billiard room. Back to his room

    $ change_room('bedroom_drunk', dissolve)

    # TODO add dialogs
    #   - Bed, with the letter still on the desk

    jump drunk_day2_morning


# ------------------------------------
#   DINNER — LADY CLAYTHORN (at the head, on his right)
#   He tries to say something about the food, realises he is not making
#   sense, and shuts up.
# ------------------------------------
label drunk_day1_dinner_host:

    """
    The fish arrives.

    Sole, poached, under a butter sauce.

    It is exquisite.

    The lady of the house ought to know that her cook deserves a rise.

    I turn to her and tell her so.
    """

    drunk """
    Lady Claythorn.

    The sole.

    Whoever... whoever made it did not hurry.

    Butter, and the liquor, and lemon, but not too much lemon.

    You cannot rush a sole, you know.

    It splits.

    Your cook... a rise.

    Give your cook a rise.
    """

    """
    She looks at me, perplexed, with no idea what to answer.

    Then she nods, with the polite smile one gives a child.

    I go back over what I have just said.

    It did not come out the way it sounded in my head.

    I return to my plate and keep my mouth for eating.
    """

    return


# ------------------------------------
#   DINNER — MISS MARSH (below him, on his left)
#   He tries to say something about the wine, realises he is not making
#   sense, and shuts up.
#   Her side of it: nurse_day1_dinner_drunk
# ------------------------------------
label drunk_day1_dinner_nurse:

    """
    Miss Marsh, on my left, has hardly touched her wine.

    I lean towards her.
    """

    drunk """
    Miss Marsh.

    The claret.

    Young.

    Young, but honest.

    They always serve it too... too warm, but there is plenty.

    Plenty of it.

    That is the great virtue of a claret.

    You should take a sip.
    """

    nurse """
    I beg your pardon, Mr Manning?
    """

    """
    I open my mouth to say it again, and find the sentence has gone.

    It made perfect sense a moment ago.

    Miss Marsh waits politely for the rest of it.

    There is no rest of it.

    So I nod at her glass, and say nothing more.
    """

    return


# ------------------------------------
#   THE LETTER (his room, straight after dinner)
#   -> day1_drink, or the bottle put down (intuition, after 'despair')
# ------------------------------------
label drunk_day1_evening_letter:

    $ change_room('bedroom_drunk', dissolve)

    $ unlock_map('bedroom_drunk')

    $ play_music('scary', 2)

    # TODO add dialogs
    #   - His room. A letter on the desk, in a fine, elegant hand
    # TODO he empties his bag, whisky bottles fall on the floor.

    call drunk_letter_first_part

    $ drunk_details.description_hidden.unlock('wife')

    $ doctor_details.description_hidden.unlock('fraud')

    # TODO add dialogs
    #   - Eleanor. The doctor, a few chairs away at dinner
    #   - He takes up a pen and writes the second half himself

    call drunk_letter_second_part

    # TODO add dialogs
    #   - The bottle in his bag

    $ time_left = 1

    call run_menu(TimedMenu("drunk_day1_evening_menu_letter", [
        TimedMenuChoice("Drink until it goes away", 'drunk_day1_evening_letter_drink', early_exit=True),
        TimedMenuChoice("Put the bottle down{{intuition}}", 'drunk_day1_evening_letter_sober', early_exit=True, condition="drunk_details.endings.is_unlocked('despair')"),
    ]))

    return


label drunk_day1_evening_letter_drink:

    $ drunk_details.threads.unlock('day1_drink')

    $ drunk_details.saved_variables["day1_drinks"] += 1

    $ set_drunk_mode(3)

    # TODO add dialogs

    return


label drunk_day1_evening_letter_sober:

    # TODO check the strength: the sherry and the dinner wine are still in him
    $ set_drunk_mode(1)

    # TODO add dialogs
    #   - From here on he only plays the drunk (lie). The others still see him slumped at the bar

    return
