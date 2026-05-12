---
name: information-gain
description: Use when writing or editing web content that must rank in search engines and be cited by AI Overviews and LLMs. Teaches extraction of novel data points, first-hand evidence, original frameworks, and expert attribution from source documents to maximize information gain scores. Triggered by "add information gain," "enrich with data," "optimize for AI visibility," "make this rank in 2026," or when content needs to outperform existing top-10 results.
---

# Information Gain Content Enrichment

## Overview

Information gain (IG) is the dominant ranking signal in 2026. It measures how much *new* information a document contributes beyond what already exists in the search index and what the user has seen in their session. Paraphrase content—summarizing the top 10 without adding original data—earns zero IG and loses 60-80% visibility. Content with original data, evidence, frameworks, and expert attribution gains 15-25% visibility and earns AI Overview citations (35% more organic clicks).

This skill teaches extracting high-signal data points from source materials and inserting them into web content to maximize IG scoring across traditional SERPs and LLM/RAG systems.

## When to Use

- Writing new web content intended to rank
- Enriching a draft article with data and evidence
- Optimizing existing content for AI Overview citations
- Responding to a ranking drop after a core update
- User says: "add information gain," "enrich with data," "make this rank," "optimize for AI," "add evidence," "insert research"

## Core Workflow

1. **Extract** data points from source documents — classify by IG dimension
2. **Insert** data points into content with attribution and context
3. **Optimize** structure for AI/LLM extractability
4. **Validate** with scorecard — minimum 7/9

### Phase 1: Extract Data Points

Read every provided source document. Produce an **extraction manifest** — a flat list of extractable data points, each tagged with its IG dimension:

| Dimension | Extract |
|---|---|
| Proprietary Data | Statistics, survey results, original datasets, benchmarks, internal data |
| First-hand Evidence | Screenshots, transcripts, tool outputs, experimental results, before/after metrics |
| Original Framework | Named methodologies, checklists, scoring rubrics, matrices, models |
| Expert Attribution | Named authors with verifiable credentials, direct quotes, institutional sources |
| Freshness Hook | Dated events (2025-2026), specific data cuts, news triggers, regulatory changes |

**Extraction rules:**
- Pull exact numbers: "61% CTR decline" not "most clicks lost"
- Preserve context: sample size (n=), methodology, collection date
- Flag every named author, organization, or institution
- Note every date — freshness decays, prioritize 2025-2026
- Capture counterintuitive findings — these have highest IG per Shannon's entropy framework

**Worked example** — from a patent analysis source document:

| Data Point | IG Dimension |
|---|---|
| "March 2026 core update: peak volatility 8.7/10, surpassing August 2024" | Freshness Hook, Proprietary Data |
| "InfoGain-RAG outperforms naive RAG by 17.9% on NaturalQA benchmark" | Proprietary Data |
| "AI Overview citations: 35% more organic clicks, 91% more paid clicks" | Proprietary Data |
| "5-dimension scoring rubric (2-2-2-2-1)" by Digital Applied | Original Framework, Expert Attribution |
| "Generic AI content farms: -60% to -80% visibility" | Proprietary Data |

### Phase 2: Insert Data Points Into Content

**Placement rules:**
- Lead with the strongest statistic in the introduction or first 150 words
- Each H2 section must contain at least one original data point
- Place proprietary data and frameworks above the fold (first ~300 words)
- Distribute data across sections — never cluster all data in one place
- Position counterintuitive findings early (high surprise = high IG)

**Attribution format:**
Every data point gets attribution. Format: `[Source], [Date]`. Example: "According to Seer Interactive's February 2026 analysis, AIO-cited brands see 35% more organic clicks."

Bad: "Studies show..." or "Research indicates..." — earns 0 on Expert Attribution.

**Integration patterns:**
- Statistics with multiple comparisons → table
- Named methodology or framework → H2 or H3 heading
- Screenshot/tool output → "Key Finding" callout or blockquote
- Expert quote → attributed pull quote with credential line
- Survey result → inline with sample size: "In a survey of 500 practitioners (n=500)..."

### Phase 3: Optimize for AI/LLM Visibility

**For AI Overview citations:**
- Write 1-2 standalone sentences per section summarizing the novel insight — these are extractable snippets
- Place the highest-IG claim in the first 150 words
- Use schema: `Article` (always), `Dataset` (for proprietary data), `FAQ` (for Q&A), `HowTo` (for step-by-step frameworks)

**For RAG/LLM retrieval:**
- Clear heading hierarchy: H1 → H2 → H3, never skip a level
- Self-contained sections that parse independently
- Data in tables where possible — LLMs extract tables efficiently
- Precise, unique language — avoid generic phrases that match the top-10 consensus

**Extractable snippet rule — each H2 should contain one sentence that:**
1. Stands alone as a complete claim
2. Contains a specific number, date, or named entity
3. Can be quoted by an AI Overview without surrounding context

Example: "The March 2026 core update penalized AI-generated paraphrase content with visibility drops of 60-80%."

## 5-Dimension Information Gain Rubric

Score content against these dimensions. Target: **7+/9**.

| Dimension | 2 points | 1 point | 0 points |
|---|---|---|---|
| Proprietary Data | Internally generated dataset or original survey | Novel analysis of existing third-party data | No original data |
| First-hand Evidence | Screenshots, transcripts, tool outputs | Paraphrased anecdote | No evidence |
| Original Framework | Named new methodology, checklist, or matrix | Modified existing framework | No framework |
| Expert Attribution | Named author with verifiable public track record | Named author without public credentials | Generic byline or anonymous |
| Freshness Hook | Content tied to 2025-2026 event or data cut | Year mentioned but no specific date | Timeless or undated |

For edge cases and expanded examples, read `references/rubric-details.md`.

## Common Mistakes

- **Paraphrase trap**: Summarizing the existing top-10 without adding original data. The LLM already knows this — zero IG.
- **Buried evidence**: Placing unique data in the last section or appendix. AI Overviews sample from page top.
- **Unattributed statistics**: "Studies show," "Research indicates" — forfeits Expert Attribution points.
- **Missing schema**: Proprietary data with no `Dataset` schema is invisible to structured-data-aware RAG systems.
- **Data dumping**: Statistics without "so what" context. Every data point needs a reader-facing implication.
- **No freshness hook**: Even evergreen content benefits from a recent development, data release, or regulatory trigger.

## Gotchas

- IG is session-based in the patent. Content that repeats the consensus top-10 earns zero even if well-written — it provides nothing new relative to what the user has already seen.
- AI Overview citations are NOT the same as organic positions. Cited-but-not-#1 beats #1-but-not-cited.
- The Helpful Content System is a primary signal now, not a secondary filter.
- LLM context windows are limited. High information density (unique facts per token) wins citations, not comprehensiveness or length.
- A 500-word post with one original citable statistic can outrank a 4,000-word guide that re-packages existing knowledge.

## Validation

After writing or enriching content, fill out `assets/scorecard-template.md`. Each dimension must cite specific evidence from the finished content. Do NOT skip this step.

Target: **7+/9**.
