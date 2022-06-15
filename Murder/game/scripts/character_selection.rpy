label character_selection:
  scene
  narrator "Select Your Character"

  menu:
    "The Soldier":
      jump soldier_day1_arrival_introduction

    "The Captain (Locked)" if char_captain:
      narrator "You lose old fart 2 save"