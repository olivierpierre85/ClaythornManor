## Ren'Py Code Structure

### No Duplicated Dialogue
- When multiple branching paths share identical or near-identical dialogue or narration blocks, **extract the shared text into a separate label** and `call` it from each branch.
- This applies to any repeated block of narration, dialogue, or inner monologue — even if it is only two or three lines.
- Name shared labels descriptively (e.g., `nurse_day3_afternoon_meal`, `doctor_day2_evening_shared_farewell`).
- Each shared label must end with `return` so it can be called from multiple places.

### Thread Variables vs Saved Variables
- Use `important_choices` (threads) for any player-facing decision that affects story branching or ending text. These are unlocked with `character_details.important_choices.unlock('name')` and checked with `character_details.important_choices.is_unlocked('name')`.
- Use `saved_variables` only for internal state tracking (visited rooms, UI flags, etc.) that the player does not need to see.
