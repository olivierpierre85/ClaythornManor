label nurse_day3_afternoon:

    call change_time(14,00, 'Afternoon', 'Sunday', hide_minutes = True, chapter='sunday_afternoon')
    
    $ change_room("main_hall")

    """
    We need to leave. Now.
    
    The Captain is trying to organize a departure.
    """
    
    if nurse_details.threads.is_unlocked('drugged_guest'):
        """
        I regret giving that sedative to Mr. Moody. It might have complicated things.
        
        Did I kill him? No, his heavy drinking did that. I just... helped him rest.
        """
        
    """
    The stress is getting to me. My chest burns.
    """
    
    if nurse_details.threads.is_unlocked('stole_item'):
        """
        I clutch the silver spoon. It feels foolish now. 
        """
        
    menu:
        "Try to escape on foot":
             """
             I can make it to the village. I have walked further than this in the war.
             """
             $ nurse_details.threads.unlock("escaped")
             jump nurse_ending_managed

        "Wait for help (Too weak)":
             """
             I... I cannot make it.
             
             I urge them to go on without me.
             """
             $ nurse_details.threads.unlock("succumbed")
             jump nurse_ending_managed

label nurse_ending_managed:
    
    if nurse_details.threads.is_unlocked('escaped'):
        
        $ change_room("manor_exterior")
        
        """
        I walk. And walk. 
        
        Pain is an old friend. I welcome it.
        
        Finally, the village lights.
        
        I survived. But the Manor... it stays with me.
        """
        
        # Trigger ending screen
        call ending_screen(nurse_details, "escaped")
        
    else:
        
        $ change_room("bedroom_nurse")
        
        """
        I lie back on the bed.
        
        It is peaceful here, now that the ghosts are quiet.
        
        I close my eyes. Just for a moment.
        """
        
        call ending_screen(nurse_details, "succumbed")
        
    return
