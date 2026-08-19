# --------------------------------------------
#   Captain Sinha confronts the hostess in the
#   tea room, before the remaining witnesses.
#
#   Shared by the Captain and the Host.
#
#   The Captain's grievances are deliberately
#   kept vague here, since the two timelines do
#   not unlock the same suspicions. Only the
#   title is named, and the title is the one
#   thing he is certain of in both.
#
#   Doctor, Broken => Dead
#   Drunk taken up by the butler
#   Lad in his room
#   That leaves : Captain, psychic, nurse, host
# --------------------------------------------
label common_day2_evening_captain_confronts_host:

    $ play_music('mysterious', 3, fadeout_val=4)

    if current_character == host_details:

        """
        The Captain does not move towards Mr Manning at all.

        He turns to my butler instead.
        """

    else:

        """
        I turn to the butler.
        """

    captain """
    Would you be so good as to escort Mr Manning to his room and lock the door behind him?

    See to it that he is not allowed out under any circumstance.
    """

    if current_character == host_details:

        """
        The butler's eyes come to me, and he waits.

        There is nothing for it but the small nod the mistress of a house would give, so I give it.

        And with that I have sent away the only man under this roof who knows what I am.
        """

    else:

        """
        He gives a brief glance at Lady Claythorn, who nods her assent.
        """

    butler """
    Of course, Captain.
    """

    if current_character == host_details:

        """
        Mr Manning is taken up by the elbow, and does not resist.

        The Captain waits until their steps have left the stair.

        He has been perfectly courteous the whole weekend, and he is in a hurry now.

        I do not care for that at all.
        """

    else:

        """
        The butler takes Manning by the elbow, and guides him up the stair without a word.

        That should give me a little time, but probably no more than a quarter of an hour.

        I should not waste any of it.
        """

    captain """
    Ladies, I know it is rather unusual, but I would like all of you to follow me into the tea room.

    There is a matter I should put before everyone.
    """

    host """
    Captain, whatever can be the matter?
    """

    captain """
    Please, my lady. It will not take long.
    """

    $ change_room("tea_room", dissolve)

    if current_character == host_details:

        """
        Miss Baxter and Miss Marsh take the small settee.

        I take the wingback chair, because it is the chair the mistress of a house would take, and because I should like something solid behind my back.

        The Captain closes the door and places himself in front of it.

        Three of them, one of me, and the only way out of the room at his shoulder.

        I have played this scene before, on the other side of it.

        Never one I was not at liberty to walk out of.
        """

    else:

        """
        Miss Baxter and Miss Marsh take the small settee.

        Lady Claythorn lowers herself into the wingback chair as though it were a witness box.

        I close the door behind us and place myself between it and our hostess.
        """

    captain """
    Forgive the abruptness. I have my reasons for the haste.

    Throughout this weekend I have observed a number of things that do not sit easily with the position our hostess claims to hold.

    Small things, most of them, and I shall not weary you with the whole of the list.

    But one of them is not small at all.

    The name she goes by is the name of this house. It is not a title.

    I do not believe she is Lady Claythorn.

    In truth, I do not believe there is a Lady Claythorn at all.
    """

    psychic surprised """
    Captain! What an extraordinary thing to say.
    """

    nurse """
    Surely there is some misunderstanding.
    """

    if current_character == host_details:

        """
        They speak up for me, both of them, and for a moment I could kiss them for it.

        Then I look at their faces.

        Neither of them means a word of it.

        They have been keeping count of my mistakes as well. They have simply been better mannered about it.
        """

    else:

        """
        Their voices come on her behalf. Their eyes do not.

        They have noticed things too. I see that now.
        """

    host """
    Captain, you have plainly taken the events of today rather harder than the rest of us.

    Whatever small oddities you have been collecting, each of them has a perfectly ordinary explanation.

    I would gladly walk you through them, if I thought it would settle your nerves.
    """

    if current_character == host_details:

        """
        It is the right line, said in the right way, and I feel it land upon nothing at all.
        """

    captain """
    We could review them all in detail, of course.

    But why not begin with the simplest of them, my lady.

    What is your title?
    """

    host """
    Well, it is Claythorn of course, the...
    """

    captain """
    That is not what I have seen. There is no 'Claythorn' title. That is meant to be your family name.

    What is your title?

    Surely you have not forgotten the title you were raised under.

    Your father would have said it aloud in your presence a hundred times.

    Letters would have come addressed to it.

    You must have heard it pronounced when you were presented at court.

    What is it?
    """

    return


# --------------------------------------------
#   She cannot give the title. The mask comes
#   off, and the butler returns to a room that
#   already knows far too much.
#
#   Shared by the Captain and the Host.
# --------------------------------------------
label common_day2_evening_host_unmasked:

    if current_character == host_details:

        """
        I have nothing left to give him that anybody in this room would believe.

        So I say nothing at all, and I let the silence do what silence always does.
        """

    else:

        """
        She opens her mouth.

        She closes it again. Her eyes go to her hands, then to the door, then back to me.

        The room takes the silence and settles into it.
        """

    psychic """
    Lady Claythorn?
    """

    if current_character == host_details:

        """
        Miss Baxter says the name gently, the way one calls a person back into a room.

        It is not my name. It never was.

        And I have not the strength to answer to it once more.
        """

    else:

        """
        There is no answer.

        Whatever air of authority she has worn this weekend leaves her by inches.

        Instead, her calm composure changes to something else.

        Fear.
        """

    host """
    Very well, Captain.

    You are right.

    I believe it is time I dropped the mask.

    I am not Lady Claythorn.
    """

    captain """
    Who are you then?
    """

    host """
    An actress.

    I was hired for being here.

    I was given a script of sorts, and the run of the house, and a fee.
    """

    if current_character == captain_details:

        $ host_details.description_hidden.unlock('lie')

    nurse """
    Hired? You mean to tell us this entire weekend has been a... a performance?
    """

    host """
    Only some of it.

    But I swear to you, things have gone far beyond what was planned.

    What has happened to Mr Moody, and to Doctor Baldwin, I had no notion.

    None of that was in any script I was given.

    I am every bit as frightened as you are. More so, perhaps.
    """

    captain """
    Frightened of whom, madam?
    """

    host """
    I do not know, and I do not understand the half of what is happening here.

    The staff. They are not staff.

    They were hired the same way I was.

    I think they know less than I do, if anything at all.

    Except for...

    Except the...
    """

    captain """
    The butler.
    """

    host """
    Yes.

    He answers to whoever is behind this directly.

    He gives the orders. He chooses what we are told and what we are not.

    If anyone in this house knows what is truly being done under its roof, it is he.
    """

    play sound door_knock

    $ play_music('danger', 2)

    if current_character == host_details:

        """
        Three knocks upon the tea room door. Unhurried.

        I have heard that knock at my own door twice already this weekend.

        I know exactly who is standing behind it, and I have no notion at all how long he has been there.
        """

    else:

        """
        A measured rap upon the door of the tea room.

        Three knocks. Unhurried.

        The colour leaves Lady Claythorn's face entirely.
        """

    butler """
    My lady? Captain Sinha?

    Forgive the intrusion.

    I find myself rather curious as to why you have all withdrawn together in here.
    """

    if current_character == host_details:

        """
        He closes the door behind him with patient courtesy, and he looks at me.

        Only at me, and only for a second, and he has the whole of it.
        """

    else:

        """
        He closes the door behind him with patient courtesy.

        His eyes go straight to Lady Claythorn's face and read it in a single glance.
        """

    butler """
    Madam.

    What is happening here?
    """

    captain """
    She told us everything, I am afraid.

    About her role in the events of this weekend.

    And about yours.
    """

    if current_character == host_details:

        """
        I watched this man carry a dead doctor up my staircase today without altering his breathing.

        He is not calm now.
        """

    else:

        """
        He receives this in silence.

        A man weighing, very rapidly, a number of unpleasant choices.
        """

    butler -serious """
    Then we have a difficulty.

    Captain, I shall not insult any of us with theatre.

    I am no more the butler here than the lady is its mistress.
    """

    captain """
    Then to whom do you answer?

    And what is being done in this house?
    """

    butler """
    I am afraid I know no more of it than whatever Lady Claythorn might have told you.
    """

    host """
    You are lying! You have been in charge here the whole time!
    """

    butler """
    That does not mean I know more than you.

    Only that I have more to do.
    """

    captain """
    Do what?

    What were you meant to do to us?

    I think it is clear, now, that we are not here to receive any prize.

    What then?

    To make a play of us all?

    To hurt us?

    To kill us, as you killed Mr Moody and Doctor Baldwin?
    """

    butler """
    No, of course not. Nobody was supposed to get hurt!

    It was supposed to be just a... just a...
    """

    captain """
    Just what?
    """

    butler """
    I cannot say more than that.

    There is no reason for you to know.

    But I give you my word, you have nothing to fear.

    Nothing bad is going to happen.

    All you have to do is retire to your rooms and wait for the police tomorrow.

    Then you will be able to forget all about this weekend.
    """

    nurse """
    And the prize money?
    """

    butler """
    I am afraid that was another lie. I am sorry.
    """

    nurse """
    Lady Claythorn, or whatever your name truly is, is he telling the truth?
    """

    host """
    He is.

    There was never any money. From what was explained to me, all of this was meant to attract you all here for the week-end.

    But I have no notion of the reasons behind it.
    """

    butler """
    Enough talking!

    Here is what is going to happen now.

    You will all go to your rooms, give me your key as I close the door behind you.

    You will have to do without supper, but I daresay it will not kill you.

    You shall be free to leave tomorrow.

    The police will come and get you.
    """

    captain """
    You really expect us to follow your orders?
    """

    butler """
    I believe you will, if you value your life, Captain.
    """

    if current_character == host_details:

        """
        He brings a revolver out from under his coat as easily as another man produces his watch.

        I engaged the maid and the cook myself. I did not engage him.

        And in all the days I have spent in this house, it never once crossed my mind that he was carrying that about beneath his livery.
        """

    else:

        """
        He swiftly produces a revolver and points it directly at me.

        I came armed myself. But the pistol is in the pocket of my other jacket, in my bedroom.

        At present, I am defenceless.
        """

    nurse """
    But you swore you would not hurt us.
    """

    butler """
    I will not, unless I am forced to.

    This is for my own protection, I assure you.
    """

    if current_character == host_details:

        """
        He holds it the way a man holds a thing he has held a great many times before.

        Nobody in this room is going to talk him out of anything.
        """

    else:

        """
        He looks very sure of him, holding the gun with a firm hand.

        Whatever this man was before he was a butler, he was no stranger to a revolver.
        """

    return


# --------------------------------------------
#   Captain Sinha goes for the revolver.
#   The first shot is lost, and it takes the
#   hostess in the side.
#
#   Shared by the Captain and the Host.
# --------------------------------------------
label common_day2_evening_butler_gunfight:

    play sound gun

    if current_character == host_details:

        """
        Captain Sinha moves before anybody in the room has finished breathing.

        The revolver goes off, and the sound of it is nothing whatever like the sound we used to make for it on a stage.

        He is already beneath the line of the barrel.

        And something takes me in the side, very hard, as though the chair had been kicked out from under me.

        There is no pain in it at all. That is the strange part.
        """

    else:

        """
        I am moving before I have properly decided to.

        He fires, and I am already beneath the line of it, and the shot goes over my shoulder.

        Behind me there is a small sound that the room has no business making.

        Then my hands are upon his wrist, and the two of us go into the tea table together.
        """

    nurse """
    She is hit! Lady Claythorn is hit!
    """

    if current_character == host_details:

        """
        Miss Marsh is on her knees beside me with both hands pressed to my dress, telling me to lie still.

        Above us the two men turn over one another on the floor, for the revolver.

        I should like very much to tell one of them my own name.

        And I cannot think of a single person in this house who would know what to do with it.
        """

    else:

        """
        Miss Marsh cries out behind me, and I have not half a second to spare for it.

        The woman is hit. I heard where the shot went, and I know well enough what it found.

        I have his wrist in both hands, and the muzzle is coming back towards me by inches.
        """

    return
