# Generic lad Dialogs.
# Accessible from :
#                   - The Psychic
#                   - TODO not sure

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

    I just arrived, and I didn't realize I would be the last one here.
    """

    return

label lad_generic_room_psychic:

    lad """
    Oh, I am in the "William the Conqueror" Bedroom.
    """

    psychic """
    An impressive king.
    """

    lad """
    Really, he was?
    """

    """
    Is he serious?

    Hasn't he heard of "William the Conqueror"?
    """

    psychic """
    Well, he was a French Duke who was able to take the throne of England from very powerful men.

    That's not nothing.

    On the other hand, he was sometimes also called the Bastard King.

    So make of that what you will.
    """

    $ unlock_map('bedroom_lad')

    return


label lad_generic_age_psychic:

    lad """
    I am 22 years old.
    """

    """
    That make sense, but he somewhat looks older than that.

    I guess it's his rugged look.

    Life is not easy for the working class.
    """

    $ lad_details.description_hidden.unlock('age')

    return


label lad_generic_background_1:

    lad """
    There isn't much to say about me.

    I was born and raised in Birmingham.
    
    I work there as a business associate.
    """

    $ lad_details.description_hidden.unlock('origin') 

    return


label lad_generic_background_psychic:
    
    call lad_generic_background_1

    psychic """
    Interesting, in what type of business?
    """

    lad """
    Well, just regular sales.
    """

    psychic """
    And do you sell anything in particular?
    """

    lad """
    A bit of everything, depending on the opportunities.
    """

    psychic """
    You don't have a store then?
    """

    lad """
    No, no, it's nothing like that.
    """

    """
    He seems uneasy.

    He is probably ashamed of what he is doing.

    I shouldn't push him further.
    """

    $ lad_details.description_hidden.unlock('job') 

    $ psychic_details.saved_variables['knows_lad_background'] = True

    return


label lad_generic_background_doctor:
    
    call lad_generic_background_1

    doctor """
    In what line of business?
    """

    lad """
    Oh, you know, regular sales.
    """

    doctor """
    Of course. What do you sell the most?
    """

    lad """
    I cannot say that I work with a specific product; it depends on the opportunities.
    """

    doctor """
    I see.
    """

    $ lad_details.description_hidden.unlock('job') 

    """
    There is something off about his answers.

    I do not think he is telling me the whole story.
    
    Perhaps I could probe him a little further.
    """

    call run_menu( TimedMenu("lad_generic_background_doctor", [
        TimedMenuChoice("I might have something to sell you", 'lad_generic_background_doctor_thief', 30, early_exit=True),
        TimedMenuChoice("No, let us just leave it at that", 'generic_cancel', 15, early_exit=True),
        ])
    )

    return


label lad_generic_background_doctor_thief:

    lad """
    Really?

    I thought you were a doctor.
    """

    doctor """
    I am, and because of that I sometimes have access to certain products in large quantities.

    Perhaps you can help me with it.
    """

    lad """
    That depends; could you tell me more?
    """

    doctor """
    Not here. It is rather sensitive.

    It is not for everyone to hear, if you see what I mean?
    """

    lad """
    Understood. I can be discreet when necessary.
    """

    doctor """
    Perfect, we will talk later.
    """

    """
    I knew it.
    """
    
    $ lad_details.description_hidden.unlock('thief') 

    #TODO: ADD for doctor choice to sell stuff to lad????? what 
    # If you go to his room

    return


label lad_generic_heroic_act_psychic:
    
    lad """
    I was in the papers for rescuing a baby from a building on fire.

    It happened last year.
    """

    psychic """
    How impressive! What I've done is nothing compared to that.
    
    Please tell me more about it.    
    """

    lad """
    I don't know how impressive it really was.
    
    It was more a matter of being in the right place at the right moment.
    """

    pause 1

    $ change_room('house_on_fire')

    $ play_music('mysterious', 3, fadeout_val=2, fadein_val=2)

    lad """
    I was just going home one day, it was rather late.

    On my way, I happened to notice smoke coming from a house across the street.

    I was about to call for the firemen.

    But out of the window, I heard a baby screaming.

    I couldn't possibly stay there and do nothing.

    So without thinking about it, I forced the front door of the house and ran upstairs.

    A fire was spreading from one of the rooms.

    Luckily, the room with the baby was still safe.

    So I ran into it, grabbed the baby, and went downstairs as fast as I could.

    When I reached outside, I could hear the firemen on their way.

    The neighbors had already alerted them.

    As soon as they arrived, I gave them the baby.

    Reporters were with them.

    When they saw me, they decided it was a story worth printing.

    But it wasn't really. Anyone would have done the same.

    I think they just wanted to sell papers. So they exaggerated what I had done.

    And they also omitted the worst part.
    """

    lad """
    The baby wasn't alone in the house, of course.

    Why would they have been?

    The fire was caused by the nanny.
    
    She had an attack and dropped a lamp on the floor.

    That was her room that was on fire.

    I didn't even check there.

    So when the firemen arrived, it was too late.

    They said there was nothing I could have done, but I am not sure.
    """

    $ change_room('PREVIOUS')

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

    $ lad_details.description_hidden.unlock('heroic_act') 

    $ play_music('PREVIOUS')

    return

label lad_generic_manor:
    
    lad """
    It's very nice.

    It's a bit far from town, I think.

    But I suppose some people like the isolation.
    """

    return