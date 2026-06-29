# --------------------------------------------
#   Captain - Saturday Hunt - V2 (Moody alive)
#
#   Grouping:
#       - Captain + Lady Claythorn + Thomas Moody + butler
#       - Doctor + Drunk + Lad + footman
#
#   Linear path: Moody isolates the Captain after luncheon
#                 and shoots him in the woods.
#
#   The north-field hunt and the confrontation are both shared with the Broken
#   storyline:
#       - common_day2_hunt_north_field
#       - common_day2_hunt_captain_confrontation
# --------------------------------------------

label captain_day2_hunt_moody_alive:

    call common_day2_hunt_north_field

    call common_day2_hunt_captain_confrontation

    jump captain_ending_shot_in_woods
