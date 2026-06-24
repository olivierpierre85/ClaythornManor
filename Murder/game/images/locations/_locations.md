# Claythorn Manor — Location Prompts

Source tables for `tools/generate_location_images.py`. Each **description** is wrapped in a FLUX.2 Klein prompt template chosen by the section it sits under. The **id** column matches the `change_room('<id>')` id used in the scripts.

## Image naming convention (time of day)

Location images now encode the time of day in the filename suffix:

- Most rooms ship a **`<id>_day.png`** / **`<id>_night.png`** pair.
- Time-independent scenes (flashbacks, one-off cutscene shots — e.g. `boxer`, `broken_flat`, `train_station`) ship a single **`<id>_neutral.png`**.

`change_room('<id>')` resolves the suffix automatically (see `resolve_room_image` in `scripts/custom_functions.rpy`): it prefers `_neutral`, otherwise picks `_night` when `current_phase == 'Evening'` and `_day` for every other phase (Morning / Afternoon / The Hunt / No Hunt), and finally falls back to a bare `<id>` for legacy/utility images with no variant (`black_background`, `india_young_captain`, `toolshed_outside_day`, `toolshed_outside_night`, `train_inside`).

The previous single-image set has been archived under `version2/` with a `_version2` filename suffix.

## Interior locations

Wrapped in the interior manor template:

> A high-quality semi-realistic digital painting of a 1920s Scottish manor **{description}** at night. Warm amber light, touches of colorful objects. Deep soft shadows, mysterious atmosphere, wide shot, empty room, rich textures.

| id               | description                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| entrance_hall    | grand entrance hall with a central staircase, side doors and a piano in a distant corner, flamboyant and impressive, deep perspective across a broad polished floor |
| tea_room         | large tea room with several chairs and a couple of tables, and drinks tray, flamboyant,impressive and bright                                                        |
| billiard_room    | billiard room with a green baize table and a small bar on the side                                                                                                  |
| dining_room      | formal dining room with a long table laid for dinner, tall candelabra, eight high-backed chairs                                                                     |
| library          | library with tall bookshelves and a small table holding an open book                                                                                                |
| portrait_gallery | narrow gallery lined with portrait paintings of various size, age with both men, women and children, a narrow runner carpet, end with a closed door                 |  |
| bedrooms_hallway | panelled ground-floor corridor with a runner carpet, closed doors only on one side, and a longcase clock                                                            |
| bedroom_lad      | impressive guest bedroom with a worn travelling case                                                                                                                |
| bedroom_psychic  | mysterious guest bedroom draped in dark velvet, with tarot cards on the dressing table                                                                              |
| bedroom_doctor   | slightly disordered guest bedroom with a doctor's bag, and a syringe on a desk                                                                                      |
| bedroom_captain  | neat guest bedroom with a military trunk, a folded officer's uniform on a stand                                                                                     |
| bedroom_host     | elegant lady's bedroom with a large vanity mirror, a chaise longue, and a bed                                                                                       |
| bedroom_drunk    | dishevelled guest bedroom with two empty whiskies bottle, a rumpled bed and a coat thrown over a chair                                                              |
| bedroom_broken   | shadowy guest bedroom with the curtains drawn                                                                                                                       |
| bedroom_nurse    | tidy guest bedroom with a neatly made bed, a folded nurse's apron and a small medical case                                                                          |
| basement_stairs  | staircase descending into the basement, view from the top                                                                                                           |
| servant_stairs   | narrow servants' staircase, plain and steep with a worn wooden handrail, a footman livery hangs on the wall                                                         |
| kitchen          | large servants' kitchen with a cast-iron range, a long worktable and a flagstone floor                                                                              |
| scullery         | cramped scullery with a deep stone sink                                                                                                                             |
| gun_room         | large downstairs gun room with a glass-fronted cabinet of hunting rifles, central table with small handgun, flagstone floor                                         |
| garage           | manor garage with an old motor car, tools hung on the wall, large garage door closed                                                                                |
| toolshed         | garden shed interior with a rectangular red petrol tin in the corner, mysterious atmosphere, realistic style,                                                       |

## Attic locations

Wrapped in the attic template — the interior template without the colourful objects, to keep the eerie attic atmosphere:

> A high-quality semi-realistic digital painting of a 1920s Scottish manor **{description}** at night. Deep soft shadows, mysterious atmosphere, wide shot, empty room, rich textures.

| id                 | description                                                                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| attic_hallway      | wide attic corridor, high ceiling, three doors on the right, one on the left all closed, bare floorboards, point of view standing at the top of a staircase, discarded furniture and objects |
| attic_storage_room | very large cluttered upstairs storage room, full of dust-sheeted furniture and other stuff                                                                                                   |
| attic_males_room   | spartan servants upstairs room for the menfolk, with two narrow iron beds and a plain washstand, one worn-out luggage                                                                        |
| attic_females_room | modest servants' upstairs room for the maids, with two narrow iron beds,a small dresser, one worn-out luggage                                                                                |
| attic_butler_room  | butler's tidy upstairs room, with a single bed, a writing desk, a neatly pressed livery, and a glass-fronted butler's pantry                                                                 |

## Outdoor locations

Wrapped in the outdoor template:

> A high-quality semi-realistic digital painting of a **{description}**. Deep soft shadows, mysterious atmosphere, wide shot, rich textures.

| id                     | description                                                                                                                                                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| broken_flat            | Victorian pauper apartment, with a dead man on his bed, with a sheet covering his head                                                                                                                                       |
| india_young_captain    | 1890s colonial Calcutta room, a young Indian boy at his lessons with a governess while his mother looks on, warm sunlight through a tall window overlooking a garden                                                         |
| manor_exterior         | grand 1920s two-storey Scottish manor seen from the gravel drive, surrounded by tall trees, towering stone facade and lit windows rising against a stormy sky, luxurious garden on the back                                  |
| manor_garden           | 1920s Scottish manor garden, gravel paths and a stone fountain, the dark house looming behind, tall trees around, touch of warm colors                                                                                       |
| forest                 | dense Scottish forest, tall trees and tangled undergrowth, mist drifting between the trunks, touch of warm colors                                                                                                            |
| forest_road            | narrow rutted road winding through a dark Scottish forest, tall trees crowding either side, touch of warm colors                                                                                                             |
| toolshed_outside_day   | small weathered wooden garden shed seen from outside, set among overgrown grass and tall trees, grey daylight                                                                                                                |
| toolshed_outside_night | small weathered wooden garden shed seen from outside, set among overgrown grass and tall trees, moonlight and deep shadows at night                                                                                          |
| train_station          | medium size Scottish railway station, daytime, old train from 1920, a few people on the platform, gas lamps, touch of warm colors                                                                                            |
| police_station         | modest small-town Scottish police station in 1920, inside with a few persons working, touch of warm colors                                                                                                                   |
| house_on_fire          | 1920s terraced house in flames at night, in the city center of a big british city, fire bursting from the windows and roof, smoke billowing into a dark sky, touch of warm colors                                            |
| train_inside_first     | 1920s first-class railway carriage interior, polished wood panelling and brass fittings, a window showing the grey-green English countryside rushing past, touch of warm colors                                              |
| train_inside_second    | 1920s second-class railway carriage interior, plain wooden bench seats and a bare luggage rack with old bag and coat, view toward a window showing the grey-green English countryside rushing past, touch of warm colors     |
| inside_car             | 1920s motor car interior, view from the passenger seat towards the windscreen, a wooded country road and rainy sky outside, touch of warm colors                                                                             |
| boxer_fight            | Boxer Rebellion in 1900 China, the Eight-Nation Alliance assault on Beijing, europeans soldiers storming a great fortified city gate amid smoke and fire                                                                     |
| boxer                  | aftermath of the Boxer Rebellion in 1900 Beijing, a few european soldiers occupying the conquered city, looted goods piled in a square before grand Chinese gates, smoke hanging in the air, chinese merchants selling wares |



