# Generic psychic Dialogs.
# Accessible from :
#                   - The lad

# ?TODO add extra choices possibilities?
label psychic_generic(skip_intro = False):

    # if not skip_intro:
    #     if 'psychic' not in current_character.has_met:

    #         if current_character.text_id == "lad":

    #             lad "Hi miss ..."

    #             psychic "Miss Baxter, Amelia Baxter."

    #             $ psychic_details.introduce()

    #             lad "Nice to meet you miss Baxter. I am Ted Haring."

    #             psychic "Nice to meet you mister Haring."
            
    #         # elif current_character.text_id == "TODO": # Maybe need a default options ? with a current char and current_char_details

    #         $ current_character.has_met.add('psychic')
            
    #     else:
    #         if current_character.text_id == "lad":

    #             lad "Hi again Miss Baxter."

    #             psychic "Oh Mister Harring. I am glad we can continue our conversation."

            # elif current_character.text_id == "# Maybe need a default options ? with a current char and current_char_details

    if not 'psychic_generic_menu' in locals():
        $ psychic_generic_menu = TimedMenu([
            TimedMenuChoice('Talk about the weather', 'psychic_generic_weather', 5),
            TimedMenuChoice('Ask her about herself', 'psychic_generic_background', 15),
            TimedMenuChoice('Talk about the manor', 'psychic_generic_manor', 10),
            TimedMenuChoice('How old are you ?', 'psychic_generic_age', 5),
            TimedMenuChoice('What room are you in ?', 'psychic_generic_room', 5),
            TimedMenuChoice('Why were you invited here ?', 'psychic_generic_heroic_act', 20, condition = "psychic_details.check_knowledge_unlocked('background')"),
            TimedMenuChoice('You don\'t have anymore questions for her', 'psychic_generic_cancel', 0, keep_alive = True, early_exit = True)
        ], image_right = "psychic")

    call run_menu(psychic_generic_menu)

    return
    
label psychic_generic_weather:

    # TODO adapt depeding of the day

    psychic """
    Well, it is not very original to ask about such things when meeting someone new.

    But it is true that is not your average rain. It looks more like a dangerous storm to me.

    And since we are basically in the middle of nowhere, that's reason enough to be a little nervous I suppose.
    """

    return

label psychic_generic_room:
    psychic """
    That's a strange question.

    But if you must know, my room is 'the George III'
    """

    call unlock_map('psychic_room')

    return


label psychic_generic_age:

    psychic angry """
    I beg your pardon ?

    You are not really asking me that ? Were you raised in a barn ?

    Only a person without any social skills would ask that to a respectable lady.
    """

    """
    I mutter an apology and quickly change the subject.
    """

    return
    

label psychic_generic_heroic_act:
    if current_character.text_id == "lad":

        play music mysterious_01 fadeout 2.0 fadein 2.0

        psychic """
        I was invited here for something I have done a couple of years back.

        You actually might remember the event. It was in all the papers at the time.

        You see, with my talent, I am sometimes able to help some people who desperately need it.

        One day, a young couple came to see me.

        Their new born child, not even one year old, had been kidnapped.

        The police had no clues of what could have happened.

        Desperate, they asked for my help.

        Right away, I could tell the child was still alive.

        """

        lad """
        Really ?! You can also talk to babies ?
        """

        psychic """
        Not exactly talk, but I can feel them, their presence.

        This time, I was certain the child was still alive. But in great danger.

        I could see him with a specific person that I described to the couple.

        They were able to identified her immediately.

        She was an old family friend who was often at their house.

        Nobody had suspected her until then.

        But it turns out I was right. The baby was with her.

        She was arrested and the baby safely returned to their parents.

        My popularity grew quite a lot after that.
        """

        lad """
        Wait, I don't understand.
        
        How did you know the child was in danger ?
        
        You can also communicate with people who are still alive ?
        """

        psychic """
        In a sense yes.

        Like I said, there is more to my gift that just talking with the dead.

        I can also sense if someone life is at risk. 

        Some say it is because when someone is close to the other world, we can sense them almost like they are already there.

        But for myself, I think it's something else entirely.

        I believe I can only talk to the dead.

        So when I can sense someone who is still alive. It means to me that there is a version of them that is not.

        I am not sure if you understand what I mean.
        """

        lad """
        I don't know.

        You mean someone can be dead and alive at the same time ?

        """

        psychic """
        Yes. I believe some version of the person died in an other realm of existence. 
        
        Then they came back to help a version of them who is still alive.

        I am sorry. That must sound like nonsense to you.

        Forget I said anything. I get carried away sometimes.

        But tell me. Why were you invited yourself ?
        """

        $ psychic_details.add_knowledge('heroic act') 
    
        "So I tell her my story."

        psychic "Oh how interesting ! I assumed most people were here because of something they did during the war."

        lad "It would have been difficult for me. I was but sixteen when the war ended."

        psychic "Really? I thought you were older."

        $ lad_details.add_knowledge('age') 

        stop music fadeout 3.0
    
    return

label psychic_generic_background:
    if current_character.text_id == "lad":
        psychic """
        Oh dear, I do a lot of things.

        But since my husband's death, what takes up the most of my time is the seances I frequently organized.

        """

        lad """
        Seances ? You mean like talking to the dead ?
        """

        psychic """
        Well simply put yes. But there is more to it than that of course.
        """

        lad """
        I have never been to one of those 'seance'. How does that work ?
        """

        psychic """
        There is not a single way of doing it.

        Myself, I usually ask people to bring items of loved one who have passed.

        Thanks to those, I am able to form a bond with the soul of the deceased.

        Then, they talk to me. Sometimes it's only a whisper. Sometimes I can see them clearly, just like I see you now.

        And in rare occasions, they can take over my body and talk directly to their relatives through me.

        """

        lad """
        You mean like being possessed ?
        """

        psychic """
        Yes, but don't worry, there is nothing unholy about it.

        It just mean the dead has something so important to communicate that they use the more efficient way to do so.

        I only last for a few moment. I always regained full power right after.
        """

        """
        Well, that doesn't make me feel good.
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