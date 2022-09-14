label character_selection:
  scene black_background
  narrator "Select Your Character"

  $ selected_choice = renpy.call_screen('character_selection') 
  if selected_choice == 'lad':
        jump hero_introduction
  else:
        jump hero_day1_evening