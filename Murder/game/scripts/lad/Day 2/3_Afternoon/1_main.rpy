# --------------------------------------------
#   Lad
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
label lad_day2_afternoon:

    call change_time(15,00, 'Afternoon', 'Saturday')

    $ lad_details.add_checkpoint("lad_day2_afternoon") 
    
    call black_screen_transition("Ted Harring", "Saturday Afternoon")

    $ change_room("great_hall", irisout)
    
    if lad_details.saved_variables["day2_hunt"]:

        """
        Everything happened so quickly; it's all a blur.

        After the screaming and crying in the woods, Captain Sinha took charge.

        He had us carry the doctor on a makeshift stretcher.
 
        It took a while, but we eventually reached the mansion.
        """        

    else:
        
        """
        I watch the hunting party enter the house.

        Amelia and Rosalind are already there, near the entrance.

        Lady Claythorn enters first, looking visibly shocked.

        Then the butler and footman follow.

        They're dragging someone on a makeshift stretcher.
        """

    $ play_music('sad')

    call common_day2_afternoon_entrance_dialog

    $ change_room("bedroom_doctor")

    """
    We carried Doctor Baldwin to his room and laid him on his bed.

    Sushil then covered him with a blanket.
    """

    captain """
    It's the best we can do at the moment.

    We shouldn't linger here.

    I want to keep an eye on Samuel Manning.
    """

    lad """
    Of course.
    """

    captain """
    Also Mister Harring, you might want to change before rejoining us.
    """

    """
    I glance at my clothes.

    They're stained with blood.
    
    He is right, I can't go back downstairs looking like this.
    """
    
    call lad_day2_afternoon_bedroom

    jump lad_day2_evening