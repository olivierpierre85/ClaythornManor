# Generic psychic Dialogs.
# Accessible from :
#                   - The lad

# TODO add extrachoice possibilities?
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

        lad "Hi again Miss Baxter."

        psychic "Oh Mister Harring. I am glad we can continue our conversation."

    if not 'psychic_generic_menu' in locals():
        $ psychic_generic_menu = TimedMenu([
        TimedMenuChoice('What do you do in life ?', 'psychic_generic_job', 20),
        TimedMenuChoice('Why were you invited here ?', 'psychic_generic_heroic_act', 20),
        TimedMenuChoice('Where are you from ?', 'psychic_generic_background', 20),
        TimedMenuChoice('You don\'t have anymore questions for her', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
        ], image_right = "psychic")

    call run_menu(psychic_generic_menu)

    return

label psychic_generic_job:
    psychic "Oh dear, I do a lot of things."

    $ psychic_details.check_characters_knowledge('job')

    return

label psychic_generic_heroic_act:
    psychic """
    Well, I think it's for something I have done during the war.

    I saved a poor man's life once. 
    
    It was nothing really. I don't think I deserve to have been invited.
    """

    "After this short explanation, she asks about your own reason. And you tell her your story."

    psychic "I assume most people are here because of something during the war."

    $ psychic_details.check_characters_knowledge('heroic act') 
    
    return

label psychic_generic_background:
    psychic "I am from Sausage Island"

    $ psychic_details.check_characters_knowledge('background')

    return
    
label psychic_generic_manor:
    psychic "It is certainly spooky right ?"

    # TODO  keep a generic response OR try to have a response different for different characters ?
    $ responses = dict()
    $ responses["hero"] = "I agree, I was a bit afraid of that at first."

    $ renpy.say(eval(current_character), responses[current_character])
    return

label psychic_generic_cancel:
    return