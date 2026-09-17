# --------------------------------------------
#   Drunk
#
#   Friday - Afternoon
#
#   15:45 -> 16:45
#
#   Music: chill
#
#   Alive: Everyone
#
#   Notes :
#       - He is drunk from the first line to the last. The chapter is a
#         string of places with the black between them: the train, the
#         platform, the car, the hall, the tea room, the sofa.
#       - Second class. The others came up first.
#       - The station and the hall are shared with Miss Baxter and the
#         Captain (common_day1_afternoon_station_manning_arrives,
#         common_day1_evening_second_arrival_part_1 and _2).
#       - Unlocks : drunk 'age', 'status', 'addict', 'job', 'heroic_act'
# --------------------------------------------
label drunk_introduction:

    call change_time(15, 45, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    $ drunk_details.add_checkpoint("drunk_introduction")

    call black_screen_transition("", "Samuel Manning")

    $ drunk_mode = True

    $ change_room("train_inside_second", irisout)

    show layer master at drunk_wobble_layer

    play sound train_moving loop

    $ play_music('chill')

    """
    The window will not stay still.

    Neither will the seat, or the man opposite, who got on at Carlisle and has been pretending to read the same page since.

    Second class. Second class is fine. Second class is what is left when the first has gone on the rent.
    """

    """
    There is a letter in my coat.

    I have read it four times since London and I could not tell you what it says.

    I read it a fifth time.
    """

    letter """
    "... in recognition of your tireless work on behalf of the poor and the friendless, who have found in you a defender when every other door was closed to them ..."
    """

    """
    Tireless.

    Somebody has been reading the wrong newspaper.

    I take the cases nobody else will, that is true. I take them because nobody else will have me, which is also true, and which the letter does not mention.

    A defender. Ha.

    I could not defend a dog.
    """

    $ drunk_details.description_hidden.unlock('job')
    $ drunk_details.description_hidden.unlock('heroic_act')

    """
    And a thousand pounds.

    That part I read six times.

    A thousand pounds is a year of not thinking. Two years, if I am careful, and I am never careful.
    """

    """
    The flask is in my other pocket.

    I know exactly how much is in it, the way a man knows how much is left in his purse.

    Enough to get to the station.

    Not enough to get to the house.

    Well. A house like that will have a cellar.
    """

    $ drunk_details.description_hidden.unlock('addict')

    """
    My father had a cellar.

    My father had a cellar, and a cook, and a table that people came forty miles to sit at, and a son he sent to the Bar because it was what one did.

    I was going to be somebody. I was somebody, for a while.

    Fifty-five years old.

    Fifty-five, and the man opposite would not lend me a shilling on the look of me.
    """

    $ drunk_details.description_hidden.unlock('age')
    $ drunk_details.description_hidden.unlock('status')

    """
    The train slows.

    Or I do.

    I close my eyes for one moment, because the window has stopped moving and that is a mercy, and...
    """

    stop sound

    scene black_background with dissolve

    pause 1.5

    play sound train_stopping

    """
    ...somebody is shouting a name.

    The name of a place. A station.

    This station.
    """

    $ change_room("train_station")

    """
    I am on the platform.

    I do not remember the door, or the step, or how the bag came with me, but the bag is in my hand and the platform is under my feet, and behind me the train is pulling out with the man from Carlisle still reading his page.

    Three people at the far end, all looking at me.

    A young fellow in livery. A tall dark man, very straight. A woman with too much hat.

    I walk towards them. The platform helps by being mostly flat.

    They have been waiting for me, it seems, which is a novelty. People do not usually wait for me any more.
    """

    footman """
    Hello, sir. Are you going to Claythorn Manor?
    """

    drunk """
    I am indeed.
    """

    footman """
    Perfect, that should be everyone.

    You can follow me to the car, and we'll be on our way.

    It will take about an hour to reach the manor.
    """

    """
    An hour.

    The straight man and the hat go into the back of the car before I have reached it.

    So the front is mine, and the driver, and the road.
    """

    $ change_room("inside_car")

    """
    He is a good-looking boy, the driver. Young. Very careful with his hands on the wheel.

    I tell him so.

    I tell him about the train, and about the man from Carlisle, and something about the Bar that I had not meant to get on to, and about halfway through it I hear my own voice from the outside, the way one sometimes does.

    It is not making words. Not whole ones.

    The boy nods at the road and says 'yes, sir' at the places where a man would say 'yes, sir', and does not look at me once.

    He is very good at that. Somebody has trained him.
    """

    """
    Behind me, the straight man is talking to the hat.

    He is telling her where he is from. It is taking a very long time.

    I take the flask out, because there is no point in saving what will not last, and I finish it.

    Then the road goes soft, and the boy's careful hands go soft, and...
    """

    scene black_background with dissolve

    pause 1.5

    call change_time(16, 30, 'Evening', 'Friday')

    """
    ...the car has stopped.

    A house. Grey, and a great deal of it, with the sky going black behind it.

    The hat and the straight man are already out, already at the door.

    I get out. The gravel comes up a little to meet me, but I have known worse gravel.
    """

    $ change_room("entrance_hall")

    """
    A butler.

    A real one, or a man doing a very fair impression. Tall, with a face that has been hit at some point and has not forgiven anybody for it.

    He says something about her ladyship.
    """

    call common_day1_evening_second_arrival_part_1

    """
    That is my voice again, and this time it has made a whole sentence.

    Drink does that. It finds the one thing a man truly wants and hands him the words for it.
    """

    call common_day1_evening_second_arrival_part_2

    """
    The straight man comes with me.

    I do not think he wants my company. I think he wants to be away from the hat.

    I know the feeling. I have been married.
    """

    $ change_room("tea_room", dissolve)

    call change_time(16, 45)

    """
    A tray.

    A tray with a decanter on it, and glasses, and I am at it before the straight man has finished being announced.

    Sherry. It will do.

    There is a woman by the tray, a thin one, all buttons, and I say good afternoon to her and something about the weather and something about the house.

    She says 'quite' and 'indeed' and steps back one pace for every one I take.

    I let her go. I am not a monster. I am only thirsty.
    """

    """
    The glasses are small.

    A house this size, and the glasses are the size of a thimble.

    There is a water glass on the side. I fill it to the brim from the decanter and I drink it the way a man drinks water, because that is what it is in, and I put it down.
    """

    $ drunk_details.saved_variables["day1_drinks"] += 1

    """
    Two men by the fire. One in spectacles, grey as a sheet. One in a mask.

    A mask.

    I have seen those, on the Strand. The war gave a lot of men a reason to hide their faces. Mine I earned on my own.

    The straight man is going over to them. He is going to tell them where he is from.

    There is a sofa.

    There is a sofa, and it is not moving, and I sit on it, and I do not remember deciding to.
    """

    $ stop_music(3)

    scene black_background with dissolve

    pause 2.0

    jump drunk_day1_evening
