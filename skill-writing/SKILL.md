---
name: skill-writing
description: Write, evaluate, and refine agent skills (SKILL.md files) that are concise, well-scoped, and effective. Use when creating a new skill, improving an existing skill, or reviewing skill quality. Covers frontmatter rules, progressive disclosure, workflow patterns, script bundling, and iteration.
---

# Skill Writing Best Practices

You are writing a SKILL.md that will be loaded by an AI agent. Every token competes with conversation history and other context. Your job is to give the agent exactly what it needs and nothing more.

## Guiding Principles

1. **The agent is already smart.** Only add what it would not know without this skill: project-specific conventions, domain-specific procedures, non-obvious edge cases, particular tools or APIs. If the agent would get it right without instruction, cut it.
2. **Context is a public good.** SKILL.md content loads into the agent's context window when triggered. Every line has a cost. Challenge each paragraph: "Would the agent fail here without this?"
3. **One skill, one job.** A skill should encapsulate a coherent unit of work. Skills scoped too narrowly force multiple skills to load for a single task. Skills scoped too broadly become hard to activate precisely.

## Frontmatter

Every SKILL.md MUST start with YAML frontmatter containing at minimum `name` and `description`.

### Name

- 1-64 characters, lowercase alphanumeric with single hyphen separators
- Must match the parent directory name
- Must not start/end with `-` or contain consecutive `--`
- Pattern: `^[a-z0-9]+(-[a-z0-9]+)*$`
- Use gerund form (`processing-pdfs`, `analyzing-spreadsheets`) or noun phrases (`pdf-processing`, `spreadsheet-analysis`)
- Never use vague names like `helper`, `utils`, `tools`, `documents`, `data`

### Description

- 1-1024 characters
- Write in third person ("Extracts text from PDFs" not "I can extract text" or "You can use this to extract text")
- MUST include both WHAT the skill does and WHEN to use it
- Include specific trigger terms so the agent can discover it from 100+ skills

```
# Good — specific, includes trigger context
description: Extracts text and tables from PDF files, fills forms, merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

# Bad — vague
description: Helps with documents
```

### Optional Fields

- `license`: License name or reference to a bundled license file
- `compatibility`: Environment requirements (system packages, network access)
- `metadata`: Arbitrary key-value map for additional metadata
- `disable-model-invocation`: Set `true` to only activate via explicit slash command

## File Structure

```
skill-name/
├── SKILL.md              # Core instructions (loaded when triggered)
├── references/           # Detailed docs loaded on demand
│   ├── advanced.md
│   └── examples.md
├── scripts/              # Executable utilities
│   ├── validate.py
│   └── generate.sh
└── assets/               # Static resources (templates, images, data)
    └── report-template.md
```

### Progressive Disclosure

SKILL.md is the entry point. It should:
- Contain core instructions the agent needs on EVERY run
- Link to reference files for details the agent needs SOMETIMES
- Keep the body under 500 lines and ~5,000 tokens

Tell the agent WHEN to load each file:

```markdown
# Good — conditional trigger
Read references/api-errors.md if the API returns a non-200 status code.

# Bad — generic
See references/ for details.
```

Keep references ONE LEVEL DEEP from SKILL.md. Never chain: `SKILL.md → advanced.md → details.md`. The agent may only partially read deeply nested files.

For reference files over 100 lines, include a table of contents at the top so the agent can scan scope before committing to a full read.

## Writing the Content

### Omit What the Agent Knows

```markdown
# Bad — explains what a PDF is (150 tokens)
PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library...

# Good — jumps to what the agent wouldn't know (50 tokens)
Use pdfplumber for text extraction. For scanned documents, fall back to
pdf2image with pytesseract.
```

### Use Consistent Terminology

Pick one term per concept and use it throughout. Do not mix "API endpoint", "URL", "API route", and "path" interchangeably.

### Provide Defaults, Not Menus

```markdown
# Bad — too many options
You can use pypdf, or pdfplumber, or PyMuPDF, or pdf2image...

# Good — default with escape hatch
Use pdfplumber for text extraction. For scanned PDFs requiring OCR,
use pdf2image with pytesseract instead.
```

### Favor Procedures Over Declarations

```markdown
# Specific answer — only useful for this exact task
Join the orders table to customers on customer_id, filter where
region = 'EMEA', and sum the amount column.

# Reusable method — works for any analytical query
1. Read the schema from references/schema.yaml to find relevant tables
2. Join tables using the _id foreign key convention
3. Apply any filters from the user's request as WHERE clauses
4. Aggregate numeric columns and format as a markdown table
```

### Include Gotchas

The highest-value content in many skills. List environment-specific facts that defy reasonable assumptions — concrete corrections to mistakes the agent WILL make without being told:

```markdown
## Gotchas
- The users table uses soft deletes. Always include WHERE deleted_at IS NULL.
- The user ID is user_id in the database, uid in the auth service, and
  accountId in the billing API. All three refer to the same value.
- The /health endpoint returns 200 even if the database is down. Use /ready.
```

Keep gotchas in SKILL.md, not in a reference file. The agent needs to see them before encountering the situation.

### Avoid Time-Sensitive Information

Use versioned sections instead of date-relative phrasing:

```markdown
# Good
## Current method
Use the v2 API endpoint: api.example.com/v2/messages

## Legacy
<details><summary>v1 API (deprecated)</summary>
Use api.example.com/v1/messages — no longer supported.
</details>

# Bad
If you're doing this before August 2025, use the old API.
```

## Calibrating Control

Match the specificity of instructions to the fragility of the task.

**High freedom** — Multiple approaches valid, decisions depend on context:
```markdown
## Code review process
1. Analyze the code structure and organization
2. Check for potential bugs or edge cases
3. Suggest improvements for readability
4. Verify adherence to project conventions
```

**Low freedom** — Operations are fragile, exact sequence required:
```markdown
## Database migration
Run exactly this script:
python scripts/migrate.py --verify --backup
Do not modify the command or add additional flags.
```

Most skills mix both. Calibrate each section independently.

## Workflow Patterns

See [references/patterns.md](references/patterns.md) for detailed examples of each pattern.

### Checklist Pattern

For multi-step tasks with dependencies or validation gates, provide an explicit checklist:

```markdown
## Workflow
Progress:
- [ ] Step 1: Analyze input (run scripts/analyze.py)
- [ ] Step 2: Create mapping (edit fields.json)
- [ ] Step 3: Validate (run scripts/validate.py)
- [ ] Step 4: Execute (run scripts/execute.py)
- [ ] Step 5: Verify output (run scripts/verify.py)
```

### Validation Loop Pattern

Always validate before proceeding:

```markdown
## Editing workflow
1. Make edits
2. Validate: python scripts/validate.py output/
3. If validation fails: review error, fix, re-validate
4. Only proceed when validation passes
```

### Plan-Validate-Execute Pattern

For batch or destructive operations, create an intermediate plan, validate it, then execute:

```markdown
1. Analyze input → create plan file
2. Validate plan against source of truth
3. If validation fails → revise plan, re-validate
4. Execute only after validation passes
```

Make validation scripts verbose: "Field 'signature_date' not found. Available: customer_name, order_total, signature_date_signed"

### Conditional Workflow Pattern

Guide through decision points:

```markdown
1. Determine modification type:
   Creating new content? → Follow "Creation workflow"
   Editing existing content? → Follow "Editing workflow"
```

## Bundling Scripts

Pre-made scripts are more reliable than generated code, save tokens, and ensure consistency.

### When to Bundle a Script

If the agent reinvents the same logic across multiple runs (parsing a format, validating output, generating charts), write a tested script once and bundle it.

### Script Rules

- Scripts MUST be self-contained with helpful error messages
- Handle errors explicitly rather than failing and leaving the agent to debug
- Justify all configuration values — no magic numbers
- Always use forward slashes in paths (`scripts/helper.py`), never backslashes
- List required packages in SKILL.md and verify they are available
- Make execution intent clear: "Run scripts/analyze.py" (execute) vs "See scripts/analyze.py" (read as reference)

### Error Handling

```python
# Good — handles errors, provides alternative
def process_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {path} not found, creating default")
        with open(path, "w") as f:
            f.write("")
        return ""

# Bad — punts to the agent
def process_file(path):
    return open(path).read()
```

## Output Format Templates

When the agent must produce specific output, provide a concrete template rather than describing the format in prose. Agents pattern-match well against structures:

````markdown
## Report structure

ALWAYS use this exact template:

```markdown
# [Analysis Title]

## Executive summary
[One-paragraph overview]

## Key findings
- Finding 1 with supporting data
- Finding 2 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
```
````

For flexible output, provide a sensible default and say "adapt sections as needed."

## Input/Output Examples

For skills where output quality depends on seeing examples, provide concrete input/output pairs:

```markdown
## Commit message format

**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication

**Example 2:**
Input: Fixed bug where dates displayed incorrectly in reports
Output: fix(reports): correct date formatting in timezone conversion
```

Examples teach style and detail level more clearly than descriptions alone.

## Testing and Iteration

### Evaluation-Driven Development

1. Identify gaps: run the agent on representative tasks WITHOUT the skill. Document failures
2. Create at least 3 evaluations that test these gaps
3. Establish baseline: measure performance without the skill
4. Write minimal instructions to address the gaps
5. Execute evaluations, compare against baseline, refine

### Iterate Using Dual-Agent Pattern

- **Agent A** (creator): helps design and refine the skill
- **Agent B** (consumer): uses the skill to perform real tasks
- Observe Agent B's behavior, bring insights back to Agent A

What to observe:
- Does the agent read files in an unexpected order? Structure may need rethinking
- Does it miss references to important files? Links may need to be more prominent
- Does it repeatedly read the same file? Consider moving that content to SKILL.md
- Does it never access a bundled file? It may be unnecessary
- Does it forget a rule in certain contexts? Make it more prominent or restructure

### Refine from Real Execution

Run the skill against real tasks. Feed ALL results (not just failures) back into refinement. Ask: what triggered false positives? What was missed? What could be cut?

Read execution traces, not just final outputs. If the agent wastes time on unproductive steps, common causes are:
- Instructions too vague (agent tries several approaches)
- Instructions that don't apply to the current task (agent follows them anyway)
- Too many options presented without a clear default

## Anti-Patterns

- **Explaining common knowledge** — The agent knows what PDFs are, how HTTP works, what a database migration does
- **Presenting equal options** — Pick a default, mention alternatives briefly
- **Deep nesting** — References should be one level from SKILL.md
- **Windows-style paths** — Always use forward slashes
- **Time-sensitive phrasing** — Use versioned sections, not date-relative statements
- **Vague descriptions** — "Helps with documents" vs "Extracts text from PDF files"
- **First/second person descriptions** — Always third person
- **Swiss-army-knife skills** — One skill should do one thing well
- **Encyclopedic content** — Comprehensive coverage hurts more than concise guidance
- **Assuming packages are installed** — List and verify dependencies

## Quick Reference Checklist

Before finalizing a skill, verify:

**Frontmatter**
- [ ] `name` is kebab-case, 1-64 chars, matches directory name
- [ ] `description` is third-person, includes WHAT and WHEN, specific trigger terms
- [ ] No unknown frontmatter fields

**Content**
- [ ] SKILL.md body under 500 lines / ~5,000 tokens
- [ ] Every paragraph passes "would the agent fail without this?" test
- [ ] Terminology is consistent throughout
- [ ] Gotchas are in SKILL.md, not buried in reference files
- [ ] No time-sensitive information
- [ ] Defaults provided where multiple approaches exist

**Structure**
- [ ] References are one level deep from SKILL.md
- [ ] Each reference file has conditional loading instructions
- [ ] Files over 100 lines have a table of contents
- [ ] All paths use forward slashes

**Scripts** (if applicable)
- [ ] Error handling is explicit, not punted to agent
- [ ] Configuration values are justified
- [ ] Dependencies are listed and verified
- [ ] Execution intent is clear (run vs read)

**Testing**
- [ ] At least 3 evaluations created
- [ ] Tested with real usage scenarios
- [ ] Agent execution traces reviewed
