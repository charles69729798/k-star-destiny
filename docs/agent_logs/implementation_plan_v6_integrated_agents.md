# [Goal] 동적 분석 엔진 고도화 및 계층형 에이전트 MCP 통합 (v6)

사용자의 최종 피드백을 반영하여, **데이터와 알고리즘에 100% 기반한 동적 분석 시스템**을 구축하고, 이를 효율적으로 관리하기 위한 **계층형 에이전트(Main-Sub Agent)와 MCP 적용 방안**을 통합합니다.

## User Review Required

> [!IMPORTANT]
> - **100% 데이터 기반 로직**: 텍스트 생성 시 `random.choice`를 배제하고, 사용자와 스타의 오행 관계(상생, 상극, 합 등)와 MBTI 매칭 점수에 근거한 확정적 문장 조합을 수행합니다.
> - **MBTI 부재 시 대응**: 스타의 MBTI가 없을 경우, 사주 오행의 깊은 파동만을 분석하는 '순수 사주(Pure Saju)' 엔진으로 자동 전환되어 전문적인 사주 보충 문구를 동적으로 생성합니다.
> - **지인 이름 입력 제거**: UI 및 API 모든 곳에서 지인 이름 입력 기능을 삭제합니다.

## 1. 계층형 에이전트 및 MCP 적용 방안

### 가. 에이전트 구조 (Hierarchical Structure)
- **Main Agent (Antigravity)**: 전체 워크플로우 제어 및 프론트엔드-백엔드 정합성 관리.
- **Sub-Agent: DB/Engine Expert**: `saju_engine.py`의 알고리즘 계산 로직 및 템플릿 바인딩 전담.
- **Sub-Agent: Linguistic/i18n Expert**: `saju_i18n.py`의 4개 국어 템플릿 품질 및 문화적 맥락(MZ 신조어 등) 관리.

### 나. MCP 스킬 적용 (MCP Integration)
- **Data Resource MCP**: `saju_i18n.py`를 MCP 리소스로 관리하여 에이전트가 실시간으로 번역 키를 조회하고 누락을 자동 감지.
- **Verification MCP**: 특정 사주 조합에 대해 생성된 문장이 논리적(오행의 원리)으로 맞는지 자동 검증하는 스크립트를 MCP 도구로 등록하여 사용.

## 2. 세부 변경 사항

### Frontend: [App.tsx](file:///c:/InsuranceProject/Sajuapp/frontend/src/App.tsx)
- **입력 필드 정비**: 지인 이름 필드 제거.
- **YouTube Social UI**: 댓글 수, 핸들, 좋아요, 답글 기능이 포함된 정교한 레이아웃 구현.

### Backend: [saju_engine.py](file:///c:/InsuranceProject/Sajuapp/backend/saju_engine.py) & [saju_i18n.py](file:///c:/InsuranceProject/Sajuapp/backend/saju_i18n.py)
- **로직 개편**: 
  - `if mbti_exists: combine_saju_mbti()` 
  - `else: deep_dive_pure_saju()`
- **동적 템플릿**: `{element_interaction}`, `{mbti_synergy_point}` 등의 전문 변수를 활용한 4개 국어 출력.

## 3. 검증 계획

### Automated Tests
- MCP 검증 도구를 활용하여 100가지 이상의 사주/MBTI 조합에 대해 텍스트 생성 논리 확인.

### Manual Verification
- MBTI가 있는 스타와 없는 스타를 각각 분석하여 결과의 차별화 여부 확인.
- 유튜브 댓글 UI의 다크모드 및 다국어 렌더링 검수.
