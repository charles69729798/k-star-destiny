import os

file_path = 'c:/InsuranceProject/Sajuapp/backend/saju_i18n.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace tabs with 4 spaces
content = content.replace('\t', '    ')

lines = content.splitlines()
new_lines = []

for line in lines:
    if not line.strip():
        new_lines.append('')
    else:
        # Standardize indentation
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        new_lines.append(' ' * indent + stripped)

with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(new_lines) + '\n')

print("Successfully cleaned saju_i18n.py indentation.")
