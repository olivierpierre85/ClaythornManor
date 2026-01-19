label common_day3_afternoon_lad_psychic_stay:

    $ stop_music(2)

    psychic """
    Well, there's no point in waiting around doing nothing.

    We haven't eaten since yesterday.

    I could check the kitchen to see if there's anything I can prepare.
    """

    lad """
    Okay, I'll come with you.
    """    

    $ change_room('basement_stairs', dissolve)

    if current_character.text_id == "lad":

        """
        We are heading to the lower floor when we hear a shout.
        """

    else:

        """
        On our way to the basement, I hear a familiar voice.
        """   

    $ play_music('mysterious', 2)
    
    nurse """
    Hello!
    """

    pause 1.0

    nurse """
    Is there someone here?
    """

    psychic """
    Oh my God, Miss Marsh, you're here!
    """

    nurse """
    Of course I am here. Why do you look so surprised?
    
    I'm afraid I overslept. I don't feel quite like myself today.

    When I woke up, I went to check the dining room but found it empty.

    I wandered in the house for a while but I didn't see anyone until I met you.

    Where is everybody?
    """

    psychic """
    Oh my dear, we don't know.
    """

    if current_character.text_id == "lad":

        """
        We updated her on what happened since this morning.

        When we had finished telling her the story, she remained relatively calm, considering the situation.
        """

    else:
        # TODO: Add more details or elaborate, since the previous explanation was brief?
        """
        We explained the situation to her as best we could.

        She doesn't appear very alarmed by it.
        
        I am finding that peculiar.
        """

    nurse """
    Poor Mr Manning, what a terrible fate.

    And what horror that must have been for you, my dear.

    Are you all right?
    """

    psychic """
    I am better now.

    Captain Sinha should be back with help soon, so I'll be fine if I can keep my mind occupied until then.

    Speaking of which, we were heading to the kitchen to see if we can prepare some sort of meal.
    """

    nurse """
    Right, it's a good idea. We might as well keep ourselves busy.
    """

    if current_character.text_id == "lad":
        """
        And just like that, we go downstairs to the kitchen.
        """
    elif current_character.text_id == "psychic":
        """
        So we go downstairs.
        """

    $ change_room('kitchen', dissolve)

    $ stop_music(2)

    """
    We look around for something to eat.
    """

    psychic """
    There isn't much.

    But I think we can manage a light luncheon if you're not picky.
    """

    nurse """
    I'll help you.
    """

    if current_character.text_id == "lad":
        """
        I offer to help as well, but they decline.
        
        So, I take a seat while they prepare the food.   

        That's probably for the best.

        I couldn't do much to help anyway.
        """
        
        $ lad_details.description_hidden.unlock('cook') 

    elif current_character.text_id == "psychic":
        """
        Mr Harring is nice enough to offer his help.

        But I don't think he has much experience in this department.

        So we decide it's best if he doesn't get involved.
        """

    pause 1.0

    $ change_room('dining_room', dissolve)

    if current_character.text_id == "lad":
        """
        When everything is ready, I carry the plates to the dining room.

        I set them at our usual places.

        Then I leave the dining room.
        """
    elif current_character.text_id == "psychic":
        """
        When the food is ready, we go to the dining room to eat.

        Ted Harring sets the table and then tries to leave.
        """


    psychic """
    Where are you going, Mr Harring?

    It's better if we stick together at all times.
    """

    lad """
    I understand, but there's something I need to do alone.

    We haven't had a moment apart the entire day and...
    """

    psychic """
    Say no more, I understand.

    I'm in the same situation.

    What about you, Miss Marsh?
    """

    nurse """
    Oh, I'm fine, thank you.

    You both go, I'll finish preparing the table.
    """

    psychic """
    Very well.

    Let's meet back here in a few minutes then.
    """

    lad """
    Of course.
    """

    pause 1.0

    return


label common_day3_afternoon_lad_falls:

    $ stop_music()

    lad surprised """
    What's happening?

    Why am I...
    """

    if current_character.text_id == "lad":
        """
        I try to speak further, but no words come out.
        """
    elif current_character.text_id == "psychic":
        """
        He is unable to say another word before he collapses to the floor.
        """

    play sound body_fall

    return