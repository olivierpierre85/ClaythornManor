init -1 python:
    class TimedMenuChoice:
        """
        Represents a single choice in a TimedMenu.
        Args:
            text (str): The text displayed for the choice.
            redirect (str): The label or function to call when this choice is selected.
            time_spent (int): Time spent when this choice is selected.
            choice_repeat (bool): If the choice can be repeated.
            hidden (bool): If the choice is hidden.
            keep_alive (bool): If the choice remains visible after being chosen.
            early_exit (bool): If selecting this choice exits the menu early.
            condition (str): Python expression for visibility.
            room (str): Room identifier for map menus.
            already_chosen (bool): If the choice has already been chosen.
            next_menu (str): ID of the next menu to show.
            linked_choice (str): ID of a linked choice for completion logic.
            parent_menu_id (str): ID of the parent menu.
        """
        def __init__(self, text, redirect, time_spent=0, choice_repeat=False, hidden=False, keep_alive=False, early_exit=False, condition=None, room=None, already_chosen=False, next_menu=None, linked_choice=None, parent_menu_id=None):
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

        @staticmethod
        def safe_eval(expr, local_vars=None):
            """
            Safely evaluate a condition string using only whitelisted variables/functions.
            This prevents arbitrary code execution and improves security.
            """
            allowed_globals = {
                'True': True,
                'False': False,
                # Add more safe built-ins or game state variables as needed
            }
            if local_vars is None:
                local_vars = {}
            return eval(expr, allowed_globals, local_vars)

        def get_condition(self):
            """Evaluates the condition for displaying this choice using safe_eval."""
            if self.condition:
                # You can pass in specific local_vars if needed for your game logic
                return TimedMenuChoice.safe_eval(self.condition)
            return True

        def is_completed(self):
            """Checks if this choice and any chained/linked choices are completed."""
            if not self.already_chosen:
                return False
            elif self.already_chosen and not self.next_menu and not self.linked_choice:
                return True
            else:
                if self.next_menu:
                    if self.next_menu not in menu_manager.all_menus:
                        return False
                    for choice in menu_manager.all_menus[self.next_menu].choices:
                        if not choice.get_condition():
                            continue
                        if not (choice.keep_alive and not choice.next_menu) and not choice.is_completed():
                            return False
                elif self.linked_choice:
                    parent_menu = menu_manager.all_menus[self.parent_menu_id]
                    found_linked_choice = False
                    for c in parent_menu.choices:
                        if c.redirect == self.linked_choice:
                            found_linked_choice = True
                            if not c.is_completed():
                                return False
                            break
                    if not found_linked_choice:
                        return True
                return True

    class TimedMenu:
        """
        Represents a menu with timed choices and optional images.
        Args:
            id (str): Unique menu identifier.
            choices (list): List of TimedMenuChoice objects.
            is_map (bool): If this menu is a map menu.
            image_left, image_right, image_left_2, image_right_2 (str): Optional image references.
        """
        def __init__(self, id, choices=[], is_map=False, image_left=None, image_right=None, image_left_2=None, image_right_2=None):
            self.id = id
            self.choices = choices
            self.is_map = is_map
            self.image_left = image_left
            self.image_right = image_right
            self.image_left_2 = image_left_2
            self.image_right_2 = image_right_2
            self.early_exit = False
            for c in self.choices:
                c.parent_menu_id = self.id

        def get_all_redirects(self):
            """Returns a set of all redirect labels for this menu's choices."""
            return set(choice.redirect for choice in self.choices)

        def is_valid(self):
            """Checks if the menu is valid (has visible choices and time left)."""
            if self.get_visible_choices_total() <= 0:
                return False
            if menu_manager.time_left <= 0 or self.early_exit:
                return False
            return True

        def get_visible_choices_total(self):
            """Returns the number of visible choices."""
            return sum(1 for choice in self.choices if not choice.hidden and choice.get_condition())

        def hide_specific_choice(self, choice_to_hide):
            """Hides a specific choice by text."""
            for current_choice in self.choices:
                if current_choice.text == choice_to_hide:
                    current_choice.hidden = True
                    current_choice.already_chosen = True

        def display_choices(self):
            """Handles displaying choices and selection logic."""
            if record_mode and len(test_choices) > 0:
                selected_choice_i = test_choices.pop(0)
                selected_choice = self.choices[selected_choice_i]
            else:
                if self.is_map:
                    global selected_floor
                    global current_floor
                    selected_floor = current_floor
                    room_id = renpy.call_screen('in_game_map_menu', timed_menu=self)
                    selected_choice = None
                    for idx, c in enumerate(self.choices):
                        if c.room == room_id and c.get_condition():
                            selected_choice = c
                            selected_choice_i = idx
                else:
                    selected_choice_i = renpy.call_screen('custom_choice', self)
                    selected_choice = self.choices[selected_choice_i]
            if record_mode:
                f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/choices_history.txt", "a")
                f.write(str(selected_choice_i) + ',' + ' # ' + selected_choice.text + '\n')
                f.close()
            if not selected_choice.keep_alive:
                selected_choice.hidden = True
                selected_choice.already_chosen = True
            return selected_choice

        def __str__(self):
            menu_str = ""
            for choice in self.choices:
                if not choice.hidden and ((not choice.condition) or eval(choice.condition)):
                    menu_str += choice.text + "\n"
            return menu_str

    class Room:
        """
        Represents a room for map-based menus.
        Args:
            id (str): Room identifier.
            name (str): Room name.
            floor (str): Floor identifier.
            area_points (list): Area points for the room.
        """
        def __init__(self, id, name, floor, area_points):
            self.id = id
            self.name = name
            self.floor = floor
            self.area_points = area_points 