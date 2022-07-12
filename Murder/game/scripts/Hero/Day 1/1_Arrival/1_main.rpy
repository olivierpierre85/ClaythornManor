# Introduction for hero
label hero_day1_arrival_main:

  #TODO show from exterior

  # TODO Menu Image
  scene great_hall

  # First Part, train explanation
  hero "I finally reached my destination."
  hero "While the driver is unloading my bags from the car, a butler opens the main entrance and greets me."

  # show host at truecenter
  show butler

  butler """

  Welcome Sir. We are glad to see you.

  I am afraid you won't have time to go change right now.
  
  Everyone is already there, and our host will be greeting all of you very soon.

  So if you follow me into the tea room, you can join the rest of the party for some drinks.
  
  """
  
  hide butler

  jump hero_day1_drinks_main
