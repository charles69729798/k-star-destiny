import os
import sys
import json
import random
from datetime import datetime, timedelta

# backend 경로 추가
sys.path.append(os.path.join(os.getcwd(), 'backend'))
from saju_engine import analyze_destiny

def generate_random_user(idx):
    # 1990년 ~ 2005년 사이 랜덤 생일
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2005, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    birth = start_date + timedelta(days=random_days)
    
    mbtis = [
        "ENFP", "INFJ", "INTJ", "ENTP", "ENFJ", "INFP", "ISFP", "ESFP",
        "ISTP", "ESTP", "ISFJ", "ESFJ", "ISTJ", "ESTJ", "INTP", "ENTJ"
    ]
    
    return {
        "id": idx + 1,
        "name": f"User_{idx+1}",
        "birth_date": birth.strftime("%Y-%m-%d"),
        "mbti": random.choice(mbtis)
    }

def run_100_simulation():
    print(f"🚀 100인 가상 유저 시뮬레이션 시작 (데이터 풀 1,000+ 검증)")
    print(f"시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = []
    unique_tips = set()
    unique_missions = set()
    unique_bias = set()
    
    # 대표 아이돌: 카리나 (11일 차이 케이스와 별개로 고정)
    idol = {"name": "카리나", "birth": "2000-04-11", "mbti": "ENFP"}
    
    for i in range(100):
        user = generate_random_user(i)
        
        analysis = analyze_destiny(
            birth_date_str=user["birth_date"], 
            user_mbti=user["mbti"], 
            idol_name=idol["name"], 
            idol_birth_date=idol["birth"], 
            idol_mbti=idol["mbti"], 
            lang="ko"
        )
        
        chem = analysis.get("chemistry_signal", {})
        
        # 유니크성 체크를 위한 키 생성
        tips_key = tuple(sorted(chem.get("tips", [])))
        mission_key = tuple(sorted([(m.get('label'), m.get('reason')) for m in chem.get("synergy_missions", [])]))
        bias_text = chem.get("bias", "")
        
        unique_tips.add(tips_key)
        unique_missions.add(mission_key)
        unique_bias.add(bias_text)
        
        # 샘플 저장 (10개마다 하나씩 상세 저장)
        if i % 10 == 0:
            results.append({
                "user": user,
                "analysis_sample": {
                    "bias": bias_text,
                    "tips": chem.get("tips", []),
                    "missions": [m.get('label') for m in chem.get("synergy_missions", [])]
                }
            })

    print("\n" + "="*50)
    print("📊 100인 시뮬레이션 결과 요약")
    print("="*50)
    print(f"- 총 테스트 인원: 100명")
    print(f"- 상대방 성향(5문장) 유니크: {len(unique_bias)} / 100")
    print(f"- 공략 꿀팁 조합 유니크: {len(unique_tips)} / 100")
    print(f"- 시너지 치트키 조합 유니크: {len(unique_missions)} / 100")
    print("="*50)
    
    # 결과 파일 저장
    output = {
        "summary": {
            "total": 100,
            "unique_bias": len(unique_bias),
            "unique_tips": len(unique_tips),
            "unique_missions": len(unique_missions)
        },
        "samples": results
    }
    
    with open("tests/simulation_results_100_0301.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 결과가 tests/simulation_results_100_0301.json 에 저장되었습니다.")

if __name__ == "__main__":
    run_100_simulation()
