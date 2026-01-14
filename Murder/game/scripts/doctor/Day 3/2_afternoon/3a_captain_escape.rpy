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

        """
        If I had been at my best, I might have kept up with Captain Sinha.

        But my withdrawal is at its peak, and my pace is wretchedly slow.

        He tried to encourage me at first.

        Soon enough, he grew tired of waiting.

        He is now well ahead, and with darkness drawing in, I can barely make him out in the distance.
        """

        call doctor_day3_afternoon_captain_escape_hear_car

        """
        It does not slow.

        It is coming at full speed towards me.

        Have they not seen me?

        I turn and try to run.

        But I am too weak.

        My legs give way, and I fall hard to the ground.

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
    I think I can hear something in the distance.
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
    I don't know, with everything they just told us, I don't believe we are safe, even the two of us staying here.
    """

    psychic """
    But I can't really travel this far
    """

    """
    Ted Harring is looking to the floor, ashamed.
    """

    lad """
    I am sorry, I can't stay here any longer I can't.
    """

    psychic """
    What? Are you really gonna abandon me?

    And you doctor? Or you Captain? Can't one of you stay with me?
    """

    """
    There is an akward silence.

    None of use reply.
    """

    psychic """
    Oh I see, so there is no chance to convince you is there?
    """

    captain """
    I would stay of course, but I am afraid they will need my military skills to make the trip.
    """

    """
    Military skills to walk alongside a road? That's a weird reaction from a war hero.

    Is he actually scared?
    """

    psychic """
    All right, then I believe that I don't have other options than to come with you.
    """

    captain """
    Are you quite sure?

    It won't be an easy walk.
    """

    psychic """
    I am certain.
    """

    captain """
    Very well, let's get ready before we leave then.
    """

    """
    Captain Sinha instruct us to tak
    """

    # WHat offer to take the car, to carry her, NO clothes in Lady Claythorn room.
    # Long march, the four of them.

    return



# AI SLOP for ending
label to_use_or_not:

    """
    I was started to lose hope when we finally reached Aberdeen.

    After a quick search we were able to locate the police station.
    """

    call change_time(17, 00)

    $ change_room("police_station", irisin)

    """
    We entered dramatically, shouting for help.

    We must have looked like madmen, and it took a while before they took us seriously.

    They offered to go and check on the others, while we rested there.
    """

    call wait_screen_transition

    """
    A couple of hours later, they called for reinforcements.

    By then, we had given our statements twice over.

    Captain Sinha was calm, but I could see the tension in his jaw.

    He wanted action, not forms and questions.
    """

    doctor """
    You must understand, there is a dead man at that house.

    Samuel Manning.

    We left his body where we found it, in his room.
    """

    """
    That, at least, seemed to cut through the doubt.

    An inspector was fetched, and the mood in the station changed at once.

    Orders were given.

    Boots moved with purpose.
    """

    captain """
    How long before you reach the manor?

    Two hours at most, if you travel light.
    """

    """
    The inspector promised they would go at once.

    A small party would ride ahead.

    The rest would follow with lanterns, ropes, and whatever else they could carry.
    """

    doctor """
    And Mr Harring?

    And Miss Baxter?

    They are still there.
    """

    inspector """
    We will see to them, Doctor.

    If they are where you say they are, they will not be left behind.
    """

    call wait_screen_transition

    """
    Night had fallen by the time the first party returned.

    The inspector came straight to us.

    His coat was damp, and his cheeks were red from the cold.

    He looked tired, but not surprised.
    """

    inspector """
    Your friends are alive.

    Shaken, but alive.

    The young man was doing his best to keep her steady.
    """

    """
   I felt my shoulders loosen for the first time in hours.

    Captain Sinha gave a curt nod.

    It was not relief, not quite.

    More like permission to breathe.
    """

    inspector """
    We found the body you described.

    Samuel Manning.

    Just as you said.

    The house, however, was all wrong.

    Too quiet.

    Too empty.
    """

    captain """
    The staff?

    The other guests?
    """

    inspector """
    Gone.

    No sign of struggle downstairs.

    No lamps lit, no fires, no supper laid out.

    As if they walked out and never came back.
    """

    """
    Reinforcements were sent anyway.

    More men, more horses, more questions.

    They swept the grounds, the woods, the road, and every outbuilding they could find.

    Nothing.

    Not a single soul, beyond the two you left behind.
    """

    doctor """
   Then we were right.

    It was coordinated.
    """

    inspector """
    It looks that way.

    We will keep searching.

    But there is something else.
    """

    """
    He hesitated before speaking.

    It was the sort of pause that makes you dread the next sentence.
    """

    inspector """
    The second body you mentioned.

    Thomas Moody.
    """

    doctor """
    Yes.

    He wore a mask.

    He was dead in his bed.
    """

    inspector """
    That is the trouble.

    Thomas Moody is already dead.
    """

    """
    The words did not make sense at first.

    I stared at him, waiting for the correction.

    None came.
    """

    captain """
    Explain yourself.

    Now.
    """

    inspector """
    We telegraphed ahead.

    We contacted the address on record.

    We checked the registry.

    Thomas Moody died weeks ago.

    There was a funeral.

    A certificate.

    A grave.
    """

    """
    My mouth went dry.

    I remembered the face under the mask.

    Untouched.

    Unscarred.

   Never his.
    """

    doctor """
    Then whoever was in that bed was not Thomas Moody.

    But someone wanted us to believe he was.
    """

    captain """
    And you are certain?

    This is not a clerical error?
    """

    inspector """
    I am certain.

    We have already sent men to confirm it in person.

    But the paperwork is solid.

    This is not a mistake.
    """

    # TODO: adjust thread key if needed
    $ doctor_details.threads.unlock('broken_already_dead')

    """
    It was like a door opening in my mind.

    The mask was not to hide wounds.

    It was to hide a lie.
    """

    doctor """
    Samuel Manning was real.

    But Thomas Moody was a name borrowed for the occasion.

    Or a story.

    Or a warning.
    """

    inspector """
    That is what we intend to find out.

    You will both remain in Aberdeen for now.

    We may need you again.

    There will be more questions.
    """

    """
    Captain Sinha did not protest.

    Not aloud.

    But I could see he hated it.

    Being trapped in a different sort of room, with a different sort of door.
    """

    call wait_screen_transition

    """
    In the days that followed, the police reached out to the families of the missing guests.

    Names were confirmed.

    Letters were sent.

    Telegraphs went unanswered.

    Every answer brought two more questions.
    """

    """
    Ted Harring and Amelia Baxter were kept under watch for a night, then released.

    They were not accused, but they were not trusted either.

    Not yet.

    Not in a case as strange as this.
    """

    """
    As for me, I tried to find Andrew again.

    I asked after him.

    I described him.

    I waited near the station, hoping he would appear as if nothing had happened.

    He never did.
    """

    doctor """
    I can only hope he is all right.

    And that he had the sense to keep moving.
    """

    """
    Claythorn Manor was sealed.

    Guards were posted.

    The forest was searched until boots wore thin and tempers grew sharp.

    Yet the truth remained out of reach.

    A house full of people.

    A house full of lies.

    And the most unsettling fact of all.

    One of the dead men had been dead already.
    """