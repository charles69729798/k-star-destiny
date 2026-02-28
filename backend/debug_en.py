from saju_engine import analyze_destiny
import json

try:
    res = analyze_destiny(
        birth_date_str="1990-01-01", 
        gender="male", 
        user_mbti="ENTJ",
        idol_name="TestIdol", 
        idol_mbti="ENFP", 
        idol_birth_date="1995-01-01",
        lang="en"
    )
    print(json.dumps(res, indent=2))
except Exception as e:
    print(f"FAILED: {e}")
