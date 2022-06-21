label debug_choices:
  menu: 
    "character_selection":
      jump character_selection
    
    # Soldier Possibilities
    # TODO set necessary var selector before soldier selection?
    "soldier_day1_arrival_introduction":
      
      jump soldier_day1_arrival_introduction

    "soldier_day1_drinks_introduction":
      jump soldier_day1_drinks_introduction

    "soldier_day1_dinner_introduction":
      $ soldier_generic_nurse = 1
      jump soldier_day1_dinner_introduction


