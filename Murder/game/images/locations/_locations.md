# Claythorn Manor — Interior Location Prompts

Source table for `tools/generate_location_images.py`. Each **description** is wrapped in the FLUX.2 Klein manor template:

> A high-quality semi-realistic digital painting of a 1920s Scottish manor **{description}** at night. Warm amber light, touches of colorful objects. Deep soft shadows, mysterious atmosphere, wide shot, empty room, rich textures.

The **id** column is the output filename (`<id>.png`) and matches the `change_room('<id>')` id used in the scripts.

| id                 | description                                                                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| entrance_hall      | grand entrance hall with a central staircase, side doors and a piano in a distant corner, flamboyant and impressive, deep perspective across a broad polished floor |
| tea_room           | large tea room with several chairs and a couple of tables, and drinks tray, flamboyant,impressive and bright                                                        |
| billiard_room      | billiard room with a green baize table and a small bar on the side                                                                                                  |
| dining_room        | formal dining room with a long table laid for dinner, tall candelabra, high-backed chairs and a great stone fireplace                                               |
| library            | library with tall bookshelves and a small table holding an open book                                                                                                |
| portrait_gallery   | long portrait gallery lined with gilt-framed ancestral oil paintings, a narrow runner carpet and wall sconces                                                       |
| hallway            | panelled ground-floor corridor with a runner carpet, closed doors and a longcase clock                                                                              |
| bedrooms_hallway   | upstairs bedroom corridor with rows of panelled doors, a long runner carpet and wall sconces                                                                        |
| bedroom_lad        | modest guest bedroom plainly furnished with a simple iron bed and a worn travelling case                                                                            |
| bedroom_psychic    | mysterious guest bedroom draped in dark velvet, with a crystal ball and tarot cards on the dressing table                                                           |
| bedroom_doctor     | disordered guest bedroom with a doctor's bag, scattered glass vials and an unmade bed                                                                               |
| bedroom_captain    | neat guest bedroom with a military trunk, a folded officer's uniform and a ceremonial sabre on the wall                                                             |
| bedroom_host       | elegant lady's bedroom with a large vanity mirror, draped theatrical gowns and a chaise longue                                                                      |
| bedroom_drunk      | dishevelled guest bedroom with empty bottles, a rumpled bed and a coat thrown over a chair                                                                          |
| bedroom_broken     | shadowy guest bedroom with the curtains drawn, a wash basin and a discarded face mask on the dresser                                                                |
| bedroom_nurse      | tidy guest bedroom with a neatly made bed, a folded nurse's apron and a small medical case                                                                          |
| basement_stairs    | narrow stone staircase descending into the basement, bare brick walls and an iron handrail                                                                          |
| servant_stairs     | narrow servants' staircase, plain and steep with a worn wooden handrail                                                                                             |
| kitchen            | large servants' kitchen with a cast-iron range, copper pots hung above a long worktable and a flagstone floor                                                       |
| scullery           | cramped scullery with a deep stone sink, washing tubs and shelves of crockery                                                                                       |
| gun_room           | gun room with a glass-fronted cabinet of hunting rifles, a revolver on the table and mounted antlers                                                                |
| garage             | manor garage with an old motor car, stacked petrol cans and tools hung on the wall                                                                                  |
| attic_hallway      | cramped attic corridor with sloping beamed ceilings, bare floorboards and a single small window                                                                     |
| attic_storage_room | cluttered attic storage room full of dust-sheeted furniture, old trunks and cobwebbed crates                                                                        |
| attic_males_room   | spartan servants' attic room for the menfolk, with a narrow iron bed and a plain washstand                                                                          |
| attic_females_room | modest servants' attic room for the maids, with twin iron beds and a small dresser                                                                                  |
| butler_room        | the butler's tidy attic room, with a single bed, a writing desk and a neatly pressed livery                                                                         |
| toolshed           | toolshed interior with a rectangular red petrol tin in the corner                                                                                                   |
