# Saturday Afternoon (Hunt) — Test Plans

Ted joins the hunting party in the forest. At the end of the introductory scene he must
choose which group to follow, leading to two mutually-exclusive paths: the accident (doctor
shot by Manning) or the no-accident (Ted follows the captain and Lady Claythorn).

---

## setup_lad_saturday_afternoon_1.json
**Checkpoint**: hunt=True  
**Path**: No accident — Ted joins Lady Claythorn and Sushil Sinha.  
- Unlocks `hunt_captain_host`.
- Captain recounts his military history (`captain_details.description_hidden.wars`).
- Group discovers the dying doctor after hearing Manning's shot.

---

## setup_lad_saturday_afternoon_2.json
**Checkpoint**: hunt=True  
**Path**: Accident — Ted joins Doctor Baldwin and Samuel Manning.  
- Unlocks `hunt_doctor_drunk`.
- Ted reveals his Birmingham origins (`lad_details.description_hidden.origin`).
- `doctor_generic_menu_lad` is called (cancelled immediately).
- Manning fires and hits the doctor (`common_day2_hunt_accident_death`).
- Unlocks `doctor_details.description_hidden.fraud`.
