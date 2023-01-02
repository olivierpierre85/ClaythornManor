label psychic_introduction:

    $ psychic_details.add_checkpoint("psychic_introduction") 
    
    call change_time(17,00, 'Evening', 'Friday')

    scene train_inside

    play sound train_moving loop

    $ play_music('chill')

    """
    I still can't believe I had to book the train ticket myself.

    The least they could have done 
    """


    play sound train_stopping

    scene train_station

    pause 5.0
    
    "As I step off the train, a man approaches me."

    footman "Welcome sir. Are you by any chance, heading to Claythorn Manor ?"

    psychic "Yes indeed"