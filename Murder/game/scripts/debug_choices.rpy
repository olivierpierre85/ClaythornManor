label debug_choices:
  menu: 
    "character_selection":
      jump character_selection
    
    # Soldier Possibilities
    # TODO set necessary var selector before soldier selection?
    "soldier_day1_arrival_main":
      
      jump soldier_day1_arrival_main

    "soldier_day1_drinks_main":
      jump soldier_day1_drinks_main

    "soldier_day1_dinner_main":
      $ soldier_generic_nurse = 1
      jump soldier_day1_dinner_main

    "soldier_day1_evening_main":
      jump soldier_day1_evening_main


