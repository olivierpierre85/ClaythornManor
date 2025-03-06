label tutorial_clock:

    $ stop_music(2)

    if not seen_tutorial_clock:

        tutorial """
        Wait, don't you hear something ticking?

        If you haven't noticed it yet, look at the clock in the upper-left corner.
        
        There, you can see the current time, as well as the day.

        This helpful tool will move as the story progresses, for example, when you start a new chapter of this adventure.

        Also, when you are faced with multiple choices, each action will take a different amount of time.

        And each scene has a limited duration.

        This means you won't always have the opportunity to explore every option on a list.

        So make every choice count.
        """

        $ seen_tutorial_clock = True
    
    $ play_music('PREVIOUS')

    return


label tutorial_description_hidden:

    $ stop_music(2)

    tutorial """
    Congratulations on discovering your first piece of information about a character! 
    
    Learning about characters is crucial in this game. You can find two types of information: essential and trivial. 
    
    To unlock a new playable character, it is necessary to learn all the essential facts about them. 
    
    Once you have acquired this knowledge, you will be able to restart the story from their perspective. 
    
    While conversing with a character can unlock certain information, some facts can only be revealed at specific moments in the story. 
    
    The "Characters" menu is now accessible.
    
    It gives you an estimation of how much essential information has been unlocked, as well as a complete description of a character.

    At the beginning, the descriptions are riddled with holes. It's up to you to fill those holes to reveal someone's true story.

    Check out for yourself.
    """

    $ _game_menu_screen = "characters"
    $ renpy.call_in_new_context("_game_menu", "navigation")

    $ play_music('PREVIOUS')

    return


label tutorial_map:

    $ stop_music(2)

    tutorial """
    Well done, you just found new information about the Manor. 
    
    As a result, additional details have been added to the Manor map to assist you in navigating the house. 

    You can access this information by navigating to the "Map" menu here.
    """

    $ _game_menu_screen = "manor_map"
    $ renpy.call_in_new_context("_game_menu", "navigation")

    $ play_music('PREVIOUS')

    return

label tutorial_intuition:

    $ stop_music(2)

    tutorial """
    You just got your first "Intuition".

    An "Intuition" is a powerful tool.

    Some say that when a death is so strong, that it will leave a mark that can be felt throughout planes of existence.

    Other say it's the ghost of a different timeline who came back to try to warn you.

    In any case, it means that you will now receive a warning somewhere in this adventure. 
    
    This will let you change the course of the story in a way that you couldn't before.

    Make good use of it.
    """

    $ play_music('PREVIOUS')

    return


label tutorial_unlock_character:

    $ stop_music(2)
    
    tutorial """
    You've unlocked a new character!

    Now, you can begin the narrative through their point a view.

    Each character possesses a distinct story, persona, and background.

    This individuality may grant you access to specific choices unavailable to others.

    Use the characters' full potential to unravel the mystery of this weekend.
    """

    $ play_music('PREVIOUS')

    return

label tutorial_progress:

    $ stop_music(2)
    
    tutorial """
    Wait, it looks like you've unlocked something.

    It could be that you made a choice, an observation, or found an object.
    
    Basically, something that can influence the rest of the story.

    To help you keep track of them, you can now consult the "Progress" page.

    Here, you'll see all the possible paths for each character you've unlocked. 

    And if you click on them, you'll see a list of all the times you've reached them.

    Selecting any of these will show you the options you've unlocked at those specific times.

    If they are in colour, it means they have been activated.

    A question mark means you've never encountered them before.

    To check what options have been unlocked at the moment, just pick the chapter that is blinking.

    Inside, you can select the "Current Status" item on the list.

    I strongly recommend that you explore these screens; they will be very useful for the rest of the game.
    """

    $ _game_menu_screen = "progress"
    $ renpy.call_in_new_context("_game_menu", "navigation")
    
    $ play_music('PREVIOUS')

    return

label tutorial_restart:
    
    tutorial """
    You now have to restart the story. 
    
    However, there's no need to worry as you can use the skip button located at the bottom right of the screen to skip over any previously encountered dialogues.
    """
    
    # TODO check if not mobile version =>
    tutorial """
    You can also use the "CTRL" key on your keyboard.
    """
    
    tutorial """
    Furthermore, you now have access to the "Restart" button in the "Progress" menu. 

    Just choose a chapter on that screen, then any checkpoint from the list.
    
    It's now possible to restart the story from the selected checkpoint. 
    
    Please be cautious, as these checkpoints save the previous choices you've made. 
    
    Therefore, it may be necessary to start from an earlier point to unlock new story paths.
    """

    return
