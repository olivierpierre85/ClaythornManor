# The script of the game goes in this file.

# The game starts here.
label start:
    
    # TODO how to add a shortcut to game menu. Below not working
    # $ config.keymap['in_game_menu'] = ['m']

    show screen current_time

    show screen in_game_menu_btn


    # Debug Menu
    jump debug_choices

    # These display lines of dialogue.
    jump character_selection
    

    return
