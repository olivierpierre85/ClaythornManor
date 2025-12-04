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
            TimedMenuChoice('Talk to Sushil Sinha', 'doctor_day2_evening_billiard_room_captain', keep_alive = True),
            TimedMenuChoice('Go to the bar for a drink', 'doctor_day2_evening_billiard_room_bar', 10),
            TimedMenuChoice('Leave the room', 'generic_cancel', 0, keep_alive = True, early_exit = True)
        ])

    else:
        # Reset menu
        $ doctor_day2_evening_billiard_room_menu.early_exit = False

        """
        I find myself once more in the billiard room.
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

    if doctor_details.threads.is_unlocked('book_opium'):

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

    Why do you say that?
    """

    captain """
    I cannot be certain.

    But after what has happened today, I should not be surprised if some of our fellow guests are afraid to leave their rooms.
    """

    doctor """
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
            TimedMenuChoice("Tell him about Thomas Moody's face {{observation}}", 'doctor_day2_evening_billiard_room_captain_mask', 0 ,condition="doctor_details.threads.is_unlocked('broken_unmasked') and all_menus['doctor_day2_evening_billiard_room_captain'].choices[0].hidden"),
            TimedMenuChoice("Leave him alone", 'doctor_day2_evening_billiard_room_captain_avoid', keep_alive=True, early_exit = True),
        ])
    )

    return


label doctor_day2_evening_billiard_room_captain_avoid:

    doctor """
    I am sorry for disturbing you but I don't really have anything else to say.

    I will leave you to your book.
    """

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

    Do not take this the wrong way
    , Doctor, but I cannot simply accept your word on what you have just told me.

    Do you have any proof of it?
    """

    doctor """
    Not really. 
    
    I did not take the letter with me, that would have appeared far too suspicious.
    """

    if doctor_details.threads.is_unlocked('burned_letter'):

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

    return

# TODO READ EVERY AND CHANGE EVERYTHING FROM HERE!
label doctor_day2_evening_billiard_room_captain_mask:

    doctor """
    There is indeed something else.

    It concerns Thomas Moody.
    """

    captain """
    Moody?

    Did you discover something about his death?
    """

    doctor """
    Yes.

    But I think it is best if you see for yourself, so that you don't need to take my word for it.
    """

    captain """
    Hm.

    Very well, I suppose we could go to his room.

    Please, lead the way, Doctor.
    """

    """
    I see that he has no intention of turning his back on me.

    We leave the billiard room together, moving as quietly as we can along the corridor.

    The house feels oddly hollow, as though all life has retreated behind closed doors.
    """

    $ change_room("bedroom_broken")

    """
    When we reach Thomas Moody's room, I open the door and step inside first.
    """

    doctor """
    Here he is, Captain.

    I must warn you, it may not be a pleasant sight.
    """

    captain """
    Do not trouble yourself, Doctor.

    I have seen the dead before.
    """

    """
    He crosses to the bed and looks down at the still form, his expression grave but composed.
    """

    captain """
    So, what is this about?
    """

    """
    I lay my hands upon Thomas Moody's mask and lift it away, revealing a contorted and intact face.
    """

    captain """
    Good Lord, what a face he is making.

    What could have caused that, Doctor?
    """

    doctor """
    I am not certain, but it was no peaceful death, that much is clear.

    Yet you are not seeing the most peculiar part.
    """

    captain """
    What do you mean?

    Oh.

    His face, it is... normal.

    He made everyone believe that he had been disfigured during the war.

    Yet it was all an act.

    But why would he do such a thing?

    What are we to make of this?
    """

    doctor """
    I have no idea.

    It is suspicious enough that I did not wish to alert anyone else.
    """

    captain """
    I understand what you mean, Doctor.

    Of course you were right, something is amiss.

    I cannot pretend any longer that these are merely unfortunate accidents.
    """

    """
    He pauses for a moment, pondering the implications of what he has just learnt.

    Then his gaze lingers on the nightstand.

    Thomas Moody's hip flask lies on its side, a greenish liquid spilling from its mouth and pooling upon the wood.
    """

    captain """
    I assume our friend was drinking from this before he died.

    What kind of alcohol could that be?

    Crème de menthe, perhaps?
    """

    """
    He picks up the flask and brings it to his nose.
    """

    captain """
    How odd.

    That smells like whisky, heavily peated I might add.

    But why is there a green puddle on the nightstand?
    """

    """
    Of course.

    I cannot believe I did not notice this before.
    """

    doctor """
    Do not drink it, Captain.

    I believe you have found the murder weapon.
    """

    captain """
    Ah, so this is the poison that caused Thomas Moody's premature death, you think?
    """

    doctor """
    Precisely.

    Everything points to a form of strychnine poisoning.

    It is a common active ingredient in certain rat poisons.

    That is probably what has given his whisky this greenish hue.
    """

    captain """
    I see.

    So we now have two deaths that are highly suspicious.
    """

    """
    He thinks for few seconds about what that implies.
    """

    """
    If someone in this house is prepared to kill once, perhaps even twice, there is no reason to imagine they will stop there.

    I believe we may both be in danger.

    I simply do not understand why.

    Who could wish me dead?

    It is not as though I have no enemies, but nothing so severe that it ought to come to this.

    At least, I do not think so.

    What about you?
    """


    doctor """
    Well, as a doctor, I may have left a few unpleasant patients here and there.

    But, like you, I do not believe there is anything so serious that it should lead to murder.
    """

    """
    I am not entirely sure that I believe my own words.

    But I see no point in sharing those doubts.
    """

    captain """
    So, we have no notion of what may be happening.

    We know only that we are in danger here, presumably from Lady Claythorn herself, even if we have no proof we could present.
    """

    doctor """
    That is what I believe as well.

    I am simply not sure what we ought to do about it.
    """

    captain """
    Well, it would be difficult to leave now, in the middle of the night.

    So we should at least be prepared to spend one more night here.

    And attempting to confide in more people could be dangerous.

    Lady Claythorn may not be acting alone in this enterprise.

    If we confront her, she will become suspicious and it will be even harder to escape this place.

    We must take every precaution we can.
    """

    doctor """
    I agree, but what do you suggest we do?
    """

    """
    I believe we should not sleep alone tonight.

    Come and share my room.

    There is a perfectly decent sofa, and we shall be within earshot of one another.

    If anything happens, at least we shall not be taken unawares.
    """

    """
    I am not sure I like this idea.

    Yet, it may be the best chance I have of surviving this weekend.

    On the other hand, it forces me to trust Sushil Sinha with my life.

    I am not sure that I can do that.
    """

    call run_menu(
        TimedMenu("doctor_day2_evening_billiard_room_captain_sleep", [
            TimedMenuChoice("Accept his offer and sleep in his room", "doctor_day2_evening_captain_sleep_yes", TIME_MAX, early_exit = True),
            TimedMenuChoice("Refuse", "doctor_day2_evening_captain_sleep_no", early_exit = True),
        ])
    )

    return


label doctor_day2_evening_captain_sleep_yes:

    doctor """
    You are right.

    It would be foolish to ignore the danger.

    I think it is better if we stay together.
    """

    captain """
    Good.

    You can collect whatever you need from your room, then you may settle on my sofa.

    Between us, I doubt anyone will find us easy prey.
    """

    """
    It is not an arrangement with which I feel entirely at ease.

    Yet I feel a little less exposed than before at least.

    I return briefly to my own room to gather my things, then I join Sushil Sinha in his.
    """

    $ change_room("bedroom_captain", dissolve)
    
    captain """
    Well, it is rather late, so I suppose we had best settle for sleep.

    You can take the sofa, or if you find it too uncomfortable, there is space enough in the bed.

    I have slept in worse conditions, so I do not mind.
    """

    doctor """
    The sofa will do very well, thank you.

    I doubt I shall sleep much in any case.
    """

    """
    There is no point in attempting anything further tonight.

    So we bid each other good night and resign ourselves to hope for the best.

    Before closing my eyes, I see Sushil Sinha place a revolver upon his bedside table.

    The sight troubles me as much as it makes me feel safer.
    """

    call doctor_day2_evening_captain_sleep_options

    $ doctor_details.threads.unlock("trust_captain")

    return


label doctor_day2_evening_captain_sleep_options:

    if doctor_details.threads.is_unlocked('book_opium'):

        """
        Now that I have settled, the cravings grow stronger than ever.

        I toss and turn upon the sofa, praying for the light of day.

        After what feels like an eternity, I finally fall asleep.
        """

    else:

        """
        Now that I am alone with my thoughts, every possible scenario runs through my mind.

        I feel certain I shall never fall asleep, yet at some point I do.
        """

    return


label doctor_day2_evening_captain_sleep_no:

    doctor """
    I am grateful for your concern, Captain, but I would rather not impose upon you.

    I shall manage well enough in my own room.
    """

    captain """
    As you wish.

    I cannot compel you.

    But at least lock your door.

    I would rather not discover we have misjudged the danger come morning.
    """

    """
    I nod, though my resolve feels far less steady than I should like.

    If I insist upon facing the night alone, I must be ready for whatever it may bring.
    """

    jump doctor_day2_evening_sleep_alone