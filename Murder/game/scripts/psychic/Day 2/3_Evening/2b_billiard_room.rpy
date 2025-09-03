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

    $ change_room('attic_hallway')

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

    And yet he entrusted it to the captain without hesitation? Curious.
    """

    play sound door_open

    captain """
    As it happens, we shall not need it. The door is already unlocked. 

    Someone must be inside.
    """

    psychic """
    Heavens.
    """

    captain """
    Hello? Is someone here?
    """
    
    $ change_room('bedroom_butler')

    """
    Without waiting for an answer, we step into the room. 

    As I feared, Rosalind Marsh is there — holding a silver candelabra.
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

    It seems unlikely he would part with his own. He would at least have accompanied you.
    """

    nurse """
    But he could not. He was too occupied and—
    """

    play sound broken_glass

    """
    Something tumbles from her pocket and smashes on the floor. 

    A champagne glass.
    """

    captain """
    Ah, and you required a crystal glass as well? 

    Planning a little party?
    """

    nurse """
    I was… I was…
    """

    captain """
    We know very well what you were about, Miss Marsh. 

    We have seen the cutlery in your room. 

    And I am sure it's not the first time you've been doing something of the sort.
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

    I was helping myself to whatever I could find. 

    Trinkets, keepsakes, silver, jewels — I have taken them all before. 

    From houses, hospitals, from the old and feeble who never noticed until it was too late. 

    And now from here. 

    It is simply what I do.

    Surprisingly, it's the first time I've been found out. 
    """

    $ nurse_details.description_hidden.unlock('lie') 

    nurse """
    Which means you leave me no choice.
    """

    """
    She draws something swiftly from her pocket — a revolver. 

    I scarcely comprehend before Sushil thrusts his hand into his coat. 

    But he is too late.
    """

    play sound gun

    """
    The shot cracks through the room. 

    The bullet strikes him full in the face. 

    He drops at once beside me.
    """

    play sound body_fall

    """
    She turns the revolver upon me.
    """

    nurse """
    I am sorry, Miss Baxter, but I cannot have you telling the police.
    """

    psychic surprised """
    I do not understand — why do such a thing? 

    We were about to receive far more money than these trifles are worth.
    """

    nurse """
    Ha! 

    You truly believed that? That we were about to get rich? 

    How very naive.
    """

    psychic """
    What do you mean? What makes you say so? I—
    """

    nurse """
    I am sorry. I have no need to explain myself. 

    Goodbye, Miss Baxter.
    """

    play sound gun

    """
    She fires. 

    A searing pain tears through my shoulder and I fall.
    """

    play sound body_fall

    """
    I am grievously wounded — but alive. 

    Rosalind Marsh advances, revolver still in hand.
    """

    nurse """
    A pity I missed your head. 

    Let me correct that.
    """

    play sound gun_empty

    """
    She pulls the trigger. 

    A dull click. Empty. 
    """

    nurse """
    Well, that is my luck. 

    Do not move.
    """

    """
    She turns away. I summon what strength I can to crawl across the floor. 

    But I cannot reach far before she returns. 

    Her gaze is vacant. 

    She holds the candelabra,
    raises it high above her head...
    """

    play sound bludgeon

    jump psychic_ending_nurse_thief
