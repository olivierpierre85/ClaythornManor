label lad_day1_evening_billiard_room:

    $ lad_day1_evening_left_bedroom = True

    # Change menu text
    $ lad_day1_evening_menu.choices[1].text = "Go back to the billiard room"

    scene billiard_room


    if not lad_day1_evening_billiard_room_visited:

        """
        Almost everyone I saw at dinner is here.

        Except for Amelia Baxter and our host.

        I recognize Doctor Baldwin sitting on a chair alone.

        There is also a choice of alcohol near the bar.

        The rest of the guests are grouped together and are talking loudly.

        And the butler is silent in a corner.
        """

        $ lad_day1_evening_billiard_room_menu = TimedMenu([
            TimedMenuChoice('Talk to Daniel Baldwin', 'lad_day1_evening_billiard_room_doctor', 50),
            TimedMenuChoice('Approach the large group of people', 'lad_day1_evening_billiard_room_group', 20),
            # TimedMenuChoice('Ask the butler about Amelia\'s room', 'lad_day1_evening_billiard_room_butler', 20),
            TimedMenuChoice('Go to the bar to have a drink', 'lad_day1_evening_billiard_room_bar_1', 20),
            TimedMenuChoice('Have another drink', 'lad_day1_evening_billiard_room_bar_2', 20, condition = 'lad_day1_drinks == 1'),
            TimedMenuChoice('Maybe one last drink', 'lad_day1_evening_billiard_room_bar_3', 20, condition = 'lad_day1_drinks == 2'),
            TimedMenuChoice('Leave the room', 'lad_day1_evening_billiard_room_cancel', 0, keep_alive = True, early_exit = True)
        ])

        $ lad_day1_evening_billiard_room_visited = True

    else:
        # Reset menu
        $ lad_day1_evening_billiard_room_menu.early_exit = False

        "You are back in the Billiard Room"

    call run_menu(lad_day1_evening_billiard_room_menu) # go back to return_menu when over

    return


label lad_day1_evening_billiard_room_bar_1:

    "I approach the bar."

    "Samuel Manning is there."

    lad "Hello sir."

    drunk "..."

    "The man stares at me but makes no sound."

    broken "Don't mind him, he seems to be totally out of it."

    """
    I am startled by a man who approached me.

    He wears one of those masks I've seen on wounded soldiers from the war.

    There were so badly injured that they have to hide their faces.

    He pretends not to notice my surprise and keeps on talking.
    """

    $ doctor_details.add_knowledge('mask') 

    broken """
    He was already asleep when I arrived. It's impressive that he managed to still be here.

    I was seating next to him at dinner and it was impossible to have him say anything coherent.

    He could eat it's food though. You could tell he is used to function like this. Poor fellow.

    Anyway, I am Thomas Moody.
    """

    $ current_character.has_met.add('broken')
    # $ broken_details.introduce()

    lad "Ted Harring, how do you do."

    broken """
    Nice to meet you mister Harring. I guess you came here for a drink.

    The choice is rather restricted I am afraid. There's only Sherry or Port.

    But luckily, I've come prepared.
    """

    """
    Before I could say anything. He reaches down his coat pocket and took a flask out. 
    
    Then he starts pouring me a glass of what looks like whisky.
    """

    broken "You'll probably enjoy this more."

    "I can't really say no to that."

    lad "Thanks. Cheers."

    #TODO if needed for the story about drunk and puking ADD here that the drunk asks for a drink
    $ lad_day1_poisoned = True
    $ lad_day1_drinks = lad_day1_drinks + 1

    broken "Cheers Mister Harring. Now if you don't mind, I'll see what this group is talking about."

    "He joins the group of people talking."

    return

label lad_day1_evening_billiard_room_group:
    """
    I walk to the main group in the room.

    They seem to have an animated discussion.

    The one currently talking is the older indian man.
    """

    # TODO extract speech to put in captain generic file ? multiple parts ?
    captain """
    That's when I knew I had to leave the army.

    The last war was the one too many.
    """

    """
    TODO put needed information => LATER
    """

    return

label lad_day1_evening_billiard_room_bar_2:
    "Another drink"
    $ lad_day1_drinks = lad_day1_drinks + 1
    return

label lad_day1_evening_billiard_room_bar_3:
    "One last drink"
    $ lad_day1_drinks = lad_day1_drinks + 1
    # TODO add blur effect if drunk, puke noise... Or just black out 

    return


label lad_day1_evening_billiard_room_doctor:
      
    if current_character.text_id == "lad":

        call doctor_lad_introduction

    else:
        
        lad "Hello again Doctor."

    call doctor_generic

    return

label lad_day1_evening_billiard_room_cancel:
    
    "You don't feel like staying in this room and leave"

    scene hallway

    return