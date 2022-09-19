# All variables
# 1. Declare All characters used by this game.
default characters_knowledge = dict()

# TODO find a way to extend say_dialog instead of copying everything
style hero_style:
    properties gui.text_properties("dialogue")
    color "#9c1a1a"
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos - 17

define nurse_name = "Woman"
define nurse    = Character("nurse_name", image="nurse", dynamic=True)

define psychic_name = "Woman"
define psychic    = Character("psychic_name", image="psychic", dynamic=True)


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
