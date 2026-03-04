# K-Destiny AI 복구 및 동기화 작업 계획서

## TL;DR

> **Quick Summary**: 백엔드와 프론트엔드 간의 데이터 변수명 불일치로 인한 UI 출력 오류(Our Fate 빈칸 현상 등)를 수정하고, Docker 환경에서 소스코드 핫 리로드(Hot-Reload)가 정상 작동하도록 설정 및 실행 스크립트를 보강하는 작업입니다.
> 
> **Deliverables**: 
> - 백엔드 `saju_engine.py`의 응답 키(`star_signal`, `action_point`) 동기화
> - `docker-compose.yml` 백엔드 서비스의 `command` 오버라이드 (uvicorn --reload)
> - `start_dev.bat` 스크립트 클린업 절차 강화 (좀비 컨테이너 완전 삭제)
> 
> **Estimated Effort**: Quick
> **Parallel Execution**: NO - sequential
> **Critical Path**: Task 1 → Task 2 → Task 3

---

## Context

### Original Request
최근 알고리즘(saju_engine, saju_i18n)을 대폭 수정하여 상대방 성향, 월별 운세, 공략 꿀팁 등을 고도화했으나, 로컬 서버 실행 시 변경 사항이 전혀 반영되지 않고 옛날 결과만 나옵니다. 특히 "Our Fate(월별 운세)" 탭에서는 데이터를 전혀 불러오지 못하고 빈칸으로 나옵니다. 원인을 진단하고 수정할 작업 계획서를 만들어달라는 요청입니다.

### Interview Summary
**Key Discussions**:
- **반영 안 됨**: Docker 컨테이너가 볼륨 마운트는 되어있으나, uvicorn 실행 시 `--reload` 옵션이 빠져있어 파이썬 파일 변경을 감지하지 못하고 예전 캐시를 돌리고 있었습니다. 또한 `start_dev.bat`가 기존 구형 컨테이너를 제대로 내리지 못한 상태였습니다.
- **Our Fate 빈칸**: 프론트엔드(`App.tsx`)는 `mf.star_signal`, `mf.action_point` 키를 기대하고 있으나, 백엔드(`saju_engine.py`)는 예전 키인 `signal`, `guide`로 데이터를 내보내고 있어 변수명 불일치로 렌더링되지 않았습니다.
- **해결 방향**: 백엔드 키 수정, Docker Compose reload 활성화, Bat 스크립트 강제 클린업 로직 추가.

### Metis Review
**Identified Gaps** (addressed):
- [Gap 1]: `start_dev.bat`에서 `docker-compose down -v` 사용 시 DB 볼륨 등 유실 위험. → **해결**: `-v` 옵션 대신 컨테이너 강제 삭제(`docker rm -f`) 및 `docker-compose down --remove-orphans`로 안전하게 이전 컨테이너만 제거.
- [Gap 2]: 프로덕션 Dockerfile의 `CMD` 자체를 수정할 위험. → **해결**: `Dockerfile`은 건드리지 않고, 로컬 전용인 `docker-compose.yml`의 `command` 필드만 오버라이드하여 `--reload` 적용.

---

## Work Objectives

### Core Objective
로컬 개발 환경의 핫 리로드를 완벽히 복구하고, 프론트/백엔드 데이터 키를 일치시켜 고도화된 운세 정보가 정상 출력되도록 수정합니다.

### Concrete Deliverables
- `backend/saju_engine.py` (키 이름 동기화)
- `docker-compose.yml` (backend 서비스 command 추가)
- `start_dev.bat` (이전 컨테이너 확실한 제거 로직 추가)

### Definition of Done
- [ ] 브라우저 접속 시 "Our Fate" 탭에 스타 시그널과 액션 포인트 데이터가 정상 출력됨.
- [ ] 코드 저장 시 Docker 컨테이너 재시작 없이 즉시 로직이 변경됨.

### Must Have
- 백엔드와 프론트엔드의 데이터 키 이름 완전 일치.

### Must NOT Have (Guardrails)
- `backend/Dockerfile` 원본 파일을 수정하지 말 것 (배포 환경 보호).
- 프론트엔드 파일(`App.tsx`)의 구조를 대규모로 변경하지 말 것 (문제의 원인은 백엔드 출력에 있음).

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: NO
- **Automated tests**: None
- **Framework**: none
- **Agent-Executed QA**: ALWAYS

### QA Policy
Every task MUST include agent-executed QA scenarios.
Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

- **API/Backend**: Use Bash (curl) — Send requests, assert response fields (`star_signal`, `action_point`).
- **CLI**: Use Bash — Check `docker ps` to verify container status and command.

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately):
├── Task 1: Update API keys in saju_engine.py [quick]
├── Task 2: Override Docker command in docker-compose.yml [quick]
└── Task 3: Strengthen cleanup in start_dev.bat [quick]

Wave FINAL (After ALL tasks):
├── Task F1: Plan compliance audit
├── Task F2: Code quality review
├── Task F3: Real manual QA
└── Task F4: Scope fidelity check

Critical Path: Task 1 → Task 2 → Task 3 → F1-F4
```

### Dependency Matrix
- **1-3**: — — 1, 2, 3

### Agent Dispatch Summary
- **1**: **3** — T1-T3 → `quick`
- **FINAL**: **4** — F1 → `oracle`, F2-F3 → `unspecified-high`, F4 → `deep`

---

## TODOs

- [ ] 1. 백엔드 데이터 출력 키 동기화 (`saju_engine.py`)

  **What to do**:
  - `backend/saju_engine.py`의 `analyze_destiny` 함수 내 `monthly_fortune.append(...)` 부분 수정.
  - `signal` 키를 `star_signal`로 변경.
  - `guide` 키를 `action_point`로 변경.
  - 하위 호환성을 위해 `signal`, `guide` 키도 일단 남겨두고, `star_signal`, `action_point` 키를 추가로 할당.

  **Must NOT do**:
  - 프론트엔드 코드 수정 금지.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 단순 변수명 할당 추가 작업.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1

  **References**:
  - `backend/saju_engine.py`: `monthly_fortune.append` 로직 부분

  **Acceptance Criteria**:
  - [ ] `curl "http://localhost:8000/api/saju/analyze?birth_date=1998-07-15&gender=female&user_mbti=ENFP&idol_name=%EC%9C%88%ED%84%B0&idol_mbti=ISFJ&idol_birth_date=2001-01-01&lang=ko"` 결과에 `star_signal`과 `action_point`가 포함되어야 함.

  **QA Scenarios**:
  ```
  Scenario: Verify API outputs correct keys
    Tool: Bash
    Preconditions: Backend is running
    Steps:
      1. curl "http://localhost:8000/api/saju/analyze?birth_date=1998-07-15&gender=female&user_mbti=ENFP&idol_name=Winter&idol_mbti=ISFJ&idol_birth_date=2001-01-01&lang=ko" > output.json
      2. grep "star_signal" output.json
      3. grep "action_point" output.json
    Expected Result: Output contains both keys.
    Failure Indicators: Grep returns nothing.
    Evidence: .sisyphus/evidence/task-1-api-keys.txt
  ```

- [ ] 2. Docker Hot-Reload 옵션 추가 (`docker-compose.yml`)

  **What to do**:
  - `docker-compose.yml` 파일 열기.
  - `backend` 서비스 설정에 `command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload` 줄을 추가하여 기본 Dockerfile의 CMD를 오버라이드.

  **Must NOT do**:
  - `backend/Dockerfile` 수정 금지.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 파일 1줄 추가.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1

  **References**:
  - `docker-compose.yml`: backend 서비스 섹션

  **Acceptance Criteria**:
  - [ ] `docker-compose config` 명령어 출력에 `backend`의 `command`가 명시되어야 함.

  **QA Scenarios**:
  ```
  Scenario: Check compose config for command override
    Tool: Bash
    Preconditions: None
    Steps:
      1. docker-compose config | grep "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
    Expected Result: Grep finds the command.
    Failure Indicators: Grep fails.
    Evidence: .sisyphus/evidence/task-2-compose-check.txt
  ```

- [ ] 3. 클린업 로직 강화 (`start_dev.bat`)

  **What to do**:
  - `start_dev.bat` 파일 수정.
  - `docker-compose down` 명령어를 `docker-compose down --remove-orphans`로 강화.
  - 기존 구형 컨테이너가 확실히 지워지도록 `docker rm -f sajuapp-backend sajuapp-frontend sajuapp-gateway 2>nul` 명령어 추가 (down 전에 실행).

  **Must NOT do**:
  - `-v` (볼륨 삭제) 옵션 사용 금지.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 단순 텍스트 2~3줄 치환/추가.
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1

  **References**:
  - `start_dev.bat`

  **Acceptance Criteria**:
  - [ ] `start_dev.bat`에 강제 삭제 명령어가 존재해야 함.

  **QA Scenarios**:
  ```
  Scenario: Verify batch script contents
    Tool: Bash
    Preconditions: None
    Steps:
      1. cat start_dev.bat | grep "remove-orphans"
    Expected Result: Grep finds the string.
    Failure Indicators: Grep fails.
    Evidence: .sisyphus/evidence/task-3-bat-check.txt
  ```

---

## Final Verification Wave

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. Verify `saju_engine.py` has `star_signal` and `action_point`. Verify `docker-compose.yml` has `--reload`.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [ ] F2. **Code Quality Review** — `unspecified-high`
  Review changed python files for syntax errors. 
  Output: `Build [PASS/FAIL] | Lint [PASS/FAIL] | Tests [N pass/N fail] | Files [N clean/N issues] | VERDICT`

- [ ] F3. **Real Manual QA** — `unspecified-high`
  Start the system using `cmd /c start_dev.bat`. Make a curl request to ensure it responds and `star_signal` is present.
  Output: `Scenarios [N/N pass] | Integration [N/N] | Edge Cases [N tested] | VERDICT`

- [ ] F4. **Scope Fidelity Check** — `deep`
  Verify nothing outside the planned scope was changed (e.g., Dockerfile was not touched).
  Output: `Tasks [N/N compliant] | Contamination [CLEAN/N issues] | Unaccounted [CLEAN/N files] | VERDICT`

---

## Commit Strategy

- **1**: `fix(backend): sync API response keys with frontend expectations and enable hot reload` — saju_engine.py, docker-compose.yml, start_dev.bat

---

## Success Criteria

### Verification Commands
```bash
curl "http://localhost:8000/api/saju/analyze?birth_date=1998-07-15&gender=female&user_mbti=ENFP&idol_name=Winter&idol_mbti=ISFJ&idol_birth_date=2001-01-01&lang=ko" | grep "star_signal"
```

### Final Checklist
- [ ] All "Must Have" present
- [ ] All "Must NOT Have" absent
