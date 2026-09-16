# Sunday Morning — Test Plans

Lady Claythorn wakes in her clothes with Captain Sinha asleep in the chair by
her door. The staff are gone, the telephone is dead, and the two of them agree
to leave, but to go through the house first for what they will need on the
road. The morning is one long map, and what she finds on it decides what is on
the table at noon.

The chapter is only reachable through `trust_captain` on the Saturday night,
so every plan carries it, although nothing in the morning reads it.

The chapter ends when the script jumps to `host_day3_afternoon`, which calls
`change_time` with `chapter='sunday_afternoon'` so the test runner detects the
chapter change.

---

## The waking

One branch before the map: `saw_car`. If she noticed the old tourer on the
Friday or Saturday evening she brings it up herself and the Captain offers to
look it over. If not, he asks whether there is another car on the estate and
she cannot say.

## The map

`host_day3_morning_map_menu`, 150 units, 09:30 to 12:00. Rooms cost 10 except
the kitchen, the garage, the garden, Mr Manning's door and the butler's attic
room, which cost 20. Every door in the house opens to the Captain's master key,
including the attic that was closed to her on Friday.

The single early exit is `Stop searching and prepare to leave`
(`host_day3_morning_bedroom_host`), where she packs what is hers. Otherwise the
map closes on 0 minutes and a short paragraph takes them back to the hall, so
every plan either ends on her room or spends the 150 units exactly. A room can
be picked only once, and the three doors she will not knock on — Harring,
Marsh, Baxter — all grey out together on the first refusal
(`host_day3_morning_bedroom_others`), so no plan visits more than one of them.

### The three things they need

| Find | Room | Cost | Unlocks |
| ---- | ---- | ---- | ------- |
| The old tourer, sound but dry | Garage | 20 | `car_checked` (observation) |
| Half a tin of petrol behind the butler's lock | Garden, then the shed | 20 | `petrol_tin` (object) |
| Bread, cheese and water for the road | Kitchen | 20 | `provisions` (object) |

The garage and the garden each read the other's flag, so the order matters:
whichever comes second plays `host_day3_morning_leave_with_car`, the Captain
saying they could go now or keep looking. The garage also reads `saw_car` for
its first sentence. All three finds are needed for the car at noon.

### Mr Manning's door

`host_day3_morning_bedroom_drunk` (20) opens the locked room and plays
`host_day3_morning_manning_body` — throat cut behind a door the Captain locked
himself — and sets `day3_morning_manning_checked`. If it is not opened here the
Captain opens it at noon in `host_day3_afternoon`, so plans are split between
the two.

### Framings that play once

| Flag | Rooms | Text |
| ---- | ----- | ---- |
| `day3_morning_others_heard` | tea room, dining room, billiard room, entrance hall | Harring and Baxter heard across the hall, and avoided |
| `day3_morning_attic_visited` | butler's room, storage, both servants' rooms | The attic stair, and the two keys the Captain carries |

## Threads read in the chapter

| Thread | Where |
| ------ | ----- |
| `saw_car` | the waking, and the first line in the garage |
| `found_poison` | the scullery, the bottle put to the Captain |
| `family_history` | the library, closing the book on Kilbraith |
| `car_checked` | the garden, whether the petrol is any use yet |
| `petrol_tin` | the garage, whether the dry tank is any use yet |

`trust_captain` is carried by every plan for realism only. `accused_butler`
and `bested_captain` are declared with `sunday_morning` among their
`relevant_chapters` but nothing in the morning reads them.

---

## Plans at a glance

| Plan | Waking | Rooms | End | State for noon |
| ---- | ------ | ----- | --- | -------------- |
| 1 | she knows the car | garage, garden, kitchen, Manning, hall | packs and leaves | car, petrol, food, Manning seen |
| 2 | she knows the car | scullery, garden, garage, library, gallery, the whole attic, tea room, kitchen | clock runs out | car, petrol, food |
| 3 | the Captain asks | dining, billiard, garage, gun room, garden, Marsh's door, Manning, both dead men | packs and leaves | car, petrol, Manning seen |
| 4 | the Captain asks | scullery, gun room, stair, billiard, hall, library, Harring's door, Captain's room, both dead men, butler's room, girl's room, Manning | clock runs out | nothing, Manning seen |
| 5 | the Captain asks | kitchen, scullery, garden, tea room, gallery, Baxter's door, storage, footman's room | packs and leaves | petrol, food |
| 6 | the Captain asks | garden, garage | packs and leaves | car, petrol |

---

## Coverage matrix

| Branch / consequence | Plan(s) |
| -------------------- | ------- |
| Waking: she brings up the tourer (`saw_car`) | 1, 2 |
| Waking: the Captain asks about a car | 3, 4, 5, 6 |
| Kitchen (`provisions`) | 1, 2, 5 |
| Scullery: the bottle put to the Captain (`found_poison`) | 2, 5 |
| Scullery: dirty dishes only | 4 |
| Garage: still here under its dust (`saw_car`), no petrol yet | 1 |
| Garage: still here under its dust, petrol already found | 2 |
| Garage: under a sheet at the back, no petrol yet | 3 |
| Garage: under a sheet at the back, petrol already found | 6 |
| Gun room, emptied | 3, 4 |
| Tea room | 2, 5 |
| Dining room | 3 |
| Billiard room | 3, 4 |
| Entrance hall, the dead line | 1, 4 |
| The other two heard, first from the hall | 1 |
| The other two heard, first from the tea room | 2, 5 |
| The other two heard, first from the dining room | 3 |
| The other two heard, first from the billiard room | 4 |
| Garden: petrol, car already checked (`leave_with_car`) | 1, 3 |
| Garden: petrol, no car yet | 2, 5, 6 |
| Servant stair (`host_servant_stairs_default`) | 4 |
| Portrait gallery | 2, 5 |
| Library: closing the book (`family_history`) | 2 |
| Library: the book unread | 4 |
| Mr Harring's door, refused | 4 |
| Miss Marsh's door, refused | 3 |
| Miss Baxter's door, refused | 5 |
| Mr Manning's door, the body | 1, 3, 4 |
| Mr Manning's door left shut for noon | 2, 5, 6 |
| The Captain's own room | 4 |
| Doctor Baldwin under the handkerchief | 3, 4 |
| Mr Moody under the sheet | 3, 4 |
| Attic framing, first from the butler's room | 2, 4 |
| Attic framing, first from the storage room | 5 |
| Butler's room, the cabinet of silver | 2, 4 |
| Storage room, the theatrical hamper | 2, 5 |
| Male servants' room | 2, 5 |
| Female servants' room | 2, 4 |
| Exit: packs her own things (`host_day3_morning_bedroom_host`) | 1, 3, 5, 6 |
| Exit: budget runs out, back to the hall | 2, 4 |
| Noon state: car, petrol and food (the car is on the menu) | 1, 2 |
| Noon state: car and petrol, no food | 3, 6 |
| Noon state: petrol and food, no car | 5 |
| Noon state: nothing found | 4 |

---

## setup_host_sunday_morning_1.json
**The quick, complete kit.** `trust_captain` and `saw_car`, so she names the
tourer herself. Garage first — the engine turns over once and dies, and the
Captain hopes for petrol elsewhere — then the shed, where the tin closes the
loop and he says they could leave now. The kitchen for the basket, Mr Manning's
door for the worst of the morning, one look at the dead telephone in the hall
where Harring and Baxter are heard for the first time, and she goes up to pack
with an hour still on the clock. Everything the car needs, and Manning already
found.

## setup_host_sunday_morning_2.json
**The thorough search, and the clock beats her.** The third debug checkpoint:
`trust_captain`, `found_poison`, `family_history`, `saw_car`. The scullery
first, where she finally tells the Captain about the bottle. The shed before
the garage, so the petrol is found with nothing to put it in, and the tourer
turns the same tin into a way out. The library book closed on Kilbraith, the
gallery, then the whole attic — the cabinet of silver he means to come back
for, the hamper, the two stripped rooms — the tea room, and the kitchen takes
the last twenty minutes. No early exit: the map closes on 0 and they go back
to the hall. All three finds, but Mr Manning's door is still locked at noon.

## setup_host_sunday_morning_3.json
**Car and petrol, and nothing to eat.** `trust_captain` alone, so the Captain
has to ask about a car, and the garage is a sheet at the back he has never
heard of. The dining room and the billiard room first, the gun room emptied,
then the shed with the car already checked. She raises her hand to Miss Marsh's
door and is stopped, opens Mr Manning's instead, and looks in on both dead men
before packing. The kitchen is never entered, so the Captain will not take the
car at noon.

## setup_host_sunday_morning_4.json
**Every room that finds nothing.** `trust_captain` alone. The scullery with
nothing in it but dishes, the gun room, the servant stair, the billiard room
and the hall, the library book she never read, Mr Harring's door refused, the
Captain's own room, the Doctor and Mr Moody, the butler's cabinet and the
girl's forgotten hairbrush, and Mr Manning's door takes the last twenty
minutes. The garage, the garden and the kitchen are never visited. Budget spent
exactly, back to the hall, nothing for the road.

## setup_host_sunday_morning_5.json
**Petrol and food, and no car to put them in.** `trust_captain` and
`found_poison`. The kitchen first, then the scullery bottle, then the shed —
where the Captain can only say that if they had a car the tin would do. The tea
room, the gallery, Miss Baxter's door refused, and the attic framing plays on
the storage room rather than the butler's. She packs and leaves with the
garage unvisited and Mr Manning's door still shut.

## setup_host_sunday_morning_6.json
**The shortest route to the car.** `trust_captain` alone. Garden, garage, done:
the petrol found before the car, the car found with the petrol already in
hand, `leave_with_car` playing in the garage, and she stops searching at once
with 110 minutes unused. Proves the chapter can be finished in two rooms, and
leaves the noon decision with car and petrol but no food and Mr Manning
unopened.
