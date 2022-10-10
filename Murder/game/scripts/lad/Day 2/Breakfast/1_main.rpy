label lad_day2_breakfast:

  call black_screen_transition("The Lad - Day 2")

  scene bedroom_lad with irisout

  "You slept through the night."

  if (lad_day1_drinks > 2):
    "You have a bad hangover. But you'll power through."
  
  "After getting ready, you leave your room to have breakfast."

  scene dining_room

  "Most of the guests are already in the dining room."

  "You seat at the same place that you did yesterday."