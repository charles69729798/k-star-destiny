import sys
import os
import random
import json
from datetime import datetime, timedelta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from saju_engine import analyze_destiny

def generate_mock_users(n=10):
    users = []
    mbtis = ["INTJ", "ENTP", "ISFJ", "ESFP", "INFJ", "ENFP", "ISTP", "ESTJ", "", "INFP"]
    base_date = datetime(1995, 1, 1)
    for i in range(n):
        users.append({
            "birth_date": (base_date + timedelta(days=random.randint(0, 3650))).strftime("%Y-%m-%d"),
            "gender": random.choice(["female", "male"]),
            "mbti": mbtis[i % len(mbtis)]
        })
    return users

def generate_mock_idols(n=100):
    idols = []
    mbtis = ["INTJ", "ENTP", "ISFJ", "ESFP", "INFJ", "ENFP", "ISTP", "ESTJ", "Unknown", "INTP", "ENTJ", "ISFP", "ESFJ", "ISTJ", "ESTP", "ENFJ"]
    base_date = datetime(2000, 1, 1)
    for i in range(n):
        idols.append({
            "name": f"Idol_{i}",
            "mbti": random.choice(mbtis),
            "birth_date": (base_date + timedelta(days=random.randint(0, 1500))).strftime("%Y-%m-%d")
        })
    return idols

def run_simulation():
    users = generate_mock_users(10)
    idols = generate_mock_idols(100)
    
    # 10 user x 100 idols = 1000 cases
    theme1_set = set()
    theme2_set = set() # checking intra-month duplicates
    theme3_set = set()
    
    intra_month_duplicate_count = 0
    en_translation_check = []
    es_translation_check = []

    for u in users:
        for i in idols:
            # KO Test
            res_ko = analyze_destiny(
                birth_date_str=u["birth_date"],
                gender=u["gender"],
                user_mbti=u["mbti"],
                idol_name=i["name"],
                idol_mbti=i["mbti"],
                idol_birth_date=i["birth_date"],
                lang="ko"
            )
            
            # 1. Theme 1 (user_saju)
            t1_text = res_ko.get("user_saju", {}).get("content", "")
            theme1_set.add(t1_text)
            
            # 2. Theme 2 (month)
            months = res_ko.get("monthly_fortune", [])
            month_descs = [m["desc"] for m in months]
            if len(set(month_descs)) < len(month_descs):
                intra_month_duplicate_count += 1
            
            # 3. Theme 3 (chemistry)
            chem = res_ko.get("chemistry_signal", {})
            t3_text = chem.get("idol_love_style", "") + chem.get("synergy", "") + "".join(chem.get("tips", []))
            theme3_set.add(t3_text)

    # Check one EN/ES translation explicitly
    res_en = analyze_destiny("1995-01-01", "female", "INTJ", "Idol_0", "ENTP", "2000-01-01", "en")
    res_es = analyze_destiny("1995-01-01", "female", "INTJ", "Idol_0", "ENTP", "2000-01-01", "es")
    
    print("=== SIMULATION RESULTS (10 Users x 100 Idols = 1000 Cases) ===")
    print(f"Total Unique Theme 1 (Soul Index) Results: {len(theme1_set)} / 1000")
    print(f"Total Cases with Intra-Month Duplications (Theme 2): {intra_month_duplicate_count} / 1000")
    print(f"Total Unique Theme 3 (Chemistry) Results: {len(theme3_set)} / 1000")
    print("\n--- Translation Check Sample ---")
    print(f"EN Soul Index Intro Valid: {'Unstoppable' in res_en['user_saju']['content'] or 'Burning' in res_en['user_saju']['content'] or 'Solid' in res_en['user_saju']['content'] or 'Sharp' in res_en['user_saju']['content'] or 'Free Flow' in res_en['user_saju']['content']}")
    print(f"ES Soul Index Intro Valid: {'Crecimiento' in res_es['user_saju']['content'] or 'Llama' in res_es['user_saju']['content'] or 'Sólida' in res_es['user_saju']['content'] or 'Afilada' in res_es['user_saju']['content'] or 'Libre' in res_es['user_saju']['content']}")
    
if __name__ == "__main__":
    run_simulation()
