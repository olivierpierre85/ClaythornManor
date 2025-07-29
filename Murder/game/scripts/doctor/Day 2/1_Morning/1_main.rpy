# --------------------------------------------
#   Doctor
#           
#   Saturday - Morning
#   
#   08:30 -> 11:00
#
#   Music: chill
#
#   Alive: Everyone but Broken
#
#   Notes : 
#       - Generic Lad ?
# --------------------------------------------
label doctor_day2_morning:

    call change_time(8, 0, 'Morning', 'Saturday', hide_minutes=True, chapter='saturday_morning')

    $ current_character.add_checkpoint("doctor_day2_morning")

    call black_screen_transition("Daniel Baldwin", chapters_names[current_chapter])

    $ change_room("bedroom_doctor", irisout)

    """
    Awake and alive.

    Why am I thinking that?

    That is a peculiar way to start the day.

    Never mind, I should get ready.
    """

    if doctor_details.objects.is_unlocked('book_opium'):

        """
        Normally, I would start my day by relaxing the best way I can.

        But today is different.

        I will be different.

        To suppress the urge, I thoroughly wash myself with cold water.

        Then I get ready to join the others for breakfast.
        """
    
    else: 

        """
        Before doing anything else, I prepare for my usual "routine".
        """

        call wait_screen_transition

        """
        That feels better. Now I can face the other guests more relaxed.
        """

    call change_time(9, 00)

    $ change_room('dining_room')

    """
    I take my place at the table. There isn't a lot of people yet.

    Besides the staff, the only person with me is Captain Sinha.
     
    But he is sitting on the other side of the table. So he just nods at me in silence.

    There is nothing to do but fixing myself a plate and eating in silence.

    I observe the other guests as they are slowly coming in.
   
    The next ones to arrive are Rosalind Marsh and Lady Claythorn, entering the room together.

    Lady Claythorn starts talking with Sushil Sinha.

    Rosalind Marsh is sitting next to me.

    I know talking directly across the table is not very polite.

    But there is no one else.
    """

    $ time_left = 30 
    call run_menu(TimedMenu("doctor_day2_morning_nurse", [
        TimedMenuChoice("Talk to Rosalind Marsh", 'doctor_day2_morning_nurse', early_exit=True),
        TimedMenuChoice("Just keep to yourself", 'generic_cancel', early_exit=True),
    ], image_right = "nurse"))

    call change_time(9, 30)
    
    """
    Suddenly I am interrupted by our host.
    """

    call common_day2_morning_host_to_doctor


    jump work_in_progress


label doctor_day2_morning_nurse:

    doctor """
    Good morning, Miss Marsh.
    """

    nurse """
    Good morning, Doctor.
    """

    call nurse_generic

    return