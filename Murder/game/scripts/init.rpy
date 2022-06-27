# All variables
# 1. Declare All characters used by this game.
define soldier_name = "Ted Haring"
define soldier  = Character("soldier_name", image="soldier", dynamic=True)
define nurse_name = "Woman"
define nurse    = Character("nurse_name", image="nurse", dynamic=True)
define doctor_name = "Man in a hat"
define doctor   = Character("doctor_name", image="doctor", dynamic=True)
define host     = Character("The Host", image="host")

define drunk    = Character("The Drunk", image="drunk")
define butler   = Character("The Butler", image="butler")


# 2. Characters locked
default char_soldier = True
default char_captain = False

# 3. Objects ( 0 not found, 1 found, 2 in you possession)

# Actions with impact 
default soldier_day1_drank_sherry = False
default soldier_day1_drank_sherry_2 = False
default soldier_day1_drank_sherry_3 = False

# 4. Insights 
# Knowledge acquired in game to unlock some dialogs
define soldier_generic_nurse = 0
define soldier_generic_doctor = 0
define soldier_nurse_location = False

# 5. menu sets TODO Not necessary
define menu_soldier_day1_drinks_main = set()
define menu_soldier_day1_dinner_main = set()
define menu_nurse_generic = set()
define menu_doctor_generic = set()
define menu_map_choices = set()

# Global Variable
define time_left = 0
define current_day = "Friday"
define current_time = "5PM"

# Global Variable to allow nested menus
define menus_options = dict()
# define choice_time_spent = dict()
# define choice_redirect = dict()
define choice_early_exit = dict()
# define choices_left = dict()

# Functions
# NOT BETTER, the call returns to the root of the call
# init python:
#   def function_menu(menu_options = [], menu_id = ""):
#     renpy.say("test", "fct " + menu_id)

#     choices = []
#     for i, item in enumerate(menu_options):
#       if (not item.has_key('condition')) or eval(item['condition']):
#         choices.append((item['text'], i)) 
#     # read choices
#     choice = menu(choices)

#     choice_time_spent = menu_options[choice]['time_spent']
#     choice_redirect = menu_options[choice]['redirect']
#     choice_early_exit = menu_options[choice].has_key('early_exit') and menu_options[choice]['early_exit']

#     # time_left -= choice_time_spent

#     # Delete current options from the choices TODO NOT IF MULTIPLE CALL Possible
#     del menu_options[choice]

#     choices_left = len(menu_options) 
#     renpy.say("test", "choice:" + str(choice))
#     # renpy.say("test", "time_consumed :[choice_time_spent], redirection: [choice_redirect], time left: [time_left], early exit: [choice_early_exit], choices_left: [choices_left]")

#     renpy.say("test","WTF IN function :Calls redirect, from " + menu_id)
#     renpy.call(choice_redirect)
#     first_choice = menu_options[0]['text']
#     renpy.say("test","WTF IN function :Leaves redirect in " + menu_id + ", first choice " + first_choice)

#   # # Jump back to start of menu if any time left, options still exist, and early exit is not set
#   # if len(menu_options) == 0:
#   #   "You have nothing more to do here"
#   #   return
  
#   # if time_left <= 0:
#   #   "no more time"
#   #   return

#     if choice_early_exit:
#       "early exit"
#       return

#     function_menu(menu_options, menu_id)