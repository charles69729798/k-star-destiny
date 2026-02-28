# K-Destiny 도커 배포 및 운영 가이드

본 프로젝트는 Docker Compose를 이용한 컨테이너 기반 배포 환경을 지원합니다. 타 AI 또는 운영자가 서비스를 클라우드나 서버 환경에 배포할 때 아래 절차를 따르십시오.

---

## 🏗️ 1. 도커 시스템 구조 (Architecture)
- **Nginx (Gateway)**: 외부 80 포트를 통해 접속을 받으며, `/api` 경로는 백엔드로, 나머지는 프론트엔드로 전달합니다.
- **Backend (FastAPI)**: Python 기반 컨테이너 (실행 포트: 8000).
- **Frontend (Vite/React)**: 빌드된 정적 파일을 서빙하거나 개발용 컨테이너로 동작 (실행 포트: 5173).

---

## 🚀 2. 실행 명령어 (Deployment)

### 서비스 전체 빌드 및 실행
```bash
docker-compose up --build -d
```
- `-d`: 백그라운드 실행 모드입니다.
- `--build`: 소스 코드 변경 사항을 반영하여 이미지를 새로 생성합니다.

### 서비스 중지 및 삭제
```bash
docker-compose down
```

### 로그 실시간 확인
```bash
docker-compose logs -f
```

---

## ⚠️ 3. 로컬 환경과의 포트 충돌 주의 (Important)
**가장 많이 발생하는 오류**: 로컬에서 `npm run dev`나 `python main.py`를 실행 중인 상태에서 Docker를 올리면 포트 충돌이 발생합니다.

- **조치**: Docker 배포 전 반드시 로컬 서버를 종료하거나, `taskkill`을 통해 기존 프로세스를 정리하십시오.
- **포트 매핑**:
  - **Docker**: 호스트 80 포트로 접속 ([http://localhost](http://localhost))
  - **Local**: 호스트 5173/8000 포트로 접속

---

## 🛠️ 4. 구성 파일 위치
- **Compose 파일**: `./docker-compose.yml`
- **Nginx 설정**: `./deploy/nginx/nginx.conf`
- **Frontend Dockerfile**: `./frontend/Dockerfile`
- **Backend Dockerfile**: `./backend/Dockerfile`

---

> [!IMPORTANT]
> **운영 팁**: Docker 컨테이너 내에서 코드가 업데이트되지 않은 것처럼 보인다면, `docker-compose down -v`를 통해 익명 볼륨을 삭제하고 `--build` 옵션과 함께 재시작하십시오.
