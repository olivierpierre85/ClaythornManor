# Claythorn Manor — Master Reference guide

This document consolidates the core project guidelines, coding standards, and narrative style requirements for Claythorn Manor. Use this as the primary "Source of Truth" for all development and writing tasks.

## Project Overview
- **Setting**: A Scottish manor in **1924**.
- **Platform**: Ren'Py.
- **Narrative**: Investigation of a murder mystery playing multiple characters across three days. Unlocking information in one character's path opens routes in another's.

## Story & Characters
### Quick Reference
| Code name | Full name | Role & Style |
|-----------|-----------|--------------|
| `lad` | Ted Harring | Hero, petty thief; informal, subtle slang/contractions. |
| `psychic` | Amelia Baxter | The killer; flowery and full language. |
| `doctor` | Daniel Baldwin | Classic middle-class; proper manners. |
| `captain` | Sushil Sinha | Formal Indian officer; noble ancestry; straight to the point. |
| `nurse` | Rosalind Marsh | Pseudo-villain; classic middle-class; proper manners. |
| `drunk` | Samuel Manning | Defence lawyer; mostly incoherent but sometimes educated. |
| `broken` | Thomas Moody | Imposter in a mask; amateur sleuth; classic middle-class. |
| `host` | Lady Claythorn | Aristocratic actress; elegant but not excessive. |

## Script & Coding Structure
- **Folder Layout**: `Murder/game/scripts/<character>/`.
- **Labels**: Follow pattern `<character>_day<N>_<period>` (e.g., `captain_day1_evening`).
- **Narrative Blocks**: Use triple quotes (`"""`) for inner-monologue and narration.
- **Line Spacing**: In Ren'Py dialogue, include a **blank line** after *every* sentence of dialogue or narration.
- **Shared Dialogue**: Extract shared text into `_common/` labels. Every shared label must end with `return`.
- **Variables**:
  - `important_choices` (threads): For player-facing decisions affecting story/endings.
  - `saved_variables`: For internal state tracking (visited rooms, UI flags).

## Grammar & Style Rules
- **English**: Standard British English (grammar and spelling).
- **Time Period**: 1924 (maintain historical tone without being overly "antiquated").
- **Punctuation**: 
  - Do **not** use semicolons in dialogue or narration.
  - Use simple quotes (`'`) instead of curly apostrophes (`’`).
- **Narration**: Written in the **present tense**. Thoughts are direct and revealing.

## Testing Framework
- **Tests**: Located in `Murder/game/tests/<character>/`.
- **Format**: `.json` plan files drive playthroughs.
- **Verification**: Launch game in test mode via Ren'Py launcher or `renpy.exe ... --test`.
