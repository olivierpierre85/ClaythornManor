# Ending for hero

# DAY 1
# Either the hero as drank sherry after dinner and die, or he hasn't and is still alive
label hero_ending_day1_poisoned:

  # Add sad sound

  """

    You don't wake up. 

    You died during the night.

    It's unfair, I know. You don't think that you did anything wrong. 

    And you probably didn't.

    But in life, people often die without knowing why. 
    
    Even thought we always believe being the hero in our story, sometimes we are just pawns.

    Don't worry, you'll have more chances at changing the fate of this character.

    You can start again now. Ideally, you have learn something that will help you in your next attempts.

    But maybe you have learned nothing.

    In this case, you'll better try to look at the story from a different point of view.

    You see, this story is not about only one hero.

    You'll get to play different characters.

    And you'll have to. 
    
    Because otherwise, you'll never discover to whole Truth of what happened this week-end, at Mandrake Castle.

  """

  # Unlock captain
  $ char_captain = True

  # Ending
  jump character_selection


