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

    # The intro for BROKen is set in an apartment.

    # A DAY EARLIER 
    """
    I am looking at Thomas, lifeless on his bed.

    His injuries had the best of him in the end.

    The mask that was suppose to help him live a normal live sits next to him.

    He won't have to wear it anymore.

    That brings a sort of relief.
    
    He couldn't bare the look of the people around him.

    After dedicated his youth to the army he ends up alone in his apartment.

    To scared to go out most of the time.

    The loneliness might have been the cause of death as much the failings of his aching body.

    I search about his place and found nothing that was not a necessity.

    On his desk is a picture of us we took when we were on leave for a weekend.
    
    The caption reads: Thomas and Archie, Talbot House, Poperinge, 1916.

    Two officers thrown in the middle of hell.
    
    With death all around us, we became best friends rapidly.

    Next to the picture sits a letter.

    Well he won't might me reading it now.

    I pick it up.
    """

    letter """
    5th September, 1924

    Dear Mr Moody,

    I am pleased to announce that you have been selected as one of the recipients of the "Exceptional Act of Bravery Award".
    """

    call change_time(14, 00, 'Arrival', 'Friday', hide_minutes=True, chapter='friday_afternoon')

    call black_screen_transition("{s}Thomas Moody{/s}", "Archibald Devereux")

    $ change_room("train_inside")

    play sound train_moving loop

    $ play_music('chill')

    """
    I am still not sure what I am doing here.

    """

    broken """
    test
    """

    jump broken_day1_evening
