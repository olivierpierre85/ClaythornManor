---
description: Correct grammar in the latest test results and apply changes to the codebase.
---

1. **Find the latest test result file**
   - List the contents of `c:\Projects\ClaythornManor\Murder\testing_results`.
   - Identify the most recently modified file or directory (and look for relevant result files inside if it's a directory, typically `.json` or `.txt` logs).

2. **Analyze for Grammar and Style**
   - Read the content of the latest test result file.
   - identifying lines of dialogue or narration that violate the project's grammar/style rules (grammar-style.md)

3. **Generate Replacements**
   - Create a list of corrections in the format: `Original Sentence <TAB> New Sentence`.
   - **Crucial**: The "Original Sentence" must match the *exact* line in the code (excluding indentation). If the test result shows a cleaned version, you might need to find the exact source line in the `.rpy` files using `grep_search` if necessary, but typically the test output mirrors the text.
   - Ignore lines that are already correct or don't need changes.

4. **Update `replacements.tsv`**
   - Read the existing `c:\Projects\ClaythornManor\Murder\replacements.tsv` to ensure no duplicates.
   - Append the new TAB-separated pairs to the file.
   - **Format**: `Old Text\tNew Text` (No header updates needed, just append lines).

5. **Apply Changes to Codebase**
   - Run the bulk replacement script:
     ```powershell
     python c:\Projects\ClaythornManor\Murder\bulk_sentence_replace_triple.py c:\Projects\ClaythornManor\Murder c:\Projects\ClaythornManor\Murder\replacements.tsv
     ```
   - Verify the output of the script to see how many lines were replaced.