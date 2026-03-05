import sys
import os
import random
from datetime import datetime, timedelta

# PYTHONPATH 설정
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), "backend"))

from backend.saju_engine import analyze_destiny

def generate_random_birth():
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2010, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def debug_uniqueness():
    mbtis = ["ENFP", "INFJ"]
    print("🐞 [디버그] 미션 데이터 실체 확인 (5회 실행)")
    
    for i in range(5):
        u_birth = generate_random_birth()
        i_birth = generate_random_birth()
        u_mbti = random.choice(mbtis)
        i_mbti = random.choice(mbtis)
        
        analysis = analyze_destiny(
            birth_date_str=u_birth,
            user_mbti=u_mbti,
            idol_name="윈터",
            idol_birth_date=i_birth,
            idol_mbti=i_mbti,
            lang="ko"
        )
        
        missions = analysis.get("chemistry_signal", {}).get("synergy_missions", [])
        print(f"\n[Iteration {i+1}] {u_birth}/{u_mbti} -> {i_birth}/{i_mbti}")
        if not missions:
            print("  ❌ No missions found in chemistry_signal!")
        for m in missions:
            print(f" - ID: {repr(m['id'])}, Label: {repr(m['label'])}, Reason: {repr(m['reason'][:50])}...")

if __name__ == "__main__":
    debug_uniqueness()
