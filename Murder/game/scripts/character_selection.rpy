label character_selection:
  system "Select Your Character"

  menu:
    "The Soldier":
        jump soldier_introduction

    "The Captain (Locked)" if char_captain:
        system "You lose old fart 2 save"