# Sunday Morning — Test Plans

Ted wakes to find the manor's staff and most guests have vanished. He explores with Amelia Baxter
until the map's time runs out. Key branches: trust_psychic changes the opening scene
and the available time (135 vs 45 min); day2_drunk adds a groggy waking narration; the gun room
offers a take/don't-take choice; the billiard room triggers a drunk branch when both day1_drunk
and day2_drunk are unlocked; visiting the garage unlocks `seen_car`.

The map has no early exit: it closes only when `time_left` reaches 0. The party then returns to
the entrance hall, where Ted calls out and Captain Sinha answers
(`common_day3_morning_entrance_hall_meeting`), and the three settle in the tea room for the
common ending sequence (Manning's body, Nurse Marsh's empty room). The entrance hall itself is
an ordinary, empty room during exploration. Each plan therefore lists enough room visits for
the total cost to exceed the time budget (most rooms 10 min, host/nurse bedrooms 20 min,
gun room 0 min plus a 10-min submenu choice).

---

## setup_lad_sunday_morning_1.json
**Checkpoint**: day2_drunk=False, trust_psychic=False  
**Time**: 45 min (starts at 09:30)  
**Path**: Garage (unlocks `seen_car`) → Gun Room (don't take gun) → Entrance Hall (empty) → Library → Dining Room (50 min, timeout)  
- Covers non-trust opening dialogue and `lad_day3_first_downstairs` first visit.  
- Gun room: `lad_day3_no_gun` branch.

---

## setup_lad_sunday_morning_2.json
**Checkpoint**: day2_drunk=True, trust_psychic=False (day1_drunk also pre-unlocked)  
**Time**: 45 min (starts at 09:30)  
**Path**: Billiard Room (day1_drunk + day2_drunk → unlocks `day3_drunk`) → Gun Room (take gun → unlocks `gun`) → Entrance Hall → Garden → Portrait Gallery (50 min, timeout)  
- Covers day2_drunk groggy waking narration.  
- Billiard room: both drunk-flag conditions True → `day3_drunk` unlock.  
- Gun room: `lad_day3_take_gun` branch.

---

## setup_lad_sunday_morning_3.json
**Checkpoint**: day2_drunk=False, trust_psychic=True  
**Time**: 135 min (starts at 07:30)  
**Path**: Richard III → Lady Claythorn's → Nurse's → Amelia's → Manning's → Captain's → Doctor's bedroom → Entrance Hall → Storage → Male Servants → Female Servants → Butler's Room (140 min, timeout)  
- Covers trust opening (`common_day3_morning_lad_psychic_journey`).  
- Exercises all bedroom visit labels and the attic rooms.

---

## setup_lad_sunday_morning_4.json
**Checkpoint**: day2_drunk=True, trust_psychic=True  
**Time**: 135 min (starts at 07:30)  
**Path**: Garage (seen_car) → Billiard Room (non-drunk branch, day1_drunk not unlocked) → Kitchen → Scullery → Library → Dining Room → Garden → Portrait Gallery → Tea room → William the Conqueror Bedroom → Storage → Male Servants → Female Servants → Entrance Hall (140 min, timeout)  
- Covers trust + day2_drunk combination (groggy waking + trust opening).  
- Billiard room: non-drunk branch (only day2_drunk unlocked, not day1_drunk).  
- Covers kitchen and scullery downstairs visits.

---

## setup_lad_sunday_morning_5.json
**Checkpoint**: day2_drunk=False, trust_psychic=True  
**Time**: 135 min (starts at 07:30)  
**Path**: Library → Dining Room → Garden → Portrait Gallery → Tea room → William the Conqueror Bedroom → Butler's Room → Storage → Kitchen → Scullery → Lady Claythorn's Bedroom → Female Servants → Entrance Hall (140 min, timeout)  
- Covers the first-floor common rooms, the tea room, and Ted's own bedroom on the trust path.
