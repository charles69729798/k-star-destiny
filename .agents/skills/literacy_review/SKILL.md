---
name: literacy_review
description: 서비스 내 4개 국어(KO, EN, ES, PT) 미션 문구의 문법, 문맥 및 관계 적절성 검토 스킬
---

# Literacy Review Skill (Team-Based)

이 스킬은 5인의 전문 에이전트 군단을 활용하여 K-Star Destiny의 다국어 미션 카드를 다각도에서 검토하고 최적화하는 방법을 정의합니다.

## 전문 에이전트 팀 구성 (The Literacy Team)

1. **Psychologist**: 관계의 정서적 경계 및 과거 경험 전제 오류 진단.
2. **Cultural Expert**: 글로벌 에티켓 및 문화적 금기 사항 검토.
3. **Trend Expert**: MZ 언어 뉘앙스 및 신조어 자연스러움 평가.
4. **Harmony Expert**: 오행 이론과 미션 액션 사이의 논리적 일치성 검증.
5. **Storytelling Expert**: 미션의 서사적 흐름 및 사용자 기여도 분석.

## 고도화된 검토 원칙 (Advanced Principles)

1. **비논리적 과거 삭제 (Erase Illogical Past)**
   - {target}과의 과거 경험(사진, 기억, 단골 장소 등)을 서비스가 임의로 생성하는 것을 엄격히 금지합니다.
   - **수정 가이드**: 모든 과거형 동사를 '현재 도출형' 또는 '미래 제안형'으로 전환합니다.

2. **오행-액션 일치 (Elemental Logic)**
   - 사용자의 사주 오행이 미션의 '분위기'와 논리적으로 연결되어야 합니다.

3. **통합 문해력 점수 (Literacy Integrity Score)**
   - 각 에이전트의 관점에서 1~5점을 부여하며, 하나라도 2점 이하일 경우 '수정 요망'으로 분류합니다.

## 통합 검토 워크플로우 (Multi-Agent Workflow)

1. **Discovery**: `backend/literacy_team_audit.py`를 통해 전수조사 대상 리스트를 뽑습니다.
2. **Debate**: 발견된 문구에 대해 5인의 에이전트 관점에서 비판적 검토를 수행합니다.
3. **Consolidation**: 검토 의견을 종합하여 '논리적 결함이 없는' 최적의 대안 문구를 도출합니다.
4. **Implementation**: `saju_i18n.py`에 반영하고 다국어 동기화를 수행합니다.
