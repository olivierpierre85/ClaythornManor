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

    $ change_room('forest')

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

    $ captain_details.threads.unlock('captain_host_suspicion_shooting')


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

    """
    The butler lays out a modest spread on a linen cloth, pours tea, then steps back with a brief bow.
    """

    butler """
    If you don't mind, my lady. I should like to look in upon the other party, that they might not want for anything.

    I shall be back soon.
    """

    host """
    Very well. Thank you.
    """

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

    """
    In due course the butler returns, composed as ever, and we resume the hunt.
    """

    pause 1.0

    play sound gun

    pause 0.5

    """
    Two shots, close together, from the direction of the western grove.

    Lady Claythorn lifts her head.
    """

    host """
    It seems the others have had better fortune than ourselves.
    """

    """
    Then, a moment later, a different sound.

    A cry. Thin and urgent, carried between the trees.
    """

    $ play_music('danger', 2)

    host """
    Captain. With me, please.
    """

    """
    She is the first to move.

    For a woman who cannot shoot, she has a commanding stride when it suits her.
    """

    call wait_screen_transition()

    """
    When we reach the others, Doctor Baldwin lies on his back in the fern.

    His shirt has been torn open and pressed dark with blood. His bag is open at his side, a pair of emptied vials loose in the moss.

    Mr Harring kneels beside him, white as paper, a useless hand resting on the ruined shirt.

    Samuel Manning stands a few paces off, his rifle at his feet, his whole frame trembling.

    The footman hovers uncertainly, having clearly not known where to place himself.
    """

    drunk """
    A rabbit. It was a rabbit.

    I never saw him. I swear it on my life, I never saw him.
    """

    footman """
    Mr Manning fired at something in the undergrowth, my lady.

    The doctor was ahead of him, and the bracken was thick between them.

    The bullet took him in the side.
    """

    """
    The doctor's face has already settled into the stillness of the dead.

    A liver shot, from the placement of the blood. Quick enough, though not quickly enough for comfort.
    """

    butler """
    A dreadful business, my lady.

    If you will permit me, we ought to return to the house and send for the proper authorities.
    """

    host """
    Yes. Yes, of course.

    Poor Doctor Baldwin. What a terrible, terrible accident.
    """

    $ stop_music(2)

    """
    Two men dead in the same day.

    And our hostess receives the second with the same well-rehearsed composure as the first.

    I shall have a great deal to think about tonight.
    """

    pause 2.0

    return


# --------------------------------------------
#   Confrontation - Captain presses Lady Claythorn
#   Butler returns in the middle of it -> strangulation ending
# --------------------------------------------
label captain_day2_hunt_confront_host:

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
    I notice a lot of things that do not make sense this weekend:

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

    Instead, she has submitted to my interrogation as if she were prepared for it.

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

    $ play_music('danger', 2, fadeout_val=4)

    """
    She prepares to answer, but cannot find the words.

    Finally, her smile fades by degrees, and something tired and older takes its place beneath it.
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

    It leads to even more questions.
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

    Not aiming, precisely. Simply making it plain that, at this small clearing, I am the one asking the questions.

    Her eyes widen. She sets her cup down with a slow, careful hand.
    """

    host """
    Captain. Please.
    """

    captain """
    Now, you will explain clearly the terms of the arrangement.

    I want to know everything.
    """

    """
    She opens her mouth to answer.

    A twig snaps behind me.
    """

    $ stop_music(1)

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

    jump captain_ending_strangled
