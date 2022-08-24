init python:
  hero_day1_evening_menu = TimedMenu([
    TimedMenuChoice('Go knock on the the door of Amalia Baxter', 'hero_day1_evening_nurse_room', 40, condition = 'hero_nurse_location'), # TODO aDD condition
    TimedMenuChoice('Meet the others in the billiard room', 'hero_day1_evening_billiard_room', 10, keep_alive = True),
    TimedMenuChoice('Go have a look in the library', 'hero_day1_evening_library', 40),
    TimedMenuChoice('Go downstairs to visit the kitchens', 'hero_day1_evening_kitchens', 10),
    TimedMenuChoice('You give up and go back to your room', 'hero_day1_evening_cancel', early_exit = True)# TODO aDD condition
  ])

label hero_day1_evening:

  $ current_time = "10PM"

  scene bedroom_hero

  narrator """

  You're entering your bedroom. 

  It is tidy, but a bit run down.

  After checking all your effects are in order, you realize that you still have plenty of time before you could sleep.

  So you go out of your room to ....

  """

  $ time_left = 120

  define hero_day1_evening_left_bedroom = False

  $ current_menu = hero_day1_evening_menu
  call run_menu(current_menu)
  $ current_menu =  None

  # python:
  #   menus_options['hero_day1_evening'] = [
  #     { 
  #       'text': 'Go knock on the the door of Amalia Baxter',
  #       'redirect': 'hero_day1_evening_nurse_room',
  #       'time_spent': 60,
  #       'condition': 'hero_nurse_location',
  #     },
  #     { 
  #       'text': 'Meet the others in the billiard room',
  #       'redirect': 'hero_day1_evening_billiard_room',
  #       'time_spent': 10,
  #       'keep_alive': True,
  #     },
  #     { 
  #       'text': 'Go have a look in the library.',
  #       'redirect': 'hero_day1_evening_library',
  #       'time_spent': 10,
  #     },
  #     { 
  #       'text': 'Go downstairs to visit the kitchens',
  #       'redirect': 'hero_day1_evening_kitchens',
  #       'time_spent': 10,
  #     },
  #     { 
  #       'text': 'You give up and go back to your room',
  #       'redirect': 'hero_day1_evening_cancel',
  #       'condition': 'hero_day1_evening_left_bedroom',
  #       'time_spent': 0,
  #       'early_exit': True,
  #     },
  #   ]

  # call timed_menu('hero_day1_evening')

  "Feeling tired, you decide it's late enough and you go to bed."

  scene bedroom_hero

  "You Notice something on your bed. a letter."

  # TODO play music SCARY

  # SHOW PNG LETTER.

  if hero_day1_drank_sherry:

    jump hero_ending_day1_poisoned

  else:

    jump hero_day2_breakfast
  
label hero_day1_evening_kitchens:

  $ hero_day1_evening_left_bedroom = True

  scene hallway

  show butler

  butler "I am sorry sir, but the kitchen is for the staff only."

  hide butler

  return

label hero_day1_evening_library:

  $ hero_day1_evening_left_bedroom = True
  
  "You look around the library."

  hero "Why am I doing here ? I can barely read."

  "On a reading table, you see a book still open."

  "You check the title."

  "\"A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.\""

  hero "Yeah, I am not reading that."

  "You leave the library."

  # TODO add trivia, The hero can't read well

  return

label hero_day1_evening_cancel:
  return