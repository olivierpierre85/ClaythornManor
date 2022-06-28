# Introduction for soldier
label soldier_day1_arrival_main:

  # TODO Menu Image
  scene great_hall

  # First Part, train explanation
  soldier "I finally reached my destination."
  soldier "A butler opens the main entrance for me, and greets me"

  # show host at truecenter
  show butler
  

  butler """

  Welcome Sir. We are glad to see you.

  Please give your bags to the footman, he will carry them to your room.

  I am afraid you won't have time to go change right now.
  
  Everyone is already there, and our will be greeting you very soon.

  So if you follow me into the tea room, you can join the rest of the party for some drinks.
  
  """
  
  hide butler

  jump soldier_day1_drinks_main
