# Billiard room — Saturday evening
# Captain enters alone and waits to see who, if anyone, will join him.
label captain_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not captain_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ captain_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        The billiard room is lit much as it was last night, but the warmth of the place has gone out of it.

        The decanters stand untouched on the side. The glasses have been laid out in expectation of a company that has chosen not to come.

        I am quite alone.

        I make no move towards the bottles.

        Instead I take a chair near the fire, where I can keep both the door and the drinks in plain view.

        And I wait.
        """

        # TODO: choose who arrives — host? butler? psychic? nurse? lad?
        # The visitor's identity should turn on which threads the captain has set
        # (host suspicions, jerrycan, master_key, attic findings).
        # For now this is a placeholder so the scene can be tested end-to-end.

        """
        TODO: someone joins the captain here.
        """

    else:

        """
        I am back in the billiard room.

        The chairs sit much as I left them.
        """

    return
