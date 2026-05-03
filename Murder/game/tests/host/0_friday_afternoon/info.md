# Friday Afternoon — Test Plans

Lady Claythorn (an out-of-work actress hired to play her) arrives at the manor
with the butler. They argue gently over who should play the lord/lady before
going inside to brief the actors playing the staff. Linear introduction with no
menu choices — the chapter ends when the script jumps to the (currently empty)
`host_day1_evening`, which calls `change_time` with `chapter='friday_evening'`
so the test runner detects the chapter change.

---

## setup_host_friday_afternoon_1.json
**Path**: Linear playthrough of `host_introduction`.
- Covers the entire arrival sequence with the butler.
