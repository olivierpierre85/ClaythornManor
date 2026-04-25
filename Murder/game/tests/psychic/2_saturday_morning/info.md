# Saturday Morning — Test Plans

Amelia Baxter has breakfast in the dining room. Ted Harring briefly joins her, then
follows the host to the doctor, leaving her with Captain Sinha for a 30-minute
`captain_generic_menu_psychic` window. After that, Lady Claythorn announces Mr
Moody's death, the doctor gives a preliminary verdict, and the hunt is organised.
The chapter jumps to `psychic_day2_no_hunt` (the psychic never participates in the
hunt).

The single menu (captain_generic, 30-min budget) forces narrow coverage per file —
each 30-minute option (background / heroic / manor) consumes the entire budget,
so these are split across separate files. Heroic-act is not directly reachable in
this chapter because `captain_generic_background_psychic` must be picked first and
it already exhausts the timer; the heroic branch is covered by Friday Evening
tests.

---

## setup_psychic_saturday_morning_1.json
**Path**: Captain: How old are you? (10) → What room are you in? (10) → Tell me
more about yourself (30, overflows and exits the menu).
- Covers `captain_generic_age_psychic`, the Saturday variant of
  `captain_generic_room` (distinct from `captain_generic_room_friday`), and
  `captain_generic_background_psychic`.

---

## setup_psychic_saturday_morning_2.json
**Path**: Captain: What do you think of this place? (30, exhausts the budget).
- Covers `captain_generic_manor_psychic`.

---

## setup_psychic_saturday_morning_3.json
**Path**: Captain: What do you think of the other guests?
(`captain_generic_other_guests_saturday_morning` intro, 0) → sub-menu:
Thomas Moody (20) → Samuel Manning (10, exits).
- Covers `captain_generic_other_guests_saturday_morning` (the Saturday-morning
  intro line "I guess we can talk a bit about the other guests"), plus the
  Moody and Manning friday-or-saturday-morning sub-menu branches.

---

## setup_psychic_saturday_morning_4.json
**Path**: Captain: On second thought, I'd better not talk to him (exit).
- Covers the quick-exit path of `captain_generic_menu_psychic`.
