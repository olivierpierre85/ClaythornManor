# --------------------------------------------
#   Captain - Saturday Hunt - V1 (Moody dead)
#
#   Grouping:
#       - Captain + Lady Claythorn + butler     (north field)
#       - Doctor + Drunk + Lad + footman        (western copse)
#
#   Branches at luncheon on both host suspicions:
#       - Confront Lady -> butler returns, strangulation ending
#       - Hold tongue   -> hunt resumes, distant shots, drunk found dead, survive
# --------------------------------------------

label captain_day2_hunt_moody_dead:

    butler """
    If it please my lady, the arrangement might run thus.

    Doctor Baldwin and Mr Manning to the western copse, with Mr Harring in their company.

    A footman shall accompany them.

    My lady and Captain Sinha to the north field, with myself to assist.
    """

    host """
    An admirable arrangement, Hargreaves.

    Captain, I trust the company shall not disappoint.
    """

    captain """
    On the contrary, my lady. I consider it a privilege.
    """

    """
    The arrangement suits me very well indeed.

    A morning in our hostess's company is precisely what I had hoped for.

    Whatever she conceals, a few hours alone may loosen her tongue.
    """

    call change_time(11, 45)

    $ change_room('forest')

    """
    We walk for some time through the undergrowth before coming across anything worth a shot.

    Lady Claythorn carries her piece with the easy confidence of a woman who wishes to appear practised.

    The bearing is correct. The eye is not.
    """

    play sound gun

    pause 1.0

    """
    Her first shot, at a pheasant breaking cover, goes wide by several yards.

    She laughs it off with a small, embarrassed shake of the head.
    """

    host """
    The light is most unhelpful today.
    """

    """
    The light is perfectly fine.

    She is simply a poor shot.

    I had thought I would have trouble keeping pace with her.

    Instead, she is worse than I am, and I am hardly impressive.

    A gentlewoman who has organised a hunting weekend on her own grounds ought to carry herself better than this.
    """

    $ captain_details.observations.unlock('captain_host_suspicion_shooting')

    play sound gun

    pause 1.0

    """
    A rabbit bolts from the fern. I raise, aim, and fire.

    A clean miss, though not by much.

    I lower the rifle and allow myself a small, private smile.

    Just as well. It would not do to outshine the hostess on her own ground.
    """

    host """
    Captain, that was a splendid attempt.

    The beast turned at quite the wrong moment.
    """

    """
    The beast did nothing of the sort.

    Her praise is as rehearsed as her manners.
    """

    call change_time(12, 30)

    """
    In due course we stop for luncheon in a small clearing.

    The butler lays out a modest spread on a linen cloth, pours tea, then steps back with a brief bow.
    """

    butler """
    With your leave, my lady. I should like to see how the other party fares.

    I shan't be more than a quarter of an hour.
    """

    host """
    Very well, Hargreaves. Thank you.
    """

    """
    And just like that, we are alone.

    A circumstance I had dared hope for but not expected.
    """

    if captain_details.threads.is_unlocked('captain_host_suspicion_name') and captain_details.threads.is_unlocked('captain_host_suspicion_portrait'):

        """
        She pours a second cup with the same rehearsed grace I have marked since Friday evening.

        A moment alone with her. A rifle across my knees. The butler a quarter-hour away.

        It may never come again.

        And yet confronting a lady with a loaded weapon is not, perhaps, the wisest course for a gentleman.
        """

        $ time_left = 1
        call run_menu(
            TimedMenu("captain_day2_hunt_menu_confront", [
                TimedMenuChoice("Press her on who she really is", 'captain_day2_hunt_confront_host', early_exit=True),
                TimedMenuChoice("Hold my tongue and enjoy the luncheon", 'captain_day2_hunt_silent_luncheon', early_exit=True),
            ])
        )

    else:

        call captain_day2_hunt_silent_luncheon

    jump work_in_progress


# --------------------------------------------
#   Silent luncheon - Captain keeps his peace
#   Leads to the drunk's death in the other party
# --------------------------------------------
label captain_day2_hunt_silent_luncheon:

    """
    I hold my peace.

    Whatever she is, she has a butler at her call and, for all I know, more besides.

    A gentleman chooses his ground with care.

    We finish the luncheon with the sort of polite small talk that reveals nothing and obliges nothing.
    """

    call change_time(13, 30)

    """
    In due course the butler returns, composed as ever, and we resume the hunt.
    """

    play sound gun

    pause 1.0

    play sound gun

    pause 0.5

    """
    Two shots, close together, from the direction of the western copse.

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
    Captain. Hargreaves. With me, please.
    """

    """
    She is the first to move.

    For a woman who cannot shoot, she has a commanding stride when it suits her.
    """

    call wait_screen_transition()

    """
    When we reach the others, Samuel Manning is on his back in the fern.

    His shirt is dark with blood. A rifle lies a few feet from his hand.

    Doctor Baldwin kneels beside him, pale, his own jacket flecked with crimson.

    Mr Harring stands a few paces off, white as paper.

    The footman hovers uncertainly, having clearly not known where to place himself.
    """

    doctor """
    He raised his gun at me.

    Raving about a letter. About his wife.

    I moved to disarm him.

    We struggled, and the weapon discharged.
    """

    """
    The doctor is plainly shaken, yet his account is too neat to be improvised.

    Whether it is true or merely well prepared, I cannot say.
    """

    butler """
    A dreadful business, sir.

    Dreadful.

    If you will permit me, we ought to return to the house and send for the proper authorities.
    """

    host """
    Yes. Yes, of course.

    Poor Mr Manning. What a terrible, terrible accident.
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

    $ play_music('danger', 2, fadeout_val=4)

    """
    I set down my cup with deliberate care and allow the rifle to rest within easier reach.

    Opportunity will not wait upon a man's second thoughts.
    """

    captain """
    Lady Claythorn. Forgive the indelicacy.

    There is a matter I should like to put to you plainly.
    """

    host """
    Goodness, Captain, how grave you sound.

    Has the luncheon offended you?
    """

    captain """
    Your surname is the name of this estate.

    Your portrait is nowhere in the gallery.

    And the hunt you yourself arranged appears to be quite beyond your skill.

    You are not Lady Claythorn.
    """

    """
    Her smile holds for a single heartbeat.

    Then it fades, and something tired and older takes its place.
    """

    host """
    No.

    No, I am not.

    I was hired to play the part.

    An out-of-work actress with a passable voice and the good fortune to look the role.

    That is all I am able to tell you, Captain.
    """

    captain """
    By whom were you hired?
    """

    host """
    That, I genuinely do not know.

    The arrangement was made through a firm of solicitors in London.

    The pay was generous. Questions were discouraged.
    """

    captain """
    And the letter left in my room last night?
    """

    host """
    What letter?

    I know nothing of any letter, Captain.

    On my mother's grave.
    """

    captain """
    And Thomas Moody?

    A man is found dead in his bed, and you carry on as though a guest had spilt his wine.
    """

    host """
    I was told he was frail. That he might not last the weekend.

    I was not told he would not.
    """

    """
    Her answers come too readily.

    Too readily, and yet too little.
    """

    captain """
    With the greatest respect, madam, I do not believe you.
    """

    """
    I lift the rifle and level it across the tea-things at her.

    Not aiming, precisely. Simply making it plain that, at this small clearing, I am the one asking the questions.

    Her eyes widen. She sets her cup down with a slow, careful hand.
    """

    host """
    Captain. Please.
    """

    captain """
    The name of the solicitor.

    The terms of the arrangement.

    Everything you were told about the other guests beneath this roof.
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
    """

    butler """
    Forgive the intrusion, my lady.
    """

    """
    A broad forearm crosses my shoulders.

    A thin leather strap, a rifle sling I think dully, crushes against my windpipe.

    I drive an elbow backwards and find nothing but heavy tweed.

    The butler's breath is steady against my ear.

    He has done this before.
    """

    host """
    Hargreaves, wait.

    Let him speak.
    """

    butler """
    Better he does not, my lady.

    Gentlemen who ask such questions seldom keep the answers to themselves.
    """

    """
    My vision blurs at the edges.

    I grope for the knife at my belt.

    My fingers will not close upon it.

    A moment more, and the forest folds inward and goes dark.
    """

    jump captain_ending_strangled
