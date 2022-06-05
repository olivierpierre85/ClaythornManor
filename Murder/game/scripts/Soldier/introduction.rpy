# Introduction for soldier
label soldier_introduction:

  # First Part, train explanation
  soldier "After a long journey, I finally reach my destination : Mandrake Manor"
  soldier "A footman opens the main entrance for me, and someone greets me"

  # Arrival to manor

  # Entrance in Manor
  show host happy at truecenter
  host "Welcome Welcome have some drinks before diner, not everyone has arrived yet."
  hide host

  # Ending
  jump soldier_day1_drinks_introduction
