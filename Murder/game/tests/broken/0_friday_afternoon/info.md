# Friday Afternoon — Test Plans

Archibald Moody opens his late brother's flat, reads the bravery-award letter,
boards the train to Claythorn Manor and arrives at the station. Linear
introduction with no menu choices — the chapter ends when the script jumps to
the (currently empty) `broken_day1_evening`, which calls `change_time` with
`chapter='friday_evening'` so the test runner detects the chapter change.

---

## setup_broken_friday_afternoon_1.json
**Path**: Linear playthrough of `broken_introduction`.
- Covers the entire introduction sequence (apartment scene, letter, train).
