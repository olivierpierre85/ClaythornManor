label host_day2_evening_billiard_room_empty:

    $ change_room('billiard_room')

    """
    The drinks have been set out on the side table, the lamps are lit, but there is not a soul in the room.

    It is not really surprising, though.

    Two deaths in the same weekend are enough to scare just about anybody.

    I do not think anyone will show up here tonight.

    I leave the room.
    """

    return


label host_day2_evening_billiard_room:

    $ change_room('billiard_room')

    """
    The Captain is alone in the billiard room, sitting with a book in his hands.

    There is no time for a drink or anything else.

    I go directly to him.
    """

    host """
    Captain.

    I was not sure anyone would come here tonight.
    """

    captain """
    Well, the events of today have probably scared some of them.
    """

    host """
    But not you, I take it.
    """

    captain """
    No indeed.

    I can see what happened today for what it is, unfortunate accidents.

    However sad that may be, I see no reason to hide in my room over them.
    """

    host """
    I see.
    """

    captain """
    But what about you, Lady Claythorn, how are you holding up tonight?
    """

    """
    Here is a chance to tell him how I really feel.

    But it would be very risky.
    """

    call run_menu(
        TimedMenu("host_day2_evening_menu_billiard_room", [
            TimedMenuChoice("Tell him what you really are", 'host_day2_evening_billiard_room_truth', early_exit=True),
            TimedMenuChoice("Keep to small talk", 'host_day2_evening_billiard_room_small_talk', early_exit=True),
        ])
    )

    return


# --------------------------------------------
#   She drops the mask
#   -> 'trust_captain'
# --------------------------------------------
label host_day2_evening_billiard_room_truth:

    """
    He missed a rabbit sitting still at twenty paces this morning, and he took my excuse about the light without a blink.

    If he is wearing a costume of his own, he may understand mine.

    And if he is not, there is nobody else left in this house to tell.
    """

    host """
    Not well, Captain.

    And I cannot answer you honestly without telling you something first.

    I am not who I say I am.
    """

    """
    He closes the book on his finger and waits.

    He does not look surprised in the least.
    """

    captain """
    Go on.
    """

    host """
    There is no Lady Claythorn.

    I am an actress. I was hired in London to play her for the weekend, and paid an advance to do it.

    The staff were hired the same way. None of us had set foot in this house before Friday.
    """

    captain """
    I had wondered.

    I have met a good many people this weekend who are not quite what they say they are.

    You are simply the first to admit it.

    Who hired you?
    """

    host """
    I do not know. I was never given a name.

    The butler deals with them. He gives the orders, and I am handed a piece of paper to read at dinner.

    Tonight he told me the whole affair is cancelled, and that he leaves in the car at eleven, with or without me.
    """

    captain """
    And the police?
    """

    host """
    Were never called.

    The telephone was disconnected long before any of us arrived.

    He had me act the call this afternoon, for the benefit of anyone listening.
    """

    """
    For a moment he says nothing at all.

    I have just told a stranger that two of his fellow guests died in a house with no way of reaching help, and that I helped to hide it.

    If he is going to call for the others, it will be now.
    """

    captain """
    A moment ago I told you I took today for accidents.

    I said that to my hostess. I will not say it to you.

    Two men do not die in one day by chance, and I do not believe you had a hand in either of them.

    You would not be sitting here telling me this if you had.
    """

    host """
    Then what am I to do? He leaves at eleven.
    """

    captain """
    Stay.

    A man who drives away in the dark is not a man I should get into a car with.

    Go up and lock your door.

    I have a pistol in my room, and I sleep lightly. If anything troubles you in the night, make a noise and I shall hear it.

    In the morning we shall see who is left in this house, and then you and I will have a long talk about the butler.

    Until then, nobody else needs to know any of this. Not Miss Marsh, not Miss Baxter, and certainly not him.
    """

    """
    I have put myself in the hands of a man I have known for two days.

    But he says it all as though it were the simplest thing in the world.

    For the first time since the shots in the wood, my hands are still.
    """

    host """
    Thank you, Captain.

    Good night.
    """

    captain """
    Good night, madam.
    """

    """
    Madam. Not my lady.

    It is the kindest thing anybody has said to me all weekend.
    """

    $ host_details.threads.unlock('trust_captain')

    return


label host_day2_evening_billiard_room_small_talk:

    """
    No.

    He is a soldier, and a soldier's first thought will be for the police.

    And the police will want to know why no call was ever made from this house.

    I have kept the part this long. I can keep it one more night.
    """

    host """
    As well as can be expected, Captain, thank you.

    It has been a very long day.
    """

    captain """
    It has indeed.
    """

    """
    I ask him about the book in his hands, he asks me about the estate, and we agree, that the poor hunt of this morning was due to bad luck.

    When the conversation dies down, I rise.
    """

    host """
    I shall leave you to your book, Captain.

    Good night.
    """

    captain """
    Good night, my lady.
    """

    return
