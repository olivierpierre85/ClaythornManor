label psychic_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not psychic_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ psychic_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        Just as I expected, the place is almost empty.

        Besides the butler, I can see only one other person in the room:

        Captain Sinha.

        Good heavens.

        He has spotted me.

        Now, I cannot avoid talking to him without appearing impolite.

        At least the bar is still there.
        """

        # day2_evening_billiard_room_talk_to_captain
        # TODO: add interaction with the butler
        $ psychic_day2_evening_billiard_room_menu = TimedMenu("psychic_day2_evening_billiard_room_menu", [
            TimedMenuChoice("First things first, go to the bar for a drink", 'psychic_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice("Reluctantly talk to Sushil Sinha", 'psychic_day2_evening_billiard_room_captain', keep_alive=True),
            TimedMenuChoice("Politeness be damned, just get out of here", 'generic_cancel', 0, condition="not psychic_details.saved_variables['day2_evening_billiard_room_talk_to_captain']", keep_alive=True, early_exit=True),
            TimedMenuChoice("Leave the room", 'generic_cancel', 0, condition="psychic_details.saved_variables['day2_evening_billiard_room_talk_to_captain']", keep_alive=True, early_exit=True),
        ])

    else:
        # Reset menu
        $ psychic_day2_evening_billiard_room_menu.early_exit = False

        """
        I am back in the Billiard Room.
        """

    call run_menu(psychic_day2_evening_billiard_room_menu)

    return

label psychic_day2_evening_billiard_room_bar:

    """
    I'll have a glass of sherry, as it's the only decent drink I can see.
    """

    if not psychic_details.saved_variables['day2_evening_billiard_room_talk_to_captain']:
    
        """
        Captain Sinha has looked up from his book and is now staring at me.

        I can't very well ignore him now.
        """

    return


label psychic_day2_evening_billiard_room_captain:

    $ psychic_details.saved_variables["day2_evening_billiard_room_talk_to_captain"] = True

    """
    I suppose I have no choice but to speak with him, at least for a little while.

    Approaching him, I notice his expression is quite grave. 

    He looks at me with a piercing gaze, as if to assess whether I am a threat.
    
    I sit down beside him, acutely aware of the tension between us.
    """

    captain """
    Miss Baxter.

    I wouldn't have thought you'd come here.
    """

    psychic """
    I wasn't sure I would to be honest.

    The atmosphere of this house has become quite sinister.

    But the idea of waiting alone in my room is not very reassuring either, so here I am.
    """

    captain """
    Yes, sorry that there isn't a larger company here.

    Everyone else seems to have been too scared to come.
    """

    psychic """
    Oh that's quite alright.

    But I am afraid I shall not be staying long in any case.
    """

    # captain """
    # I hope you are not afraid of me?
    # """

    call captain_generic

    return


label psychic_day2_evening_nurse_captain:

    captain """
    What do you mean something weird?
    """

    psychic """
    Well, I am not sure I should tell you that, but Miss Marsh is very ill.
    """

    captain """
    Yes, now that you mention it, I noticed she spent a lot of time in her room.

    I just assumed she was shy.
    """

    psychic """
    Yes but that is the thing.

    She should be in her room, but she isn't.

    I just went in to check and her room is empty.
    """

    captain """
    Really? Do you often visit other people rooms when they are not there?
    """

    psychic """
    Don't be absurd, of course not.

    It was purely for medical reasons, I feared for her well-being you see.
    """

    captain """
    If you say so.

    But she could be anywhere, it's not like she couldn't get out at all.
    """

    psychic """
    Right, but there is something else. 

    In her room, there was a stash of silverware. The same we used at dinner.

    And there was too many to assume it was just for her benefit.
    """

    captain """
    What are you saying? That she stole them?
    """

    psychic """
    I don't know, maybe.

    Don't you think it's odd?
    """

    captain """
    I must concede, it is a bit.

    I've read in the paper about people who are compelled to take things that aren't theirs.

    It's a disease apparently, called kleptomania.

    I guess it's a possibility Miss Marsh is afflicted by it.

    Because it wouldn't make sense to risk losing the reward money by angering our host.

    But I don't know, there is no way of knowing really without talking to her first.
    """

    psychic """
    Of course, but I don't know where she is now.

    She could be anywhere.
    """

    captain """
    That is correct, but if she is roaming the Manor looking for something to steal, there are obvious places she could look.
    """

    psychic """
    Really? Like where?
    """

    captain """
    As you certainly know, the silverware is probably stored in the butler's pantry.

    It could be either, in his room, or somewhere downstairs, like in the kitchen or the scullery.
    """

    psychic """
    I don't think I am allowed downstairs, so maybe I should go check the butler's room.
    """

    captain """
    You could try, but it could be dangerous, I should come with you.
    """

    call run_menu(TimedMenu("psychic_day2_evening_nurse_captain", [
            TimedMenuChoice("I guess there is no other choice", 'psychic_day2_evening_butler_room', 0, early_exit=True),
            TimedMenuChoice("Don't go alone with him", 'psychic_day2_evening_nurse_captain_cancel', 10, early_exit=True),
        ]))

    return


label psychic_day2_evening_nurse_captain_cancel:

    """
    It's an interesting offer, but I don't feel comfortable being alone with him in the attic.
    """

    psychic """
    Thank you but I don't think I need to do that.

    I probably have the wrong idea.

    I am sure Rosalind Marsh just went for a walk to help her sleep.

    Nothing more.
    """

    captain """
    You are probably right.
    """

    return


label psychic_day2_evening_butler_room:

    $ change_room('attic_hallway')

    psychic """
    Here we are, how will we enter?

    The room is probably locked.
    """

    captain """
    No worries, the butler gave me a master key to lock Samuel Manning earlier.

    I still have it with me.
    """

    psychic """
    Oh, how convenient.
    """

    """
    He has a master key?

    Which means he has access to almost every room in this place.

    How come the butler just gave it to him?
    """

    play sound door_open

    captain """
    The key won't be necessary, the door is not locked.

    So someone is probably inside.
    """

    psychic """
    Heavens.
    """

    captain """
    Hello, is there someone here?
    """
    
    $ change_room('bedroom_butler')

    """
    Without waiting for an answer, we quickly enter the room.

    And as I predicted, Rosalind Marsh is there.

    Holding a silver candelabra.
    """

    nurse """
    God.

    What are you doing here?
    """


    captain """
    We could ask you the same question.

    But I don't think we need to, it's pretty obvious why you are here.
    """

    """
    The captain points at the candlestick in the nurse's hands.
    """

    nurse """
    That?

    I just needed more light in my room.

    The butler was kind enough to gave me key to take this with me.
    """

    captain """
    Really? 

    That is strange since I already have the only spare key he had.

    I don't think likely that he would give you his only key.

    He would have come with you at least.
    """

    nurse """
    But he couldn't.

    He was too busy to come with me and...
    """

    play sound broken_glass

    """
    Something fell from her pocket.

    A champagne glass.
    """

    captain """
    You also needed a crystal glass I see.

    Were you planning a party?
    """

    nurse """
    Well I was, I was ...
    """

    captain """
    We know very well what you were doing miss Marsh.

    We know about the cutlery in your room as well.

    And I am sure it's not the first time you've been doing this.
    """


    $ play_music('scary', 2)

    """
    Her expression changes.

    She no longer looks embarrassed. Instead, a quiet resignation forms on her face.

    She puts down the candelabra.
    """
    
    nurse """
    I see.

    There is no point in pretending anymore.

    I was trying to make the most of this place.

    I found many valuable things roaming this house.

    I am getting good at it, because as you said, I have been doing this for a long time.

    In hospitals, from the elderly I cared for, and in many other places I can't even remember.

    Surprisingly, it's the first time I've been found out. 
    """

    $ nurse_details.description_hidden.unlock('lie') 

    nurse """
    That means you're leaving me no choice.
    """

    """
    She then picks up something quickly from her pocket.

    A gun.

    I don't have time to realize what's happening.

    Sushil Sinha plunges his own hand in his pocket.

    But he is too late.
    """

    play sound gun

    """
    Rosalind Marsh shot him right in the face.
    """

    play sound body_fall

    """
    He immediately falls down next to me.

    She then turns her gun towards me.
    """

    nurse """
    I am sorry Miss Baxter, but I can't have you talk to the police.
    """

    psychic scared """
    I don't understand, why would you do such a thing?

    We were about to receive way more money that those objects are worth.
    """

    nurse """
    Ah!

    You really believe that?

    That you were about to get rich?

    How naive of you.
    """

    psychic """
    What do you mean? What makes you say such a thing? I ...
    """

    nurse """
    I am sorry, but I don't need to explain myself to you.

    Goodbye Miss Baxter.
    """

    play sound gun

    """
    She shot at me.

    I feel a sharp pain in my shoulder, 
    
    and fall to the ground.
    """

    play sound body_fall

    """
    I am badly wounded.

    But I am still alive.

    Rosalind Marsh approaches me, gun in hand.
    """

    nurse """
    Sorry I missed your head.

    Let me correct that.
    """

    play sound gun_empty

    """
    She tries to shoot me again.

    But nothing came out. She must be out of bullets.
    """

    nurse """
    Well that's my luck.

    Don't move.
    """

    """
    She turns around.

    I gather my remaining strength to crawl away from her.

    But I haven't time to move far enough.
    
    I see her coming back at me.

    Her gaze is empty.

    She is holding the candelabra in her hands.

    Then, she raises it above her head.
    """

    jump psychic_ending_nurse_thief