# Generic psychic Dialogs.
# Accessible from :
#                   - The lad
#                   - The Captain? TODO not sure

#?TODO add extra choices possibilities?
label psychic_generic:

    # Reset if previous early exit
    $ current_character.saved_variables["psychic_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["psychic_generic_menu"])

    return


label psychic_generic_weather_friday:

    psychic """
    Well, it is not very original to ask about such things when meeting someone new.

    But it is true that this is not your average rain. It looks more like a dangerous storm to me.

    And since we are basically in the middle of nowhere, that's reason enough to be a little nervous I suppose.
    """

    return

label psychic_generic_weather_saturday:

    psychic """
    I must say that last night was quite scary.

    It has been a while since I've experienced a storm like that.

    We should consider ourselves lucky if there is no damage to the manor.
    """

    return

label psychic_generic_weather_sunday:

    psychic """
    Really, you want to talk about the weather with everything that is happening around us?

    What is wrong with you?
    """

    # TODO achievement? ALWAYS ASKING ABOUT WEATHER if all three dialog unlocked
    return

label psychic_generic_room:

    psychic """
    That's a strange question.

    But if you must know, my room is "Elizabeth the First."
    """

    $ unlock_map('bedroom_psychic')

    $ current_character.saved_variables['knows_bedroom_psychic'] = True

    return


label psychic_generic_age:

    psychic angry """
    I beg your pardon?

    Are you truly asking me that? Were you raised in a barn?

    Only a person without any social skills would ask such a question of a respectable lady.
    """

    """
    I mutter an apology and quickly change the subject.
    """

    $ psychic_details.description_hidden.unlock('age') 

    return


label psychic_generic_background:

    psychic """
    Oh, where to begin? I suppose I'm just an old woman who keeps herself busy.

    I tend to my garden and brew herbal remedies,

    and I usually keep to myself, except for the séances that I frequently organise.
    """

    lad """
    Séances? You mean like talking to the dead?
    """

    psychic """
    Well, simply put, yes. But there's more to it than that, of course.
    """

    lad """
    I've never been to one of those... séances. How does that work?
    """

    psychic """
    There isn't just one way of doing it.

    Personally, I usually ask people to bring items that belonged to their loved ones who have passed.

    Through these objects, I am able to form a bond with the soul of the deceased.

    Then, they communicate with me. Sometimes it's just a whisper, barely audible.

    Other times, I can see them clearly, just as I see you now.

    And on rare occasions, they can take over my body and speak directly to their loved ones through me.
    """

    lad """
    You mean... like being possessed?
    """

    psychic """
    Yes, but don't worry, there's nothing unholy about it.

    It only lasts for a few moments, and I always regain full control immediately after.
    """

    """
    Still... that doesn't make me feel at ease.
    """

    $ psychic_details.description_hidden.unlock('background')

    return

label psychic_generic_heroic_act:

    $ play_music('mysterious')

    psychic """
    I was invited here because of something I did a couple of years ago.

    You might actually remember the event. It was in all the papers at the time.

    You see, with my talent, I am sometimes able to help people who desperately need it.

    One day, a young couple came to see me. 

    Their only son, not even five years old, had been kidnapped.

    The police had no clues about what might have happened.

    Desperate, they sought my help.

    Right away, I could tell the child was still alive but in great danger.

    I saw him with a specific individual whom I described to the couple.

    They were able to identify her immediately.

    She was an old family friend who often visited their house.

    Nobody had suspected her until that point.

    But it turned out I was right. The child was indeed with her.

    She was arrested and the boy was safely returned to his parents.

    Since they were prestigious members of the nobility, a duke and duchess, the story was prominent in the press.

    My popularity grew quite a lot after that.
    """

    lad """
    Wait, I don't understand.
    
    How did you know the child was in danger?
    
    You can also communicate with people who are still alive?
    """

    psychic """
    In a sense yes.

    Like I said, there is more to my gift than simply speaking with the dead.

    I can also sense if someone's life is at risk.

    Some say it is because when someone is close to the other world, we can sense them almost like they are already there.

    But for myself, I think it's something else entirely.

    I believe I can only talk to the dead.

    So when I can sense someone who is still alive. It means to me that there is a version of them that is not.

    I am not sure if you understand what I mean.
    """

    lad """
    I don't know.

    You mean someone can be dead and alive at the same time?
    """

    psychic """
    Yes. I believe some version of the person died in another realm of existence.
    
    Then they came back to help a version of them who is still alive.

    I am sorry. That must sound like nonsense to you.

    Forget I said anything. I get carried away sometimes.

    But tell me. Why were you invited yourself?
    """

    $ psychic_details.description_hidden.unlock('heroic_act') 

    """
    So I tell her my story.
    """

    psychic """
    Oh how interesting! I assumed most people were here because of something they did during the war.
    """

    lad """
    It would have been difficult for me. I was but sixteen when the war ended.
    """

    psychic """
    Really? I thought you were older.
    """

    $ lad_details.description_hidden.unlock('age') 

    $ play_music('PREVIOUS')
    
    return

label psychic_generic_manor:

    psychic """
    Such a magnificent house right?

    Even if the style is not very recent, it still possesses a great deal of charm.
    
    You don't see a lot of that type of place anymore. 

    The only problem is I don't see a lot of help for a house this big.

    And I don't think money is a problem.

    Lady Claythorn couldn't possibly give away so much money if she lacked the means.

    More likely, she couldn't find enough people to come live here.
    
    It has become very hard to recruit good help since the war.

    And it must be especially difficult when you are so far away from a city.
    
    Even in London, some of my neighbors are struggling finding employees.

    In any case, she should have made more of an effort for this weekend.

    I hope we won't suffer any inconvenience because of this.
    """

    if current_character.text_id == "lad":
        """
        Okay. I would not have thought of that.

        She seems in her element here.

        Am I the only one in here who has never had a butler waiting on him?
        """

    $ psychic_details.description_hidden.unlock('status')
    
    return