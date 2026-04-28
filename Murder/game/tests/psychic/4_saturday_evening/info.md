# Psychic — Saturday Evening (`psychic_day2_evening`)

Each plan starts at the chapter label and runs to the end of the period (or to an ending). The chapter has three distinct gates:
1. **Pre-dinner bedroom menu** (`psychic_day2_evening_bedroom`) — talk to Rosalind, talk to Ted, or nap.
2. **Dinner narration** (host speech, lad/psychic conversation).
3. **Map menu** (`psychic_day2_evening_map_menu`, 60 min) followed by either the lad follow-up discussion or a quiet sleep.

## setup_psychic_saturday_evening_1.json — Visit Ted Harring (visit_lad path)
- Bedroom menu: **Try to talk to Ted Harring** → unlocks `visit_lad`.
- Map: visits William the Conqueror Bedroom, declines to enter (locked), then exits via **Wait in your room for Ted Harring**.
- Triggers `psychic_day2_evening_lad_discussion_follow_up` → full `lad_generic` (background, heroic act, manor, exit).

## setup_psychic_saturday_evening_2.json — Discover Rosalind is sick + silverware
- Bedroom menu: **Try to talk to Rosalind Marsh** → insist → unlocks `nurse_sick`.
- Map: Queen Alexandra (knock, no answer) → **Make sure she is still alive** → enters empty room and unlocks `silverware`.
- Exits via **Wait in your room** (no `visit_lad`).

## setup_psychic_saturday_evening_3.json — Confront Rosalind via Captain (ending: shot)
- Pre-set threads: `nurse_sick`, `silverware`.
- Bedroom: nap. Map: Billiard Room → bar → Sushil Sinha → `captain_generic`.
- Captain menu: **There is something weird about Rosalind Marsh** → accept escort → butler's room confrontation → `psychic_ending_nurse_thief` (shot ending).

## setup_psychic_saturday_evening_4.json — Tell Captain but decline escort, then revisit billiard
- Same pre-set as plan 3. Bedroom: nap. Billiard → bar → captain.
- Captain menu: **There is something weird about Rosalind Marsh** → **Do not go alone with him** → returns to captain talk → **On second thought, I'd better not talk to him** → leave billiard room.
- Returns to billiard room a second time (exercises the `day2_evening_billiard_room_visited` else branch and the captain's `talk_to_captain` else reprompt), exits captain talk again, then **Wait in your room**.

## setup_psychic_saturday_evening_5.json — Quiet evening, body found
- Bedroom: nap. Map covers the downstairs default (Kitchen), Garden (locked-out at night), Edward II Bedroom (sees Doctor Baldwin's body), George IV Bedroom (drunk grunts), then **Wait in your room**.

## setup_psychic_saturday_evening_6.json — Decline to push Rosalind, locked-bedroom try-enters, attic
- Bedroom: **Try to talk to Rosalind Marsh** → **Do not push her further** (no `nurse_sick`).
- Map: George I Bedroom try-enter → no_enter (tries=0); Henry IV Bedroom try-enter → enter then locked (tries=1, exercises the second text-pair); Storage Room then Male Servants Room (two attic visits, exercises both `day2_evening_attic_visited` branches); **Wait in your room**.

## setup_psychic_saturday_evening_7.json — Already-seen broken bedroom, returning to attic, ignore nurse
- Pre-set: threads `visited_attic`, `lord_name`, `lord_age`, `nurse_sick`; saved variables `day2_has_seen_bedroom_broken=true`, `attic_visited=true`.
- Bedroom: nap (no Rosalind option since `nurse_sick` is set).
- Map: Richard III Bedroom → `psychic_day2_bedroom_broken_already_see`; Storage Room → attic_default with `visited_attic` branch; Queen Alexandra → **Don't be so nosy**; Library default; **Wait in your room**.
