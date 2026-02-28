# [Goal] 동적 분석 엔진 고도화 및 유튜브 댓글 시스템 통합 (v5)

사용자의 피드백을 바탕으로 **지인 이름 입력 필드를 제거**하고, 모든 분석 문구를 **4개 국어 기반 동적 템플릿**으로 전환하여 실시간 데이터 결합력을 극대화합니다. 또한 하단에 유튜브 스타일의 소셜 소통 창구를 구축합니다.

## User Review Required

> [!IMPORTANT]
> - **지인 이름 입력 제거**: 현재 존재하는 지인(Partner) 이름 입력 필드를 UI에서 제거하고, 사주 분석 로직에서도 이를 제외합니다.
> - **다국어 동적 변환**: `saju_i18n.py`의 모든 문구를 `{element}`, `{mbti}` 등의 변수를 포함한 템플릿으로 변경하여, 어떤 언어에서도 동일한 알고리즘이 적용되도록 합니다.

## Proposed Changes

### 1. 프론트엔드 UI 정비 (Frontend)

#### [MODIFY] [App.tsx](file:///c:/InsuranceProject/Sajuapp/frontend/src/App.tsx)
- **입력 필드 삭제**: 지인(Friend/Partner)의 이름을 입력받는 `Input` 필드를 삭제하여 사용자 인터페이스를 간소화합니다.
- **YouTube Comment UI 통합**: 
  - 댓글 수 표시, 핸들(@), 타임스탬프, 좋아요/댓글 기능을 포함한 '소울 커뮤니티' 섹션 추가.
  - 실제 유튜브와 동일한 레이아웃 가이드라인 준수.

### 2. 동적 엔진 고도화 (Backend)

#### [MODIFY] [saju_i18n.py](file:///c:/InsuranceProject/Sajuapp/backend/saju_i18n.py)
- **4개 국어 템플릿화**: `ko`, `en`, `es`, `pt` 모든 언어의 텍스트를 `{var}` 변수 기반 문장 구조로 변환.
- 정적인 문장을 세밀한 '데이터 포인트'로 분절하여 정의.

#### [MODIFY] [saju_engine.py](file:///c:/InsuranceProject/Sajuapp/backend/saju_engine.py)
- **실시간 데이터 바인딩**: 계산된 사주 데이터와 MBTI 특성을 `saju_i18n.py`의 템플릿에 주입하여 결과를 생성.
- **알고리즘 강화**: 랜덤 선택 비중을 줄이고, 실제 오행 관계에 따른 문장 조합 로직 적용.

## Verification Plan

### Automated Tests
- 백엔드 테스트 스크립트를 통해 4개 국어 모두에서 동적 변수가 올바르게 치환되는지 확인.

### Manual Verification
- UI에서 지인 이름 필드가 사라졌는지 확인.
- 분석 결과 하단의 유튜브 댓글 보드가 정상적으로 렌더링되고 소셜 인터랙션이 작동하는지 육안 점검.
