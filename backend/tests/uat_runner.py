import json
import re
import os
import sys
from datetime import datetime
from typing import List, Dict, Any

# Add backend directory to path
sys.path.append(os.path.dirname(__file__))

from saju_engine import analyze_destiny
from saju_i18n import I18N_DATA

from main import IDOL_POOL

# 1. Test Data Definition (From test_matrix_global.md)
PERSONAS = [
    {"id": "U1", "name": "Minji", "lang": "ko", "birth": "1998-05-12", "gender": "female", "mbti": "ENFP"},
    {"id": "U2", "name": "James", "lang": "en", "birth": "1995-12-25", "gender": "male", "mbti": "INTJ"},
    {"id": "U3", "name": "Garcia", "lang": "es", "birth": "1990-01-01", "gender": "female", "mbti": "ESFJ"},
    {"id": "U4", "name": "Silva", "lang": "pt", "birth": "2002-08-15", "gender": "male", "mbti": "INFP"},
    {"id": "U5", "name": "Yuki", "lang": "en", "birth": "2005-03-03", "gender": "female", "mbti": "ISFP"},
    {"id": "U6", "name": "Kim", "lang": "ko", "birth": "1985-11-20", "gender": "male", "mbti": "ISTJ"},
    {"id": "U7", "name": "Elena", "lang": "es", "birth": "1997-07-07", "gender": "female", "mbti": "ENFJ"},
    {"id": "U8", "name": "Joao", "lang": "pt", "birth": "1993-04-20", "gender": "male", "mbti": "ENTP"},
    {"id": "U9", "name": "Smith", "lang": "en", "birth": "2000-02-29", "gender": "female", "mbti": "INFJ"}, # Leap Year
    {"id": "U10", "name": "Park", "lang": "ko", "birth": "2010-10-10", "gender": "female", "mbti": "ENTJ"},
]

STARS = [
    {"name_kr": idol["name_kr"], "name_en": idol["name_en"], "mbti": idol["mbti"], "birth": idol["birth_date"]}
    for idol in IDOL_POOL
]

def contains_korean(text: str) -> bool:
    if not text: return False
    return bool(re.search('[가-힣]', text))

def run_uat():
    results = []
    total_tests = len(PERSONAS) * len(STARS)
    passed = 0
    failures = []

    print(f"🚀 Starting UAT Runner: {total_tests} combinations...")

    for user in PERSONAS:
        for star in STARS:
            try:
                # Use name_kr or name_en based on user lang
                star_name = star["name_kr"] if user["lang"] == "ko" else star["name_en"]
                
                # Execute engine
                analysis = analyze_destiny(
                    birth_date_str=user["birth"],
                    gender=user["gender"],
                    user_mbti=user["mbti"],
                    idol_name=star_name,
                    idol_mbti=star["mbti"],
                    idol_birth_date=star["birth"],
                    lang=user["lang"]
                )

                # 1. Validation: Language Integrity (Non-residue)
                lang_fail = False
                if user["lang"] != "ko":
                    # Check key text fields
                    fields_to_check = [
                        analysis["user_saju"]["content"],
                        analysis["lifetime_fortune"],
                        analysis["chemistry_signal"]["synergy"]
                    ] + [m["label"] for m in analysis["chemistry_signal"]["synergy_missions"]]
                    
                    for f in fields_to_check:
                        if contains_korean(f):
                            lang_fail = True
                            failures.append(f"[{user['id']}-{star_name}] Korean residue found in {user['lang']} output.")
                            break

                # 2. Validation: Data Integrity (Check if birth dates match in summary if possible, or just engine crash)
                if not analysis or "error" in analysis:
                    failures.append(f"[{user['id']}-{star_name}] Engine error occurred.")
                    continue

                if not lang_fail:
                    passed += 1

            except Exception as e:
                failures.append(f"[{user['id']}-{star_name}] Exception: {str(e)}")

    # 3. Generate Report
    report_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", ".gemini", "antigravity", "brain", "d64370ba-7db7-4720-bdb4-440d2de7350b", "uat_result_summary.md")
    # Normalize path if needed for environment
    
    with open("uat_report.md", "w", encoding="utf-8") as f:
        f.write(f"# UAT Execution Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## Summary\n")
        f.write(f"- **Total Tests**: {total_tests}\n")
        f.write(f"- **Passed**: {passed}\n")
        f.write(f"- **Failed**: {len(failures)}\n")
        f.write(f"- **Success Rate**: {(passed/total_tests)*100:.1f}%\n\n")
        
        if failures:
            f.write(f"## Failures\n")
            for fail in failures:
                f.write(f"- {fail}\n")
        else:
            f.write(f"## ✅ All Tests Passed\n")
            f.write("No Korean residue detected in foreign language modes. No engine crashes detected.\n")

    print(f"✅ UAT Finished. Report generated: uat_report.md")

if __name__ == "__main__":
    run_uat()
