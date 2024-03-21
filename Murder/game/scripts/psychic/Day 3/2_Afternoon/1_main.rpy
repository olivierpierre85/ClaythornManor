# --------------------------------------------
#   Psychic
#           
#   Sunday - Afternoon
# 
#   12:00 -> Ending
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic
#       - Dead : broken, doctor, drunk
#       -? : Host, nurse
#
#   Notes : 
#       - 
# --------------------------------------------
label psychic_day3_afternoon:

    call change_time(12,00, "Afternoon", "Sunday")
    
    $ lad_details.add_checkpoint("psychic_day3_afternoon") 

    call black_screen_transition("Amelia Baxter", "Sunday Afternoon")

    $ change_room("tea_room", irisout)

    """
    We waited in the tea room without exchanging any words for a short time.

    Finally, Captain Sinha came back.
    """

    $ play_music('mysterious')

    call common_day3_afternoon_lad_psychic_captain_discussion

    jump work_in_progress
