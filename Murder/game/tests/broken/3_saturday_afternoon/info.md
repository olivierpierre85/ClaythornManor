# Broken - Saturday Afternoon (The Hunt)

Broken joins the Captain's party in the north field. The hunt hardens his
conviction that Sinha is a fraud. Two of the Captain's actions stoke his anger,
each tempered by a thread the player may carry:

- `host_lies`      tempers the poor-shooting beat (the Host is a fraud too).
- `talked_to_maid` tempers the luncheon war-story beat (warns of a setup).

Choice gate: with `talked_to_maid`, Broken may SPARE or KILL the Captain.
Without it, rage wins and the kill is the only path. The kill itself is shared
with the Captain's storyline via `common_day2_hunt_captain_confrontation`.

## setup_broken_saturday_afternoon_1.json
No threads. No tempering, no menu. Linear give-in-to-anger kill. (`choices: []`)

## setup_broken_saturday_afternoon_2.json
`talked_to_maid` unlocked. The revenge menu appears; this plan picks KILL.

## setup_broken_saturday_afternoon_3.json
`talked_to_maid` unlocked. The revenge menu appears; this plan picks SPARE,
exercising the branch where Broken refuses and rushes toward the far party.

## setup_broken_saturday_afternoon_4.json
`host_lies` unlocked (no `talked_to_maid`). The shooting beat is tempered, but
with no maid warning there is no menu: linear kill. (`choices: []`)
