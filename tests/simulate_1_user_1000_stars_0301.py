import os
import sys
import json
import random
from datetime import datetime, timedelta

# backend 경로 추가
sys.path.append(os.path.join(os.getcwd(), 'backend'))
from saju_engine import analyze_destiny

def generate_random_star(idx):
    # 스타는 다양한 연령대로 생성 (1980~2010)
    start_date = datetime(1980, 1, 1)
    end_date = datetime(2010, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    birth = start_date + timedelta(days=random_days)
    
    mbtis = [
        "ENFP", "INFJ", "INTJ", "ENTP", "ENFJ", "INFP", "ISFP", "ESFP",
        "ISTP", "ESTP", "ISFJ", "ESFJ", "ISTJ", "ESTJ", "INTP", "ENTJ"
    ]
    
    return {
        "id": idx + 1,
        "name": f"MegaStar_{idx+1}",
        "birth_date": birth.strftime("%Y-%m-%d"),
        "mbti": random.choice(mbtis)
    }

def run_1vs1000_simulation():
    print(f"🚀 1인 vs 1,000인 스타 대규모 시뮬레이션 시작")
    print(f"시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 고정 유저: 1995-05-05 (INFJ)
    user = {"name": "K-Destiny_Fan", "birth": "1995-05-05", "mbti": "INFJ"}
    
    results = []
    unique_tips = set()
    unique_missions = set()
    unique_bias = set()
    scores = []
    
    for i in range(1000):
        star = generate_random_star(i)
        
        analysis = analyze_destiny(
            birth_date_str=user["birth"], 
            user_mbti=user["mbti"], 
            idol_name=star["name"], 
            idol_birth_date=star["birth_date"], 
            idol_mbti=star["mbti"], 
            lang="ko"
        )
        
        chem = analysis.get("chemistry_signal", {})
        
        # 유니크성 체크
        tips_key = tuple(sorted(chem.get("tips", [])))
        mission_key = tuple(sorted([(m.get('label'), m.get('reason')) for m in chem.get("synergy_missions", [])]))
        bias_text = chem.get("bias", "")
        score = chem.get("base_synergy_score", 0)
        
        unique_tips.add(tips_key)
        unique_missions.add(mission_key)
        unique_bias.add(bias_text)
        scores.append(score)
        
        # 100개마다 진행 상황 출력
        if (i + 1) % 100 == 0:
            print(f"진행 중... {i+1}/1000 완료")
            
        # 샘플 저장 (100개마다 하나씩 상세 저장)
        if i % 100 == 0:
            results.append({
                "star": star,
                "score": score,
                "analysis_sample": {
                    "bias": bias_text,
                    "tips": chem.get("tips", []),
                    "missions": [m.get('label') for m in chem.get("synergy_missions", [])]
                }
            })

    print("\n" + "="*50)
    print("📊 1인 vs 1,000인 스타 시뮬레이션 결과 요약")
    print("="*50)
    print(f"- 고정 유저: {user['name']} ({user['birth']}, {user['mbti']})")
    print(f"- 총 테스트 스타 수: 1,000명")
    print(f"- 상대방 성향(5문장) 유니크: {len(unique_bias)} / 1000")
    print(f"- 공략 꿀팁 조합 유니크: {len(unique_tips)} / 1000")
    print(f"- 시너지 치트키 조합 유니크: {len(unique_missions)} / 1000")
    print(f"- 평균 시너지 점수: {sum(scores)/len(scores):.2f}")
    print(f"- 최고 점수: {max(scores)} / 최저 점수: {min(scores)}")
    print("="*50)
    
    # 결과 파일 저장
    output = {
        "user_info": user,
        "summary": {
            "total_stars": 1000,
            "unique_bias": len(unique_bias),
            "unique_tips": len(unique_tips),
            "unique_missions": len(unique_missions),
            "avg_score": sum(scores)/len(scores),
            "max_score": max(scores),
            "min_score": min(scores)
        },
        "samples": results
    }
    
    with open("tests/simulation_results_1000_stars_0301.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 결과가 tests/simulation_results_1000_stars_0301.json 에 저장되었습니다.")

if __name__ == "__main__":
    run_1vs1000_simulation()
