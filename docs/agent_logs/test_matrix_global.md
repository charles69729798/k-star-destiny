# UAT Multi-Agent Test Matrix (10 Users x 30 Stars)

## 1. Virtual User Personas (10)

| ID | Name | Lang | Birth Date | Gender | MBTI | Purpose of Test |
|:---|:---|:---|:---|:---|:---|:---|
| U1 | Minji | KO | 1998-05-12 | Female | ENFP | Korean Native & Calendar Analysis |
| U2 | James | EN | 1995-12-25 | Male | INTJ | English UI & Hard-T Logic |
| U3 | Garcia | ES | 1990-01-01 | Female | ESFJ | Spanish Translation & Edge Date |
| U4 | Silva | PT | 2002-08-15 | Non-binary| INFP | Portuguese Expansion & Sensitivity |
| U5 | Yuki | EN | 2005-03-03 | Female | ISFP | Gen-Z Vibe & Emoji Check |
| U6 | Kim | KO | 1985-11-20 | Male | ISTJ | Older Gen User & Accuracy |
| U7 | Elena | ES | 1997-07-07 | Female | ENFJ | Passionate Interaction & Mission |
| U8 | Joao | PT | 1993-04-20 | Male | ENTP | Portuguese Transition & Error Logic |
| U9 | Smith | EN | 2000-02-29 | Female | INFJ | Leap Year Bug & Rare MBTI |
| U10 | Park | KO | 2010-10-10 | Female | ENTJ | Alpha Gen & Future Prediction |

## 2. Global Star Scan List (30)

- **IDOL_POOL (Local)**: 장원영, 카리나, 정국, 차은우, 뷔, 지수, 제니 등 20인
- **AI Search (External)**: NewJeans Hanni, BTS RM, TXT Yeonjun, aespa Winter, IVE Yujin 등 10인

## 3. Verification Checklist (무결성 기준)

1. **Deterministic Results**: 동일 입력에 대해 상시 동일한 사주 결과 도출 여부.
2. **No Korean Residue**: EN/ES/PT 모드에서 한국어 문자열 1개라도 노출 시 실패.
3. **Data Integrity**: 장원영(IVE) 검색 시 생일(2004-08-31) 및 MBTI(ENTJ) 정합성.
4. **UI Harmony**: 모든 컴포넌트가 Glassmorphism 스타일을 유지하며 중복 배너가 없는지.
5. **Mission Logic**: 사주 시너지 점수에 따른 동적 미션 3종이 논리적으로 타당한지.
