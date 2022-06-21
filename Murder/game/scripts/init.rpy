# All variables
# 1. Declare All characters used by this game.

define soldier  = Character("The Soldier", image="soldier")
define host     = Character("The Host", image="host")
define nurse_name = "Woman"
define nurse    = Character("nurse_name", image="nurse", dynamic=True)
define drunk    = Character("The Drunk", image="drunk")
define butler   = Character("The Butler", image="butler")
define doctor   = Character("The Doctor", image="doctor")

# 2. Characters locked
default char_soldier = True
default char_captain = False

# 3. Objects ( 0 not found, 1 found, 2 in you possession)


# 4. Insights 
# Knowledge acquired in game to unlock some dialogs
define soldier_generic_nurse = 0
define soldier_generic_doctor = 0

# 5. menu sets
define menu_soldier_day1_drinks_introduction = set()
define menu_soldier_day1_dinner_introduction = set()

# Re-usable dialogs

define host_welcome_speech = """ 
  Welcome every one. I am sorry to have kept you waiting. Now that we are all gather here, I would like again to show you my gratitude.

  As you already know, you are all here because of an heroic act you've done in the past. 
  
  I took notice of what you've done and took upon me to give you a formal thank you.

  I know the letter inviting you was rather vague, so I will clarify it now.

  My first gift to you, is this stay in my manor. You will fully be catered too, with the most refine food expertly prepared by my personal cook.

  During the three days we will spend together, we'll also enjoy various activities I am sure you will love

  The second gift, is a price of ten thousands pounds to share among yourselves. It's my way to thank people so selfless as to help other people.
  """