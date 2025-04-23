label init_broken:

    # call broken_config_map
    
    # call broken_config_menu
    
    python:
        broken_name = "Thomas Moody"
        
        broken_init_variables = {
        }

        broken_extra_information = CharacterDescriptionHiddenList([
            CharacterInformation(0, "mask", "injured at the start of the war, he is now what people call a 'Gueule Cassée' or broken face"),
            CharacterInformation(0, "age", "27-year-old", is_important = True),
            CharacterInformation(0, "background", "a fancy house as a boot boy before graduating to footman.There he learned how to behave among the rich and wealthy", is_important = True),   
            CharacterInformation(0, "job", "a car mechanic", is_important = True),         
            CharacterInformation(0, "heroic_act", "the act of bravery that led to his injuries is what made Lady Claythorn invite him to the Manor", is_important = True),   
            CharacterInformation(0, "city", "Liverpool", is_important = True),         
            CharacterInformation(0, "shy", "married, perhaps because his condition has rendered him rather shy towards the fairer sex", is_important = True),   
            CharacterInformation(0, "lie", "entirely true, except for two small details: his name, which he stole from his deceased friend and real war hero, and his injuries, which are faked to give him a reason to hide his real face, should any acquaintance of the real Thomas Moody happen to be at the Manor", is_important = True),   
            ], broken_name
        )

        # broken_description_full = """
        # Thomas Moody is a 27-year-old working-class fellow. Born in Liverpool, he started working in a fancy house as a boot boy before graduating to footman.
        # There he learned how to behave among the rich and wealthy.
        # His life took a dramatic turn when he was called to serve during the Great War. Badly injured at the Somme at the start of the war, he is now what people call a 'Gueule Cassée' or broken face. However, the silver lining is that the act of bravery that led to his injuries is what made Lady Claythorn invite him to the Manor.
        # He is not married, perhaps because his condition has rendered him rather shy towards the fairer sex. 
        # After the war, he managed to find a job as a car mechanic.
        # Well, that story is almost entirely true, except for two small details: his name, which he stole from his deceased friend and real war hero, and his injuries, which are faked to give him a reason to hide his real face, should any acquaintance of the real Thomas Moody happen to be at the Manor.
        # """
        broken_description = """
        Thomas Moody is a <info:age> working-class fellow. Born in <info:city>, he started working in <info:background>.
        His life took a dramatic turn when he was called to serve during the Great War. Badly <info:mask>. However, the silver lining is that <info:heroic_act>.
        After the war, he managed to find a job as <info:job>. 
        He is not <info:shy>. 
        Well, that story is almost <info:lie>.
        """

        broken_details  = CharacterDetails(
            text_id = "broken", 
            locked = True,
            know_real_name = True,
            real_name = broken_name,
            nickname = "The Broken Face",
            description_short = "Masked Man",
            description_long = broken_description,
            description_hidden = broken_extra_information,
            important_choices = CharacterInformationList([]),
            endings = CharacterInformationList([]),
            observations = CharacterInformationList([]),
            objects = CharacterInformationList([]),
            progress = [],
        )
        broken = Character("broken_details.get_name()", image="broken", dynamic=True)
    
    return