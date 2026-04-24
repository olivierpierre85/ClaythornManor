# Friday Evening — Test Plans

Amelia Baxter arrives at the manor, meets Ted Harring for drinks, then dines. After
dinner she retires to her room (Elizabeth I Bedroom) and has free time to explore
the manor via the map menu. Key branches: dinner partners (Sushil / Ted / no one),
billiard room (captain story, bar, doctor), and the Lord of the Manor arc (attic →
portrait → library).

---

## setup_psychic_friday_evening_1.json
**Path**: Drinks cancel → Dinner: Talk to Ted (lad_generic: background → heroic →
manor → age → room → exit) → Talk to Sushil (triggers
`captain_psychic_should_talk_to_captain_first`; captain_generic: background runs
before the dinner timer exhausts) → Map: Billiard room → Talk to Daniel Baldwin
(full `doctor_generic_menu_psychic` + `doctor_generic_other_guests_menu_psychic`)
→ Leave → Go to bed.
- Covers `psychic_day1_dinner_lad`, `psychic_day1_dinner_captain`,
  `captain_psychic_should_talk_to_captain_first`,
  `psychic_day1_evening_billiard_room` first-visit, `_doctor`, and most of
  `doctor_generic_menu_psychic`. The dinner exits mid-captain because Ted's full
  menu consumes most of the 90-minute dinner budget (File 7 covers the rest of
  captain_generic).

---

## setup_psychic_friday_evening_2.json
**Path**: Drinks cancel → Don't engage at dinner → Map: Tea room → Dining room →
Garden (bad weather narration) → Entrance Hall → Library (`psychic_library_default`,
attic not visited) → Portrait Gallery (`psychic_portrait_gallery_default`, attic not
visited) → Edward II Bedroom (`psychic_day1_evening_default_bedroom`) → George IV
Bedroom (`psychic_day1_evening_bedroom_drunk` special narration) → Kitchen
(`psychic_day1_evening_downstairs_default` hides the other basement rooms) → Go to
bed.
- Covers the first-floor walk, the default bedroom narration, the drunk-bedroom
  variant, and the "basement is off-limits" downstairs branch.

---

## setup_psychic_friday_evening_3.json
**Path**: Drinks cancel → Don't engage at dinner → Map: Library (default) → Storage
Room (`psychic_day1_evening_attic_default` unlocks `visited_attic` and hides the
other attic rooms) → Library (`psychic_library_look_for_lord_failed`, attic-visited
branch, sets `book_read`) → Portrait Gallery (`psychic_portrait_gallery_look_for_lord`,
attic-visited branch, unlocks `lord_name`).
- Covers the first attic visit with Lord Claythorn, the "already visited" else
  branch of `psychic_library_intro` (second library visit), and the portrait look-up
  that discovers his name.

---

## setup_psychic_friday_evening_4.json
**Path**: Drinks cancel → Don't engage at dinner → Map: Storage Room (attic, unlocks
`visited_attic`) → Portrait Gallery (look_for_lord, unlocks `lord_name`) → Library
(`psychic_library_look_for_lord_succeed` with `book_read=False` → calls
`psychic_library_look_for_lord` which sets `book_read=True` and unlocks `lord_age`).
- Covers the successful library look-up path (first-time "page turning" branch).

---

## setup_psychic_friday_evening_5.json
**Checkpoint**: threads `visited_attic`, `lord_name`, `lord_age` pre-unlocked;
saved variables `attic_visited=True`, `book_read=True`, `library_visited=True`,
`portrait_gallery_visited=True` pre-set.  
**Path**: Drinks cancel → Don't engage → Map: Portrait Gallery
(`psychic_portrait_gallery_look_for_lord` — already-visited else branch "paintings
remain unchanged") → Library (`psychic_library_look_for_lord_succeed` —
book_read=True branch "I turn back to the page") → Return to the Attic
(`psychic_attic_return` menu) → "On second thought, it is rather scary. Let's back
down" → Go to bed.
- Covers the repeat-visit branches for portrait and library, and the
  `psychic_attic_return` menu with the safe back-down choice (confronting the lord
  would trigger the `psychic_ending_lord` ending and is reserved for Saturday/Sunday
  tests).

---

## setup_psychic_friday_evening_6.json
**Path**: Drinks cancel → Don't engage at dinner → Map: Billiard room → Go to the
bar (`psychic_day1_evening_billiard_room_bar`, calls `lad_generic` which exits
immediately) → Leave → Billiard room (second visit, "I should check again"
narration) → Endure another story by Mr Sinha
(`psychic_day1_evening_billiard_room_group`, the 120-minute Boxer Rebellion speech
exits the map timer after it returns).
- Covers the billiard bar scene and the captain's group story, plus the re-entry
  narration when returning to the billiard room.

---

## setup_psychic_friday_evening_7.json
**Path**: Drinks: lad "What do you think of the other guests?"
(`lad_generic_other_guests_friday_dinner`) → exit → Dinner: Talk to Sushil first
(no should-talk-to-captain-first trigger) → captain_generic: background → heroic
→ guests sub-menu (Host, Nurse, Baldwin) → Map: Go to bed.
- Covers `lad_generic_other_guests_friday_dinner`, the captain's heroic-act path,
  and the "What do you think of Daniel Baldwin?" sub-menu branch that File 1
  does not reach.
