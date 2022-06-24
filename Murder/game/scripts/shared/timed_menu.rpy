label timed_menu(menu_options = []):

  python:
    # choices = [(item[0], i) for i, item in enumerate(menu_options)]
    choices = [(item['text'], i) for i, item in enumerate(menu_options)]
    choice = menu(choices)

  # $ result = renpy.display_menu([ ("East", "east"), ("West", "west") ])
  # call expression 'to_choice_'+choice

  # Add time 
  $ choice_time_spent = menu_options[choice]['time_spent']
  $ choice_redirect = menu_options[choice]['redirect']

  # Jump back to start of menu if any time left
  "choice: [choice], time_consumed :[choice_time_spent], redirection: [choice_redirect], time left: [time_left]"

  call expression choice_redirect

  $ time_left -= choice_time_spent

  $ del menu_options[choice]

  if time_left > 0 and len(menu_options) > 0:
    call timed_menu(menu_options)
  else:
    return


