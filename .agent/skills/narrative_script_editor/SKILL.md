---
name: narrative_script_editor
description: Performs a targeted editorial pass on Ren'Py (.rpy) script files. This skill specialises in replacing "TODO" placeholders with context-aware prose and making minimal, necessary corrections to existing dialogue and narration, while strictly preserving code integrity and indentation.
---
--------------

**Instructions:**
1. **Scope & Identification:** 
   - Identify the target file (primarily `.rpy` scripts). 
   - Isolate dialogue strings (e.g., `char "..."`) and narration blocks (enclosed in `"""` or `'''`).

2. **Source of Truth (Hard Rule):**
   - Strictly adhere to the rules in [master_reference.md](file:///c:/Projects/ClaythornManor/.agent/master_reference.md).
   - This includes character-specific styles, 1920s British English, and structural conventions.

3. **Code & Syntax Preservation (Hard Rule):**
   - **Do Not Modify:** Labels (`label:`), jumps (`jump`), calls (`call`), variable assignments (`$ var = ...`), or logic (`if/else`). 
   - **Indentation:** Maintain the exact original leading whitespace for every line.
   - **Formatting:** Ensure all rewritten text remains properly enclosed in its original quote types.

4. **Ren'Py Structural Conventions:**
   - **Blank Lines:** Add a blank line after *every* sentence of dialogue or narration.
   - **Shared Dialogue:** If text matches another scene, it must be extracted to `_common/`.
   - **Variables:** Use `important_choices` for story-critical threads and `saved_variables` for state.

5. **Contextual TODO Resolution:**
   - Locate all instances of `TODO`, `[TODO]`, or empty narrative brackets. 
   - Analyse the surrounding scene to infer mood and plot. 
   - Replace placeholders with fully-realised dialogue or inner-monologue beats.

6. **Light-Touch Editing (Conservative by Default):**
   - **Editorial Mandate:** Preserve existing dialogue and narration unless it contains a grammar error, breaks voice, is anachronistic, or is flagged as `TODO`.
   - **Brevity over Description:** Prefer short, punchy lines. Narration should rarely exceed two or three sentences.
   - **Inner Monologue First:** Narration read as the character's internal voice — brief, direct, and revealing.
   - **Present Tense (Hard Rule):** All narration and inner monologue must be in the **present tense**. Correct existing text if necessary.

7. **Final Polish:** Ensure all dialogue sequences reach a natural conclusion and that the narrative flow feels professional and cohesive.

8. **Ignore**: Don't use the workflow `grammar_correction.md`. It's a different skill.