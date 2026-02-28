# 🧪 Sajuapp: Comprehensive Test Strategy

## 1. Overview
The Sajuapp project aims to provide K-pop fans with Saju-MBTI matching and AI-driven idol search. This document defines the quality standards and verification plan to ensure a robust and accurate user experience.

## 2. Success Criteria (KPIs)
| Metric | Target | Description |
| :--- | :--- | :--- |
| **Match Rate** | >= 90% | Accuracy of AI-extracted idol data and Saju compatibility logic. |
| **Critical Issues** | 0 | No P0/P1 bugs, security leaks, or core feature failures. |
| **API Response Time** | < 2s (Mock) | Quick response for search and analysis. |
| **Test Coverage** | > 80% (Core) | Unit and integration tests for matching algorithms. |

## 3. Verification Plan

### 3.1 Static Code Analysis & Linting
- **Frontend**: TypeScript strict mode, ESLint for pattern consistency.
- **Backend**: Ruff/Pytest-check for Python code quality.

### 3.2 Automated Testing
- **Unit Tests (Backend)**: Verify Saju calculation logic (Five Elements) and MBTI mapping.
- **Integration Tests**: Test the `/api/idol/search` and `/api/saju/analyze` endpoints.
- **E2E Tests**: (Future) Playwright/Cypress for the full "Search -> Analyze -> Share" flow.

### 3.3 Feature Gap Detection
- **AI Search**: Move from mock data to actual extraction logic (using LLM/Scraping).
- **MBTI Diagnostic**: Implement the "1-minute Quick MBTI" tool for users without MBTI data.
- **Day Pillar Mode**: Support analysis for users without birth times.

### 3.4 Runtime Monitoring
- Log AI extraction failures to refine the extraction prompts.
- Monitor API error rates and performance under load.

## 4. Current Quality Status (As of Feb 21, 2026)
- **Quality Grade**: 🟡 Yellow (Functional MVP, no tests)
- **Coverage**: 0%
- **Identified Risks**:
  - Dependency on mock data for "AI Search".
  - Lack of input validation for birth dates/times.
  - No automated verification for Saju calculation logic.

## 5. Recommended Actions
1. **Implement Unit Tests** for `backend/main.py` using `pytest`.
2. **Add Input Validation** (Pydantic models) for API endpoints.
3. **Build the MBTI Diagnostic UI** to fulfill the "Must-have" requirement.
4. **Configure CI/CD** with linting and test execution.
