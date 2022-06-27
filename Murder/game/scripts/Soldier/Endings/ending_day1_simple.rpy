# Ending for soldier

# DAY 1
# Either the soldier as drank sherry after dinner and die, or he hasn't and is still alive
label soldier_ending_day1_poisoned:
  narrator "Well you are dead now are you"

  # Unlock captain
  $ char_captain = True

  # Ending
  jump character_selection


