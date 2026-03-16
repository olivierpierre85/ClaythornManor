# Day 3 Afternoon — Poisoning & Plate Swaps

All three plates are poisoned (the food itself, from the same pot).
Three diners: **Nurse** (Rosalind Marsh), **Lad** (Ted Harring), **Psychic** (Amelia Baxter).

Nurse is left alone with the plates before the meal. Her choice — and whether Ted catches her — determines who eats what.

---

## Scenario 1: No Swap (Nurse leaves plates as they are)

> Nurse perspective: chooses "Leave the plates as they are"
> Lad perspective: goes to the toilet (default / paranoid choice)

```mermaid
graph LR
    subgraph Before["Before (no swap)"]
        direction TB
        NP1["🍽 Nurse's plate"] -->|seated at| N1["Nurse"]
        LP1["🍽 Lad's plate"] -->|seated at| L1["Lad"]
        PP1["🍽 Psychic's plate"] -->|seated at| P1["Psychic"]
    end

    Before -->|"no swap"| After

    subgraph After["After (unchanged)"]
        direction TB
        NP2["🍽 Nurse's plate"] -->|eaten by| N2["Nurse ☠️"]
        LP2["🍽 Lad's plate"] -->|eaten by| L2["Lad ☠️"]
        PP2["🍽 Psychic's plate"] -->|eaten by| P2["Psychic"]
    end

    subgraph Outcomes["Outcomes"]
        direction TB
        O1["NURSE: collapses first → nurse_ending_poisoned"]
        O2["LAD: collapses after standing → lad poisoned ending"]
        O3["PSYCHIC: survives the meal (her fate depends on her own storyline)"]
    end
```

---

## Scenario 2: Nurse Swaps with Lad (undetected)

> Nurse perspective: chooses "Swap my plate with Mr Harring's"
> Lad perspective: goes to the toilet (default / paranoid choice) — doesn't witness the swap
> Psychic perspective: returns to find everyone seated

```mermaid
graph LR
    subgraph Before["Before (at usual seats)"]
        direction TB
        NP1["🍽 Nurse's plate"] -->|seated at| N1["Nurse"]
        LP1["🍽 Lad's plate"] -->|seated at| L1["Lad"]
        PP1["🍽 Psychic's plate"] -->|seated at| P1["Psychic"]
    end

    Before -->|"Nurse swaps her plate ↔ Lad's plate"| After

    subgraph After["After swap"]
        direction TB
        LP2["🍽 Lad's plate"] -->|eaten by| N2["Nurse ☠️"]
        NP2["🍽 Nurse's plate"] -->|eaten by| L2["Lad ☠️"]
        PP2["🍽 Psychic's plate"] -->|eaten by| P2["Psychic"]
    end

    subgraph Outcomes["Outcomes by perspective"]
        direction TB
        O1["NURSE: Ted dies first, then Nurse realises all plates were poisoned → nurse_ending_poisoned (swapped)"]
        O2["LAD: collapses after standing → lad poisoned ending"]
        O3["PSYCHIC: Ted collapses → Nurse reveals the swap, finds gun on Ted, points it at Psychic"]
        O3a["  → Talk her down: Nurse panics, shoots Psychic → psychic_ending_shot"]
        O3b["  → Take gun by force: gun goes off, Psychic drags tablecloth, fire → psychic_ending_burns"]
    end
```

---

## Scenario 3: Nurse Caught — Swaps with Psychic Instead

> Lad perspective only: chooses "Hold it in and go back downstairs" (intuition, requires `poisoned` ending unlocked)
> Lad catches Nurse holding his plate, refuses the swap
> Nurse swaps her plate with Psychic's instead

```mermaid
graph LR
    subgraph Before["Before (at usual seats)"]
        direction TB
        NP1["🍽 Nurse's plate"] -->|seated at| N1["Nurse"]
        LP1["🍽 Lad's plate"] -->|seated at| L1["Lad"]
        PP1["🍽 Psychic's plate"] -->|seated at| P1["Psychic"]
    end

    Before -->|"Nurse tried Lad's plate → caught!\nSwaps her plate ↔ Psychic's plate"| After

    subgraph After["After swap"]
        direction TB
        PP2["🍽 Psychic's plate"] -->|eaten by| N2["Nurse"]
        LP2["🍽 Lad's plate"] -->|eaten by| L2["Lad ☠️"]
        NP2["🍽 Nurse's plate"] -->|eaten by| P2["Psychic ☠️"]
    end

    subgraph Outcomes["Outcomes"]
        direction TB
        O1["PSYCHIC: collapses first, confesses she's a fraud, dies"]
        O2["LAD: realises he's also poisoned, confronts Nurse"]
        O2a["  → Nurse blames Ted, finds gun on Ted's body"]
        O2b["  → Lad flees, locks himself in room, tries to climb out window"]
        O2c["  → lad 'fell' ending"]
        O3["NURSE: armed with gun, pursues Lad"]
    end
```

---

## Summary Table

| Scenario | Nurse eats | Lad eats | Psychic eats | First to die | Trigger |
|----------|-----------|----------|-------------|-------------|---------|
| 1. No swap | her own plate | his own plate | her own plate | Nurse (nurse POV) / Lad (lad POV) | Nurse: "Leave plates" |
| 2. Nurse ↔ Lad | Lad's plate | Nurse's plate | her own plate | Lad (Ted) | Nurse: "Swap with Mr Harring's" |
| 3. Nurse ↔ Psychic | Psychic's plate | his own plate | Nurse's plate | Psychic (Amelia) | Lad catches Nurse, she swaps with Psychic |
