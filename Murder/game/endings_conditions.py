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

def cond_psychic_fell(toggles):
    return toggles.get('visited_attic', False) and toggles.get('lord_name', False) and toggles.get('lord_age', False)

def cond_psychic_bludgeoned(toggles):
    return toggles.get('silverware', False) and toggles.get('nurse_sick', False)

def cond_psychic_burned(toggles):
    return toggles.get('steal_gun', False) and not toggles.get('leave_manor', False)

def cond_psychic_shot(toggles):
    return not toggles.get('steal_gun', False) and not toggles.get('leave_manor', False)

def cond_psychic_escape(toggles):
    return toggles.get('leave_manor', False) and not toggles.get('steal_gun', False)

def cond_doctor_overdose(toggles):
    return not toggles.get('flirt', False) and not toggles.get('book_opium', False) and not toggles.get('book_mystery', False)

def cond_doctor_shot_by_drunk(toggles):
    return not toggles.get('drunk_letter', False)

def cond_doctor_burned(toggles):
    return not toggles.get('drunk_letter', False)

def cond_doctor_throat_cut(toggles):
    return not toggles.get('trust_captain', False) and not toggles.get('trust_nurse', False)


# Create the conditions dictionary.
CONDITIONS_DICT = {
    "lad_deathbed": cond_lad_killed_by_whisky,
    "lad_gunned_down": cond_lad_killed_gunned_down,
    "lad_poisoned": cond_lad_killed_poisoned,
    "lad_fell": cond_lad_killed_by_fall,
    "lad_escape": cond_lad_escape,

    "psychic_fell": cond_psychic_fell,
    "psychic_bludgeoned": cond_psychic_bludgeoned,
    "psychic_burned": cond_psychic_burned,
    "psychic_shot": cond_psychic_shot,
    "psychic_escape": cond_psychic_escape,
    
    "doctor_overdose": cond_doctor_overdose,
    "doctor_shot_by_drunk": cond_doctor_shot_by_drunk,
    "doctor_burned": cond_doctor_burned,
    "doctor_throat_cut": cond_doctor_throat_cut
}