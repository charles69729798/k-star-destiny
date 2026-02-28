from saju_engine import analyze_destiny
import json

def test_next_gen_output():
    # 테스트 케이스: ENTJ 타입, 1995-05-15 생일 (오행 분포가 뚜렷한 사례)
    result = analyze_destiny(
        birth_date_str="1995-05-15",
        gender="male",
        user_mbti="ENTJ",
        lang="ko"
    )
    
    print("=== [Next-Gen Algorithm Output Prototype] ===")
    print(f"Summary: {result['user_saju']['summary']}")
    print(f"Element: {result['user_saju']['element']}")
    print("-" * 50)
    print(result['user_saju']['content'])
    print("-" * 50)

if __name__ == "__main__":
    test_next_gen_output()
