label timed_menu(menu_id = "", choice=0):
  # Build the choices from the menu_id
  python:
    choices = []
    for i, item in enumerate(menus_options[menu_id]):
      # if ((not item.has_key('condition')) or eval(item['condition'])) and (not item.has_key('hidden') or not item['hidden']):
      # choices.append((item['text'], i)) 
      if not item.hidden:
        choices.append((item.choice_text, i))
    
  # Leave if no valid choice
  if len(choices) <= 0:
    return
  
  # read the choices
  if False:  # TODO diff between normal menu and map menu
    $ choice = renpy.call_screen('in_game_menu', _layers="screens") 
  else: 
    $ choice = menu(choices)

  # After selection, decrease the time life, 
  # if menus_options[menu_id][choice].has_key('time_spent'):
  #   $ time_left -= menus_options[menu_id][choice]['time_spent']

  # Hides the menu if necessary
  # if not menus_options[menu_id][choice].has_key('keep_alive') or not menus_options[menu_id][choice]['keep_alive']:
  #   $ menus_options[menu_id][choice]['hidden'] = True
  if not menus_options[menu_id][choice].keep_alive:
    $ menus_options[menu_id][choice].hidden = True


  # Calls redirect, from [menu_id]
  # if menus_options[menu_id][choice].has_key('early_exit') and menus_options[menu_id][choice]['early_exit']:
  #   # When choice has early_exit, return to last position after call
  #   call expression menus_options[menu_id][choice]['redirect']
  #   return
  # else:

  # Otherwise call the menu back
  # call expression menus_options[menu_id][choice]['redirect']
  call expression menus_options[menu_id][choice].redirect
  # Jump back to start of menu if any time left,  and early exit is not set
  if time_left <= 0:
    return
  
  call timed_menu(menu_id, choice)

  return
  


