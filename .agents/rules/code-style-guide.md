---
description: description: 파일 저장 자동화 및 한국어 고정 룰
---

description: 파일 저장 자동화 및 한국어 고정 룰
---

# 필수 준수 사항 (Always On)

1. 언어: 모든 답변과 코드 주석은 '한국어'로만 작성한다.
2. 작업 가시성: 에이전트 내부의 task.md 아티팩트와 별개로, 모든 작업의 진행 상황(테스크 리스트)과 결과 리포트(.md)는 사용자가 실시간으로 확인할 수 있도록 반드시 워크스페이스 '루트 디렉토리(./)'에 '_MMDD_HHMM' 형식의 파일명을 붙여 `write_to_file` 도구(IsArtifact=false)를 사용하여 즉시 저장 또는 갱신한다.

4. 개발 환경: uv를 사용하며 가상환경은 .venv 폴더를 이용한다.
5. 시각화: matplotlib 사용 시 koreanize-matplotlib을 기본 설정한다.