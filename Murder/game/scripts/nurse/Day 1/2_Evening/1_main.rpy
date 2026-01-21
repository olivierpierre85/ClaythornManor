# --------------------------------------------
#   Nurse
#           
#   Friday - Evening
#   
#   16:30 -> 23:00
#
#   Music: chill, upbeat
#
#   Alive: Everyone
#
#   Notes:
#       - Nurse arrives early, gets to case the manor
#       - Meets Lady Claythorn before other guests
#       - Dinner scene: observing everyone
#       - Evening exploration: stealing opportunities
#
# --------------------------------------------
label nurse_day1_evening:

    call change_time(16, 30, "Evening", "Friday", hide_minutes = True, chapter='friday_evening')

    $ current_character.add_checkpoint("nurse_day1_evening") 

    call black_screen_transition("Rosalind Marsh", chapters_names[current_chapter])

    $ change_room('great_hall', dissolve)
    
    $ play_music('upbeat')

    """
    The entrance hall takes my breath away.

    High ceilings. Original woodwork. A chandelier that could feed a family for a decade.

    And those paintings on the walls—portraits of ancestors, landscapes, religious scenes.

    Each one worth more than everything I've ever stolen combined.

    I force myself to breathe normally.
    """

    butler """
    Welcome to Claythorn Manor.

    I trust your journey was pleasant?
    """

    nurse """
    Very pleasant, thank you.
    """

    butler """
    Excellent. Lady Claythorn has asked me to show you to your rooms.

    Dinner won't be served until the remaining guests arrive.

    In the meantime, you're welcome to rest or explore the ground floor.
    """

    """
    Explore. Yes. I'd like that very much.
    """

    doctor """
    A rest sounds welcome. The journey was quite long.
    """

    broken """
    I'll take a room as well.
    """

    butler """
    Very good. Please follow me upstairs.
    """

    $ change_room('bedrooms_hallway', dissolve)

    """
    The butler leads us up the grand staircase.

    I count the steps. Eighteen. Note the creaking boards on the fourth and twelfth.

    Old habits.
    """

    butler """
    Miss Marsh, you've been assigned the "Victoria" room.
    """

    $ unlock_map('bedroom_nurse')

    $ change_room('bedroom_nurse')

    """
    He opens the door with a small brass key and gestures for me to enter.

    The room is modest by the manor's standards, but still larger than my flat in London.

    A four-poster bed. A vanity with silver-framed mirror. 

    And a window overlooking the gardens. 

    More importantly, I spot the small safe in the corner.

    Where there's one safe, there are usually more.
    """

    butler """
    I hope the room is to your satisfaction.

    The washroom is through that door, and the bell pull will summon a maid if you need assistance.

    Dinner will be at half past six.
    """

    nurse """
    Thank you. This is lovely.
    """

    """
    The butler leaves, closing the door behind him.

    I wait until his footsteps fade down the corridor.

    Then I get to work.
    """

    pause 1.0

    """
    First, I check the safe. Locked, of course, but a simple tumbler mechanism.

    I could crack it in minutes if I had the time. But not now. Too risky on the first day.

    Instead, I survey the room methodically.

    The drawers. Empty, as expected for a guest room.

    The wardrobe. Nothing but extra linens.

    Under the mattress. Clean.

    Behind the mirror. Just wall.

    Professional habit. Always know your exits, your hiding spots, your opportunities.
    """

    pause 1.0

    """
    A coughing fit catches me off guard.

    This one is worse. Deeper. I taste copper on my tongue.

    I rush to the washroom and lean over the basin. 
    
    When I'm done, I rinse away the evidence.

    The face in the mirror looks tired. Older than forty-two.

    How much longer do I have?

    Stop it. Focus on the job.
    """

    call change_time(17, 30)

    """
    I've rested long enough. Time to explore.

    The butler said the ground floor was open to guests.

    Time to see what this manor is really hiding.
    """

    $ change_room('great_hall', dissolve)

    """
    I make my way downstairs quietly.

    The staff are busy preparing for dinner. Perfect.

    I have perhaps an hour before the other guests arrive and the house becomes crowded.
    """

    $ time_left = 45

    call run_menu( TimedMenu("nurse_day1_exploration", [
        TimedMenuChoice('Explore the tea room', 'nurse_day1_tea_room', 15),
        TimedMenuChoice('Examine the paintings in the hallway', 'nurse_day1_paintings', 15),
        TimedMenuChoice('Find the library', 'nurse_day1_library', 15),
        TimedMenuChoice('Return to your room', 'generic_cancel', early_exit=True),
        ])
    )

    call change_time(18, 10)

    $ stop_music()

    """
    The sound of voices drifts from the entrance hall.

    More guests have arrived.

    Time to play my part.
    """

    $ change_room('tea_room', dissolve)

    $ play_music('upbeat')

    butler """
    Ah, Miss Marsh. The other guests have arrived.

    Allow me to introduce everyone.
    """

    """
    The butler gestures to each person in turn.
    """

    show captain at truecenter
    butler """ 
    This is Captain Sushil Sinha, recently returned from service abroad.
    """
    hide captain

    show psychic at truecenter
    butler """
    Miss Amelia Baxter, a renowned spiritualist from London.
    """
    hide psychic

    show drunk at truecenter
    butler """
    And Mr Samuel Manning, a... gentleman of independent means.
    """
    hide drunk

    """
    The hesitation in the butler's voice tells me everything.

    Manning is drunk. Obvious even from across the room.

    The spiritualist has sharp eyes but a false smile. A fellow performer, perhaps.

    The captain carries himself with military precision. Dangerous to underestimate.

    And somewhere in this house are Dr Baldwin and Mr Moody.

    Seven guests in total. Each one a potential obstacle or opportunity.
    """

    $ time_left = 15

    call run_menu( TimedMenu("nurse_day1_tea_intro", [
        TimedMenuChoice('Observe from a distance', 'nurse_day1_observe_guests', 10),
        TimedMenuChoice('Approach the spiritualist', 'nurse_day1_psychic_intro', 10),
        TimedMenuChoice('Stay quiet until dinner', 'generic_cancel', early_exit=True),
        ], image_left = "captain", image_right = "psychic")
    )

    call change_time(18, 30)

    play sound dinner_gong

    pause 1.0

    butler """
    Dinner is served. Please follow me to the dining room.
    """

    """
    Finally. Time to meet our mysterious host.
    """

    $ stop_music()

    call change_time(18, 30)

    $ change_room('dining_room', irisout)

    $ play_music('chill')

    """
    The dining room is as impressive as the rest of the manor.

    Crystal chandelier. Silver service. Genuine Wedgwood china.

    I keep my expression neutral as I calculate the value of the tableware.

    The last guest arrives just as we're being seated.
    """

    butler """
    Mr Ted Harring!
    """

    """
    A young man enters. Good-looking, but clearly out of his element.

    His suit doesn't quite fit right. His eyes dart around the room nervously.

    He reminds me of myself, twenty years ago.

    Before I learned to hide better.
    """

    pause 1.0

    """
    Everyone takes their seats.

    I find myself between Captain Sinha and Mr Moody.

    Not ideal company, but a good vantage point to observe everyone else.
    """

    """
    Then Lady Claythorn makes her entrance.
    """

    call common_day1_evening_host_welcome_speech

    """
    One thousand pounds. Bearer bonds. 
    
    Untraceable.

    But there's something in her words that unsettles me.

    "Exceptional acts of bravery."

    If only she knew.
    """

    host """
    Please, there's no need to thank me. 
    
    The food will be served shortly. 
    
    Enjoy your meal.
    """

    """
    The butler and footman begin serving.

    I watch the staff carefully. The footman seems nervous around the doctor.

    The butler misses nothing. He'll be the one to avoid.

    The food is excellent, but I barely taste it.

    I'm too busy cataloguing. Observing. Planning.
    """

    $ time_left = 60

    call run_menu( TimedMenu("nurse_day1_dinner", [
        TimedMenuChoice('Engage Captain Sinha in conversation', 'nurse_day1_dinner_captain', 20, next_menu="captain_generic_menu_nurse"),
        TimedMenuChoice('Try to draw out Mr Moody', 'nurse_day1_dinner_broken', 20),
        TimedMenuChoice('Listen to the other conversations', 'nurse_day1_dinner_listen', 20),
        TimedMenuChoice('Eat in silence, observe everything', 'generic_cancel', early_exit=True),
        ], image_left = "captain", image_right = "broken")
    )

    call change_time(21, 00)

    $ stop_music()

    """
    Dinner comes to an end.

    Lady Claythorn mentions drinks in the billiard room for those interested.

    Several guests seem eager to continue socialising.

    But I have other plans.
    """

    host """
    For those who are tired from your journey, the staff can show you to your rooms.

    We have a busy weekend ahead.
    """

    nurse """
    I think I'll retire early, if that's alright. It's been a long day.
    """

    host """
    Of course, Miss Marsh. Rest well.
    """

    """
    I head upstairs, but I don't go directly to my room.
    """

    $ change_room('bedrooms_hallway', dissolve)

    $ play_music('upbeat')

    """
    The corridor is empty.

    Most guests are still downstairs. The staff are occupied.

    This is my chance for reconnaissance.
    """

    $ time_left = 90

    call run_menu(nurse_details.saved_variables["day1_evening_map_menu"])

    call change_time(23, 00)

    $ stop_music()

    """
    I've pushed my luck far enough for one night.

    Time to return to my room and take stock.
    """

    $ change_room('bedroom_nurse', dissolve)

    """
    I lock the door behind me.

    My notebook comes out. I record everything I've observed.

    The layout of the manor. The location of valuables. The habits of the staff.

    The other guests and their weaknesses.

    A coughing fit interrupts my notes.

    This one leaves spots of blood on the page.

    I tear it out and burn it in the candle flame.

    No evidence. Not even of my own mortality.
    """

    pause 1.0

    """
    I change into my nightclothes and get into bed.

    Tomorrow, the real work begins.

    One thousand pounds is a nice prize.

    But this manor holds much more than that.

    I close my eyes.

    Sleep comes quickly, but my dreams are filled with masks and shadows.
    """

    jump nurse_day2_morning

    return


# ============================
# EXPLORATION LABELS - AFTERNOON
# ============================

label nurse_day1_tea_room:

    $ change_room('tea_room', dissolve)

    """
    The tea room is elegantly furnished.

    Plush sofas. Side tables with silver tea service.

    I run my finger along a candlestick. Solid silver. 

    Not plate—the real thing.

    It would fit nicely in my bag.

    But not yet. Too soon. Someone might notice.

    I make a mental note and move on.
    """

    """
    A drinks cabinet catches my attention.

    Crystal decanters filled with amber liquid. Port. Whisky. Brandy.

    The stoppers alone are worth stealing.

    I check the lock on the cabinet. Simple. Child's play.
    """

    pause 1.0

    nurse """
    (Muttering)
    Patience. Always patience.
    """

    """
    I memorise the layout and slip back into the hallway before anyone spots me.
    """

    return


label nurse_day1_paintings:

    $ change_room('bedrooms_hallway', dissolve)

    """
    I pause before a landscape painting.

    Constable, unless I'm mistaken. Early work, perhaps, but authentic.

    It would fetch a small fortune at auction.

    But stealing paintings is too conspicuous. They're noticed immediately.

    Silverware, jewellery, small objects—those disappear without anyone noticing for days.

    Besides, I couldn't carry it.
    """

    """
    I study the portraits instead.

    Generations of Claythorns stare back at me.

    The same prominent nose. The same cold eyes.

    One portrait catches my attention—a young woman in Victorian dress.

    Her jewellery is painted with exquisite detail.

    I wonder if those pieces are still in the house.
    """

    return


label nurse_day1_library:

    $ change_room('library', dissolve)

    """
    The library is massive.

    Floor-to-ceiling shelves, packed with leather-bound volumes.

    First editions, no doubt. The wealthy always collect books they never read.

    I scan the spines. Medical texts, surprisingly.

    "Materia Medica." "Gray's Anatomy." "A Treatise on Opium."

    Someone in this family had an interest in medicine.

    Or poison.
    """

    pause 1.0

    """
    I check the desk drawers. Locked.

    The wastepaper basket holds nothing of interest.

    But behind a row of books on the third shelf, my fingers find something hidden.

    A small key.

    I pocket it without hesitation.

    Every key opens something.
    """

    # TODO: Make this an object/observation later
    # $ nurse_details.objects.unlock('library_key')

    return


# ============================
# TEA ROOM INTRODUCTION LABELS
# ============================

label nurse_day1_observe_guests:

    """
    I position myself near the window, half-hidden by the curtains.

    From here, I can watch everyone without being watched.

    The captain is regaling the doctor with war stories.

    Dr Baldwin's attention keeps drifting to the footman.

    Interesting.
    """

    """
    Miss Baxter, the spiritualist, is speaking to Lady Claythorn's portrait.

    Or perhaps she's pretending to commune with the dead.

    Either way, she's more observant than she appears.

    I catch her glancing at me twice.

    A fellow professional recognises another.
    """

    """
    Samuel Manning is unconscious in his chair, glass in hand.

    The masked man, Moody, sits alone in the corner.

    His eyes scan the room constantly, cataloguing everything.

    Just like mine.

    We're all hiding something.
    """

    return


label nurse_day1_psychic_intro:

    """
    I approach the spiritualist.

    She turns before I reach her, as if she sensed my presence.

    Theatrical, but effective.
    """

    nurse """
    Miss Baxter, isn't it? I'm Rosalind Marsh.
    """

    psychic """
    Ah, Miss Marsh. I felt you approaching.

    The spirits whispered of someone with heavy burdens.
    """

    """
    I keep my expression neutral.

    If she's fishing for information, she'll have to try harder than that.
    """

    nurse """
    How fascinating. You're a medium, then?
    """

    psychic """
    I prefer 'spiritualist.' I help those who've passed communicate with those who remain.

    Do you have someone you wish to contact?
    """

    """
    My sister. My mother. A dozen soldiers I couldn't save.

    But I don't tell her that.
    """

    nurse """
    Not at the moment, thank you.

    Perhaps we can speak more over the weekend.
    """

    psychic """
    I look forward to it.

    The spirits tell me we have more in common than you might think.
    """

    """
    Her smile doesn't reach her eyes.

    Neither does mine.
    """

    return


# ============================
# DINNER LABELS
# ============================

label nurse_day1_dinner_captain:

    nurse """
    Captain Sinha, wasn't it? I understand you served abroad.
    """

    captain """
    Indeed. Thirty years in His Majesty's service.

    India, mostly. Though I spent time in Africa as well.
    """

    """
    His accent is cultured. English schooling, probably.

    But there's steel beneath the politeness.
    """

    nurse """
    I was in the military myself. Nursing corps.

    Though my service was more... recent.
    """

    captain """
    The Great War? You have my respect, Miss Marsh.

    The things those nurses endured...
    """

    """
    He trails off, lost in memory.

    We share that, at least. Some things you can never unsee.
    """

    call captain_generic

    return


label nurse_day1_dinner_broken:

    """
    I turn to my other neighbour.

    The masked man has barely touched his food.

    Eating must be difficult with that prosthetic.
    """

    nurse """
    Mr Moody, isn't the food to your liking?
    """

    broken """
    The food is fine.
    """

    """
    His voice is quiet. Distorted slightly by the mask.

    He doesn't elaborate.
    """

    nurse """
    I understand if you'd rather not talk. I was a nurse during the war.

    I've seen what men like you have endured.
    """

    """
    For a long moment, he says nothing.

    Then, quietly:
    """

    broken """
    You've seen the aftermath.

    You haven't seen the moment it happens.

    The sound your own face makes when it's torn apart.
    """

    """
    I don't look away.
    """

    nurse """
    No. I haven't.

    But I've held men's hands while they died from wounds like yours.

    Does that count for anything?
    """

    broken """
    Maybe.
    """

    """
    He returns to his silence.

    But something has shifted between us.

    A recognition, perhaps. Two people who've seen too much.
    """

    return


label nurse_day1_dinner_listen:

    """
    I keep my head down and my ears open.

    Years of hospital shifts have taught me the value of eavesdropping.
    """

    pause 1.0

    """
    The captain is telling Dr Baldwin about tiger hunting.

    The doctor seems more interested in watching the footman than listening.

    At the far end of the table, Miss Baxter is asking Lady Claythorn about the manor's history.
    """

    host """
    The manor has been in my family for generations.

    My husband's grandfather built it. Though my husband has been... unwell for some time.
    """

    psychic """
    I'm sorry to hear that. Is he here?
    """

    host """
    He keeps to the upper floors. You're unlikely to see him.
    """

    """
    Interesting. An invalid husband hidden away.

    What else is Lady Claythorn hiding?
    """

    pause 1.0

    """
    The young man—Harring—is eating too fast and talking too little.

    He's nervous. Out of place.

    Mr Manning is drinking steadily. He'll be unconscious before dessert.

    And Mr Moody...

    Mr Moody is watching everyone.

    Including me.
    """

    return
