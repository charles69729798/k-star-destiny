import sys

with open('backend/saju_i18n.py', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if '"en": {' in line or '"es": {' in line or '"pt": {' in line or '"MISSION_COMPONENTS": {' in line:
            print(f"{idx+1}: {line.strip()}")
