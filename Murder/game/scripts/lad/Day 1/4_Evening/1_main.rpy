label lad_day1_evening:

  call change_time(22,00)

  scene bedroom_hero

  # narrator """

  # You're entering your bedroom. 

  # It is tidy, but a bit run down.

  # After checking all your effects are in order, you realize that you still have plenty of time before you could sleep.

  # So you go out of your room to ....

  # """

  "You go to"

  $ time_left = 120

  define lad_day1_evening_left_bedroom = False

  $ lad_day1_evening_menu = TimedMenu([
    TimedMenuChoice('Go knock on the the door of Amalia Baxter', 'lad_day1_evening_nurse_room', 55, room = 'psychic_room'),
    TimedMenuChoice('Meet the others in the billiard room', 'lad_day1_evening_billiard_room', 0, keep_alive = True, room = 'billiard_room'),
    TimedMenuChoice('Go have a look in the library', 'lad_day1_evening_library', 40, room = 'library'),
    TimedMenuChoice('Go downstairs to visit the kitchens', 'lad_day1_evening_kitchens', 10, room = 'kitchens'),
    TimedMenuChoice('You give up and go back to your room', 'lad_day1_evening_cancel', early_exit = True, room = 'lad_room')
  ], is_map = True)

  call run_menu(lad_day1_evening_menu)

  call change_time(23,59)

  "You are now feeling tired, you decide it's late enough and you go to bed."

  scene bedroom_hero

  "You Notice something on your bed. a letter."

  # TODO play music SCARY

  # SHOW PNG LETTER.

  # if lad_day1_poisoned:

  jump lad_ending_day1_poisoned

  # else:

  #   jump lad_day2_breakfast
  
label lad_day1_evening_kitchens:

  $ lad_day1_evening_left_bedroom = True

  scene hallway

  show butler at truecenter

  butler "I am sorry sir, but the kitchen is for the staff only."

  hide butler

  return

label lad_day1_evening_library:

  $ lad_day1_evening_left_bedroom = True
  
  "You look around the library."

  lad "Why am I doing here ? I can barely read."

  "On a small table, you see a open book."

  "You check the title."

  "\"A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.\""

  lad "Yeah, I am not reading that."

  "You leave the library."

  # TODO add trivia, The lad can't read well

  return

label lad_day1_evening_cancel:
  return