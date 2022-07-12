label hero_day1_drinks_main:

  scene tea_room

  hero "I look around the room, see multiple persons already engage in conversation."
  hero "Two persons seem alone, a middle age man sitting on a couch, and a young woman"

  show nurse at right

  show drunk at left

  $ time_left = 30

  python:
    menus_options['hero_day1_drinks_main'] = [
      { 
        'text': 'Talk to the man',
        'redirect': 'hero_day1_drinks_drunk',
      },
      { 
        'text': 'Talk to the woman',
        'redirect': 'hero_day1_drinks_nurse',
      }
    ]

  call timed_menu('hero_day1_drinks_main')

  narrator "You would like to keep talking, but you are interrupted by the butler entering the room."

  show butler 

  butler "Dinner is served. Please follow me to the dining room."

  hide butler 

  narrator "Everyone moves to the dining room"

  jump hero_day1_dinner_main