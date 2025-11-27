label doctor_day1_evening_bedroom_drunk_enter:

    $ change_room("bedroom_drunk")

    """
    I step into the room.

    It is a dreadful mess.

    The bottles of whisky, some already emptied, give me a fair idea whose room this is.

    There is no doubt that Samuel Manning sleeps here.
    """
    
    $ unlock_map("bedroom_drunk")

    $ play_music("mysterious")

    """
    I glance around, uncertain what I am hoping to find, when I notice a letter upon the desk.

    I take it up.

    The first part is written in a fine, elegant hand.
    """

    call drunk_letter_first_part

    """
    What on earth does this mean?

    Who could have written such a thing?

    Still, what troubles me most is the second part, barely legible, most likely added later by Samuel Manning himself.
    """

    call drunk_letter_second_part

    $ doctor_details.objects.unlock("drunk_letter")

    """
    My legs feel weak.

    I sit on the edge of the bed, struggling to make sense of it all.

    I try to remember Samuel Manning, but I cannot say for certain that I ever treated his wife.

    That does not mean the charge is false.

    I know I have done similar things to a good many patients. Mrs Manning may well have been among them, and I have simply forgotten.

    One thing is certain though. Someone in this house means me harm.

    And they are trying to use Samuel Manning to hurt me.

    I say they, but it is plain enough who must have written this note.

    Lady Claythorn invited me here. She is the most obvious culprit.

    In that case my invitation here was no kindly whim, but a deliberate act.

    Yet I cannot be sure, for I did not recognise her at all when we were introduced.

    But that, again, may mean very little.

    It could, of course, be an extraordinary coincidence.

    Perhaps some enemy of mine is numbered among the guests, and Lady Claythorn has nothing at all to do with this.

    It is not very likely, yet not impossible.

    What am I to do now.

    The prudent course might be to warn everyone and abandon the whole business.

    But I have no notion how any of them would react to such an announcement.

    That could mean sacrificing the prize money.

    And if this letter were to be spoken of outside these walls, it might cost me my practice as well.

    I cannot afford that.

    Besides, this could yet prove no more than a cruel jest, or some wretched misunderstanding.

    If I remain, nothing more may come of it.

    I need only be on my guard, and watch Samuel Manning closely.

    I must decide.

    Do I risk my life, or do I risk losing the kind of money that would set me up comfortably for years to come.
    """

    call run_menu( 
        TimedMenu("doctor_day1_evening_bedroom_drunk_enter", [
            TimedMenuChoice("Do not risk your life — leave this place", "doctor_day1_evening_bedroom_drunk_leave_manor", 20, early_exit=True, next_menu="doctor_day1_evening_bedroom_drunk_leave_manor"),
            TimedMenuChoice("Do not risk losing the money — stay", "doctor_day1_evening_bedroom_drunk_stay", early_exit=True),
        ])
    )

    return


label doctor_day1_evening_bedroom_drunk_leave_manor:

    """
    Why am I even considering staying here?

    I should leave at once and warn the others.

    I believe they are all gathered in the billiard room.

    If Lady Claythorn truly is behind this, I would rather face her with witnesses than wait alone for whatever she has planned.
    """

    $ change_room("billiard_room") 
    
    """
    I find most of them assembled around Captain Sinha.

    I interrupt him.
    """

    doctor """
    Pardon me, Captain, but I have something you should see.
    """

    """
    I hand him the letter.

    He reads it aloud to the assembled company.
    """

    captain """
    What is the meaning of this?

    Where did you find it?
    """

    doctor """
    In Samuel Manning's room.
    """

    captain """
    Really? And what were you doing there?
    """

    doctor """
    The door was open, and I was—
    """

    drunk """
    Wait, you went into my room?

    What gave you the right to do such a thing?
    """

    doctor """
    That is not the issue. How do you explain this letter?
    """

    drunk """
    I have never seen it before.

    It isn't mine.
    """

    doctor """
    Truly? And we are supposed to take you at your word?
    """

    drunk """
    I don't see why anyone should believe you either.

    A man who thinks it proper to barge into another's room.

    Unless, of course, you did not enter it at all, and wrote this yourself.
    """

    doctor """
    Why on earth would I do that? It makes no sense.
    """

    drunk """
    No less sense than what you're implying, Doctor.

    Do you truly expect anyone here to believe you?
    """

    """
    I glance around the room. All eyes are upon us.

    The others look perplexed, unsure what to make of the exchange.

    Silence lingers until Captain Sinha finally speaks.
    """

    captain """
    There is something amiss here, though I cannot tell who is at fault.
    """

    doctor """
    Surely it cannot be me. Just look at Samuel Manning.

    Is he even sober enough to make sense?
    """

    drunk """
    What makes you say I am drunk?

    I can gather my wits when the occasion calls for it.
    """

    captain """
    Enough, both of you.

    I do not understand any of this. We should think it over with cooler heads.

    Lady Claythorn, what do you make of it?
    """

    """
    Our hostess is visibly shaken, yet manages to reply.

    I watch her closely.

    If she wrote the first part of that letter, then this is her handiwork laid bare before everyone.

    Yet I cannot tell whether her distress is genuine horror or a performance.
    """

    host """
    I, I don't know.

    I'm not certain whom to believe.

    What do you suggest, Captain?
    """

    captain """
    We shan't settle this now. It requires thought.

    I propose we confine the two of you to your rooms until we reach a conclusion.
    """

    doctor """
    What? No.

    I must leave this place at once. I am not safe here.
    """

    captain """
    It's far too late to leave now. The storm makes travel dangerous.

    You'll be safer in your room.
    """

    #TODO: Add thunder sound, and notice on it?
    # Just after saying that, a loud thunder erupts in the night. (replace I ponder that for a moment)

    """
    I ponder that for a moment. The storm is raging outside, leaving now would be perilous.

    Yet staying in my room hardly feels safer, not with Samuel Manning and perhaps Lady Claythorn herself set against me.

    The others watch me uneasily. I can tell they do not quite believe me.
    """

    doctor """
    Very well, I'll go to my room.

    But I want your word that I will be allowed to leave at first light.

    I do not wish to remain here a moment longer than necessary.
    """

    captain """
    You have my word, Doctor.

    And you, Mr Manning?
    """

    drunk """
    All right, I'll go to my room as well.

    It's late enough.
    """

    captain """
    Then it's settled. Please, follow me, Doctor Baldwin.
    """

    """
    Captain Sinha escorts me to my room.

    The butler and Lady Claythorn accompany Samuel Manning to his.

    I am far from reassured, yet see no alternative.

    I enter my room as the Captain remain outside.
    """

    $ change_room("bedroom_doctor")

    captain """
    My apologies, Doctor Baldwin. I am sure we shall sort this out soon enough.

    In the meantime, we shall have to lock you in.
    """

    """
    Before he can close the door, I lower my voice.
    """

    doctor """
    Captain, between ourselves, you must see what this implies.

    Lady Claythorn invited us both here.

    She is in all likelihood the one who wrote that letter to Samuel Manning.

    Which means something dangerous may be at play here.
    """

    """
    He hesitates, then answers just as quietly.
    """

    captain """
    I cannot deny the thought has crossed my mind.

    But from my point of view, I have only an anonymous letter that you say you found in rather singular circumstances.

    I cannot possibly accuse our hostess openly on that alone.
    """

    doctor """
    I understand your position, but please keep it in mind, and be careful.
    """

    captain """
    You have my word.
    """

    """
    He leaves me alone, so I lock my door and do what I can to secure it.
    """

    play sound door_locked

    """
    I have no intention of sitting idly by, so I barricade the door in case Manning, or even Lady Claythorn herself, decides to pay a visit.
    """

    play sound moving_furniture

    """
    Now all I can do is wait.
    """
    
    call wait_screen_transition()

    call change_time(23,30)

    """
    After what feels like hours, someone knocks at my door.
    """

    play sound door_knock

    captain """
    Doctor Baldwin, after some discussion, we have decided you may be right in one respect.

    There is too much here that does not add up.

    We shall all leave in the morning.

    For the time being, we shall all rest easier if you and Mister Manning stay in your rooms for the night.

    I did not dare accused Lady Claythorn directly, but I will also keep an eye her.
    """

    """
    Good, he has not dismissed my suspicions entirely.
    """

    doctor """
    Very well. I have barricaded myself anyway.
    """

    captain """
    A wise precaution, Doctor. Again, my apologies.
    """

    doctor """
    Of course, I understand, Captain. Good night.
    """

    captain """
    Good night, Doctor.
    """

    """
    At least this dreadful business will soon be over.

    What am I to do now? 
    
    I do not think I could sleep in this state.

    And perhaps it is better to stay alert.

    But on the other hand, I think I am protected enough here.
    """

    call run_menu( 
        TimedMenu("doctor_day1_evening_bedroom_drunk_leave_manor", [
            TimedMenuChoice("I know something that will help me sleep", "doctor_day1_evening_bedroom_drunk_leave_manor_sleep", early_exit=True),
            TimedMenuChoice("I should stay awake to be safe", "doctor_day1_evening_bedroom_drunk_leave_manor_awake", early_exit=True),
        ])
    )

    return


label doctor_day1_evening_bedroom_drunk_leave_manor_sleep:

    """
    I am far too tense.

    Despite the risk, I cannot resist the urge to calm my nerves.
    """

    jump doctor_laudanum_death



label doctor_day1_evening_bedroom_drunk_leave_manor_awake:

    """
    I lie on my bed, not expecting to close my eyes before morning.

    Nevertheless, after a few hours, I doze off, utterly exhausted.
    """

    call wait_screen_transition()

    play sound fire loop

    """
    I am awakened by a strange noise.

    What is that?

    I realise I cannot breathe.
    """

    play sound woman_cough

    """
    Smoke.

    Something is burning.

    I spring to my feet.

    The walls of the room are ablaze.

    Smoke fills the air, I can scarcely see a thing.

    I rush towards the door, but the furniture I placed against it blocks my way.

    I summon all my strength to move it, yet I have no energy left.

    My head spins.

    I...
    """

    play sound body_fall

    jump doctor_ending_burn



label doctor_day1_evening_bedroom_drunk_stay:

    """
    I do not believe I am in any great danger.

    I shall stay, though I must be cautious from now on.

    Especially around Samuel Manning.

    And I should try to discover who could have written this wretched letter.
    """

    # $ doctor_details.objects.unlock("drunk_letter")

    $ play_music("PREVIOUS")

    return
