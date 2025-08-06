# Generic captain Dialogs.
# Accessible from :
#                   - The lad

#?TODO add extra choices possibilities?
label captain_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["captain_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["captain_generic_menu"])

    return


label captain_generic_weather_friday:

    captain """
    I can see that a storm is coming.

    And it looks like a big one.
    """

    return

label captain_generic_weather_saturday:

    captain """
    The little storm we had yesterday seems to have worn off.

    The weather should improve from now on.
    """

    return


label captain_generic_weather_sunday:

    captain """
    (Placeholder for Sunday weather dialogue)
    """

    return

label captain_generic_room:

    captain """
    The 'George I' Bedroom.

    An ordinary room named after an ordinary King.
    """

    if current_character.text_id == "psychic":

        captain """
        The only remarkable thing about 'George I' is that ...
        """

        psychic """
        He was a foreigner, yes.

        As the first King of the house of Hanover, he was born in Germany and had a very limited grasp of English.
        """

        captain """
        Well, I was going to say his reign marked the beginning of the gradual transformation of the British monarchy into a more constitutional one,
        
        with real political power shifting towards Parliament and ministers.

        But I guess you're right too.
        """

    $ unlock_map('bedroom_captain')

    return


label captain_generic_origin_psychic_1:

    captain """
    I come directly from London.

    I have been living there for the last two decades.    
    """

    psychic """
    London.

    Right.

    But that's not what I meant.
    """

    captain """
    I am sorry, what did you mean?
    """

    $ psychic_details.description_hidden.unlock('racist')
    $ captain_details.description_hidden.unlock('city')

    return 

label captain_generic_origin_psychic_2:
    
    captain """
    Oh ... I was raised in Calcutta. 
    
    But I've been living in England for so long that I don't even think about it anymore.
    """

    psychic """
    Alright. Calcutta is in the far east, right?
    """

    captain """
    Yes, it's in North India.
    """

    # ChatGPT
    captain """
    I was born there. 
    
    Growing up, I was always fascinated by the stories of the Raj army and their brave officers. 
    
    I knew from a young age that I wanted to join the army and serve my country.

    As I grew older, I began to prepare myself for the rigorous training that would be required to become an officer in the Raj army. 
    
    I studied hard and practiced my shooting and horseback riding skills. 
    
    I also learned about the history of India and the British Raj, so that I could understand the context of the conflicts that the army was involved in.

    Finally, in 1890, I was accepted into the Raj army as a cadet. 
    
    The training was grueling, but I was determined to succeed. 
    
    I was taught how to march, how to shoot, and how to lead my men in battle. 
    
    I also learned about strategy and tactics, so that I could make quick decisions in the heat of battle.

    After two years of training, I was finally commissioned as an officer. 
    
    I was assigned to a regiment and sent to the frontier, where I would be fighting against the tribes that were trying to rebel against the British Raj.

    It was a difficult and dangerous assignment, but I was determined to do my best. 
    
    I led my men into battle and fought bravely, always thinking of the safety and well-being of my men. 
    
    I was able to successfully quell the rebellion, and my men and I returned home as heroes.

    I continued to serve in the Raj army for many years, rising through the ranks and taking on more responsibility. 

    As the years went by, I was increasingly exposed to the ways of the British army and began to adopt their techniques and strategies. 
    
    I was eventually sent to London to train new officers, ...
    """

    # where I finished my career as a respected trainer in the British army.

    """
    My god, he is going to tell me his whole life story.

    How rude.

    And there is no way to avoid him here.

    So I nod in assent and barely listens to what he is saying.
    """

    $ captain_details.description_hidden.unlock('talker')     

    return

# TODO: 3 questions that will lead to the psychic to notice inconsistency in his speech
# The latest question can only be asked on the latest dicscussion DAY 2 evening
label captain_generic_background_psychic_1:

    # The second part should contradict A little something.
    # Make psychic say something like : There is something that doesn't make sense here 
    # About the BOxers rebellion of course => Check what he said
    """
    Why am I encouraging him?
    """

    captain """
    Oh, I thought I already said plenty in the car.

    But, if you insist of course.

    I think I mostly mentioned a lot about my military career.
    ...

    """

    return


label captain_generic_background_psychic_2:

    # Again, there is something wrong with his story. I can feel he doesn't say the truth
    """
    2
    """

    return


label captain_generic_background_psychic_3:

    # You noticed some inconsistency before, so now is you chance to ask which one is a problem

    """
    Really, is there a
    """

    return


label captain_generic_heroic_act_psychic:
    
    # AI generated
    captain """
    It is most likely because of my actions during the Great War.

    In particular, those in 1917, during the Mesopotamian campaign.
    
    Our regiment was tasked with taking control of a heavily fortified Turkish position. 
    
    The battle was intense and brutal, with heavy gunfire and explosions all around us.

    I led my men through the chaos, urging them forward and providing cover fire. 
    
    Despite the danger, we were able to push through the enemy lines and take control of the position.

    I was severely injured in the battle, but I refused to be taken off the field until the objective was secured. 
    
    My actions, bravery and leadership inspired my men and led to the success of our mission.

    For my actions, I was awarded the Military Cross, one of the highest honors that can be given to an officer of the British army. 
    
    I was proud to have served my country and to have played a role in the ultimate victory of the Great War.
    """

    """
    Well, he certainly likes to tell a story in full.

    That's my fault for asking.
    """

    $ captain_details.description_hidden.unlock('heroic_act') 
    
    return

    
label captain_generic_manor_psychic:

    captain """
    It's a splendid house.

    A bit old, and it could used some renovations.

    But I know it is no easy task.
    """

    #chatGPT
    captain """
    I have seen my fair share of grand buildings and stately homes, and I can confidently say that renovating an old Victorian mansion is no easy feat. 
    
    The challenge lies in balancing the preservation of the building's historical integrity with the necessary updates and modernizations for contemporary living.

    One issue that often arises is the cost of renovations. 
    
    Victorian mansions were built with materials and techniques that are not always easily replicated today, making repairs and replacements quite expensive. 
    
    Additionally, many of these homes have unique architectural features that require specialized skills and knowledge to maintain.

    Another obstacle to overcome is the potential for structural issues. 
    
    Victorian mansions are often quite old, and over time, they can suffer from wear and tear. 
    
    This means that any renovation work will need to be done with an eye towards ensuring the building's stability and safety.

    Personally, I believe that renovating an old Victorian mansion is a noble endeavor. 
    
    These buildings are a testament to a bygone era and preserving them for future generations is important. 
    
    However, it is crucial to approach the task with a realistic understanding of the challenges and costs involved. 
    
    A balance must be struck between maintaining the historical integrity of the building and ensuring that it is functional and comfortable for modern living.

    Ultimately, renovating an old Victorian mansion is not for the faint of heart, but for those who are willing to put in the time, effort, and resources, the end result can be truly spectacular.
    """

    """
    Another long story.

    But how does he know such things?

    Is he one of those bookish people who read about everything and anything?
    """

    $ captain_details.description_hidden.unlock('mansion')

    return 

label captain_generic_room_friday:

    captain """
    I am not sure actually.

    I guess I'll see after dinner.
    """

    return

label captain_generic_age_psychic:
    
    captain """
    Why?
    
    Are you having trouble guessing my age because I'm Indian?
    
    Many people do.
    """

    psychic """
    Gosh no, I'm merely asking out of curiosity.
    
    I didn't intend any offense.
    """

    captain """
    Hmph.
    
    Very well.
    
    I am 56 years old.
    """

    $ captain_details.description_hidden.unlock('age')
    
    return

