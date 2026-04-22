# Sunday Morning — Test Plans

Ted wakes to find the manor's staff and most guests have vanished. He explores with Amelia Baxter
until they regroup with Captain Sinha. Key branches: trust_psychic changes the opening scene
and the available time (135 vs 45 min); day2_drunk adds a groggy waking narration; the gun room
offers a take/don't-take choice; the billiard room triggers a drunk branch when both day1_drunk
and day2_drunk are unlocked; visiting the garage unlocks `seen_car`.

Captain Sinha can be found by visiting the entrance hall during the map, which sets
`day3_morning_captain_found=True` and unlocks "Go wait for Sushil" as the map's early exit.
All four files use this exit to close the map cleanly, then continue through the common ending
sequence (Manning's body, Nurse Marsh's empty room).

**Coverage gap**: `common_day3_morning_lad_psychic_tea_room_1` is called when the captain is NOT
found during the search (he hails the party from outside the tea room). This path requires the map
to time out without visiting the entrance hall, which cannot be driven by a clean early-exit
choice. It is covered when the psychic character's tests exercise the same common label.

---

## setup_lad_sunday_morning_1.json
**Checkpoint**: day2_drunk=False, trust_psychic=False  
**Time**: 45 min (starts at 09:30)  
**Path**: Garage (unlocks `seen_car`) → Gun Room (don't take gun) → Entrance Hall (captain found) → wait  
- Covers non-trust opening dialogue and `lad_day3_first_downstairs` first visit.  
- Gun room: `lad_day3_no_gun` branch.

---

## setup_lad_sunday_morning_2.json
**Checkpoint**: day2_drunk=True, trust_psychic=False (day1_drunk also pre-unlocked)  
**Time**: 45 min (starts at 09:30)  
**Path**: Billiard Room (day1_drunk + day2_drunk → unlocks `day3_drunk`) → Gun Room (take gun → unlocks `gun`) → Entrance Hall (captain found) → wait  
- Covers day2_drunk groggy waking narration.  
- Billiard room: both drunk-flag conditions True → `day3_drunk` unlock.  
- Gun room: `lad_day3_take_gun` branch.

---

## setup_lad_sunday_morning_3.json
**Checkpoint**: day2_drunk=False, trust_psychic=True  
**Time**: 135 min (starts at 07:30)  
**Path**: Richard III → Lady Claythorn's → Nurse's → Amelia's → Manning's → Captain's → Doctor's bedroom → Entrance Hall (captain found) → wait  
- Covers trust opening (`common_day3_morning_lad_psychic_journey`).  
- Exercises all bedroom visit labels.

---

## setup_lad_sunday_morning_4.json
**Checkpoint**: day2_drunk=True, trust_psychic=True  
**Time**: 135 min (starts at 07:30)  
**Path**: Garage (seen_car) → Billiard Room (non-drunk branch, day1_drunk not unlocked) → Kitchen → Scullery → Entrance Hall (captain found) → wait  
- Covers trust + day2_drunk combination (groggy waking + trust opening).  
- Billiard room: non-drunk branch (only day2_drunk unlocked, not day1_drunk).  
- Covers kitchen and scullery downstairs visits.
