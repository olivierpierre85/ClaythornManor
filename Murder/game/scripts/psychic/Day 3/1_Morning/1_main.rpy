# --------------------------------------------
#   Psychic
#           
#   Sunday - Morning
# 
#   7:30 / 9:30 -> 12:00
#
#   Music: mysterious
#
#   Position
#       - House: lad, captain, psychic
#       - Dead : broken, doctor, drunk
#       -? : Host, nurse
#
#   Notes : 
#       - ???
# --------------------------------------------
label psychic_day3_morning:

    $ psychic_details.add_checkpoint("psychic_day3_morning") 

    call black_screen_transition("Amelia Baxter", "Sunday Morning")

    call change_time(7, 0, "Morning", "Sunday", hide_minutes=True)

    $ change_room('bedroom_psychic', irisout)

    """
    Unsurprisingly, I slept terribly last night.

    At least it's the last day. All of this will be over soon.
    """

    if psychic_details.important_choices.is_unlocked('visit_lad'):
        
        """
        Now I need to get my things ready and head to Ted Harring.
        """

    else:

        """
        Even though I didn't had a talk with Ted Harring last night, I still feel seeing him now is.
        """


    $ change_room('bedrooms_hallway', dissolve)

    """
    On my way to Ted's, the emptiness of the Manor hits me.
    """

    play sound door_knock

    """
    He is not responding.

    I hope he is well.
    """

    play sound door_knock

    psychic """
    Mr Harring, are you there?
    """

    if psychic_details.important_choices.is_unlocked('visit_lad'):

        call common_day3_morning_lad_psychic_journey
    
    else:
        
        call psychic_day3_morning_has_not_visited_lad


    """
    And we started to look for others in the manor,

    inspecting every room.

    I let him choose where we were going,

    even though his choices didn't always make much sense.
    """

    $ change_room('tea_room', irisout)

    call change_time(11,00)

    """
    After a long search, we took a break in the tea room.

    We rested there until we heard a familiar voice.
    """

    call common_day3_morning_lad_psychic_tea_room_1

    call common_day3_morning_lad_psychic_tea_room_2

    call common_day3_morning_lad_psychic_captain_death_manning

    """
    I sat there quietly, pondering what had happened, what I should do next.
    """

    pause 1.0

    """
    After some time, they came back.
    """

    call common_day3_morning_lad_psychic_captain_deaths_end

    pause 1.0

    $ stop_music()

    jump psychic_day3_afternoon


label psychic_day3_morning_has_not_visited_lad:

    lad """
    I'm coming!
    """

    """
    Finally, I was getting worried.

    He opens the door for me and I enter.
    """

    $ change_room('bedroom_lad')

    $ play_music('mysterious', 2)

    psychic """
    Mister Haring, I am sorry to disturb you but something strange is happening.
    """

    lad """
    What do you mean?
    """

    psychic """
    I haven't seen any staff members on my way here.

    At this hour, they should be busy with lighting fires, cleaning and setting up breakfast.

    Yet, I neither saw nor heard anyone.

    It's as silent as a graveyard in here.
    """

    lad """
    Are you sure it's not just because it's so early?
    """

    psychic """
    I'm certain.

    I was up at the same time yesterday, and the house was bustling with activity.

    Something's not right, I assure you.
    """

    lad """
    Okay, if you say so. 
    """

    """
    He paused for a second there, he must have realised it's serious.
    """

    lad """
    What do you propose we do then?
    """

    psychic """
    I am not sure, but I think we should start by searching the Manor to try to understand what's happening.
    """

    lad """
    Alright, let's investigate then.
    """

    return