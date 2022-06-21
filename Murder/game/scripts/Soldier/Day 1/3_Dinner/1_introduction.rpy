# Introduction for soldier
label soldier_day1_dinner_introduction:

  scene dining_hall

  narrator """
  Every one sits at a place with their names on them.

  You turn your attention to the group of people seated a the table, and count TODO persons.

  While you are examining everyone, a old lady enters the room, and takes her place at the end of the table.

  """

  show host 

  call host_welcome_speech

  "Our host then sits down to her chair."

  hide host

  narrator "After the speech, everyone seems pleased. And a few of the guests started showing their appreciation to the host"

  host "Please no need to thank me. The food will be served, enjoy your meal."

  narrator "The butler then enters the room, accompany by a footman."

  narrator """
  They proceed in serving the first dish and pouring drinks to everyone.
  
  The mood starts to relax, and the sound of different conversations fills the room.

  You then turn your attention to the guests next to you

  You are sitting between Amalia Baxter, and a middle aged man wearing a bowl hat.

  It's name card reads 'Doctor Daniel Baldwin'
  """


  $ menu_soldier_day1_dinner_introduction = set()

  jump soldier_day1_dinner_introduction_choice

label soldier_day1_dinner_introduction_choice:  

  show nurse at right
  show doctor at left

  menu:
    set menu_soldier_day1_dinner_introduction
    "Talk to Daniel Baldwin":
        jump soldier_day1_dinner_doctor

    "Talk to Amalia Baxter":
        jump soldier_day1_dinner_nurse
