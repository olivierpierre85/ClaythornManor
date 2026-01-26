# Lad - Day 1 Story Flow (BETA Try)

This chart represents the narrative flow, choices, and potential endings for the "Lad" character on Day 1.

```mermaid
graph TD
    Start((Start: Afternoon)) --> Train[Train: Read Letter]
    Train --> Station[Station: Meet Footman]
    Station --> Car[Car Ride: Chat with Footman]
    Car --> Manor[Arrival at Manor]
    Manor --> TeaRoom[Tea Room: Meet Guests]

    subgraph Evening [Evening 18:00 - 23:00]
        TeaRoom --> TeaChoices{Tea Room Choices}
        TeaChoices -- Talk to Samuel Manning --> DrunkTalk[Drunk Sleeping]
        TeaChoices -- Talk to Amelia Baxter --> PsychicTalk[Chat with Psychic]
        TeaChoices -- Stand Awkwardly --> Dinner
        DrunkTalk --> Dinner
        PsychicTalk --> Dinner

        Dinner[Dinner: Host Speech] --> DinnerChoices{Dinner Conversation}
        DinnerChoices -- Talk to Daniel Baldwin --> DoctorDinner[Chat with Doctor]
        DinnerChoices -- Talk to Amelia Baxter --> PsychicDinner[Chat with Psychic]
        DinnerChoices -- Eat in Silence --> Bedroom
        DoctorDinner --> Bedroom
        PsychicDinner --> Bedroom

        Bedroom[Bedroom: Unpack] --> MapMenu{Free Roam / Map}
        
        MapMenu -- Go to Sleep --> NightEnd
        MapMenu -- Visit Other Rooms --> GenericRooms[Generic Room Visits]
        GenericRooms --> MapMenu
        
        MapMenu -- Visit Billiard Room --> BilliardRoom[Billiard Room]
    end

    subgraph Billiard_Room [Billiard Room Events]
        BilliardRoom --> BilliardChoices{Actions}
        BilliardChoices -- Talk to Doctor --> DocBilliard[Chat with Doctor]
        BilliardChoices -- Approach Group --> GroupStory[Listen to Captain's Story]
        BilliardChoices -- Ask Butler --> UnlockPsychic[Unlock Psychic's Bedroom]
        
        BilliardChoices -- Go to Bar --> Bar1
        
        Bar1[Bar 1: Meet Thomas Moody] --> Whisky[Drink Whisky]
        Whisky -- Unlocks --> ThreadWhisky[Thread: Whisky]
        Whisky --> Bar2[Bar 2: Drink Sherry]
        Bar2 --> Bar3[Bar 3: Drink Port]
        Bar3 --> Drunk[Get Drunk]
        Drunk -- Unlocks --> ThreadDrunk[Thread: Day 1 Drunk]
        
        DocBilliard --> MapMenu
        GroupStory --> MapMenu
        UnlockPsychic --> MapMenu
        Whisky --> MapMenu
        Drunk --> MapMenu
    end

    UnlockPsychic -.-> |If unlocked| PsychicRoom[Visit Psychic Bedroom]
    MapMenu -- Visit Psychic Bedroom --> PsychicRoom
    PsychicRoom --> MapMenu

    subgraph Night_Resolution [Night Resolution]
        NightEnd{Check Status}
        
        NightEnd -- "Thread: Whisky AND NOT Thread: Drunk" --> Death[Ending: Poisoned/Deathbed]
        NightEnd -- "Thread: Drunk (Pukes)" --> Morning[Day 2 Morning]
        NightEnd -- "No Whisky" --> Morning
    end

    classDef distinct fill:#f96,stroke:#333,stroke-width:2px;
    classDef morning fill:#9f6,stroke:#333,stroke-width:2px;
    class Death distinct;
    class Morning morning;
```

## Key Decision Points

1.  **Billiard Room - Bar**: This is the critical path.
    *   **Meeting Thomas Moody** triggers the first drink (Whisky). This sets the `whisky` thread.
    *   **Drinking too much (3 drinks)** sets the `day1_drunk` thread.
2.  **Survival Logic**:
    *   The Whisky is poisoned (or causes the death condition).
    *   If you get **Drunk**, you vomit in your room, expelling the poison.
    *   **Equation**: `Whisky + Not Drunk = Death`. `Whisky + Drunk = Survival`. `No Whisky = Survival`.

## Minor Choices
*   **Social**: Conversations in Tea Room and Dinner affect relationship threads (generic interactions) but don't strictly branch the main plotline for Day 1.
*   **Psychic Room**: Asking the Butler allows you to knock on Amelia's door, but she turns you away.
