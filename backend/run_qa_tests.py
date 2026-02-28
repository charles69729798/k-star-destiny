import requests
import json
import time

API_BASE_URL = "http://localhost:8000/api"

LANGUAGES = ["ko", "en", "es"]
# 아이돌 5명 + 배우 5명
TARGET_STARS = [
    # 아이돌
    {"name": "장원영", "birth": "2004-08-31", "mbti": "ISFP"},
    {"name": "카리나", "birth": "2000-04-11", "mbti": "ENFP"},
    {"name": "정국", "birth": "1997-09-01", "mbti": "INTP"},
    {"name": "차은우", "birth": "1997-03-30", "mbti": "INFJ"},
    {"name": "윈터", "birth": "2001-01-01", "mbti": "ISTP"},
    # 배우
    {"name": "이도현", "birth": "1995-04-11", "mbti": "ENFJ"},
    {"name": "한소희", "birth": "1994-11-18", "mbti": "INFP"},
    {"name": "송강", "birth": "1994-04-23", "mbti": "INTP"},
    {"name": "고윤정", "birth": "1996-04-22", "mbti": "ISTP"},
    {"name": "변우석", "birth": "1991-10-31", "mbti": "ESFJ"},
]

USER_PROFILE = {
    "birth_date": "1998-05-15",
    "gender": "female",
    "user_mbti": "ENFP"
}

def run_qa_tests():
    print("🚀 [대규모 다국어 사주 분석 QA 에이전트 가동]")
    print(f"총 예상 테스트 건수: {len(LANGUAGES)}개 국어 x {len(TARGET_STARS)}명 = {len(LANGUAGES) * len(TARGET_STARS)}건\n")
    
    success_count = 0
    fail_count = 0
    report = []

    start_time = time.time()

    for lang in LANGUAGES:
        print(f"\n================ [언어: {lang.upper()}] 테스트 시작 ================")
        for star in TARGET_STARS:
            print(f"➡️ [테스트 진행 중] 타겟: {star['name']} ({lang.upper()}) ... ", end="", flush=True)
            try:
                # 1. 대상 정보 생성 요청 (saju analyze endpoint)
                params = {
                    "birth_date": USER_PROFILE["birth_date"],
                    "gender": USER_PROFILE["gender"],
                    "user_mbti": USER_PROFILE["user_mbti"],
                    "idol_name": star["name"],
                    "idol_mbti": star["mbti"],
                    "idol_birth_date": star["birth"],
                    "lang": lang
                }
                
                resp = requests.get(f"{API_BASE_URL}/saju/analyze", params=params, timeout=10)
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get("status") == "success":
                        result_data = data.get("analysis", {})
                        # 기본 필수 데이터 검증
                        if "user_saju" in result_data and "chemistry_signal" in result_data:
                            print("✅ PASS")
                            success_count += 1
                        else:
                            print("❌ FAIL (Missing Keys)")
                            fail_count += 1
                            report.append(f"{lang} / {star['name']} - Response missing expected keys")
                    else:
                        print("❌ FAIL (Status not success)")
                        fail_count += 1
                        report.append(f"{lang} / {star['name']} - Backend returned Error Status")
                else:
                    print(f"❌ FAIL (HTTP {resp.status_code})")
                    fail_count += 1
                    report.append(f"{lang} / {star['name']} - HTTP {resp.status_code}")
            except Exception as e:
                print(f"❌ ERROR: {e}")
                fail_count += 1
                report.append(f"{lang} / {star['name']} - Exception: {e}")
            
            # rate limit 방지를 위한 짧은 휴식
            time.sleep(0.1)

    elapsed_time = time.time() - start_time
    print(f"\n================ 테스트 종료 ================")
    print(f"총 소요 시간: {elapsed_time:.2f}초")
    print(f"성공: {success_count}건")
    print(f"실패: {fail_count}건")
    
    if fail_count > 0:
        print("\n[실패 상세 내역]")
        for msg in report:
            print(f"- {msg}")
    
    # 결과를 파일로 저장
    with open("c:/InsuranceProject/Sajuapp/backend/qa_report.txt", "w", encoding="utf-8") as f:
        f.write(f"QA 테스트 결과 (소요 시간: {elapsed_time:.2f}초)\n")
        f.write(f"총 시도: {success_count + fail_count}건 | 성공: {success_count}건 | 실패: {fail_count}건\n")
        if fail_count > 0:
            f.write("실패 내역:\n")
            for msg in report:
                f.write(f"- {msg}\n")

if __name__ == "__main__":
    run_qa_tests()
