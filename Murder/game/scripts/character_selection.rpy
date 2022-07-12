label character_selection:
  scene
  narrator "Select Your Character"

  menu:
    "The hero":
      jump hero_introduction

    "The Captain (New)" if char_captain:
      jump captain_day1_arrival