# K-Destiny AI 미션 생성 로직 고도화 및 버그 수정 작업 계획서

## TL;DR

> **Quick Summary**: 사주 미션 카드(Analysis 1, 2, 3)에서 동일한 문장이 여러 번 중복 생성되는 문제(랜덤 풀 중복 샘플링 버그)와, 앞서 발견된 한국어 조사 및 어미 호응 오류를 한 번에 해결하는 작업입니다.
> 
> **Deliverables**: 
> - `saju_engine.py`의 미션 생성 로직 수정 (중복 방지 세트 도입)
> - `saju_i18n.py`의 문맥 호응 오류 및 오타 수정
> 
> **Estimated Effort**: Short
> **Parallel Execution**: YES - 2 tasks in parallel
> **Critical Path**: Task 1, 2 (parallel) → F1

---

## Context

### Original Request
유저가 첨부한 스크린샷에서 "Analysis 1, 2, 3" 탭에 "동료 팬들과 함께 수영/명상 챌린지를 진행하며..." 같은 **완전히 똑같은 미션 문장이 중복해서 등장**하는 버그가 발견되었습니다. 

### Interview Summary
**Key Discussions**:
- **문제 1: 중복 생성 버그**: Explore 에이전트 분석 결과, `saju_engine.py`에서 미션을 뽑을 때 `_det_pick` 함수를 사용하는데, 이미 뽑은 문장인지 확인(기억)하는 로직이 없어 **'복원 추출(Sampling with replacement)'**이 일어나고 있었습니다.
- **문제 2: 문맥/오타 버그**: 앞선 테스트에서 파악했듯, "진행하며"가 "제행하며"로 오타가 나 있고, "참여하며... 방법입니다" 처럼 어미 호응이 맞지 않는 문제가 `saju_i18n.py`에 남아있습니다.
- **해결 방향**: 엔진에서 `used_tasks = set()`을 도입해 이미 뽑은 액션/문맥은 건너뛰게 만들고, 번역 파일의 텍스트를 문법에 맞게 일괄 교정합니다.

---

## Work Objectives

### Core Objective
미션 텍스트가 100% 겹치지 않는 유니크한 문장으로 생성되도록 보장하고, 한국어 문법과 문맥을 완벽하게 맞춥니다.

### Concrete Deliverables
- `backend/saju_engine.py` (중복 방지 로직 `used_tasks` 추가)
- `backend/saju_i18n.py` (조사, 어미, 오타 일괄 교정)

### Definition of Done
- [ ] 3개의 Analysis 탭 내에 있는 총 9개의 미션 중 중복되는 문장이 하나도 없음.
- [ ] 문장의 끝맺음이 자연스러움 (예: "~하는 것을 추천합니다.", "~해보세요.")

### Must Have
- 중복 방지를 위한 `used_tasks` Set 기반의 재시도(Re-roll) 로직.

### Must NOT Have (Guardrails)
- 기존의 다국어 지원(EN, ES, PT) 구조를 깨뜨리지 말 것.

---

## Verification Strategy

### Test Decision
- **Agent-Executed QA**: ALWAYS
- **API/Backend**: Use Python script / curl to generate missions and assert len(set(missions)) == 9.

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately):
├── Task 1: Fix Duplication Logic in Engine [quick]
└── Task 2: Fix Grammar & Typos in I18N [quick]

Wave FINAL (After ALL tasks):
└── Task F1: Mission Uniqueness & Grammar QA [unspecified-high]
```

---

## TODOs

- [ ] 1. 엔진의 미션 중복 추출 버그 수정 (`saju_engine.py`)

  **What to do**:
  - `backend/saju_engine.py`를 수정합니다.
  - `guide_map` 루프가 시작되기 전(약 495번 라인)에 `used_combinations = set()` 변수를 선언합니다.
  - `is_gen` 블록 내에서 `act`와 `ctx`를 뽑을 때, `f"{act}_{ctx}"` 조합이 `used_combinations`에 이미 존재한다면 다른 조합을 뽑을 때까지 `t_idx`에 임의의 값을 더해 해시 시드(seed)를 재굴림(re-roll) 하는 `while` 루프를 추가합니다.
  - 유니크한 조합을 찾으면 `used_combinations`에 추가하고 `selected_tasks`에 넣습니다.

  **Recommended Agent Profile**:
  - **Category**: `quick`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1

  **References**:
  - `backend/saju_engine.py`: `def analyze_destiny` 함수 내 미션 조합 부분

  **Acceptance Criteria**:
  - [ ] 한 번의 API 호출에서 반환되는 9개의 미션 문장 내용이 모두 다름.

  **QA Scenarios**:
  ```
  Scenario: Assert all missions are unique
    Tool: Bash
    Preconditions: Backend is running
    Steps:
      1. python tests/collect_missions.py > output.txt
      2. python -c "lines = open('output.txt').readlines(); assert len(set(lines)) == len(lines), 'Duplicates found!'"
    Expected Result: Script passes with no assertion error.
    Failure Indicators: "Duplicates found!" assertion error.
    Evidence: .sisyphus/evidence/task-1-uniqueness.txt
  ```

- [ ] 2. 한국어 문맥 및 오타 일괄 교정 (`saju_i18n.py`)

  **What to do**:
  - `backend/saju_i18n.py` 파일의 한국어(`ko`) 딕셔너리 내 `GEN_MISSION_COMPONENTS` 부분을 수정합니다.
  - `actions` 배열의 모든 `~하며`를 `~하는 것은` 으로 변경합니다. (예: "참여하며" -> "참여하는 것은", "제행하며" -> "진행하는 것은")
  - `contexts` 배열의 문장 중 어색한 부분을 수정합니다. (예: "서로의 다름을 {point} 매력으로 승화시키는 마법입니다.")
  - 오타 수정: `제행` -> `진행`, `{point}한` -> `{point}` (중복 조사 제거)

  **Recommended Agent Profile**:
  - **Category**: `quick`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1

  **References**:
  - `backend/saju_i18n.py`: `GEN_MISSION_COMPONENTS` 딕셔너리 영역

  **Acceptance Criteria**:
  - [ ] 생성된 문장이 "~~하는 것은 ~~하는 방법입니다." 형태의 완벽한 한국어 문법을 갖춤.

  **QA Scenarios**:
  ```
  Scenario: Verify grammar fixes in source
    Tool: Bash
    Preconditions: None
    Steps:
      1. grep "제행" backend/saju_i18n.py
      2. grep "하며" backend/saju_i18n.py | grep "actions"
    Expected Result: No matches found for typos or old verb forms.
    Failure Indicators: Grep finds the old strings.
    Evidence: .sisyphus/evidence/task-2-grammar.txt
  ```

---

## Final Verification Wave

- [ ] F1. **Mission Uniqueness & Grammar QA** — `unspecified-high`
  서버를 재시작하고 앞서 만들었던 `tests/collect_missions.py` 스크립트를 한 번 더 실행합니다. 
  추출된 파일(`.sisyphus/evidence/mission_sentences.txt`)을 읽고, 다음 두 가지를 완벽하게 만족하는지 확인합니다:
  1) 동일한 아이돌에 대해 9개의 미션 중 내용이 똑같은 문장이 하나도 없는가? (완전 무결한 유니크함)
  2) 문맥이 어색하거나(호응 불일치) 오타가 있는가?
  Output: `Uniqueness [PASS/FAIL] | Grammar [PASS/FAIL] | VERDICT`

---

## Commit Strategy

- **1**: `fix(engine): ensure mission uniqueness and correct Korean grammar context` — saju_engine.py, saju_i18n.py
