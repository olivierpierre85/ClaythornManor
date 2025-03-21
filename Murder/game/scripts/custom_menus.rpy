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

    if change_level:
        $ menu_level += 1

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
        
        $  selected_choice[menu_level] = current_menu.display_choices()
        # $ print(menu_level, selected_choice, selected_choice[menu_level])
        
        # Hide choices when activated
        if current_menu.image_left:
            $ renpy.hide(current_menu.image_left)
        if current_menu.image_right:
            $ renpy.hide(current_menu.image_right)
        if current_menu.image_left_2:
            $ renpy.hide(current_menu.image_left_2)
        if current_menu.image_right_2:
            $ renpy.hide(current_menu.image_right_2)

        if  selected_choice[menu_level].early_exit:
            $ current_menu.early_exit = True        

        call expression selected_choice[menu_level].redirect

        # Change current time
        $ time_diff[menu_level] = None
        if time_left > 0 and  selected_choice[menu_level].time_spent:
            $ time_diff[menu_level] = datetime.combine(date.today(), current_time) + timedelta(minutes=selected_choice[menu_level].time_spent)

        # $ print("CHANGE TIME", menu_level, selected_choice[menu_level].time_spent, time_left)
        if time_diff[menu_level]:
            call change_time(time_diff[menu_level].time().hour, time_diff[menu_level].time().minute)

        pause 0.7

        call run_menu(current_menu, change_level=False)

    if change_level:
        $ menu_level -= 1
    

    $ current_menu.early_exit = False

    return

init -1 python:

    # SAVE in persistent data if the player has visited the map.µ
    # It is supposed to work like the standard menu grey options
    def record_visit(chapter, room_id):
        # Make sure the dictionary for the chapter exists
        if chapter not in persistent.visited_map:
            persistent.visited_map[chapter] = set()

        # Add the room to the chapter’s set
        persistent.visited_map[chapter].add(room_id)

        # Save the persistent data to disk
        renpy.save_persistent()

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
    
        def __init__(self, id, choices = [], is_map = False, image_left = None, image_right = None, image_left_2 = None,image_right_2 = None,):
            self.id = id
            self.choices = choices
            self.is_map = is_map
            self.image_left = image_left
            self.image_right = image_right
            self.image_left_2 = image_left_2
            self.image_right_2 = image_right_2
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
                    # visible_choices.append((choice.text + " {{" + self.id + "}}", i))
                    # Add the direction of the choice in invisible redirect to avoid greying choices with same text ({{}}} hidden in menu screen)
                    visible_choices.append((choice.text + " {{" + choice.redirect + "}}", i))
                    
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
                # print("Selected Choice:" + str(selected_choice))
            elif full_testing_mode:
                # TODO Build a tree to take first option
                # BUT IS MENU ID ENOUGH??? NO we can call this menu multiple time,
                # We also need a Passage id, a real node identifier?
                # NO We need => Correct ID, each choice must have a boolean, is this path full HOW DO THAT?
                if (full_testing_mode_char, self.id) not in decision_tree:
                    decision_tree[(full_testing_mode_char, self.id)] = self.get_visible_choices()

                current_choice = decision_tree[("lad", self.id)].pop()

                print("Id Menu:", self.id)
                print("current_choice:", current_choice)
                current_choice = 0
                (visible_choices_text, visible_choices_i) = self.get_visible_choices()[current_choice]
                  
                selected_choice = self.choices[visible_choices_i]

                f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/full_testing.txt", "a")
                f.write(str(current_choice) + ',' + ' # ' + selected_choice.text + ", " + selected_choice.redirect+ '\n')
                f.close()
            # NORMAL MODE
            else:
                if current_menu.is_map:
                    global selected_floor
                    global current_floor
                    selected_floor = current_floor
                    visited_rooms_for_this_chapter = persistent.visited_map.get(current_menu.id, set())

                    room_id = renpy.call_screen('in_game_map_menu', timed_menu=self)

                    selected_choice = None
                    for idx, c in enumerate(self.choices):
                        if c.room == room_id and c.get_condition():
                            selected_choice = c
                            selected_choice_i = idx
                
                    # Record menu and choice for later run through
                    record_visit(current_menu.id,room_id)
                    
                    # LEGACY, normally not needed? because all choices are filled? TODO CHECK
                    if not selected_choice:
                        selected_choice = TimedMenuChoice('FILLER CHOICE', current_character.text_id + "_" +room_id + '_defaultERROR', 5)
                        self.default_visited.append(room_id) # TODO: Double check the use if this
                        selected_choice_i = -1
                else:
                    selected_choice_i = menu(self.get_visible_choices())
                    selected_choice = self.choices[selected_choice_i]

            # RECORD history to build debug path (TODO should be done all the time?)
            if record_mode:
                f = open("C:/Users/arthu/Documents/VisualNovelProject/Murder/choices_history.txt", "a")
                f.write(str(selected_choice_i) + ',' + ' # ' + selected_choice.text + '\n')
                f.close()

            if not selected_choice.keep_alive:
                selected_choice.hidden = True
                
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
    
    # class Hotspot:
    #     def __init__(
    #         self, 
    #         description, 
    #         position,
    #         area_points, 
    #     ):
    #         self.description = description
    #         self.position = position
    #         self.area_points = area_points



