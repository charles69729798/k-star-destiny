# [Goal] 동적 분석 엔진 고도화 및 유튜브 댓글 시스템 통합

단순히 저장된 텍스트를 보여주는 방식에서 벗어나, 사용자와 스타의 실제 데이터(사주 오행, MBTI)를 조합하여 **실시간으로 변화하는 동적 분석 결과**를 생성하고, 그 하단에 유튜브 스타일의 소셜 소통 창구를 구축합니다.

## Proposed Changes

### 1. 동적 엔진 고도화 (Backend)

#### [MODIFY] [saju_i18n.py](file:///c:/InsuranceProject/Sajuapp/backend/saju_i18n.py)
- **정적 문장을 템플릿화**: `{user_name}`, `{target_name}`, `{element}` 등의 변수를 포함한 문장으로 수정.
- 언어별(`en`, `es`, `pt`, `ko`)로 누락된 `SYNERGY_MISSIONS` 및 `MONTH_KEYWORDS`를 완벽히 구축.

#### [MODIFY] [saju_engine.py](file:///c:/InsuranceProject/Sajuapp/backend/saju_engine.py)
- **데이터 바인딩 알고리즘 적용**: `saju_i18n.py`의 템플릿을 가져와서 실시간 계산된 사용자와 스타의 정보(오행 관계, MBTI 매칭률 등)를 주입(`str.format()`)하여 최종 출력 생성.
- 하드코딩된 한글 파편을 모두 제거하고 로컬라이징 데이터 기반의 동적 생성 방식으로 전환.

### 2. 유튜브 스타일 댓글 보드 (Frontend)

#### [MODIFY] [App.tsx](file:///c:/InsuranceProject/Sajuapp/frontend/src/App.tsx)
- **YouTube Comment UI**: 
  - 댓글 수 표시 및 정렬(최신순/인기순) 버튼.
  - 핸들(`@Name`), 작성 시간(`1 hour ago`), 좋아요/싫어요/답글 버튼 구현.
  - 실제 유튜브 댓글 섹션의 레이아웃(Margin, Padding, Typo)을 정교하게 모사.
- **다국어 매핑**: 인터랙티브 보드에 필요한 모든 텍스트를 `translations` 맵에 4개 국어로 주입.

## Verification Plan

### Automated Tests
- 다양한 생년월일 조합으로 분석을 실행하여 결과 텍스트가 입력값에 따라 다르게 생성되는지 백엔드 단위 테스트 수행.

### Manual Verification
- 브라우저에서 언어를 변경하며 분석 결과 하단의 댓글 섹션이 정상 출력되는지 확인.
- 댓글 입력 및 좋아요 버튼 클릭 시 시각적 피드백(애니메이션) 확인.
