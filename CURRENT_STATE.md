# 📝 현재 작업 진척도 및 인수인계 사항 (Last Updated: 2026-03-05)

## 직전 완료된 작업 (최근 세션 요약)
- **프론트엔드(`App.tsx`):** 한국어(KO) ↔ 영어(EN) 등 언어 탭 전환 시 또는 '스타와 매칭' ↔ '친구와 매칭' 모드 전환 시, 사용자가 이전에 입력해 둔 '내 프로필(생년월일, 성별, MBTI)'과 '검색창 텍스트'가 날아가는 상태 초기화 버그를 완벽하게 수정 및 검증(UAT) 완료.
- **백엔드(`main.py`):** 존재하지 않는 `git_sync` 모듈 임포트로 인한 uvicorn 서버 크래시 에러 해결 및 해당 코드 주석 처리 완료.
- **AI 엔진(`run_search.py`):** 검색 엔진(Wikipedia) 실패 시 DuckDuckGo 크롤러로 자동 fallback되어 인물 정보 및 MBTI를 찾아오는 로직 정상 구동 확인 완료.
- **배포 및 인프라:** 
  - `destiny-signal.duckdns.org` 도메인 실서버 연동을 위해 `backend/.env` 및 `frontend/.env.production` 환경 변수 최신화 완료.
  - 로컬 핫 리로딩(Volume Mount) 환경의 실체를 확인하였고, `docker-compose down && up -d --build`를 통해 성공적으로 실서버 배포(적용)까지 마침.

## 현재 집중하고 있는 문제 (또는 다음 목표)
- 본 세션에서의 가장 큰 목표였던 "로컬 UAT 및 실서버 배포"까지 성공적으로 완수되었습니다.
- (향후 논의 필요) 4개 국어(KO, EN, ES, PT) 응답 메시지의 톤앤매너, 문법적 자연스러움 체크.
- (향후 논의 필요) 나무위키 등 추가 정보 파서의 성능 향상 또는 속도 이슈 최적화 여부.

## 다음에 올 AI를 위한 팁
- 이 프로젝트는 `localhost` 포트가 아닌 **Docker 내 핫-리로딩 환경(Hot-Reloading Volume Mount)**으로 구동됩니다. 
- 파이썬/JS 코드를 직접 수정하기만 하면 곧바로 `destiny-signal.duckdns.org` 라이브 서버에 반영되므로, 절대 사용자에게 `npm run dev`나 `GitHub Push/Pull` 배포 명령어를 요구하지 마십시오.
