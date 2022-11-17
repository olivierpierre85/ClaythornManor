label lad_day2_afternoon_bedroom:
    call  change_room('lad_room')

    call change_time(16,00)

    """
    So we carried Doctor Baldwin to his room and lay him down on his bed.

    Afterwards, I retreated to my room to change my clothes.

    They were stained with blood.

    As I was preparing to go downstairs again, someone knocks on my door.
    """

    play sound door_knock

    psychic """
    Mister Harring, can I come in ?
    """

    """
    Amelia Baxter... What does she want ?
    """

    # TODO CHoice of letting her in or not ?

    lad """
    Come on in Mrs Baxter. The door is open.
    """

    play sound door_open

    # play mystery music

    psychic """
    I am sorry to intrude, but I think we should talk.
    """

    """
    She doesn't wait for an answer and starts explaining.
    """

    psychic """
    There is something dangerous happening here.
    """

    lad """
    What do you mean ?
    """

    psychic """
    I mean that I don't think those deaths were an accident.
    """

    lad """
    What makes you think that ?
    """

    psychic """
    Don't you think is strange two different persons died in the same place, of two different causes ?
    """

    lad """
    Well, I don't know for Thomas Moody. 
    
    But for the doctor's death, you said it yourself: Samuel Manning was probably drunk. 
    
    That's sad, but not really a surprise.
    """

    psychic """
    That's what I thought at first. 

    But I just had a chat with the butler. He could swear that Samuel Manning was clear of mind when he gave him his gun.
    """

    lad """
    So what, you think he faked the accident ?

    He could have simply drank too much during the hunt.
    """

    psychic """
    True, but it's still suspicious. 

    And I have other reasons to believe there is something off here.

    Let's just say I can feel it.
    """

    lad """
    You can 'feel' it ?
    """

    psychic """
    Don't mock what you don't understand Mister Harring.

    But it's alright, I don't need you to believe me.

    I am just warning you to be careful.
    """

    lad """
    You are afraid of Samuel Manning ?
    """

    psychic """
    Yes, but not only of him. 
    
    Other people may be involved in this.

    I don't think we can trust anyone.
    """

    lad """
    You seem to trust me. 
    """

    psychic """
    Well I wouldn't say that exactly. 

    But if someone is after me, I couldn't defend myself. So I need an ally. 

    And you are strong enough to protect me in case their is a direct confrontation.

    So I made a bet to confide in you.
    
    I hope I was right.
    """

    """
    I don't know what to say.

    But she leaves before I could answer.

    A murder ?

    It's probably nonsense.

    But still ...

    What should I do now ?
    """

    call change_time(17,00)

    $ time_left = 90

    # TODO More possibilities 
    call run_menu(TimedMenu([
            TimedMenuChoice('Library', 'lad_library', 10, room = 'library'), # condition not visited ?
            TimedMenuChoice('Richard III Bedroom', 'lad_day2_broken_room', 20, room = 'broken_room'),
            TimedMenuChoice('Edward II Bedroom', 'lad_day2_doctor_room', 20, room = 'doctor_room'),
            TimedMenuChoice('Rest in your room until dinner.', 'lad_day2_afternoon_skip', early_exit = True, room = 'lad_room'),
        ], is_map = True))


    call change_time(18,30)

    play sound dinner_gong

    """
    I hear the gong.

    I should go to the dining room.
    """

    jump lad_day2_evening

label lad_day2_afternoon_skip:

    """
    I can't think of anything interesting to do now.

    So I better rest.
    """

    return

label lad_day2_doctor_room:

    scene bedroom_doctor

    """
    I don't feel good being in here.

    But I might as well look for something useful.

    I look over his personal effects when I stubble into his medication suitcase.

    There is nothing out of the ordinary in there.

    A stethoscope, bandages, a few bottle of medications,...

    There is one in particular that he has more that the others. 
    
    Laudanum is written on the label.

    He has almost a dozen of those bottles.

    Laudanum... , I heard that before.
    
    It's opium.

    Looks like the doctor wasn't using it only on patients.
    """

    $ doctor_details.add_knowledge('addict') 

    """
    And I might as well take a few for myself.
    """

    # TODO is the lad a thief ? likely ADD HERE

    return

