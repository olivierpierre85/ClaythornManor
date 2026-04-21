# Saturday Evening — Test Plans

Ted returns to the manor after the hunt (or watches the party return). After a bedroom interlude
(Amelia Baxter warns him of danger) and dinner, he has free time to explore. Key branches:
billiard room captain hypotheses, Amelia's room (trust/don't trust), doctor's room (laudanum),
and drinking to excess.

The eight checkpoints cover the full cross-product of hunt/no-hunt, hunt group, day1_drunk, and
the no-hunt investigation threads.

---

## setup_lad_saturday_evening_1.json
**Checkpoint**: hunt=True, hunt_captain_host=True, day1_drunk=False  
**Path**: Doctor's room → Billiard room (captain talk: laudanum + drunk hypotheses)  
- Visits doctor's room: finds laudanum, unlocks `laudanum`.  
- Billiard captain talk: `hunt_doctor_drunk` NOT unlocked, so drunk hypothesis shows basic branch.  
- Covers `lad_day2_evening_billiard_room_captain_hypothesis_doctor` and `_drunk`.

---

## setup_lad_saturday_evening_2.json
**Checkpoint**: hunt=True, hunt_captain_host=True, day1_drunk=True  
**Path**: Billiard room (4 drinks → `day2_drunk`) → sleep  
- Drinks chain: bar → bar_2 → bar_3 (captain reacts) → bar_4 (unlocks `day2_drunk`).  
- End-of-chapter: `day2_drunk + day1_drunk` branch unlocks `poor_drinker`.

---

## setup_lad_saturday_evening_3.json
**Checkpoint**: hunt=True, hunt_captain_host=False (= hunt_doctor_drunk unlocked), day1_drunk=False  
**Path**: Billiard room (captain: drunk hypothesis with hunt_doctor_drunk branch) → Psychic room (trust)  
- Drunk hypothesis shows extra captain dialogue when `hunt_doctor_drunk` is unlocked.  
- Psychic trust: unlocks `trust_psychic`, runs `common_day2_evening_lad_psychic_discussion_2`,
  calls `psychic_generic_menu_lad` (cancelled immediately).

---

## setup_lad_saturday_evening_4.json
**Checkpoint**: hunt=True, hunt_captain_host=False, day1_drunk=True  
**Path**: Psychic room (don't trust) → sleep  
- Amelia gets angry and throws Ted out. No `trust_psychic` unlocked.

---

## setup_lad_saturday_evening_5.json
**Checkpoint**: hunt=False, all threads False  
**Path**: Sleep immediately  
- Covers no-hunt intro narration (watching party arrive) and the full fixed-dialogue chain
  (entrance hall, bedroom interlude, dinner).

---

## setup_lad_saturday_evening_6.json
**Checkpoint**: hunt=False, downstairs_1=True, rest False  
**Path**: Psychic room (trust → cancel psychic_generic) → sleep  
- Second run of the psychic trust path from a no-hunt starting state.

---

## setup_lad_saturday_evening_7.json
**Checkpoint**: hunt=False, downstairs_1=True, downstairs_2=True, green_liquid=True, burned_letter=True, day1_drunk=False  
**Path**: Richard III Bedroom (back visit) → Doctor's room → Billiard (all four hypotheses) → Richard III Bedroom (flask taste visit) → sleep  
- `lad_day2_bedroom_broken_back`: second look at Moody's room (nothing new found).  
- Doctor's room: unlocks `laudanum`.  
- Billiard captain talk: all four hypothesis options exercised (laudanum, green liquid, burned
  letter, drunk). Green liquid hypothesis sets `day2_evening_taste_from_flask=True` (since
  `whisky` not unlocked).  
- `lad_day2_bedroom_broken_back_for_drink`: Ted looks for the flask after Sushil's suggestion.

---

## setup_lad_saturday_evening_8.json
**Checkpoint**: hunt=False, downstairs_1=True, downstairs_2=True, green_liquid=True, burned_letter=True, day1_drunk=True  
**Path**: Billiard room (4 drinks → `day2_drunk`) → sleep  
- Covers the drunk-evening path on the no-hunt route.  
- End-of-chapter: `day2_drunk + day1_drunk` branch unlocks `poor_drinker`.
