from saju_engine import analyze_destiny, calc_dominant
import json

def test_theory_alignment():
    print("Testing Theory Alignment and Determinism...")
    
    # Test cases: (Birth, Gender, MBTI)
    user_samples = [
        ("1990-01-01", "female", "ENFP"), # Wood (likely)
        ("1995-05-05", "male", "INTJ"),   # Fire (likely)
        ("2000-10-10", "female", "ISTJ"), # Earth (likely)
    ]
    
    idol_samples = [
        ("Wonyoung", "2004-08-31", "ENFP"),
        ("Karina", "2000-04-11", "ENFP"),
    ]

    for b_date, gender, mbti in user_samples:
        dominant = calc_dominant(b_date)
        print(f"\n--- Testing User: {b_date} ({gender}, {mbti}) -> Dominant: {dominant} ---")
        
        # 1. Determinism Check
        res1 = analyze_destiny(b_date, gender, mbti, idol_name="TestIdol", idol_birth_date="2000-01-01", lang="ko")
        res2 = analyze_destiny(b_date, gender, mbti, idol_name="TestIdol", idol_birth_date="2000-01-01", lang="ko")
        
        d1 = json.dumps(res1, sort_keys=True, indent=2)
        d2 = json.dumps(res2, sort_keys=True, indent=2)
        
        if d1 == d2:
            print("[PASS] Determinism: Results are consistent.")
        else:
            print("[FAIL] Determinism: Results differ!")
            # Save for debugging
            with open("DEBUG_res1.json", "w", encoding="utf-8") as f: f.write(d1)
            with open("DEBUG_res2.json", "w", encoding="utf-8") as f: f.write(d2)

        # 2. Theory Alignment (Lifetime Fortune)
        lifetime = res1.get("lifetime_fortune", "")
        print(f"Lifetime Fortune: {lifetime}")
        
        element_map = {"Wood": "목", "Fire": "화", "Earth": "토", "Metal": "금", "Water": "수"}
        expected_kw = element_map.get(dominant)
        if expected_kw and expected_kw in lifetime:
            print(f"[PASS] Theory Alignment: Fortune matches dominant element ({expected_kw}).")
        else:
            print(f"[NOTE] Theory Alignment: No specific element keyword found or different.")

        # 3. Synergy Score Range Check
        score = res1["chemistry_signal"]["base_synergy_score"]
        print(f"Synergy Score: {score}")
        if 65 <= score <= 100:
            print(f"[PASS] Score Range: {score} is valid.")
        else:
            print(f"[FAIL] Score Range: {score} is out of bounds!")

        # 4. Missions check
        missions = res1["chemistry_signal"]["synergy_missions"]
        print(f"Missions selected: {len(missions)}")
        for m in missions:
            print(f" - {m['tasks'][0]}")

if __name__ == "__main__":
    test_theory_alignment()
