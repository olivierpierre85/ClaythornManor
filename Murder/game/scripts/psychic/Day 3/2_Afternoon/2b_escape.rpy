label psychic_day3_afternoon_escape:

    $ psychic_details.important_choices.unlock('leave_manor')

    psychic """
    You're right.

    I can't stay one more minute in this cursed place.
    """

    captain """
    Are you sure?

    It won't be an easy walk.
    """

    psychic """
    I am certain.
    """

    captain """
    Very well, let's get ready before we leave then.

    I suggest we all put on our most comfortable shoes, warm clothing and leave everything else here.

    No need to be encumbered by our luggage. Hopefully, we will come back soon enough to retrieve it.

    Let's get ready and meet in the main hall in 15 minutes.

    Do you agree?
    """

    psychic """
    Of course.
    """

    lad """
    Sounds good to me.
    """

    pause 1.0

    $ change_room('great_hall', dissolve)

    # TODO on her room there is Rosalind Marsh, she stabs her. NEW SCENE WHEN ENDING REACHED
    # TODO change grab what I need by something implying I killed Rosalind Marsh
    """
    I rush to my room, grab what I need, and hurry down to the hall as fast as possible.

    The others are already there.

    Captain Sinha has a large coat and sturdy boots with him.

    Ted Harring, on the other hand, doesn't seem to have changed his clothes at all.
    """

    captain """
    All right, if everyone is ready, let's set out.
    """

    """
    We then proceed to exit the house, leaving its impressive shadow behind us.
    """

    $ change_room('forest_road', dissolve)

    $ stop_music()

    """
    We've been walking for a couple of miles already.
    
    I am struggling to keep up but, besides that, everything is going smoothly.
    
    Maybe too smoothly.
    
    I stop to take a brief break.
    
    As I catch my breath, I look at the forest surrounding us.
    
    Then...
    """

    $ play_music('danger')

    psychic """
    Captain, could you come and see something?
    """

    captain """
    Of course, what is it?
    """

    """
    He retraces his steps to my level, while Ted Harring continues walking ahead.
    """

    psychic """
    Can you look over there, behind that huge oak tree?

    I thought I saw something.

    I might be imagining things, but it looked like a person.
    """

    captain """
    I can spot the tree but see no one.
    """

    psychic """
    I don't see it anymore, but it was definitely there a second ago.

    I'm sure of it.
    """

    captain """
    Alright, I'll go and check quickly.
    """

    """
    Without hesitation, he rushes towards the large tree ahead.
    """

    play sound gun 

    psychic """
    Captain!!
    """

    """
    The gunshot stops him in his tracks.

    It looks like he's going to collapse, but then he steadies himself and comes back towards me.
    """

    # I barely have time to hide the smoking gun in my right hand.

    captain """
    Bloody hell, I didn't see that one coming.

    Somebody shot at us.

    Run!
    """

    """
    He then began to limp as fast as he could.

    I try to help him by carrying him.
    """

    captain """
    Stop this nonsense,

    Run to safety.
    """

    psychic """
    I can't leave you; you are injured, you need help.
    """

    captain """
    It's probably too late for that anyway.

    I think the bullet hit an artery.
    """

    """
    I looked down and saw that his shirt is bright red.

    He is right, the wound looks fatal.

    But I try not to alarm him.
    """

    psychic """
    It's not so bad.

    I am sure you've had worse than this.
    """

    captain """
    Yeah, right.

    If only that were true.
    """

    psychic """
    What do you mean?
    """

    captain """
    I've never fought a battle in my life,

    I am an...

    ...administrative officer.

    This weekend was definitely the most dangerous...

    ...situation I've ever been in.

    I shouldn't...

    ...have come here.
    """

    $ captain_details.description_hidden.unlock('lie') 

    """
    He collapses after saying that.

    There's no need to carry him any more.

    So I leave him and try to run to Ted Harring.

    But he is already so far away, I can't see him.

    I realise that he didn't even try to help us.
    """

    $ stop_music()
    
    pause 1.0 

    $ change_room('police_station', dissolve)

    $ play_music('end_credits')

    """
    I went as fast as I could but was never able to catch up with Ted Harring.

    At least until I reached the town.

    I went straight to the police station and there he was.

    When I entered, he looked embarrassed to see me.

    Probably feeling the weight of the guilt of leaving me to an uncertain fate.
    """

    pause 1.0 
    
    """
    But I was glad he had made it anyway.

    I hugged him and told him about Sushil Sinha.

    He replied that officers were on their way to Claythorn Manor.

    We waited for them for a long time.

    They came back only to confirm what we already knew.

    Sushil Sinha had succumbed to his injuries.
    
    There was no one alive at the manor.

    In addition to Samuel Manning, Thomas Moody, and Daniel Baldwin, they also found Rosalind Marsh's body.

    She had been stabbed to death and was lying somewhere in the attic.

    However, they found no trace of Lady Claythorn and her staff.
    """

    jump psychic_ending_escape