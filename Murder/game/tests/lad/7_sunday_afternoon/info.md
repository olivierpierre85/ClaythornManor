# Sunday Afternoon — Test Plans

Ted, Amelia Baxter, and Captain Sinha regroup in the tea room. The captain has found no one
and the telephone is dead; the group must decide whether to stay or escape on foot.

The main menu (`lad_day3_escape_menu`) offers three choices:
- **Leave with car** — only available when `seen_car` is unlocked; shows dialogue confirming
  the car is out of petrol, then returns to the menu (no early_exit, cost=0).
- **Stay** — Ted remains with Amelia; the captain leaves alone (`early_exit`).
- **Escape** — Ted follows the captain on foot, leaving Amelia behind (`early_exit`).

**Stay path**: leads to `lad_day3_stay`. If the `poisoned` ending has been unlocked in a
prior playthrough, an inner menu (`lad_day3_stay`) appears letting Ted choose to go to his
room (toilet → poisoned ending) or return straight to the dining room (no_toilet → fell ending).
Without the `poisoned` ending pre-unlocked, the game goes directly to the toilet branch.
Within the no_toilet branch, having `gun` unlocked adds extra confrontation dialogue.

**Escape path**: Ted and the captain leave together. If `gun` is unlocked, the captain spots
Ted's gun and shoots him (`gunned_down` ending). Without a gun, the captain is ambushed
in the forest and Ted escapes alone (`escape` ending).

---

## setup_lad_sunday_afternoon_1.json
**Checkpoint**: seen_car=False, gun=False  
**Path**: Stay (no poisoned pre-unlocked) → straight to toilet → `poisoned` ending  
- Covers the default stay branch with no prior playthrough context.

---

## setup_lad_sunday_afternoon_2.json
**Checkpoint**: seen_car=True, gun=False  
**Path**: Leave with car (dialogue, returns to menu) → Escape → `escape` ending  
- Covers `lad_day3_leave_with_car` dialogue (seen_car condition) and the no-gun escape path.

---

## setup_lad_sunday_afternoon_3.json
**Checkpoint**: seen_car=False, gun=True  
**Path**: Escape → gunned_down ending  
- Covers the `gun` branch inside `lad_day3_escape` (captain confrontation).

---

## setup_lad_sunday_afternoon_4.json
**Checkpoint**: seen_car=True, gun=True; poisoned ending pre-unlocked  
**Path**: Leave with car → Stay → no_toilet (gun dialogue) → `fell` ending  
- Covers `seen_car` + `gun` combination, the `lad_day3_stay` inner menu (poisoned pre-unlocked),
  and the no_toilet branch with gun confrontation dialogue.

---

## setup_lad_sunday_afternoon_5.json
**Checkpoint**: seen_car=False, gun=False; poisoned ending pre-unlocked  
**Path**: Stay → inner menu → toilet choice → `poisoned` ending  
- Covers the `lad_day3_stay` inner menu when the poisoned ending has been seen before,
  and the toilet option (inner monologue about the strange feeling, then goes to room).

---

## setup_lad_sunday_afternoon_6.json
**Checkpoint**: seen_car=False, gun=False; poisoned ending pre-unlocked  
**Path**: Stay → inner menu → no_toilet (no gun) → `fell` ending  
- Covers the no_toilet path without a gun: Ted intercepts the nurse swapping plates,
  the psychic is poisoned instead, and Ted flees through the bedroom window.
