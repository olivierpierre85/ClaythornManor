label tutorial_clock:

    $ stop_music(2)

    if not seen_tutorial_clock:

        tutorial """
        Wait, don't you hear something ticking?

        If you haven't noticed it yet, look at the clock in the upper-left corner.
        
        There, you can see the current time, as well as the day.

        This helpful tool will move as the story progresses, for example, when you start a new chapter of this adventure.

        Also, when you are faced with multiple choices, each action will take a different amount of time.

        Since each scene has a limited duration, this means you won't always have the opportunity to explore every option on a list.

        So make every choice count.

        Also, there is no need to rush reading, the time spent on an choice is set and not dependent on the speed of your actions.
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
    
    The "Characters" menu gives you an estimation of how much essential information has been unlocked, as well as a complete description of a character.

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
    You just received your first "Intuition"

    An "Intuition" is a powerful tool.

    Some say that when a death is particularly strong, it leaves a mark that can be felt across different planes of existence.

    Others believe it's the ghost of an alternate timeline returning to warn you.

    In any case, it means you will now receive a warning at some point during this adventure. 
    
    This will allow you to change the course of the story in ways that were previously impossible.

    Make good use of it.
    """

    $ play_music('PREVIOUS')

    return


label tutorial_unlock_character:

    $ stop_music(2)
    
    tutorial """
    You've unlocked a new character!

    Now, you can begin the narrative through their point of view.

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

    To help you, you can now consult the "Progress" page.

    Let's have a look at it.
    """

    # Here, you'll see all the possible paths for each character you've unlocked. 

    # And if you click on them, you'll see a list of all the times you've reached them.

    # Selecting any of these will show you the options you've unlocked at those specific times.

    # Inside, you can select the "Current Status" item on the list.

    # I strongly recommend that you explore these screens; they will be very useful for the rest of the game.
    # """

    $ _game_menu_screen = "progress"
    $ tutorial_on = True
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

    $ show_skip_hint_for_tutorial = True

    """
    This blinking icon will be visible when it is possible to fast forward.
    """

    $ show_skip_hint_for_tutorial = False
    
    tutorial """
    Furthermore, you now have access to the "Restart" button in the "Progress" menu. 

    Just choose a chapter on that screen, then any checkpoint from the list.
    
    It's now possible to restart the story from the selected checkpoint. 
    
    Please be cautious, as these checkpoints save the previous choices you've made. 
    
    Therefore, it may be necessary to start from an earlier point to unlock new story paths.
    """

    return


label tutorial_already_chosen:

    tutorial """
    You've selected a choice that was in dark.

    That means you've already made that choice before.

    No need to worry — there's nothing wrong with wanting to retrace your steps.

    However, you should know that if there were other choices to be made afterwards, you've already explored them all as well.

    To explain, let's take a simple example: imagine a question such as "Do you like apples?"

    If you answer "no", then the conversation ends there.

    But if you choose "yes", a new question appears: "Do you prefer red or green apples?"

    In that case, the "no" will turn dark once you've chosen it once.

    But the "yes" option from the first question won't turn dark until you've also selected both "red apples" and "green apples".

    I hope that makes things clearer.
    """

    # TODO: if impossible to grey all the possibilities, put this on
    # """
    # Of course, this can be a bit tricky, since some paths require that several choices be made at the right moment.

    # In that case, you may need to try a different combination of choices to unlock something new —

    # some you've already taken, and others you haven't.

    # But I promise it’s less complicated than it sounds.

    # Good luck!
    # """

    return


label tutorial_already_chosen_map:

    tutorial """
    You've selected a place you've already visited — at least during the same period.

    If you didn't notice, the text appeared in a darker tone.

    No need to worry — there's nothing wrong with revisiting the same location.

    But on a map, if a place name appears in dark, you're unlikely to find anything new there.

    I hope that helps you save some time.
    """

    return
