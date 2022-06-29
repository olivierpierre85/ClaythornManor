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
# define menu_soldier_day1_drinks_main = set()
define menu_soldier_day1_dinner_main = set()
define menu_nurse_generic = set()
define menu_doctor_generic = set()
define menu_map_choices = set()

# Global Variable
define time_left = 0
define current_day = "Friday"
define current_time = "5PM"

define menus_options = dict()

# Generic menu