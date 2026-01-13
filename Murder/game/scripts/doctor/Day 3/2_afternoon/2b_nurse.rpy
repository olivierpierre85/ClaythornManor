# TODO rewrite everything BAD AI JOB
label doctor_day3_afternoon_nurse:

# Now it's the afteroon.
    call change_time(12, 00, "Afternoon", "Sunday")

    # Captain Sinha leaves the manor alone
    
    """
    Eventually, we see movement again.
    
    Captain Sinha emerges from the tea room.
    
    He is alone.
    
    He heads towards the entrance hall and then out the front door.
    """

    nurse """
    He is leaving.
    
    Now is our chance.
    """

    # So you and the nurse approach Ted Harring and Amelia Baxter.

    """
    We make our way down to the tea room.
    """

    $ change_room("tea_room")

    """
    Ted Harring and Amelia Baxter are sitting there, looking anxious.
    
    They jump when we enter.
    """

    lad """
    Doctor! Miss Marsh!
    
    Where have you been? We were worried.
    """

    doctor """
    We... were safe.
    """

    psychic """
    Safe?
    
    Well, at least you are here now.
    """

    """
    We sit down with them.
    
    The atmosphere is heavy.
    """
    
    # Then the end is close to the ending lad_day3_afternoon_toilet, but with you (doctor balwin) collapsing

    """
    But as I sit, a wave of dizziness hits me.
    
    The room seems to tilt.
    """

    doctor """
    I...
    """

    """
    I try to stand up, but my legs refuse to support me.
    """

    lad """
    Doctor? Are you alright?
    """

    """
    I collapse back into the chair, then slide to the floor.
    """

    nurse """
    Doctor!
    """

    """
    My vision blurs. 
    
    I can hear voices, but they sound like they are coming from underwater.
    """

    doctor """
    Poison...
    """

    """
    It is the only explanation.
    
    But how? I haven't eaten anything...
    
    Unless...
    
    The water in the room? Or something earlier?
    """
    
    $ doctor_details.endings.unlock('poisoned')
    $ doctor_details.add_ending_checkpoint(ending=doctor_details.endings.get_item('poisoned'))

    call death_screen_transition

    """
    My breath catches in my throat.
    
    Darkness closes in.
    
    I will never know the truth.
    """

    jump ending_generic