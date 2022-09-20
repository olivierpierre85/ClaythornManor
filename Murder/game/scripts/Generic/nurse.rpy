label nurse_generic_choices:

  call timed_menu('nurse_generic_choices')
  
  return

label nurse_generic_job:
  nurse "I am a nurse. I work in an hospital in London."

  # Special label/function that will also play sound
  $ renpy.notify("You found the occupation for The nurse")
  #TODO problem, they superpose, thus erasing the previous message. They should be queue or something...
  $ renpy.notify("You have unlock a new Character (The nurse)")
  return

label nurse_generic_heroic_act:
  nurse """
  Well, I think it's for something I have done during the war.

  I saved a poor man's life once. 
  
  It was nothing really. I don't think I deserve to have been invited.
  """

  "After this short explanation, she asks about your own reason. And you tell her your story."

  nurse "I assume most people are here because of something during the war."
  
  return


label nurse_generic_background:
  nurse "I am from Sausage Island"
  return
  
label nurse_generic_manor:
  nurse "It is certainly spooky right ?"

  # TODO  keep a generic response OR try to have a response different for different characters ?
  $ responses = dict()
  $ responses["lad"] = "I agree, I was a bit afraid of that at first."

  $ renpy.say(eval(current_character), responses[current_character])
  return

label nurse_generic_cancel:
  return