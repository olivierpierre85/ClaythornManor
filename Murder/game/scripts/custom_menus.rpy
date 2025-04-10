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

    # For custom choice: Add menu to a structure with menu
    if current_menu.id in all_menus:
        $ current_menu = all_menus[current_menu.id]
    else:
        $ all_menus[current_menu.id] = current_menu

    if change_level:
        $ menu_level += 1
        # Check if there is a selected choice from the previous level.
        # Since selected_choice is a list, we use indexing and check the length.
        if menu_level > 0 and len(selected_choice) >= menu_level and selected_choice[menu_level - 1]:
            $ selected_choice[menu_level - 1].next_menu = current_menu.id

    if current_menu.is_valid():
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

        call expression selected_choice[menu_level].redirect

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
            already_chosen = False, 
            next_menu = None
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
        
        def get_condition(self):
            if self.condition:
                return eval(self.condition)

            return True

        def is_completed(self):
            if not self.already_chosen:
                return False
            elif self.already_chosen and not self.next_menu:
                return True
            else:
                # When already selected we need to check if the next menu is completed
                if self.next_menu not in all_menus:
                    return False 

                for choice in all_menus[self.next_menu].choices:
                    # if the condition is not met (invisible), skip the test
                    if not choice.get_condition():
                        continue
                    # A choice is seen as completed if it is a keep alive without a menu,
                    # or if it is itself completed 
                    if not (choice.keep_alive and not choice.next_menu) and not choice.is_completed():
                        return False

                return True

    # A Timed
    class TimedMenu:
    
        def __init__(self, id, choices = [], is_map = False, image_left = None, image_right = None, image_left_2 = None,image_right_2 = None,):
            self.id = id
            self.choices = choices
            self.is_map = is_map
            self.image_left = image_left
            self.image_right = image_right
            self.image_left_2 = image_left_2
            self.image_right_2 = image_right_2
            self.early_exit = False
            # self.default_visited = []
    
        def get_all_redirects(self):
            all_redirects = set()
            for choice in self.choices:
                all_redirects.add(choice.redirect)
            
            return all_redirects

        def is_valid(self):
            if self.get_visible_choices_total() <= 0:
                return False
                
            if time_left <= 0 or self.early_exit:
                return False

            return True

        def get_visible_choices_total(self):
            visible_choices = 0
            for i, choice in enumerate(self.choices):
                if not choice.hidden and choice.get_condition():
                    visible_choices += 1
                    
            return visible_choices
        
        def hide_specific_choice(self, choice_to_hide):
            for current_choice in self.choices:
                if current_choice.text == choice_to_hide:
                    current_choice.hidden = True


        def display_choices(self):

            # DEBUG MODE
            if record_mode and len(test_choices) > 0:
                selected_choice_i = test_choices.pop(0) 
                selected_choice = self.choices[selected_choice_i]
            else:
                if current_menu.is_map:
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

            # RECORD history to build debug path (TODO should be done all the time?)
            if record_mode:
                f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/choices_history.txt", "a")
                f.write(str(selected_choice_i) + ',' + ' # ' + selected_choice.text + '\n')
                f.close()

            if not selected_choice.keep_alive:
                selected_choice.hidden = True
                selected_choice.already_chosen = True
                
            global time_left
            time_left -= selected_choice.time_spent

            return selected_choice

        def __str__(self):
            menu_str = ""
            for choice in self.choices:
                if not choice.hidden and ((not choice.condition) or eval(choice.condition)):
                    menu_str += choice.text + "\n"
            return menu_str

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