# Draft: Playwright UAT Automation & UI Optimization

## Requirements (confirmed)
- [UAT]: Implement automated E2E tests using Playwright.
- [Scenarios]: 
    1. Idol Search (Success, Multi-candidate, MBTI Fallback).
    2. Analysis Execution (Validation checks, Result display).
    3. Mission System (Interaction, Score calculation verification).
    4. I18n (KO/EN/ES/PT switching, check key UI elements).
- [Bug Fixes]: Address missing translations (ES/PT) and hardcoded Korean strings in `App.tsx`.
- [Performance]: Apply Framer Motion optimizations (upgrade to v12+, `layoutDependency`).

## Technical Decisions
- [Testing Tool]: Playwright (TypeScript).
- [Target URL]: `http://localhost:5173`.
- [I18n Strategy]: Sync missing keys in `App.tsx` translations object based on `bg_c601481d` audit.
- [Performance Pattern]: Force GPU acceleration via `translate3d(0,0,0)` and use `layout="position"`.

## Research Findings
- [bg_acf7f313]: Frontend is a single 2,700-line `App.tsx`. API endpoints mapped.
- [bg_c601481d]: Found missing PT/ES keys (`recentFortune`, `stage`, `userSajuResult`) and 6 hardcoded string instances.
- [bg_475ed3dc]: MBTI fallback logic verified as robust.
- [bg_f154fd05]: Recommended upgrade to `motion/react` and using `layoutDependency` for large files.

## Open Questions
- None (All confirmed).

## Scope Boundaries
- INCLUDE: Playwright setup, Test writing, I18n fix, Performance tuning.
- EXCLUDE: Large-scale component decomposition (postponed per user request "작업 전략은 나중에").
