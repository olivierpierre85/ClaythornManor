# Saturday Afternoon (No Hunt) — Test Plans

Amelia Baxter declines the hunt and stays at the manor with Rosalind Marsh. The
chapter has two map menus separated by a fixed luncheon scene with the nurse:

1. **Map 1** (60 min, pre-noon) — `condition_saturday_hunt_morning` is True.
   Bedroom Nurse appears as "Queen Alexandra" (busy). Exit options:
   "Wait for Rosalind Marsh in the Tea Room" (early-exit), "Take a nap" (early-exit).
2. **Tea-room scene** — fixed `psychic_day2_hunt_tea_room` label, runs
   `nurse_generic_menu_psychic` (60-min budget).
3. **Map 2** (60 + leftover + 90 min, post-noon) — `condition_saturday_hunt_morning`
   is False. Bedroom Nurse appears as "Go check on Rosalind Marsh" (blood scene).
   Exit option: "Wait until the others come back" (early-exit).

The chapter then jumps to `psychic_day2_evening`.

---

## setup_psychic_saturday_afternoon_no_hunt_1.json
**Path**: Map 1: Edward II Bedroom → enter (locked) → Wait for Rosalind. Tea:
nurse_generic full (weather + bg + heroic + manor, exhausting the 60-min budget).
Map 2: Wait until others.
- Covers `psychic_day2_no_hunt_bedroom_doctor`,
  `psychic_day2_no_hunt_bedroom_try_enter` enter branch,
  `psychic_day2_no_hunt_default_room_locked`, `psychic_day2_hunt_tea_room`,
  `nurse_generic_weather_saturday_morning`, `nurse_generic_background_psychic`,
  `nurse_generic_heroic_act_psychic`, `nurse_generic_manor`,
  `psychic_day2_no_hunt_cancel`.

---

## setup_psychic_saturday_afternoon_no_hunt_2.json
**Path**: Map 1: Doctor (no_enter) → Drunk (enter, finds the messy room) → Wait
for Rosalind. Tea: nurse exit. Map 2: Garden (30) → Billiard → Dining →
Entrance Hall → Wait until others.
- Covers `psychic_day2_no_hunt_default_room_no_enter`,
  `psychic_day2_no_hunt_bedroom_drunk_enter`, `psychic_garden_default`,
  `psychic_billiard_room_default`, `psychic_dining_room_default`,
  `psychic_entrance_hall_default`.

---

## setup_psychic_saturday_afternoon_no_hunt_3.json
**Path**: Map 1: Queen Alexandra (nurse busy) → Captain (no_enter) → Host
(no_enter) → Wait for Rosalind. Tea: nurse_generic guests sub-menu (Manning +
Lady Claythorn). Map 2: Go check on Rosalind Marsh → Insist (unlocks
`nurse_sick`) → Richard III Bedroom → Wait until others.
- Covers `psychic_day2_no_hunt_bedroom_nurse_busy`,
  `psychic_day2_no_hunt_bedroom_captain`, `psychic_day2_no_hunt_bedroom_host`,
  `nurse_generic_other_guests_saturday_morning` + sub-menu,
  `nurse_generic_drunk_saturday_morning`, `nurse_generic_host_saturday`,
  `psychic_day2_no_hunt_bedroom_nurse_blood` + insist branch
  (`psychic_day2_no_hunt_bedroom_nurse_insist`), `psychic_day2_bedroom_broken`.

---

## setup_psychic_saturday_afternoon_no_hunt_4.json
**Path**: Map 1: Storage Room (60-min attic visit, unlocks `visited_attic`).
Tea: nurse exit. Map 2: Kitchen (downstairs hides others) → Library
(`look_for_lord_failed` since attic_visited and not lord_name) → Wait until
others.
- Covers `psychic_day2_no_hunt_attic_default` → `psychic_attic_default`,
  `psychic_day2_no_hunt_downstairs_default` → `psychic_downstairs_default`,
  `psychic_library_look_for_lord_failed`.

---

## setup_psychic_saturday_afternoon_no_hunt_5.json
**Path**: Map 1: Storage Room (attic, unlocks `visited_attic`). Tea: nurse exit.
Map 2: Portrait Gallery (`look_for_lord`, unlocks `lord_name`) → Library
(`look_for_lord_succeed`, unlocks `lord_age`) → Return to the Attic
(`psychic_attic_return` → "back down"). Wait until others.
- Covers the full lord-of-the-manor arc on Day 2: portrait look-up, library
  succeed (first-time "page turning" branch), and the return-to-attic menu's
  safe back-down choice.

---

## setup_psychic_saturday_afternoon_no_hunt_6.json
**Checkpoint**: thread `visited_attic` pre-unlocked, `attic_visited=True`.  
**Path**: Map 1: Storage Room (`psychic_day2_no_hunt_attic_return_too_soon`,
because `visited_attic` and not `lord_age`) → Wait for Rosalind. Tea: nurse
exit. Map 2: Go check on Rosalind Marsh → Do not push her further (ignore
branch). Wait until others.
- Covers `psychic_day2_no_hunt_attic_return_too_soon` →
  `psychic_attic_return_too_soon` and the
  `psychic_day2_no_hunt_bedroom_nurse_ignore` branch.

---

## setup_psychic_saturday_afternoon_no_hunt_7.json
**Path**: Map 1: Take a nap (early-exit, runs `psychic_day2_no_hunt_cancel`).
Tea: nurse exit. Map 2: Wait until others.
- Covers the "Take a nap" Map 1 exit option.
