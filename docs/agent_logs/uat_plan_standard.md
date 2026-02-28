# UAT Plan: K-Destiny System Verification

> **Summary**: Comprehensive UAT plan for K-Destiny AI application using Multi-Agent workflow.
> **Project**: K-Destiny-MZ-Saju
> **Version**: 1.0.0
> **Author**: Antigravity (as @cto-lead)
> **Date**: 2026-02-25
> **Status**: Approved (Auto-Approval Mode)

---

## 1. Overview
### 1.1 Purpose
본 계획서는 K-Destiny 앱의 전체 기능을 트리 구조로 분석하고, 다국어 환경(KO, EN, ES, PT)에서의 이벤트 발생 및 정합성을 가상의 사용자 10명과 스타 30명을 대상으로 전수 검증하기 위함입니다. 특히 최근 보고된 "장윤정" 데이터 중복 및 수정 전 서버 의심 문제를 해결하는 데 중점을 둡니다.

---

## 2. Functional Tree (시스템 기능 구조)

- **[F0] Home / Landing**
  - [E0.1] 언어 선택 (KO, EN, ES, PT)
  - [E0.2] 글로벌 통계 노출 (전체 방문자, 오늘의 도전자)
- **[F1] User Information Input**
  - [E1.1] 생년월일 입력 (DatePicker)
  - [E1.2] 성별 선택 (Male/Female)
  - [E1.3] MBTI 선택 (Quick Select / Skip)
- **[F2] Star Selection & AI Search**
  - [E2.1] 아이돌 이름 검색 (Perplexity AI 연동)
  - [E2.2] 검색 후보군 선택 (Candidate Selection Modal)
  - [E2.3] 인기 아이돌 빠른 선택 (Personalized Recommendation)
- **[F3] Analysis Engine (Saju + MBTI)**
  - [E3.1] 사주 팔자(8자) 계산 및 오행 분석
  - [E3.2] MBTI 시너지 점수 산출
  - [E3.3] "스타 페르소나" 상세 성향 생성 (3문단)
- **[F4] Interaction Features**
  - [E4.1] 2026 갓생 캘린더 (월간 운세)
  - [E4.2] Destiny Signal (궁합 분석)
  - [E4.3] 시너지 미션 (게이지 업데이트)
  - [E4.4] 소셜 댓글 (YouTube Style)

---

## 3. UAT Scenario (가상 사용자 10명 x 스타 30명)

### 3.1 Test Matrix
- **언어**: KO(4), EN(2), ES(2), PT(2)
- **사용자**: MZ세대 가상 페르소나 10인 (다양한 MBTI 및 생일 조합)
- **스타**: K-Pop 아이돌, 배우 등 30인 (IDOL_POOL + AI 검색 대상)

### 3.2 Key Verification Points
1. **장윤정 중복 데이터 확인**: 결과 화면에서 "장윤정" 데이터가 중복 발생하거나 구형 UI가 노출되는지 확인.
2. **다국어 무결성**: PT(포르투갈어) 등 신규 확장된 데이터에서 한국어 잔여 텍스트 노출 여부.
3. **캘린더 기능**: 한국어 모드에서 `MONTH_KEYWORDS` 정상 노출 및 분석 결과 출력 여부.
4. **리얼타임 동기화**: 미션 달성 시 게이지가 즉각적으로 반응하는지 확인.

---

## 4. Execution Pipeline (@pdca-iterator)
1. 기능 트리별 이벤트 전수 테스트 수행.
2. 발견된 문제점(Bug/UI Gap) 발생 시 `.claudecode/commands`를 통해 즉시 수정.
3. 무결점 상태 도달 시까지 반복 루프 수행.
