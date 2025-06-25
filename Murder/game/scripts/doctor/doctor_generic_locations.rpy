label doctor_library_default:

    $ change_room('library')

    # if not doctor_details.saved_variables["library_visited"]:

    #     """
    #     It's a very nice library. But what am I doing here? 
        
    #     I can barely read.
    #     """

    #     $ doctor_details.description_hidden.unlock('education')

    #     """
    #     There is an open book on a small table.

    #     "A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain."

    #     Yeah, I'm not reading that.

    #     I should probably look elsewhere.
    #     """
    #     # TODO add info on BOOK???
    #     $ doctor_details.saved_variables["library_visited"] = True

    # else:

    #     """
    #     There is nothing different from the last time I was in here.

    #     No reason to look further.
    #     """

    return

label doctor_attic_default:

    $ change_room("attic_hallway")

    # if not doctor_details.saved_variables['attic_visited']:

    #     """
    #     I took the stairs to the attic.

    #     I'm not sure if I should be here.
    #     """

    #     $ doctor_details.saved_variables["attic_visited"] = True

    return

label doctor_downstairs_default:

    $ change_room("basement_stairs")

    # if not doctor_details.important_choices.is_unlocked('downstairs_1'):

    #     """
    #     I was on my way to the basement when a young maid stopped me.
    #     """

    #     maid """
    #     Hello Sir, may I help you?
    #     """

    #     lad """
    #     Oh, don't mind me. I'm just taking a look around.
    #     """

    #     maid """
    #     I'm sorry, but the basement is off-limits to guests.

    #     However, there are plenty of rooms upstairs that you can explore.
    #     """

    #     lad """
    #     Of course, thank you.
    #     """

    #     $ doctor_details.saved_variables["has_met_maid"] = True

    #     $ doctor_details.important_choices.unlock('downstairs_1')

    # elif doctor_details.important_choices.is_unlocked('downstairs_1'):

    #     """
    #     Let's see if I can check downstairs now.

    #     I walk down the stairs slowly, being very careful not to attract attention.

    #     But as I'm stepping down to the basement, the same woman stops me.
    #     """

    #     maid """
    #     You again, Sir? As I already told you, I'm afraid you're not allowed to be here.
    #     """

    #     lad """
    #     Of course, I was just lost. I'm terribly sorry.
    #     """

    #     maid """
    #     It's alright, don't worry about it, sir.
    #     """

    #     """
    #     I'd better be careful. If I'm caught here a third time, it will really start to look suspicious.
    #     """

    #     $ doctor_details.important_choices.unlock('downstairs_2')

    # elif doctor_details.important_choices.is_unlocked('downstairs_2'):

    #     """
    #     Maybe I'm pushing my luck, trying to go downstairs, but I feel like I have to go there.
    #     """

    #     maid """
    #     Mister Harring? I thought I made myself clear earlier.

    #     What are you trying to do here?

    #     You can't possibly make me believe that you got lost again?
    #     """

    #     call run_menu(
    #         TimedMenu("doctor_has_try_sneaking_downstairs", [
    #             # TimedMenuChoice("I know it sounds ridiculous, but I DID get lost again", 'doctor_downstairs_lost', 5, early_exit=True),
    #             TimedMenuChoice("Zzzzzz (Pretend you're sleepwalking)", 'doctor_downstairs_sleepwalk', 10, early_exit=True),
    #             TimedMenuChoice("Actually, I just wanted to talk to you (flirt your way out)", 'doctor_downstairs_flirt', 10, early_exit=True),
    #         ])
    #     )

    #     $ doctor_details.important_choices.unlock('downstairs_3')

    return



label doctor_garden_default:

    $ change_room('manor_garden')

    # """
    # A beautiful garden.

    # I wandered in it for a while, enjoying a relaxing walk.

    # But I didn't find anything of interest.
    # """

    return


label doctor_garage_default:

    call doctor_downstairs_default

    return


label doctor_tea_room_default:
    
    $ change_room('tea_room')
    
    # """
    # There is nobody here.

    # No need to stay any longer.
    # """

    return

label doctor_dining_room_default:
    
    $ change_room('dining_room')
    
    # """
    # The dining room is empty at the moment.
    
    # I shouldn't stay here.
    # """

    return

label doctor_billiard_room_default:
    
    $ change_room('billiard_room')
    
    # """
    # It's empty.

    # No need to stay here.
    # """

    return

label doctor_bedroom_default:


    return

label doctor_entrance_hall_default:
    
    $ change_room("great_hall")
    
    # """
    # It's certainly an impressive entrance hall.
    
    # Nobody is here.
    # """

    return

label doctor_portrait_gallery_default:
    
    $ change_room("portrait_gallery")

    # if not doctor_details.saved_variables["portrait_gallery_visited"]:
    
    #     """
    #     That's a creepy portrait gallery.

    #     I don't recognize anyone, so I guess these are people from the Claythorn family.
    #     """

    #     # TODO: Possibility to zoom in on specific members?

    #     $ doctor_details.saved_variables["portrait_gallery_visited"] = True
    
    # else:

    #     """
    #     Nothing new here.

    #     It still gives me a weird, creepy feeling.
    #     """

    return

# Downstairs
label doctor_kitchen_default:
    call doctor_downstairs_default
    return

label doctor_scullery_default:
    call doctor_downstairs_default
    return

label doctor_gun_room_default:
    call doctor_downstairs_default
    return

# Attic
label doctor_storage_default:

    call doctor_attic_default

    # """
    # I try to open the attic storage room, but it's closed.
    # """
    
    return

label doctor_females_room_default:

    call doctor_attic_default

    # """
    # I try to open the room, but it's closed.
    # """

    return

label doctor_males_room_default:

    call doctor_attic_default

    # """
    # I try to open the room, but it's closed.
    # """

    return

label doctor_butler_room_default:
    
    call doctor_attic_default

    # """
    # I try to open the room, but it's closed.
    # """

    return
