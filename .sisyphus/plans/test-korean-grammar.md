# K-Destiny AI 미션 문장 한국어 문맥 검증 테스트 계획서

## TL;DR

> **Quick Summary**: 가상의 유저 1명과 K-pop 스타 10명을 대상으로 사주 분석 API를 호출하여 생성된 '도전 시너지 레벨업 치트키(미션)' 문장들을 수집하고, 이를 전문 에이전트(Oracle)가 한국어 문법과 문맥적 자연스러움을 정밀 평가하는 테스트 계획입니다.
> 
> **Deliverables**: 
> - 문장 수집용 파이썬 스크립트 작성 (`tests/collect_missions.py`)
> - 수집된 미션 문장 데이터 파일 생성 (`.sisyphus/evidence/mission_sentences.txt`)
> - 국어 전문 에이전트(Oracle)의 문맥 자연스러움 평가 리포트
> 
> **Estimated Effort**: Short
> **Parallel Execution**: NO - sequential
> **Critical Path**: Task 1 → Task 2 → Final Oracle Review

---

## Context

### Original Request
미션 문장(Action + Target + Context 조합) 생성 로직 수정 후, 생성된 문장들이 한국어 문법과 문맥에 맞게 자연스럽게 출력되는지 가상의 유저와 10명의 스타 데이터를 이용해 전문 에이전트가 검증할 수 있는 테스트 계획을 세워달라는 요청입니다.

### Interview Summary
**Key Discussions**:
- 앞서 `{tgt}` 변수가 중복 삽입되어 문맥이 파괴되는 버그를 수정했습니다. (`full_task = f"{act} {ctx}"`로 변경)
- 이제 수정한 로직이 **실제로 모든 조합(E/I 성향, 오행별 Target, Context)에서 매끄러운 한국어 문장을 만들어내는지** 확신이 필요합니다.
- 단순 API 호출 성공 여부(HTTP 200)가 아니라, **"사람이 읽었을 때 말이 되는가"**를 평가해야 하므로 LLM 기반의 AI 전문가(Oracle 에이전트)를 활용한 정성적 평가가 필요합니다.

---

## Work Objectives

### Core Objective
생성형 미션 문구 조합 로직(`GEN_MISSION_COMPONENTS`)이 한국어 조사, 어순, 문맥 호응 측면에서 결함 없이 작동하는지 철저히 검증합니다.

### Concrete Deliverables
- `tests/collect_missions.py` (API를 호출해 문장만 파싱하는 스크립트)
- 10명의 스타와의 궁합 결과에서 추출된 약 30~90개의 미션 문장 데이터셋.
- Oracle 에이전트의 문장 검수 및 교정 제안 리포트.

### Definition of Done
- [ ] 10명의 스타에 대한 미션 문장이 성공적으로 추출되어 파일로 저장됨.
- [ ] Oracle 에이전트가 문장들을 읽고 "어색함", "조사 불일치", "단어 중복" 등의 기준에 따라 합격/불합격 판정을 내림.

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: NO
- **Automated tests**: API Script + LLM Evaluation
- **Framework**: Python requests + Oracle Agent
- **Agent-Executed QA**: ALWAYS

### QA Policy
Every task MUST include agent-executed QA scenarios.
Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately):
├── Task 1: Create mission collection script [quick]
└── Task 2: Execute script and save sentences [quick]

Wave FINAL (After ALL tasks):
└── Task F1: Expert Agent (Oracle) Grammar & Context Review [oracle]

Critical Path: Task 1 → Task 2 → F1
```

### Dependency Matrix
- **1-2**: — — 1, 2

### Agent Dispatch Summary
- **1**: **2** — T1, T2 → `quick`
- **FINAL**: **1** — F1 → `oracle`

---

## TODOs

- [ ] 1. 미션 문장 수집용 파이썬 스크립트 작성 (`tests/collect_missions.py`)

  **What to do**:
  - `tests/collect_missions.py` 파일을 생성합니다.
  - 로컬 API(`http://localhost:8000/api/saju/analyze`)에 가상 유저(1998-07-15, ENFP, 여성)와 10명의 다양한 아이돌 데이터를 전송합니다.
  - 반환된 JSON에서 `analysis -> chemistry_signal -> synergy_missions -> tasks` 배열 안의 문자열들만 순수하게 추출합니다.
  - 콘솔에 출력합니다.

  **Must NOT do**:
  - 서버 코드는 절대 수정하지 않습니다.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 단순 파이썬 API 호출 및 파싱 스크립트 작성입니다.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential

  **References**:
  - API 엔드포인트: `/api/saju/analyze`

  **Acceptance Criteria**:
  - [ ] `tests/collect_missions.py` 파일이 존재하고 실행 가능해야 함.

  **QA Scenarios**:
  ```
  Scenario: Script creation successful
    Tool: Bash
    Preconditions: None
    Steps:
      1. ls tests/collect_missions.py
    Expected Result: File exists.
    Failure Indicators: File not found.
    Evidence: .sisyphus/evidence/task-1-script-check.txt
  ```

- [ ] 2. 스크립트 실행 및 증거 데이터 수집

  **What to do**:
  - 작성된 `tests/collect_missions.py`를 실행합니다.
  - 출력 결과를 `.sisyphus/evidence/mission_sentences.txt` 파일로 저장합니다.

  **Must NOT do**:
  - 수작업으로 텍스트를 복사/붙여넣기 하지 않습니다.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 스크립트 실행 및 파일 리다이렉션.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Blocked By**: Task 1

  **References**:
  - None

  **Acceptance Criteria**:
  - [ ] `.sisyphus/evidence/mission_sentences.txt` 파일에 한글 문장들이 저장되어 있어야 함.

  **QA Scenarios**:
  ```
  Scenario: Sentences collected successfully
    Tool: Bash
    Preconditions: Task 1 completed, Backend is running
    Steps:
      1. python tests/collect_missions.py > .sisyphus/evidence/mission_sentences.txt
      2. cat .sisyphus/evidence/mission_sentences.txt | head -n 5
    Expected Result: File contains generated Korean mission sentences.
    Failure Indicators: File is empty or contains API errors.
    Evidence: .sisyphus/evidence/task-2-sentences.txt
  ```

---

## Final Verification Wave

- [ ] F1. **전문가 에이전트(Oracle) 한국어 문맥 및 문법 검수** — `oracle`
  수집된 `.sisyphus/evidence/mission_sentences.txt` 파일을 정밀하게 읽고 분석합니다.
  
  **[Oracle 평가 기준]**
  1. **조사 호응**: 목적어와 서술어의 조사가 자연스러운가? (예: "아이템을", "장소에서")
  2. **단어 중복**: 한 문장 내에 같은 명사(Target 등)가 불필요하게 두 번 이상 반복되지 않는가?
  3. **어조의 일관성**: MZ 세대 특유의 트렌디한 어투와 행동 지침의 어조가 어색하게 섞이지 않았는가?
  
  모든 문장을 검토한 후, 
  - 어색한 문장이 없다면 **"VERDICT: APPROVE (완벽함)"**을 선언합니다.
  - 어색한 문장이 하나라도 있다면 해당 문장과 이유를 나열하고 **"VERDICT: REJECT (수정 필요)"**를 선언합니다.
  
  Output: `Analyzed [N] sentences | Grammatical Errors [N] | VERDICT: APPROVE/REJECT`

---

## Commit Strategy

- **1**: `test: add script to collect and verify mission sentence grammar` — tests/collect_missions.py

---

## Success Criteria

### Verification Commands
```bash
cat .sisyphus/evidence/mission_sentences.txt
```

### Final Checklist
- [ ] 문장 30개 이상 수집 완료
- [ ] Oracle 에이전트 검수 통과 (APPROVE)
