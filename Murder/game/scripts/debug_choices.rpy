label debug_choices:
  python:
    test_mode = True
    test_choices = []

    hero_dinner_simple = [
        0, # Talk to the man => not needed?
        1, # Talk to the woman
        3, # Learn nothing about the psychic
      ]

    hero_evening_simple = hero_dinner_simple + [
      0, # Doctor
      3, # Early leave
      1, # Psychic
      3, # Early leave
    ]

    hero_evening_doctor = hero_dinner_simple + [
      0, # Learn about the doctor Doctor 
      0,
      1,
      3, # Early leave
      1, # Psychic
      3, # Early leave
    ]

    hero_end_day1_doctor = hero_evening_doctor + [
      0, # Learn about the doctor Doctor 
      0,
      1,
      3, # Early leave
      1, # Psychic
      3, # Early leave
    ]
    
  menu: 
    "character_selection":
      jump character_selection

    "Hero Drinks":
      $ test_choices = []
      jump hero_introduction

    "Hero Dinner":
      $ test_choices = hero_dinner_simple
      jump hero_introduction

    "Hero Evening":
      # $ test_choices = hero_evening_simple
      $ test_choices = hero_evening_doctor
      jump hero_introduction

    "hero_day1_evening":
      jump hero_day1_evening
      


