# Draft: Project Rules & Guidelines for Anti-Gravity

## Requirements (confirmed)
- Goal: Create a guidance document (Gemini-style rules) in Markdown format for the "Anti-Gravity" environment.
- Context: Tailored to `k-star-destiny` project (Saju/MBTI matching).
- Content: Must cover core logic, file roles, development, deployment, and backup.

## Technical Decisions
- Format: Markdown (`.md`) compatible with AI IDE rules (e.g., `.cursorrules`).
- Tech Stack: React 19 (Vite), Tailwind v4, FastAPI (Python 3.11), Docker.
- Language: Dual-language support (KO/EN) for the rules themselves if needed, but primarily English for technical guidelines.

## Research Findings
- Core Logic: `saju_engine.py` (logic), `ai_search.py` (Perplexity integration), `main.py` (FastAPI).
- Automation: `APScheduler` in backend for daily data updates and `git_sync` for data persistence.
- Infrastructure: Docker-compose with Nginx gateway and Certbot SSL.
- Design: "Vibe Coding" philosophy (aesthetics, Gen-Z slang, Framer Motion).

## Open Questions
- Is there a specific file name preferred for Anti-Gravity? (Defaulting to `ANTI_GRAVITY_RULES.md`)
- Should I include specific UAT testing scenarios in the rules? (I'll add a section for this).

- Goal: Create a guidance document (Gemini-style rules) in Markdown format.
- Context: Tailored to the current project folder (`k-star-destiny`).
- Target Tool: "Anti-Gravity" (needs clarification).

## Technical Decisions
- Format: Markdown (`.md`).
- Content Strategy: Based on codebase patterns, tech stack, and deployment workflows.

## Research Findings
- Project Name: `k-star-destiny`.
- Issue: Permission errors encountered when accessing `deploy/certbot/` files.
- Pending: Background task `bg_f6d87bce` is exploring core logic and structure.

## Open Questions
- What is "Anti-Gravity"? Is it a specific IDE extension (like Cursor), or a custom internal tool?
- Does it require a specific filename (e.g., `.cursorrules`, `.windsurfrules`, `README.md`)?
- Are there specific coding standards (e.g., Airbnb, Google) or internal conventions already in use?

## Scope Boundaries
- INCLUDE: Coding standards, file structure conventions, deployment steps, backup procedures.
- EXCLUDE: Implementation of the logic itself (Prometheus only plans).
