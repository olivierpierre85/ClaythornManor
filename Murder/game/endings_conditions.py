# Ending conditions hardcoded for Testing (needed to create all possible checkpoints)

# LAD
def cond_lad_killed_by_whisky(toggles):
    return toggles.get('whisky', False) and not toggles.get('day1_drunk', False)

def cond_lad_killed_gunned_down(toggles):
    return toggles.get('abandoned_psychic', False) and toggles.get('gun', False) and not toggles.get('protect_food', False)

def cond_lad_killed_poisoned(toggles):
    return not toggles.get('abandoned_psychic', False) and not toggles.get('protect_food', False)

def cond_lad_killed_by_fall(toggles):
    return not toggles.get('abandoned_psychic', False) and toggles.get('protect_food', False)

def cond_lad_escape(toggles):
    return toggles.get('abandoned_psychic', False) and not toggles.get('gun', False) and not toggles.get('protect_food', False)

# Create the conditions dictionary.
CONDITIONS_DICT = {
    "lad_deathbed": cond_lad_killed_by_whisky,
    "lad_gunned_down": cond_lad_killed_gunned_down,
    "lad_poisoned": cond_lad_killed_poisoned,
    "lad_fell": cond_lad_killed_by_fall,
    "lad_escape": cond_lad_escape,
    # "psychic_fell": cond_psychic_fell,
    # "psychic_burned": cond_psychic_burned,
    # "psychic_shot": cond_psychic_burned,
    # "psychic_escape": cond_psychic_burned,
}