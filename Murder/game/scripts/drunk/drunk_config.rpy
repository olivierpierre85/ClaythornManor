label init_drunk:

    call drunk_config_progress

    call drunk_config_menu

    python:
        drunk_name = "Samuel Manning"

        drunk_init_variables = {
            # Generic Menus
            "day2_evening_think_menu" : drunk_day2_evening_menu_think,

            # Friday: every glass he empties. The sherry in the tea room and
            # the wine at dinner are the story's, the rest are his.
            "day1_drinks" : 0,

            # Saturday evening: which topics he has thought through
            "day2_evening_topics" : [],

            # Sunday afternoon: whether the boy has been carried off before
            # the butler asks about the lawyer upstairs
            "day3_afternoon_confession_heard" : False,
        }

        drunk_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                1, "raided_bar",
                "You carried every bottle worth the name up from the billiard room on the first night",
                content_negative="You left the billiard room bar alone on the first night",
                image_file="whisky",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
            CharacterInformation(
                2, "day1_drink",
                "You read the letter, and drank until it went away",
                content_negative="You read the letter, and put the bottle down",
                image_file="drunk",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning', 'saturday_afternoon'],
            ),
            CharacterInformation(
                3, "watered_flask",
                "You filled your flask with water and a finger of whisky for the smell, and played the drunk all day",
                content_negative="You took a full flask of whisky into the woods",
                image_file="whisky",   # TODO proper image, a hip flask under a tap
                chapters=['saturday_morning'],
                relevant_chapters=['saturday_morning', 'saturday_afternoon'],
            ),
            CharacterInformation(
                4, "shot_doctor",
                "You fired at Doctor Baldwin through the bracken and called it a rabbit",
                content_negative="You lowered the rifle and let Doctor Baldwin walk on",
                image_file="hunting_rifle",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening'],
            ),
            CharacterInformation(
                5, "understood",
                "You sat with the whole weekend behind a locked door and worked out what it was",
                content_negative="You never put the weekend together",
                image_file="murder_board",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_afternoon'],
            ),
            CharacterInformation(
                6, "played_dead",
                "You painted your throat with port, made a ruin of the bed, and lay down to be found",
                content_negative="You did not play dead",
                image_file="throat_cut",   # TODO proper image, a razor and a port bottle on the washstand
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning', 'sunday_afternoon'],
            ),
            CharacterInformation(
                7, "swapped_back",
                "You rang the gong, and put the two plates back where Miss Marsh found them",
                content_negative="You watched Miss Marsh move the plates, and let them lie",
                image_file="swapping_of_plates",
                chapters=['sunday_afternoon'],
                relevant_chapters=['sunday_afternoon', 'end'],
            ),
        ])

        drunk_observations = CharacterObservationList([
            CharacterInformation(
                1, "phone_call",
                "Lady Claythorn's telephone call to the police had no questions in it",
                content_negative="You did not think about the telephone call",
                image_file="phone",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_afternoon'],
            ),
            CharacterInformation(
                2, "butler_face",
                "You placed the butler's face. You have seen him in the dock",
                content_negative="You did not place the butler's face",
                image_file="butler",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_afternoon'],
            ),
        ])

        drunk_objects = CharacterObjectList([
            CharacterInformation(
                1, "port",
                "A bottle of port, put by in your room on the first night",
                content_negative="You have no port in your room",
                image_file="whisky",   # TODO proper image, a bottle of port
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening', 'sunday_morning'],
            ),
        ])

        drunk_endings = CharacterEndingList([
            CharacterInformation(1, "despair",
                "You shot a man for a rabbit, and it was one thing too many",
                image_file="hunting_rifle",
                is_intuition=True,
                chapters=['saturday_afternoon']),
            CharacterInformation(2, "spared",
                "You lowered the rifle, and somebody with a key finished the night for you",
                image_file="deathbed",
                chapters=['saturday_afternoon']),
            CharacterInformation(3, "throat_cut",
                "You drank what was left, and cut your own throat. Nobody came in the night. Nobody needed to",
                image_file="throat_cut",
                chapters=['saturday_evening']),
            CharacterInformation(4, "silenced",
                "You told the whole house there was a killer among them, and one of them heard you",
                image_file="butler_key",
                chapters=['saturday_evening']),
            CharacterInformation(5, "found_out",
                "The Captain did not check the bed. The butler did",
                image_file="gun_firing",
                chapters=['sunday_afternoon']),
            CharacterInformation(6, "survived",
                "You lay dead for a day, and walked out of Claythorn Manor on your own two feet",
                image_file="escape_poor",
                chapters=['sunday_afternoon']),
        ])

        drunk_extra_information = CharacterDescriptionHiddenList([
            # CharacterInformation(0, "background", "???"),
            CharacterInformation(1, "status", "prominent family", unlock_chapters=[('host', 'friday_evening'), ('drunk', 'friday_afternoon')]),
            CharacterInformation(2, "age", "55-year-old ", unlock_chapters=[('drunk', 'friday_afternoon')]),
            CharacterInformation(2, "wife", "the untimely death of his wife. Still young and healthy, she would never have died if the doctor responsible for her operation hadn't been so high on opioids", is_important = True, unlock_chapters=[('doctor', 'saturday_afternoon'), ('broken', 'saturday_afternoon'), ('drunk', 'friday_evening'), ('drunk', 'saturday_morning')]), # Confess to Doctor, to Moody at the hunt, and the letter in his own room (read on Friday, or again hungover on Saturday)
            CharacterInformation(3, "addict", "an addiction of his own. He started drinking regularly to numb the pain. It got worse and worse until he was no longer able", is_important = True, unlock_chapters=[('broken', 'friday_evening'), ('captain', 'friday_evening'), ('doctor', 'friday_evening'), ('lad', 'friday_evening'), ('host', 'friday_evening'), ('drunk', 'friday_afternoon')]), # Everyone
            CharacterInformation(60, "job", "lawyer, losing cases he should have won and disparaging his clients", is_important = True, unlock_chapters=[('host', 'friday_evening'), ('drunk', 'friday_afternoon')]), # Confess to Broken, and to the Host at the Friday dinner
            CharacterInformation(60, "heroic_act", "have left him; only the poorest and the most desperate would ever hire him. He assumes that this choice of clients has made him look like a fervent defender of the poor in the eyes of Lady Claythorn, hence his invitation", is_important = True, unlock_chapters=[('host', 'friday_evening'), ('drunk', 'friday_afternoon')]), # Confess to Broken, and to the Host at the Friday dinner
            CharacterInformation(60, "lie", "he can sober up, or at least act sober enough when the situation demands it. He has also become quite good at feigning drunkenness to avoid unpleasant situations", is_important = True, unlock_chapters=[('doctor', 'saturday_afternoon'), ('host', 'friday_evening'), ('host', 'sunday_afternoon'), ('drunk', 'saturday_morning')]), # Confess to Doctor - the Host catches the act at dinner, and hears it from him on the Sunday - the watered flask
            CharacterInformation(60, "food", "his palate. He can tell how a sauce was made from a single mouthful, and he speaks of a kitchen like a man who grew up beside one", is_important = True, unlock_chapters=[('host', 'friday_evening'), ('drunk', 'friday_evening')]), # He praises the sole at the Host's dinner, stone cold sober
            CharacterInformation(70, "faked_death", "he can play dead as well as drunk. He lay a whole day in his bed at Claythorn Manor with his throat painted in port, and nobody came close enough to look twice", is_important = True, unlock_chapters=[('host', 'sunday_afternoon'), ('drunk', 'sunday_morning')]), # He tells the Host himself, in the dining room, once she has come down from the attic and found him
            # Not needed to unlock him: the one thing he learns about himself in his own story
            CharacterInformation(80, "lost_case", "the woman he was too drunk to defend, years ago, over a break-in at an orphanage. She was sent down for it, and she remembered him", unlock_chapters=[('drunk', 'sunday_afternoon')]),
            ], drunk_name
        )
        drunk_description = """
        A <info:age> gentleman, raised in a <info:status>, he hasn't been the same since <info:wife>.
        Ironically, the ordeal drove Samuel Manning to <info:addict> to perform his duties as a <info:job>.
        Now, almost all of them <info:heroic_act>.
        The one pleasure the drink has never taken from him is <info:food>.
        His particular situation has given him certain skills: for one, <info:lie>.
        It turns out <info:faked_death>.
        What he only learnt at the very end is that he was not invited by mistake. One of the guests was <info:lost_case>.
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
            real_name = drunk_name,
            nickname = "The Drunk",
            description_short = "Drunk Man",
            description_long = drunk_description,
            description_hidden = drunk_extra_information,
            important_choices = drunk_important_choices,
            endings = drunk_endings,
            observations = drunk_observations,
            objects = drunk_objects,
            progress = drunk_progress,
            saved_variables = copy.deepcopy(drunk_init_variables),
            test_checkpoints = drunk_test_checkpoints,
        )
        drunk = Character("drunk_details.get_name()", image="drunk", dynamic=True)

    return
