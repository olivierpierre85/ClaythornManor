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

---

## setup_lad_saturday_afternoon_no_hunt_4.json
**Checkpoint**: downstairs_1=True, has_met_maid=True, day2_breakfast_follow=True,
day2_nohunt_has_visited_tea_room=True  
**Path**: Nurse busy → Psychic try-enter (locked) → Host try-enter (locked) → Broken back-visit
→ Garden → Nap.
- Covers `lad_day2_no_hunt_bedroom_nurse_busy` (post-tea-room nurse visit).
- Covers `lad_day2_no_hunt_default_room_locked` (the "I try to push the door open. It's
  locked." line shared by every locked bedroom).
- Covers the broken bedroom back-visit branch (`day2_breakfast_follow=True`).
- Covers `lad_garden_default` via the no-hunt Garden choice.

---

## setup_lad_saturday_afternoon_no_hunt_5.json
**Checkpoint**: library_visited=True, portrait_gallery_visited=True (simulates a prior visit
from Day 1 evening so the back-visit branches fire).  
**Path**: Tea Room first (no kitchen visit, so `has_met_maid=False`) → Library (back-visit)
→ Portrait Gallery (back-visit) → Billiard Room → Dining Room → Entrance Hall → Nap.
- Covers the tea room else-branch (`Aren't they all out on the hunt?`).
- Covers `lad_library_default` second-visit dialogue.
- Covers `lad_portrait_gallery_default` second-visit dialogue.
- Covers `lad_billiard_room_default`, `lad_dining_room_default`, `lad_entrance_hall_default`.

---

## setup_lad_saturday_afternoon_no_hunt_6.json
**Checkpoint**: downstairs_1=True, has_met_maid=True  
**Path**: Tea Room (cancel psychic_generic) → Tea Room back-visit (cancel psychic_generic) → Nap.
- Covers `lad_day2_hunt_tea_room_return` — the "Go back to the Tea Room" map option that only
  appears after `day2_nohunt_has_visited_tea_room` has been set by the first visit.
