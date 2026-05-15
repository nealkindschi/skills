# ATS Optimization Report

**Prepared for:** [Candidate Name]
**Job Posting:** [Job Title] at [Company]
**Analysis Date:** [Date]

---

## Executive Summary

[2-3 sentence overview of the candidate's ATS readiness for this specific role.
Highlight the estimated ATS match score with the clear disclaimer that this is
an estimate based on published research, not an actual ATS score. Summarize the
top 1-2 critical issues and top 1-2 strengths.]

**Estimated ATS Match Score:** [XX.X%]
*This score is an estimate based on published ATS research (TF-IDF, cosine similarity, and
weighted dimension models). Actual ATS scores vary by vendor, proprietary algorithms, and
the employer's specific configuration. Use this as a directional signal, not a prediction.*

Score Breakdown:
- Skill Match (40% weight): [XX.X% raw → XX.X contribution]
- Experience (30% weight): [XX.X% raw → XX.X contribution]
- Education (20% weight): [XX.X% raw → XX.X contribution]
- Format (10% weight): [XX.X% raw → XX.X contribution]

---

## 1. Format Audit

**Status:** [PASS / NEEDS ATTENTION — description]

List each format issue found with:
- Severity (Critical / High / Medium / Info)
- The specific issue detected
- Why this matters to ATS parsers (cite specific vendor behaviors where relevant
  — e.g., "Oracle Taleo's linear parser merges two-column content into scrambled text")
- The recommended fix with concrete instructions

If no issues found: "No format issues detected. The resume appears to follow
ATS-friendly formatting conventions."

---

## 2. Section Structure Analysis

**Standard sections found:** [list]
**Critical sections missing:** [list]
**Risky/creative headings detected:** [list if any]

For each missing section, explain:
- Which ATS database fields it maps to
- What data is invisible to the parser without it
- The exact standard heading to use

For any creative headings, explain the mapping failure risk (e.g., "'Career Journey'
will not be recognized by iCIMS's section-recognition engine as equivalent to
'Work Experience'. All keywords in this section will be invisible to the algorithm.")

---

## 3. Keyword Gap Analysis

**Overall keyword match:** [XX.X%] — [XX] of [XX] job keywords found in resume.

**Exact matches (strengths):** [list top matches]

**Critical missing keywords:**
For each, include:
- The keyword and how many times it appears in the job posting
- Why it matters (TF-IDF weighting, likely Required criterion, etc.)
- Suggested context for inclusion in the resume

**Missing skills:** [list any skills from job posting not found in resume]

---

## 4. Knockout Risk Assessment

**Knockout risks detected:** [X total — X critical, X high, X medium]

For each risk:
- The type (minimum experience, degree requirement, work authorization, etc.)
- The exact requirement detected in the job posting
- Why this is a knockout risk (explain auto-disqualification logic — e.g., "In platforms
  like Oracle Taleo, this maps to a 'Required' criterion. If unmet, the candidate is
  automatically routed to a rejected status pool without human review.")
- What the resume must demonstrate to clear this gate

If no knockout risks detected: "No knockout risks detected in the job posting."

---

## 5. Experience and Education Alignment

**Experience:**
- Years parsed from resume: [X] (or "Could not determine")
- Minimum required by job: [X years] (or "Not specified")
- Alignment: [PASS / GAP — explanation]

**Education:**
- Highest degree parsed: [X] (or "Could not determine")
- Minimum required by job: [X] (or "Not specified")
- Alignment: [PASS / GAP — explanation]

If the parser could not determine experience years or education level, explain:
- How ATS parsers extract dates (they look for YYYY-YYYY or YYYY-Present on separate
  lines in reverse-chronological order)
- How ATS parsers extract education (degree name, institution, and year in proximity
  under the "Education" section header)

---

## 6. Prioritized Recommendations

Rank ALL recommendations by impact on ATS pass-through rate. Most critical first.
For each recommendation, include:

1. **What to change** (concrete, specific instruction)
2. **Why it matters** (reference the ATS mechanic — vendor, scoring dimension, or knockout logic)
3. **How to implement** (exact text, placement guidance, formatting specification)

**Priority 1 — Critical (likely to cause auto-rejection or catastrophic score reduction)**
- [List]

**Priority 2 — High (significantly depresses match score)**
- [List]

**Priority 3 — Medium (improves ranking within surviving candidates)**
- [List]

**Priority 4 — Low (minor optimizations for edge cases)**
- [List]

---

*This analysis is based on the Applicant Tracking System Report and published
research on ATS parsing, scoring, and filtering mechanics. Recommendations are
designed to maximize the probability of passing automated screening and reaching
human review. No outcome is guaranteed.*
