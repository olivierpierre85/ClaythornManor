label timed_menu(menu_id = "", choice=0):
  python:
    choices = []
    for i, item in enumerate(menus_options[menu_id]):
      if ((not item.has_key('condition')) or eval(item['condition'])) and (not item.has_key('hidden') or not item['hidden']):
        choices.append((item['text'], i)) 

    
  # No valid choice
  if len(choices) <= 0:
    "You have nothing more to do here"
    return
  
  # read choices
  $ choice = menu(choices)

  # $ choice_time_spent[menu_id] = menus_options[menu_id][choice]['time_spent']
  # $ choice_redirect[menu_id] = menus_options[menu_id][choice]['redirect']
  $ choice_early_exit[menu_id] = menus_options[menu_id][choice].has_key('early_exit') and menus_options[menu_id][choice]['early_exit']

  $ time_left -= menus_options[menu_id][choice]['time_spent']

  # Delete current options from the choices TODO NOT IF MULTIPLE CALL Possible
  # "DELete current options from the choices by changing option [menu_id], [choice]"
  # if menus_options[menu_id][choice].has_key('never_delete'): TODO NOT NEEDED NOW
  
  $ menus_options[menu_id][choice]['hidden'] = True

  # "choice: [choice], time_consumed :choice_time_spent, redirection: [choice_redirect], time left: [time_left], early exit: [choice_early_exit], choices_left: [choices_left]"

  # "Calls redirect, from [menu_id]"
  call expression menus_options[menu_id][choice]['redirect']
  # $ first_choice = menus_options[menu_id][0]['text']
  # "Leaves redirect in [menu_id], last_choice= [choice], first choice [first_choice]"
  

  # Jump back to start of menu if any time left,  and early exit is not set
  if time_left <= 0:
    return

  if choice_early_exit[menu_id]:
    return

  call timed_menu(menu_id, choice)


