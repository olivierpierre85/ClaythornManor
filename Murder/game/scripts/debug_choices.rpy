label debug_choices:
  menu: 
    "character_selection":
      jump character_selection
    
    # hero Possibilities
    # TODO set necessary var selector before hero selection?
    "hero_day1_arrival":
      
      jump hero_day1_arrival

    "hero_day1_drinks":
      jump hero_day1_drinks

    "hero_day1_dinner":
      $ hero_generic_nurse = 1
      jump hero_day1_dinner

    "hero_day1_evening":
      jump hero_day1_evening

    "Test Hero full run":
      $ test_mode = True
      jump hero_day1_arrival
      


