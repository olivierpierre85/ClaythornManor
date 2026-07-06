transform character_choice_left:
  xpos 100  
  ypos 300

transform character_choice_left_2:
  xpos 400  
  ypos 500

transform character_choice_right:
  xpos 1600  
  ypos 300

transform character_choice_right_2:
  xpos 1300  
  ypos 500

label run_menu(current_menu, change_level=True):

    window hide

    # The instance cached in all_menus carries the dynamic state (hidden /
    # already-chosen choices) and is the one every alias points at, so it
    # stays the live menu. Its definition (texts, costs, conditions) is
    # refreshed from the latest template constructed from code, so menu edits
    # reach players whose saves already contain the menu.
    python:
        if current_menu.id in all_menus:
            _cached_menu = all_menus[current_menu.id]
            _template_menu = TimedMenu.templates.get(current_menu.id)
            if _template_menu is not None and _template_menu is not _cached_menu:
                refresh_menu_from_template(_cached_menu, _template_menu)
            current_menu = _cached_menu
        else:
            all_menus[current_menu.id] = current_menu

    if change_level:
        $ menu_level += 1
        # Check if there is a selected choice from the previous level.
        # Since selected_choice is a list, we use indexing and check the length.
        if menu_level > 0 and len(selected_choice) >= menu_level and selected_choice[menu_level - 1]:
            $ selected_choice[menu_level - 1].next_menu = current_menu.id

    if current_menu.is_valid(opening=change_level):

        # Record the time at opening of the menu
        python:
            now = datetime.now()

        # Show characters when activated
        if current_menu.image_left:
            $ renpy.show(current_menu.image_left, at_list=[character_choice_left])
        if current_menu.image_left_2:
            $ renpy.show(current_menu.image_left_2, at_list=[character_choice_left_2])
        if current_menu.image_right:
            $ renpy.show(current_menu.image_right, at_list=[character_choice_right])
        if current_menu.image_right_2:
            $ renpy.show(current_menu.image_right_2, at_list=[character_choice_right_2])
        
        $ selected_choice[menu_level] = current_menu.display_choices()
        
        # Hide choices when activated
        if current_menu.image_left:
            $ renpy.hide(current_menu.image_left)
        if current_menu.image_right:
            $ renpy.hide(current_menu.image_right)
        if current_menu.image_left_2:
            $ renpy.hide(current_menu.image_left_2)
        if current_menu.image_right_2:
            $ renpy.hide(current_menu.image_right_2)

        if selected_choice[menu_level].early_exit:
            $ current_menu.early_exit = True     

        # Save choices for debug
        # First get all possible choices and put them in list:
        python:
            global time_left

            current_choices = []
            for choice in current_menu.choices:
                if (not choice.hidden and choice.get_condition()) or choice.text==selected_choice[menu_level].text :
                    current_choices.append(choice.text)

            time_to_decide = None
            time_since_last = None

            if all_choices:
                last_timestamp = datetime.fromisoformat(all_choices[-1]["timestamp"])
                time_since_last = (now - last_timestamp).total_seconds()

            time_to_decide = (datetime.now() - now).total_seconds()

            all_choices.append({
                "menu": current_menu.id,
                "other_choices": current_choices,
                "selected": selected_choice[menu_level].text,
                "redirect": selected_choice[menu_level].redirect,
                "time_left": time_left,
                "timestamp": now.isoformat(),
                "time_to_decide": time_to_decide,
                "time_since_last": time_since_last,
            })

            
            if not infinite_time_activated:
                time_left -= selected_choice[menu_level].time_spent

        python:
        # Add selected choice in log
            if current_menu.is_map:
                _history_list.append(ChoiceHistory("Map Choice", selected_choice[menu_level].text))
            else:
                _history_list.append(ChoiceHistory("Menu Choice", selected_choice[menu_level].text))
                # renpy.say(current_character.real_name, selected_choice[menu_level].text, interact=False)


        # Autosave after every committed choice. The custom menus bypass the
        # `menu` statement, so this is where autosave_on_choice actually happens.
        # block=True keeps the save off the background thread (the old flaky
        # path). Loading this save puts the player back at this menu.
        if config.autosave_on_choice and not full_testing_mode and not renpy.is_in_test():
            $ renpy.force_autosave(take_screenshot=True, block=True)

        if show_tutorial_already_chosen:
            $ show_tutorial_already_chosen = False
            call expression "tutorial_already_chosen"
            $ seen_tutorial_already_chosen = True


        if show_tutorial_already_chosen_map:
            $ show_tutorial_already_chosen_map = False
            call expression "tutorial_already_chosen_map"
            $ seen_tutorial_already_chosen_map = True

        # ---- Now the actual call to the selected option
        call expression selected_choice[menu_level].redirect
        # --------------------------------------------------- 

        # We used to deduct time after choice, but it was a problem with submenu
        # $ global time_left
        # $ time_left -= selected_choice[menu_level].time_spent

        # Change current time
        $ time_diff[menu_level] = None
        if time_left > 0 and selected_choice[menu_level].time_spent:
            $ time_diff[menu_level] = datetime.combine(date.today(), current_time) + timedelta(minutes=selected_choice[menu_level].time_spent)

        if time_diff[menu_level]:
            call change_time(time_diff[menu_level].time().hour, time_diff[menu_level].time().minute)

        pause 0.7

        call run_menu(current_menu, change_level=False)

    if change_level:
        $ menu_level -= 1

    $ current_menu.early_exit = False

    return


# Rebuild menu templates from current code whenever a save is loaded, so that
# menu edits reach existing saves. Only pure construction labels are called:
# the per-character generic-menu configs (<char>_config_menu) and the
# per-chapter map menus, whose label name matches the menu id by convention.
# Constructing a TimedMenu registers it in TimedMenu.templates; run_menu then
# refreshes the cached instances in place on their next open.
label after_load:

    python:
        menu_rebuild_labels = []
        for rebuild_char in (getattr(renpy.store, "char_list_flat", None) or []):
            rebuild_label = rebuild_char.text_id + "_config_menu"
            if renpy.has_label(rebuild_label):
                menu_rebuild_labels.append(rebuild_label)
        for rebuild_menu_id in all_menus:
            if rebuild_menu_id.endswith("_map_menu") and renpy.has_label(rebuild_menu_id):
                menu_rebuild_labels.append(rebuild_menu_id)
        menu_rebuild_i = 0

    while menu_rebuild_i < len(menu_rebuild_labels):

        call expression menu_rebuild_labels[menu_rebuild_i]

        $ menu_rebuild_i += 1

    return


init -1 python:
    # Used for Logs
    class ChoiceHistory(object):
        def __init__(self, who, what, who_id=None, what_id=None):
            self.who = who
            self.what = what
            self.who_id = who_id
            self.what_id = what_id

    def is_linked_choice_hidden(menu_id, linked_choice_name):
        """
        Returns True if the choice in menu_id that has linked_choice matching linked_choice_name is hidden.
        """
        if menu_id in all_menus:
            for choice in all_menus[menu_id].choices:
                if choice.linked_choice == linked_choice_name:
                    return choice.hidden
        return False

    def is_choice_hidden(menu_id, redirect):
        """
        Returns True if the choice in menu_id whose redirect matches `redirect` is
        hidden (i.e. it has already been chosen).

        Prefer this over positional access such as
        all_menus[menu_id].choices[N].hidden: indexing by position breaks silently
        the moment a choice is inserted into or removed from the menu, whereas the
        redirect is stable. Positional .choices[N] access is deprecated.
        """
        if menu_id in all_menus:
            for choice in all_menus[menu_id].choices:
                if choice.redirect == redirect:
                    return choice.hidden
        return False

    def is_choice_already_chosen(menu_id, redirect):
        """
        Returns True if the choice in menu_id whose redirect matches `redirect` has
        already been chosen. Like is_choice_hidden, prefer this over positional
        .choices[N].already_chosen access, which is deprecated.
        """
        if menu_id in all_menus:
            for choice in all_menus[menu_id].choices:
                if choice.redirect == redirect:
                    return choice.already_chosen
        return False

    # Shortcut to be used in the Menu to avoid showing a menu when there is nothing after. e.g: Used for billiard room
    def is_menu_valid(menu_id):
        if menu_id not in all_menus:
            return True
        return all_menus[menu_id].is_valid(next_menu=True)

    def find_choice_for_room(menu, room_id):
        """
        The choice a map menu executes for a room: the first one whose
        condition holds. Single source of truth shared by the map screen's
        hotspot scan and display_choices, so the tooltip shown and the choice
        executed can never disagree when two conditions overlap.
        """
        for choice in menu.choices:
            if choice.room == room_id and choice.get_condition():
                return choice
        return None

    # Possible choices for a menu
    class TimedMenuChoice:
    
        def __init__(
            self, 
            text, 
            redirect, 
            time_spent = 0, 
            choice_repeat = False, 
            hidden = False, 
            keep_alive = False, 
            early_exit = False,
            condition = None,
            room = None,
            already_chosen = False, 
            next_menu = None,
            linked_choice = None,
            parent_menu_id = None
        ):
            self.text = text
            self.redirect = redirect
            self.time_spent = time_spent
            self.choice_repeat = choice_repeat
            self.hidden = hidden
            self.keep_alive = keep_alive
            self.early_exit = early_exit
            self.condition = condition
            self.room = room
            self.already_chosen = already_chosen
            self.next_menu = next_menu
            self.linked_choice = linked_choice
            self.parent_menu_id = parent_menu_id
        
        def get_condition(self):
            if self.condition:
                return eval(self.condition)
            return True

        def is_valid(self):
            # IF choice has next_menu, make sure the menu is valid? Or is doesn't exist in all_menu
            if not self.hidden and self.get_condition():
                if not self.next_menu:
                    return True
                else:
                    if self.next_menu not in all_menus:
                        # menu not loaded yet so it should be valid if build logically
                        return True 
                    else:
                        # Check is next menu is valid
                        return all_menus[self.next_menu].is_valid(next_menu=True)

            return False

        def is_already_chosen(self):
            if not self.already_chosen:
                return False
            elif self.already_chosen and not self.next_menu and not self.linked_choice:
                return True
            else:
                if self.next_menu:
                # When already selected we need to check if the next menu is completed
                    if self.next_menu not in all_menus:
                        return False 

                    for choice in all_menus[self.next_menu].choices:
                        # if the condition is not met (invisible), skip the test
                        if not choice.get_condition():
                            continue
                        # A choice is seen as completed if it is a keep alive without a menu,
                        # or if it is itself completed 
                        if not (choice.keep_alive and not choice.next_menu) and not choice.is_already_chosen():
                            return False
                elif self.linked_choice:

                    parent_menu = all_menus[self.parent_menu_id]
                    found_linked_choice = False

                    for c in parent_menu.choices:
                        if c.redirect == self.linked_choice:
                            found_linked_choice = True
                            if not c.is_already_chosen():
                                return False
                            break
                    # If we never found the linked choice in the parent menu, treat as is_already_chosen (I assume wrong rewrite)
                    if not found_linked_choice:
                        return True

                return True

    # A Timed
    class TimedMenu:

        # Latest instance constructed from code, per menu id. A class
        # attribute is neither saved nor rolled back, and unpickling a menu
        # from a save does not call __init__, so this only ever contains
        # menus built by the current code - run_menu uses it to refresh
        # cached menus (see refresh_menu_from_template).
        templates = {}

        def __init__(self, id, choices = None, is_map = False, image_left = None, image_right = None, image_left_2 = None,image_right_2 = None,):
            self.id = id
            self.choices = choices if choices is not None else []
            self.is_map = is_map
            self.image_left = image_left
            self.image_right = image_right
            self.image_left_2 = image_left_2
            self.image_right_2 = image_right_2
            self.early_exit = False
            # Make each choice aware of its parent menu
            for c in self.choices:
                c.parent_menu_id = self.id
            TimedMenu.templates[self.id] = self
    
        def get_all_redirects(self):
            all_redirects = set()
            for choice in self.choices:
                all_redirects.add(choice.redirect)
            
            return all_redirects

        def is_valid(self, next_menu=False, opening=False):
            if self.get_visible_choices_total(next_menu) <= 0:
                return False

            # A sub-menu the player has just committed to may proceed even when
            # the clock has run out, so the parent choice can charge a real visit
            # cost without the sub-menu vanishing.
            # Conditions:
            #   opening      -> this is the first open (change_level=True), not a
            #                   re-display of the same menu after a choice.
            #   not next_menu -> only the run check is relaxed, never the choice
            #                   visibility check, so parent map choices stay
            #                   time-gated and cannot be started at <= 0 time.
            #   menu_level>0 -> only sub-menus, never a top-level map menu.
            # Re-displays (opening=False) fall through to the strict check below,
            # so the sub-menu still closes once the player runs out of time.
            if (opening and not next_menu and menu_level > 0
                    and len(selected_choice) >= menu_level
                    and selected_choice[menu_level - 1]):
                return True

            if time_left <= 0 or self.early_exit:
                return False

            return True

        # The next_menu bool is needed because we don't want to reach a next_menu with only the exit
        # But if we already are  in the menu, we should see it
        def get_visible_choices_total(self, next_menu):
            visible_choices = 0
            for i, choice in enumerate(self.choices):                
                # When a choice is keep_alive and early_exit, it's a generic choice to leave and shouldn't count on it's own
                if choice.is_valid():
                    if not (next_menu and choice.keep_alive and choice.early_exit):
                        visible_choices += 1
                    
            return visible_choices
        
        def hide_specific_choice(self, choice_to_hide):
            for current_choice in self.choices:
                if current_choice.text == choice_to_hide:
                    current_choice.hidden = True
                    current_choice.already_chosen = True


        def display_choices(self):

            selected_choice = None

            # --- Ren'Py automated tests: use recorded plan, never open UI ---
            if renpy.is_in_test() and not ollama_autoplay:
                t = getattr(renpy.store, "test", None)
                if t and getattr(t, "autorunner", None) and t.autorunner.active:
                    selected_choice = t.autorunner.pick_choice_for_menu(self)
                    selected_choice_i = self.choices.index(selected_choice)

            # --- Full-game autoplay: a local LLM (Ollama) picks the choice ---
            elif ollama_autoplay:
                selected_choice = ollama_pick_menu_choice(self)
                selected_choice_i = self.choices.index(selected_choice)

            # --- (Optional) keep your existing full_testing_mode for manual debug runs ---
            elif full_testing_mode and full_testing_mode_choices:

                full_testing_mode_choice = full_testing_mode_choices.pop(0)
                redirect_target = full_testing_mode_choice.get("redirect")
                selected_text = full_testing_mode_choice.get("selected")

                # Prefer redirect match (most stable), fallback to text match
                if redirect_target:
                    for i, choice in enumerate(self.choices):
                        if choice.is_valid() and redirect_target == choice.redirect:
                            selected_choice = choice
                            selected_choice_i = i
                            break

                if not selected_choice and selected_text:
                    for i, choice in enumerate(self.choices):
                        if choice.is_valid() and selected_text == choice.text:
                            selected_choice = choice
                            selected_choice_i = i
                            break

                if not selected_choice:
                    # If we don't find the choice, we stop the full testing mode and return to manual
                    # This allows the user to continue from where the test ended
                    renpy.store.full_testing_mode = False
                

            if not selected_choice:

                if current_menu.is_map:
                    global selected_floor
                    global current_floor
                    selected_floor = current_floor

                    room_id = renpy.call_screen('in_game_map_menu', timed_menu=self)

                    selected_choice = find_choice_for_room(self, room_id)

                else:
                    selected_choice_i = renpy.call_screen('custom_choice', self) 
                    selected_choice = self.choices[selected_choice_i]

            if not selected_choice.keep_alive:
                selected_choice.hidden = True
            
            # don't grey out exit choices (BUT implies more changes in is_already_chosen
            # if not selected_choice.keep_alive and not selected_choice.early_exit:
            selected_choice.already_chosen = True
                
            # global time_left
            # time_left -= selected_choice.time_spent

            return selected_choice

        def __str__(self):
            menu_str = ""
            for choice in self.choices:
                if not choice.hidden and ((not choice.condition) or eval(choice.condition)):
                    menu_str += choice.text + "\n"
            return menu_str

    # ------------------------------------------------------------------
    # Menu dynamic state
    #
    # The dynamic state of a menu is which choices are hidden / already
    # chosen (plus the next_menu links established at runtime). Checkpoints
    # store only this state, keyed by menu id and choice key, instead of
    # deep copies of whole TimedMenu graphs - keeping per-choice autosaves
    # small and letting code edits to menus reach existing saves.
    # ------------------------------------------------------------------

    def menu_choice_state_key(choice):
        # Stable identity of a choice across code edits: the room (map
        # menus) or the visible text, plus the redirect. Keying map choices
        # by room means their wording can be edited without losing state.
        if choice.room:
            return (choice.room, choice.redirect)
        return (choice.text, choice.redirect)

    def capture_menu_state(menu):
        # Sparse snapshot: only choices with non-default state are recorded.
        state = {}
        for choice in menu.choices:
            if choice.hidden or choice.already_chosen:
                state[menu_choice_state_key(choice)] = (choice.hidden, choice.already_chosen)
        return state

    def capture_all_menus_state():
        state = {}
        for menu_id, menu in all_menus.items():
            menu_state = capture_menu_state(menu)
            if menu_state:
                state[menu_id] = menu_state
        return state

    def refresh_menu_from_template(menu, template):
        # In-place update of a cached menu's definition from a freshly
        # constructed template, preserving the dynamic state of choices that
        # survive the edit. In place, so every alias to the cached menu
        # (saved_variables entries, the run_menu call stack) stays valid.
        old_choices = {}
        for choice in menu.choices:
            old_choices[menu_choice_state_key(choice)] = choice

        for choice in template.choices:
            old_choice = old_choices.get(menu_choice_state_key(choice))
            if old_choice is not None:
                choice.hidden = old_choice.hidden
                choice.already_chosen = old_choice.already_chosen
                choice.next_menu = old_choice.next_menu
            choice.parent_menu_id = menu.id

        menu.choices = template.choices
        menu.is_map = template.is_map
        menu.image_left = template.image_left
        menu.image_right = template.image_right
        menu.image_left_2 = template.image_left_2
        menu.image_right_2 = template.image_right_2

    def copy_saved_variables(saved_variables):
        # Copy of a saved_variables dict for storing in / restoring from a
        # checkpoint. Scalars and containers are deep-copied; TimedMenu
        # values are kept by reference - such an entry is only an id carrier
        # (the live state of a menu is the all_menus instance), and sharing
        # the reference lets the save pickler store the menu once instead of
        # once per checkpoint.
        copied = {}
        for key, value in saved_variables.items():
            if isinstance(value, TimedMenu):
                copied[key] = value
            else:
                copied[key] = copy.deepcopy(value)
        return copied