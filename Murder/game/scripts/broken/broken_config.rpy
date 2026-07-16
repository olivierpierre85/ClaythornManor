label init_broken:

    # call broken_config_map

    call broken_config_progress

    call broken_config_menu

    call broken_day1_evening_map_menu

    call broken_day2_evening_map_menu

    python:
        broken_name = "Thomas Moody"

        broken_init_variables = {
            # Generic Menus
            "host_generic_menu": host_generic_menu_broken,
            "doctor_generic_menu" : doctor_generic_menu_broken,
            "drunk_generic_menu" : drunk_generic_menu_broken,

            # MAP Menus
            "day1_evening_map_menu" : broken_day1_evening_map_menu,
            "day2_evening_map_menu" : broken_day2_evening_map_menu,

            # Evening day 1
            "day1_evening_bedroom_refusals" : 0,
            "day1_evening_billiard_room_visited" : False,
            "day1_evening_billiard_room_butler_approached" : False,
            "day1_evening_downstairs_refused" : False,
            "day1_evening_wearing_livery" : False,

            # Evening day 2 (the night map and the gathering)
            "day2_evening_billiard_room_visited" : False,
            "day2_evening_billiard_captain_approached" : False,
            "day2_evening_gong_idea" : False,
            "day2_evening_no_pretence" : False,
            "day2_evening_staff_oddities" : 0,
        }

        broken_important_choices = CharacterImportantChoiceList([
            CharacterInformation(
                0, "drink_good_whisky",
                "You drank the special whisky on the first night",
                content_negative="You left the special whisky alone on the first night",
                image_file="whisky",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_morning'],
            ),
            CharacterInformation(
                0, "talked_to_maid",
                "You questioned the maid in the kitchen about the butler",
                content_negative="You didn't questioned the maid in the kitchen",
                image_file="talked_to_maid",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
            CharacterInformation(
                0, "manning_partner",
                "You partnered with Samuel Manning, who pledged to follow your lead",
                content_negative="You didn't partner with Samuel Manning",
                image_file="drunk",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                0, "gather_everyone",
                "You rang the dinner gong, gathered the household, and arranged a watch for the night",
                content_negative="You didn't gather the others to keep watch through the night",
                image_file="lord",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(
                0, "left_together",
                "You laid the whole truth before the others and convinced everyone to leave together",
                content_negative="You could not convince the others, and set out with only the Captain",
                image_file="leave_manor",
                chapters=['sunday_morning'],
                relevant_chapters=['sunday_morning', 'sunday_afternoon'],
            ),
        ])

        broken_observations = CharacterObservationList([
            CharacterInformation(1, "found_livery",
                "You found a footman's livery in the servant stair that lets you pass below stairs unseen",
                content_negative="You didn't find a footman's livery",
                image_file="footman_livery",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
            CharacterInformation(1, "host_lies",
                "You noticed Lady Claythorn is hiding something",
                content_negative="You didn't noticed Lady Claythorn is hiding something",
                image_file="host",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
            CharacterInformation(1, "doctor_boxer",
                "You learned Dr Baldwin served as a field surgeon in the Boxer Rebellion",
                content_negative="You didn't learn where Dr Baldwin served",
                image_file="doctor",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
            CharacterInformation(1, "butler_surprise",
                "You talked to the butler about the surprise",
                content_negative="You didn't talk to the butler about the surprise",
                image_file="butler",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening'],
            ),
            CharacterInformation(1, "drunk_letter",
                "Samuel Manning was sent a letter blaming Doctor Baldwin for his wife's death, just as you were turned against the Captain",
                content_negative="You didn't learn what was driving Samuel Manning",
                image_file="drunk_letter",
                chapters=['saturday_afternoon'],
                relevant_chapters=['saturday_afternoon', 'saturday_evening'],
            ),
            CharacterInformation(1, "phone_dead",
                "You tried the telephone in the entrance hall and found the line dead",
                content_negative="You didn't try the telephone in the entrance hall",
                image_file="phone",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
            CharacterInformation(1, "staff_missing",
                "You pieced together from the state of the servants' floor that the staff have deserted their posts and do not mean to return",
                content_negative="You didn't notice the staff had deserted their posts",
                image_file="staff_missing",
                chapters=['saturday_evening'],
                relevant_chapters=['saturday_evening', 'sunday_morning'],
            ),
        ])

        broken_objects = CharacterObjectList([
            CharacterInformation(1, "found_poison",
                "You took a bottle of rat poison from the scullery",
                content_negative="You didn't take a bottle of rat poison from the scullery",
                image_file="rat_poison",
                chapters=['friday_evening'],
                relevant_chapters=['friday_evening', 'saturday_evening'],
            ),
        ])

        broken_endings = CharacterEndingList([
            CharacterInformation(1, "deathbed", "You died in your sleep", image_file="deathbed", chapters=['saturday_morning']),
            CharacterInformation(1, "throat_cut", "Your throat was cut in your sleep", image_file="throat_cut", chapters=['saturday_morning']),
            CharacterInformation(1, "strangled", "Someone strangled you from behind in the woods", image_file="strangled_woods", chapters=['saturday_afternoon']),
            CharacterInformation(1, "shot", "The butler shot you down after you killed captain Sinha", image_file="hunting_rifle", chapters=['saturday_afternoon']),
            CharacterInformation(1, "shielded", "You threw yourself in front of Doctor Baldwin and took Manning's bullet in the western grove", image_file="hunting_rifle", chapters=['saturday_afternoon']),
            CharacterInformation(1, "poisoned", "You were poisoned at dinner along with every other guest", image_file="rat_poison", chapters=['saturday_evening']),
            CharacterInformation(1, "impaled", "You leapt from your window to escape the fire and were impaled on the iron fence below", image_file="fence", chapters=['saturday_evening']),
            CharacterInformation(2, "ambushed", "You and the Captain were shot down on the road to the village", image_file="shot_from_behind_i", is_intuition=True, chapters=['sunday_afternoon']),
            CharacterInformation(3, "walked_out", "You led everyone out of the manor together and reached the police station", image_file="leave_manor", chapters=['end']),
        ])

        broken_description_hidden = CharacterDescriptionHiddenList([
            CharacterInformation(0, "mask", "injured at the start of the war, he is now what people call a 'Gueule Cassée' or broken face"),
            CharacterInformation(0, "age", "43-year-old", is_important = True),
            CharacterInformation(0, "background", "a fancy house as a boot boy before graduating to footman. There he learned how to behave among the rich and wealthy", is_important = True),
            CharacterInformation(0, "tall", "above-average height", is_important = True),
            CharacterInformation(0, "job", "a car mechanic", is_important = True),
            CharacterInformation(0, "heroic_act", "that led to his injuries is what made Lady Claythorn invite him to the Manor", is_important = True),
            CharacterInformation(0, "city", "Liverpool", is_important = True),
            CharacterInformation(0, "shy", "married, perhaps because his condition has rendered him rather shy towards the opposite sex", is_important = True),
            CharacterInformation(0, "lie_mask", "however, a fiction - his face was never touched by the war", is_important = True),
            CharacterInformation(0, "lie_name", "'Thomas' is not his own. His friends call him 'Archie'", is_important = True),
            CharacterInformation(0, "lie_impostor", "not who he claims to be", is_important = True),
            ], broken_name
        )

        broken_description = """
        Thomas Moody is a <info:age> working-class fellow. Born in <info:city>, he started working in <info:background>. His <info:tall> helped him secure the post.
        His life took a dramatic turn when he was called to serve during the Great War. Badly <info:mask>. The act of bravery <info:heroic_act>.
        After the war, he managed to find a job as <info:job>. 
        He is not <info:shy>. 
        The wounds beneath that mask are, <info:lie_mask>.
        The name <info:lie_name>.
        And finally, the most important thing about him is that he is <info:lie_impostor>. 
        """
        # Well, that story is almost entirely true, except for two small details: his injuries are faked, and his name, as well as back story is not his own.  He borrowed it from his deceased friend and real war hero, in order to investigate the manor

        broken_details  = CharacterDetails(
            text_id = "broken", 
            locked = True,
            real_name = broken_name,
            nickname = "The Broken Face",
            description_short = "Masked Man",
            description_long = broken_description,
            description_hidden = broken_description_hidden,
            important_choices = broken_important_choices,
            endings = broken_endings,
            observations = broken_observations,
            objects = broken_objects,
            progress = broken_progress,
            test_checkpoints = broken_test_checkpoints,
            saved_variables = copy.deepcopy(broken_init_variables),
        )
        broken = Character("broken_details.get_name()", image="broken", dynamic=True)
    
    return