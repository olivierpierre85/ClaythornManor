# a label is mandatory for the call expression, because of limitations with the python function (a call can't be returned inside python code)
label run_menu(current_menu):

    if current_menu.is_valid():

        $ selected_choice = current_menu.display_choices()

        call expression current_menu.choices[selected_choice].redirect
        
        call run_menu(current_menu)

    return


init -1 python:
    # Possible choices for a menu
    class TimedMenuChoice:
    
        def __init__(self, text, redirect, choice_time=0, choice_repeat = False, hidden = False, keep_alive = False):
            self.text = text
            self.redirect = redirect
            self.choice_time = choice_time
            self.choice_repeat = choice_repeat
            self.hidden = hidden
            self.keep_alive = keep_alive

    # A Timed
    class TimedMenu:
    
        def __init__(self, choices = [], time_left = 0):
            self.choices = choices
            self.time_left = time_left
    
        def is_valid(self):
            if len(self.get_visible_choices())>0:
                return True
            return False

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

            return selected_choice

