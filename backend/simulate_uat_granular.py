import random
import json
from saju_engine import analyze_destiny

# 1. 가상 데이터 생성 (고정된 시드로 재현 가능성 확보)
random.seed(42)
users = [
    {"birth": f"{random.randint(1980, 2010)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}", 
     "gender": random.choice(["male", "female"]), "mbti": random.choice(["ENTJ", "INFP", "ENFJ", "ISTJ", "ESTP"])}
    for _ in range(20)
]

stars = [
    {"name": f"Idol_{i}", "birth": f"1995-{random.randint(1,12):02d}-{random.randint(1,28):02d}", 
     "mbti": random.choice(["ENFP", "ISFJ", "ENTP", "INTJ", "ESFJ"]) if i%2==0 else ""}
    for i in range(1, 11)
]

# 친구 매칭 테스트 데이터
friends = [
    {"name": f"Friend_{i}", "birth": f"1992-{i:02d}-20", "mbti": random.choice(["INFJ", "ESTJ", "ISFP", "INTP", "ENFP"])}
    for i in range(1, 6)
]

languages = ["ko", "en", "es", "pt"]

def jaccard_similarity(str1, str2):
    if not str1 or not str2: return 0
    s1 = set(str1.split())
    s2 = set(str2.split())
    if not s1 or not s2: return 0
    return len(s1 & s2) / len(s1 | s2)

def run_granular_uat():
    master_report = {}
    print(f"🚀 [Next-Gen Granular UAT] 시작")

    for lang in languages:
        print(f"\n--- Testing Language: {lang.upper()} ---")
        lang_data = {
            "saju_weights": [], "mbti_dynamics": [], "rpre_hypothesis": [],
            "calendar": [], "signal": []
        }
        
        # 10x10 시뮬레이션
        for u in users:
            for s in stars:
                input_mbti = s["mbti"] if s["mbti"] else "ENFP" # 직접 입력 시뮬레이션
                
                res = analyze_destiny(
                    birth_date_str=u["birth"], gender=u["gender"], user_mbti=u["mbti"],
                    idol_name=s["name"], idol_mbti=input_mbti, idol_birth_date=s["birth"],
                    lang=lang
                )
                
                content = res["user_saju"]["content"]
                
                # 영역별 파싱 (줄바꿈 및 라벨 기준)
                parts = content.split("\\n\\n")
                # 📊 영역 (0: 과학적 분석-가중치/MBTI)
                # 🔬 영역 (1: RPRE 가설)
                if len(parts) >= 2:
                    lang_data["saju_weights"].append(parts[0])
                    lang_data["rpre_hypothesis"].append(parts[1])
                
                # 캘린더 (12개월 합본)
                cal_str = " ".join([m["desc"] for m in res["monthly_fortune"]])
                lang_data["calendar"].append(cal_str)
                
                # 운명 시그널 (개별 필드 조립)
                sig = res["chemistry_signal"]
                sig_str = f"{sig.get('relationship', '')} {sig.get('bias', '')} {sig.get('tmi', '')} {sig.get('recentFortune', '')} {sig.get('synergyWhy', '')} {sig.get('synergy', '')}"
                lang_data["signal"].append(sig_str)

        # 유사도 분석
        stats = {}
        for key, pool in lang_data.items():
            sims = []
            if len(pool) > 1:
                # 랜덤하게 20쌍 비교하여 평균 산출
                for _ in range(50):
                    a, b = random.sample(pool, 2)
                    sims.append(jaccard_similarity(a, b))
            stats[key] = sum(sims)/len(sims) if sims else 0

        print(f"[{lang.upper()}] 평균 유사도 결과:")
        for k, v in stats.items():
            print(f"  - {k:15}: {v:.4f} ({'PASS' if v < 0.3 else 'CHECK NEEDED'})")
        
        master_report[lang] = stats

    # 친구 매칭 검증 (KO 기준 샘플)
    print("\n--- Testing Friend Matching (KO) ---")
    f_res = analyze_destiny(
        birth_date_str=users[0]["birth"], gender=users[0]["gender"], user_mbti=users[0]["mbti"],
        idol_name=friends[0]["name"], idol_mbti=friends[0]["mbti"], idol_birth_date=friends[0]["birth"],
        lang="ko"
    )
    if f_res["chemistry_signal"]["idol_name"] == friends[0]["name"]:
        print("  - Idol Name Match Check: PASS")
    else:
        print("  - Idol Name Match Check: FAIL")

    return master_report

if __name__ == "__main__":
    run_granular_uat()
