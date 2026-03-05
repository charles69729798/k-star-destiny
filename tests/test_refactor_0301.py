import requests
import json
import time

API_URL = "http://localhost:8000/api/saju/analyze"

# 가상 유저 1명
USER = {
    "birth_date": "1998-07-15",
    "gender": "female",
    "user_mbti": "ENFP",
    "lang": "ko"
}

# 테스트용 스타 10명 (다양한 생일과 MBTI 조합)
STARS = [
    {"idol_name": "카리나", "idol_birth_date": "2000-04-11", "idol_mbti": "ENFP"},
    {"idol_name": "차은우", "idol_birth_date": "1997-03-30", "idol_mbti": "ENTJ"},
    {"idol_name": "장원영", "idol_birth_date": "2004-08-31", "idol_mbti": "ISFP"},
    {"idol_name": "정국", "idol_birth_date": "1997-09-01", "idol_mbti": "INTP"},
    {"idol_name": "아이유", "idol_birth_date": "1993-05-16", "idol_mbti": "INFJ"},
    {"idol_name": "뷔", "idol_birth_date": "1995-12-30", "idol_mbti": "INFP"},
    {"idol_name": "제니", "idol_birth_date": "1996-01-16", "idol_mbti": "INFP"},
    {"idol_name": "지수", "idol_birth_date": "1995-01-03", "idol_mbti": "ESTP"},
    {"idol_name": "윈터", "idol_birth_date": "2001-01-01", "idol_mbti": "ISFJ"},
    {"idol_name": "해찬", "idol_birth_date": "2000-06-06", "idol_mbti": "ENFP"}
]

def run_test():
    print(f"🧪 [Test Start] User: {USER['birth_date']} ({USER['user_mbti']}) vs 10 Stars\n")
    
    success_count = 0
    fail_count = 0
    
    for i, star in enumerate(STARS, 1):
        params = {**USER, **star}
        try:
            start_time = time.time()
            response = requests.get(API_URL, params=params)
            elapsed = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    analysis = data.get("analysis", {})
                    chem = analysis.get("chemistry_signal", {})
                    score = chem.get("base_synergy_score", "N/A")
                    u_el = analysis.get("dominant_element", "N/A")
                    
                    print(f"✅ [{i}/10] {star['idol_name']} ({star['idol_mbti']})")
                    print(f"   - 시너지 점수: {score}점")
                    print(f"   - 유저 오행: {u_el}")
                    print(f"   - 응답 시간: {elapsed:.2f}초")
                    success_count += 1
                else:
                    print(f"❌ [{i}/10] {star['idol_name']} - API Error: {data.get('message')}")
                    fail_count += 1
            else:
                print(f"❌ [{i}/10] {star['idol_name']} - HTTP {response.status_code}")
                fail_count += 1
                
        except Exception as e:
            print(f"❌ [{i}/10] {star['idol_name']} - Request Failed: {e}")
            fail_count += 1
            
    print("\n📊 [Test Summary]")
    print(f"Total: 10 | Success: {success_count} | Fail: {fail_count}")
    
    if fail_count == 0:
        print("🎉 리팩토링(Phase 3) 후에도 모든 로직이 완벽하게 작동합니다!")
    else:
        print("⚠️ 일부 에러가 발생했습니다. 로그를 확인해주세요.")

if __name__ == "__main__":
    run_test()
