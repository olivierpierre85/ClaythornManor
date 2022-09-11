# All variables
# 1. Declare All characters used by this game.
define characters_knowledge = dict()

define hero_name = "Ted Haring"
define hero  = Character("hero_name", image="hero", dynamic=True)
define nurse_name = "Woman"
define nurse    = Character("nurse_name", image="nurse", dynamic=True)

define psychic_name = "Woman"
define psychic    = Character("psychic_name", image="psychic", dynamic=True)
define characters_knowledge['psychic'] = set()

define doctor_name = "Man in a hat"
define doctor   = Character("doctor_name", image="doctor", dynamic=True)
define host     = Character("The Host", image="host")

define drunk    = Character("The Drunk", image="drunk")
define butler   = Character("The Butler", image="butler")

define broken_name = "Masked Man"
define broken   = Character("broken_name", image="broken", dynamic=True)


# 2. Characters locked
default char_hero = True
default char_captain = False

# 3. Objects ( 0 not found, 1 found, 2 in you possession)

# Actions with impact 
default hero_day1_drinks = 0
default hero_day1_poisoned = False

# 4. Insights 
# Knowledge acquired in game to unlock some dialogs
define hero_generic_nurse = 0
define hero_generic_psychic = 0
define hero_generic_doctor = 0
define hero_nurse_location = False

# Global Variable
init -100 python:
  from datetime import datetime, time, timedelta, date
define time_left = 0
define current_day = "Friday"
# define current_time = "05:00PM" 
define current_time = time(17,00,00)
define hours_angle = 0
define first_display = True

define menus_options = dict()

define current_character = "hero"

define current_floor = 1 # 1 Equal ground floor, 0 is kitchen floor
define tooltip = "Click on a room to move there"
define MIN_FLOOR = 0
define MAX_FLOOR = 1 # TODO Add floors

