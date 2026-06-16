# Friday Evening — Test Plans

Thomas Moody (Archibald in disguise) arrives at the manor, rests in the
'Richard the Third' room, then comes down to the tea room where he meets the
doctor, the nurse, the captain and the drunk. The gong calls everyone in to
dinner, where he is seated beside Lady Claythorn. After her welcome speech he
takes the chance to question her directly over the first course.

The chapter is linear up to the dinner conversation. Its only menu is the
shared host conversation (`host_generic_menu_broken`). The chapter ends with
`jump work_in_progress` (the rest of the story is unwritten), which now ends the
test cleanly in test mode.

---

## setup_broken_friday_evening_1.json
**Path**: Linear playthrough that exhausts every question in the host dinner
conversation.

- Covers the full arrival, tea-room and dinner narration plus all five shared
  `_common` Friday-evening labels (doctor/nurse/broken arrival, doctor
  introduction, captain arrival, nurse joining the captain, host welcome speech).
- Walks the whole `host_generic_menu_broken` conversation: weather, background,
  the invite question (only offered after the background question is asked, via
  its `linked_choice`), the other guests, the manor and her room — then exits.
  Total cost is 80 of the 90 available time units, so every branch is reached in
  one pass.
