# The script of the game goes in this file.

# The game starts here.
label start():

    # Default Menu screen when press ESC in-game
    $ _game_menu_screen = "manor_map"

    $ characters_knowledge['psychic'] = set() #TODO reset all

    show screen current_time

    show screen in_game_menu_btn

    $ test_mode = False

    # Debug Menu # TODO remove when prod
    jump debug_choices

    # These display lines of dialogue.
    jump character_selection

    return
