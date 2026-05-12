# 5-Dimension Information Gain Rubric — Detailed Reference

Read this when you need to resolve edge cases in scoring or need concrete examples for each tier.

## 1. Proprietary Data (0-2 points)

**What counts:** Numeric data that does not exist in Google's index at publication time.

### Score 2 — Internally Generated Dataset
- Results from a survey you conducted with disclosed methodology and sample size
- Internal company data (customer behavior, platform metrics, A/B test results)
- Original benchmark data you produced by running tests
- Example: "We analyzed 10,000 support tickets and found 43% originate from mobile devices"
- Example: "In a survey of 200 compliance officers (n=200), 68% reported using AI for audit"

### Score 1 — Novel Analysis of Third-Party Data
- A new statistical analysis of publicly available data that reveals a pattern no one else has published
- Cross-referencing two existing datasets to produce a novel correlation
- Data visualization that surfaces an insight not visible in the raw source
- Example: "Cross-referencing FDA recalls with SEC filings reveals a 6-month lag between safety signals and disclosure impact"

### Score 0 — No Original Data
- Re-stating statistics from other published articles
- Paraphrasing industry reports without adding new analysis
- "According to Gartner..." without adding your own computation or insight on top

### Edge Cases
- Public government data re-analyzed with a novel methodology → Score 2 if methodology is named and new
- Competitor data scraped and aggregated → Score 1 (third-party, novel analysis)
- A screenshot of your own analytics dashboard → This goes to First-hand Evidence (Dimension 2), not Proprietary Data. It qualifies for both.

---

## 2. First-hand Evidence (0-2 points)

**What counts:** Verifiable proof that the claimed process or result actually happened.

### Score 2 — Screenshots, Transcripts, Tool Outputs
- Screenshots of software interfaces showing real results
- Transcripts of interviews or conversations
- Raw tool output (terminal logs, API responses, test results)
- Photos of physical processes or before/after comparisons
- Example: Screenshot of Google Search Console showing ranking changes
- Example: Terminal output of a benchmark command with timestamps

### Score 1 — Paraphrased Anecdote
- Describing a case study in your own words without showing the raw data
- "One client saw a 40% increase..." without a screenshot or named source
- Acceptable only as supplementary, not as primary evidence

### Score 0 — No Evidence
- Claims without any backing
- "Many companies have seen success with this approach"
- Abstract descriptions with no concrete anchor

### Edge Cases
- Video embedded in the page → Score 2 if it shows the actual process/result
- Anonymized screenshot (company name redacted) → Score 1 (reduced verifiability)
- A diagram you created illustrating a concept → This goes to Original Framework (Dimension 3), not First-hand Evidence

---

## 3. Original Framework (0-2 points)

**What counts:** A specifically named, novel methodology or mental model introduced by the content.

### Score 2 — Named New Methodology
- A framework with a distinct name you coined (e.g., "The CASKET Model," "4-D Audit Matrix")
- A step-by-step process or checklist that doesn't exist elsewhere
- A scoring rubric or decision tree you designed
- Example: "We developed the TRUST framework: Transparency, Reproducibility, Urgency, Specificity, Timeliness"
- Example: "The Information Density Score (IDS) = unique facts / total word count"

### Score 1 — Modified Existing Framework
- Adding a dimension to an existing model (e.g., "I extended the 4 Ps of marketing with a 5th: Purpose")
- Adapting a framework from one domain to another with credited source
- Re-ordering or re-prioritizing an existing methodology with justification

### Score 0 — No Framework
- Presenting information without any organizing structure
- Using someone else's framework without modification or credit

### Edge Cases
- A mnemonic that reorganizes existing knowledge → Score 1 unless the reorganization reveals new insight
- A checklist derived from regulatory requirements → Score 0 (not original to you) unless you added original items and named it
- A diagram that maps relationships between concepts → Score 1-2 depending on whether the mapping is novel

---

## 4. Expert Attribution (0-2 points)

**What counts:** Named individuals with verifiable credentials who created or endorsed the content.

### Score 2 — Named Author with Verifiable Track Record
- Author has a public LinkedIn profile showing relevant expertise
- Author has published papers, spoken at conferences, or holds certifications in the domain
- Content includes author bio with specific credential claims (not "industry expert")
- Example: "By Dr. Sarah Chen, PhD in Information Retrieval, author of 12 papers on search algorithms"
- Example: Byline links to author page showing publication history

### Score 1 — Named Author Without Public Credentials
- Author name is present but no bio, no linked profile, no credential claims
- "By John Smith" with no further information
- Acceptable as a floor but insufficient for competitive queries

### Score 0 — Generic Bylines
- "By Our Editorial Team"
- "Staff Writer"
- No author attribution at all
- AI-generated content presented as human-authored

### Edge Cases
- Multiple authors with varying credentials → Score based on lead author, mention co-authors
- Guest post by a practitioner without academic credentials → Score 2 if they have a verifiable company role and track record in the domain
- Interview format where the expert is quoted but doesn't author → Score 2 for the expert quoted, but author attribution must also be present

---

## 5. Freshness Hook (0-1 point)

**What counts:** A specific, recent temporal anchor that makes the content current.

### Score 1 — Tied to 2025-2026 Event or Data Cut
- References a specific core update, conference, regulation, or news event with date
- Contains data specifically collected or cut within the current or previous year
- "As of Q1 2026, the data shows..."
- Example: "Following the March 2026 core update, ranking volatility hit 8.7/10"

### Score 0 — Timeless or Undated
- No temporal reference at all
- "Here's how to do SEO" with no date context
- Content could have been written in 2019
- Year in title but no specific data cut: "SEO Guide 2026" without a single dated data point

### Edge Cases
- Historical analysis of a past event → Score 1 if framed with current implications (e.g., "What the 2024 update teaches us about the 2026 landscape")
- Annual update of a piece → Score 1 if at least one new data point is added with a current date
- Timeless content with a "Last updated" date → Score 0 unless the body contains a specific dated reference
