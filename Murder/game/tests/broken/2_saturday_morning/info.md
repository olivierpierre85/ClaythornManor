# Broken - Saturday Morning (Breakfast / the Death Reveal)

Straight narration, no menus at all: Broken wakes, comes down to a dining
room, and Lady Claythorn returns from upstairs to announce that Ted Harring
died in the night. Doctor Baldwin can find no cause. Lady Claythorn proposes
carrying on with the shooting party regardless; Miss Marsh objects, is
overruled, and Broken privately decides to join the hunt to get Captain Sinha
alone. The label ends with an unconditional `jump broken_day2_hunt`.

The only branching is two internal thoughts, gated on threads carried over
from Friday evening (`broken_config.rpy`):

- `talked_to_maid` — adds a paragraph wondering whether the letter is part of
  the "surprise" the maid mentioned.
- `found_poison` — adds a paragraph noticing the rat poison bottle from the
  scullery again once the room is sitting with the news.

Both are independent, so all four combinations are covered.

## setup_broken_saturday_morning_1.json
No threads. Neither aside appears. (`choices: []`)

## setup_broken_saturday_morning_2.json
`talked_to_maid`. The letter/surprise aside appears; the poison aside does
not. (`choices: []`)

## setup_broken_saturday_morning_3.json
`found_poison`. The poison aside appears; the letter/surprise aside does not.
(`choices: []`)

## setup_broken_saturday_morning_4.json
`talked_to_maid` and `found_poison`. Both asides appear. (`choices: []`)
