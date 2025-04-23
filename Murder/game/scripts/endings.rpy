label ending_generic:

    $ stop_music(2)

    if not is_death and first_survive:

        """
        You made it out alive.

        But it's not the perfect ending either.

        Don't get me wrong, it's still an impressive feat.

        But surviving Claythorn Manor is merely the first step.

        Your goal is to save everyone.
        """

        if not first_ending:
            """
            And to do that, you need to start the story over.
            """

        $ first_survive = False

    if first_ending:

        """
        Don't worry, you'll have more chances to change the fate of this character.

        You can start again now. Ideally, you've learned something that will help you in your next attempts.

        But perhaps you haven't learned anything.

        In that case, try to look at the story from a different perspective.

        This story isn't about just one hero.

        You'll get to play as different characters.

        And you must.

        Because otherwise, you'll never uncover the whole truth about what happened that weekend at Claythorn Manor.
        """

        $ first_ending = False

    $ is_death = True

    python:
        if not seen_tutorial_restart:
            seen_tutorial_restart = True
            renpy.call('tutorial_restart')

        if not seen_tutorial_restart and is_intuition:
            is_intuition = False
            seen_tutorial_restart = True
            renpy.call('tutorial_restart')

        # if full_testing_mode:
        #     f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/full_testing.txt", "a")
        #     f.write('You are DEAD - TODO save last death info\n')
        #     f.close()

        if show_tutorial_unlock_character:
            show_tutorial_unlock_character = False
            renpy.call('tutorial_unlock_character')



    hide screen centered_text

    jump character_selection

    return