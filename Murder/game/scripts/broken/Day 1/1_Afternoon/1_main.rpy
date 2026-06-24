# --------------------------------------------
#   Broken
#
#   Friday - Afternoon
#
#   14:00 -> 14:45
#
#   Music: Chill, upbeat
#
#   Alive: Everyone
#
#   Notes :
#       -
# --------------------------------------------
label broken_introduction:

    $ broken_details.add_checkpoint("broken_introduction")

    call change_time(14, 00, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    $ change_room("broken_flat")

    $ play_music('sad', 2)

    """
    I am looking at Thomas, lifeless on his bed.

    His injuries got the best of him in the end.

    The mask that was supposed to help him live a normal life sits beside him.

    He won't have to wear it any longer.

    That brings me a sort of relief.

    He could never bear the way people looked at him.

    After sacrificing his youth to his country, he ended up alone in his flat.

    Too frightened to go out, most days.

    The loneliness may have killed him as surely as his failing body.

    I searched the place and found nothing that was not a necessity.

    On his desk sits a photograph of the two of us, taken on leave one weekend.

    The caption reads: Thomas and Archie, Talbot House, Poperinge, 1916.

    Two officers from the Intelligence Service, assigned to chaperone the senior journalists reporting on the war.

    I don't think I would have become a reporter without that assignment.

    I met Thomas there, and with death all around us, both of us chasing the same stories, we became firm friends soon enough.

    His upbringing would not normally have opened that path to him.

    But war is the great leveller, and when given the opportunity, he took it and excelled.

    Of the two of us, he was the natural journalist, always inquisitive, questioning everything.
    
    He was also not shy about showing his disapproval when we were ordered to soften a tragedy into a minor defeat, which sadly happened all too often.

    Were it not for the accident, he would be the one working for The Times today, not me.
    """

    pause 1

    """
    Beside the photograph lies a letter.

    Well, he won't mind me reading it now.

    I pick it up.
    """

    letter """
    5th September, 1924

    Dear Mr Moody,

    I am pleased to announce that you have been selected as one of the recipients of the "Exceptional Act of Bravery Award".
    """

    call black_screen_transition("{s}Thomas Moody{/s}", "Archibald Devereux")

    $ change_room("train_inside_first")

    play sound train_moving loop

    $ play_music('chill')

    """
    I am still not sure what I am doing here.

    Impersonating my dear Thomas.

    But there was something about that letter that would not let me rest.

    Years of chasing stories have left me unable to look away from a thing that does not add up.

    A journalist learns to read between the lines, and these lines did not sit right.

    So I did what I always do.

    I started asking questions.

    The place, at least, exists.

    That much I confirmed.

    Yet the award was unheard of before this year, so this must be the very first time it has been given.

    And a few quiet enquiries into the estate's finances told a familiar tale.

    Like most second-rate aristocratic families, the one keeping Claythorn Manor has precious little to spare.

    So why give away such a sum?

    Perhaps it is the final wish of some dying aristocrat's fortune, to do a little good before the end.

    Or perhaps it is bait, dressed up as charity, to draw a particular sort of guest to their door.

    Either way, I feel there is a story in it worth the telling.

    But I would be lying if I said that were the whole of it.

    The money on offer is substantial, and a journalist's wage has never stretched far.

    If I can carry off the part of Thomas, Lady Claythorn has no reason not to hand me the prize.

    I glance at the mask I have brought with me.

    It should help me pass unnoticed.

    Still, I have no notion of how much the host already knows of him, so I must be ready to answer as Thomas, whatever she asks.

    Fortunately, I know it all.

    His childhood, his dreams, his every fear.

    But I must stay in character at all times.

    From now on, I am no longer Archibald Devereux.

    I am
    """

    call black_screen_transition("", "Thomas Moody", is_fast=True)

    play sound train_stopping

    $ change_room("train_station")
    """
    The train has stopped and I step out.

    I look around for a few minutes until I spot a group of people who could be heading for the same place as me.

    So I introduce myself.
    """

    call common_day1_afternoon_station_doctor_nurse_broken

    $ change_room("inside_car")

    """
    The journey is rather quiet, which suits me well.

    The less I say, probably the better.

    After a while, we reach our destination.
    """    
    
    $ stop_music()
    
    $ change_room("manor_exterior")

    """
    It is good we have arrived early, for the sky promises a storm before long.

    I take a good look at the place.

    Claythorn Manor is what I imagined it would be.

    Impressive but not regal.

    One of hundreds of grand houses of this type.

    If my research is correct, it is bound to be sold and turned into something else in the near future.

    But in the meantime, it should prove a pleasant place to stay.
    """
    
    jump broken_day1_evening
