# All variables
# 1. Declare All characters used by this game.
define hero_name = "Ted Haring"
define hero  = Character("hero_name", image="hero", dynamic=True)
define nurse_name = "Woman"
define nurse    = Character("nurse_name", image="nurse", dynamic=True)
define doctor_name = "Man in a hat"
define doctor   = Character("doctor_name", image="doctor", dynamic=True)
define host     = Character("The Host", image="host")

define drunk    = Character("The Drunk", image="drunk")
define butler   = Character("The Butler", image="butler")


# 2. Characters locked
default char_hero = True
default char_captain = False

# 3. Objects ( 0 not found, 1 found, 2 in you possession)

# Actions with impact 
default hero_day1_drank_sherry = False
default hero_day1_drank_sherry_2 = False
default hero_day1_drank_sherry_3 = False

# 4. Insights 
# Knowledge acquired in game to unlock some dialogs
define hero_generic_nurse = 0
define hero_generic_doctor = 0
define hero_nurse_location = False

# Global Variable
define time_left = 0
define current_day = "Friday"
define current_time = "5PM"

define menus_options = dict()

define current_character = "hero"

# Generic menu
#TODO how to have it in the right file ?
init python:
  menus_options['nurse_generic_choices'] = [
    { 
      'text': 'What do you do in life ?',
      'redirect': 'nurse_generic_job',
      'time_spent': 20,
    },
    { 
      'text': 'Why were you invited here ?',
      'redirect': 'nurse_generic_heroic_act',
      'time_spent': 10,
    },
    { 
      'text': 'What do you think of this place',
      'redirect': 'nurse_generic_manor',
      'time_spent': 10,
    },
    { 
      'text': 'Where are you from',
      'redirect': 'nurse_generic_background',
      'time_spent': 10,
    },
    { 
      'text': 'You have nothing more to ask',
      'redirect': 'nurse_generic_cancel',
      'time_spent': 0,
      'early_exit': True,
      'keep_alive': True,
    },
  ]