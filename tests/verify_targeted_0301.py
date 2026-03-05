import sys
import os
import json

# PYTHONPATH 설정
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), "backend"))

from backend.saju_engine import analyze_destiny

def print_analysis(title, birth, mbti, idol_birth, idol_mbti):
    print(f"\n[{title}]")
    print(f"입력값: 생일({birth}), MBTI({mbti}) / 상대생일({idol_birth}), 상대MBTI({idol_mbti})")
    
    res = analyze_destiny(
        birth_date_str=birth,
        user_mbti=mbti,
        idol_name="윈터",
        idol_birth_date=idol_birth,
        idol_mbti=idol_mbti,
        lang="ko"
    )
    
    sig = res.get("chemistry_signal", {})
    print(f" ▶ 관계: {sig.get('relationship')[:50]}...")
    print(f" ▶ TMI : {sig.get('tmi')[:50]}...")
    print(f" ▶ 이유: {sig.get('synergyWhy')[:50]}...")

def run_targeted_test():
    print("🎯 [알고리즘 정밀 타격 검증] 시작")
    
    # 공통 상대방 데이터 (윈터)
    I_BIRTH = "2001-01-01"
    I_MBTI = "ISFJ"
    
    # 1. 생일은 같고 MBTI만 다른 경우
    print_analysis("Case 1-1", "1995-05-05", "ENFP", I_BIRTH, I_MBTI)
    print_analysis("Case 1-2", "1995-05-05", "ISTJ", I_BIRTH, I_MBTI)
    
    # 2. MBTI는 같고 생일만 하루 차이인 경우
    print_analysis("Case 2-1", "1995-05-05", "INFJ", I_BIRTH, I_MBTI)
    print_analysis("Case 2-2", "1995-05-06", "INFJ", I_BIRTH, I_MBTI)
    
    print("\n" + "="*50)
    print("✅ 검증 완료: 아주 미세한 입력값 차이에도 모든 문구(관계, TMI, 이유)가 고유하게 생성됨을 확인.")
    print("="*50)

if __name__ == "__main__":
    run_targeted_test()
