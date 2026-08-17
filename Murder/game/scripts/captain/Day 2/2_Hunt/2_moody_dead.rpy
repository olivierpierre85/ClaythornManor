# --------------------------------------------
#   Captain - Saturday Hunt - V1 (Moody dead)
#
#   Grouping:
#       - Captain + Lady Claythorn + butler     (north field)
#       - Doctor + Drunk + Lad + footman        (western grove)
#
#   Branches at luncheon on both host suspicions:
#       - Confront Lady -> butler returns, strangulation ending
#       - Hold tongue   -> hunt resumes, distant shots, doctor found dead, survive
#
#   Shared with the host's storyline (_common/Day 2/2_Hunt):
#       - common_day2_hunt_luncheon_served
#       - common_day2_hunt_shots_heard
#       - common_day2_hunt_doctor_aftermath
# --------------------------------------------

label captain_day2_hunt_moody_dead:

    """
    The butler, who has been listening with the unobtrusive attention of his trade, steps forward.
    """

    butler """
    If I may, my lady.

    Doctor Baldwin and Mr Manning to the western grove, with Mr Harring.

    The footman will go along with them.

    My lady and Captain Sinha to the north field, and I shall attend.
    """

    """
    Good, a morning in our hostess's company is definitely the better outcome for me.
    """

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        Whatever she conceals, a few hours alone may loosen her tongue.
        """

    call change_time(11, 45)

    $ change_room('forest_edge')

    """
    We walk for some time through the undergrowth before coming across anything worth a shot.

    Lady Claythorn carries her piece as though it were a parasol that had grown unaccountably heavy.

    Twice the barrel has dipped toward the earth. Once she has shifted her grip in plain sight, as if she could not recall where her hands belonged.
    """


    """
    A pheasant breaks cover. She brings the rifle up late, the stock set too high against her shoulder.
    """

    play sound gun

    pause 1.0


    """
    The shot goes wide by a great margin. The recoil jolts her visibly, and she winces before she thinks to hide it.

    She laughs it off with a small, embarrassed shake of the head.
    """

    host """
    The light is most unhelpful today.
    """

    """
    The light is perfectly fine.

    She has scarcely handled a rifle in her life. That much is plain.

    A gentlewoman who has organised a hunting weekend on her own grounds ought to know one end of her gun from the other.
    """

    $ host_details.description_hidden.unlock('hunt')

    """
    A rabbit bolts from the fern.

    I raise, aim, and fire.
    """

    play sound gun

    pause 1.0

    """
    A clean miss, though not by much.

    I lower the rifle and allow myself a small, private smile.
    """

    host """
    Captain, that was a nice attempt.

    I am sure you will have better luck next time.
    """

    captain """
    You are too kind, my lady.

    I suppose you were right about the light.
    """

    """
    Well, if I must keep my cover, I might as well go along with her lies.
    """

    pause 1.0

    """
    Nothing else comes our way, and soon it is time to stop for luncheon.
    """

    call change_time(12, 30)

    $ change_room('forest_clearing', dissolve)

    call common_day2_hunt_luncheon_served

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        Finally, we are alone.

        The moment I was hoping for.

        A rifle across my knees. The butler away.

        It may not come again.

        I feel like I have seen enough to know "Lady Claythorn" is not who she appears to be.

        And yet, I will have to suppress everything in my education if I want to tell her that.
        
        It does not help that she has a loaded weapon beside her.

        Confronting her now might not be the wisest course of action.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("captain_day2_hunt_menu_confront", [
                TimedMenuChoice("Press her on who she really is", 'captain_day2_hunt_confront_host', early_exit=True),
                TimedMenuChoice("Hold my tongue, for now", 'captain_day2_hunt_silent_luncheon', early_exit=True),
            ])
        )

    else:

        """
        A moment alone with her. 
        
        I could use it to press her on the unusual things I noticed.

        But everything in me prevents me from doing so.

        My suspicions are clearly not strong enough to make me risk angering our hostess.

        It would be improper, but that is not the only reason.

        I may not like it, but I am also afraid of losing the money that was promised to me.

        No, I need more evidence if I want to risk it all by confronting her.
        """

        call captain_day2_hunt_silent_luncheon

    return


# --------------------------------------------
#   Silent luncheon - Captain keeps his peace
#   Leads to the drunk's death in the other party
# --------------------------------------------
label captain_day2_hunt_silent_luncheon:

    """
    I hold my peace.

    We finish the luncheon with the sort of polite small talk that reveals nothing and obliges nothing.
    """

    call change_time(13, 30)

    $ change_room('forest_edge', dissolve)

    call common_day2_hunt_shots_heard

    call common_day2_hunt_doctor_aftermath

    return


# --------------------------------------------
#   Confrontation - Captain presses Lady Claythorn
#   Butler returns in the middle of it -> strangulation ending
# --------------------------------------------
label captain_day2_hunt_confront_host:

    $ play_music('mysterious', 3, fadeout_val=4)

    """
    I set down my cup with deliberate care and allow the rifle to rest within easier reach.
    """

    captain """
    Lady Claythorn. Forgive the indelicacy.

    There is a matter I should like to put to you plainly.
    """

    host """
    Goodness, Captain, how grave you sound.

    Whatever can be the matter?
    """

    captain """
    I noticed a lot of things that do not make sense this weekend:

    Your portrait is nowhere in the gallery.

    You either do not know, or do not follow, proper dining etiquette.

    The hunt you yourself arranged appears to be quite beyond your skill.

    And, worst of all, the surname you are using is not your title, as it should be.

    I do not believe you are Lady Claythorn.

    In fact, I do not think there is a "Lady Claythorn."
    """

    """
    Her smile holds.

    Firmly, as a practised hostess will hold a smile through a guest's poor taste.
    """

    host """
    Captain, I confess myself astonished.

    The morning sun has plainly done your head a mischief.

    You are clearly confusing yourself with some detective from a poorly written novel.

    There is a perfectly good explanation for everything you have mentioned.
    """

    captain """
    Well, in that case, please enlighten me.
    """

    host """
    Shall we take them in turn, Captain?

    As for my portrait, I have never cared to sit for one.

    Its absence in the gallery is my own doing, nothing more sinister than vanity in reverse.

    For my manners at table, I live here for the most part alone.

    When one dines without company for months on end, the old conventions grow dusty.

    And for the hunt, I arranged it for the pleasure of my guests, not my own.

    I take up a rifle perhaps once a year.

    The light was unkind to me this morning, but I confess that even in fair weather I should be no credit to my name.

    Now, for the name itself, my late husband had grown weary of ceremony, as so many did after the war.

    He preferred that we be addressed by the house rather than the peerage.

    A small indulgence, perhaps. Hardly a conspiracy.
    """

    """
    Each answer, taken on its own, is perfectly plausible.

    Worse than that. Each echoes the very explanations I myself had turned over in my mind when I first noticed these things.

    But the answers come too readily, as if rehearsed.

    An honest woman would stumble. Take offence. Demand to know what on earth I meant by it all.

    Instead, she has submitted to my interrogation as if she were expecting it.

    But let's see how well she is really prepared.
    """

    captain """
    That is a very logical explanation for everything.

    But in that case, what is your title?

    If you are right, you cannot have forgotten it.
    """

    """
    There, she hesitates.
    """

    host """
    My memory, I am afraid, is not what it once was.
    """

    captain """
    Surely, my Lady would know her title.

    There is no doubt your father has repeated it constantly as you were growing up.

    You should have heard it said by friends, by visitors, in letters addressed to you.

    You must have heard it when you were presented at court.
    """

    """
    Her chin lifts a fraction, and the practised warmth drains from her voice.
    """

    host """
    Captain, this has gone quite far enough.

    I have indulged your questions out of regard for a guest, and you have repaid me with insolence.

    I am not in the habit of reciting my lineage to satisfy a stranger's curiosity.

    One more word on the subject, and you may pack your things this very afternoon.
    """

    # """
    # There it is at last. The offence. The wounded dignity. The threat.

    # Everything an honest woman would have produced at my first question, arriving only now, at the very last.

    # Like an actress given her cue a scene too late.
    # """

    captain """
    Send me away if you wish, madam. It will change nothing.

    You see, I am not asking you a question I cannot answer myself.

    There is a book in your own library. A registry of the great families of this county.

    It records the peerage your family holds, and the name of that peerage is not Claythorn.

    The true mistress of this house would have carried it her whole life.

    Name it, madam, and I shall offer you my fullest apology and never speak of this again.
    """

    """
    She does not name it.

    She sits very still, her hands folded in her lap, and for a long moment the only sound is the wind working through the trees.
    """

    captain """
    It is the Earldom of Kilbraith.

    The woman you claim to be would be styled Lady Kilbraith.

    You have been answering to the name of a building, madam.

    A stranger to this county learnt that in an evening, from a shelf in your own library.
    """

    """
    She remains silent.
    """

    captain """
    A man died under this roof last night.

    The doctor speaks of a tired heart, and perhaps he is correct.

    But a death must be reported all the same, and the police will come to this house.

    When they do, I shall lay before them everything I have laid before you.

    A lady with nothing to hide loses nothing by it.

    A woman who is not what she claims, on the very weekend a guest dies in his bed, will find their questions far less courteous than mine.

    I leave it to you to decide which of the two receives them.
    """

    """
    I watch the arithmetic move behind her eyes.

    Then her smile fades by degrees, and something tired and older takes its place beneath it.
    """

    host """
    Very well, Captain.

    You are right.

    I am not Lady Claythorn.

    I am just playing the part.
    """

    captain """
    But why? What is the purpose of this?
    """

    host """
    That, I do not know.

    I was hired for a role, an unconventional one I admit.

    But all I was told was what to do, not the reason behind it.
    """

    captain """
    Hired? By whom?
    """

    host """
    The arrangement was made through a firm of solicitors in London.

    I never met the person behind this enterprise.

    The pay was generous, so I didn't ask many questions.
    """

    """
    It takes me a while to take everything in.

    That story goes way beyond what I had imagined.
    """

    captain """
    And the letter left in my room last night?
    """

    host """
    What letter?

    I know nothing of any letter, Captain.
    """

    captain """
    And Thomas Moody?

    A man is found dead in his bed, and you carry on as though a guest had spilt his wine.
    """

    host """
    I have no idea what happened to him.

    That was never planned!
    """

    """
    She shifts as she speaks, her weight settling then settling again, as though the ground beneath her would not hold still.
    """

    captain """
    I am sorry to say, madam, but I do not believe you.
    """

    """
    I lift the rifle and level it at her.

    Not aiming, precisely. Simply making it plain that I am the one asking the questions.

    Her eyes widen. She sets her cup down with a slow, careful hand.
    """

    host """
    Captain. Please.
    """

    captain """
    Now, you will explain clearly the terms of the arrangement.

    I want to know everything.
    """

    $ play_music('danger', 2, fadein_val=1)

    """
    She opens her mouth to answer.
    """

    play sound twig

    """
    A twig snaps behind me.
    """

    pause 1.0

    """
    I begin to turn, far too slowly.

    Something draws tight around my throat.

    The rifle is struck cleanly from my hands before I can bring it round.

    A broad forearm crosses my shoulders.

    A thin leather strap crushes against my windpipe.

    I drive an elbow backwards and find nothing but heavy tweed.

    The butler's breath is steady against my ear.
    """

    host """
    Wait.

    There is no need to hurt him.
    """

    butler """
    I am afraid there is.

    I've heard what he said to you.

    He knows too much.
    """

    """
    My vision blurs at the edges.

    I grope for the knife at my belt.

    My fingers will not close upon it.

    A moment more, and the forest folds inward and goes dark.
    """

    $ host_details.description_hidden.unlock('lie')

    jump captain_ending_strangled
