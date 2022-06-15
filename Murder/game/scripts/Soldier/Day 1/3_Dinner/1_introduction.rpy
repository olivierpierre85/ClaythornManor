# Introduction for soldier
label soldier_day1_dinner_introduction:

  show butler happy
  butler "Diner is served"

  narrator "Everyone moves to the dining room"

  scene dining_hall

  narrator "You're ended up sitting between the nurse you talked to before, and a middle aged man"

  $ menu_soldier_day1_dinner_introduction = set()

  jump soldier_day1_dinner_introduction_choice

label soldier_day1_dinner_introduction_choice:  

  menu:
    set menu_soldier_day1_dinner_introduction
    "Talk to the man":
        jump soldier_day1_dinner_doctor

    "Talk to the nurse":
        jump soldier_day1_dinner_nurse
