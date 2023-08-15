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
#       - Generic psychic, 120 minutes,?TODO too long?
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

    # TODO play dramatic music
    psychic surprised """
    Oh my God! What happened!?

    Is that Doctor Baldwin? Is he injured?

    Oh no! Is he... dead?
    """

    captain """
    I'm sorry, dear, but he is.
    """

    psychic """
    But... what happened?
    """

    captain """
    It was an accident. 
    """

    drunk sad """
    I swear it was! I have no idea how I could have hit him.
    
    I was aiming at a rabbit. I didn't even see him.
    """

    """
    Everyone turns to him.
    """
        
    psychic angry """
    You fool! You were probably too drunk, and that's why you hit him.

    You could barely walk this morning. Who gave you a gun?
    """

    captain """
    Please, there's no need to point fingers now. It's done.

    The police will handle it.

    Speaking of which, has anyone from the city arrived yet?
    """

    nurse """
    No, not yet.

    We're still waiting for them.
    """

    captain """
    We should tell them to hurry.

    Lady Claythorn, where's the phone?
    """

    host """
    I'll handle it.
    """

    """
    She leaves the group, with the butler following closely behind.

    The room falls silent.

    Most eyes are on Sam Manning, filled with disdain.

    Then, the hostess returns.
    """

    host """
    I just spoke with the police. They aren't coming today.
    """

    captain """
    What!? Why not?
    """

    host """
    They were on their way but encountered a huge tree blocking the road.
    
    They couldn't get past it.
    
    They said they'll be back tomorrow with assistance.
    """

    psychic """
    But... what are we going to do with him until then?
    """

    captain """
    We'll move him to his bed for now. 
    
    It's the best we can do under the circumstances.

    Anyone willing to help?
    """

    lad """
    I will.
    """

    $ change_room("doctor_room")

    """
    We carried Doctor Baldwin to his room and laid him on his bed.

    Sushil then covered him with a blanket.
    """

    captain """
    It's best this way for now.

    I want to keep an eye on Samuel Manning.
    """

    """
    I nod in agreement.
    """

    captain """
    You should change before rejoining us.
    """

    """
    I glance at my clothes.

    They're stained with blood.

    Luckily, they aren't mine. 
    
    But I should still change them.
    """
    
    call lad_day2_afternoon_bedroom

    jump lad_day2_evening