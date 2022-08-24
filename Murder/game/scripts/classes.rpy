# a label is mandatory for the call expression, because of limitations with the python function (a call can't be returned inside python code)
label run_menu(current_menu, return_menu = None):
    $ print(len(current_menu.choices))
    if current_menu.is_valid():
        $ print("Menu Valid")
        $ selected_choice = current_menu.display_choices()

        $ print(current_menu.choices[selected_choice].text)
        $ print("Call " + current_menu.choices[selected_choice].redirect)
        call expression current_menu.choices[selected_choice].redirect

        if current_menu.choices[selected_choice].early_exit:
            if return_menu:
                call run_menu(return_menu)
            else:
                return
        else:
            call run_menu(current_menu, return_menu)

    if return_menu:
        call run_menu(return_menu)

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
            early_exit = False
        ):
            self.text = text
            self.redirect = redirect
            self.time_spent = time_spent
            self.choice_repeat = choice_repeat
            self.hidden = hidden
            self.keep_alive = keep_alive
            self.early_exit = early_exit

    # A Timed
    class TimedMenu:
    
        def __init__(self, choices = []):
            self.choices = choices
    
        def is_valid(self):
            if len(self.get_visible_choices())<=0:
                return False
            if time_left <= 0:
                return False
            return True

        def get_visible_choices(self):
            visible_choices = []
            for i, choice in enumerate(self.choices):
                if not choice.hidden:
                    visible_choices.append((choice.text, i))
            return visible_choices

        def display_choices(self):
            selected_choice = menu(self.get_visible_choices())

            if not self.choices[selected_choice].keep_alive:
                self.choices[selected_choice].hidden = True

            global time_left
            time_left -= self.choices[selected_choice].time_spent

            return selected_choice

