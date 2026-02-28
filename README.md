# 🔮 K-Destiny AI: Global K-pop Saju & MBTI Matching

![K-Destiny Banner](https://img.shields.io/badge/K--Pop-Saju-blueviolet?style=for-the-badge&logo=k-pop)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=fastapi&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

**K-Destiny AI** is a premium web application that connects global K-pop fans with their favorite stars through the mystical lens of **K-Saju (Korean Traditional Fortune Telling)** and **MBTI**.

---

## ✨ Key Features

- **Soul Index (K-Saju):** Deep analysis of your core element (Wood, Fire, Earth, Metal, Water) based on ancient Korean algorithms.
- **2026 God-saeng Calendar:** A monthly fortune guide filled with dopamine-boosting insights and "Lucky Vicky" vibes.
- **Destiny Signal:** Universal telepathy analysis between you and your idol, featuring personality matching and synergy tips.
- **AI Idol Search:** Automatically retrieves idol data from Wikipedia and Namuwiki.
- **Multi-language Support:** Fully localized in **English**, **Korean**, and **Spanish** with Gen-Z slang (Slay, Rizz, Vibes).
- **Premium UI/UX:** Stunning Glassmorphism design with smooth Framer Motion animations.

## 🚀 Tech Stack

### Frontend
- **Framework:** React 19 (Vite)
- **Styling:** Tailwind CSS v4 (Vanilla CSS philosophy)
- **Animations:** Framer Motion
- **Icons:** Lucide React

### Backend
- **Framework:** FastAPI (Python 3.11)
- **Search Engine:** Playwright & BeautifulSoup4 for real-time web scraping.
- **Analysis:** Custom Saju/MBTI Mapping Algorithm.
- **Infrastructure:** Docker & Docker Compose ready.

## 🛠️ Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[YOUR_USERNAME]/K-Destiny-MZ-Saju.git
   cd K-Destiny-MZ-Saju
   ```

2. **Backend Setup:**
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

3. **Frontend Setup:**
   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```

4. **Access the App:**
   Open `http://localhost:5173` in your browser.

## 🐳 Docker Deployment (Independent Linux Environment)

본 프로젝트는 리눅스 컨테이너(Docker) 기반의 독립 구동을 지원합니다. 외부에서 접속 가능한 서버를 구축하려면 아래 명령어를 사용하세요.

```bash
# 전체 서비스 빌드 및 백그라운드 실행
docker-compose up -d --build
```

### Infrastructure Summary
- **Gateway (Nginx)**: Port 80 (외부 접속 창구)
- **Frontend**: Multi-stage 빌드된 정적 파일을 Nginx가 서빙
- **Backend API**: `/api` 경로를 통해 격리된 포트로 프록시 매핑

### 외부 접속 가이드
1. 서버의 방화벽에서 **80번 포트**를 개방하세요.
2. 도메인 또는 서버 IP를 통해 `http://서버IP`로 접속 가능합니다.

---

## 🎨 Design Philosophy
K-Destiny focuses on **"Vibe Coding"**—creating an emotional connection with users through high-quality aesthetics, interactive micro-animations, and a youthful, energetic tone.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Built with passion by the K-Destiny AI Team.*
