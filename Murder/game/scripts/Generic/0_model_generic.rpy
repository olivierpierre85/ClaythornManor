 
label todo_generic():

  # if 'todo' not in current_character.has_met:
    
  #   if current_character.text_id == "lad":

  #     lad "Hi sir ..."

  #     todo "Hi, I am todo Daniel Baldwin."

  #     lad "Nice to meet you todo."

  # else:
    
  #   lad "Hello again todo."

  if not 'todo_generic_menu' in locals():
    $ todo_generic_menu = TimedMenu([
      TimedMenuChoice('Talk about the weather', 'todo_generic_weather', 5),
      TimedMenuChoice('Ask him about himself', 'todo_generic_job', 20),
      TimedMenuChoice('Why were you invited here ?', 'todo_generic_heroic_act', 20),
      TimedMenuChoice('Talk about the manor', 'todo_generic_manor', 10),
      TimedMenuChoice('Ask him his age', 'todo__generic_age', 5),
      TimedMenuChoice('What room are you in ?', 'todo_generic_room', 5),
      TimedMenuChoice('You don\'t have anymore questions for him', 'todo_generic_cancel', 0, keep_alive = True, early_exit = True)
    ], image_right = "todo")

  call run_menu(todo_generic_menu)
  
  return

label todo_generic_weather:

    return

label todo_generic_age:

    return
  
label todo_generic_room:
  psychic """
  That's a strange question.

  But if you must know, my room is 'the George III'
  """

  $ unlock_map('psychic_room')

  return

label todo_generic_heroic_act:
    #if current_character.text_id == "lad":
    
    return

label todo_generic_background:

    return
    
label todo_generic_manor:
    
    return

label todo_generic_cancel:
    return