# Introduction for hero
label lad_day1_arrival:

  #TODO show from exterior

  # TODO Menu Image
  scene great_hall

  # First Part, train explanation
  lad "I finally reached my destination."
  lad "While the driver is unloading my bags from the car, a butler opens the main entrance and greets me."

  # show host at truecenter
  # show butler at truecenter

  butler """

  Welcome Sir. May I help you ?

  """

  lad "Hello, I am Ted Harring, I was invited by Lady TODO"

  $ lad_details.introduce()

  butler """

  Yes, of course Mr Harring.

  Welcome at Claythorn Manor.

  I am afraid you won't have time to go change right now. 
  Everyone is already there, and our host will be greeting all of you very soon.

  So if you follow me into the tea room, you can join the rest of the party for some drinks.
  
  """
  
  hide butler

  jump lad_day1_drinks
