# ------------------------------------
#   THE GONG
# ------------------------------------
label broken_day2_evening_ring_gong:

    $ change_room('dining_room')

    """
    The gong stands by the dining room door, the beater hanging at its side.

    I must make sure everybody hears it.
    """

    play sound dinner_gong

    """
    Once is probably not enough.
    """

    play sound dinner_gong

    """
    And a third for good measure.
    """

    play sound dinner_gong

    """
    The sound rolls through the house like a wave.
    
    I stop to check the entrance hall to see if anyone is coming down.
    """
    
    $ broken_details.threads.unlock('gather_everyone')

    $ change_room('entrance_hall')

    """
    The first person I see is Amelia Baxter.

    She gives us a puzzled look.
    """

    psychic angry """
    What is happening here?

    Who rang the gong like that?

    If this is some sort of drunken joke, it's in very poor taste.
    """

    """
    She looks intensely at Samuel Manning as she is saying that.
    """

    captain """
    I am sorry, Miss Baxter, but I am afraid it is not a joke.

    There is some very serious matter we need to discuss urgently with everybody.
    """

    psychic -angry """
    How serious you sound, Captain.

    What is this about?
    """

    broken """
    We will wait until everyone is here before discussing it all.
    """

    """
    Rosalind Marsh is now coming down too, looking tired and perplexed.

    She is followed by Doctor Baldwin.

    Of the three, he is the one looking the worst, holding the stair rail so as not to fall.
    """

    doctor """
    What is the meaning of this?
    
    I thought the house might have been on fire.
    """

    captain """
    Nothing so dramatic, Doctor.

    But we do need to talk to everyone.
    """

    nurse """
    Well, in that case there is only Lady Claythorn missing.

    And the staff too, of course.

    Where could they be?
    """

    broken """
    That is what we need to discuss.

    We believe the staff have left.
    """

    captain """
    And it is then most likely that Lady Claythorn is gone as well.
    """

    nurse """
    That is correct.

    I passed in front of her room before coming down.

    It was left wide open, and empty.

    I thought she would already be here.
    """

    captain """
    I am not surprised.
    
    We probably are the only living persons left in this house tonight.
    """

    """
    A silence follows this.
    """

    doctor """
    I am sorry Captain, but I am going to need more of an explanation than this.
    """

    captain """
    Of course, Mr Moody will explain everything.

    After all he is the closest we have to an investigator.
    """

    doctor """
    An investigator?

    I thought you were a footman turned car mechanic, Mr Moody.
    """

    broken """
    I am afraid I led you on, Doctor.

    A necessity to avoid attracting attention.

    Nobody is suspicious of a car mechanic asking questions.
    """

    doctor """
    Really, but why? 
    
    Why were you investigating at all?

    I do not understand.
    """


    broken """
    Right, let me start at the beginning.

    I was suspicious of the letter the minute I saw it.

    A mysterious prize, given in a very remote location.

    I couldn't believe it.

    So I researched it before coming.

    You see, I am a journalist, so I knew where to look, and for what.

    And what I found brought enough questions to come here, though not in the hope of receiving any prize.

    More to try and understand what it was all about.

    And I immediately found that Lady Claythorn was lying about many things.
    """

    nurse """
    Lying? About what?
    """

    broken """
    The award, for instance. 
    
    She told me her family had been giving it away for years.

    But I couldn't find any trace of it during my research.

    No, all I found was that the family owning Claythorn Manor was actually in debt.

    Hardly in a position to give money away freely.
    """

    nurse """
    Of course, there was never any money.

    I feared as much myself.

    But the idea of receiving such a large sum was too enticing to decline.
    """

    broken """
    Exactly.

    Very few of us were in a position to turn down that money.

    That is why most of us accepted the invitation.

    Even so, from what I learned, the reason given was often vague.
    """

    doctor """
    What do you mean? 

    Mine was very specific.

    It was true that I had been in charge of St Margaret Hospital for the longest time.

    I have actually checked the records to be sure.
    """

    broken """
    That may be true, but there are hundreds of such hospitals.

    Do you think you were the most deserving in the whole nation?
    """

    doctor """
    I don't know...

    I suppose I can see why it would be a bit hard to believe.
    """

    psychic """
    But mine mentioned a very memorable fact.

    Something that even reached the papers.

    How my gift allowed for the miraculous saving of a child, the son of a prominent member of the aristocracy.

    And Mr Harring had something in the press as well.
    
    I believe he rescued someone from a fire and...
    """

    broken """
    All right, some reasons were more specific than others.

    But mine and Captain Sinha's were about things that happened during the war.
    
    Things that could have applied to hundreds, if not thousands, of people in this country.
    """

    nurse """
    Then why are we all here, if not to receive a prize?
    """

    """
    I pause a little before answering.
    """

    broken """
    Well, I cannot say for certain.
    
    But I think someone invited us here to hurt us, or more precisely, to make some of us hurt the others.
    """

    nurse surprised """
    Hurt some of the others?

    Wait, what do you mean by that?
    """

    doctor """
    Yes, please explain.
    """

    captain """
    Well, to put it bluntly, doctor, Mr Moody was given a letter that was supposed to make him want to kill me.
    """

    psychic """
    What?!
    """

    nurse """
    Kill you?

    But why?
    """

    captain """
    That is not all.

    Samuel Manning was also given a letter.
    
    A letter that could very well have driven him to hurt you, Dr Baldwin.

    Luckily, Mr Moody was clever enough to understand the plot, and perhaps save your life, Doctor.
    """

    doctor """
    What on earth?

    But why?

    Why would Mr Manning do such a thing?

    I do not even know him.
    """

    drunk angry """
    Are you sure of that, doctor?

    You might not remember.

    You have seen a lot of patients in your time, I suppose.

    And I think you have another reason to be more forgetful than most.

    I've seen you with your drugs.
    """

    doctor angry """
    What are you talking about?

    And you are one to talk, Mr Manning.

    If someone here is forgetting things, I believe everyone would agree it is most likely yourself.
    """

    captain """
    Stop it, both of you!

    There is no reason for insults.
    """

    broken """
    Captain Sinha is right.

    It is better to settle this with logic than by shouting at one another.
    """

    doctor """
    Right, and how are we supposed to do that?
    """

    broken """
    Easily.

    Mr Manning, where and when did your wife pass away?
    """

    drunk """
    Five years ago.

    At St Bartholomew's, in London.

    But I remember it clearly.

    The doctor was out of his mind half the time, and barely competent the other half.

    I am sure he was using the drugs himself.
    """

    broken """
    Doctor, where were you working five years ago?
    """

    doctor """
    Well, as I said, I have been at St Margaret Hospital for more than ten years.

    That is the reason I am here.

    At least, that is what was written in the letter.
    """

    broken """
    Good.

    Do you have it on you?
    """

    """
    He checks his pocket, then hands me a crumpled piece of paper.

    I read it, and it matches what he said.
    """

    broken """
    It appears Dr Baldwin was telling the truth.
    
    So he has nothing to do with the death of your wife, Mr Manning.
    """

    drunk """
    But the drugs, they were...
    """

    broken """
    I am sorry, Mr Manning, but I think it is sadly not uncommon for a doctor to abuse his medicine. 

    Not that I am saying this applies to you, Dr Baldwin.
    """

    doctor """
    Right.

    Also, if your doctor had really stolen your wife's narcotics, that would not have changed her chances of survival.

    You see, the drugs were only supposed to make the patient feel better, not cure them.
    """

    drunk angry """
    But that means she suffered for no reason!

    That does not make it any better.

    She was in such terrible pain.
    """

    doctor """
    I am sorry, but that wouldn't have changed her fate in the end.
    """

    drunk sad """
    Eleanor, she could have avoided so much pain...
    """

    """
    He then takes his flask in his hands and drinks it all in one go.

    Then he goes to sit on the stairs, still mumbling.
    """

    drunk """
    So much pain, why...
    """

    """
    The room is silent again.

    The others all turn towards me, waiting for me to continue.
    """

    broken """
    So here it is, I am sorry but this is all I know for now.

    I believe we are here under false pretences.

    And that some of us, if not all, are in danger.
    """

    nurse """
    I am willing to agree with you, but what are you suggesting we do now?
    """

    broken """
    Well, the most obvious choice would be to leave now.

    All of us, together.
    """

    psychic """
    But how?

    Can you drive a motorcar?
    """

    broken """
    I can.

    But that is not the problem.

    Lady Claythorn and her staff probably left with it.
    """

    psychic """
    Oh, right of course.

    Then how?
    """

    nurse """
    I saw another car, in the garage downstairs.

    But I do not know if it is working.
    """

    captain """
    I can go and check.
    """

    broken """
    Good idea, Miss Marsh, can you show the car to Captain Sinha?
    """

    nurse """
    Of course.
    """

    """
    They both leave for downstairs.

    I now realise how odd it is that she visited the garage.

    But I am interrupted in my thoughts.
    """

    psychic """
    If the car is working, that is very good.
    
    But it would probably be too small to carry us all.

    Then we won't be able to leave together.
    """

    broken """
    Maybe not.

    Some of us might have to stay here while waiting for help.
    """

    psychic """
    Wait here!?

    But you just said we were all in danger.
    """

    doctor """
    That is true, how could we decide who is to leave and who is staying?
    """

    broken """
    I don't know, but let's wait to know more before discussing it.
    """ 

    """
    Everyone agrees and we wait in silence for Miss Marsh and Sushil Sinha.

    It only takes a few minutes before they are back.
    """

    captain """
    The car won't start.

    The tank is empty and the tyres are flat.

    Probably too old to rely on them.
    """

    broken """
    I see, tough luck.
    
    That was our best chance to get out of here.
    """

    nurse """
    But the police will come tomorrow, we could wait for them, right?
    """

    broken """
    I do not think so.

    I checked the phone earlier and it is out of order.

    I doubt anyone called the police today.

    We should not count on anyone coming to rescue us tomorrow.
    """

    doctor """
    Really? 
    """

    broken """
    You can see for yourself.
    """

    """
    He goes to the phone and puts it to his ear.
    """

    doctor """
    No tone, this phone is broken.
    """

    broken """
    Yes, and I believe it never worked during the weekend.

    Lady Claythorn never planned on calling the police.

    That must be part of her plan.
    """

    nurse """
    Oh my.
    """

    doctor """
    All right, so what else could we do?

    Leave on foot?
    """

    broken """
    That is the only option I see for now, yes.

    Not tonight, of course.

    We wouldn't make it far in the dark.
     
    But we should go tomorrow at first light.

    No point in waiting for somebody to rescue us.
    """

    psychic scared """
    On foot! I would never make it!
    """

    nurse """
    Me neither, I am afraid.

    My health is not very strong, you see.

    Is there another way?
    """

    broken """
    Not without splitting into groups and leaving someone behind.

    But I strongly believe it would be best if we stayed together.
    """

    captain """
    Agreed. 

    Just because we assume the staff and Lady Claythorn have left, doesn't mean they have.

    They could still be close.

    Maybe they haven't given up on their plans yet.
    """
    
    nurse """
    You mean they could be hiding somewhere, waiting for the right moment to hurt us?

    How scary you make all of it sound.
    """

    captain """
    I am sorry to scare you, but it is the truth.
    """

    psychic """
    Captain, how are you expecting us to sleep if you keep telling us such stories?
    """

    captain """
    I do not know that we should sleep at all, actually.

    I probably won't.

    It is better to have someone standing guard at all times.
    """

    broken """
    I won't sleep either. 
    
    Better to have two guards than one.
    """ 

    psychic """
    Standing guard where?

    In the hallway?
    """

    broken """
    I don't know, even that feels dangerous.

    I was thinking we should all stay together, in the same room.
    """

    psychic """
    Really? That is very improper.
    """ 

    broken """
    These are exceptional circumstances.

    The safest choice would be to all group in the billiard room.

    The couches there are comfortable enough for a decent sleep.

    And those standing guard could stay on a chair.
    """

    nurse """
    That is not ideal, but I will concede it does sound the safest choice.
    """

    doctor """
    I agree.
    """

    captain """
    Me too.
    """

    """
    Even Samuel Manning wakes from his mumbling.
    """

    drunk """
    Fine by me.
    """

    broken """
    We are in agreement then.

    Aren't we, Miss Baxter?
    """ 

    psychic """
    Fine, if everyone agrees, I guess I won't be the only one in my room.
    """

    broken """
    Perfect.

    Then let's prepare the room.
    """

    $ change_room('billiard_room', dissolve)

    """
    We quickly got bedsheets from the bedroom.

    Everyone settled in as best they could.

    I am sure everyone still has plenty of questions, but we are too tired to talk more.

    Captain Sinha and I are taking chairs and beginning our watch.

    At first I thought nobody would be able to sleep, but soon enough Samuel Manning started snoring.

    The rest of them followed suit.

    I don't know how they can.

    I am clearly too stressed to close my eyes.
    """

    return