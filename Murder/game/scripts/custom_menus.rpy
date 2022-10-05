transform character_choice_left:
  xpos 100  
  ypos 300

transform character_choice_right:
  zoom 1
  xpos 1600  
  ypos 300

label run_menu(current_menu):

    if current_menu.is_valid():
        $ print(current_menu.default_visited)
        # Show characters when activated
        if current_menu.image_left:
            $ renpy.show(current_menu.image_left, at_list=[character_choice_left])
        if current_menu.image_right:
            $ renpy.show(current_menu.image_right, at_list=[character_choice_right])

        $ selected_choice = current_menu.display_choices()

        # Hide choices when activated
        if current_menu.image_left:
            $ renpy.hide(current_menu.image_left)
        if current_menu.image_right:
            $ renpy.hide(current_menu.image_right)

        if selected_choice.early_exit:
            $ current_menu.early_exit = True        
        
        # Change current time
        $ time_diff = None
        if time_left > 0 and selected_choice.time_spent:
            $ time_diff = datetime.combine(date.today(), current_time) + timedelta(minutes=selected_choice.time_spent)

        call expression selected_choice.redirect

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
    
        def __init__(self, choices = [], is_map = False, image_left = None, image_right = None):
            self.choices = choices
            self.is_map = is_map
            self.image_left = image_left
            self.image_right = image_right
            self.early_exit = False
            self.default_visited = []
    
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
                selected_choice_i = test_choices.pop(0) 
                selected_choice = self.choices[selected_choice_i]
                print("Selected Choice:" + str(selected_choice))
            # NORMAL MODE
            else:
                if current_menu.is_map:
                    room_id = renpy.call_screen('in_game_map_menu', timed_menu=self)

                    selected_choice = None
                    for c in self.choices:
                        if c.room == room_id:
                            selected_choice = c
                    
                    if not selected_choice:
                        selected_choice = TimedMenuChoice('FILLER CHOICE', room_id + '_default', 5)
                        self.default_visited.append(room_id)
                else:
                    selected_choice_i = menu(self.get_visible_choices())
                    selected_choice = self.choices[selected_choice_i]

            if not selected_choice.keep_alive:
                selected_choice.hidden = True

            global time_left
            time_left -= selected_choice.time_spent

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



