import sys

filename = r"c:\Projects\ClaythornManor\Murder\game\scripts\psychic\psychic_lord_locations.rpy"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_if = False
for i, line in enumerate(lines):
    if line.startswith('    lord """'):
        if i > 10 and i < 150: # Only the first occurrence inside psychic_attic_default
            in_if = True
    
    if in_if:
        if line.startswith('    return') and i < 150:
            # We reached the end of the block
            in_if = False
            new_lines.append(line) # keep return unindented so it returns from the label
            # wait, I also need to add the else block here.
            continue
        elif i < 150:
            if line == '\n':
                new_lines.append(line)
            else:
                new_lines.append("    " + line)
            continue

    new_lines.append(line)

with open(filename, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
