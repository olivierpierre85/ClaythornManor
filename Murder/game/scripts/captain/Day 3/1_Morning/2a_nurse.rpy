# --------------------------------------------
#   Captain — Sunday morning, nurse path
#
#   The captain confided in Miss Marsh last night, and she comes for him at
#   first light. After they take stock, he is offered a choice that is really
#   no choice at all:
#     - Leave at once: Miss Marsh cannot face the road on foot and admits she
#       is unwell, so the captain yields and they go to ground after all.
#     - Go to ground: they hide in the butler's attic room directly.
#   Either way they wait the morning out and come down in the afternoon.
# --------------------------------------------

label captain_day3_morning_nurse:

    $ change_room('bedroom_captain', irisout)

    """
    I sleep poorly, and only in patches.

    The house stays quiet through the night.

    A little before half past eight, I dress and sit on the edge of the bed.
    """

    play sound door_knock

    """
    There is a soft, quick knock at the door.
    """

    nurse """
    Captain. It's me.
    """

    """
    I unlock the door.

    Miss Marsh slips inside without a word and closes it behind her.

    She is pale, but quite collected.
    """

    captain """
    Miss Marsh.

    Are you all right?
    """

    nurse """
    I am, but there is something wrong with the house.
    """

    captain """
    What do you mean?
    """

    nurse """
    There are no staff. No fires lit. No breakfast laid.

    I have walked the dining room, the kitchen, the back corridor.

    Not a soul.
    """

    captain """
    So I was right, something strange is happening here.

    Have you checked any of the other rooms?
    """

    nurse """
    No, I came straight to you.
    """

    captain """
    A sound choice.

    It might not be safe for you to just roam around the house.
    """

    nurse """
    I believe you are right.

    I was thinking we might hide for a while, at least until the police come.
    """

    captain """
    Right, the police.

    I do not know for sure they will come, Miss Marsh.

    There is a good chance they were never called in the first place.
    """

    nurse """
    Never called, but Lady Claythorn...

    Oh...
    """

    captain """
    Yes, if Lady Claythorn is behind this masquerade, and there is a very good chance that she is, there was no reason for her to call the police.

    We might wait here indefinitely.
    """

    nurse """
    What can we do then?
    """

    captain """
    I see two options: 
    
    First, we could search this place and try to make sense of what is happening.

    I have a gun, so I can protect myself.
    """

    nurse """
    I do not like the idea of roaming around the house, even with you to protect me.

    What is the second option?
    """

    captain """
    We could leave right away, on foot if we must.
    """

    nurse """
    On foot, Captain?
    """

    captain """
    I am afraid yes.

    Lady Claythorn and her staff most likely left with the motor car.

    It is a fairly long walk to the town, but it is still early, I am sure we can make it.
    """

    nurse """
    Oh, I am sure you could, Captain.

    Sadly I can't.
    """

    """
    She says it quietly, and I see now what I had been too preoccupied to mark before.

    The pallor that is not only fear.

    The careful way she holds herself.
    """

    nurse """
    I am not a healthy woman, Captain.

    There is a good chance my body will not hold for such a long journey.
    """

    captain """
    I see.
    """

    """
    I think her condition might be worse than her quiet behaviour shows.

    But if she does not want to tell me more, I will not press her.
    """

    captain """
    In that case, I believe the safer bet is for me to leave alone.

    And I should go as soon as possible then, this way there is a very good chance that I can come back for you before the end of the day.

    You could hide until then.
    """

    nurse """
    I see.

    If I am being honest, I do not like this, Captain.

    It feels extremely dangerous for me.
    """

    captain """
    I know and I am sorry, but I still believe it is our best chance.

    And if it can ease your mind, you can take this pistol.

    I try to always keep it on me, one never knows when one might need protection.

    Do you know how to use one?
    """

    nurse """
    I can manage, I believe.

    But I really hope I won't have to use it.
    """

    captain """
    You probably won't, just find a safe hidden place, close the door and do not open to anybody.

    It is safe to say that everyone is a suspect at this point.
    """

    nurse """
    You are right.

    I believe the attic is the best place to hide.

    It should be empty now.
    """

    captain """
    The attic, good idea.

    I have the butler's master key.

    Use it to open a room and hide in it.
    """

    """
    I hand her the key, I do not need it anymore anyway.
    """

    nurse """
    All right, I think I can manage that.

    Thank you, Captain.
    """

    captain """
    Great, in that case I see no reason to linger.

    I will go straight away and come back as soon as possible.

    Good luck, Miss Marsh.
    """

    nurse """
    Good luck, Captain.
    """

    $ change_room('entrance_hall', dissolve)

    """
    I do not waste time and go down fast to the entrance hall.

    It is still empty, so I make it outside.
    """

    call change_time(12, 00)

    $ change_room('forest_road', dissolve)
    
    """
    I take only my coat and what will fit in its pockets.

    The drive gives way to a rough road, and the road to open country between the trees.
    """

    $ play_music('danger')

    """
    I keep a solid pace for an hour, then, away to my right, I notice something.

    A shape that is the wrong colour for bark.

    And from that shape, I can spot the barrel of a rifle.

    I quickly grab for my own gun but come up empty.

    Miss Marsh has it.

    I am now defenceless.
    """

    play sound gun

    jump captain_ending_shot_fleeing

