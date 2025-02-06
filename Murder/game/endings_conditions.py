# Ending conditions hardcoded for Testing (needed to create all possible checkpoints)

# LAD
def cond_killed_by_whisky(toggles):
    return toggles.get('whisky', False) and not toggles.get('day1_drunk', False)

# Create the conditions dictionary.
CONDITIONS_DICT = {
    "poisoned": cond_killed_by_whisky,
    # "flooded_basement": cond_flooded_basement,
    # add more conditions as needed...
}