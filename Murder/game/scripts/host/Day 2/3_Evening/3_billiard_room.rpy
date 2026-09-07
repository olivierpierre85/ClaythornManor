# --------------------------------------------
#   THE BILLIARD ROOM - CAPTAIN SINHA
# --------------------------------------------
label host_day2_evening_billiard_room:

    $ change_room('billiard_room')

    """
    The Captain is alone in the billiard room, sitting with a book in his hands.
    """

    # TODO add choice of talking telling him the truth or just making small talks?
    host """
    Captain.

    I am going to tell you something, and I would ask you to hear all of it before you say anything at all.
    """

    $ host_details.threads.unlock('trust_captain')

    return
