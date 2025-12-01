label doctor_day2_evening_exploration:
    
    call change_time(21, 00)

    $ change_room("bedroom_doctor")

    """
    I now find myself faced with several courses of action.

    The most obvious would be to remain here in my room and wait for the morning.

    I could even move some furniture against the door to make certain no one can enter.

    Yet that, too, feels dangerous. There are other ways for someone to reach me.

    The alternative is to attempt to discover who wrote that note to Samuel Manning.

    That is the person I ought to fear.

    Everything points towards Lady Claythorn, yet I cannot be sure.

    If only I could trust at least one other person, I might ask for their assistance.

    It would be safer to investigate in company, but in whom ought I place my trust?

    It would be ideal to have someone implicitly trustworthy, like a judge.

    But everyone here appears suspicious to me.
    """

    if doctor_details.important_choices.is_unlocked('flirt'):

        """
        I might turn to Andrew. After the time we have spent together, I find it hard to picture him as a likely culprit.

        He is probably downstairs with the staff at present, unless he has already retired for the night.
        """

    if doctor_details.observations.is_unlocked('remember_nurse'):

        """
        By good fortune, I already know Nurse Rosalind Marsh. That acquaintance makes me more comfortable about approaching her.
        """
    
    if doctor_details.objects.is_unlocked('book_opium'):
        
        """
        To make matters worse, the symptoms of withdrawal are steadily increasing.

        My hands tremble, and I am sweating more than is reasonable.

        They will only grow worse as the night wears on, which will not be in my favour.
        """

    """
    I feel very much at a crossroads.

    What I decide to do now may mean the difference between life and death.

    So what shall it be?
    """

    $ time_left = 90
    call run_menu(doctor_details.saved_variables["day2_evening_map_menu"])

    return


label doctor_day2_evening_billiard_room:

    $ change_room('billiard_room')

    if not doctor_details.saved_variables["day2_evening_billiard_room_visited"]:

        $ doctor_details.saved_variables["day2_evening_billiard_room_visited"] = True

        """
        Just as I imagined, the room is almost deserted.

        I can see only Captain Sinha seated upon a sofa, and the butler standing discreetly in the corner.

        The bar is still available, but I promised myself to keep a clear head, so I ought to avoid it.
        """

        $ doctor_day2_evening_billiard_room_menu = TimedMenu("doctor_day2_evening_billiard_room_menu", [
            TimedMenuChoice('Talk to Sushil Sinha', 'doctor_day2_evening_billiard_room_captain'),
            TimedMenuChoice('Go to the bar for a drink', 'doctor_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ doctor_day2_evening_billiard_room_menu.early_exit = False

        """
        I find myself once more in the billiard room.

        Little appears to have changed since my last visit.
        """

    call run_menu(doctor_day2_evening_billiard_room_menu)

    return


label doctor_day2_evening_billiard_room_bar:

    """
    In spite of knowing full well it is a mistake, my steps carry me straight to the bar.

    Before I have quite registered it, I am already pouring myself a glass of sherry.

    The moment I realise what I have done, a wave of shame washes over me.

    Yet now that the glass is in my hand, I cannot simply set it aside.

    I might as well drink it.

    But this will be the last one.
    """

    if doctor_details.objects.is_unlocked('book_opium'):

        """
        At last, I have a chance to free myself from opium entirely.

        I shouldn't exchange one addiction for another.
        """

    return


label doctor_day2_evening_billiard_room_captain:

    """
    I go over to Captain Sinha.

    He notices my approach and sets his book down upon the table.
    """

    captain """
    Doctor Baldwin, it is good to see you.

    I fear most of the other guests have decided to remain in their rooms.
    """

    doctor """
    Really?

    What should they be afraid of?
    """

    captain """
    Well, nothing, of course.

    It is obvious to me that the two unhappy deaths this weekend were both tragic, but unfortunate events.
    """

    doctor """
    Yet you believe not everyone agrees with you.

    So they are afraid, but of what exactly?

    Ah.

    I suppose they must be afraid of me.

    And here I thought they had accepted that what occurred during the hunt was a dreadful accident.
    """

    captain """
    Do not reproach yourself too much, Doctor.

    I am sure they still think so, but they prefer to be cautious.

    Most of them are not accustomed to being so close to death as you and I.
    """

    doctor """
    Quite.

    I had not considered it from that angle.
    """

    captain """
    But tell me, was there something in particular you wished to speak to me about, Doctor?
    """

    call run_menu(
        TimedMenu("doctor_day2_evening_billiard_room_captain", [
            TimedMenuChoice("Tell him about the letter", 'doctor_day2_evening_billiard_room_captain_letter'),
            TimedMenuChoice("Tell him about Thomas Moody's face", 'doctor_day2_evening_billiard_room_captain_mask', 30 ,condition="doctor_details.observations.is_unlocked('broken_unmasked') and all_menus['doctor_day2_evening_billiard_room_captain'].choices[0].hidden"),
            TimedMenuChoice("Find someone else to confide in", 'doctor_day2_evening_billiard_room_captain_avoid', keep_alive=True, early_exit = True),
        ])
    )

    return


label doctor_day2_evening_billiard_room_captain_letter:

    doctor """
    There is something I need to share with you.

    I have not been entirely honest about what happened before the hunt.
    """

    """
    I lower my voice and give him a brief account of the letter I found, and how it led to the quarrel with Samuel Manning and, in the end, to his death.

    The captain listens to it all without the slightest change in his expression.

    When I have finished, he answers at last.
    """

    captain """
    I admit this is very strange.

    But you must forgive me, I am not quite sure what to do with this information.
    """

    doctor """
    What do you mean?

    This surely proves beyond doubt that something very wrong is happening here.

    I am telling you so that we may work together to discover what is truly going on.
    """

    """
    Sushil Sinha studies me in silence for a moment.
    """

    captain """
    I see.

    Do not take this amiss, Doctor, but I cannot simply accept your word on what you have just told me.

    Do you have any proof of it?
    """

    doctor """
    Not really. 
    
    I did not take the letter with me, that would have appeared far too suspicious.
    """

    if doctor_details.observations.is_unlocked('burned_letter'):

        doctor """
        And I have been in Samuel Manning's room since.

        He burned the letter before leaving for the hunt.
        """

    captain """
    That's not ideal.

    I do not say that I disbelieve you.

    But put yourself in my place.

    If I were to accuse our hostess, or any of the guests, on this alone, I should be thought excitable at best, malicious at worst.
    """

    """
    He does not trust me, not entirely.

    I understand.

    In the end, I am the one who killed Samuel Manning, so to him I must be the most suspicious person in this house.

    If I truly wish to convince him, I will need stronger evidence.
    """

    doctor """
    I understand.

    I will not trouble you further for now.

    I will leave you to your book.
    """

    captain """
    I am sorry, Doctor.

    But if you have upon more convincing evidence, I may yet change my mind about this whole affair.
    """

    return


label doctor_day2_evening_billiard_room_captain_mask:

    """
    I hesitate for a moment, then decide to speak plainly.

    If I want an ally, I must be prepared to share the whole truth.
    """

    doctor """
    There is indeed something else.

    It concerns Thomas Moody.
    """

    captain """
    Moody?

    The chap from the City?
    """

    doctor """
    Yes.

    When we first met, he wore a mask and would not remove it.

    I thought it an odd affectation, but I did not press him.

    After his death, when I examined the body, I saw why he wore it.

    His face was terribly disfigured, as though by burns or some old injury.

    It was not a recent wound.
    """

    """
    I can still picture the ravaged features in my mind.

    They were not the marks of a man in perfect health who simply fell and broke his neck.
    """

    doctor """
    You were not present during the examination.

    You saw only the body later, when it had been made as presentable as possible.

    But there is something else.

    When I was in his room, I was distracted.

    I fear I may have overlooked certain details.
    """

    captain """
    Overlooked what sort of details?
    """

    doctor """
    Bottles on the nightstand.

    Medicines perhaps.

    I was more concerned with the obvious signs of death than with what he might have taken before it.
    """

    captain """
    Hm.

    That is the sort of thing which can make all the difference.

    Show me the room, Doctor.

    If there is anything of that nature, I should like to see it with my own eyes.
    """

    """
    We leave the billiard room together, moving as quietly as we can along the corridor.

    The house feels oddly hollow, as if all life had retreated behind closed doors.
    """

    # TODO: change_room to Thomas Moody's bedroom, if needed
    # $ change_room("bedroom_moody")

    """
    When we reach Thomas Moody's room, I unlock the door and step aside to let the captain enter first.

    The air is faintly stale, with a lingering scent of tobacco and something medicinal.
    """

    captain """
    Do not trouble yourself, Doctor.

    I have seen the dead before.
    """

    """
    He crosses to the bed and looks down at the still form, his expression grave but composed.

    Then his gaze shifts to the small table by the bedside.
    """

    captain """
    Ah.

    There we are.
    """

    """
    He picks up a small bottle I scarcely recall noticing.

    He turns it between his fingers, reading the label in silence.
    """

    captain """
    This is not any ordinary sleeping draught.

    I know this maker.

    They supply vermin poison to estates in my part of the country.

    A few drops would be quite sufficient to stop a man's heart.
    """

    doctor """
    Are you certain?
    """

    captain """
    Quite certain.

    If this was in his glass, then Thomas Moody did not die by mischance.

    Someone wished him out of the way.
    """

    """
    A chill runs down my spine.

    I thought the events of the hunt might be linked to Samuel Manning alone.

    Now it seems that death is stalking more than one of us.
    """

    captain """
    You understand what this means, Doctor.

    You were right to suspect that something is amiss.

    I cannot in conscience pretend any longer that these are merely unfortunate accidents.
    """

    """
    For the first time since we arrived, I feel that I am no longer quite alone in my suspicions.
    """

    captain """
    Very well.

    From this moment, we watch and we share what we learn.

    But there is another matter.

    If someone in this house is prepared to kill once, or twice, they may not stop there.
    """

    doctor """
    You believe I might be in danger as well.
    """

    captain """
    I think we both might be.

    I have a favour to ask, and I hope you will not refuse me.
    """

    doctor """
    What is it?
    """

    captain """
    I would rather you did not sleep alone tonight.

    Come and share my room.

    There is a perfectly decent sofa, and we shall be within earshot of one another.

    If anything happens, at least we shall not be taken unawares.
    """

    """
    The idea of surrendering my solitude is not an attractive one.

    Yet the memory of the letter, and now this bottle, makes the prospect of a solitary night far more alarming.
    """

    call run_menu(
        TimedMenu("doctor_day2_evening_billiard_room_captain_sleep", [
            TimedMenuChoice("Accept his offer and sleep in his room", "doctor_day2_evening_captain_sleep_yes", early_exit = True),
            TimedMenuChoice("Refuse and sleep alone", "doctor_day2_evening_captain_sleep_no", early_exit = True),
        ])
    )

    # TODO: unlock a "trust_captain" flag here if desired
    # $ doctor_details.relationships.unlock('trust_captain')

    return


label doctor_day2_evening_captain_sleep_yes:

    doctor """
    You are right.

    It would be foolish to ignore the danger.

    I shall accept your offer.
    """

    captain """
    Good.

    We shall collect what you need from your room, then you can settle on my sofa.

    Between us, I doubt anyone will find us easy prey.
    """

    """
    It is not an arrangement I would ever have imagined myself making.

    Yet as we leave the room together, I feel a little less exposed than before.
    """

    # TODO: set a flag here so that the night sequence knows you are with the captain
    # $ doctor_details.saved_variables["slept_with_captain"] = True

    return


label doctor_day2_evening_captain_sleep_no:

    doctor """
    I am grateful for your concern, Captain, but I do not wish to impose upon you.

    I shall manage well enough in my own room.
    """

    captain """
    As you wish.

    I cannot compel you.

    But do at least lock your door, and keep something to hand that might serve as a weapon.

    I would rather not find we have misjudged the danger come morning.
    """

    """
    I nod, though my resolve feels less steady than I would like.

    If I choose to face the night alone, I must be prepared for whatever it brings.
    """


    return


label doctor_day2_evening_billiard_room_captain_avoid:

    doctor """
    Not especially.

    I merely wished to see who was about.
    """

    captain """
    Very well.

    If you do not mind, I was in the middle of a most captivating chapter.
    """

    doctor """
    Of course.

    I shall leave you to it.
    """

    """
    For all his courtesy, I do not feel ready to place my fate entirely in his hands.

    If I seek help, I may need to look elsewhere.
    """

    return
