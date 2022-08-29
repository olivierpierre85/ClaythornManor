# init python:
  # hero_day1_evening_menu = TimedMenu([
  #   TimedMenuChoice('Go knock on the the door of Amalia Baxter', 'hero_day1_evening_nurse_room', 40, condition = 'hero_nurse_location'), # TODO aDD condition
  #   TimedMenuChoice('Meet the others in the billiard room', 'hero_day1_evening_billiard_room', 10, keep_alive = True),
  #   TimedMenuChoice('Go have a look in the library', 'hero_day1_evening_library', 40),
  #   TimedMenuChoice('Go downstairs to visit the kitchens', 'hero_day1_evening_kitchens', 10),
  #   TimedMenuChoice('You give up and go back to your room', 'hero_day1_evening_cancel', early_exit = True)# TODO aDD condition
  # ])

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

  $ hero_day1_evening_menu = TimedMenu([
    TimedMenuChoice('Go knock on the the door of Amalia Baxter', 'hero_day1_evening_nurse_room', 40, condition = 'hero_nurse_location'),
    TimedMenuChoice('Meet the others in the billiard room', 'hero_day1_evening_billiard_room', 10, keep_alive = True),
    TimedMenuChoice('Go have a look in the library', 'hero_day1_evening_library', 40),
    TimedMenuChoice('Go downstairs to visit the kitchens', 'hero_day1_evening_kitchens', 10),
    TimedMenuChoice('You give up and go back to your room', 'hero_day1_evening_cancel', early_exit = True)
  ])

  call run_menu(hero_day1_evening_menu)

  "You are now feeling tired, you decide it's late enough and you go to bed."

  scene bedroom_hero

  "You Notice something on your bed. a letter."

  # TODO play music SCARY

  # SHOW PNG LETTER.

  if hero_day1_poisoned:

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

  "On a small table, you see a open book."

  "You check the title."

  "\"A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.\""

  hero "Yeah, I am not reading that."

  "You leave the library."

  # TODO add trivia, The hero can't read well

  return

label hero_day1_evening_cancel:
  return