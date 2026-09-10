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
            TimedMenuChoice("Tell him what you really are", 'host_day2_evening_billiard_room_truth', 666, early_exit=True),
            TimedMenuChoice("Keep to small talk", 'host_day2_evening_billiard_room_small_talk', early_exit=True),
        ])
    )

    return

label host_day2_evening_billiard_room_truth:

    host """
    Not well, Captain.

    I am very disturbed by what happened today.
    """

    captain """
    I understand, but you should not blame yourself.

    Accidents like this happen all the time.
    """

    host """
    Maybe, but the circumstances of this weekend were not really ordinary.

    I am afraid that played a part in all that.
    """

    """
    He closes the book on his finger and waits.
    """

    captain """
    What do you mean?
    """

    host """
    Let me tell you a story.

    I warn you, it is rather unsettling, and you will have a thousand questions for me, I am sure.

    But please, I need you to wait until the end, then we can discuss further.
    """

    captain """
    You intrigue me, Lady Claythorn.

    But please, do tell your story.
    """

    """
    First, I am not Lady Claythorn.

    I don't even think there is one.

    I'm an actress playing a role.

    I have been doing it this entire weekend.
    """

    """
    At this revelation he flinches a little, but as promised he does not stop me.
    """

    host """
    A few months ago.

    An acquaintance of mine approached me to offer me a rather unusual acting job.

    Impersonating a Lady in her Manor to entertain guests.

    The explanations were scarce but the money was good.

    The reason for the weekend remained evasive, he just told me it was a prank of sorts.

    At that point, my career was not going so well that I could afford to turn down a job.

    So I agreed.

    My role was explained in detail, what I should know, how I should act.

    Then I came to this manor with two other actors, who played the footman and the maid you saw this weekend.

    The butler was the one who offered me the job and is in charge of the whole operation.
    """

    """
    I look to Captain Sinha and his face is as still as ever.
    """

    captain """
    So the butler is the one managing this weekend, but on whose behalf?

    And what is the purpose of all this?
    """

    host """
    I do not know who is behind this.

    I was never given a name.

    And I still have no idea of the reasons, but I am starting to suspect it was not just to play a harmless joke.
    """

    captain """
    And what did you tell the police?
    """

    host """
    They were never called.

    The telephone was disconnected long before any of us arrived.

    He had me act the call this afternoon, for the benefit of anyone listening.
    """

    """
    For a moment he says nothing at all.
    """

    host """
    I know it is a lot, Captain, but please believe me.

    I did not know things would turn this bad, I am in the same boat as everyone else.
    """

    captain """
    Do not worry, I believe you.

    I do not think you would be telling me this if you were responsible.

    Also, even though I acted as though everything were pure coincidence, the truth is I suspected something was wrong.

    I just could not understand what.

    Now it is clear what should be done.
    """

    host """
    Good, so what do you have in mind?
    """

    captain """
    There is only one logical thing to do.

    Ask the only person who must know exactly what is happening.
    """

    host """
    The butler, he will leave soon with the car.

    We should hurry if we want to catch him before he leaves.
    """

    captain """
    Let us not waste time then.
    """

    host """
    But he might be dangerous.
    """

    captain """
    Do not worry, I have a pistol on me if he tries anything.
    """

    $ play_music('danger', 2)

    """
    He sets the book down and rushes to the entrance hall.
    """

    $ change_room('entrance_hall')

    """
    The hall is dark and the stair is empty.

    But we can hear the sound of an engine in the driveway.
    """

    $ change_room('manor_garden', dissolve)

    """
    The car stands on the gravel with its lamps lit and the luggage already strapped behind.

    The maid and the footman are in the back, sitting very straight, looking at nothing.
    """

    host """
    There he is.
    """

    """
    The butler turns at my voice, and the Captain steps into the light before I can put a hand out to stop him.

    He sees the Captain first.

    He does not look at me at all.
    """

    """
    Whatever he reads in that face, he does not care to discuss it.

    He is behind the wheel before either of us has crossed the gravel.
    """

    play sound car_driving

    """
    Captain Sinha chases the car for a moment, but he quickly realises it is pointless.

    It is on the road now, and we will not catch it.
    """

    captain """
    Well, he felt guilty enough to run without even trying to give an explanation.

    That tells us all we need to know.
    """

    host """
    But what should we do now?
    """

    captain """
    Well, I am afraid we will have to wait until tomorrow.
    """

    host """
    And then?
    """

    captain """
    Then we will leave as well, on foot if we must.
    """

    host """
    Right.
    """

    """
    The cold comes up through my shoes.

    I have walked out here in my dinner things without a coat, and only noticed now.

    The Captain notices my shivering.
    """

    captain """
    Let us go back inside, there is no point waiting here in the cold.
    """

    $ change_room('entrance_hall')

    captain """
    I think now we should wake the others and tell them what you have told me.

    They have a right to know what is happening.
    """

    host """
    I don't know, Captain.

    Maybe telling everyone is not the best way.
    """

    captain """
    Why is that?
    """

    host """
    Well, earlier today the butler claimed that he had received word from whoever is behind this.

    But as I told you, the phone is down.

    So I am not sure how he got that message.

    Unless...
    """

    captain """
    Unless the culprit is somewhere in this house.
    """

    host """
    Yes, the house is big enough that they could hide in a room, but I have also imagined that...
    """

    captain """
    That they could be among us.

    One of the guests could be manipulating what is happening here.
    """

    host """
    Yes, I may sound paranoid, but I do not want to exclude that possibility.
    """

    captain """
    I see.

    Very well.

    We say nothing to anyone until daylight.

    We will decide what to do next then.

    In the meantime, I do not like to leave you alone in your room.
    """

    host """
    What do you propose?
    """

    captain """
    I could sit up in your room tonight.

    It would be safer this way.
    """

    host """
    In my room.
    """

    captain """
    In a chair, by the door, with the lamp out.

    I am aware of how that looks.

    I am rather more concerned with how the alternative might look in the morning.
    """

    host """
    Thank you, Captain.

    You are right, it is probably safer for me.

    You are sure you won't be too uncomfortable in a chair?
    """

    captain """
    I have slept on worse.

    And besides, I do not think I will be able to sleep much tonight.
    """

    host """
    You are right, me neither.
    """

    captain """
    Then it is decided.

    We can go up now if you wish.

    It is late enough.
    """

    host """
    All right.
    """

    $ host_details.threads.unlock('trust_captain')

    return


label host_day2_evening_billiard_room_small_talk:

    """
    No.

    He is a soldier, and a soldier's first thought will be for the police.

    And the police will want to know why no call was ever made from this house.

    I have kept up the part this long.

    I can keep it one more night.
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
