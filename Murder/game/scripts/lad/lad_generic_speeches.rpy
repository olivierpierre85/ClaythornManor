# Shared With PSYCHIC
label day2_breakfast_lad_psychic:

    psychic """
    Hello, Mister Harring. How are you?
    """

    lad """
    Very well, thank you.
    """

    psychic """
    I was wondering if everyone would join us on time.
        
    There are still a few people missing.

    For instance, I don't think we'll see Mister Manning anytime soon.

    He was so drunk yesterday that I wouldn't be surprised if he doesn't show up before noon.
    """

    if current_character == lad_details:
        
        """
        Suddenly, Samuel Manning enters the room.

        He stumbles to the buffet table and picks up a plate, visibly shaking.
        """

    else:

        """
        Right after saying those words, Samuel Manning steps into the room.

        Displaying evident unease, he makes his way to the buffet and, with trembling hands, selects a plate.

        He appears to still be drunk, or at least seriously hungover.
        """

    psychic angry """
    Well, I spoke too soon. Here he is. And in such a state.

    How dreadful.
    """

    if current_character == lad_details:

        """
        At the same moment, the butler rushes into the room.
            
        He goes to Lady Claythorn and whispers something in her ear.

        I can tell it's not good news.

        She looks shocked and worried.

        She stands up and walks in my direction, then stops in front of the doctor.
        """

    else:

        """
        While I am watching Samuel Manning, the butler enters and discreetly shares a message with Lady Claythorn.
        
        Her alarmed expression indicates the gravity of the news. 
        
        Rising, she approaches, pausing only when she reaches the doctor.
        """
    
    host """
    Doctor Baldwin, I'm sorry to interrupt your breakfast, but would you mind coming with me?

    We need your assistance.
    """

    """
    Without hesitation, Daniel Baldwin stands up.
    """

    doctor """
    Of course, I'll follow you.
    """

    return