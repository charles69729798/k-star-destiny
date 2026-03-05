import sys
import os
import random

# Add backend directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from saju_engine import assemble_mz_report

# Dummy user data
user_name = "TestUser"
birth_date_str = "19950505"
birth_time_str = "1200"
gender = "f"
user_mbti = "ENFP"

# 30 Dummy Idols (mix of elements and MBTIs)
IDOLS = [
    ("Idol_1_W_ENFJ", "20000101", "ENFJ"), ("Idol_2_F_INTP", "20000202", "INTP"),
    ("Idol_3_E_ESFP", "20000303", "ESFP"), ("Idol_4_M_ISTJ", "20000404", "ISTJ"),
    ("Idol_5_W_ENTP", "20000505", "ENTP"), ("Idol_6_F_ISFJ", "20000606", "ISFJ"),
    ("Idol_7_E_ESTP", "20000707", "ESTP"), ("Idol_8_M_INFJ", "20000808", "INFJ"),
    ("Idol_9_W_ENFP", "20000909", "ENFP"), ("Idol_10_F_INTJ", "20001010", "INTJ"),
    ("Idol_11_E_ESFJ", "20001111", "ESFJ"), ("Idol_12_M_ISTP", "20001212", "ISTP"),
    ("Idol_13_W_ENTJ", "20010101", "ENTJ"), ("Idol_14_F_ISFP", "20010202", "ISFP"),
    ("Idol_15_E_ESTJ", "20010303", "ESTJ"), ("Idol_16_M_INFP", "20010404", "INFP"),
    ("Idol_17_W_ENFJ", "20010505", "ENFJ"), ("Idol_18_F_INTP", "20010606", "INTP"),
    ("Idol_19_E_ESFP", "20010707", "ESFP"), ("Idol_20_M_ISTJ", "20010808", "ISTJ"),
    ("Idol_21_W_ENTP", "20010909", "ENTP"), ("Idol_22_F_ISFJ", "20011010", "ISFJ"),
    ("Idol_23_E_ESTP", "20011111", "ESTP"), ("Idol_24_M_INFJ", "20011212", "INFJ"),
    ("Idol_25_W_ENFP", "20020101", "ENFP"), ("Idol_26_F_INTJ", "20020202", "INTJ"),
    ("Idol_27_E_ESFJ", "20020303", "ESFJ"), ("Idol_28_M_ISTP", "20020404", "ISTP"),
    ("Idol_29_W_ENTJ", "20020505", "ENTJ"), ("Idol_30_F_ISFP", "20020606", "ISFP")
]

def run_uniqueness_test(lang_code):
    print(f"\n[{lang_code.upper()}] Running Mission Uniqueness Test for 30 Idols...")
    all_generated_missions = []
    from saju_engine import analyze_destiny
    idol_mission_counts = {}

    for idol_name, idol_bdate, idol_mbti in IDOLS:
        # Request report via main pipeline function to handle i18n properly
        gender = "f" # fixed for test
        user_mbti = "ENFP" # fixed for test
        report = analyze_destiny(
            birth_date_str, gender, user_mbti,
            idol_name, idol_mbti, idol_bdate, lang_code
        )
        
        # Extract missions from chemistry_signal
        chemistry = report.get("chemistry_signal", {})
        missions = chemistry.get("synergy_missions", [])
        idol_tasks = []
        for m in missions:
            idol_tasks.extend(m.get("tasks", []))
            
        all_generated_missions.extend(idol_tasks)
        idol_mission_counts[idol_name] = len(idol_tasks)
        
    total_missions_generated = len(all_generated_missions)
    unique_missions = len(set(all_generated_missions))
    duplicate_count = total_missions_generated - unique_missions
    duplicate_rate = (duplicate_count / total_missions_generated) * 100 if total_missions_generated > 0 else 0
    
    print(f"Total Missions Generated: {total_missions_generated} (Expected: 30 idols * 9 missions = 270)")
    print(f"Unique Missions: {unique_missions}")
    print(f"Duplicate Missions (Collisions): {duplicate_count}")
    print(f"Collision Rate: {duplicate_rate:.2f}%")
    
    if duplicate_count > 0:
        print("\nSample Duplicates (Top 3):")
        from collections import Counter
        counts = Counter(all_generated_missions)
        dups = [item for item, count in counts.items() if count > 1]
        for d in dups[:3]:
            print(f"  - '{d}' (Appeared {counts[d]} times)")
            
    return total_missions_generated, unique_missions, duplicate_rate

if __name__ == "__main__":
    languages = ["ko", "en", "es", "pt"]
    results = {}
    
    print("==================================================")
    print("   Mission Generator Uniqueness Stress Test")
    print("==================================================")
    
    for lang in languages:
        total, unique, rate = run_uniqueness_test(lang)
        results[lang] = {
            "total": total,
            "unique": unique,
            "rate": rate
        }
        
    print("\n==================================================")
    print("   Final Report")
    print("==================================================")
    for lang, res in results.items():
        print(f"[{lang.upper()}] Collision Rate: {res['rate']:.2f}% ({res['unique']}/{res['total']} unique)")
