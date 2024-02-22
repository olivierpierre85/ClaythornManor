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

    It's the 8th edition, printed in 1894. A while ago then.

    Maybe I should check out "Lord Claythorn" in this book.
    """ 

    play sound page_turning

    pause 2.0

    """
    It takes a while, but in the end I found the page with the entries for Claythorn.

    There are more than a dozen person of the same name.
    """

    return

label psychic_library_look_for_lord_succeed:

    if psychic_details.saved_variables['book_read']==False:
        call psychic_library_look_for_lord
    else:

        """
        I reach again for the page with the Claythorn name.

        Now I now which one to look at.
        """

    """
    Nicholas Claythorn is the third entry in the book.
    """

    letter """
    NICHOLAS CRESWELL THE THIRD OF CLAYTHORN MANOR.

    Born 22 June, 1813
    Parents: Nicholas Creswell the second of Claythorn Manor and
    Agnes Cicely

    By Mary Kirwan, his wife, he had 1 son and 1 daughter.

    1. Elisabeth, his heir born 1865
    2. Andrew born 1867, death 1869

    Lineage...
    """

    """
    There is more information on the history of this place.

    But something is not right.

    Born in 1813.

    Wait that would made him.

    111 years old?

    That can't be right.

    If that was true, he would probably be the oldest man in England.

    Maybe the world.

    But he didn't look that old.
    """

    $ psychic_details.observations.unlock('lord')

    return

label psychic_library_look_for_lord_failed:

    call psychic_library_look_for_lord

    """
    Without more information, I can't possibly guess which Claythorn this manor belongs to.
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
    Now, I realize that they are probably paintings of the Claythorn family here.

    I should check if there is one with Lord Claythorn in here.
    """

    pause 2.0

    """
    It doesn't take long for me to spot him.

    He looks exactly like as in real life.

    I check on the label below the painting.

    "Nicholas Claythorn, third of his name."

    Nicholas is is first name then.

    Good to know.
    """

    $ psychic_details.saved_variables['knows_lord_name'] = True

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

        $ play_music('mysterious', 3, fadeout_val=2, fadein_val=2)

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
        I climbed the stairs to the attic.

        The room is filled with darkness.

        I don't think I should venture here.

        There is no reason for me to disturb Lord Claythorn any further.
        
        For now at least.
        """

    return

# TODO maybe won't ever be used? Find what to do with attic
# label psychic_storage_default:

#     call psychic_attic_default

#     """
#     I try to open the attic storage room, but it's closed.
#     """
    
#     return

# label psychic_females_room_default:

#     call psychic_attic_default

#     """
#     I try to open the room, but it's closed.
#     """

#     return

# label psychic_males_room_default:

#     call psychic_attic_default

#     """
#     I try to open the room, but it's closed.
#     """

#     return

# label psychic_butler_room_default:
    
#     call psychic_attic_default

#     """
#     I try to open the room, but it's closed.
#     """

#     return