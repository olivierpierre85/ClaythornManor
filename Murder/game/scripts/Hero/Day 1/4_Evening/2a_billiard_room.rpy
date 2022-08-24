label hero_day1_evening_billiard_room:

  $ hero_day1_evening_left_bedroom = True

  scene billiard_room

  # TODO Hides explanation on re-entry
  #if menus_options['hero_day1_evening'][1]['text'] != 'Go back to the billiard room':

  """
  You see multiple people in the room.

  Amalia Baxter doesn't seem to be here.

  But you recognize Doctor Baldwin in conversation with another man.

  The rest of the guests are grouped together and are talking loudly.

  There is also a choice of alcohol near the bar.

  And the butler is silent in a corner.
  """

  $ return_menu = current_menu 
  $ current_menu = TimedMenu([
    TimedMenuChoice('Talk to Daniel Baldwin', 'hero_day1_evening_billiard_room_doctor', 50),
    TimedMenuChoice('Approach the large group of people', 'hero_day1_evening_billiard_room_group', 20),
    TimedMenuChoice('Ask the butler about Amelia', 'hero_day1_evening_billiard_room_butler', 20),
    TimedMenuChoice('Leave the room', 'hero_day1_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
  ])
  call run_menu(current_menu, return_menu) # go back to return_menu when over

  return


label hero_day1_evening_billiard_room_bar_1:
  "Your pour yourself a glass of sherry from the bottle lying at the bar"
  "You start to relax a little"

  "The drunk man who was asleep before is near the bar, barely holding up"

  hero "Hi there"

  "The mans stares at you but makes no sound"

  "You leave him at the bar, distraught."

  $ hero_day1_drank_sherry = True

  return

label hero_day1_evening_billiard_room_bar_2:
  "Another drink"
  $ hero_day1_drank_sherry_2 = True
  return

label hero_day1_evening_billiard_room_bar_3:
  "One last drink"
  $ hero_day1_drank_sherry_3 = True
  return


label hero_day1_evening_billiard_room_doctor:
  "choice 2 is cool"
  return

label hero_day1_evening_billiard_room_group:
  "choice 3 very long"
  return

label hero_day1_evening_billiard_room_butler:
  show butler
  "Where is Miss Baxter ? "
  butler "it's a bit personal."

  # TODO develop choices to convince Butler

  # TODO unlock nurse room position on the map
  butler "Fine. You'll find miss Baxter in the Sun room."
  $ hero_nurse_location = True

  hide butler
  
  return

label hero_day1_evening_billiard_room_cancel:
  "You don't feel like staying in this room and leave"
  # TODO Change name of options ??
  # $ menus_options['hero_day1_evening'][1]['text'] = 'Go back to the billiard room'
  scene hallway

  return