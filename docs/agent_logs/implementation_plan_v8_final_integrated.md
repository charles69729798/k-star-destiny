# [Goal] 전면적인 개별화 및 글로벌 번역 버그 수정

사용자께서 지적하신 Portuguese(PT) 환경에서의 한국어 잔존 문제("인생네컷", "중꺾마" 등)를 해결하고, 모든 시너지 미션과 설명이 사용자 데이터에 기반해 동적으로 생성되도록 전면 개편합니다.

## User Review Required

> [!IMPORTANT]
> **현재 상태 확인**: 포르투갈어(PT) 등 일부 언어에서 설명은 번역되나 헤더(Keyword)가 여전히 한국어로 출력되는 버그가 있습니다. 이는 `saju_engine.py`의 기본값 폴백 로직과 `saju_i18n.py`의 데이터 매칭 불일치 때문입니다.

> [!WARNING]
> **알고리즘 개편**: 현재 3개뿐인 시너지 미션을 20개 이상으로 확장하고, 사용자와 아이돌의 MBTI/오행 조합에 따라 '필터링'하여 추출하는 방식으로 변경합니다.

---

## Proposed Changes

### 1. [Component] Localization Data (`saju_i18n.py`)

#### [MODIFY] `saju_i18n.py`
- **전수 조사 및 수정**: EN, ES, PT 섹션에서 누락된 `MONTH_KEYWORDS` 및 `SYNERGY_MISSIONS`를 완전히 수정합니다. 특히 "인생네컷(Photo Moment)", "중꺾마(Never Give Up)" 등 한국식 표현을 각 문화권에 맞는 자연스러운 표현으로 교체합니다.
- **데이터 풀 확장**: 시너지 미션 데이터를 현재 3개에서 **각 언어별 20개 이상**(`missions_pool`)으로 대폭 확장합니다.
- **태그 시스템 도입**: 각 미션에 `tags=["E", "I", "Wood", "Fire", ...]`를 부여하여 알고리즘이 선택할 수 있게 합니다.

---

### 2. [Component] Synergy Algorithm (`saju_engine.py`)

#### [MODIFY] `saju_engine.py`
- **폴백 로직 제거**: `analyze_destiny` 함수 내에서 `lang`이 "ko"가 아닐 경우 한국어 상수를 참조하지 않도록 엄격히 제어합니다.
- **동적 미션 선택 로직 구현**:
  - `missions_pool`에서 사용자의 MBTI(E/I 성향)와 오행 궁합에 적합한 미션 3개를 필터링 후 랜덤 추출합니다.
  - 예: 사용자가 'I' 성향이면 '조용한 카페 데이트' 미션 우선 배정.
- **시너지 텍스트 조합기**:
  - 고정된 문장이 아닌 `[서두] + [성격 궁합] + [조언]` 형태의 템플릿 기반 조합 시스템으로 변경하여 수천 건의 조합이 나오도록 합니다.
- **점수 계산 정밀화**: 단순히 `random.randint`를 쓰지 않고, MBTI와 오행의 점수를 가중치 합산하여 결정론적(Deterministic)이면서도 개별화된 점수를 산출합니다.

---

### 3. [Component] Frontend Verification (`App.tsx`)

#### [MODIFY] `App.tsx` (Verification only)
- 브라우저 테스트를 통해 포르투갈어 및 스페인어에서 한국어 키워드가 더 이상 노출되지 않는지 확인합니다.

---

## Verification Plan

### Automated Tests
- `pytest` 스타일의 스크립트로 100회 이상의 시뮬레이션 분석을 수행하여 결과의 다양성(Diversity)과 번역 완결성을 검증합니다.

### Manual Verification
- 브라우저 설정(lang)을 바꿔가며 "2026 달력" 섹션과 "시너지 퀘스트" 섹션의 텍스트가 모두 현지화되어 있는지 스크린샷으로 확인합니다.
