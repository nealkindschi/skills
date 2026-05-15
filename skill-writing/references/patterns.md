# Skill Patterns and Examples

Detailed examples of structural patterns for skill content.

## Pattern 1: High-Level Guide with References

Best for skills with multiple feature areas where only one area is typically needed per invocation.

````markdown
---
name: pdf-processing
description: Extracts text and tables from PDF files, fills forms, and merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---

# PDF Processing

## Quick start

Extract text with pdfplumber:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Advanced features

**Form filling**: See [references/forms.md](references/forms.md) for complete guide
**API reference**: See [reference/api.md](reference/api.md) for all methods
**Examples**: See [references/examples.md](references/examples.md) for common patterns
````

## Pattern 2: Domain-Specific Organization

Best when content naturally splits by domain and the agent only needs one domain per task.

```text
bigquery-skill/
├── SKILL.md (overview and navigation)
└── references/
    ├── finance.md (revenue, billing metrics)
    ├── sales.md (opportunities, pipeline)
    └── product.md (API usage, features)
```

````markdown
# BigQuery Data Analysis

## Available datasets

**Finance**: Revenue, ARR, billing → See [references/finance.md](references/finance.md)
**Sales**: Opportunities, pipeline, accounts → See [references/sales.md](references/sales.md)
**Product**: API usage, features, adoption → See [references/product.md](references/product.md)

## Quick search

Find specific metrics using grep:

```bash
grep -i "revenue" references/finance.md
grep -i "pipeline" references/sales.md
```
````

## Pattern 3: Conditional Details

Show basic content inline, link to advanced content with clear conditions.

```markdown
# DOCX Processing

## Creating documents

Use docx-js for new documents. See [references/docx-js.md](references/docx-js.md).

## Editing documents

For simple edits, modify the XML directly.

**For tracked changes**: See [references/redlining.md](references/redlining.md)
**For OOXML details**: See [references/ooxml.md](references/ooxml.md)
```

## Pattern 4: Generator Pattern

Skills that create new artifacts from templates or specifications.

```markdown
# API Documentation Generator

You generate API documentation from OpenAPI specifications.

## Process
1. Read the specification from user input
2. Load template from assets/api-doc-template.md
3. Apply transformations based on endpoint type
4. Output formatted result

## Templates Available
- assets/api-doc-template.md — REST endpoints
- assets/websocket-template.md — WebSocket events
- assets/graphql-template.md — GraphQL schemas
```

## Pattern 5: Integrator Pattern

Skills that connect multiple systems or data sources.

```markdown
# Multi-Source Analytics

Combine data from BigQuery, Mixpanel, and Salesforce into unified reports.

## Process
1. Read query parameters from user request
2. Fetch BigQuery data using references/bigquery-queries.md patterns
3. Enrich with Mixpanel events using references/mixpanel-api.md
4. Cross-reference Salesforce accounts using references/salesforce.md
5. Merge and deduplicate using scripts/merge.py
6. Output formatted report using assets/report-template.md
```

## Pattern 6: Converter Pattern

Skills that transform content from one format to another.

```markdown
# Markdown to Confluence

Convert markdown documentation to Confluence-compatible HTML.

## Conversion rules
1. Map headers to Confluence macros
2. Convert code blocks to code-panel macros
3. Transform internal links to Confluence page references
4. Handle admonitions using info/tip/warning panels

## Edge cases
- Tables with merged cells: See references/tables.md
- Embedded diagrams: See references/diagrams.md
```

## Checklist Pattern (Detailed)

For complex multi-step tasks with validation gates.

````markdown
## PDF form filling workflow

Copy this checklist and check off items as you complete them:

```
Task Progress:
- [ ] Step 1: Analyze the form (run scripts/analyze_form.py)
- [ ] Step 2: Create field mapping (edit fields.json)
- [ ] Step 3: Validate mapping (run scripts/validate_fields.py)
- [ ] Step 4: Fill the form (run scripts/fill_form.py)
- [ ] Step 5: Verify output (run scripts/verify_output.py)
```

**Step 1: Analyze the form**

Run: `python scripts/analyze_form.py input.pdf`

This extracts form fields and their locations, saving to `fields.json`.

**Step 2: Create field mapping**

Edit `fields.json` to add values for each field.

**Step 3: Validate mapping**

Run: `python scripts/validate_fields.py fields.json`

Fix any validation errors before continuing.

**Step 4: Fill the form**

Run: `python scripts/fill_form.py input.pdf fields.json output.pdf`

**Step 5: Verify output**

Run: `python scripts/verify_output.py output.pdf`

If verification fails, return to Step 2.
````

## Plan-Validate-Execute Pattern (Detailed)

For batch operations or destructive changes.

````markdown
## Batch PDF form filling

1. Extract form fields: `python scripts/analyze_form.py input.pdf` → `form_fields.json`
   (lists every field name, type, and whether it's required)

2. Create `field_values.json` mapping each field name to its intended value

3. Validate: `python scripts/validate_fields.py form_fields.json field_values.json`
   (checks that every field name exists in the form, types are compatible,
   and required fields aren't missing)

4. If validation fails, revise `field_values.json` and re-validate

5. Fill the form: `python scripts/fill_form.py input.pdf field_values.json output.pdf`

Do NOT skip step 3. Validation catches:
- References to non-existent fields
- Type mismatches (text in number fields)
- Missing required fields
````

## Research Synthesis Workflow (Non-Code)

````markdown
## Research synthesis workflow

Copy this checklist and track your progress:

```
Research Progress:
- [ ] Step 1: Read all source documents
- [ ] Step 2: Identify key themes
- [ ] Step 3: Cross-reference claims
- [ ] Step 4: Create structured summary
- [ ] Step 5: Verify citations
```

**Step 1: Read all source documents**

Review each document. Note main arguments and supporting evidence.

**Step 2: Identify key themes**

Look for patterns across sources. Where do sources agree or disagree?

**Step 3: Cross-reference claims**

For each major claim, verify it appears in the source material.

**Step 4: Create structured summary**

Organize findings by theme. Include:
- Main claim
- Supporting evidence from sources
- Conflicting viewpoints (if any)

**Step 5: Verify citations**

Check that every claim references the correct source. If incomplete, return to Step 3.
````

## Style Guide Compliance Loop (Non-Code)

```markdown
## Content review process

1. Draft content following guidelines in references/style-guide.md
2. Review against checklist:
   - Terminology consistency
   - Examples follow standard format
   - All required sections present
3. If issues found:
   - Note each issue with specific section reference
   - Revise the content
   - Review checklist again
4. Only proceed when all requirements are met
```
