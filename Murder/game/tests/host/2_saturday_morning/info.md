# Saturday Morning — Test Plans

Lady Claythorn wakes, breakfasts with her guests, is fetched upstairs to Mr
Moody's bedroom, announces his death to the table and then reads out the
butler's speech introducing the hunt. Linear chapter with no menu at all, so a
single plan covers it.

The shared beats come from `_common/Day 2/1_Morning/1_main.rpy`:
`common_day2_morning_host_to_doctor`, `common_day2_morning_host_death`,
`common_day2_morning_host_death_doctor` and `common_day2_morning_host_hunt`.

The chapter ends when the script jumps to `host_day2_hunt`, which calls
`change_time` with `chapter='saturday_afternoon'` so the test runner detects the
chapter change.

---

## setup_host_saturday_morning_1.json
**Path**: Linear playthrough of `host_day2_morning`, no threads pre-unlocked.
- Covers the waking, the breakfast, the body upstairs, the announcement and the
  hunt speech.
