label tutorial_clock:

    if not seen_tutorial_clock:

        tutorial """
        Wait, don't you hear something ticking?

        If you haven't noticed it yet, look at the clock in the upper-left corner.
        
        There, you can see the current time, as well as the day.

        This helpful tool will move as the story progresses, for example, when you start a new chapter of this story.

        Also, when you are faced with multiple choices, each action will take a different amount of time.

        And each scene has a limited duration.

        This means you won't always have the opportunity to explore every option on a list.

        So make every choice count.
        """

        $ seen_tutorial_clock = True

    return


label tutorial_description_hidden:

    tutorial """
    Congratulations on discovering your first piece of information about a character! 
    
    Learning about characters is crucial in this game as it involves two types of information: essential and trivial. 
    
    To unlock a new playable character, it is necessary to learn all the essential facts about them. 
    
    Once you have acquired this knowledge, you will be able to restart the story from their perspective. 
    
    While conversing with a character can unlock certain information, some facts can only be revealed at specific moments in the story. 
    
    The "Characters" menu gives you an estimation of how much essential information has been unlocked.
    """

    return


label tutorial_map:

    tutorial """
    Well done on finding information about the manor! 
    
    As a result, additional details have been added to the manor map to assist you in navigating the house. 

    You can access this information by navigating to the "Map" menu.
    """

    return

label tutorial_unlock_character:
    
    tutorial """
    You've unlocked a new character!

    Now, you can begin the narrative through their point a view.

    Each character possesses a distinct story, persona, and background.

    This individuality may grant you access to specific choices unavailable to others.

    Utilize the characters' full potential to unravel the mystery of this weekend.
    """

    return

label tutorial_timeline:
    
    tutorial """
    You now have to restart the story. 
    
    However, there is no need to worry as you can use the skip button located at the bottom right of the screen to skip over any previously encountered dialogues. 
    
    Furthermore, you now have access to the \"Progress\" menu, which provides you with an overview of each character's past progress. 
    
    It is possible to restart the story from various checkpoints that occurred during the weekend's events. 
    
    Please be cautious as these checkpoints save the previous choices you have made. 
    
    Therefore, it may be necessary to start from an earlier point to unlock new story paths.
    """

    return