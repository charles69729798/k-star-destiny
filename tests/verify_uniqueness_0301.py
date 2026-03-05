import sys
import os
import random
from datetime import datetime, timedelta

# PYTHONPATH 설정 (backend 및 내부 모듈 접근을 위함)
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), "backend"))

from backend.saju_engine import analyze_destiny

def generate_random_birth():
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2010, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def run_uniqueness_test(iterations=500):
    mbtis = ["ENFP", "INFJ", "INTJ", "ENTP", "ISFP", "ESFJ", "ISTJ", "ESTP", 
             "ENFJ", "INFP", "INTP", "ENTJ", "ISFJ", "ESFP", "ISTP", "ESTJ"]
    
    results = []
    unique_full_reports = set()
    
    components = {
        "relationship": [],
        "bias": [],
        "tmi": [],
        "synergyWhy": []
    }
    
    print(f"🚀 {iterations}회 알고리즘 유니크성 시뮬레이션 시작...")
    
    for i in range(iterations):
        u_birth = generate_random_birth()
        i_birth = generate_random_birth()
        u_mbti = random.choice(mbtis)
        i_mbti = random.choice(mbtis)
        
        analysis = analyze_destiny(
            birth_date_str=u_birth,
            user_mbti=u_mbti,
            idol_name="TestIdol",
            idol_birth_date=i_birth,
            idol_mbti=i_mbti,
            lang="ko"
        )
        
        signal = analysis.get("chemistry_signal", {})
        
        # 핵심 컴포넌트 추출
        report_tuple = (
            signal.get("relationship"),
            signal.get("bias"),
            signal.get("tmi"),
            signal.get("synergyWhy")
        )
        
        results.append(report_tuple)
        unique_full_reports.add(report_tuple)
        
        for key in components:
            components[key].append(signal.get(key))
            
    # 결과 요약
    print("\n" + "="*50)
    print("📊 알고리즘 유니크성 분석 리포트")
    print("="*50)
    print(f"- 총 테스트 시나리오: {iterations}")
    print(f"- 완전히 고유한 리포트 세트: {len(unique_full_reports)} / {iterations}")
    print(f"- 유니크 성공률: {(len(unique_full_reports)/iterations)*100:.2f}%")
    
    print("\n[컴포넌트별 고유 문장 수]")
    for key, val_list in components.items():
        u_count = len(set(val_list))
        print(f" - {key:<15}: {u_count}개")
        
    if len(unique_full_reports) < iterations * 0.95:
        print("\n⚠️ 경고: 결과 중복률이 예상보다 높습니다. 해시 로직 개선을 권장합니다.")
    else:
        print("\n✅ 성공: 알고리즘의 유니크성이 충분히 확보되었습니다.")
    print("="*50)

if __name__ == "__main__":
    run_uniqueness_test(500)
