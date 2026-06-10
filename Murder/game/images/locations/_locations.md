# Claythorn Manor — Location Prompts

Source tables for `tools/generate_location_images.py`. Each **description** is wrapped in a FLUX.2 Klein prompt template chosen by the section it sits under. The **id** column is the output filename (`<id>.png`) and matches the `change_room('<id>')` id used in the scripts.

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
| toolshed         | garden shed interior with a rectangular red petrol tin in the corner, mysterious atmosphere                                                                         |

## Attic locations

Wrapped in the attic template — the interior template without the colourful objects, to keep the eerie attic atmosphere:

> A high-quality semi-realistic digital painting of a 1920s Scottish manor **{description}** at night. Deep soft shadows, mysterious atmosphere, wide shot, empty room, rich textures.

| id                 | description                                                                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| attic_hallway      | wide attic corridor, high ceiling, three doors on the right, one on the left all closed, bare floorboards, point of view standing at the top of a staircase, discarded furniture and objects |
| attic_storage_room | very large cluttered upstairs storage room, full of dust-sheeted furniture and other stuff                                                                                                   |
| attic_males_room   | spartan servants upstairs room for the menfolk, with two narrow iron beds and a plain washstand, one worn-out luggage                                                                        |
| attic_females_room | modest servants' upstairs room for the maids, with two narrow iron beds,a small dresser, one worn-out luggage                                                                                |
| butler_room        | butler's tidy upstairs room, with a single bed, a writing desk, a neatly pressed livery, and a glass-fronted butler's pantry                                                                 |

## Outdoor locations

Wrapped in the outdoor template:

> A high-quality semi-realistic digital painting of a **{description}**. Warm amber light. Deep soft shadows, mysterious atmosphere, wide shot, rich textures.

| id                     | description                                                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| manor_exterior         | grand 1920s Scottish manor seen from the gravel drive, its towering stone facade and lit windows rising against a stormy sky |
| manor_garden           | 1920s Scottish manor garden with clipped hedges, gravel paths and a stone fountain, the dark house looming behind            |
| forest                 | dense Scottish pine forest, tall trees and tangled undergrowth, mist drifting between the trunks                             |
| forest_road            | narrow rutted road winding through a dark Scottish forest, tall trees crowding either side                                   |
| toolshed_outside_day   | weathered stone toolshed in the manor grounds by day, a heavy wooden door and overgrown grass around it                      |
| toolshed_outside_night | weathered stone toolshed in the manor grounds at night, a heavy wooden door and shadows pooling around it in the rain        |
| train_station          | small rural Scottish railway station with an empty platform, gas lamps, a wooden bench and a canopy                          |
| police_station         | modest small-town Scottish police station of grey stone, seen from the street, a blue lamp above its door                    |
| house_on_fire          | 1920s Scottish manor engulfed in flames at night, fire bursting from the windows and roof, smoke billowing into a dark sky   |
