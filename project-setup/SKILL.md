---
name: project-setup
description: Initializes new projects by generating foundational context files (PRD.md, ARCHITECTURE.md, UI_UX.md, STATE.md, BRAINSTORM.md) through a 4-phase interview. Use when the user says "setup project," "initialize project," "bootstrap project," "create context files," "start a new project," or when starting work in a project that lacks these files.
---

# Project Setup

Conduct a 4-phase interview to extract the user's intent, scope, aesthetics, and architecture, then generate the five foundational context files that keep coding agents aligned and deterministic.

## Workflow

```
Progress:
- [ ] Phase 0: Check for existing files
- [ ] Phase 1: Intent — core problem and value proposition
- [ ] Phase 2: Scope — user persona, MVP, explicit exclusions
- [ ] Phase 3: Aesthetics — visual constraints and design system
- [ ] Phase 4: Architecture — technology stack, dependencies, deployment
- [ ] Phase 5: Generate all files and set initial STATE
- [ ] Phase 6: Handoff to brainstorming
```

## Critical Rules

- Ask ONE question at a time. Never combine multiple questions.
- Prefer multiple-choice questions when possible, but open-ended is fine.
- Do NOT generate any code during this process. This skill creates documentation files only.
- Do NOT invoke brainstorming, writing-plans, or any implementation skill until Phase 6 handoff.
- Do NOT suggest technologies or make assumptions the user hasn't stated.
- Challenge scope creep: enforce YAGNI ruthlessly in Phase 2.

## Phase 0: Check for Existing Files

Before starting the interview, check the project root for existing files:
- PRD.md, ARCHITECTURE.md, UI_UX.md (or design.md), STATE.md (or MEMORY.md), BRAINSTORM.md

If any exist, ask: "I found existing [file names]. Should I skip those, overwrite them, or merge your new answers into them?"

Do not skip this check. Overwriting without asking destroys prior work.

## Phase 1: Intent — Core Problem and Value Proposition

Ask: "What is the fundamental problem this software solves, or what is its primary utility? In one or two sentences, what does it do?"

Analyze the response:
- Is it an actionable goal, or a vague aspiration? If vague, ask for a concrete restatement.
- Does it describe what the software IS, not just an industry or domain? Push for specifics.
- Extract the core value proposition — this becomes the top of PRD.md.

Do not move on until you have a crisp, specific statement.

## Phase 2: Scope — User Persona, MVP, and Explicit Exclusions

**User persona:** Ask: "Who is the primary end-user? Examples: technical developers needing dense data displays, casual consumers wanting mobile-first simplicity, enterprise administrators requiring accessibility compliance?"

**Enforce YAGNI:** Ask: "What is the absolute Minimum Viable Product — the single core feature that validates this product? We'll defer everything else to future milestones."

If the user describes a sprawling feature set (multiple subsystems, real-time features, complex billing, analytics), flag it immediately: "That sounds like multiple independent systems. Which single feature represents the core MVP?"

**Explicit exclusions:** Ask: "What features are explicitly out of scope for the MVP? This prevents the agent from building unrequested functionality."

Document all exclusions in PRD.md.

## Phase 3: Aesthetics — Visual Constraints and Design System

Ask about design preferences in a structured way. Offer multiple choice where helpful:

"Tell me about the visual direction. I'll ask about a few dimensions — you can be brief or detailed on each."

1. **Color palette**: "Do you have a color preference? Options: dark mode (grays/blacks with accent colors), light/minimalist (whites with muted accents), high-contrast/accessibility-first, or a specific brand palette (provide hex values if you have them)."

2. **Typography**: "Any font preferences? Options: system font stack (zero dependencies), monospace-forward (developer tool feel), or a specific font family?"

3. **Information density**: "Should the UI feel spacious with fewer elements visible at once, or dense and data-rich (like a dashboard or IDE)?"

4. **Component library** (if applicable): "Any preference for UI primitives? Options: raw CSS, Tailwind CSS, or a headless component library (Radix, Headless UI)?"

Document all answers in UI_UX.md.

## Phase 4: Architecture — Technology Stack and Deployment

Ask for exact technologies. Demand specificity — vague answers produce broken architecture files.

"Now for the technical foundation. I'll need specific answers — 'React' isn't enough; I need 'Next.js 14 with App Router' level detail."

1. **Frontend**: "What frontend framework and version? Be specific — e.g., Next.js 14 (App Router) vs Remix vs Vite SPA."

2. **Backend** (if applicable): "What backend runtime and framework? e.g., Cloudflare Workers, Node.js + Express, Python + FastAPI, or no backend (static site)."

3. **Database** (if applicable): "What database? e.g., PostgreSQL, D1, Durable Objects, MongoDB, or no database."

4. **State management** (if applicable): "Any state management? e.g., React Context, Zustand, Redux, or none."

5. **Deployment**: "Where does this deploy? e.g., Cloudflare Pages, Vercel, Netlify, AWS, or not yet determined."

6. **Package manager**: "Which package manager? npm, pnpm, yarn, or bun?"

7. **Additional constraints**: "Any other technical constraints — monorepo tooling, required libraries, banned dependencies, CI/CD requirements?"

Document exact versions, names, and configurations in ARCHITECTURE.md. If the user says "not sure" on a dimension, mark it as TBD in the file rather than guessing.

## Phase 5: Generate Files

Once all 4 phases are complete, generate the files. Use the templates in `assets/` populated with the user's answers.

### File Generation Order

1. **PRD.md** — Populate `assets/prd-template.md` with Phase 1 and Phase 2 answers
2. **ARCHITECTURE.md** — Populate `assets/architecture-template.md` with Phase 4 answers
3. **UI_UX.md** — Populate `assets/ui-ux-template.md` with Phase 3 answers
4. **STATE.md** — Populate `assets/state-template.md` with initial milestone
5. **BRAINSTORM.md** — Write a minimal scratchpad file

### STATE.md Initial Content

The STATE.md must be initialized with:

```
## Current Active Milestone
Milestone 0: Repository architecture initialized. Awaiting Phase One design specifications via the brainstorming skill.

## Completed Objectives
- Project context files generated (PRD.md, ARCHITECTURE.md, UI_UX.md, STATE.md, BRAINSTORM.md)

## Known Bugs and Technical Debt
None — project not yet implemented.

## Immediate Next Steps
1. Invoke brainstorming to design the first feature from PRD.md
```

### Existing Files

If the user chose to skip or merge in Phase 0, honor that decision. If merging, incorporate new answers into the existing file structure rather than replacing wholesale.

### Write BRAINSTORM.md

Create a minimal scratchpad:

```
# Brainstorm

Exploratory scratchpad for feature ideation, architectural trade-offs, and design thinking. Content here is provisional — conclusions are formalized into PRD.md and ARCHITECTURE.md before implementation.
```

## Phase 6: Handoff

After all files are written, print this message:

> "Project context files created:
> - `PRD.md` — product requirements and scope
> - `ARCHITECTURE.md` — technology stack and constraints
> - `UI_UX.md` — design system and visual rules
> - `STATE.md` — project memory and progress tracking
> - `BRAINSTORM.md` — ideation scratchpad
>
> **Next step**: Invoke the brainstorming skill to design the first feature from PRD.md."

Do NOT automatically invoke brainstorming. The user decides when to proceed.

## Gotchas

- **Empty project detection**: If the project directory is completely empty (no files at all), skip Phase 0's existing-file check and proceed directly to Phase 1.
- **Partial file sets**: If only some files exist (e.g., PRD.md exists but ARCHITECTURE.md doesn't), only ask about the existing ones. Generate the missing ones without asking about them.
- **User says "not sure"**: Mark as TBD in the generated file. Never invent or assume answers.
- **Multi-project confusion**: If the working directory doesn't look like a project root (e.g., home directory, Desktop), ask: "This doesn't look like a project directory. Where should I create the files?"
- **Scope creep during interview**: If the user adds features mid-interview that contradict earlier YAGNI decisions, flag it: "That feature wasn't in the MVP we defined. Should I add it to the exclusion list, or update the MVP scope?"
- **ARCHITECTURE.md without a tech decision**: If the user can't decide on a technology, don't stall the interview. Mark it TBD with context: "TBD: user evaluating options between X and Y."
- **The agent must NOT start building after this skill completes**: The handoff explicitly directs to brainstorming. If the user says "now build it," remind them: "Let's brainstorm the first feature first to get the design right."
