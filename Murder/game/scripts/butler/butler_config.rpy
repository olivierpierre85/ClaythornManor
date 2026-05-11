# Minimal butler config — placeholder character used only for the
# is_butler_visible preview in the progress screen. No story, no
# threads, no progress timeline, no endings.
label init_butler:

    python:
        butler_name = "The Butler"

        butler_init_variables = {}

        butler_details = CharacterDetails(
            text_id = "butler",
            locked = False,
            know_real_name = True,
            real_name = butler_name,
            nickname = "The Butler",
            description_short = "The Butler",
            description_long = "",
            description_hidden = CharacterDescriptionHiddenList([], butler_name),
            important_choices = CharacterImportantChoiceList([]),
            endings = CharacterEndingList([]),
            observations = CharacterObservationList([]),
            objects = CharacterObjectList([]),
            progress = [],
            saved_variables = copy.deepcopy(butler_init_variables),
        )

    return
