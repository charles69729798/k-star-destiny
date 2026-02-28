# K-Destiny AI 화면 기능 트리 구조

```
🌐 K-DESTINY AI (http://localhost:5173)
│
├── 🌍 Language Switcher
│   └── [ES] [EN] [KO]
│
├── 📌 HEADER
│   ├── Title: "K-DESTINY AI"
│   ├── Subtitle: "Global Saju + MBTI Matching for K-pop Fans"
│   └── Intro Box
│
├── 👤 사용자 프로필 섹션
│   ├── 📅 생년월일 입력 (YYYY-MM-DD)
│   ├── ⚥ 성별 선택 (Female/Male/Non-binary)
│   └── 🧠 MBTI 입력 (QuickMBTI 컴포넌트)
│
├── 🔄 모드 전환
│   ├── 🎤 스타 매칭 (Idol Mode)
│   └── 👥 지인 매칭 (Friend Mode)
│
├── 🔍 검색/입력 영역
│   │
│   │ 🎤 [Idol Mode]
│   │   ├── 검색 입력창
│   │   ├── AI 검색 버튼
│   │   ├── 후보 선택 UI (동명이인)
│   │   └── 인기 아이돌 목록
│   │
│   │ 👥 [Friend Mode]
│   │   ├── 이름 입력
│   │   ├── 성별 선택
│   │   ├── 생년월일 입력
│   │   └── MBTI 입력
│
├── ⚠️ 상태 메시지
│
├── 🎯 아이돌 프로필 배너
│
├── 📊 분석 결과 영역
│   ├── ⚡ 분석 전 화면
│   └── 📈 분석 후 화면
│       ├── 🔮 Tab 1: Soul Index (K-사주)
│       ├── 📅 Tab 2: 2026 갓생 캘린더
│       └── 📡 Tab 3: Destiny Signal
│
└── 🦶 FOOTER
```

---

## 주요 기능 요약

| 기능 | 설명 |
|------|------|
| **MBTI Picker** | QuickMBTI - 16가지 MBTI 선택 팝업 |
| **AI 검색** | 백엔드 API로 아이돌 정보 자동 수집 |
| **후보 선택** | 동명이인 있을 때 선택 UI |
| **3가지 탭** | Soul Index / 갓생 캘린더 / Destiny Signal |
| **다국어** | 영어, 한국어, 스페인어 자동 감지 |

---

## UAT 테스트 체크리스트

- [ ] MBTI Picker: 16가지 유형 선택 팝업 확인
- [ ] 지인 매칭 모드: 탭 전환 후 MBTI 선택
- [ ] Ctrl + Shift + R: 강력 새로고침
- [ ] 스타 모드: 아이유 검색 → 분석 실행
- [ ] 지인 모드: 이름 입력 → 분석 실행
- [ ] 모바일 반응형: 375px 레이아웃 확인
