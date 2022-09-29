# Generic psychic Dialogs.
# Accessible from :
#                   - The lad

# ?TODO add extra choices possibilities?
label psychic_generic:

    if 'psychic' not in current_character.has_met:

        if current_character.text_id == "lad":

            lad "Hi miss ..."

            psychic "Miss Baxter, Amalia Baxter."

            $ psychic_details.introduce()

            lad "Nice to meet you miss Baxter. I am Ted Haring."

            psychic "Nice to meet you mister Haring."
        
        # elif current_character.text_id == "TODO": # Maybe need a default options ? with a current char and current_char_details

        $ current_character.has_met.add('psychic')
        
    else:
        if current_character.text_id == "lad":

            lad "Hi again Miss Baxter."

            psychic "Oh Mister Harring. I am glad we can continue our conversation."

        # elif current_character.text_id == "TODO": # Maybe need a default options ? with a current char and current_char_details

    if not 'psychic_generic_menu' in locals():
        $ psychic_generic_menu = TimedMenu([
        TimedMenuChoice('Talk about the weather', 'psychic_generic_weather', 20),
        TimedMenuChoice('Ask about her situation', 'psychic_generic_background', 20),
        TimedMenuChoice('Talk about the manor', 'psychic_generic_manor', 20),
        TimedMenuChoice('Ask her her age', 'psychic_generic_age', 20),
        TimedMenuChoice('Ask her about the invitation', 'psychic_generic_heroic_act', 20, condition = "psychic_details.check_knowledge_unlocked('background')"),
        TimedMenuChoice('You don\'t have anymore questions for her', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
        ], image_right = "psychic")

    call run_menu(psychic_generic_menu)

    return

label psychic_generic_weather:

    psychic """
    Well, it is not very original to ask about such things when meeting someone new.

    But it is true that is not your average rain. It looks more like a dangerous storm to me.

    And since we are basically in the middle of nowhere, that's reason enough to be a little nervous I suppose.
    """

    return

label psychic_generic_age:

    psychic """
    I beg your pardon ?

    You are not really asking me that ? Were you raised in a barn ?

    Only a person without any social skills would ask that to a respectable lady.
    """

    """
    You mutter an apology and quickly change the subject.
    """

    return
    

label psychic_generic_heroic_act:
    psychic """
    I was invited here for something I have done a couple of years back.

    You actually might remember the event. It was in all the papers at the time.

    TODO Kidnapping story

    You see, my talent. I am lucky enough to help some people who despertaly need help

    """

    $ psychic_details.add_knowledge('heroic act') 
    

    if current_character.text_id == "lad":
        "After this short explanation, she asks about your own reason. And you tell her your story."

        psychic "Oh how interesting ! I assumed most people were here because of something they did during the war."

        lad "It would have been difficult for me. I was but sixteen when the war ended."

        psychic "Really? I thought you were older."

        $ lad_details.add_knowledge('age') 
    
    return

label psychic_generic_background:
    psychic """
    Oh dear, I do a lot of things.

    But what takes up the most of my time is my readings.

    TODO find info on old psychic


    """

    $ psychic_details.add_knowledge('background')

    return
    
label psychic_generic_manor:
    psychic """
    Such a magnificent house right ?

    Even if the style is not very recent, it still has a lot of cachet. 
    
    You don't see a lot of that type of place anymore.

    The only problem I see is there is not a lot of help for a house this big.

    I only noticed one footman and the butler so far.

    That's not a lot when you entertain guests.

    And I don't think the money is a problem.

    Lady Claythorn couldn't possibly give away so much money if she had enough resources.

    More likely, she couldn't find enough people to come live here.
    
    It has become very hard to recruit good help since the war.

    And it must be especially difficult when you are so far away from a city.

    In any case, she should have a made more of an effort for this weekend.

    I hope we won't suffer inconvenience because of this.

    """

    if current_character.text_id == "lad":
        """
        Okay. I would not have thought of that.

        She seems in her element here.

        Am I the only one in here who has never had a butler waiting on him ?
        """

    $ psychic_details.add_knowledge('status')
    
    return

label psychic_generic_cancel:
    return