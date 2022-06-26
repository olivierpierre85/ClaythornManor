label timed_menu(menu_options = []):
  python:
    # choices = [(item[0], i) for i, item in enumerate(menu_options)]
    choices = []
    for i, item in enumerate(menu_options):
      if (not item.has_key('condition')) or eval(item['condition']):
        choices.append((item['text'], i)) 
    choice = menu(choices)
    # read choices


  # Add time 
  $ choice_time_spent = menu_options[choice]['time_spent']
  $ choice_redirect = menu_options[choice]['redirect']

  $ time_left -= choice_time_spent

  # Delete current options from the choices
  $ del menu_options[choice]

  # Jump back to start of menu if any time left
  "choice: [choice], time_consumed :[choice_time_spent], redirection: [choice_redirect], time left: [time_left]"

  call expression choice_redirect

  if len(menu_options) == 0:
    "You have nothing more to do here"
    return
  
  if time_left <= 0:
    return

  call timed_menu(menu_options)


