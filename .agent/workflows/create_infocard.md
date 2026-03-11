---
description: Create a square infocard image for a 1920s murder mystery
---

1. **Prepare the prompt**
   - Take the user's description of the object or character for the infocard.
   - Append the required style modifiers: "detailed oil painting illustration, rich natural color palette, intricate textures, full-frame composition filling the entire square area, painterly 1920s historical style, dark and moody atmosphere." 
   - CRITICAL: Ensure the image is borderless by avoiding prompts that ask for frames, or by explicitly asking for full-bleed artwork without mentioning borders.

2. **Generate the image**
   - Use the `generate_image` tool.
   - **Prompt**: [The user's description] + style modifiers.
   - **ImageName**: A descriptive snake_case name for the image (e.g., `silver_letter_opener_infocard`).

3. **Save to the target folder**
   - The generated image will be in the artifacts directory.
   - You MUST copy or move the generated image to `c:\Projects\ClaythornManor\Images\info_cards`.
   - Ensure the filename is consistent with existing project naming conventions (snake_case).

4. **Verify the result**
   - Check that the image is correctly placed in `c:\Projects\ClaythornManor\Images\info_cards`.
   - Confirm the style matches the new "detailed oil painting" and "natural colors" requirements.
   - Check that there are absolutely no artificial borders or frames around the image.
