# --------------------------------------------
#   Host - Sunday afternoon, she hides
# --------------------------------------------
label host_day3_afternoon_attic:

    host """
    I don't think I can make the journey on foot, Captain.

    I should not get as far as the gates before you would have to carry me.

    And even if I could, I would slow you down.

    We might get caught in the dark before reaching the town.
    """

    captain """
    I see.

    I could go alone then, and come back with help.
    """

    host """
    You should.

    I do not like it, but you will be much faster this way.
    """

    captain """
    Understood, if that is what you think is best, I will leave now and walk as fast as possible.
    """

    """
    Strange. I expected him to argue against leaving me here alone.

    But I suppose he is even more eager than I am to leave this place as fast as possible.

    Could he be scared?
    """

    host """
    Very well.
    """

    captain """
    But what will you do?
    """

    host """
    I will find a place to hide and wait for you.

    I do not want to risk talking with anyone until then.
    """

    captain """
    It is probably for the best.

    Here, take the butler's key then. It opens every door in this house.
    
    Lock yourself in somewhere, and open to nobody but me.
    """

    """
    I take the key.
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
    I go up the main stair as quietly as possible and head for the attic.
    """

    play sound door_open

    $ change_room('attic_storage_room', dissolve)

    """
    I enter the largest room of the attic.

    Filled with stacked trunks, furniture under dust sheets, boxes that cannot have been opened in a generation.

    It is the perfect place. 
    
    Even if someone comes here, I will be able to find a place to hide.

    I lock the door behind me, and I put the key back in my pocket, and I sit down on a trunk in the half-dark.

    Then I wait.
    """
    
    call wait_screen_transition()

    call change_time(14, 00)

    """
    For a while, the house is silent. If anything is happening downstairs, it is happening quietly.

    Then, from two floors down, a scream.

    A woman's voice, and then nothing.

    I stand up. I sit down again.

    A long time passes. Nearly an hour, perhaps.

    Then a shot.

    And, a moment later, another.

    Then nothing.

    I want to go and see what happened, but I am paralysed with fear.

    I remind myself that I should wait for Captain Sinha.

    So I remain here and try to listen to what might be happening downstairs.
    """

    call wait_screen_transition()

    call change_time(16, 00)
    
    $ change_room('attic_storage_room')

    """
    I do not know how long I have been listening to nothing.

    An hour at least, probably more.

    It is dark outside now, and I begin to worry that Captain Sinha will not come back.
    
    I cannot stand staying here any more.

    So I gather all the courage I can muster, and unlock the door.

    I will try to peek at what is happening downstairs.
    """

    play sound door_open

    $ change_room('entrance_hall', dissolve)

    """
    First I go to the main hall.

    There is nobody here.

    The dining room door is open. I try to see what is in it.
    """

    $ change_room('dining_room', dissolve)

    $ play_music('scary', 2)

    """
    I stop in the doorway.

    Mr Harring is lying on the floor beside his chair.

    There is not a mark on him.

    But his jaw is clenched and his hands are drawn up tight, as though he died in great pain.

    Miss Baxter lies next to him, with one arm across his chest.

    There is blood in her hair, and a dark pool of it on the carpet under her head.

    A few feet away, Miss Marsh is still in her chair, slumped forward over her plate, as though she had fallen asleep at the table.

    There is a red stain spreading across the tablecloth under her.
    """

    host """
    Good God...
    """

    """
    I do not scream. I have no breath to do it with.

    I hold on to the door frame and try to make sense of what I see.

    The two women have been shot. That much is clear.

    But Mr Harring has no wound at all.

    And why would Miss Baxter be lying beside him like that, as if she had been holding him?

    I do not understand any of it.
    """

    play sound door_open

    """
    On the other side of the table, the service door opens.
    """

    $ play_music('danger', 2)

    """
    A man steps into the room.

    Samuel Manning.

    His collar is open, and the front of his shirt is stiff with dried blood.

    The same blood I saw on his throat this morning, when Captain Sinha found him in his bed.
    """

    host """
    No...

    You were dead.

    I saw you. Your throat...
    """

    drunk """
    My lady, please.

    Do not scream.
    """

    host """
    It was you.

    You pretended to be dead, and then you came down here and killed them all.
    """

    drunk """
    No.

    I have not killed anybody. Listen to me...
    """

    """
    He takes a step towards me.

    I take a step back.

    I should have asked Captain Sinha for a gun before he left.

    Then I see it.

    On the carpet, between Miss Marsh and Miss Baxter, there is a revolver.

    I do not think. I bend down and take it.

    It is heavier than I expected.

    I point it at him with both hands.
    """

    host """
    Stay where you are.
    """

    """
    He stops, and slowly raises his hands.
    """

    drunk """
    Please, allow me to explain myself.
    """

    host """
    Go on.

    You were dead, with your throat cut.
    """

    drunk """
    What you saw was an act.

    I staged it with port wine and my own razor.
    """

    host """
    Why would you do such a thing?
    """

    drunk """
    Because I was going to be next.

    I worked that out yesterday, in my room, with the door locked on me and a tray coming up the back stair.

    I might have killed Doctor Baldwin, but someone drove me to it.

    And it dawned on me that nobody would organise such an elaborate scheme just to kill one man.

    No, we were probably all going to be killed in the end.

    I realised that too late.

    I could not escape, so I reasoned that if it looked as though I had killed myself, the real killer might leave me alone.

    When the Captain found me, he cannot have looked very closely.

    And that was that.

    From then on, I was free to explore on my own.
    """

    $ drunk_details.description_hidden.unlock('faked_death')

    """
    I look at him, over the barrel of the revolver.

    Samuel Manning, who could not find his own chair at dinner on Friday, standing in this dining room stone cold sober and telling me how he outlived the whole house.

    I do not know whether to laugh or to be sick.
    """

    host """
    No, that makes no sense.

    There are only the two of us left in this house.

    And I know I am not the killer.

    So it must be you.
    """

    drunk """
    I swear I had nothing to do with these deaths.

    Put that down, my lady, and I will tell you everything.
    """

    """
    He lowers his hands, and takes a step towards me.
    """

    host """
    Stay where you are.
    """

    drunk """
    I only want to talk.

    You are shaking. Give me the gun, before somebody else gets hurt.
    """

    """
    He keeps coming towards me, slowly, with one hand held out.
    """

    host """
    I said stay where you are!
    """

    $ stop_music()

    play sound gun

    """
    The noise fills the room.

    Mr Manning stops.

    He looks down at his shirt, where a new stain is spreading over the old one.

    This time, it is not port.

    He sits down heavily against the sideboard, and then he slides onto his side.
    """

    play sound body_fall

    pause 1.0

    """
    I lower the revolver.

    My hands will not stop shaking.

    Mr Harring. Miss Baxter. Miss Marsh. And now Mr Manning.

    Mr Moody and Doctor Baldwin before them.

    Almost everyone who came to this house for the weekend is dead.

    And they will blame me for it.

    I cannot afford to talk to the police now.

    They will never believe me.

    I need to leave as fast as I can, before Captain Sinha comes back with them.
    """

    play sound fire loop

    """
    That is when I smell it.

    Smoke.

    It is coming from under the door to the hall.

    The door is shut. I do not remember shutting it.
    """

    $ play_music('danger', 2)

    """
    I run to it and take hold of the handle.

    It is warm.

    It turns, but the door does not open.

    I take out the butler's key and push it into the lock with shaking fingers.

    The lock turns.

    The door still does not move.

    Something is holding it shut from the other side.
    """

    host """
    Help!

    Is anybody there?
    """

    """
    Nobody answers.

    I turn to the windows.

    I cross the room and pull at the catch of the nearest one.

    It will not move.

    I try the next one, and the one after that.

    They are all shut fast.
    """

    play sound woman_cough

    """
    The smoke is in my throat now.

    I strike the glass with the butt of the revolver.
    """

    play sound broken_glass

    """
    It breaks, but there is a steel frame behind it.

    There is not enough room for me to get through.

    I try to lift a chair to break the whole frame, but I have no strength left.

    The room is filling with smoke, and there is a red glow under the door now.

    I think of Captain Sinha, coming back up the drive with the police.

    I hope he gets here in time.
    """

    jump host_ending_burned
