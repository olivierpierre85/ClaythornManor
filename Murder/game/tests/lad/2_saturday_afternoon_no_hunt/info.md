# Saturday Afternoon (No Hunt) — Test Plans

Ted stays inside while the others go hunting. He can explore the manor freely,
visit the tea room with Amelia Baxter and Rosalind Marsh, and investigate bedrooms.

---

## setup_lad_saturday_afternoon_no_hunt_1.json
**Checkpoint**: downstairs_1=False  
**Path**: Minimal — Ted takes a nap immediately.  
Covers intro narration and `lad_day2_no_hunt_cancel`.

---

## setup_lad_saturday_afternoon_no_hunt_2.json
**Checkpoint**: downstairs_1=False  
**Path**: Kitchen → Library → Tea Room → Broken's bedroom  
- Kitchen triggers first downstairs encounter: maid stops Ted, sets `has_met_maid=True`, unlocks `downstairs_1`.
- Library: first visit (education description unlock).
- Tea Room (first visit): `has_met_maid=True` so Ted mentions "the girl from downstairs". Nurse leaves after lunch. Calls `psychic_generic` (cancelled immediately).
- Richard III Bedroom: Ted investigates Thomas Moody's room, finds the green liquid on the nightstand. Unlocks `green_liquid`. (`day2_breakfast_follow=False` branch.)

---

## setup_lad_saturday_afternoon_no_hunt_3.json
**Checkpoint**: downstairs_1=True, has_met_maid=True  
**Path**: Nurse bedroom → Captain bedroom (enter) → Drunk bedroom (enter) → Kitchen → Nap  
- Nurse bedroom (before tea room): knock, no answer, try-enter menu → choose not to enter.
- Captain bedroom: Ted enters (explores, finds a gun in the drawer).
- Drunk bedroom: Ted enters, finds the burned letter. Unlocks `burned_letter`.
- Kitchen: second downstairs attempt — maid stops Ted again, unlocks `downstairs_2`.
- Nap to end the chapter.
