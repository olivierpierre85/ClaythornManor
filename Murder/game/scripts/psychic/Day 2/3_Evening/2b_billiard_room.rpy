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
        # TODO: add interaction with the butler?
        $ psychic_day2_evening_billiard_room_menu = TimedMenu("psychic_day2_evening_billiard_room_menu", [
            TimedMenuChoice("First things first, go to the bar for a drink", 'psychic_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice("Reluctantly talk to Sushil Sinha", 'psychic_day2_evening_billiard_room_captain', keep_alive=True),
            TimedMenuChoice("Politeness be damned, just get out of here", 'generic_cancel', 0, condition="not psychic_details.saved_variables['day2_evening_billiard_room_talk_to_captain']", keep_alive=True, early_exit=True),
            TimedMenuChoice("Leave the room", 'generic_cancel', 0, condition="psychic_details.saved_variables['day2_evening_billiard_room_talk_to_captain']", keep_alive=True, early_exit=True),
        ])

    else:
        # Reset menu
        # $ psychic_day2_evening_billiard_room_menu.early_exit = False

        """
        I am back in the billiard room.
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

    if not psychic_details.saved_variables["day2_evening_billiard_room_talk_to_captain"]:

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

    else:

        captain """
        Miss Baxter, is there anything else?
        """

    call captain_generic

    return


label psychic_day2_evening_nurse_captain:

    captain """
    What do you mean, something weird?
    """

    psychic """
    Well, I am not certain I should tell you, but Miss Marsh is very ill.
    """

    captain """
    Yes, now that you mention it, I noticed she has spent a good deal of time in her room. 

    I simply assumed she was shy.
    """

    psychic """
    Yes, but that is the point. 

    She should be in her room, and she is not. 

    I went in to check, and it was empty.
    """

    captain """
    Really? Do you often wander into other people's rooms when they are absent?
    """

    psychic """
    Don't be absurd, of course not. 

    It was entirely for medical reasons. I feared for her well-being, you see.
    """

    captain """
    If you say so. 

    Still, she could be anywhere. It is not as though she were confined.
    """

    psychic """
    Quite, but there was something else. 

    In her room I found a quantity of silverware — the very same we used at dinner. 

    And far too much to suppose it was simply for her own use.
    """

    captain """
    What are you implying? That she stole it?
    """

    psychic """
    I do not know, perhaps. 

    Do you not think it rather odd?
    """

    captain """
    I must concede, it is. 

    I have read in the papers about people driven to take what is not theirs. 

    An illness, apparently — kleptomania, they call it. 

    I suppose it is possible Miss Marsh is afflicted with it. For it would be folly indeed to risk the reward money by provoking our host. 

    But who can say, without speaking to her first?
    """

    psychic """
    Of course, yet I have no idea where she has gone. 

    She could be anywhere.
    """

    captain """
    True. But if she is prowling about in search of something to steal, there are only so many places she might try.
    """

    psychic """
    Really? Such as where?
    """

    captain """
    As you know, the silver is most likely kept in the butler's pantry. 

    That may be in his own quarters, or perhaps downstairs, in the kitchen or scullery.
    """

    psychic """
    I am not permitted below stairs. Perhaps I should try the butler's room.
    """

    captain """
    You might — but it could be dangerous. I ought to come with you.
    """

    call run_menu(TimedMenu("psychic_day2_evening_nurse_captain", [
            TimedMenuChoice("I suppose there is no other choice", 'psychic_day2_evening_butler_room', 0, early_exit=True),
            TimedMenuChoice("Do not go alone with him", 'psychic_day2_evening_nurse_captain_cancel', 10, early_exit=True),
        ]))

    return


label psychic_day2_evening_nurse_captain_cancel:

    """
    It is a tempting offer, yet I do not feel at ease being alone with him in the attic.
    """

    psychic """
    Thank you, but I do not believe it is necessary. 

    I must have the wrong idea. 

    I am sure Miss Marsh has only gone for a walk to help her sleep. 

    Nothing more.
    """

    captain """
    You are probably right.
    """

    return


label psychic_day2_evening_butler_room:

    psychic """
    Yes, I would like for you to come check with me.

    Would you mind?
    """

    captain """
    Not at all, I don't have much else to do anyway.

    But I really don't think we will find her there.
    """

    $ change_room('attic_hallway', dissolve)

    """
    We don't waste any time and go straight to the attic.
    """

    psychic """
    Here we are. How shall we get in? 

    The door is likely locked.
    """

    captain """
    No matter. The butler gave me a master key earlier, when I had to secure Samuel Manning. 

    I still have it.
    """

    psychic """
    How convenient.
    """

    """
    A master key? Then he can open nearly every door in the house. 

    And yet the butler entrusted it to the captain without hesitation? 
    
    That is not very sensible.
    """

    play sound door_open

    """
    Captain's sinha unlocks the door and we both step in.
    """
    
    $ change_room('bedroom_butler')

    """
    As we suspected, Rosalind Marsh is there — holding a silver candelabra.
    """

    nurse """
    God. 

    What are you doing here?
    """

    captain """
    We might put the same question to you. 

    Though I daresay the answer is plain enough.
    """

    """
    The captain points to the candlestick in her hand.
    """

    nurse """
    This? I only wished for more light in my room. 

    The butler kindly gave me the key so I could take it.
    """

    captain """
    Did he indeed? 

    Strange, for I already hold the only spare key in his possession. 

    Also, why would you lock the door behind you if you have nothing to hide?
    """

    nurse """
    Did I? It must have be by habit and—
    """

    play sound broken_glass

    """
    Something tumbles from her pocket and smashes on the floor. 

    A champagne glass.
    """

    captain """
    Ah, and you needed a crystal glass as well? 

    Planning a little party?
    """

    nurse """
    I was… I was…
    """

    psychic """
    We know very well what you were about, Miss Marsh. 

    I have seen the cutlery in your room. 

    Are even really sick or was it just for show?
    """

    $ play_music('scary', 2)

    """
    Her face alters. 
    
    The flustered look vanishes, replaced by a cold resignation. 

    She sets the candelabra down.
    """
    
    nurse """
    I see. 

    There is no point in pretence any longer. 

    You are right. I was helping myself to whatever I could find. 

    Trinkets, keepsakes, silver, jewels — I have taken them all before. 

    From houses, hospitals, from the old and feeble who never noticed until it was too late. 

    And now from here. 

    It is simply what I do.

    Surprisingly, it's the first time I've been found out. 

    And sadly yes, I am really sick, but not quite as severely as I let you believed.

    It just provides a great cover for my little excursions.
    """

    $ nurse_details.description_hidden.unlock('lie') 

    nurse """
    And now you have put me in a very difficult position.
    """

    """
    Her voice is strained, almost pleading.

    But the captain is not moved.

    His jaw tightens and he reaches into his coat.
    """

    captain """
    I think not. You will come with us downstairs, and we shall settle this properly.
    """

    """
    He draws a revolver and levels it at her.

    He acts with confidence, but I can see his hand shaking.

    Miss Marsh recoils, but does not move towards the door.
    """

    nurse """
    You wouldn't dare.
    """

    captain """
    I said move.
    """

    play sound gun

    """
    The captain fires into the ceiling.

    Plaster rains down upon us.

    Miss Marsh screams — and in the same breath, her hand darts into her pocket.

    She has a gun of her own.
    """

    play sound gun

    """
    The shot catches the captain square in the chest.

    He staggers back, a look of utter disbelief upon his face, and crumples to the floor.
    """

    play sound body_fall

    """
    She stands over him, breathing hard, her hands trembling.

    For a moment she looks as though she might be sick.

    Then she turns to me, the revolver still in her grip.
    """

    nurse """
    He fired at me. You saw it. He fired at me.
    """

    psychic surprised """
    I did. But you needn't make things worse. Put the gun down. We can explain what happened.
    """

    """
    For a fleeting instant, I believe she might listen.

    But then her expression hardens.
    """

    nurse """
    You went through my room. You told the captain. You led him up here.

    None of this would have happened if you had simply left well enough alone.

    But you couldn't, could you? You had to play the clairvoyant.

    Now you will tell them everything, I assume.

    About the silver, the stealing — all of it.

    You will claim that you "saw" it.

    That will give you another "proof" of your power.

    Another reason to take advantage of vulnerable people.
    """

    psychic """
    That is not true. I would not -
    """

    nurse """
    Well it doesn't matter now.

    I can't really take the chance.
    """

    """
    Her hand steadies on the gun.

    There is no madness in her eyes — only a dreadful, weary resolve.

    The look of someone who has already made her choice and cannot turn back.
    """

    nurse """
    I am sorry, Miss Baxter. Truly I am.

    But I cannot go to prison. Not for this.
    """

    play sound gun

    """
    The shot strikes my shoulder and I fall.
    """

    play sound body_fall

    """
    I am grievously wounded — but alive.

    Rosalind Marsh stands over me. Her face is pale, drawn tight with fear.

    She raises the gun once more.
    """

    play sound gun_empty

    """
    A dull click. Empty.

    She lets out a shuddering breath.
    """

    """
    For a long moment she simply stands there, the useless weapon hanging at her side.

    Then, without a word, she sets it down and picks up the candelabra.

    Her hands are still shaking.
    """

    nurse """
    I wish you hadn't made me do this.
    """

    play sound bludgeon

    jump psychic_ending_nurse_thief
