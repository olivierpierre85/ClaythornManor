label run_menu(current_menu):

    if current_menu.is_valid():

        $ selected_choice = current_menu.display_choices()
        
        if current_menu.choices[selected_choice].early_exit:
            $ current_menu.early_exit = True        
        
        # Change current time
        $ time_diff = None
        if time_left > 0 and current_menu.choices[selected_choice].time_spent:
            $ time_diff = datetime.combine(date.today(), current_time) + timedelta(minutes=current_menu.choices[selected_choice].time_spent)

        call expression current_menu.choices[selected_choice].redirect

        if time_diff:
            call change_time(time_diff.time().hour, time_diff.time().minute)

        call run_menu(current_menu)

    $ current_menu.early_exit = False

    return

init -1 python:
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
        
        def get_condition(self):
            if self.condition:
                return eval(self.condition)

            return True

    # A Timed
    class TimedMenu:
    
        def __init__(self, choices = [], is_map = False):
            self.choices = choices
            self.early_exit = False
            self.is_map = is_map
    
        def is_valid(self):
            if len(self.get_visible_choices()) <= 0:
                return False
                
            if time_left <= 0 or self.early_exit:
                return False
            return True

        def get_visible_choices(self):
            visible_choices = []
            for i, choice in enumerate(self.choices):
                if not choice.hidden and choice.get_condition():
                    visible_choices.append((choice.text, i))
            return visible_choices

        def display_choices(self):

            # DEBUG MODE
            if test_mode and len(test_choices) > 0:
                selected_choice = test_choices.pop(0) 
                print("Selected Choice:" + str(selected_choice))
            # NORMAL MODE
            else:
                if current_menu.is_map:
                    selected_choice = renpy.call_screen('in_game_map_menu', choices=self.choices) 
                else:
                    selected_choice = menu(self.get_visible_choices())

            if not self.choices[selected_choice].keep_alive:
                self.choices[selected_choice].hidden = True

            global time_left
            time_left -= self.choices[selected_choice].time_spent

            return selected_choice

    class Room:
        def __init__(
            self, 
            id,
            name, 
            floor, 
            area_points, 
        ):
            self.id = id
            self.name = name
            self.floor = floor
            self.area_points = area_points
    
    class Hotspot:
        def __init__(
            self, 
            description, 
            position,
            area_points, 
        ):
            self.description = description
            self.position = position
            self.area_points = area_points



