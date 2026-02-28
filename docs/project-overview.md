# 🏗️ K-Destiny AI 프로젝트 개요 및 배포 가이드

이 문서는 K-Destiny AI 프로젝트의 주요 파일 구조와 Git을 통한 배포 및 운영 환경 설정을 정리한 가이드입니다.

---

## 📂 1. 주요 파일 구조 및 역할

### 🔹 Backend (`/backend`)
FastAPI 기반의 서버로, 사주 로직 분석 및 아이돌 데이터 수집을 담당합니다.
- `main.py`: 서버 엔트리 포인트 및 API 라우팅.
- `saju_engine.py`: 생년월일 기반 오행 및 사주 분석 핵심 엔진.
- `ai_search.py`: Playwright/BS4를 이용한 아이돌 정보(생일, MBTI) 수집 로직.
- `saju_i18n.py`: 다국어(KO, EN, ES) 번역 및 로컬라이징 관리.
- `idols.json`: 사전 수집된 아이돌 데이터베이스.
- `requirements.txt`: 백엔드 의존성 패키지 목록.

### 🔹 Frontend (`/frontend`)
React 19(Vite) 기반의 SPA로, 사용자 경험(UX) 및 인터렉티브 UI를 담당합니다.
- `src/App.tsx`: 메인 어플리케이션 컴포넌트 및 레이아웃.
- `src/components/`: MBTI Picker, 분석 결과 탭 등 재사용 가능한 UI 컴포넌트.
- `src/main.tsx`: 앱 렌더링 시작점.
- `tailwind.config.js`: Tailwind CSS v4 스타일링 설정.

### 🔹 Documentation (`/docs`)
- `user-manual.md`: 일반 사용자를 위한 서비스 이용 가이드.
- `agent_logs/`: 개발 및 UAT(테스트) 과정에서 생성된 상세 로그 및 보고서.
- `SAJU_LOGIC.md`: 사주-MBTI 매핑 알고리즘 상세 설계 문서.

---

## 🚀 2. Git 및 배포 가이드

본 프로젝트는 **Docker 컨테이너**를 통한 독립적이고 일관된 배포 환경을 지향합니다.

### 🐳 Docker 배포 (추천)
루트 디렉토리의 `docker-compose.yml`을 사용하여 전체 스택(Nginx, Backend, Frontend)을 한 번에 구동합니다.

1.  **서비스 빌드 및 실행:**
    ```bash
    docker-compose up -d --build
    ```
2.  **인프라 구성:**
    - **Nginx (Port 80)**: 외부 요청을 받는 게이트웨이. `/api` 경로는 백엔드로, 나머지는 프론트엔드로 라우팅.
    - **Backend (Port 8000)**: 내부망(`saju-net`)에서만 노출되며 Nginx를 통해 통신.
    - **Frontend**: 정적 파일 빌드 후 Nginx가 직접 서빙.

### 🛠️ 수동 배포 (개발 환경)
Docker 없이 로컬에서 테스트할 경우의 순서입니다.

1.  **Backend:**
    ```bash
    cd backend
    pip install -r requirements.txt
    python main.py
    ```
2.  **Frontend:**
    ```bash
    cd frontend
    npm install
    npm run dev
    ```

### ⚠️ 배포 시 주의사항
- **환경 변수**: `backend/Dockerfile` 및 `docker-compose.yml`에서 `ENV=production` 설정을 확인하세요.
- **포트 개방**: 클라우드 서버(AWS, GCP 등) 배포 시 인바운드 규칙에서 **80번 포트**를 반드시 개방해야 합니다.
- **Git 관리**: `.gitignore` 설정에 따라 `node_modules`, `__pycache__`, `.env` 등 민감하거나 불필요한 파일이 저장소에 포함되지 않도록 관리되고 있습니다.

---
*최종 업데이트: 2026-02-28*
