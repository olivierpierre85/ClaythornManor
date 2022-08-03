label hero_day1_drinks:

  scene tea_room

  hero "I look around the room, see multiple persons already engage in conversation."
  hero "Two persons seem alone, a middle age man sitting on a couch, and a young woman"

  show psychic at character_choice_right

  show drunk at character_choice_left

  $ time_left = 30
    
  $ current_menu = TimedMenu([
      TimedMenuChoice('Talk To the man', 'hero_day1_drinks_drunk'),
      TimedMenuChoice('Talk To the woman', 'hero_day1_drinks_psychic')
    ])
  call run_menu(current_menu)

  narrator "You would like to keep talking, but you are interrupted by the butler entering the room."

  show butler 

  butler "Dinner is served. Please follow me to the dining room."

  hide butler 

  narrator "Everyone moves to the dining room"

  jump hero_day1_dinner