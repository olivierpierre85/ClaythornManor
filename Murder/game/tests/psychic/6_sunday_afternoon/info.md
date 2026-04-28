# Psychic — Sunday Afternoon (`psychic_day3_afternoon`)

The chapter opens in the tea room with the shared captain discussion (`common_day3_afternoon_lad_psychic_captain_discussion_1`). Behaviour then splits on whether the `burned` ending has been unlocked previously:

- **Burned not yet unlocked** — falls straight through `common_day3_afternoon_lad_psychic_captain_discussion_2` (no intuition prefix), then jumps to `psychic_day3_afternoon_stay`.
- **Burned already unlocked** — opens the timed `psychic_day3_stay` menu with two choices: leave with the captain (escape ending) or stay despite the intuition (continues into discussion_2 with the "I disregard the uneasy feeling" prefix, then on to stay path).

Inside `psychic_day3_afternoon_stay`, the chapter walks through the kitchen lunch preparation, Ted's collapse, and the nurse's revelation, ending at the timed `psychic_day3_gun` menu (talk her down → shot ending; take the gun by force → fire ending).

## setup_psychic_sunday_afternoon_1.json — Stay path, talk Rosalind down (shot ending)
- Burned ending **not** unlocked, so no `psychic_day3_stay` menu fires.
- Falls through to `psychic_day3_afternoon_stay`.
- Gun menu: **Try to talk her** → `psychic_day3_afternoon_convince_nurse` → `psychic_ending_shot`.

## setup_psychic_sunday_afternoon_2.json — Stay path, grab the gun (fire ending)
- Burned ending **not** unlocked, same fall-through into stay path.
- Gun menu: **Try to take the gun by force** → `psychic_day3_afternoon_gun_death` → `psychic_ending_burns` (also unlocks `steal_gun` thread mid-run).

## setup_psychic_sunday_afternoon_3.json — Intuition fires, leave with the captain (escape ending)
- Pre-set ending: `burned` (forces the `psychic_day3_stay` timed menu to appear).
- Stay menu: **Let's not take any chance and leave this place{intuition}** → `psychic_day3_afternoon_escape` → `psychic_ending_escape` (also unlocks `leave_manor` thread).

## setup_psychic_sunday_afternoon_4.json — Intuition fires, ignore it and stay (fire ending)
- Pre-set ending: `burned`.
- Stay menu: **I am not going out in these clothes** → `common_day3_afternoon_lad_psychic_captain_discussion_2`. This exercises the `psychic` + `burned` else branch in discussion_2 ("I disregard the uneasy feeling I've just experienced").
- Falls through to `psychic_day3_afternoon_stay`.
- Gun menu: **Try to take the gun by force** → `psychic_day3_afternoon_gun_death` → `psychic_ending_burns`.
