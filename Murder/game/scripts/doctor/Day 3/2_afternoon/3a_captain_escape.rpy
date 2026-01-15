label doctor_day3_afternoon_captain_escape_without_psychic:


    if doctor_details.saved_variables['doctor_day3_afternoon_captain_share'] > 1:

        """
        Ted Harring pauses for a second.

        I can see my revelations have troubled him.

        He does not seem certain what he ought to do.
        """

    else:

        """
        Ted Harring answers without hesitation.
        """

    lad """
    Of course, I'll stay.

    Only a monster would leave you alone like this.
    """

    psychic normal """
    Thank you, Mr Harring.

    That means the world to me.
    """

    captain """
    Very well.

    Doctor Baldwin and I will go at once.

    I do not wish to lose time, darkness will be upon us soon.

    With luck, we shall be back with help tonight.
    """

    psychic """
    Very well, we will wait here.

    Hopefully nothing will happen until then.
    """

    captain """
    Then it is decided.

    Doctor, let us take the bare necessities from our rooms and be on our way.

    The sooner, the better.
    """

    $ change_room("forest_road", dissolve)

    call change_time(15, 00)

    """
    We took only a few things to help us on the road.

    Most of our luggage remains at the manor.

    We shall have it back soon enough, I hope.
    """

    doctor """
    That was a rather swift departure.
    """

    captain """
    Perhaps.

    But we were at an impasse.

    I do not believe we would have learned more by staying.

    There was no point in delaying the inevitable.

    Night will be upon us before long, and we must not waste a moment.
    """

    doctor """
    Indeed.
    """

    """
    We set off at a brisk pace, hoping to reach the town before dark.
    """

    call wait_screen_transition

    call change_time(17, 00)

    """
    A couple of hours in, I am exhausted.
    """



    if doctor_details.threads.is_unlocked('book_opium'):

        $ stop_music()

        """
        If I had been at my best, I might have kept up with Captain Sinha.

        But my withdrawal is at its peak, and my pace is wretchedly slow.

        He tried to encourage me at first.

        Soon enough, he grew tired of waiting.

        He is now well ahead, and with darkness drawing in, I can barely make him out in the distance.
        """

        $ play_music('danger_short')

        call doctor_day3_afternoon_captain_escape_hear_car

        """
        It does not slow.

        It is coming at full speed towards me.

        Have they not seen me?

        I turn and try to run.

        But I am too weak.

        My legs give way, and I fall hard to the ground.
        """

        play sound body_fall

        """
        I look back at the car.

        It only seems to be gaining speed.

        I brace for impact.
        """

        jump doctor_ending_run_over

    else:

        """
        If Captain Sinha is tired as well, he does not show it.

        I do not dare ask him to slow down.

        I will have to endure until we reach the town.

        Hopefully it will not be much longer now.
        """

        call doctor_day3_afternoon_captain_escape_hear_car

        stop sound

        """
        It stops right beside us.

        I can't see the driver, so I step closer, hoping to find a familiar face.
        """

        play sound gun

        jump doctor_ending_shot


label doctor_day3_afternoon_captain_escape_hear_car:

    """
    I think I can hear something coming.
    """

    play sound car_driving fadein 4 loop

    """
    It sounds like a motor car.

    It is coming from behind.

    Could it be that the others finally found a way out?

    I turn around.

    I think I recognise Lady Claythorn's car.

    I wave at it.
    """

    return


label doctor_day3_afternoon_captain_escape_with_psychic:

    lad """
    I don't know.

    After everything they've just told us, I don't think we're safe.

    Not even if the two of us stay behind.
    """

    psychic """
    But I cannot travel that far.
    """

    """
    Ted Harring stares at the floor, ashamed.

    He looks as though he wishes he could vanish into the carpet.
    """

    lad """
    I'm sorry.

    I can't stay here any longer.

    I can't.
    """

    psychic """
    What?

    Are you truly going to abandon me?

    And you, Doctor?

    Or you, Captain?

    Can't one of you stay with me?
    """

    """
    An awkward silence follows.

    None of us replies.
    """

    psychic """
    Oh, I see.

    So there is no chance of convincing you, is there?
    """

    captain """
    I would stay, of course.

    But I am afraid you will need my experience to make the journey.
    """

    """
    Experience to walk along a road.

    It is an odd remark from a decorated soldier.

    Could it be that, behind his impassive face, he is frightened after all?
    """

    psychic """
    Very well.

    Then I have no choice but to come with you.
    """

    captain """
    Are you quite certain?

    It will not be an easy walk.
    """

    psychic """
    I am certain.

    I will likely be slower than you.

    I trust you will not leave me behind.
    """

    captain """
    Very well.

    Let us prepare ourselves before we set off.
    """

    """
    Captain Sinha instructs us to take the bare minimum from our rooms.

    He tells us to meet outside without delay.
    """

    $ change_room("forest_road", irisin)

    """
    Once the four of us were ready, we wasted no time and took to the road.

    Our progress was slow, but we stayed together for two long hours.

    I had begun to lose hope when we finally reached Aberdeen.

    After a quick search, we located the police station.
    """

    call change_time(17, 00)

    $ change_room("police_station", irisin)

    $ stop_music()

    """
    We entered in a rush, calling for help.

    We must have looked half-mad.

    It took some time before anyone took us seriously.

    They sent men to check on the manor, while we remained to give our statements.

    I explained everything, insisting on the peculiar situation of Samuel Manning.
    """

    call wait_screen_transition

    $ play_music('end_credits')

    """
    A couple of hours later, they returned.

    By then, we had given our statements twice over.

    With sombre faces, they told us they had found another body.

    Rosalind Marsh.

    She was in the attic, stabbed to death.

    Even if we half expected it, the news struck us hard.

    My mind went at once to Andrew.

    What could have become of him?

    They had found nothing to explain where Lady Claythorn and the staff had gone.

    In the days that followed, the police contacted the families of the missing guests.

    We were asked to remain nearby for a short while.

    They soon dismissed us as suspects.

    They accepted the most obvious conclusion.

    The culprits were among the missing.

    Their motives remained unclear.
    """

    """
    Captain Sinha, Ted Harring, and Amelia Baxter eventually returned home.

    As for me, I tried to find Andrew again.

    I asked after him.

    I described him.

    I waited near the station, hoping he would appear as if nothing had happened.

    He never did.

    I can only hope he is all right.

    And that he had the sense to keep moving.
    """

    """
    A week later, I returned to the police station one last time.

    They were ready to move on.

    Yet they had just received unsettling news.

    They had found Thomas Moody's mother, and informed her of her son's death.

    But when they told her Thomas was dead, she said they were mistaken.

    Thomas Moody had died months ago, apparently from war injuries.

    Then she added something else.

    Her other son, Archibald, had been missing for a week or more.
    """

    $ broken_details.description_hidden.unlock('lie_name')

    jump doctor_ending_escape
