label character_selection:
  scene
  narrator "Select Your Character"

  menu:
    "The Soldier":
      jump soldier_day1_arrival_main

    "The Captain (New)" if char_captain:
      jump captain_day1_arrival_main