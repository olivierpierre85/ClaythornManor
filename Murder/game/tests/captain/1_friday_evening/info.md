## File 1 — Simple map choices

### Dinner
- Ignore Miss Baxter (silent dinner)

### Map Choices
- George IV Bedroom (first bedroom refusal)
- Edward II Bedroom (second bedroom refusal — blocks all other bedrooms)
- Gun room (blocks the rest of the downstairs)
- Storage Room (blocks the rest of the attic)
- Library — Look up the Claythorns in the index
- Tea room
- Portrait Gallery
- Dining Room
- Entrance Hall
- Ends when the 90-minute timer runs out

## File 2 — Billiard room (tell the story, two visits)

The billiard room is entered twice so that the "I am back in the
billiard room" re-entry narration is exercised.

### Dinner
- Talk to Miss Baxter (psychic dinner branch)

### Map Choices
- Meet the others in the billiard room (first visit)
    - Approach the large group
        - Tell the story of the Boxer Rebellion
    - Leave the room
- Meet the others in the billiard room (second visit — triggers the re-entry narration)
    - Have a drink at the bar
    - Approach Dr Baldwin
    - Leave the room
- Retire for the night

## File 3 — Outside (garden, no lantern)

The captain has no lantern on Friday, so the no-lantern garden choice fires:
he braves the rain, spots the outbuilding, and turns back. No shed thread is
set on this evening.

### Dinner
- Ignore Miss Baxter

### Map Choices
- Garden (no-lantern branch) -> `captain_garden_default_no_lantern`
- Retire for the night

## File 4 — Billiard room (refuse the story)

### Dinner
- Ignore Miss Baxter

### Map Choices
- Meet the others in the billiard room
    - Approach the large group
        - Decline the request (forces an early exit from the billiard room)
- Retire for the night

## File 5 — Host suspicion (portrait before library)

Portrait Gallery is visited before the Library so that both
`captain_host_suspicion_portrait` and `captain_host_suspicion_name`
are unlocked when `captain_host_suspicion` is called from
`captain_library_read`, triggering the combined suspicion narration.

### Dinner
- Ignore Miss Baxter

### Map Choices
- Portrait Gallery (unlocks `captain_host_suspicion_portrait`)
- Dining Room
- Entrance Hall
- Library — Look up the Claythorns in the index (unlocks `captain_host_suspicion_name`; fires the full host suspicion block)
- Retire for the night
