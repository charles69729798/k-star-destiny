import json
from saju_engine import analyze_destiny

print("--- 3x3 MISSION (ACTION GUIDES) UAT CHECK ---\n")

user_profile = {"birth_date": "1995-10-13", "gender": "female"}
idol_info = {"name": "LISA (BLACKPINK)", "birth_date": "1997-03-27"}
mbti_info = {"userMBTI": "ENFP", "idolMBTI": "ISFP"}

for lang in ["ko", "en", "es", "pt"]:
    res = analyze_destiny(
        birth_date_str=user_profile["birth_date"],
        gender=user_profile["gender"],
        user_mbti=mbti_info.get("userMBTI"),
        idol_name=idol_info["name"],
        idol_mbti=mbti_info.get("idolMBTI"),
        idol_birth_date=idol_info["birth_date"],
        lang=lang
    )
    missions = res.get("chemistry_signal", {}).get("synergy_missions", [])
    
    print(f"[{lang.upper()} MISSIONS]")
    if not missions:
        print("  ❌ No missions returned.")
        continue
        
    for m in missions:
        print(f"  ■ Title: {m.get('label')}")
        print(f"    Sub-tasks:")
        for t in m.get('tasks', []):
            print(f"      - {t}")
    print()
