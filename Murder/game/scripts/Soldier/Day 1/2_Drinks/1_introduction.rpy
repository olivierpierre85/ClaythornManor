label soldier_day1_drinks_introduction:
  scene tea_room

  soldier "I look around the room, see multiple persons already engage in conversation."
  soldier "Two persons seem alone, a middle age man sitting on a couch, and a young woman"

  $ menu_soldier_day1_drinks_introduction = set()

  jump soldier_day1_drinks_introduction_choice

label soldier_day1_drinks_introduction_choice:  

  show nurse at right

  if "Talk to the man" not in menu_soldier_day1_drinks_introduction:
    show drunk at left

  menu:
    set menu_soldier_day1_drinks_introduction
    "Talk to the man":
        hide nurse
        hide drunk
        jump soldier_day1_drinks_drunk

    "Talk to the woman":
        hide nurse
        hide drunk
        call soldier_day1_drinks_nurse

  narrator "You would like to keep talking, but you are interrupted by the butler entering the room."

  show butler 

  butler "Dinner is served. Please follow me to the dining room."

  hide butler 

  narrator "Everyone moves to the dining room"

  jump soldier_day1_dinner_introduction