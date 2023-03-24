# Generic psychic Dialogs.
# Accessible from :
#                   - The lad
#                   - The Captain? TODO not sure

#?TODO add extra choices possibilities?
label lad_generic:
    
    # Reset if previous early exit
    $ current_character.saved_variables["lad_generic_menu"].early_exit = False

    call run_menu(current_character.saved_variables["lad_generic_menu"])

    return


label lad_generic_weather_saturday:

    return

label lad_generic_weather_sunday:

    return

label lad_generic_room_friday:

    lad """
    I don't know, I haven't been to my room yet.

    I just arrived, I didn't realize I would be the last one here.
    """

    return

label lad_generic_room_psychic:

    lad """
    Oh I am in the \"William the Conqueror\" Bedroom.
    """

    psychic """
    An impressive king, better than mine.
    """

    lad """
    What do you mean?
    """

    """
    I have the \"George III\" Bedroom.

    A strange name as he is not one of our most famous king.

    I wonder why they named a room after him.
    """

    lad """
    And William the Conqueror is better?
    """

    """
    He is serious?

    Hasn't he heard of \"William the Conqueror\"?
    """

    psychic """
    Well, he was a French Duke who was able to take the throne of England from very powerful men.

    That's not nothing.

    On the other hands, he was sometimes also called the Bastard King.

    So make that what you want.
    """

    $ unlock_map('lad_room')

    return


label lad_generic_age_psychic:

    lad """
    I am 22 years old.
    """

    """
    Really, I would I have pegged him older than that.

    I guess it's his rugged look.

    Life is not easy for the working class.
    """

    $ lad_details.unlock_knowledge('age')

    return

label lad_generic_background_psychic:
    
    lad """
    There isn't much to say about me.

    I was born and raise in Birmingham.
    
    And I am working there as a business associate.
    """

    $ lad_details.unlock_knowledge('background') 

    psychic """
    Interesting, in what type of business?
    """

    lad """
    Well,..., general sales.
    """

    psychic """
    And you sell anything in particular?
    """

    lad """
    A bit of everything, depending on the opportunities.
    """

    psychic """
    You don't have a store then?
    """

    lad """
    No no, it's nothing like that.
    """

    """
    He seems uneasy.

    He is probably ashamed of what he is doing.

    I shouldn't push him further.
    """

    $ lad_details.unlock_knowledge('job') 

    $ psychic_details.saved_variables['knows_lad_background'] = True

    return

label lad_generic_heroic_act_psychic:
    
    lad """
    I was in the papers for rescuing a baby from a building on fire.

    It happened last year.
    """

    psychic """
    How impressive! What I've done is nothing compare to that.
    
    Please tell me more about it.    
    """

    lad """
    I don't know how impressive it really was.
    
    It was more a matter of being at the right place at the right moment.
    """

    pause 1

    # todo scene fire_building

    $ play_music('mysterious', 3,fadeout_val=2, fadein_val=2 )

    lad """
    I was just going home one day, it was rather late.

    On my way I happened to noticed smoke coming from a house across the street.

    I was about to call for the firemen.

    But out of the window, I heard a baby screaming.

    I couldn't possibly stay there and do nothing.

    So without thinking about it, I forced the front door of the house and ran upstairs.

    A fire was spreading from one of the rooms.

    Luckily, the one with the baby was still safe.

    So I ran into it, grabbed the baby and went downstairs as fast as I could.

    When I reached outside, I could here the firemen on their way.

    The neighbours had already alerted them.

    As soon as they arrived, I gave them the baby.

    Reporters were with them.

    When they saw me, they decided it was a story worth printing.

    But it wasn't really. Anyone would have done the same.

    I think they just wanted to sell papers. So they exaggerated what I had done.

    And they also omitted the worst part.
    """

    pause 1.0 

    """
    The baby wasn't alone in the house of course.

    Why would he have been.

    The fire was caused by the nanny.
    
    She had an attack and dropped a lamp on the floor.

    That was her room that was on fire.

    I didn't even check there.

    So when the firemen arrived, it was too late.

    They said they was nothing I could have done, but I am not sure.
    """

    $ change_room('PREVIOUS') # TODO PREVIOUS ROOM !!!!!!

    psychic """
    Don't say that. I am certain it was too late for her.

    You did the only thing you could have done.

    You shouldn't blame yourself.
    """

    lad """
    I guess.

    But it's hard.

    I still have nightmares about it.
    """    

    psychic """
    ...
    """

    """
    I don't know what to say here.
    """

    $ play_music('PREVIOUS')

    return

label lad_generic_manor:
    
    lad """
    It's very nice.

    A bit far out of town I think.

    But I suppose some people like the isolation.
    """

    return