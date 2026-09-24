# --------------------------------------------
#   Drunk - Saturday night, the three ways out of the locked room
#
#   - drink    -> he cuts his own throat (throat_cut)
#   - confront -> he warns the house and one of them silences him (silenced)
#   - play dead -> he paints his throat with port, drops his razor beneath his
#                  hand and lies down (played_dead), and the story goes on to
#                  Sunday. Real or staged, every other route reads the body the
#                  same way: a suicide behind a locked door
# --------------------------------------------


# ------------------------------------
#   Accept it, and drink. -> throat_cut
# ------------------------------------
label drunk_day2_evening_drink:

    $ change_room('bedroom_drunk')

    # TODO add dialogs

    jump drunk_ending_throat_cut


# ------------------------------------
#   Warn the house. Nobody believes a drunk. -> silenced
# ------------------------------------
label drunk_day2_evening_confront:

    $ change_room('bedroom_drunk')

    $ play_music('danger', 2)

    # TODO add dialogs

    jump drunk_ending_silenced


# ------------------------------------
#   Play dead. -> played_dead, Sunday
# ------------------------------------
label drunk_day2_evening_play_dead:

    $ change_room('bedroom_drunk')

    $ play_music('mysterious', 2)

    # TODO add dialogs

    $ drunk_details.threads.unlock('played_dead')

    # TODO add dialogs

    jump drunk_day3_morning
