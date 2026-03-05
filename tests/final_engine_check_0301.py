import sys, os
sys.path.insert(0, 'backend')
from saju_engine import analyze_destiny
import json

# 테스트 데이터
birth = "1995-12-30" # 뷔 생일 예시
mbti = "INFP"
idol_name = "V"
idol_mbti = "ENFP"
lang = "ko"

print("--- [KO 분석 결과 검증] ---")
result = analyze_destiny(birth, "male", mbti, idol_name, idol_mbti, "", lang)

sig = result.get("chemistry_signal", {})
traits = sig.get("idol_detailed_traits", [])
missions = sig.get("synergy_missions", [])
tips = sig.get("tips", [])

print(f"1. 상대방 성향 문장 수: {len(traits)}")
for i, t in enumerate(traits):
    print(f"   [{i+1}] {t[:50]}...")

print(f"\n2. 시너지 미션 개수: {len(missions)}")
for m in missions:
    print(f"   - Label: {m['label']}")
    print(f"   - Tasks (3개): {m['tasks']}")

print(f"\n3. 꿀팁 개수: {len(tips)}")
for t in tips:
    print(f"   - Tip: {t[:50]}...")

print("\n--- [EN 분석 결과 검증] ---")
result_en = analyze_destiny(birth, "male", mbti, idol_name, idol_mbti, "", "en")
sig_en = result_en.get("chemistry_signal", {})
print(f"EN 미션 첫번째 Label: {sig_en.get('synergy_missions', [{}])[0].get('label')}")
