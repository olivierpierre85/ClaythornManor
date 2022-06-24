label soldier_day1_evening_billiard_room:

  "You see multiple people in the room"

  python:
    menu_options = [
      { 
        'text': 'choice 1',
        'redirect': 'to_choice_1',
        'time_spent': 10,
      },
      { 
        'text': 'choice 2222222',
        'redirect': 'to_choice_2',
        'time_spent': 50,
      }
    ]

  call timed_menu(menu_options)

  "You have nothing more to do here"

  return

label to_choice_1:
  "choice 1 is cool"
  return

label to_choice_2:
  "choice 2 is cool"
  return