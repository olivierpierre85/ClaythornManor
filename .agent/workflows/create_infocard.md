---
description: Create a square infocard image for a 1920s murder mystery
---

1. **Prepare the prompt**
   - Take the user's description of the object or character for the infocard. Keep the description simple and focused on the main subject.
   - Append the required style modifiers: "simple 1920s style illustration, minimal details, dark and moody atmosphere, focused subject." 
   - CRITICAL: Ensure the image is borderless by avoiding prompts that ask for frames, or by explicitly asking for full-bleed artwork without mentioning borders.

2. **Generate the image**
   - Use the `generate_image` tool.
   - **Prompt**: [The user's description] + style modifiers.
   - **ImageName**: A descriptive snake_case name for the image without a suffix (e.g., `silver_letter_opener`).
   - **ImagePaths** (CRITICAL): You MUST pass 2 or 3 of the following reference images to match the established low-detail style:
     - `c:\Projects\ClaythornManor\Images\info_cards\old images\remember_nurse.png`
     - `c:\Projects\ClaythornManor\Images\info_cards\old images\opium_book.png`
     - `c:\Projects\ClaythornManor\Images\info_cards\old images\throat_cut.png`

3. **Save to the target folder**
   - The generated image will be in the artifacts directory.
   - You MUST copy or move the generated image to `c:\Projects\ClaythornManor\Images\info_cards`.
   - Ensure the filename is consistent with existing project naming conventions (snake_case).

4. **Verify the result**
   - Check that the image is correctly placed in `c:\Projects\ClaythornManor\Images\info_cards`.
   - Confirm the style matches the new "detailed oil painting" and "natural colors" requirements.
   - Check that there are absolutely no artificial borders or frames around the image.
