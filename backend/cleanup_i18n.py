import re
import os

file_path = r'c:\InsuranceProject\Sajuapp\backend\saju_i18n.py'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove "(단계 X)" and "(Level X)" from MONTH_KEYWORDS and other places
# Pattern: space followed by (단계 or Level followed by digits and )
content = re.sub(r'\s*\((?:단계|Level)\s*\d+\)', '', content)

# 2. Fix literal \\n to actual \n (inside strings)
# Note: we need to be careful not to break actual escape sequences if they are intended as such for some reason, 
# but in this file, \\n seems to be a mistake where \n was intended.
# In Python strings, if it's r'\\n' it's literal. If it's '\\n' it's also literal backslash n.
# We want actual newlines in the JSON-like structure or single \n which is processed by Python.
content = content.replace('\\\\n', '\\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleanup complete.")
