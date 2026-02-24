### **Claude Skill: Narrative Script Architect**

**Name:** `narrative_script_editor`

**Description:** Performs a targeted editorial pass on Ren'Py (.rpy) script files. This skill specialises in replacing "TODO" placeholders with context-aware prose and making minimal, necessary corrections to existing dialogue and narration, while strictly preserving code integrity and indentation.

**Instructions:**
1. **Scope & Identification:** - Identify the target file (primarily `.rpy` scripts). 
   - Isolate dialogue strings (e.g., `char "..."`) and narration blocks (enclosed in `"""` or `'''`).

2. **Code & Syntax Preservation (Hard Rule):** - **Do Not Modify:** Labels (`label:`), jumps (`jump`), calls (`call`), variable assignments (`$ var = ...`), or logic (`if/else`). 
   - **Indentation:** Maintain the exact original leading whitespace for every line to prevent script errors.
   - **Formatting:** Ensure all rewritten text remains properly enclosed in its original quote types.

3. **Contextual TODO Resolution:** - Locate all instances of `TODO`, `[TODO]`, or empty narrative brackets. 
   - Analyse the surrounding scene (preceding and following lines) to infer the intended mood and plot. 
   - Replace placeholders with fully-realised dialogue or inner-monologue beats that bridge the scene naturally.

4. **Light-Touch Editing (Conservative by Default):** - **Style Guide:** Strictly adhere to the linguistic rules defined in `grammar-style.md`.
   - **Editorial Mandate:** Preserve existing dialogue and narration unless there is a clear reason to change it. Do **not** rewrite text simply to vary the phrasing or add flavour.
     - **When to leave text unchanged:** If a line is grammatically correct, fits the character's voice, and reads naturally — leave it as-is.
     - **When to intervene:** Only modify existing text if it contains a grammar or spelling error, clearly breaks the character's established voice, is too modern/anachronistic for the 1924 setting, or is flagged as `TODO`.
     - **Minimal edits:** When a change is needed, make the smallest possible edit — fix the specific problem without restructuring surrounding sentences.
     - **Brevity over Description:** When writing new text (for TODOs), prefer short, punchy lines. A narration block should rarely exceed two or three sentences.
     - **Inner Monologue First:** New narration reads as the character's internal voice — brief, direct, and revealing. Favour thoughts over scene-painting.
     - **Pruning:** When writing new text, avoid filter words (e.g., "I saw," "He felt," "It seemed").

5. **Final Polish:** Ensure all dialogue sequences reach a natural conclusion and that the narrative flow feels professional and cohesive.

6. **Ignore**: Don't use the workflow grammar_correction.md. It's a different skill.