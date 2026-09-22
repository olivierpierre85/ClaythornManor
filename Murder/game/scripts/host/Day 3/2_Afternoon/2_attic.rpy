# --------------------------------------------
#   Host - Sunday afternoon, she hides
#
#   She cannot face ten miles of that road, so the Captain goes for the
#   town alone and leaves her the butler's key. She locks herself into the
#   attic storage room and waits.
#
#   Lunch happens two floors below without her. She hears the end of it
#   through the boards, and then nothing, for a long time.
#
#   She comes down at three and finds Samuel Manning alive in the dining
#   room, everyone else dead, and then the butler walking up the drive.
#   She can stand, so it is her choice to be found at the table.
#
#   Unlocks : drunk 'faked_death' and 'lie', butler 'took_valuables'
# --------------------------------------------
label host_day3_afternoon_attic:

    host """
    I cannot walk it, Captain.

    I should not get as far as the gates before you had to carry me.
    """

    captain """
    I see.

    I could go alone then, and come back with help.
    """

    host """
    You should.

    I do not like it, but one of us must reach the town.

    You will be much faster this way.

    Go now, while there is daylight, and send them up here as fast as they will come.
    """

    captain """
    understood, but what will you do?
    """

    host """
    I will find a place to hide and wait for you.

    I do not want to risk talking with anyone else until then.
    """

    captain """
    It is probably for the best.

    Here, takes the butler's key then. It opens every door in this house. 
    
    Lock yourself in somewhere, and open to nobody but me.
    """

    """
    I take it.
    """

    captain """
    I will be back before dark, with the police.
    """

    host """
    I hope so.
    """

    """
    Without further ceremony, he goes out by the main door.

    I stand in the hall and listen to his feet on the gravel until I cannot hear them any more.
    """

    call change_time(12, 15)

    """
    I go up the main stair as quietly as possible.
    """

    $ change_room('attic_hallway', dissolve)

    play sound door_open

    $ change_room('attic_storage_room', dissolve)

    """
    I am in the largest room of the attic.

    Filled with stacked trunks, furniture under dust sheets, boxes that cannot have been opened in a generation.

    It is the perfect place. 
    
    Even if someones comes here, I will be able to hide.

    I lock the door behind me, and I put the key back in my pocket, and I sit down on a trunk in the half dark.

    Then I wait.
    """

    call change_time(13, 00)

    call wait_screen_transition()

    """
    A house makes its own noises when it is left alone.

    A door, below. The stair, once. The boy's voice, a long way down, calling for the Captain, and then for me.

    I sit with my hands in my lap and my shoes beside me, and I do not answer.
    """

    call change_time(14, 00)

    call wait_screen_transition()

    """
    Then, from two floors down, shouting.

    A man's voice, and a woman's over it, and then something that might have been a shot, or a door, or a chair going over.

    I cannot tell through this much house.

    I stand up. I sit down again.
    """

    """
    Then nothing.
    """

    call change_time(15, 00)

    call wait_screen_transition()

    """
    I do not know how long I have been listening to nothing.

    An hour, by the light. Perhaps more.

    Whatever happened down there, it is over, and nobody has come up the stair to tell me who won.
    """

    """
    I put my shoes on, and I unlock the door.
    """

    play sound door_open

    $ change_room('bedrooms_hallway', dissolve)

    """
    The corridor, with all the doors shut but one.
    """

    $ change_room('entrance_hall', dissolve)

    """
    The hall. Nobody.

    The tea room door stands open on an empty room and a dead fire.

    The dining room door is open too.
    """

    call host_day3_afternoon_attic_manning

    call host_day3_afternoon_attic_butler

    jump host_ending_shot_by_butler


# --------------------------------------------
#   The dining room. Samuel Manning.
# --------------------------------------------
label host_day3_afternoon_attic_manning:

    $ change_room('dining_room', dissolve)

    $ play_music('scary', 2)

    """
    I stop in the doorway.

    The first thing I see is a man sitting on the floor with his back to the sideboard and his collar open, looking at me.

    The second thing is who he is.
    """

    """
    Samuel Manning.

    Samuel Manning, whose throat I saw cut this morning.
    """

    """
    I do not scream. I have no breath to do it with.

    I have my hand on the door frame and I cannot feel it.
    """

    drunk """
    Do not scream.

    For God's sake. I have heard enough of it for one day.
    """

    """
    He does not get up. He does not come towards me.
    """

    drunk """
    I am not going to hurt you.

    Look at me. Look.

    I am not one of them.
    """

    host """
    You were dead.

    I saw you. Your throat...
    """

    drunk """
    Port.

    A decent one, from the billiard room. And a razor, for the edge of it. Not deep. It did not need to be.
    """

    """
    He pulls his collar down.

    Under it, a line of scab from one side of his neck to the other, shallow as a cat's scratch and black with dried wine.
    """

    drunk """
    Nobody checks a cut throat, my lady.

    That was the whole of my case.
    """

    """
    And then, because I have not looked anywhere else yet, I look.
    """

    """
    Miss Marsh is on her side by her chair, with her eyes open.

    Mr Harring is by the window, half under the curtain, as though he had tried to get behind it.

    And Miss Baxter lies across the far end of the table with her hair in the plates.
    """

    host """
    Are they...
    """

    drunk """
    All of them.

    I have looked. I did not want to.
    """

    host """
    What happened?

    What happened here?
    """

    drunk """
    I do not know.

    I was upstairs, in my bed, being dead.

    There was shouting. The boy, and a woman screaming over him, I could not say which.

    Then a shot. Two, perhaps. I did not count.

    Then nothing, for a very long time.

    I waited an hour after the nothing before I came down.
    """

    host """
    So did I.
    """

    """
    He looks at me, and then at the ceiling, and something that is nearly a laugh goes through him and does not come out.
    """

    drunk """
    Two of us, then.

    Sitting in the dark at either end of the house, waiting for the other one to go first.
    """

    """
    He looks at his hands.
    """

    host """
    Why?

    Why would you do such a thing?
    """

    drunk """
    Because I was going to be next.

    I worked that out on Saturday, in that room, with the door locked on me and a tray coming up the back stair.

    Two men dead in two days, and both of them accidents, and the whole house nodding along.

    I have stood up in court for twenty years and watched juries nod like that.

    It is what people do when they have decided not to see something.
    """

    host """
    But to cut yourself...
    """

    drunk """
    A locked door is nothing to whoever has been walking this house at night.

    I could not get out, and I could not fight. I am not built for either.

    But I could be no longer worth the trouble.

    So I took the bottle I had put by, and I made a mess of the bed, and I lay down in it and waited for somebody to open the door and decide I was finished.

    It was the Captain who did, and I heard him tell you not to come closer.

    I could have kissed him.
    """

    $ drunk_details.description_hidden.unlock('faked_death')

    """
    I look at him.

    Samuel Manning, who could not find his own chair at dinner on Friday, sitting on the floor of this dining room stone cold sober and telling me how he outlived the whole house.

    I do not know whether to laugh or to be sick.
    """

    host """
    You were never as drunk as you let us think.
    """

    drunk """
    I was every bit as drunk as I let you think.

    I was simply not drunk the whole time.

    It is a useful thing to be thought, my lady. People stop watching you.
    """

    $ drunk_details.description_hidden.unlock('lie')

    return


# --------------------------------------------
#   The butler comes back
# --------------------------------------------
label host_day3_afternoon_attic_butler:

    """
    And then we both hear it.

    Feet on the gravel, outside. One man, walking, and in no hurry.
    """

    $ play_music('danger', 2)

    drunk """
    Somebody on the drive.
    """

    """
    I go to the window, and keep to the side of it, and look out.

    A man coming up from the gates on foot, with his hat down and his coat open, and mud on him to the knee.

    I do not need to see his face.
    """

    host """
    It is him.

    The butler. He has come back.
    """

    """
    Mr Manning is on his feet faster than a man of his years has any right to be.
    """

    drunk """
    Then I am going back to bed.

    It has served me well for a day. It can serve me a while longer.

    Come. It is a wide bed, and he will not look under it twice.
    """

    """
    I look at the service door, and I look at the three of them, and I do the sum.
    """

    host """
    No.
    """

    drunk """
    My lady...
    """

    host """
    He has come back for the silver and the pearls, and for me.

    If he finds this room with nobody alive in it, he will go through the house until he finds me, and he will find you.

    If I am here, he has no reason to look.
    """

    """
    He looks at me for one second longer, and then he goes, quickly and quietly, by the service door.

    He does not look back. I did not want him to.
    """

    play sound door_open

    """
    The front door.

    Footsteps in the hall, unhurried, the way they always were.

    He was the best butler I ever saw, and he was never a butler at all.
    """

    """
    I sit down in my own chair at the head of the table.

    If I am going to be found, I am going to be found there.
    """

    """
    He stops in the dining room doorway, and he looks round the room the way he looked round the tea room on Saturday night.

    All of it, in one glance. The three of them, and me.

    He is out of livery. He looks like what he is.
    """

    butler """
    Well.

    Still with us, my lady.
    """

    host """
    You came back.
    """

    butler """
    I was owed a great deal of money for this weekend, and I have seen nothing of it since the advance.

    I do not think our patron will be paying now.

    So I have come to pay myself, with what the house has to offer.
    """

    host """
    The silver.

    The pearls.
    """

    butler """
    It is not what I was promised.

    It is what there is.
    """

    $ butler_details.description_hidden.unlock('took_valuables')

    host """
    And them?
    """

    """
    I do not look at the floor. He does.
    """

    butler """
    None of my doing.

    I have been on the road since eleven last night, and I have the mud to prove it.

    They did this to each other, or somebody did it for them. I was not here.
    """

    host """
    Then who?

    You said nobody was supposed to be hurt.
    """

    butler """
    Nobody was.

    I did not think it would end like this. I am not sure I was meant to think at all.
    """

    """
    He takes his hand out of his coat, and the revolver is in it, and it is pointed at the floor.

    For now.
    """

    butler """
    You told the Captain.

    I saw his face last night, on the gravel. He knew what I was, and there is only one way he could have known it.

    I met him on the road, a mile past the gates. He will not be sending anybody.
    """

    """
    I knew it when he went. It is different, hearing it.
    """

    butler """
    Who else?
    """

    host """
    Nobody.
    """

    butler """
    I should like to believe that.

    It is not enough.
    """

    host """
    Manning...
    """

    """
    It is out before I can stop it.

    His eyes go to the ceiling for a moment, and come back.
    """

    butler """
    Mr Manning is upstairs with his throat cut, where the Captain found him.

    You are not going to confuse me at this hour of the day, my lady.
    """

    """
    I do not correct him.

    It is the last thing I have to give anybody, and I give it to Samuel Manning.
    """

    butler """
    You know my face. You know my name.

    You are the only one left in this house who does.
    """

    host """
    You said nobody was supposed to get hurt.
    """

    butler """
    I am sorry.
    """

    play sound gun

    return
