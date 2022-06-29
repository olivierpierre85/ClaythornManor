label nurse_generic_choices:

  call timed_menu('nurse_generic_choices')
  
  return

label nurse_generic_job:
  nurse "I am a nurse."

  # Special label/function that will also play sound
  $ renpy.notify("You found the occupation for The nurse")
  #TODO problem, they superpose, thus erasing the previous message. They should be queue or something...
  $ renpy.notify("You have unlock a new Character (The nurse)")
  return

label nurse_generic_heroic_act:
  nurse "I saved a poor man's life once. It was nothing really. I don't think I deserve to have been invited"
  return

label nurse_generic_background:
  nurse "I am from Sausage Island"
  return
  
label nurse_generic_location:
  nurse "It is certainly spooky right ?"
  return

label nurse_generic_cancel:
  return