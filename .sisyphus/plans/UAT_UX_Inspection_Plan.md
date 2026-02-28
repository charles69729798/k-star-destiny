# K-Destiny AI UX 상태 점검 UAT 계획

**버전:** 1.0  
**생성일:** 2026-02-23  
**플랫폼:** React 19 + FastAPI + Tailwind CSS  
**목표:** 10인 전문 에이전트팀을 통한 UX 상태 종합 점검

---

## 1. Executive Summary

### 1.1 목적
K-Destiny AI 웹앱의 사용자 경험(UX) 품질을 종합적으로 점검하고, 발견된 문제점을 체계적으로 분석하여 개선 방안을 도출합니다.

### 1.2 배경
이전 UAT 테스트에서 발견된 **다국어 모달 버그** 및 **아이돌 MBTI 미검색** 문제를 해결하기 위해, 10명의 전문 에이전트팀을 구성하여 심층 UX 점정을 수행합니다.

### 1.3 범위
- **테스트 환경:** http://localhost:5173 (로컬), http://k-destiny.com (배포 서버)
- **대상 언어:** 영어(EN), 한국어(KO), 스페인어(ES)
- **대상 기기:** Desktop (1920px), Tablet (768px), Mobile (375px)

---

## 2. UAT 에이전트 팀 구성

### 2.1 팀 조직도

```
📋 UAT Orchestrator (총괄)
│
├── 🎨 Visual QA Agent (비주얼 품질)
├── 🔤 Localization Agent (다국어)
├── 📱 Mobile UX Agent (모바일 최적화)
├── ⚡ Performance Agent (성능)
├── ♿ Accessibility Agent (접근성)
├── 🔍 Search UX Agent (검색 기능)
├── 🎯 Form UX Agent (입력 양식)
├── 🧪 Edge Case Agent (경계 조건)
├── 📊 Analytics Agent (데이터 분석)
└── 🔒 Security Agent (보안)
```

### 2.2 각 에이전트 역할 상세

| # | 에이전트 | 역할 | 핵심 점검 항목 |
|---|---------|------|---------------|
| 1 | **Visual QA Agent** | UI/비주얼 일관성 검사 | 색상, 폰트, 아이콘, 글래스모피즘, 애니메이션 |
| 2 | **Localization Agent** | 다국어 번역 및 표시 | 모달, 알림, 에러 메시지 언어 일관성 |
| 3 | **Mobile UX Agent** | 모바일 반응형 검증 | 375px/768px 레이아웃, 터치 타겟, 스크롤 |
| 4 | **Performance Agent** | 로딩 속도 및 응답성 | TTFB, FCP, LCP, 인터랙션 딜레이 |
| 5 | **Accessibility Agent** | 접근성 기준 준수 | 키보드 네비게이션, 스크린 리더 호환, 대비비 |
| 6 | **Search UX Agent** | 검색 기능 심층 검증 | 아이돌 검색, 자동완성,候选자 선택 UI |
| 7 | **Form UX Agent** | 입력 양식 사용자 경험 | 유효성 검사, 에러 메시지, 피드백 |
| 8 | **Edge Case Agent** | 예외 상황 처리 | 네트워크 오류, 빈 결과,超时, 동명이인 |
| 9 | **Analytics Agent** | 사용자 행동 추적 | 클릭률, 이탈률, 클릭 热区 분석 |
| 10 | **Security Agent** | 보안 취약점 검토 | XSS, 입력 검증, 세션 관리 |

---

## 3. 상세 테스트 시나리오

### 3.1 Visual QA Agent 체크리스트

| # | 테스트 항목 | 예상 결과 | 스크린샷 |
|---|-----------|----------|---------|
| V1 | 메인 화면 레이아웃 | 모든 요소가 중앙 정렬, 글래스모피즘 효과 적용 | main_layout.png |
| V2 | 다크 모드 지원 | Dark/Light 모드 토글 시 색상 정상 전환 | theme_toggle.png |
| V3 | 아이콘 일관성 | Lucide React 아이콘이 일관된 스타일 | icons_check.png |
| V4 | 애니메이션 부드러움 | Framer Motion 전환이 60fps로 부드러움 | animation_check.png |
| V5 | 폰트 렌더링 | 한국어, 영어, 스페인어 폰트가 선명하게 표시 | font_rendering.png |

### 3.2 Localization Agent 체크리스트

| # | 테스트 항목 | 예상 결과 | 스크린샷 |
|---|-----------|----------|---------|
| L1 | 언어 스위처 | ES/EN/KO 버튼 클릭 시 UI 전체가 해당 언어로 전환 | lang_switch.png |
| L2 | 모달 번역 | 스페인어 모드에서 MBTI 미입력 모달이 스페인어로 표시 | modal_es.png |
| L3 | 에러 메시지 | 각 언어에 맞는 에러 메시지 표시 | error_messages.png |
| L4 | 날짜 형식 | 한국=YYYY-MM-DD, 미국=MM/DD/YYYY, 유럽=DD/MM/YYYY | date_formats.png |
| L5 | MBTI 텍스트 | 16가지 MBTI가 해당 언어로 표시 | mbti_locale.png |

### 3.3 Mobile UX Agent 체크리스트

| # | 테스트 항목 | 예상 결과 | 스크린샷 |
|---|-----------|----------|---------|
| M1 | 375px 레이아웃 | 콘텐츠가 세로로 정상 배치 | mobile_375.png |
| M2 | 768px 레이아웃 | 태블릿에 최적화된 2열 또는 1열 배치 | tablet_768.png |
| M3 | 터치 타겟 크기 | 모든 버튼/링크가 최소 44x44px | touch_targets.png |
| M4 | 세로 모드 강제 | 横방향 회전 시 레이아웃 유지 | portrait_mode.png |
| M5 | 스와이프 동작 | 분석 결과 탭 스와이프가 자연스러움 | swipe_test.png |

### 3.4 Performance Agent 체크리스트

| # | 테스트 항목 | 목표값 | 스크린샷 |
|---|-----------|-------|---------|
| P1 | First Contentful Paint | < 1.5s | performance_01.png |
| P2 | Largest Contentful Paint | < 2.5s | performance_02.png |
| P3 | Time to Interactive | < 3.0s | performance_03.png |
| P4 | 검색 응답 시간 | < 2.0s | search_timing.png |
| P5 | 애니메이션 프레임 | 60fps 유지 | fps_check.png |

### 3.5 Accessibility Agent 체크리스트

| # | 테스트 항목 | 예상 결과 | 스크린샷 |
|---|-----------|----------|---------|
| A1 | 키보드 네비게이션 | Tab 키로 모든 입력 필드 접근 가능 | keyboard_nav.png |
| A2 | 포커스 표시 | 활성 요소에明显的 포커스 스타일 | focus_indicator.png |
| A3 | 스크린 리더 | ARIA 레이블이 정상 동작 | aria_labels.png |
| A4 | 색상 대비 | 텍스트/배경 대비가 4.5:1 이상 | contrast_check.png |
| A5 | 폰트 크기 | 최소 16px 이상 유지 | font_size.png |

### 3.6 Search UX Agent 체크리스트

| # | 테스트 항목 | 예상 결과 | 스크린샷 |
|---|-----------|----------|---------|
| S1 | 아이돌 검색 (IU) | 아이유 정보 (이름, 사진, MBTI) 정상 표시 | search_iu.png |
| S2 | 아이돌 검색 (정국) | 방탄소년단 정국 정보 정상 표시 | search_jungkook.png |
| S3 | 자동완성 | 입력 시 관련 아이돌 목록 표시 | autocomplete.png |
| S4 | 동명이인 처리 | "민지" 검색 시 5명候选자 표시 | ambiguous_name.png |
| S5 | 검색 결과 없음 | 존재하지 않는 이름 시 적절한 메시지 | no_results.png |
| S6 | 인기 아이돌 목록 | 메인 화면에 추천 아이돌 표시 | popular_idols.png |

### 3.7 Form UX Agent 체크리스트

| # | 테스트 항목 | 예상 결과 | 스크린샷 |
|---|-----------|----------|---------|
| F1 | 생년월일 유효성 | 올바른 날짜만 입력 가능, 잘못 입력 시 에러 표시 | date_validation.png |
| F2 | MBTI 선택 | MBTI Picker에서 16가지 유형 선택 가능 | mbti_picker.png |
| F3 | 필수字段 표시 | 필수 입력 항목을 visual하게 구분 | required_fields.png |
| F4 | 에러 피드백 | 입력 오류 시 즉시 명확한 메시지 표시 | error_feedback.png |
| F5 | 성공 확인 | 분석 완료 후 결과 화면으로 자연스러운 전환 | success_flow.png |

### 3.8 Edge Case Agent 체크리스트

| # | 테스트 항목 | 예상 결과 | 스크린샷 |
|---|-----------|----------|---------|
| E1 | 네트워크 오류 | 검색 실패 시 재시도 옵션과 함께 에러 표시 | network_error.png |
| E2 | 빈 검색 결과 | 검색 결과 없을 때 대안 제안 | empty_results.png |
| E3 |超时 처리 | 검색시간 초과 시 적절한 메시지 | timeout.png |
| E4 | 특수문자 입력 | 이름에 특수문자 입력 시 정상 처리 | special_chars.png |
| E5 | 매우 긴 이름 | 50자 이상 이름 입력 시 레이아웃 유지 | long_name.png |

### 3.9 Analytics Agent 체크리스트

| # | 테스트 항목 | 분석 항목 |
|---|-----------|----------|
| AN1 | 클릭 热区 | 사용자가 가장 많이 클릭하는 영역 |
| AN2 | 이탈 지점 | 사용자가 서비스를 떠나는 위치 |
| AN3 | 클릭률 (CTR) | 각 버튼/링크의 클릭 빈도 |
| AN4 | 세션 시간 | 평균 사용 시간 및 전환율 |
| AN5 | 에러 발생률 | 각 에러 메시지의 표시 빈도 |

### 3.10 Security Agent 체크리스트

| # | 테스트 항목 | 예상 결과 |
|---|-----------|----------|
| SC1 | XSS 방지 | 스크립트 태그 입력 시 실행되지 않음 |
| SC2 | 입력 검증 | 특수문자가 포함된 입력 정상 처리 |
| SC3 | API 인증 | 백엔드 API가 적절한 에러 반환 |
| SC4 | 세션 관리 | 세션 타임아웃이 적절히 작동 |
| SC5 | HTTPS | 프로덕션 서버가 HTTPS 사용 |

---

## 4. 테스트 실행 계획

### 4.1 실행 순서

```
[Phase 1] 환경 설정 (Orchestrator)
│
├── [Phase 2] 기초 UX 점검 (에이전트 1-5)
│   ├── Visual QA Agent
│   ├── Localization Agent
│   ├── Mobile UX Agent
│   ├── Performance Agent
│   └── Accessibility Agent
│
├── [Phase 3] 기능 UX 점검 (에이전트 6-8)
│   ├── Search UX Agent
│   ├── Form UX Agent
│   └── Edge Case Agent
│
├── [Phase 4] 고급 분석 (에이전트 9-10)
│   ├── Analytics Agent
│   └── Security Agent
│
└── [Phase 5] 종합 보고
    └── UAT 종합 보고서 생성
```

### 4.2 예상 소요 시간

| Phase | 내용 | 소요 시간 |
|-------|------|---------|
| Phase 1 | 환경 설정 및 서버 상태 확인 | 10분 |
| Phase 2 | 기초 UX 점검 (5 에이전트) | 30분 |
| Phase 3 | 기능 UX 점검 (3 에이전트) | 25분 |
| Phase 4 | 고급 분석 (2 에이전트) | 20분 |
| Phase 5 | 종합 보고서 작성 | 15분 |
| **총계** | | **100분** |

---

## 5. 발견된 문제점 분류 기준

### 5.1 심각도 분류

|等级 | 설명 | 대응 시간 |
|-----|------|---------|
| 🔴 CRITICAL | 서비스 장애, 데이터 손실 위험 | 即時 해결 |
| 🟠 HIGH | 주요 기능 미작동, 사용자 불편 | 24시간 내 |
| 🟡 MEDIUM | UX 불편, 시각적 문제 | 1주일 내 |
| 🔵 LOW | 미미한 문제, 개선 권장사항 |次回 업데이트 |

### 5.2 영역 분류

| 영역 | 설명 |
|-----|------|
| VISUAL | UI/비주얼 관련 |
| I18N | 다국어/번역 관련 |
| MOBILE | 모바일 반응형 관련 |
| PERFORMANCE | 성능 관련 |
| ACCESSIBILITY | 접근성 관련 |
| SEARCH | 검색 기능 관련 |
| FORM | 입력 양식 관련 |
| EDGE | 예외 처리 관련 |
| SECURITY | 보안 관련 |

---

## 6. 산출물

### 6.1 필수 산출물

| # | 산출물 | 설명 |
|---|--------|------|
| 1 | `UAT_VISUAL_REPORT.md` | 비주얼 품질 점정 결과 |
| 2 | `UAT_I18N_REPORT.md` | 다국어 점정 결과 |
| 3 | `UAT_MOBILE_REPORT.md` | 모바일 UX 점정 결과 |
| 4 | `UAT_PERFORMANCE_REPORT.md` | 성능 점정 결과 |
| 5 | `UAT_ACCESSIBILITY_REPORT.md` | 접근성 점정 결과 |
| 6 | `UAT_SEARCH_REPORT.md` | 검색 UX 점정 결과 |
| 7 | `UAT_FORM_REPORT.md` | 양식 UX 점정 결과 |
| 8 | `UAT_EDGE_REPORT.md` | 경계 조건 점정 결과 |
| 9 | `UAT_ANALYTICS_REPORT.md` | 분석 결과 |
| 10 | `UAT_SECURITY_REPORT.md` | 보안 점정 결과 |
| 11 | `UAT_FINAL_REPORT.md` | 종합 최종 보고서 |

### 6.2 스크린샷 저장 구조

```
docs/agent_logs/
├── screenshots/
│   ├── 01_visual/
│   ├── 02_i18n/
│   ├── 03_mobile/
│   ├── 04_performance/
│   ├── 05_accessibility/
│   ├── 06_search/
│   ├── 07_form/
│   ├── 08_edge/
│   ├── 09_analytics/
│   └── 10_security/
└── reports/
    └── [위 산출물 MD 파일들]
```

---

## 7. 성공 기준

### 7.1 UAT 성공 조건

| 지표 | 목표값 |
|-----|-------|
| CRITICAL 문제 수 | 0건 |
| HIGH 문제 수 | ≤ 2건 |
| 평균 UX 점수 | ≥ 8.5/10 |
| 모바일 호환성 | 100% |
| 다국어 완전 지원 | 100% |
| 접근성 준수도 | WCAG 2.1 AA |

---

## 8. 참고 자료

- **이전 UAT 보고서:** `docs/agent_logs/UAT_TEST_REPORT.md`
- **화면 구조:** `docs/agent_logs/K-DESTINY_SCREEN_TREE.md`
- **작업 이력:** `docs/agent_logs/task.md`

---

*UAT 계획 작성 완료: 2026-02-23*
