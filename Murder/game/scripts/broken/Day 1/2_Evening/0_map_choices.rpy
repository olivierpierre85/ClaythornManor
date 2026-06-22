# Map choices for Broken (Thomas Moody), Friday evening
#
# Servants' floor (kitchen, scullery, garage, gun room):
#   - Each downstairs room has TWO map choices with mutually exclusive conditions:
#       * livery found    -> the real room (broken_day1_evening_<room>)
#       * livery not found -> a "staff only" refusal. Trying it once sets
#         day1_evening_downstairs_refused, which greys the whole servants' floor
#         until the livery is found in the servant stair (which re-enables the
#         real choices regardless of the refused flag).
#
# Floor crossing:
#   - The engine tracks current_room/previous_room (custom_functions.rpy). At
#     the top of a room's redirect label, current_room is still the room he is
#     leaving, so we can tell when he crosses between floors.
#   - Going DOWN from above stairs  -> broken_descend_if_needed (livery on, mask off)
#   - Coming UP from below stairs   -> broken_ascend_if_needed (livery off, mask on)
#   - Moving below-to-below or above-to-above triggers no change.

init python:
    def broken_is_downstairs(room_id):
        # The servants' floor (basement). Crossing into or out of this group is
        # what triggers the livery change.
        return room_id in ('kitchen', 'scullery', 'garage', 'gun_room')


label broken_day1_evening_map_menu:
    python:
        broken_day1_evening_map_menu = TimedMenu(
            "broken_day1_evening_map_menu",
            [
            # Attic
            TimedMenuChoice(default_room_text('storage'), 'broken_day1_evening_attic_default', 10, room='storage'),
            TimedMenuChoice(default_room_text('males_room'), 'broken_day1_evening_attic_default', 10, room='males_room'),
            TimedMenuChoice(default_room_text('females_room'), 'broken_day1_evening_attic_default', 10, room='females_room'),
            TimedMenuChoice(default_room_text('attic_butler_room'), 'broken_day1_evening_attic_default', 10, room='attic_butler_room'),
            # Bedrooms (his own room is the retire exit, so it is not listed here)
            TimedMenuChoice(default_room_text('bedroom_lad'), 'broken_day1_evening_bedroom_avoid', 10, room='bedroom_lad'),
            TimedMenuChoice(default_room_text('bedroom_host'), 'broken_day1_evening_bedroom_avoid', 10, room='bedroom_host'),
            TimedMenuChoice(default_room_text('bedroom_nurse'), 'broken_day1_evening_bedroom_avoid', 10, room='bedroom_nurse'),
            TimedMenuChoice(default_room_text('bedroom_doctor'), 'broken_day1_evening_bedroom_avoid', 10, room='bedroom_doctor'),
            TimedMenuChoice(default_room_text('bedroom_drunk'), 'broken_day1_evening_bedroom_avoid', 10, room='bedroom_drunk'),
            TimedMenuChoice(default_room_text('bedroom_psychic'), 'broken_day1_evening_bedroom_avoid', 10, room='bedroom_psychic'),
            TimedMenuChoice(default_room_text('bedroom_captain'), 'broken_day1_evening_bedroom_avoid', 10, room='bedroom_captain'),
            # Ground floor
            TimedMenuChoice(default_room_text('tea_room'), 'broken_day1_evening_tea_room', 10, room='tea_room'),
            TimedMenuChoice(default_room_text('dining_room'), 'broken_day1_evening_dining_room', 10, room='dining_room'),
            TimedMenuChoice(default_room_text('manor_garden'), 'broken_day1_evening_garden', 10, room='manor_garden'),
            TimedMenuChoice(default_room_text('entrance_hall'), 'broken_day1_evening_entrance_hall', 10, room='entrance_hall'),
            TimedMenuChoice(default_room_text('servant_stairs'), 'broken_day1_evening_servant_stairs', 10, room='servant_stairs'),
            TimedMenuChoice(default_room_text('portrait_gallery'), 'broken_day1_evening_portrait_gallery', 10, room='portrait_gallery'),
            TimedMenuChoice(default_room_text('library'), 'broken_day1_evening_library', 10, room='library'),
            # Servants' floor — two choices each. With the livery, the real room.
            # Without it, a "staff only" refusal that greys the whole floor once
            # tried (day1_evening_downstairs_refused), until the livery is found.
            TimedMenuChoice(default_room_text('kitchen'), 'broken_day1_evening_kitchen', 10, room='kitchen', condition="broken_details.threads.is_unlocked('found_livery')"),
            TimedMenuChoice(default_room_text('kitchen'), 'broken_day1_evening_downstairs_refused', 10, room='kitchen', condition="not broken_details.threads.is_unlocked('found_livery') and not broken_details.saved_variables['day1_evening_downstairs_refused']"),
            TimedMenuChoice(default_room_text('scullery'), 'broken_day1_evening_scullery', 10, room='scullery', condition="broken_details.threads.is_unlocked('found_livery')"),
            TimedMenuChoice(default_room_text('scullery'), 'broken_day1_evening_downstairs_refused', 10, room='scullery', condition="not broken_details.threads.is_unlocked('found_livery') and not broken_details.saved_variables['day1_evening_downstairs_refused']"),
            TimedMenuChoice(default_room_text('garage'), 'broken_day1_evening_garage', 10, room='garage', condition="broken_details.threads.is_unlocked('found_livery')"),
            TimedMenuChoice(default_room_text('garage'), 'broken_day1_evening_downstairs_refused', 10, room='garage', condition="not broken_details.threads.is_unlocked('found_livery') and not broken_details.saved_variables['day1_evening_downstairs_refused']"),
            TimedMenuChoice(default_room_text('gun_room'), 'broken_day1_evening_gun_room', 10, room='gun_room', condition="broken_details.threads.is_unlocked('found_livery')"),
            TimedMenuChoice(default_room_text('gun_room'), 'broken_day1_evening_downstairs_refused', 10, room='gun_room', condition="not broken_details.threads.is_unlocked('found_livery') and not broken_details.saved_variables['day1_evening_downstairs_refused']"),
            # Specific actions
            TimedMenuChoice('Look in on the others in the billiard room', 'broken_day1_evening_billiard_room', 10, room='billiard_room'),
            TimedMenuChoice('Retire for the night', 'generic_cancel', early_exit=True, room='bedroom_broken'),
        ], is_map = True)

    return


# ------------------------------------
#   FLOOR CROSSING (livery change)
# ------------------------------------
# Changing in or out of the livery is not free: each change costs ten minutes,
# taken off the map's time budget (and advanced on the clock to match).
label broken_livery_change_penalty:

    if not infinite_time_activated:

        $ time_left -= 10

        python:
            _penalty_time = datetime.combine(date.today(), current_time) + timedelta(minutes=10)

        call change_time(_penalty_time.hour, _penalty_time.minute)

    return


label broken_descend_if_needed:

    # Coming from above stairs -> change into the livery before going below.
    if not broken_is_downstairs(current_room):

        $ change_room('servant_stairs')

        """
        I duck into the servant stair, take the livery from its peg, and shrug it on.

        Then the mask, worked loose and tucked away inside the coat.

        A footman is furniture. No one below will give me a second glance.
        """

        call broken_livery_change_penalty

    return


label broken_ascend_if_needed:

    # Coming from below stairs -> change back before rejoining the guests.
    if broken_is_downstairs(current_room):

        $ change_room('servant_stairs')

        """
        I cannot go back up among the guests dressed as a servant.

        I hang the livery on its peg, pull on my own coat, and fix the mask into place.

        Mr Moody again.
        """

        call broken_livery_change_penalty

    return


# ------------------------------------
#   GROUND FLOOR
# ------------------------------------
label broken_day1_evening_servant_stairs:

    call broken_ascend_if_needed

    $ change_room('servant_stairs')

    if not broken_details.threads.is_unlocked('found_livery'):

        """
        A low door lets onto a narrow stair, plainly the servants' way through the house.

        A footman's livery hangs on a peg, pressed and waiting for the morning.

        On an impulse I hold it up against myself.

        It fits. They cut these for tall men, and tall is the one thing I have never lacked.
        """

        pause 0.5

        """
        And there it is. The thought arrives before I have quite decided to think it.

        With this on my back, and the mask off my face, no one below stairs would look at me twice.

        A guest cannot set foot on the servants' floor without being marked and remembered.

        But a footman is furniture. He may go where he pleases.
        """

        $ broken_details.threads.unlock('found_livery')

    else:

        """
        The servant stair, quiet and dim.

        The livery waits on its peg, where I leave it between uses.
        """

    return


label broken_day1_evening_tea_room:

    call broken_ascend_if_needed

    call broken_tea_room_default

    return


label broken_day1_evening_dining_room:

    call broken_ascend_if_needed

    call broken_dining_room_default

    return


label broken_day1_evening_entrance_hall:

    call broken_ascend_if_needed

    call broken_entrance_hall_default

    return


label broken_day1_evening_garden:

    call broken_ascend_if_needed

    $ change_room('manor_garden')

    """
    Rain, and a wind getting up.

    There is nothing to be had out here in the dark and the wet.

    I step back inside.
    """

    return


label broken_day1_evening_portrait_gallery:

    call broken_ascend_if_needed

    call broken_portrait_gallery_default

    return


label broken_day1_evening_library:

    call broken_ascend_if_needed

    call broken_library_default

    return





# ------------------------------------
#   BEDROOMS
# ------------------------------------
label broken_day1_evening_bedroom_avoid:

    call broken_ascend_if_needed

    $ broken_details.saved_variables['day1_evening_bedroom_refusals'] += 1

    if broken_details.saved_variables['day1_evening_bedroom_refusals'] >= 1:

        $ change_room('bedrooms_hallway')

        """
        I pause at the door.

        No.

        I am already taking risk enough passing myself off as another man.

        I cannot afford to be caught coming out of a guest's room.

        Besides, this is not how I care to come by my information.

        As a journalist, I know I will learn far more from talking to people than from rummaging through their belongings.
        """

        # Block all bedrooms on the first refusal
        $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_lad'))
        $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_host'))
        $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_nurse'))
        $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_doctor'))
        $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_drunk'))
        $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_psychic'))
        $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('bedroom_captain'))

    return


# ------------------------------------
#   ATTIC
# ------------------------------------
label broken_day1_evening_attic_default:

    call broken_ascend_if_needed

    $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('storage'))
    $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('males_room'))
    $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('females_room'))
    $ all_menus[broken_details.saved_variables["day1_evening_map_menu"].id].hide_specific_choice(default_room_text('attic_butler_room'))

    """
    The servants sleep up under the eaves.

    A stranger is no more welcome there than a guest would be below.

    Whatever is up there will keep.
    """

    return
