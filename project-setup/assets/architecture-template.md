# Architecture

## Primary Frameworks and Languages

### Frontend
- Framework: [e.g., Next.js 14 (App Router), Remix, Vite + React, Astro]
- Language: [e.g., TypeScript, JavaScript]
- Runtime: [e.g., Node.js 20, Bun, Edge]

### Backend
- Framework: [e.g., Cloudflare Workers, Hono, Express, FastAPI — or "None (static site)"]
- Language: [e.g., TypeScript, Python, Go]
- Runtime: [e.g., Node.js, Bun, Cloudflare Workers, Python 3.12]

### Database
- Primary: [e.g., PostgreSQL 16, Cloudflare D1, SQLite (Turso), MongoDB, Durable Objects — or "None"]
- ORM / Query Builder: [e.g., Drizzle ORM, Prisma, Knex, None]

## Dependency Management

- Package manager: [npm, pnpm, yarn, bun]
- Lock file policy: [Lock files committed to repository]
- Versioning: [Exact versions preferred, no caret ranges]
- Banned dependencies: [List any packages, patterns, or versions explicitly prohibited]

## State Management

- Strategy: [e.g., React Context, Zustand, Redux Toolkit, URL search params, None]

## Data Models

[Core entities, their fields, types, and relationships.]

### [Entity Name]
- `id`: [type] — [description]
- `[field]`: [type] — [description]
- Relations: [e.g., belongs to User, has many Items]

## API Design

- Protocol: [REST, GraphQL, tRPC, WebSocket — or "None (static)"]
- Authentication: [e.g., JWT, session cookies, OAuth 2.0, Clerk, None]
- Authorization: [e.g., RBAC, per-resource policies, None]

## Infrastructure and Deployment

- Hosting: [e.g., Cloudflare Pages, Vercel, Netlify, AWS, self-hosted]
- CI/CD: [e.g., GitHub Actions, Cloudflare Pages Git integration, None yet]
- Environment variables: [List required secrets/config with descriptions — no values]
- Domains / URLs: [TBD or specified]

## Testing

- Framework: [e.g., Vitest, Jest, pytest, None yet]
- E2E: [e.g., Playwright, Cypress, None yet]
- Coverage target: [e.g., 80%, TBD]

## Architectural Constraints

- [Constraint 1: e.g., zero runtime JavaScript where possible]
- [Constraint 2: e.g., all data fetching at build time]
- [Constraint 3: e.g., no server-side state between requests]
