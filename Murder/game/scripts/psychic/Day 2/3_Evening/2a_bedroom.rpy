label psychic_day2_evening_bedroom:
    
    $ change_room('bedroom_psychic', dissolve)

    call change_time(18, 00)

    """
    I return to my room to change and collect my thoughts.

    So much has happened today, it is overwhelming.

    I use this brief respite to compose myself.

    There is little time before dinner, so I could wait here,

    or take the opportunity to have a private word with someone.

    I do not think it would be wise to approach Captain Sinha,

    nor Lady Claythorn.
    """

    if psychic_details.observations.is_unlocked('nurse_sick'):

        """
        And I should let Rosalind Marsh rest.

        However, I do not believe I am taking too much of a risk by talking with Ted Harring.
        """

    else:

        """
        However, I do not believe I am taking too much of a risk by talking with Rosalind Marsh or Ted Harring.
        """

    $ time_left = 1
    call run_menu(TimedMenu("psychic_day2_evening_bedroom", [
            TimedMenuChoice('Try to talk to Rosalind Marsh', 'psychic_day2_evening_bedroom_nurse_blood', 0, early_exit=True, condition = "not psychic_details.observations.is_unlocked('nurse_sick')"),
            TimedMenuChoice('Try to talk to Ted Harring', 'psychic_day2_evening_lad_discussion', 0, early_exit=True),
            TimedMenuChoice('Just have a quick nap instead', 'psychic_day2_evening_cancel_nap', 0, early_exit=True),
            # Talk with host anyway??? Intuition things are not going according to plan.
        ])
    )

    return


label psychic_day2_evening_bedroom_nurse_blood:

    # Second chance to check Rosalind Marsh illness
    call psychic_day2_no_hunt_bedroom_nurse_blood

    $ change_room('bedroom_psychic')

    """
    I return to my room to rest.

    But very quickly, the gong rings.
    """

    call change_time(18,30)

    play sound dinner_gong

    """
    I guess I'd better join the others downstairs.
    """    

    return


label psychic_day2_evening_lad_discussion:

    $ change_room("bedrooms_hallway")

    call common_day2_evening_lad_psychic_discussion_0

    $ psychic_details.important_choices.unlock('visit_lad')

    return

# NOt used because => If barricaded he can't visit her afterwards, so he is absent
# label psychic_day2_evening_lad_bedroom:

#     $ change_room("bedrooms_hallway")

#     play sound door_knock

#     psychic """
#     Mister Harring, are you there?
#     """

#     lad """
#     Yes, what is it, Miss Baxter?
#     """

#     psychic """
#     Nothing in particular.

#     I only wished to make sure you were safe.
#     """

#     lad """
#     I am.

#     I've even just pushed some furniture up against the door, which means I can't let you in just now.
#     """

#     psychic """
#     No matter.

#     You did the right thing.
#     """

#     psychic """
#     I'll say good night then.
#     """

#     lad """
#     Good night, Miss Baxter.
#     """

#     return



label psychic_day2_evening_cancel_nap:

    """
    That's about all I can manage right now.

    I should rest for a bit.
    """

    call wait_screen_transition()

    call change_time(18,30)    

    play sound dinner_gong

    """
    Right on time, the dinner gong rings.
    
    I guess I should join the others downstairs.
    """

    return


label psychic_day2_evening_bedroom_nurse_gone:

    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock gently on the door.

    but there is no answer.
    """

    if psychic_details.observations.is_unlocked('nurse_sick'):

        """
        She is probably resting.

        After all, she said it herself. At night she takes her medicine then falls asleep.

        But I don't know.

        She looked in dreadful shape when I last spoke with her.

        Perhaps her condition has worsened.

        Should I make certain she is all right?
        """

        call run_menu(TimedMenu("psychic_day2_evening_bedroom_nurse_gone", [
                TimedMenuChoice("Make sure she is still alive{{observation}}", 'psychic_day2_evening_bedroom_nurse_gone_enter', 20, early_exit=True),
                TimedMenuChoice("Don't be so nosy", 'psychic_day2_evening_bedroom_nurse_gone_do_not_enter', 10, early_exit=True),
            ]))

    else: 

        call psychic_day2_evening_bedroom_nurse_gone_do_not_enter

    return


label psychic_day2_evening_bedroom_nurse_gone_enter:

    """
    I know it's very impolite, but this is for her own good.

    I try to open the door.

    It is unlocked.
    """

    $ change_room("bedroom_nurse")

    """
    But there is no one in here.

    Where is Miss Marsh?

    She seemed so sick earlier.

    I look around the room.

    It is tidy, clean and well-organized.

    At first I don't notice anything out of the ordinary, but as I pry deeper I see something weird next to her bedstand.

    Is that silverware?

    What is it doing here?

    Perhaps she was planning to eat in her room and changed her mind at the last minute.

    But there is more then one set.

    Unless she wanted to entertain a few guests, there is no reason for her to have that many utensils in her room.

    I am not sure what to make of that.
    """
    
    $ psychic_details.observations.unlock('silverware')

    return


label psychic_day2_evening_bedroom_nurse_gone_do_not_enter:

    """
    She is probably just asleep. 
    
    There is no reason to wake her up.
    """
    
    return