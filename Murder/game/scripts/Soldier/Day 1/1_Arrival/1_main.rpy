# Introduction for soldier
label soldier_day1_arrival_main:

  # TODO Menu Image
  scene great_hall

  # First Part, train explanation
  soldier "After a long journey, I finally reached my destination : Mandrake Manor"
  soldier "A footman opens the main entrance for me, and someone greets me"

  # Arrival to manor

  # Entrance in Manor
  # show host at truecenter
  show butler
  
  butler "Welcome Sir. We are glad to see you."

  butler "Please give your bags to the footman, he will carry them to your room."

  butler "And if you are ready, you can have some drinks before dinner? Not everyone has arrived yet."
  
  hide butler

  # Ending
  jump soldier_day1_drinks_main
