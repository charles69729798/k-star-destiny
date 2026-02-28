import random
import json
from saju_engine import analyze_destiny

# 1. 가상 데이터 생성
users = [
    {"birth": f"1990-{m:02d}-{m*2:02d}", "gender": "male" if m%2==0 else "female", "mbti": random.choice(["ENTJ", "INFP", "ENFJ", "ISTJ", "ESTP"])}
    for m in range(1, 11)
]

stars = [
    {"name": f"Idol_{i}", "birth": f"1995-{i:02d}-15", "mbti": random.choice(["ENFP", "ISFJ", "ENTP", "INTJ", "ESFJ"]) if i%2==0 else ""}
    for i in range(1, 11)
]

languages = ["ko", "en", "es", "pt"]

def jaccard_similarity(str1, str2):
    s1 = set(str1.split())
    s2 = set(str2.split())
    if not s1 or not s2: return 0
    return len(s1 & s2) / len(s1 | s2)

def run_comprehensive_uat():
    report = []
    print(f"🚀 차세대 알고리즘 대규모 UAT 시작 (4개 국어 x 10유저 x 10스타 = 400개 조합)")
    
    for lang in languages:
        lang_similarities = []
        next_gen_checks = {"weight": 0, "mbti": 0, "rpre": 0}
        
        print(f"--- Language: {lang.upper()} Test ---")
        
        results_pool = []
        for u in users:
            for s in stars:
                # MBTI가 없는 경우 직접 입력 시뮬레이션
                input_mbti = s["mbti"] if s["mbti"] else "ENFP"
                
                res = analyze_destiny(
                    birth_date_str=u["birth"],
                    gender=u["gender"],
                    user_mbti=u["mbti"],
                    idol_name=s["name"],
                    idol_mbti=input_mbti,
                    idol_birth_date=s["birth"],
                    lang=lang
                )
                
                content_data = res.get("user_saju", {})
                if not content_data:
                    print(f"Error in UAT [{lang}]: {res}")
                    continue
                
                content = content_data.get("content", "")
                results_pool.append(content)
                
                # Next-Gen 포맷 체크 (KO 기준 라벨 확인)
                if "가중치" in content or "Weight" in content or "Peso" in content: next_gen_checks["weight"] += 1
                if "역동" in content or "Dynamics" in content or "Dinámica" in content: next_gen_checks["mbti"] += 1
                if "가설" in content or "Hypothesis" in content or "Hipótesis" in content: next_gen_checks["rpre"] += 1

        # 유사성 측정
        if len(results_pool) > 1:
            for i in range(len(results_pool)-1):
                sim = jaccard_similarity(results_pool[i], results_pool[i+1])
                lang_similarities.append(sim)
        
        avg_sim = sum(lang_similarities)/len(lang_similarities) if lang_similarities else 0
        print(f"[{lang.upper()}] 평균 유사도: {avg_sim:.4f}")
        print(f"[{lang.upper()}] Next-Gen 포맷 적용률: Weight({next_gen_checks['weight']/100:.0%}), MBTI({next_gen_checks['mbti']/100:.0%}), RPRE({next_gen_checks['rpre']/100:.0%})")
        
        report.append({
            "lang": lang,
            "avg_sim": avg_sim,
            "checks": next_gen_checks
        })

    return report

if __name__ == "__main__":
    run_comprehensive_uat()
