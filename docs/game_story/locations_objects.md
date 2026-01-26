# 🏰 The Manor Locations & Objects

## 📍 Interactive Rooms & Associated Threads

### Ground Floor (Floor 1)
- **Library**
    - **Psychic Path**: Find the name of the "LORD" (`lord_name`). Requires having visited the Attic.
    - **Captain Path**: Learn that the host is not aristocracy.
- **Tea Room**
    - Central social hub. Used for talking with guests and group scenes.
- **Billiard Room**
    - Social hub. Locations for bar and games.
- **Dining Room**
    - Group meals and major plot events.
- **Entrance Hall**
    - Main entry point. First arrival location.
- **Portrait Gallery**
    - **Psychic Path**: Look for portraits of the old lords (`lord_name`, `lord_age`). Requires having visited the Attic.

### Basement (Floor 0)
- **Kitchen**
    - **Object**: Poison bottle.
    - **Thread**: `green_liquid` (Lad path, Saturday Evening).
- **Scullery**
    - Potential hiding spot for the Nurse chase sequence.
- **Garage**
    - **Objects**: Old car, Gasoline, Car keys.
    - **Threads**: `seen_car` (Lad path, Sunday Morning).
- **Gun Room**
    - **Object**: Enfield Mk II Revolver.
    - **Threads**: `gun` (Lad path, Sunday), `steal_gun` (Psychic Path, Sunday).
    - **Condition**: Weaponry use often requires military background (Captain).

### Attic (Floor 3)
- **Attic Hallway & Storage Room**
    - **Psychic Path**: Meet "the old man" (The Lord). Unlocks `visited_attic`.
- **Servants' Rooms** (Male, Female, Butler)
    - **Action**: Finding livery or staff-related clues.
    - **Threads**: `footman_french_1`, `footman_actor`.

### Outdoors
- **Gardens**
    - Scene for the hunt and outdoor confrontations.
    - **Threads**: `hunt` (Saturday Afternoon).

---

## 🛏️ Bedrooms (Floor 2)
The bedrooms are themed after English Royalty, reflecting the character's archetypes or fates. Bedroom assignments are critical for sneaking sequences.

### The Lad - William the Conqueror Room
- **Reference**: The "Hero" king / Self-made man.
- **Context**: Reflects the Lad's background as someone who "conquered" his circumstances.

### The Psychic - Elizabeth I Room
- **Reference**: The "Virgin Queen".
- **Context**: Powerful, mysterious, and influential.

### The Doctor - Edward II Room
- **Reference**: The failing/addict king.
- **Context**: Enter as the Doctor to find narcotics-related clues.

### The Captain - George I Room
- **Reference**: The foreign/administrative king.
- **Context**: Reflects the Captain's noble but "outsider" status.

### The Host - Henry IV Room
- **Reference**: The usurper king.
- **Context**: Reflects the nature of the Host's position.

### The Drunk - George IV Room
- **Reference**: The drunk king.
- **Context**: Find the `drunk_letter` here (accessible by the Doctor).

### The Broken - Richard III Room
- **Reference**: The injured/hunchback king.
- **Context**: Reflects his "Broken Face" condition.

### The Nurse - Queen Alexandra Room
- **Reference**: Strong interest in nursing and military medicine.
- **Context**: Dedicated to the Nurse's professional background.

---

---

## 🗝️ Key Objects & Story Threads

### Discovery Checklist
- **Whisky** (`whisky`): Found/shared in the Evening (Lad/Drunk).
- **Poison / Green Liquid** (`green_liquid`): Discovered in the kitchen scullery areas.
- **Enfield Mk II Revolver** (`gun` / `steal_gun`): Found in the Gun Room. Bullets may be locked.
- **Footman Livery**: Used for infiltration (Broken path).
- **Burned Letter** (`burned_letter`): Found in the downstairs areas (Ladpath).
- **Silverware** (`silverware`): Identified by the Psychic as a potential clue.
- **Books**: `book_mystery` and `book_opium` (Doctor path).
- **Chains**: To move blocking trees during the escape.

### Major State Flags
- `visited_attic`: Unlock Psychic-specific library interactions.
- `broken_unmasked`: Evidence of the Impostor's identity.
- `trust_captain` / `trust_nurse`: Defines Sunday Afternoon alliances.
- `day1_drunk` / `day2_drunk`: Tracks the state of the Drunk guest.



