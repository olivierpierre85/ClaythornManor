label hero_day1_evening_billiard_room:

  $ hero_day1_evening_left_bedroom = True

  # Change menu text
  $ hero_day1_evening_menu.choices[1].text = "Go back to the billiard room"

  scene billiard_room

  # TODO Hides explanation on re-entry
  $ first_time = not 'hero_day1_evening_billiard_room_menu' in locals()
  if first_time: # and not hero_day1_evening_billiard_room_menu.early_exit:

    """
    You see multiple people in the room.

    Amalia Baxter doesn't seem to be there.

    But you recognize Doctor Baldwin in conversation with another man.

    The rest of the guests are grouped together and are talking loudly.

    There is also a choice of alcohol near the bar.

    And the butler is silent in a corner.
    """

    $ hero_day1_evening_billiard_room_menu = TimedMenu([
      TimedMenuChoice('Talk to Daniel Baldwin', 'hero_day1_evening_billiard_room_doctor', 50),
      TimedMenuChoice('Approach the large group of people', 'hero_day1_evening_billiard_room_group', 20),
      TimedMenuChoice('Ask the butler about Amelia', 'hero_day1_evening_billiard_room_butler', 20),
      TimedMenuChoice('Go to the bar to have a drink', 'hero_day1_evening_billiard_room_bar_1', 20),
      TimedMenuChoice('Have another drink', 'hero_day1_evening_billiard_room_bar_2', 20, condition = 'hero_day1_drinks == 1'),
      TimedMenuChoice('Maybe one last drink', 'hero_day1_evening_billiard_room_bar_3', 20, condition = 'hero_day1_drinks == 2'),
      TimedMenuChoice('Leave the room', 'hero_day1_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
    ])

  else:
    # Reset menu
    $ hero_day1_evening_billiard_room_menu.early_exit = False

    "You are back in the Billiard Room"

  call run_menu(hero_day1_evening_billiard_room_menu) # go back to return_menu when over

  return


label hero_day1_evening_billiard_room_bar_1:

  "You approach the bar"

  "The drunk man who was asleep before is near the bar, barely holding up"

  hero "Hello sir."

  "The mans stares at you but makes no sound"

  show broken at truecenter

  broken "Don't mind him, he seems to be totally out of it."

  "You are taken aback by the masked man. You haven't noticed he was next to you."

  hero "Yeah, he was already asleep when I arrived. It's impressive he managed to make it through dinner."

  broken """
    He barely did. I was seating next to him at dinner and it was impossible to have him say anything coherent.

    He could eat it's food though. You could tell he is used to function like this. Poor fellow.

    Anyway, I am Thomas Moody.
    """

  $ broken_name = "Thomas Moody"

  hero "Ted Harring, how do you do."

  broken """
    Nice to meet you mister Harring. I guess you came here for drink.

    The choice of drinks is rather small I am afraid. There's only Sherry or Port.

    But luckily, I've come prepared
    """

    "Before you could say anything. He reaches down is coat pocket and get a flask, then start pouring you a glass"

  broken "You'll probably enjoy this more."

  hero "Well ..., Thanks. Cheers"

  $ hero_day1_drinks = hero_day1_drinks + 1

  broken "Cheers Mister Harring. Now if you don't mind, I'll see what this group is talking about."

  "Thomas Moody joins the group of people talking."

  hide broken

  return

label hero_day1_evening_billiard_room_bar_2:
  "Another drink"
  $ hero_day1_drinks = hero_day1_drinks + 1
  return

label hero_day1_evening_billiard_room_bar_3:
  "One last drink"
  $ hero_day1_drinks = hero_day1_drinks + 1
  return


label hero_day1_evening_billiard_room_doctor:
  
  call doctor_generic

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