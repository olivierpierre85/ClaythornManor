# Generic Captain location visits.
# Used for places that can be visited on multiple days with the same options.

label captain_library_default:

    $ change_room('library')

    if captain_details.threads.is_unlocked('captain_host_suspicion_name'):

        """
        I have already read what I needed from the genealogy book.

        There is nothing more here for me.
        """

        return

    """
    A well-stocked library. The kind one would expect in a house like this.

    A book lies open on a table.

    'A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.'

    The eighth edition, printed in 1894.

    I remember dreaming of seeing my name in such a book.

    I know now that it will never happen.
    """

    call run_menu(
        TimedMenu("captain_library_menu", [
            TimedMenuChoice('Look up the Claythorns in the index', 'captain_library_read', 30, early_exit=True),
            TimedMenuChoice('Leave the book be', 'generic_cancel', 10, early_exit=True)
        ])
    )

    return


label captain_library_read:

    """
    I glance through a few pages.

    Let us see if the Claythorns are mentioned.

    I search through the index. Clarendon, Claridge, Clark...

    Claythorn.

    There are several entries. I find the one concerning this manor.
    """

    call library_book_content

    """
    I read the entry twice.

    There it is. The family name is Claythorn, but their title is not.

    They hold a peerage — the Earldom of Kilbraith. Their seat is this manor, but the title is quite separate.

    A peer is addressed by his title, not by his surname. The Earl of Kilbraith is styled 'Lord Kilbraith', and his countess, 'Lady Kilbraith'.

    Never 'Lord Claythorn', nor 'Lady Claythorn'.

    Still, I should not leap to conclusions.

    It is not unheard of for a family to set the formal title aside in daily use. 
    
    Since the war, I have heard of peers who have grown weary of ceremony.

    Or perhaps it is a local habit. The villagers call her 'Lady Claythorn' after the name of the house, and in time she has simply let it stick.

    And yet, it is something strange enough that I should not dismiss it entirely.

    I close the book and place it back on the table.
    """

    $ captain_details.threads.unlock('captain_host_suspicion_name')

    call captain_host_suspicion

    return


label captain_host_suspicion:

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        That is the third intriguing thing I notice about Lady "Claythorn".

        A lapse in manner at dinner.

        No visible portrait of her in her house.

        And a rather unconventional use of her name.

        What could this mean?

        I am starting to fear that something is amiss here.
        """

    return


# ------------------------------------
#   GARDEN AND SHED (shared across days)
# ------------------------------------
# The captain always braves the rain, regardless of weather.
# Two map choices share the same intro:
#   - captain_garden_default_no_lantern  (visible when the captain has no lantern)
#   - captain_garden_default_with_lantern (visible when the lantern is in hand)
# Without a lantern he turns back; the choice itself deducts the time on the map.
# With a lantern he can approach the shed; the inner sub-menu deducts the time.
# The shed door is always locked. With the master key (only available from
# saturday_evening onward) he opens it and discovers the petrol tin inside.

label captain_garden_intro:

    python:
        _captain_garden_intro_key = current_chapter + "_captain_garden_intro_done"
        _captain_garden_intro_done = captain_details.saved_variables.get(_captain_garden_intro_key, False)

    if _captain_garden_intro_done:

        $ change_room('manor_garden')

        """
        I step back out into the rain.

        The garden is as I left it earlier: gravel underfoot, the outbuilding waiting in the dark.
        """

        return

    $ captain_details.saved_variables[_captain_garden_intro_key] = True

    $ change_room('entrance_hall')

    if current_chapter == 'friday_evening':

        """
        I look through the window. The rain is coming down hard.

        A storm is gathering. I can hear the wind picking up against the glass.

        Most men would turn back at this point.

        But I have marched through monsoons. A bit of rain is hardly cause for concern.
        """

    else:

        """
        I look through the window.

        A steady rain is falling again.

        Lighter than last night, though enough to soak a man through.

        But that is nothing that can really prevent me from going.
        """

    $ change_room('manor_garden')

    """
    I step outside.

    The air is cold and the rain heavier than it looked from indoors.

    Within moments my jacket is soaked through.

    I walk a short distance around the house.

    A gravel path, wet grass, and, further off in the dark, the shape of an outbuilding.
    """

    return


label captain_garden_default_no_lantern:

    call captain_garden_intro

    """
    Without a light, I cannot venture any further out here.

    I shall not stumble about in the dark.

    I turn back to the house.
    """

    $ change_room('bedroom_captain')

    """
    I head inside to change out of these wet clothes.
    """

    return


label captain_garden_default_with_lantern:

    call captain_garden_intro

    """
    The lantern's pool of light picks out the gravel path, the wet grass beyond, the dark mass of the hedge.

    I make my way around to the outbuilding.
    """

    call run_menu(TimedMenu("captain_garden_shed_menu", [
        TimedMenuChoice("Take a closer look at the outbuilding", 'captain_garden_shed', 30, early_exit=True),
        TimedMenuChoice("Don't stay too long in the rain", 'generic_cancel', 10, early_exit=True),
    ]))

    $ change_room('bedroom_captain')

    """
    I slip back inside and brush the damp from my coat.
    """

    return


label captain_garden_shed:

    $ change_room('toolshed_outside_night')
    
    """
    I press on through the rain, boots sinking into the sodden gravel.

    The outbuilding proves to be a squat timber shed, half hidden behind an overgrown hedge.

    I try the handle.

    It does not give. The door is locked, and firmly so.
    """

    if not captain_details.objects.is_unlocked('butler_key'):

        """
        A garden shed, out here in the middle of nowhere, bolted shut against what?

        Whoever fitted that lock had a reason, and it was not the threat of common thieves.

        I have no means of opening it tonight.
        """

        return

    """
    I fit the master key to the lock. It does not turn at first.

    A patient adjustment, and the bolt slides clear.

    The door creaks open on a small, low-roofed space smelling strongly of oil and old timber.
    """

    play sound door_open

    $ change_room("toolshed")

    """
    The lantern's glow picks out a workbench, a coil of rope, a tarpaulin folded against one wall.

    And, set rather neatly in the middle of the floor, a metal petrol tin.

    I unscrew the cap and lower my nose to it for a moment. Petrol, and a great deal of it.

    A full can — that could be useful.

    I search a little further but find nothing more of interest.

    I step out and lock the door behind me as carefully as I opened it.
    """

    $ captain_details.threads.unlock('petrol_tin_in_shed')

    return


label captain_portrait_gallery_default:

    $ change_room('portrait_gallery')

    if captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        The Claythorn forebears still gaze down from their frames, silent and stern.

        The absence of our host's portrait remains as striking as before.

        There is nothing more the gallery can tell me.
        """

        return

    """
    A gallery of family portraits lines the walls.

    The Claythorn lineage, rendered in oil and gilt frames.

    I study the faces. Old money, passed down through blood.

    There are perhaps a dozen portraits here, spanning several generations.

    Stern-looking gentlemen in powdered wigs. Ladies in elaborate gowns.

    But then something strikes me.

    None of them resemble our host.

    Where is Lady Claythorn?

    If she is the current mistress of this house, her portrait ought to hang here alongside her forebears.

    And yet there is nothing.

    And I do not recall seeing it anywhere else in the house.

    In itself, that does not mean much.

    Perhaps she had difficulty persuading a decent artist to come all the way out here.

    Or, it could simply be a personal preference.

    But I will keep that in mind nonetheless.
    """

    $ captain_details.threads.unlock('captain_host_suspicion_portrait')

    return
