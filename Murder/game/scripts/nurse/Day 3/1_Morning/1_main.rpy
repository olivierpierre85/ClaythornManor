# --------------------------------------------
#   Nurse
#           
#   Sunday - Morning
# 
#   8:30 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic, doctor, nurse
#       - Dead : broken, drunk
#       -? : Host
#
#   Notes : 
#       - No more maps
#   Useful Threads:
#       - Knows about footman
# --------------------------------------------
label nurse_day3_morning:

    call change_time(8, 30, "Morning", "Sunday", hide_minutes=True, chapter='sunday_morning')

    $ nurse_details.add_checkpoint("nurse_day3_morning") 

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room("bedroom_nurse", irisout)

    $ play_music('mysterious')

    #TODO

    # nurse wakes up, if day1_exhaustion or day2_exhaustion, small comment about it.

    # then she goes to have breakfast in the dinning, room

    # The dinning room is empty

    # She realise there is no help in the manor, and that something is not right. (I should have known, it may be too late now, what should I do)
    # she gets out in the entrance hall.    #  
    # There she notices a weird key next to the entrance
    # The butlers ghost key, to open everything.

    # If she has seen the butler's room before, she will know that she now can open the silver drawer
    # If not, give a hint that it might be there.

    # then she hears others coming down 

    # She now has 2 choices => leave now ( leave poor ending)

    # => Go into the attic to try to steal the good stuff. then wait until the afternoon.


    jump work_in_progress
