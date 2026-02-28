# 실행 계획서: 지침 파일 및 워크플로우 무결성 동기화 (0227_0959)

이 계획서는 사용자가 제공한 이미지와 실제 `instructions.md` 파일 간의 불일치(날짜 형식 등)를 해결하고, 프로젝트 전반의 지침을 `MMDD_HHMM` 형식으로 통일하는 것을 목표로 합니다.

## 제안된 변경 사항

### 1. 지침 파일(instructions.md) 전면 동기화 (완료)
- **[instructions.md](file:///C:/InsuranceProject/Sajuapp/instructions.md)**: 
  - 파일명 규칙을 `파일명_MMDD_HHMM`으로 확정.
  - 헤더 및 단계(Phase/Step) 명칭에 `(MMDD_HHMM)` 필수 기재 원칙 유지.
  - 이미지에서 발견된 `YYYYMMDD` 형식을 모두 제거하고 최신화된 예시로 교체.

### 2. 프로젝트 관리 리포트 무결성 검증
- 새로 생성되는 모든 아티팩트(`implementation_plan`, `task`, `walkthrough`)에 대해 강화된 명명 규칙을 엄격히 적용합니다.
- 프로젝트 루트 디렉토리(`C:\InsuranceProject\Sajuapp`)에 실시간 저장 여부를 상시 확인합니다.

---

## 검증 계획

### 자동화 테스트
- `C:\InsuranceProject\Sajuapp\instructions.md` 내에 `YYYYMMDD` 문자열이 포함되어 있는지 검색하여 0건임을 확인합니다.
- 프로젝트 폴더 내 최신 생성 파일들이 `_MMDD_HHMM.md` 형식을 갖추었는지 리스팅합니다.

### 수동 검증
1. 본 계획서 및 `task_0227_0959.md`의 최상단 헤더에 `(0227_0959)`가 명확히 기재되어 있는지 확인합니다.
2. 사용자가 지적한 "이미지와의 차이"가 해소되었음을 `instructions.md` 내용을 통해 최종 입증합니다.
