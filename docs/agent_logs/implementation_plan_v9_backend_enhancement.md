# Implementation Plan v9: Backend Engine Enhancement & Individualization

본 계획은 `Backend Engine Audit Report`의 결과를 바탕으로, 사용자의 피드백(데이터 풀 확장 우선, 전문 에이전트 참여, 텍스트 기반 선검증)을 전적으로 반영한 고도화 플랜입니다.

## User Review Required

> [!IMPORTANT]
> **데이터 풀 확장 우선 원칙**: 모든 알고리즘 수정에 앞서 언어별 데이터 풀(미션, 팁, 설명문 등)을 최소 20개 이상으로 확장하는 작업을 최우선으로 진행합니다.

> [!TIP]
> **텍스트 기반 검증**: 프론트엔드 UI 스크린샷 이전에, 수정된 알고리즘이 생성하는 "예상 분석 결과"를 텍스트 로그 형태로 먼저 출력하여 사용자의 정성적 검토를 받습니다.

## Proposed Changes

### 1. Saju Theory-Based Data Expansion (Massive Scaling)
개인별 사주(평생 총운)와 월별 사주 정보의 알고리즘적 다양성을 확보하기 위해 데이터 풀을 대폭 확장합니다.
- **개인별 사주(Lifetime)**: 격국(Gyeokguk) 및 오행 상성에 기반한 심층 분석 텍스트를 최소 100개 이상으로 확장하여 개별화된 '소울 설계도'를 제공합니다.
- **월간 운세(Monthly)**: 신살(Sinsal) 및 십이운성(12 Unseong) 로직이 반영된 월별 키워드와 설명문을 언어별로 100개 이상 대량 확보하여 `saju_i18n.py`에 통합합니다.
- **시너지 분석**: 아이돌과의 궁합(Chemistry) 데이터를 MBTI와 오행 관계를 교차하여 더욱 정교한 100개 단위의 미션 및 팁 풀을 구축합니다.

### 2. Saju Engine Refactoring & Logic Verification
- **ID 기반 고정 추출 및 총체적 로직/데이터 분리 (Deterministic & Decoupled Architecture)**:
    - **결정론적 알고리즘**: 이름, 생년월일, MBTI 등을 조합한 해시값을 `random.seed()`로 사용하여 각 사용자에게 고유하고 일관된 결과를 제공합니다.
    - **엔진 최적화 (Strict Decoupling)**: `saju_engine.py`에 남아있는 모든 하드코드 상수(`ENERGY_TRAITS`, `MONTH_KEYWORDS` 등)를 제거합니다. 
    - **동적 데이터 호출**: 모든 텍스트 데이터는 `saju_i18n.py`를 통해서만 가져오며, 특정 언어 데이터 누락 시 한국어(`ko`)로 자동 Fallback 되는 시스템을 구축합니다.
- **예상 출력 선검증 (Text-based Preview)**: 로직 수정 후, 실제 파일 업데이트 전에 수정된 알고리즘이 생성하는 텍스트 로그를 먼저 검토받습니다.

### 3. Strict Localization (No Korean Policy)
- **한글 노출 원천 차단**: 글로벌(EN, ES, PT) 모드에서는 분석 결과 텍스트 및 이미지 내에서 한글이 단독으로 노출되는 것을 금지합니다.
- **병기 원칙**: 사주 용어 등 불가피하게 한글이 필요한 경우, 반드시 현지어 설명 뒤에 괄호로 병기(`Local Language (한글)`)하여 현지 사용자의 혼란을 방지합니다.

### 4. Frontend Idol UX Optimization (`App.tsx`)
- 인기 아이돌 클릭 시 불필요한 검색 단계를 건너뛰고 내부 DB를 통해 즉시 분석으로 연결하여 속도를 개선합니다.

---
**작업 순서:**
1. `saju_i18n.py`에 100개 데이터 세트 주입 (현재 진행 예정).
2. `saju_engine.py` 알고리즘(ID 기반 시드 및 모듈형 조합) 개편.
3. 텍스트 기반 결과물 보고 및 승인.

## Verification Plan

### Step 1: Data Pool Quality Audit
- 확장된 텍스트 데이터의 언어별 완결성 및 문화적 적합성 검토.

### Step 2: Text-Based Dry Run
- `debug_logic_test.py` 스크립트를 작성하여 다양한 입력값(MBTI, 생년월일 조합)에 대한 출력 텍스트를 생성.
- **출력 결과물의 다양성(Diversity) 지표 확인.**

### Step 3: UI & UX Consistency
- 텍스트 검증 승인 후, 프론트엔드 연동 및 최종 스크린샷 캡처.
- 클릭 로직의 속도 개선 확인.

---
**승인 시 작업을 시작하지 않고, 우선 데이터 확장을 위한 세부 에이전트 가이드부터 마련하겠습니다.**
