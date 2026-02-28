import re
import json
import sys

def find_korean_remnants(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract the dictionary content (basic estimation)
        # Assuming the structure is like LANG_DATA = { ... }
        
        # Regex to find Korean characters: [가-힣]
        korean_pattern = re.compile(r'[가-힣]+')
        
        # We want to find Korean text inside "en", "es", "pt" sections
        # This is a bit complex with regex on a python file, 
        # but let's look for lines that contain Korean AND are likely in non-ko sections.
        
        lines = content.split('\n')
        remnants = []
        current_lang = None
        
        for i, line in enumerate(lines):
            # Detect language section
            lang_match = re.search(r'"(en|es|pt|ko)"\s*:', line)
            if lang_match:
                current_lang = lang_match.group(1)
            
            if current_lang and current_lang != 'ko':
                matches = korean_pattern.findall(line)
                if matches:
                    remnants.append({
                        "line": i + 1,
                        "lang": current_lang,
                        "text": line.strip(),
                        "matches": matches
                    })
        
        return remnants
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    path = r"c:\InsuranceProject\Sajuapp\backend\saju_i18n.py"
    results = find_korean_remnants(path)
    if isinstance(results, list):
        for r in results:
            print(f"[{r['lang']}] Line {r['line']}: {r['text']} (Found: {', '.join(r['matches'])})")
    else:
        print(f"Error: {results}")
