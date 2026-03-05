---
description: K-Star Destiny 프로젝트의 단일 서버 및 Docker 아키텍처, 도메인, SSL 인증서 환경 상세 가이드
---

# K-Star Destiny 배포 및 인프라 상세 가이드

이 문서는 AI 요원(Agents)이 이 프로젝트(`c:\InsuranceProject\k-star-destiny`)에서 작업할 때 현재 시스템의 아키텍처와 배포 구조를 완벽히 이해하도록 돕기 위한 필수 지침서입니다.

## 1. 전반적인 서버 환경 (로컬 PC = 운영 서버)
현재 프로젝트가 저장되고 실행되고 있는 Windows 컴퓨터 자체가 실제 서비스가 전 세계로 구동되는 **메인 운영 서버(Production Server)**입니다.
즉, 전통적인 방식처럼 로컬에서 개발한 뒤 GitHub에 소스를 올리고, AWS 같은 다른 원격 리눅스 서버에서 이를 다운(Pull)받아 배포하는 과정을 거치지 않습니다.

## 2. 운영 도메인 및 SSL 인증서 (Certbot)
- **운영 간판(도메인):** `https://destiny-signal.duckdns.org`
- **SSL 인증서 저장소:** 프로젝트 내 `./deploy/certbot/conf/live/destiny-signal.duckdns.org/` 폴더에 실서버용 인증서 페어(`fullchain.pem`, `privkey.pem`)가 존재합니다.
- **자동 갱신:** `sajuapp-certbot` 컨테이너가 12시간마다 백그라운드에서 Let's Encrypt 만료 여부를 체크하고 자동으로 갱신(renew)을 시도하는 완벽한 구조를 갖추고 있습니다.

## 3. Nginx 대문 방 (게이트웨이)의 역할
- **컨테이너 이름:** `sajuapp-gateway`
- **주요 역할 (라우팅 및 보안):** 외부 인터넷에서 80번(HTTP) 또는 443번(HTTPS) 포트로 들어오는 모든 손님을 제일 먼저 맞이하는 대문입니다.
- **세부 설정 (`deploy/nginx/nginx.conf`):**
  - **도메인 검증:** `server_name destiny-signal.duckdns.org;` 설정을 통해 해당 도메인명으로 찾아온 정상적인 요청만 처리합니다.
  - **API 길잡이:** `https://destiny-signal.duckdns.org/api/...` 로 들어오는 요청은 사주 원리를 계산하는 **백엔드 주방(`http://backend:8000`)**으로 보냅니다.
  - **화면 길잡이:** 나머지 모든 요청(`/`)은 예쁜 화면을 띄워주는 **프론트엔드 홀(`http://frontend`)**로 보냅니다.

## 4. Docker 컨테이너 4형제와 볼륨 마운트 (Hot-Reloading)
이 프로젝트는 총 4개의 컨테이너 방이 띄워져 있으며, 이 방들은 로컬 윈도우 폴더와 **창문(Volume Mount)**이 뚫려 있어 실시간 동기화가 이루어집니다.
1. `sajuapp-gateway` (nginx): 통신 대문 처리 (위 3번 항목 참조).
2. `sajuapp-certbot` (certbot): SSL 인증 관리.
3. `sajuapp-backend` (python): 백엔드 파이썬 알고리즘. `./backend` 폴더 내 파일이 수정되면 **즉시 재가동(Reload)** 됩니다.
4. `sajuapp-frontend` (node): 프론트엔드 React 화면. `./frontend` 폴더 내 소스가 수정되면 역시 **즉시 반영**됩니다.

## 5. 배포(업데이트) 가이드
위에서 설명한 볼륨 마운트 구조 덕분에, **소스 코드(파이썬, 자바스크립트 등)를 저장(수정)하는 순간, 별도의 재구동이나 터미널 명령어 없이도 실제 도메인 인터넷 서비스에 즉각(Hot-Reload) 반영됩니다.**

단, 아래와 같이 **'인프라의 뼈대'**를 수정했을 때만 도커를 껐다 켜야(배포 명령어) 합니다:
- `.env` 등 환경 변수 파일 수정 시
- `Dockerfile` 내부 설정 수정 시
- `requirements.txt`나 `package.json`에서 새로운 언어팩/라이브러리를 추가 설치했을 때
- Nginx 설정 파일 (`nginx.conf`) 변경 시

**인프라 변경 시 수동 배포 명령어:**
```bash
docker-compose down
docker-compose up -d --build
```

## 6. AI 요원 (Agent) 핵심 금지 사항
다음 작업부터 AI가 코드를 수정하거나 배포를 안내할 때 아래 규칙을 반드시 준수하십시오:
- **전통적인 배포 방식 제안 금지:** GitHub Commit/Push/Pull이나 외부 원격 서버로의 접속(SSH) 절차를 사용자에게 요구하거나 안내하지 마십시오.
- **서버 환경 절대 인지:** 이 PC(`c:\InsuranceProject\k-star-destiny`)에서 뜨는 Docker가 곧 전 세계로 서비스되는 라이브(운영) 서버임을 명심하십시오.
