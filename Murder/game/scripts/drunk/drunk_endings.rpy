# --------------------------------------------
#   Drunk endings
# --------------------------------------------

label drunk_ending_despair:

    $ drunk_mode = False

    $ drunk_details.endings.unlock('despair')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('despair'))

    call death_screen_transition

    # TODO add dialogs

    jump ending_generic


label drunk_ending_spared:

    $ drunk_details.endings.unlock('spared')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('spared'))

    call death_screen_transition

    # TODO add dialogs

    jump ending_generic


label drunk_ending_throat_cut:

    $ drunk_mode = False

    $ drunk_details.endings.unlock('throat_cut')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('throat_cut'))

    call death_screen_transition

    # TODO add dialogs

    jump ending_generic


label drunk_ending_silenced:

    $ drunk_details.endings.unlock('silenced')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('silenced'))

    call death_screen_transition

    # TODO add dialogs

    jump ending_generic


label drunk_ending_found_out:

    $ drunk_details.endings.unlock('found_out')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('found_out'))

    call death_screen_transition

    # TODO add dialogs

    jump ending_generic


label drunk_ending_survived:

    call survive_screen_transition

    $ play_music('end_credits')

    $ drunk_details.endings.unlock('survived')
    $ drunk_details.add_ending_checkpoint(ending=drunk_details.endings.get_item('survived'))

    # TODO add dialogs

    $ is_death = False

    jump ending_generic
