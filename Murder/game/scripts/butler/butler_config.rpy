# Non-playable butler — the final character to unlock. He has no story,
# no progress timeline and no endings, but finishing the game requires
# discovering all the important information about him.
# He only appears in the progress screen once any of it has been
# discovered (see is_butler_visible() in characters.rpy).
label init_butler:

    python:
        butler_name = "The Butler"

        butler_init_variables = {}

        butler_extra_information = CharacterDescriptionHiddenList([
            # Unlocked after the death text of the captain 'burned' and
            # 'shot_butler' endings (same paths as the host 'not_guilty' info)
            CharacterInformation(0, "manages_weekend", "managing this entire weekend on behalf of someone else", is_important = True),
            # TODO unlock points for the items below are not written yet
            CharacterInformation(10, "poisoned_moody", "slipped the poison into Thomas Moody's flask", is_important = True),
            CharacterInformation(20, "took_valuables", "long gone, and the jewellery and silverware with him", is_important = True),
        ], butler_name)

        butler_description = """
        Discreet, punctual and ever-present, the butler appears to be the very model of his profession.
        But the manor is not his to serve - he is merely <info:manages_weekend>.
        It was he who <info:poisoned_moody>.
        And by the time anyone thought to look for him, he was <info:took_valuables>.
        """

        butler_details = CharacterDetails(
            text_id = "butler",
            locked = True,
            know_real_name = True,
            real_name = butler_name,
            nickname = "The Butler",
            description_short = "The Butler",
            description_long = butler_description,
            description_hidden = butler_extra_information,
            important_choices = CharacterImportantChoiceList([]),
            endings = CharacterEndingList([]),
            observations = CharacterObservationList([]),
            objects = CharacterObjectList([]),
            progress = [],
            saved_variables = copy.deepcopy(butler_init_variables),
        )

    return
