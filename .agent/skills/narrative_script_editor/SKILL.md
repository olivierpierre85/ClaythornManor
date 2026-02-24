### **Claude Skill: Narrative Script Architect**

**Name:** `narrative_script_editor`

**Description:** Performs a high-level editorial rewrite of Ren'Py (.rpy) script files. This skill specialises in replacing "TODO" placeholders with context-aware prose, rewriting narration as short inner-monologue beats, and refining character dialogue while strictly preserving code integrity and indentation.

**Instructions:**
1. **Scope & Identification:** - Identify the target file (primarily `.rpy` scripts). 
   - Isolate dialogue strings (e.g., `char "..."`) and narration blocks (enclosed in `"""` or `'''`).

2. **Code & Syntax Preservation (Hard Rule):** - **Do Not Modify:** Labels (`label:`), jumps (`jump`), calls (`call`), variable assignments (`$ var = ...`), or logic (`if/else`). 
   - **Indentation:** Maintain the exact original leading whitespace for every line to prevent script errors.
   - **Formatting:** Ensure all rewritten text remains properly enclosed in its original quote types.

3. **Contextual TODO Resolution:** - Locate all instances of `TODO`, `[TODO]`, or empty narrative brackets. 
   - Analyse the surrounding scene (preceding and following lines) to infer the intended mood and plot. 
   - Replace placeholders with fully-realised dialogue or inner-monologue beats that bridge the scene naturally.

4. **Editorial Overhaul:** - **Style Guide:** Strictly adhere to the linguistic rules defined in `grammar-style.md`.
   - **Editorial Mandate:** This is a full rewrite, not a grammar correction.
     - **Brevity over Description:** Prefer short, punchy lines of inner dialogue over long descriptive passages. A narration block should rarely exceed two or three sentences. If it can be said in one line, say it in one line.
     - **Inner Monologue First:** Narration reads as the character's internal voice — brief, direct, and revealing. Favour thoughts over scene-painting. The character reacts; they do not describe the room.
     - **Voice & Subtext:** Refine dialogue to reflect unique character rhythms, slang, and implied emotion.
     - **Pruning:** Remove redundant sentences and filter words (e.g., "I saw," "He felt," "It seemed") to increase player immersion.

5. **Final Polish:** Ensure all dialogue sequences reach a natural conclusion and that the narrative flow feels professional and cohesive.

6. **Ignore**: Don't use the workflow grammar_correction.md. It's a different skill.