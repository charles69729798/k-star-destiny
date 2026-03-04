# Plan: Create Antigravity Workspace Rules for K-Destiny AI

## TL;DR
> **Quick Summary**: Create a comprehensive workspace rule for the Antigravity AI agent to ensure consistent development, maintenance, and UAT of the K-Destiny AI (Saju + MBTI) service.
> 
> **Deliverables**: 
> - `.sisyphus/docs/ANTIGRAVITY_WORKSPACE_RULES.md` (Rule source)
> - Ready-to-paste snippet for Antigravity Workspace Rule.
> 
> **Estimated Effort**: Quick
> **Parallel Execution**: YES
> **Critical Path**: Rule content generation → User confirmation

---

## Context

### Original Request
Create the first Workspace-level rule in Antigravity for the `k-star-destiny` project to minimize repetitive prompts and ensure the AI agent follows project-specific constraints during modification and management.

### Interview Summary
- **Target**: Antigravity "+ Workspace" rule.
- **Project**: K-Destiny AI (Global K-pop Saju & MBTI matching).
- **Frontend**: React 19 (Vite), Tailwind CSS v4, Framer Motion (Vibe Coding).
- **Backend**: FastAPI (Python 3.11), Pydantic, APScheduler.
- **Infrastructure**: Docker, Docker Compose, Nginx, Certbot SSL.

---

## Work Objectives

### Core Objective
Generate a structured rule set that identifies the project's identity, tech stack, design philosophy, and operational guardrails to optimize AI development within the Antigravity environment.

### Concrete Deliverables
- [ ] `.sisyphus/docs/ANTIGRAVITY_WORKSPACE_RULES.md`: A source file containing the rules for version control.
- [ ] Final summary with the copy-pasteable text for the Antigravity UI.

### Definition of Done
- [ ] Markdown file created in `.sisyphus/docs/`.
- [ ] Rule content includes Tech Stack, Design Policy, Logic Context, and Deployment Knowledge.

### Must Have
- Awareness of React 19 and Tailwind v4 (Alpha/Beta stage compatibility).
- "Vibe Coding" philosophy for frontend changes.
- Multi-language support requirements (EN, KO, ES).
- Docker/Nginx/Certbot configuration awareness.

### Must NOT Have
- Suggestions for alternative frameworks (e.g., Next.js, Django) unless explicitly requested.
- Inconsistent naming conventions for Saju-related logic.

---

## Verification Strategy

### QA Policy
Since this is a documentation/rule-creation task, the verification will involve the agent (Sisyphus) reading the generated file to ensure it matches the project's actual architecture and constraints found during research.

---

## Execution Strategy

### Parallel Execution Waves
Wave 1: Generate the Rule source file and the summary snippet.

---

## TODOs

- [ ] 1. Create Workspace Rule File

  **What to do**:
  - Generate `.sisyphus/docs/ANTIGRAVITY_WORKSPACE_RULES.md`.
  - Content must cover:
    - **Identity**: Global K-pop Saju/MBTI matching.
    - **Frontend**: React 19 + Vite + Tailwind v4 + Framer Motion. Emphasis on Glassmorphism and animations.
    - **Backend**: FastAPI + Python 3.11. Emphasis on `saju_engine` and daily bot automation.
    - **Infra**: Docker Compose, Nginx (Port 80/443), Certbot.
    - **Conventions**: Multi-language support (Gen-Z slang), proper error handling for external APIs (Perplexity).

  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: [`skill-protocol`]

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1

  **References**:
  - `README.md`: Tech stack and features.
  - `backend/main.py`: API structure and CORS.
  - `docker-compose.yml`: Infrastructure.

  **Acceptance Criteria**:
  - [ ] File exists at `.sisyphus/docs/ANTIGRAVITY_WORKSPACE_RULES.md`.
  - [ ] Content includes "Vibe Coding" and specific version numbers (React 19, Tailwind v4).

  **QA Scenarios**:
  ```
  Scenario: Content Accuracy Check
    Tool: Bash
    Steps:
      1. grep "React 19" .sisyphus/docs/ANTIGRAVITY_WORKSPACE_RULES.md
      2. grep "Tailwind CSS v4" .sisyphus/docs/ANTIGRAVITY_WORKSPACE_RULES.md
      3. grep "Vibe Coding" .sisyphus/docs/ANTIGRAVITY_WORKSPACE_RULES.md
    Expected Result: All keywords found, confirming accurate representation of the tech stack.
    Evidence: .sisyphus/evidence/task-1-content-check.txt
  ```

---

## Final Verification Wave

- [ ] F1. **Scope Fidelity Check** — `deep`
  Verify the rules match the discovered codebase reality (React 19, FastAPI, Docker).

---

## Success Criteria
- [ ] Antigravity Workspace Rule content is generated and presented to the user.
- [ ] Source file is stored in `.sisyphus/docs/`.
