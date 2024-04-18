label psychic_downstairs_default:

    $ change_room("basement_stairs")

    """
    The basement is where the domestic staff work.
    
    I definitely shouldn't go down there, it's not my place.
    """

    return

label psychic_library_default:

    $ change_room('library') 
    
    """
    Here is an impressive library.

    "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain." is open on a table.
    """

    """
    But I don't feel like reading now.
    """

    return

label psychic_library_look_for_lord:

    $ change_room('library') 
    
    """
    Here is an impressive library.

    "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain." is open on a table.
    """

    """
    I take a closer look at the book.

    It's the 8th edition, printed in 1894. That was quite some time ago.

    Perhaps I should look up information about the people living here.
    """ 

    play sound page_turning

    pause 2.0

    """
    It takes some time, but eventually I find the page with the entries for Claythorn Manor.

    There's quite a list of places mentioned here.
    """

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
    Nicholas Creswell The Third of Claythorn Manor.

    Born on June 22, 1813.

    His parents were Nicholas Creswell the Second of Claythorn Manor and Agnes Cicely.

    With Mary Kirwan, his wife, he fathered one son and one daughter:

    1. Elisabeth, his heir, born in 1865.
    
    2. Andrew, born in 1867, died in 1869.

    Lineage...
    """

    # TODO should we unlock THe host age (NO because it's not the good one?) but the first name is not ok either?
    # $ host_details.description_hidden.unlock('name') 

    """
    There's additional information about the history of this place.

    But something seems off.

    Born in 1813.

    Wait, that would make him...

    111 years old?

    That can't be right.

    If that were true, he'd likely be the oldest man in England.

    Possibly even the world.

    Yet he didn’t appear to be that old.
    """

    $ psychic_details.observations.unlock('lord')

    return


label psychic_library_look_for_lord_failed:

    call psychic_library_look_for_lord

    """
    Without further information, I can't possibly guess which manor is the one I'm in.
    """

    return


label psychic_tea_room_default:
    
    $ change_room('tea_room')
    
    """
    There's no one here.

    There's no reason to linger.
    """

    return

label psychic_dining_room_default:
    
    $ change_room('dining_room')
    
    """
    The dining area is currently unoccupied.

    I shouldn't stay here.
    """

    return


label psychic_billiard_room_default:
    
    $ change_room('billiard_room')
    
    """
    The billiard room is empty right now.

    I should leave.
    """

    return


label psychic_garden_default:

    $ change_room('manor_garden')
    
    """
    A lovely garden.

    I took a peaceful stroll through it.

    Still, nothing caught my attention.
    """

    return


label psychic_entrance_hall_default:
    
    $ change_room("great_hall")
    
    """
    A very nice great hall.
    
    But it is totally empty.
    """

    return

label psychic_portrait_gallery_look_for_lord:
    
    call psychic_portrait_gallery_default

    """
    Now, I realize that there are probably paintings of the Claythorn family here.

    I should check if there is one with Lord Claythorn in it.
    """

    pause 2.0

    """
    It doesn't take long for me to spot him.

    He looks exactly as he does in real life.

    I check the label below the painting.

    "Nicholas III, of Claythorn Manor"

    So, Nicholas is his first name.
    """

    $ psychic_details.saved_variables['knows_lord_name'] = True
    $ lord_name = "Sir Nicholas"

    return

label psychic_portrait_gallery_default:
    
    $ change_room("portrait_gallery")

    if not psychic_details.saved_variables["portrait_gallery_visited"]:
    
        """
        There are quite a few impressive portraits here.

        However, no one else is present.
        """

        $ psychic_details.saved_variables["portrait_gallery_visited"] = True
    
    else:

        """
        The paintings remain unchanged.
        """

        # TODO: Or did they change? 

    return


label psychic_bedroom_default:
    
    $ change_room("bedrooms_hallway")

    play sound door_knock
    
    """
    I knock on the door, waiting for a response.

    There's silence. No one replies.
    """

    return


# Attic
label psychic_attic_default:

    $ change_room("attic_hallway")

    # TODO really keep this? but to what end?
    if not psychic_details.saved_variables["attic_visited"]:

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

        Yes.

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
        I am not sure what that was.

        But I don't think I should return here too soon.
        """

        $ play_music('PREVIOUS')

        $ psychic_details.saved_variables["attic_visited"] = True
    
    else:

        """
        I climb the stairs to the attic.

        The room is filled with darkness.

        I think I shouldn't venture here.

        There's no reason for me to disturb Lord Claythorn any further,

        at least for now.
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
            TimedMenuChoice('Of course I should!', 'psychic_confront_lord', early_exit=True),
            TimedMenuChoice("On second thought, it is rather scary. Let's back down.", 'generic_cancel', early_exit=True)
        ])
    )

    """
    I've changed my mind, I'd better leave him alone.

    God knows what I might stir up here.
    """

    return

label psychic_confront_lord:

    $ play_music('scary', 3)

    """
    I know I must confront him.

    But what am I hoping to prove?

    That's a dangerous path I fear I'm taking here.
    """

    psychic """
    Sir Nicholas, are you here?
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
    That you are 111 years old.
    """

    lord """
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

    Because either I am a ghost...

    Or maybe you're just losing your mind.
    """


    """
    He inches closer to me.
    """

    lord angry """
    So, which will it be?

    That a liar, someone who preyed on the bereaved to make money,

    is actually a real-life medium?

    That it was in her all along?

    Then maybe she wasn't really deceiving people her entire life.

    But it's too simple now, isn't it?

    You understand what's happening here, don't you?
    """
    
    """
    He is now almost next to my face.

    I can't take this.

    I slowly take a step back.

    But my foot doesn't find the ground behind me.
    """

    play sound body_fall

    jump psychic_ending_lord
