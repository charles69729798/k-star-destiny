# Implementation Plan: Dynamic Synergy Missions & MZ Quests

Refine the synergy missions in the Saju analysis engine to be dynamic, personalized, and culturally relevant for the MZ generation.

## User Review Required

> [!IMPORTANT]
> 시너지 미션의 동적 포맷팅은 **사주 및 MBTI 분석 결과(궁합 점수 및 속성)**를 바탕으로 선택된 텍스트 템플릿에 `{user}`와 `{idol}` 이름을 주입하는 방식으로 작동합니다.
> - **로직 구성**: `saju_engine.py`에서 계산된 `mbti_synergy`, `element_harmony` 등 세부 항목별로 최적화된 미션 텍스트를 `saju_i18n.py`에서 가져온 후, 실시간으로 이름을 바인딩합니다.

## Proposed Changes

### Backend: Saju Analysis Engine & I18N

#### [MODIFY] [saju_i18n.py](file:///c:/InsuranceProject/Sajuapp/backend/saju_i18n.py)
- Add `SYNERGY_MISSIONS` for `en`, `ko`, `es`, and `pt`.
- Use dynamic placeholders: `{user}` and `{idol}`.
- Include MZ-style quests like "Life-four-cuts", "Aesthetic cafe visit", and "MBTI balance game".

#### [MODIFY] [saju_engine.py](file:///c:/InsuranceProject/Sajuapp/backend/saju_engine.py)
- `analyze_destiny` 함수 내에서 `synergy_missions` 생성 시, `label`, `reason`, `tasks` 필드에 `.format(user=display_user, idol=display_idol)`을 적용합니다.
- 예: `label = loc["SYNERGY_MISSIONS"]["mbti"]["label"].format(user=display_user, idol=display_idol)`

---

## Verification Plan

### Automated Tests
- Run `pytest` if available (though currently we are relying on manual verification via UI).
- Check backend logs for any formatting errors (KeyError/ValueError in `.format()`).

### Manual Verification
1.  Run the application locally.
2.  Perform a Saju analysis for a user and an idol.
3.  Verify that the "Synergy Missions" section correctly displays the user and idol names.
4.  Switch languages and confirm translations are working correctly.
5.  Check that the missions feel like "MZ style" (e.g., using slang and trendy activities).
