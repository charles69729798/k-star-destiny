file_path = 'c:/InsuranceProject/Sajuapp/backend/saju_i18n.py'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

stack = 0
for i, line in enumerate(lines):
    stripped = line.strip()
    # Count braces ignoring comments (simplified)
    open_braces = line.count('{')
    close_braces = line.count('}')
    
    prev_stack = stack
    stack += open_braces - close_braces
    
    if (i+1) in [434, 435, 436, 931, 932, 933]:
        print(f"Line {i+1}: stack {prev_stack} -> {stack} | {repr(line)}")

if stack != 0:
    print(f"Final stack: {stack} (Structural Mismatch!)")
else:
    print("Braces are balanced.")
