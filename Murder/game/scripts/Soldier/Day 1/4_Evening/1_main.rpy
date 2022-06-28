label soldier_day1_evening_main:

  $ current_time = "10PM"

  scene bedroom_soldier

  narrator """

  You're entering your bedroom. 

  It is tidy, but a bit run down.

  After checking all your effects are in order, you realize that you still have plenty of time before you could sleep.

  So you go out of your room to go....

  """

  $ time_left = 120

  define soldier_day1_evening_left_bedroom = False

  python:
    menus_options['soldier_day1_evening_main_menu_options'] = [
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
        'text': 'Go to the kitchens',
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

  call timed_menu('soldier_day1_evening_main_menu_options')

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

label soldier_day1_evening_cancel:
  return

# label soldier_day1_evening_scullery:
#   "What the hell is a scullery ?"

#   "Anyway, there is nothing there"

#   return
  
#   # Introduce map choice

#   # reset choices
#   $ menu_map_choices = set()
#   # Set how much time until next phase (min)
#   $ time_left = 120

#   jump soldier_day1_evening_map_choices

# label soldier_day1_evening_map_choices:
#   # TODO add map background
#   if time_left > 0:
#     menu:
#       set menu_map_choices
#       "Meet the others in the billiard room":
#         call soldier_day1_evening_billiard_room
#         $ time_left = time_left - 30
#         jump soldier_day1_evening_map_choices

#       "Go knock on the the door of Amalia Baxter":
#         # TODO only if you got nurse location
#         call soldier_day1_evening_nurse_room
#         $ time_left = time_left - 60
#         jump soldier_day1_evening_map_choices
      
#       "Go to the kitchens":
#         call soldier_day1_evening_kitchens
#         $ time_left = time_left - 60
#         jump soldier_day1_evening_map_choices
      
#       "Go to the scullery":
#         call soldier_day1_evening_scullery
#         $ time_left = time_left - 60
#         jump soldier_day1_evening_map_choices

#       "You give up and go back to your room":
#         # TODO only if you got out a bit
#         $ time_left = 0
#         scene bedroom_soldier
#         jump soldier_day1_evening_map_choices