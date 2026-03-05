import sys
import os

# Add the backend folder to sys.path so we can import backend modules directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from saju_engine import analyze_destiny

def test_tips():
    user_birth_date = "1994-01-01"
    user_birth_time = "1000"
    user_gender = "M"
    user_mbti = "INFP"

    idol_cases = [
        {"name": "Karina", "mbti": "ENFP", "birth_date": "2000-04-11", "is_friend": False},
        {"name": "Wonbin", "mbti": "ISTJ", "birth_date": "2002-03-02", "is_friend": False},
        {"name": "Minji", "mbti": "ESTP", "birth_date": "2004-05-07", "is_friend": True},
        {"name": "Jason", "mbti": "ENTJ", "birth_date": "1995-11-11", "is_friend": True}
    ]

    langs = ['ko', 'en', 'es', 'pt']
    
    for case in idol_cases:
        print(f"\n==========================================")
        print(f"Testing Target: {case['name']} (MBTI: {case['mbti']}, Friend Mode: {case['is_friend']})")
        print(f"==========================================")
        for lang in langs:
            print(f"\n[{lang.upper()}] Tips:")
            res = analyze_destiny(
                birth_date_str=user_birth_date,
                gender=user_gender,
                user_mbti=user_mbti,
                idol_name=case['name'],
                idol_mbti=case['mbti'],
                idol_birth_date=case['birth_date'],
                lang=lang,
                is_friend=case['is_friend']
            )
            
            tips = res.get("chemistry_signal", {}).get("tips", [])
            for i, tip in enumerate(tips):
                print(f"  {i+1}. {tip}")

if __name__ == "__main__":
    test_tips()
