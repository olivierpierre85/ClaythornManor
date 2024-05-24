label init_drunk:

    # call drunk_config_map
    
    # call drunk_config_menu
    
    python:
        drunk_name = "Samuel Manning"
        
        drunk_init_variables = {
        }

        drunk_extra_information = CharacterDescriptionHiddenList([
            CharacterInformation(0, "background", "???"), 
            CharacterInformation(1, "status", "prominent family"),
            CharacterInformation(2, "age", "55-year-old "),
            CharacterInformation(2, "wife", "the untimely death of his wife. Still young and healthy, she would never have died if the doctor responsible for her operation hadn't been so high on opioids"),
            CharacterInformation(3, "addict", "an addiction of his own. He started drinking regularly to numb the pain. It got worse and worse until he was no longer able to perform his duties as", is_important = True),
            CharacterInformation(60, "job", "lawyer, losing cases he should have won and disparaging his clients", is_important = True),
            CharacterInformation(60, "heroic_act", "have left him; only the poorest and the most desperate would ever hire him. He assumes that this choice of clients has made him look like a fervent defender of the poor in the eyes of Lady Claythorn, hence his invitation", is_important = True),
            CharacterInformation(60, "lie", "he can sober up, or at least act sober enough when the situation demands it. He has also become quite good at feigning drunkenness to avoid unpleasant situations", is_important = True),
            ], drunk_name
        )
        drunk_description = """
        A <info:age> gentleman, raised in a <info:status>, he hasn't been the same since <info:wife>.
        Ironically, the ordeal drove Samuel Manning to <info:addict> a <info:job>.
        Now, almost all of them <info:heroic_act>.
        His particular situation has given him certain skills: for one, <info:lie>.
        """


        # drunk_description_full = """
        # An older gentleman, raised in a prominent family, he hasn't been the same since the untimely death of his wife.
        # Still young and healthy, she would never have died if the doctor responsible for her operation hadn't been so high on opioids.
        # Ironically, the ordeal drove Samuel Manning to an addiction of his own. He started drinking regularly to numb the pain. It got worse and worse until he was no longer able to perform his duties as a lawyer, losing cases he should have won and disparaging his clients.
        # Now, almost all of them have left him; only the poorest and the most desperate would ever hire him. He assumes that this choice of clients has made him look like a fervent defender of the poor in the eyes of Lady Claythorn, hence his invitation.
        # His particular situation has given him certain skills: for one, he can sober up, or at least act sober enough when the situation demands it. He has also become rather good at feigning drunkenness to avoid unpleasant situations.
        # """



        drunk_details  = CharacterDetails(
            text_id = "drunk", 
            locked = True,
            know_real_name = True,
            real_name = drunk_name,
            nickname = "The Drunk",
            description_short = "Drunk Man",
            description_long = drunk_description,
            description_hidden = drunk_extra_information,
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            intuitions = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
        )
        drunk = Character("drunk_details.get_name()", image="drunk", dynamic=True)

    return