import sys
import os
import random
import json
from datetime import datetime, timedelta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from saju_engine import analyze_destiny
from saju_i18n import get_localized_data

def run_10x20_simulation():
    users = []
    mbtis = ["INTJ", "ENTP", "ISFJ", "ESFP", "INFJ", "ENFP", "ISTP", "ESTJ", "ISFP", "INFP"]
    base_date = datetime(2000, 1, 1)
    for i in range(10):
        users.append({
            "name": f"User_{i}",
            "birth_date": (base_date + timedelta(days=random.randint(0, 3650))).strftime("%Y-%m-%d"),
            "gender": random.choice(["female", "male"]),
            "mbti": mbtis[i]
        })

    idols = []
    for i in range(20):
        idols.append({
            "name": f"Idol_{i}",
            "mbti": random.choice(mbtis),
            "birth_date": (base_date + timedelta(days=random.randint(0, 1500))).strftime("%Y-%m-%d")
        })

    theme1_set = set()
    intra_month_duplicate_count = 0
    theme3_set = set()
    
    # Run 10 x 20 = 200 cases
    for u in users:
        for i in idols:
            res_ko = analyze_destiny(
                birth_date_str=u["birth_date"],
                gender=u["gender"],
                user_mbti=u["mbti"],
                idol_name=i["name"],
                idol_mbti=i["mbti"],
                idol_birth_date=i["birth_date"],
                lang="ko"
            )
            
            # Theme 1
            t1_text = res_ko.get("user_saju", {}).get("content", "")
            theme1_set.add(t1_text)
            
            # Theme 2
            months = res_ko.get("monthly_fortune", [])
            month_descs = [m["desc"] for m in months]
            if len(set(month_descs)) < len(month_descs):
                intra_month_duplicate_count += 1
                
            # Theme 3
            chem = res_ko.get("chemistry_signal", {})
            t3_text = chem.get("idol_love_style", "") + chem.get("synergy", "") + "".join(chem.get("tips", []))
            theme3_set.add(t3_text)

    print("=== 10x20 시뮬레이션 결과 (총 200건) ===")
    print(f"Theme 1 (고유 본질 분석 결과 수): {len(theme1_set)} / 200")
    print(f"Theme 2 (월별 캘린더 중복 발생 건수): {intra_month_duplicate_count} / 200")
    print(f"Theme 3 (고유 궁합 결과 수): {len(theme3_set)} / 200")
    
    # 텍스트 샘플 추출 (Fire 요소 - ENTP 테스트)
    print("\n=== 영어/스페인어 원어민 에이전트 피드백용 텍스트 샘플 (Fire 요소 예시) ===")
    en_data = get_localized_data("en")
    es_data = get_localized_data("es")
    
    print("[EN] Fire - desc_intro:", en_data["ENERGY_TRAITS"]["Fire"]["desc_intro"][0])
    print("[EN] Fire - desc_core (E):", en_data["ENERGY_TRAITS"]["Fire"]["desc_core"]["E"][0])
    print("[EN] Fire - desc_career:", en_data["ENERGY_TRAITS"]["Fire"]["desc_career"][0])
    
    print("\n[ES] Fire - desc_intro:", es_data["ENERGY_TRAITS"]["Fire"]["desc_intro"][0])
    print("[ES] Fire - desc_core (E):", es_data["ENERGY_TRAITS"]["Fire"]["desc_core"]["E"][0])
    print("[ES] Fire - desc_career:", es_data["ENERGY_TRAITS"]["Fire"]["desc_career"][0])

if __name__ == "__main__":
    run_10x20_simulation()
