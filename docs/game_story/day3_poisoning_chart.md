# Day 3 Afternoon — Poisoning & Plate Swaps

The psychic wants to kill the nurse, so she poisoned her plate.
But she wants to sedate the lad (Ted Harring), so she gives him a sedative.

But the plates will be switched, so the ending is not always what was planned.

**Legend:**
- ☠️ **Poison:** Deadly (Strychnine)
- 💤 **Sedative:** Sleeping pills
- 🍽️ **Clean:** Normal food

## Base Scenario (No Swaps)

```mermaid
graph TB
    subgraph Before["Before (no swap)"]
        direction TB
        NP1["🍽️ Nurse's plate (☠️ Poison)"] -->|seated at| N1["Nurse"]
        LP1["🍽️ Lad's plate (💤 Sedative)"] -->|seated at| L1["Lad"]
        PP1["🍽️ Psychic's plate (🍽️ Clean)"] -->|seated at| P1["Psychic"]
    end

    Before -->|"eaten as intended"| After

    subgraph After["After (unchanged)"]
        direction TB
        NP2["🍽️ Nurse's plate (☠️ Poison)"] -->|eaten by| N2["Nurse ☠️ (Dead)"]
        LP2["🍽️ Lad's plate (💤 Sedative)"] -->|eaten by| L2["Lad 💤 (Asleep)"]
        PP2["🍽️ Psychic's plate (🍽️ Clean)"] -->|eaten by| P2["Psychic 🍽️ (Fine)"]
    end
```

## First encounter - Lad

### Scenario A: Lad is Late
He comes late and didn't notice the nurse switching their plates, so he eats hers and vice versa.

```mermaid
graph LR
    subgraph ScenarioA["Scenario A: Lad is Late (Nurse & Lad Swap)"]
        NP3["🍽️ Nurse's original plate (☠️ Poison)"]
        LP3["🍽️ Lad's original plate (💤 Sedative)"]
        PP3["🍽️ Psychic's original plate (🍽️ Clean)"]

        N3["Nurse 💤 (Asleep)"]
        L3["Lad ☠️ (Dead)"]
        P3["Psychic 🍽️ (Fine)"]

        NP3 ~~~ LP3
        LP3 ~~~ PP3
        
        N3 ~~~ L3
        L3 ~~~ P3

        NP3 -->|eaten by| L3
        LP3 -->|eaten by| N3
        PP3 -->|eaten by| P3
    end
```

### Scenario B: Lad is Early
He comes back early and forces the nurse to change her plate with the psychic.

```mermaid
graph LR
    subgraph ScenarioB["Scenario B: Lad is Early (Nurse & Psychic Swap)"]
        NP4["🍽️ Nurse's original plate (☠️ Poison)"]
        LP4["🍽️ Lad's original plate (💤 Sedative)"]
        PP4["🍽️ Psychic's original plate (🍽️ Clean)"]

        N4["Nurse 🍽️ (Fine)"]
        L4["Lad 💤 (Asleep)"]
        P4["Psychic ☠️ (Dead)"]

        NP4 ~~~ LP4
        LP4 ~~~ PP4
        
        N4 ~~~ L4
        L4 ~~~ P4

        NP4 -->|eaten by| P4
        LP4 -->|eaten by| L4
        PP4 -->|eaten by| N4
    end
```
