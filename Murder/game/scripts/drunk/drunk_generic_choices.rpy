label drunk_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["drunk_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["drunk_generic_menu"])

    return