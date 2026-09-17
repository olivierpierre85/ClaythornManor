# --------------------------------------------
#   Drunk
#
#   Saturday - Evening
#
#   15:00 -> 23:30
#
#   Music: sad for the return, mysterious for the room, danger for the night
#
#   Position
#       - House    : host, captain, lad, psychic, nurse, butler
#       - Confined : drunk, locked in his room
#       - Dead     : broken (Thomas Moody), doctor (Daniel Baldwin)
#
#   Notes :
#       - Only reached through the hunt fire path (shot_doctor). He is
#         carried home a killer, accused, and locked in the George IV room
#         with the butler's key on the outside.
#       - The whole chapter is one room and one long think. The generic
#         self-talk menu (drunk_day2_evening_menu_think) is his gift: sober,
#         behind a locked door, he takes the weekend apart. Three topics
#         make the picture whole (the letter, the telephone call, the
#         butler), and once he has them the 'understood' thread unlocks and
#         the two ways out appear.
#       - Three endings hang off the night:
#           * accept it and drink -> he cuts his own throat (throat_cut)
#           * confront the house  -> nobody believes a drunk (silenced)
#           * play dead with port  -> Sunday (played_dead), needs the port
#
#   Unlocks : drunk 'understood', 'phone_call', 'butler_face', 'played_dead'
# --------------------------------------------
label drunk_day2_evening:

    call change_time(15, 00, 'Evening', 'Saturday', hide_minutes=True, chapter='saturday_evening')

    $ drunk_details.add_checkpoint("drunk_day2_evening")

    call black_screen_transition("Samuel Manning", chapters_names[current_chapter])

    $ drunk_mode = False

    $ change_room('entrance_hall', irisout)

    $ play_music('sad', 2)

    """
    The hall, and the whole house waiting in it, and me coming through the door with a dead man's bag.

    They have made up their minds before I am over the threshold. I can see it. I have watched a hundred juries do it, and it always looks the same.
    """

    call drunk_day2_evening_accusation

    call drunk_day2_evening_telephone

    call drunk_day2_evening_confined

    # ------------------------------------
    #   The room. The long think.
    # ------------------------------------
    $ change_room('bedroom_drunk', dissolve)

    $ play_music('mysterious', 2)

    play sound door_locked

    """
    The key turns on the far side, and the Captain's footsteps go away down the corridor, and I am alone.

    Locked in.

    It is the best thing that has happened to me all weekend.

    No one will knock. No one will watch. No one will offer me a drink, or take one away, or wonder why a barrister is sitting in the dark not touching the bottle on the washstand.

    For the first time since Carlisle I have nothing to do and nobody to do it in front of.

    So I sit in the one chair, and I do the thing I used to be paid for.

    I think.
    """

    call drunk_day2_evening_think_loop

    # ------------------------------------
    #   The choice. What a man does with a locked door.
    # ------------------------------------
    call change_time(23, 30)

    $ play_music('danger', 3)

    """
    The house has gone quiet below me.

    A door, once, and feet on a stair, and then nothing.

    Here is where I am, then. A locked door, a bed, and a bottle of the house's whisky on the washstand.
    """

    if drunk_details.threads.is_unlocked('understood'):

        """
        And behind my eyes, at last, the whole shape of it.

        There is a killer in this house, and I know it, and I know I am on the list, because a man does not write a letter like the one I burned to somebody he means to spare.

        Two men dead in two days, and both of them accidents, and the whole house nodding along.

        I am the third.
        """

    else:

        """
        And a headache where the thinking should be.

        Something is wrong in this house. I have felt it since the woods, since before the woods. But I could not tell you what, and I am too tired to chase it now.
        """

    """
    A locked door is nothing to whoever has been walking this house at night. It did not save Thomas Moody. It will not save me.

    What does a man do with a night like this.
    """

    $ time_left = 1
    call run_menu(TimedMenu("drunk_day2_evening_menu_choice", [
        TimedMenuChoice('Play dead. Port for blood, a razor for the edge', 'drunk_day2_evening_play_dead', early_exit=True, condition="drunk_details.threads.is_unlocked('understood') and drunk_details.objects.is_unlocked('port')"),
        TimedMenuChoice('Hammer on the door and warn the whole house', 'drunk_day2_evening_confront', early_exit=True, condition="drunk_details.threads.is_unlocked('understood')"),
        TimedMenuChoice('Accept it, and drink', 'drunk_day2_evening_drink', early_exit=True),
    ]))

    return


# ------------------------------------
#   The accusation in the hall
# ------------------------------------
label drunk_day2_evening_accusation:

    psychic surprised """
    Good heavens! What happened!?

    Is that Doctor Baldwin? Is he injured?

    Oh no! Is he... dead?
    """

    captain """
    I'm sorry, dear, but he is.

    Samuel Manning missed his target and hit Doctor Baldwin instead.
    """

    """
    Missed my target.

    That is the kindest description anybody has given of my work in five years, and it is a lie, and I let it stand.
    """

    drunk sad """
    It was an accident, I swear.

    I was aiming at a rabbit. I never saw him.
    """

    psychic angry """
    You fool! You were probably too drunk, and that's why you hit him.

    You could barely walk this morning. Who gave you a gun?
    """

    """
    Too drunk.

    I let my mouth hang, and my eyes swim, and I give her exactly the man she has described. It is not difficult. I have played him for years, and today, of all days, I am not even playing.

    Let them have the drunk who could not help it.

    A drunk who could not help it hangs. A man who took aim through the bracken and squeezed does something a great deal worse than hang.

    Better the drunk.
    """

    captain """
    Please, there's no need to point fingers now. It's done.

    The police will handle it.

    Lady Claythorn, where's the telephone?
    """

    host """
    I'll handle it.
    """

    return


# ------------------------------------
#   The telephone call, watched
# ------------------------------------
label drunk_day2_evening_telephone:

    """
    She goes to the back of the hall, where the telephone stands on its table under the stair, and the butler goes with her.

    Everybody else looks at me, so I look at the floor, which is what they expect of me.

    But a man looking at the floor can still hear.

    And I have taken a great many statements in my time. I know the shape of a real telephone call to the police, and I know the shape of a performance of one, and I file the difference away without quite knowing yet why it matters.
    """

    host """
    I just spoke with the police. They aren't coming today.
    """

    call common_day2_evening_police_tree_explanation

    """
    A tree across the road.

    On a night with no storm.
    """

    return


# ------------------------------------
#   Confined. The Captain walks him up.
# ------------------------------------
label drunk_day2_evening_confined:

    """
    They talk about me as though I have already gone.

    The thin woman thinks I might do somebody harm. The hat thinks I might run. The butler says the sensible thing, in the sensible voice, and it is always the butler who says the sensible thing.

    Lock him in his room.
    """

    call change_time(16, 00)

    $ change_room('bedrooms_hallway', dissolve)

    captain """
    I hope you understand we're left with little choice.

    You have to retire to your room. The door will be locked from the outside.

    Is that clear?
    """

    drunk """
    Yes, of course.

    I understand.
    """

    """
    He is not unkind about it, the straight man. He walks me up himself, with the butler's key in his hand, and at my door he pauses as though he means to say something and cannot find it.

    A decent man. The only one in the house, I think.

    That is his misfortune. Decent men open doors they should leave shut.
    """

    return


# ------------------------------------
#   The think loop
# ------------------------------------
label drunk_day2_evening_think_loop:

    call change_time(21, 00)

    $ current_character.saved_variables["day2_evening_think_menu"].early_exit = False

    $ time_left = TIME_MAX
    call run_menu(current_character.saved_variables["day2_evening_think_menu"])

    call drunk_day2_evening_think_conclusion

    return


# The three topics that make the picture whole are the letter, the telephone
# call and the butler. Think through all three and 'understood' unlocks.
label drunk_day2_evening_think_conclusion:

    python:
        _topics = drunk_details.saved_variables["day2_evening_topics"]
        _key = {"letter", "telephone", "butler"}
        _has_all = _key.issubset(set(_topics))

    if _has_all and not drunk_details.threads.is_unlocked('understood'):

        $ drunk_details.threads.unlock('understood')

        """
        And there it is.

        I have put a great many cases together in my time, badly, and this is the first one in years I have put together sober, and it is the plainest I have ever seen.

        A letter, in a woman's hand, naming a man and handing me the means. A house with no telephone and a hostess who can act. A butler with a fighter's knuckles and a fighter's face, running it all in the sensible voice.

        Somebody gathered us here. Somebody who knew about Eleanor, and about the doctor, and about whatever the mask had done, and whatever the straight man had done, and set us against one another like dogs and stood back to watch.

        And I did exactly what I was brought here to do.

        I am not the next to die by accident. I am the next to die because I have served my purpose, and a man who has served his purpose is tidied away.

        Unless he is already dead.
        """

    return


# ------------------------------------
#   The topics
# ------------------------------------
label drunk_day2_evening_think_letter:

    $ drunk_details.saved_variables["day2_evening_topics"].append("letter")

    """
    The letter first.

    A fine hand. A woman's, or a clerk's taught by one. And angry, in a way that has had years to go cold, which is the most dangerous kind.

    Whoever wrote it knew about Eleanor. Not the fact of a dead wife, which anybody might dig up, but her name, and that I blamed a doctor for it, and that the doctor took the medicine for himself.

    That is not gossip. That is somebody who went through my life with a lamp.

    And they did the same to the doctor, to put him at my table. And to the mask, and the straight man, I would wager, and all the rest.

    We were not invited. We were assembled.
    """

    return


label drunk_day2_evening_think_moody:

    """
    The mask. Thomas Moody.

    Dead in his bed on the first night, of an old war wound that chose its moment.

    He drank from his own flask and would not touch the house's wine. I noticed it at dinner and thought him rude.

    A man who will not drink what he is given, dead by morning.

    I have been drinking what I am given all my life. It is a wonder I have lasted this long.
    """

    return


label drunk_day2_evening_think_telephone:

    $ drunk_details.saved_variables["day2_evening_topics"].append("telephone")

    if not drunk_details.observations.is_unlocked('phone_call'):
        $ drunk_details.observations.unlock('phone_call')

    """
    The telephone call.

    I stood in that hall and heard her make it, and there was something wrong with it, and now I have the quiet to find out what.

    She asked no questions.

    A woman telephoning the police to report two dead men in her own house asks questions. When can you come. What should we do until then. Should we touch nothing.

    She gave a little speech and put the receiver down. There was nobody on the other end of it.

    The line is dead, or there is no line, and there never was going to be a policeman up that road.

    We are ten miles from the town, and nobody is coming, and everybody in this house but me thinks help is on its way.
    """

    return


label drunk_day2_evening_think_butler:

    $ drunk_details.saved_variables["day2_evening_topics"].append("butler")

    if not drunk_details.observations.is_unlocked('butler_face'):
        $ drunk_details.observations.unlock('butler_face')

    """
    The butler.

    I have been trying to place his face since the tea room, and behind a locked door, with nothing else to do, I place it.

    I have seen that man in a dock.

    Years ago, in the north, before the drink took the best of my practice. A big man with a broken face, up for something with his fists in it, and got off, because the man who was supposed to speak against him did not turn up.

    He is no more a butler than I am a barrister any more.

    He serves from the left and holds the platter at the right height because somebody taught him the part, the way somebody taught her ladyship hers.

    He is running this house. She only presides over it. And whatever is being done in it is being done by him, in the sensible voice, with the sensible key.
    """

    return


label drunk_day2_evening_think_psychic:

    """
    The hat. Miss Baxter.

    She counts the boy's fingers when she looks at him, the way Eleanor counted other people's children.

    A woman who wanted one and did not get one, or got one and lost it. I have sat across a table from a hundred of them and I know the look.

    Whatever she is doing here, it is about that boy, and not about any of the rest of us.

    There is a whole other story in this house, running under mine, and I am not in it. That is almost a comfort.
    """

    return


label drunk_day2_evening_think_self:

    """
    And why me.

    A defence barrister who lost more than he won, and drank the difference. There is no shortage of men I have failed. Any one of them might hate me enough for this.

    But the letter was not about a client. It was about Eleanor, and the doctor, which means whoever wrote it does not want me punished for my failures.

    They want me used.

    I was brought here to point at Daniel Baldwin, and I did, and I shot him for them, and now I am no more use to anybody than a spent match.

    That is the answer, and I do not much care for it.
    """

    return
