# Introduction for soldier
label soldier_day1_arrival_introduction:

  # TODO Menu Image
  scene great_hall

  # First Part, train explanation
  soldier "After a long journey, I finally reached my destination : Mandrake Manor"
  soldier "A footman opens the main entrance for me, and someone greets me"

  # Arrival to manor

  # Entrance in Manor
  show host at truecenter
  host "Welcome Sir. We are glad to see you. Have some drinks before diner, not everyone has arrived yet."
  hide host

  # Ending
  jump soldier_day1_drinks_introduction
