# Attic
label psychic_attic_default:

    $ change_room("attic_hallway")

    """
    I climb the stairs to the attic and arrive in a dimly lit hallway.

    There are multiple doors, most of them lie in darkness.

    As I move into the hallway, I hear something.
    """

    $ play_music('mysterious')

    lord """
    Hello, is someone there?
    """

    psychic """
    Hello...

    My name is Amelia Baxter.
    """

    lord """
    Nice to meet you, Miss Baxter.

    It's rare to meet someone up here.

    I am usually by myself.
    """

    psychic """
    Nice to meet you too.

    I am sorry to ask,

    but who are you?
    """

    lord """
    Oh, where are my manners?

    I am the Lord of this Manor, of course.
    """

    """
    Wait, what?
    """

    psychic """
    I am sorry, Lady Claythorn didn't mention you.
    """

    lord """
    Lady Claythorn? You probably mean my daughter then.

    I suppose she likes having all the attention to herself.

    She must be relieved that I spend most of my time alone in my room here.
    """

    psychic """
    You live here?
    """

    lord """
    Yes, it's rather uncommon, but I enjoy how peaceful it is.

    Plus, I believe I have the biggest room in the manor.
    """

    """
    He points to the big door in front of the stairs.
    """

    psychic """
    Right...
    """

    """
    I don't know what to say. There is something wrong with all this.
    """

    lord """
    So my dear, were you looking for something in particular by coming here?
    """

    psychic """
    Well, not really. I was mostly exploring your home.
    """

    lord """
    In that case, I would advise you not to linger here.

    There's not much to see in this old attic.

    You'll find more interesting rooms downstairs.
    """

    """
    Alright, he probably wants to stay alone.
    """

    psychic """
    Of course, I will continue visiting elsewhere.
    """

    lord """
    Thank you, my dear.

    Enjoy your stay.
    """

    psychic """
    Thank you.
    """

    """
    This was rather peculiar.

    I don't think I should return here too soon.
    """

    $ play_music('PREVIOUS')

    $ psychic_details.saved_variables["attic_visited"] = True

    return


label psychic_attic_return_too_soon:

    $ change_room("attic_hallway")

    """
    I climb the stairs to the attic.

    The room is filled with darkness.

    I think I shouldn't venture here.

    There's no reason for me to disturb Lord Claythorn any further,

    at least for now.

    So I turn back.
    """

    return 

label psychic_attic_return:

    $ change_room("attic_hallway")

    """
    I've decided to return to the attic.

    I have some questions to ask the "Lord" of this place.

    But am I sure I should?
    """

    call run_menu(
        TimedMenu("psychic_lord_ending_menu", [
            TimedMenuChoice('Of course, there is no logical reason to be afraid', 'psychic_confront_lord', early_exit=True),
            TimedMenuChoice("On second thought, it is rather scary. Let's back down", 'generic_cancel', early_exit=True)
        ])
    )

    """
    I've changed my mind, I'd better leave him alone.

    God knows what I might stir up here.
    """

    return


label psychic_library_look_for_lord:

    call psychic_library_intro

    """
    I take a closer look at the book.

    It's the 8th edition, printed in 1894. That was quite some time ago.

    Perhaps I should look up information about the people living here.
    """ 

    play sound page_turning

    pause 2.0

    """
    I find multiple entries for families with the name Claythorn.
    """

    $ psychic_details.saved_variables['book_read'] == True

    return

label psychic_library_look_for_lord_succeed:

    if psychic_details.saved_variables['book_read'] == False:
        
        call psychic_library_look_for_lord

    else:

        """
        I turn back to the page with the Claythorn name.

        Now I know which one to look at.
        """

    """
    There's only one place associated with a Nicholas.
    """

    book """
    Nicholas Claythorn The Third of Claythorn Manor.

    Born on June 22, 1813.

    His parents were Nicholas Claythorn the Second of Claythorn Manor and Agnes Cicely.

    With Mary Kirwan, his wife, he fathered one son and one daughter:

    1. Elisabeth, his heir, born in 1865.
    
    2. Andrew, born in 1867, died in 1869.

    Lineage...
    """

    $ host_details.description_hidden.unlock('name_age') 

    """
    There's additional information about the history of this place.

    But something seems off.

    Born in 1813.

    Wait, that would make him...

    111 years old?

    That can't be right.

    If that were true, he'd likely be the oldest man in England.

    Possibly even the world.

    Yet he didn't appear to be that old.

    I suppose this must be an mistake in the book.

    If they tried to list all the gentry of this country, they were bound to make some errors.
    """

    $ psychic_details.observations.unlock('lord')

    return


label psychic_library_look_for_lord_failed:

    call psychic_library_look_for_lord

    """
    But I am not sure which one relates to the family living here.

    How could I? I don't even know Lady Claythorn's first name.
    """

    return


label psychic_portrait_gallery_look_for_lord:
    
    call psychic_portrait_gallery_default

    """
    Now, I realize that there are probably paintings of the Claythorn family here.
    """

    pause 2.0

    """
    I can't find Lady Claythorn here, but after a while I spot Lord Claythorn.

    He looks exactly as he does in real life.

    I check the label below the painting.

    "Nicholas III, of Claythorn Manor"

    So, Nicholas is his first name.
    """

    $ psychic_details.saved_variables['knows_lord_name'] = True
    $ lord_name = "Sir Nicholas"

    return

label psychic_confront_lord:

    $ play_music('scary', 3)

    """
    I know I must confront him.

    But what am I hoping to prove?

    That's a dangerous path I fear I'm taking here.

    He is not in the hallway, so I head to his room.

    I don't bother knocking and enter right away.
    """

    play sound door_open

    $ change_room("attic_big_room")

    """
    It's even more decrepit than the rest of the attic.

    Why would anyone decide to live here?
    """

    psychic """
    Sir Nicholas, are you there?
    """

    pause 1.0

    lord """
    Oh good, you've returned.

    And you've learned my name as well.

    Impressive.
    """

    psychic """
    That's not all I've learned, though.
    """

    lord """
    Really? What else?
    """

    psychic """
    That you're supposed to be 111 years old.
    
    Is this true?
    """

    lord """
    111 years...

    Has it been that long already?

    Well, I suppose that's true.
    """

    psychic """
    No one can live this long.
    """

    lord """
    Probably not.
    """

    psychic """
    So, are you...

    Are you...
    """

    lord """
    Am I what, my dear?

    Dead?
    """

    lord """
    That's what you think, right?

    Or rather, it's what you're hoping.
    """

    psychic surprised """
    What do you mean?
    """

    lord """
    Because either I am a ghost...

    Or you're just losing your mind.
    """

    """
    He inches closer to me.
    """

    lord angry """
    So, which will it be?

    That a liar, someone who preyed on the bereaved to make money,

    is actually a real-life medium?

    That it was in her all along?

    I understand the appeal to believe that now.

    That would mean that you weren't really deceiving people your entire life.

    But that would be too easy, wouldn't it?

    I am afraid there is only one other alternative.

    You must see it too now.

    You understand what's happening here, don't you?
    """
    
    """
    He is now almost next to my face.

    I can't take this.

    I rush outside his room.
    """

    $ change_room("attic_hallway")

    """
    But he is already there.

    Standing in front of me.
    """

    lord angry """
    Where are you going?

    Do you think you can get rid of me that easily?
    """

    psychic surprised """
    What do you want from me?
    """

    lord angry """
    Me? I don't want anything.

    The question is: what do you want?
    """

    """
    I slowly take a step back towards the stairs.
    """

    lord angry """
    Do you feel remorse maybe?
    """

    """
    I take another step.
    """

    lord angry """
    Some regret over what you've done?
    """

    psychic surprised """
    Please, leave me alone.
    """

    """
    I try to walk back further,

    but my foot doesn't find the ground behind me.
    """

    play sound body_fall

    jump psychic_ending_lord
