# --------------------------------------------
#   Psychic
#           
#   Saturday - Afternoon
# 
#   15:00 -> 18:30
#
#   Music: sad
#
#   Position
#       - House: Everyone else
#       - Dead : broken, doctor
#
#   Notes : 
#       - 
# --------------------------------------------
label psychic_day2_afternoon:

    call change_time(15,00, 'Afternoon', 'Saturday')

    $ psychic_details.add_checkpoint("psychic_day2_afternoon") 
    
    call black_screen_transition("Amelia Baxter", "Saturday Afternoon")

    $ change_room("great_hall", irisout)
    
    """
    I observe the hunting party as they make their way into the house.

    Rosalind was already by the entrance.

    Lady Claythorn steps through the doorway first, her expression one of sheer disbelief.

    Following close behind are the butler and footman.

    They're carefully carrying someone on an improvised stretcher.
    """

    $ play_music('sad')

    call common_day2_afternoon_entrance_dialog

    """
    I watch Captain Sinha and Ted Harring carrying doctor Baldwin to his room.
    """

    # TODO discussion about samuel Manning 
    call common_day2_afternoon_samuel_manning_discussion



    # AFTER discussion choice to either talk to ted harring OR leave him be????

    # jump psychic_day2_evening