# 실행 계획서: 명명 규칙 최적화 및 지침 준수 확고화 (0227_0846)

이 계획서는 지침 파일 내의 날짜 형식을 사용자의 요청에 따라 `MMDD_HHMM`으로 완전히 고정하고, 모든 아티팩트의 무결성을 재검증하는 것을 목표로 합니다.

## 제안된 변경 사항

### 1. 지침 파일(instructions.md) 최종 정비
- **[instructions.md](file:///C:/InsuranceProject/Sajuapp/instructions.md)**: 
  - `파일명_YYYYMMDD_HHMM`이라는 텍스트가 남아있지 않도록 전면 검토 및 수정합니다.
  - 모든 예시와 규정을 `MMDD_HHMM` 형식으로 통일합니다.
  - 연도 기재에 관한 예외 조항을 삭제하여 형식을 엄격히 통제합니다.

### 2. 아티팩트 정렬 및 실시간 기록
- 현재 세션에서 생성되는 모든 문서의 파일명 및 헤더를 `MMDD_HHMM` 형식으로 동기화합니다.
- `C:\InsuranceProject\Sajuapp` 경로에 실시간으로 저장되는지 상시 확인합니다.

---

## 검증 계획

### 자동화 테스트
- `C:\InsuranceProject\Sajuapp\instructions.md` 파일에서 `YYYYMMDD` 문자열을 검색하여 결과가 0건인지 확인합니다.

### 수동 검증
1. 본 계획서 및 `task_0227_0846.md` 파일의 제목과 파일명이 `MMDD_HHMM` 포맷을 따르는지 확인합니다.
2. 사용자가 `instructions.md`를 열었을 때 `파일명_MMDD_HHMM`이 명확히 명시되어 있는지 검토합니다.
