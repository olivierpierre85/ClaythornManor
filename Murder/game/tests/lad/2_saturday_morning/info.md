# Saturday Morning — Test Plans

Ted wakes after the storm and joins breakfast. The chapter ends when he chooses
between joining the hunt or staying behind, which jumps to the relevant
afternoon chapter.

---

## setup_lad_saturday_morning_1.json
**Checkpoint**: day1_drunk=True  
**Path**: Follow Lady Claythorn and the doctor (covers the body discovery off-screen
narration) → choose to join the hunt.
- Covers the hung-over wake-up narration (`day1_drunk` branch in the intro).
- Covers `day2_breakfast_follow=True` re-entry dialogue.

---

## setup_lad_saturday_morning_2.json
**Checkpoint**: day1_drunk=False  
**Path**: Stay and eat breakfast (covers the breakfast chat with Amelia and
`psychic_generic` cancel) → stay behind during the hunt.
- Covers the sober wake-up narration.
- Covers `lad_day2_breakfast_eat` and the no-hunt branch.
