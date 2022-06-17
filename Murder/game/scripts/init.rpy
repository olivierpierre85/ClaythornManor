# All variables
# 1. Declare All characters used by this game.

define soldier = Character("The Soldier", image="soldier")
define host = Character("The Host")
define nurse = Character("The Nurse")
define drunk = Character("The Drunk")
define butler = Character("The Butler", image="butler")

define doctor = Character("The Doctor", image="doctor")

# image side doctor = "../images/characters/doctor_neutral.png"
# image side doctor surprised = "../images/characters/doctor_surprised.png"


# 2. Characters locked
default char_soldier = True
default char_captain = False

# 3. Objects ( 0 not found, 1 found, 2 in you possession)


# 4. Insights 
# Knowledge acquired in game to unlock some dialogs
define soldier_generic_nurse = 0
define soldier_generic_doctor = 0

# 5. menusets
define menu_soldier_day1_drinks_introduction = set()
define menu_soldier_day1_dinner_introduction = set()