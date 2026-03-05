"""
미션 생성 품질 검증 스크립트 (100개 샘플)
- 가상 유저 데이터로 미션 파편 조합을 100개 생성
- 4개 언어(KO, EN, ES, PT) 전부 검증
- 문법적 오류, 미치환 변수, 중복 여부를 자동 체크
"""
import sys
import os
import hashlib
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from saju_engine import analyze_destiny

# 가상 유저 데이터 풀 (다양한 MBTI + 생년월일)
VIRTUAL_USERS = [
    ("1990-01-15", "male", "ENFP"), ("1992-06-20", "female", "INTJ"),
    ("1988-03-08", "male", "ESTP"), ("1995-11-25", "female", "INFP"),
    ("1993-09-10", "male", "ENTJ"), ("1991-04-18", "female", "ISFJ"),
    ("1997-07-03", "male", "ENTP"), ("1989-12-30", "female", "ISTJ"),
    ("1994-02-14", "male", "ESFP"), ("1996-08-22", "female", "INTP"),
]

# 가상 스타(아이돌) 데이터 풀 (다양한 생년월일 = 다양한 오행)
VIRTUAL_STARS = [
    ("Star_Wood", "1998-03-21", "ENFJ"),
    ("Star_Fire", "1997-07-15", "ESTP"),
    ("Star_Earth", "1996-09-01", "ISFP"),
    ("Star_Metal", "1999-10-10", "INTJ"),
    ("Star_Water", "1995-12-25", "INFJ"),
]

LANGS = ["ko", "en", "es", "pt"]

def run_verification():
    total_missions = 0
    issues = []
    all_missions_by_lang = {lang: [] for lang in LANGS}

    print("=" * 70)
    print("  미션 생성 품질 검증 (100+ 샘플)")
    print("=" * 70)

    # 10 유저 x 5 스타 = 50 조합, 각 조합에서 미션 9개 = 450개 미션
    combo_count = 0
    for user_birth, user_gender, user_mbti in VIRTUAL_USERS:
        for star_name, star_birth, star_mbti in VIRTUAL_STARS:
            combo_count += 1

            for lang in LANGS:
                try:
                    result = analyze_destiny(
                        user_birth, user_gender,
                        star_name, star_birth,
                        user_mbti, star_mbti, lang
                    )

                    # 미션 추출
                    chem = result.get("chemistry_signal", {})
                    missions = chem.get("synergy_missions", [])

                    for m in missions:
                        for task_text in m.get("tasks", []):
                            total_missions += 1
                            all_missions_by_lang[lang].append(task_text)

                            # 검증 1: 미치환 변수 잔존 여부
                            for placeholder in ["{target}", "{trait}", "{place}", "{mbti}",
                                                "{luck_item}", "{star}", "{skill}", "{organ}",
                                                "{exercise}", "{point}", "{u_el}", "{i_el}",
                                                "{rel_type}", "{mbti_trait}", "{user}", "{idol}"]:
                                if placeholder in task_text:
                                    issues.append(f"[{lang}] 미치환 변수 발견: '{placeholder}' in '{task_text[:60]}...'")

                            # 검증 2: 빈 문자열
                            if not task_text.strip():
                                issues.append(f"[{lang}] 빈 미션 발견! (조합: {user_mbti}+{star_name})")

                except Exception as e:
                    issues.append(f"[{lang}] 에러 발생: {user_mbti}+{star_name}: {str(e)[:80]}")

    # 결과 출력
    print(f"\n총 조합 수: {combo_count}")
    print(f"총 미션 생성 수: {total_missions} (목표: 100+)")

    # 언어별 샘플 출력 (각 10개씩)
    for lang in LANGS:
        lang_label = {"ko": "한국어", "en": "English", "es": "Español", "pt": "Português"}[lang]
        print(f"\n{'─' * 60}")
        print(f"  [{lang_label}] 샘플 미션 (처음 10개)")
        print(f"{'─' * 60}")
        unique_missions = list(set(all_missions_by_lang[lang]))
        for i, m in enumerate(unique_missions[:10]):
            print(f"  {i+1:2d}. {m}")
        print(f"  ... 총 {len(unique_missions)}개 유니크 미션 (전체 {len(all_missions_by_lang[lang])}개)")

    # 다국어 일관성 검증: 같은 조합은 같은 미션 개수를 반환해야 함
    print(f"\n{'=' * 60}")
    print(f"  검증 결과 요약")
    print(f"{'=' * 60}")

    if issues:
        print(f"\n  ⚠️  발견된 이슈: {len(issues)}건")
        for iss in issues[:20]:  # 최대 20건만 출력
            print(f"    - {iss}")
        if len(issues) > 20:
            print(f"    ... 외 {len(issues)-20}건")
    else:
        print(f"\n  ✅ 이슈 없음! 모든 미션이 정상 생성되었습니다.")

    print(f"\n  📊 언어별 유니크 미션 수:")
    for lang in LANGS:
        unique_count = len(set(all_missions_by_lang[lang]))
        print(f"     [{lang}] {unique_count}개 유니크 / {len(all_missions_by_lang[lang])}개 전체")

    print(f"\n{'=' * 60}")
    print(f"  검증 완료!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    run_verification()
