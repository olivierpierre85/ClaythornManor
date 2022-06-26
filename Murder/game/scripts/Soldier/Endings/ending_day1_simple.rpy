# Ending for soldier

# DAY 1
# Either the soldier as drank sherry after dinner and die, or he hasn't and is still alive
label soldier_ending_day1:

  if soldier_day1_drank_sherry:
    narrator "Well you are dead now are you"

    # Unlock captain
    $ char_captain = True

    # Ending
    jump character_selection

  elif:
    jump soldier_day2_breakfast_main


