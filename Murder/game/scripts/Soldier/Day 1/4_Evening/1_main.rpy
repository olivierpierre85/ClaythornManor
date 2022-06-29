label soldier_day1_evening_main:

  $ current_time = "10PM"

  scene bedroom_soldier

  narrator """

  You're entering your bedroom. 

  It is tidy, but a bit run down.

  After checking all your effects are in order, you realize that you still have plenty of time before you could sleep.

  So you go out of your room to ....

  """

  $ time_left = 120

  define soldier_day1_evening_left_bedroom = False

  python:
    menus_options['soldier_day1_evening_main'] = [
      { 
        'text': 'Go knock on the the door of Amalia Baxter',
        'redirect': 'soldier_day1_evening_nurse_room',
        'time_spent': 60,
        'condition': 'soldier_nurse_location',
      },
      { 
        'text': 'Meet the others in the billiard room',
        'redirect': 'soldier_day1_evening_billiard_room',
        'time_spent': 10,
        'keep_alive': True,
      },
      { 
        'text': 'Go have a look in the library.',
        'redirect': 'soldier_day1_evening_library',
        'time_spent': 10,
      },
      { 
        'text': 'Go downstairs to visit the kitchens',
        'redirect': 'soldier_day1_evening_kitchens',
        'time_spent': 10,
      },
      { 
        'text': 'You give up and go back to your room',
        'redirect': 'soldier_day1_evening_cancel',
        'condition': 'soldier_day1_evening_left_bedroom',
        'time_spent': 0,
        'early_exit': True,
      },
    ]

  call timed_menu('soldier_day1_evening_main')

  "Feeling tired, you decide it's late enough and you go to bed."

  scene bedroom_soldier

  "You Notice something on your bed. a letter."

  # TODO play music SCARY

  # SHOW PNG LETTER.

  if soldier_day1_drank_sherry:

    jump soldier_ending_day1_poisoned

  else:

    jump soldier_day2_breakfast_main
  
label soldier_day1_evening_kitchens:

  $ soldier_day1_evening_left_bedroom = True

  scene hallway

  show butler

  butler "I am sorry sir, but the kitchen is for the staff only."

  hide butler

  return

label soldier_day1_evening_library:

  $ soldier_day1_evening_left_bedroom = True
  
  "You look around the library."

  soldier "Why am I doing here ? I can barely read."

  "On a reading table, you see a book still open."

  "You check the title."

  "\"A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain.\""

  soldier "Yeah, I am not reading that."

  "You leave the library."

  # TODO add trivia, The soldier can't read well

  return

label soldier_day1_evening_cancel:
  return