label soldier_day1_drinks_introduction:
  scene tea_room

  soldier "I look around the room, see multiple persons already engage in conversation."
  soldier "Two persons seem alone, a middle age man sitting on a couch, and a young woman"

  $ menu_soldier_day1_drinks_introduction = set()

  jump soldier_day1_drinks_introduction_choice

label soldier_day1_drinks_introduction_choice:  

  menu:
    set menu_soldier_day1_drinks_introduction
    "Talk to the man":
        jump soldier_day1_drinks_drunk

    "Talk to the woman":
        jump soldier_day1_drinks_nurse