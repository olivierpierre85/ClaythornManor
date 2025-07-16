# Import menu classes
init -1 python:
    from scripts.custom_menu_classes import TimedMenu, TimedMenuChoice, Room

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

init -1 python:
    class MenuManager:
        def __init__(self):
            self.menu_level = 0
            self.selected_choice = {}
            self.all_menus = {}
            self.time_left = 0
            self.time_diff = {}

    menu_manager = MenuManager()

label run_menu(current_menu, change_level=True):

    # For custom choice: Add menu to a structure with menu
    if current_menu.id in menu_manager.all_menus:
        $ current_menu = menu_manager.all_menus[current_menu.id]
    else:
        $ menu_manager.all_menus[current_menu.id] = current_menu

    if change_level:
        $ menu_manager.menu_level += 1
        # Check if there is a selected choice from the previous level.
        # Since selected_choice is a list, we use indexing and check the length.
        if menu_manager.menu_level > 0 and len(menu_manager.selected_choice) >= menu_manager.menu_level and menu_manager.selected_choice[menu_manager.menu_level - 1]:
            $ menu_manager.selected_choice[menu_manager.menu_level - 1].next_menu = current_menu.id

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
        
        $ menu_manager.selected_choice[menu_manager.menu_level] = current_menu.display_choices()
        
        # Hide choices when activated
        if current_menu.image_left:
            $ renpy.hide(current_menu.image_left)
        if current_menu.image_right:
            $ renpy.hide(current_menu.image_right)
        if current_menu.image_left_2:
            $ renpy.hide(current_menu.image_left_2)
        if current_menu.image_right_2:
            $ renpy.hide(current_menu.image_right_2)

        if menu_manager.selected_choice[menu_manager.menu_level].early_exit:
            $ current_menu.early_exit = True        

        call expression menu_manager.selected_choice[menu_manager.menu_level].redirect

        $ menu_manager.time_left -= menu_manager.selected_choice[menu_manager.menu_level].time_spent

        # Change current time
        $ menu_manager.time_diff[menu_manager.menu_level] = None
        if menu_manager.time_left > 0 and menu_manager.selected_choice[menu_manager.menu_level].time_spent:
            $ menu_manager.time_diff[menu_manager.menu_level] = datetime.combine(date.today(), current_time) + timedelta(minutes=menu_manager.selected_choice[menu_manager.menu_level].time_spent)

        if menu_manager.time_diff[menu_manager.menu_level]:
            call change_time(menu_manager.time_diff[menu_manager.menu_level].time().hour, menu_manager.time_diff[menu_manager.menu_level].time().minute)

        pause 0.7

        call run_menu(current_menu, change_level=False)

    if change_level:
        $ menu_manager.menu_level -= 1

    $ current_menu.early_exit = False

    return