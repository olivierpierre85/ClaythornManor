Chart of possible and linked unlocking

```mermaid
graph TD;
    lad -->|Full| doctor;
    lad -->|Full| psychic;
    psychic -->|Thief| nurse;
    psychic -->|TODO| broken;
    doctor -->|Boxers Rebellion| nurse;
    doctor -->|Letter and not drunk| drunk;
    doctor -->|Unmask| broken;
    nurse -->|Not a fighter| captain;
    nurse -->|Wife Story| drunk;
    captain -->|is not nobility| host;
    drunk -->|full confession| host;
    broken -->|TODO| drunk;
```