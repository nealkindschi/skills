---
name: ai-security-data
description: Enriches AI security articles and content by inserting verified data points, statistics, case studies, and anecdotes from the AI Security Report Data Gathering research report. Use when writing or editing content about AI cybersecurity, AI threat landscape, AI vulnerabilities, AI governance, adversarial AI, or AI compliance. Triggered by phrases like "enrich with data," "add statistics," "back this up," "insert research," "add evidence," or when the user provides draft content needing data-backed claims in the AI security domain.
---

# AI Security Data Enrichment

Take draft AI security content and insert relevant, verified data from the research report at `references/report.md`. The report covers the 2026 AI security landscape: market economics, breach costs, adversary tactics, vulnerability statistics, regulatory frameworks, workforce trends, and defensive AI.

## Data Index

Scan the report using grep to find relevant data by domain. The report is organized into these sections:

| Section | Data available | Grep anchor |
|---------|---------------|-------------|
| Macroeconomic context | AI spending ($2.5T), market growth (26.9%), adoption rates (53%) | `1. Macroeconomic` |
| Financial impact of breaches | Breach costs ($4.88M), Shadow AI premium (+$670K), containment savings ($2.22M) | `2. The Financial` |
| Adversarial threat vectors | Polymorphic malware, APT tool usage, exploit velocity (5 days) | `3. The Adversarial` |
| Mexican government breach | 195M taxpayer IDs, Claude Code + GPT-4.1 exploitation walkthrough | `4. The Mexican` → actually section 3 sub-section; "Mexican Government"  |
| Vulnerability statistics | 2,130 AI CVEs (+34.6%), component breakdown, hallucination rates (22%-94%) | `4. The Exploitation` or `5. Agentic` |
| MITRE ATLAS agentic threats | PleaseFix attacks, SesameOp, credential harvesting, clickbait | `5. Agentic` or `MITRE ATLAS` |
| Supply chain & AIBOM | 45% AI code has vulns, 65% orgs hit by supply chain attack, data poisoning | `6. Open Source` |
| Enterprise readiness | Confidence Gap, Shadow AI (59%), workforce stats, ISACA poll | `7. Evaluating Enterprise` |
| Risk modeling & regulation | FAIR-AIR, NIST AI RMF, EU AI Act penalties (€35M/7%) | `8. Quantitative Risk` |
| Defensive AI | Claude Security, GPT-5.5-Cyber, JailbreakBench, HMNS attack | `9. Offensive Defense` |

**Works cited**: The final section of the report contains source URLs. Every data point in the report traces to a numbered citation.

## Workflow

Copy this checklist and track progress:

```
Enrichment Progress:
- [ ] Step 1: Read the target content
- [ ] Step 2: Identify data opportunities
- [ ] Step 3: Extract matching data from the report
- [ ] Step 4: Verify every data point against the report
- [ ] Step 5: Insert data gracefully into the content
- [ ] Step 6: Add source citations
- [ ] Step 7: Final review
```

### Step 1: Read the target content

Read the full article or content the user provides. Identify:
- What claims are made that could benefit from supporting data
- What sections lack evidence or specificity
- What topics overlap with the report's domains

### Step 2: Identify data opportunities

For each section of the target content, note where data from the report could strengthen it. Favor opportunities where:

- A claim is made but unsupported ("AI breaches are expensive" → add the $4.88M figure)
- A trend is mentioned without scale ("adoption is growing fast" → add 53% in 3 years stat)
- A threat is described abstractly ("attackers use AI for phishing" → add specific APT technique)
- A solution is proposed without evidence ("governance frameworks help" → add FAIR-AIR or NIST RMF data)
- A gap exists where a case study would bring the point to life (Mexican government breach)

Limit to 1-2 data insertions per ~300 words. Over-stuffing weakens impact.

### Step 3: Extract matching data from the report

Use grep or read `references/report.md` to find exact data matching the opportunity. Use the Data Index above to target the right section.

### Step 4: Verify every data point against the report

**This is the most critical step.** For each data point you plan to insert:

1. Locate the exact sentence in the report where the data appears
2. Confirm the number, statistic, year, or detail matches exactly
3. Confirm the citation number in the report
4. If the data point cannot be traced to a specific report sentence, discard it

Never round numbers, paraphrase statistics into different numbers, or combine data points from different sources in the report into a single claim.

### Step 5: Insert data gracefully

Integrate data into the existing narrative. Do not create standalone "Data Box" sections.

**Good** (flows with the text):
> The financial stakes are staggering. According to IBM, the global average cost of a data breach held at $4.88 million in 2025, and organizations grappling with ungoverned Shadow AI saw that figure swell by an additional $670,000 per incident.

**Bad** (bolted on):
> **Key Statistics:**
> - Average breach cost: $4.88M
> - Shadow AI adds $670K to breach costs

Match the tone, voice, and sentence structure of the surrounding content. Use the report's source attribution style (e.g., "according to IBM," "the World Economic Forum found," "Stanford's AI Index reports").

### Step 6: Add source citations

For every inserted data point, include a citation. The report uses numbered references (1-62). Use this format:

> According to IBM, the global average cost of a data breach held at $4.88 million in 2025.¹¹

If the target content uses a different citation style (e.g., hyperlinks, parenthetical), match that style using the source URLs from the Works Cited section.

### Step 7: Final review

- [ ] Every inserted data point matches the report verbatim
- [ ] Every data point has a source citation
- [ ] Insertions flow naturally within the surrounding text
- [ ] No section has more than 2 data insertions
- [ ] No data point was fabricated, rounded, or combined

## Quality Rules

- **Verification is mandatory.** Never insert a statistic without confirming it exists in the report.
- **Prefer specificity.** "2,130 AI-related CVEs were disclosed in 2025 alone, a 34.6% year-over-year increase" beats "AI vulnerabilities are growing rapidly."
- **Case studies over numbers when available.** The Mexican government breach narrative (Section 3) carries more weight than raw statistics alone.
- **Attribute every data point.** Use the source attribution found in the report (IBM, WEF, Stanford HAI, Trend Micro, etc.).
- **Don't fabricate sources.** If the report cites "IBM" for a stat, cite IBM. Do not substitute a different source name.
- **Respect the content's voice.** Do not change the author's tone, style, or formatting conventions.

## Gotchas

- The report uses numbered citations (¹, ² through ⁶²). These correspond to the Works Cited list at the end. Do not renumber them.
- Section numbering in the report's Table of Contents may not match the actual content headings exactly — always grep for the phrase, not the section number.
- The Mexican government breach is a subsection of Section 3 ("The Adversarial Arsenal"), not its own top-level section.
- Market figures use both billions and millions — $2.5 trillion vs $38.2 billion vs $670,000. Double-check units before inserting.
- Some statistics appear in the report text and the data table — both are valid sources. The table on lines 9-17 consolidates key economic indicators.
- Hallucination epistemology data (Section 4, lines 79-80) is nuanced — GPT-4o drops from 98.2% to 64.4% accuracy under belief framing. Do not oversimplify this as "AI models are 64% accurate."
- The report's data is from 2026 reporting. When inserting into content about a different year, acknowledge the temporal context ("as of 2026," "in 2025 data," etc.).
