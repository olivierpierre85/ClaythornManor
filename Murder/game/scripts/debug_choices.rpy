label debug_choices:
  menu: 
    "character_selection":
      jump character_selection
    
    # hero Possibilities
    # TODO set necessary var selector before hero selection?
    "hero_day1_arrival_main":
      
      jump hero_day1_arrival_main

    "hero_day1_drinks_main":
      jump hero_day1_drinks_main

    "hero_day1_dinner_main":
      $ hero_generic_nurse = 1
      jump hero_day1_dinner_main

    "hero_day1_evening_main":
      jump hero_day1_evening_main


