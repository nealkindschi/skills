# ATS Vendor Profiles — Parsing Behavior Reference

Reference for explaining WHY specific resume formatting and keyword choices matter.
Load this file when the analysis output references vendor-specific behavior that
needs additional context for the candidate's recommendations.

---

## Oracle Taleo Enterprise

**Typical users:** Fortune 500, large enterprises, government agencies.

**Parsing behavior:**
- Older, rigid linear parser. Scans left-to-right, top-to-bottom.
- Relies on strict pattern matching for section recognition (hunts for date range +
  degree title + institution name as a triple to identify "Education").
- Two-column layouts are merged horizontally, scrambling job titles with dates from
  adjacent columns, destroying the semantic link between tenure and responsibilities.
- Non-standard section headings cause the parser to fail to categorize content,
  effectively hiding those keywords from scoring.

**Scoring / filtering:**
- Uses a centralized "Library" of prescreening questions. Recruiters assign
  "Required" (auto-disqualify) and "Asset" (weighted ranking) criteria per requisition.
- "ACE" candidate flagging: candidates who pass Required criteria AND accumulate high
  Asset criteria are flagged with a star icon for prioritized recruiter review.
- Administrators can configure percentage thresholds on Asset criteria to trigger
  automated follow-up emails.

**Recommendation focus:** Absolute structural compliance. Single-column, standard
headings (`Work Experience`, `Education`, `Skills`). Embed exact keyword phrases
from the job posting — Taleo's TF-IDF scoring rewards verbatim matches.

---

## Workday Recruiting

**Typical users:** Mid-to-large enterprises with integrated HCM needs.

**Parsing behavior:**
- Integrated into end-to-end workforce planning (HCM). Resume data flows through
  configured "business process stages" (e.g., State Talent Acquisition Review, Screen, Assessment).
- Uses skills intelligence for AI-powered matching — identifies exact AND adjacent
  capabilities, potentially expanding the qualified pool beyond verbatim keyword matches.
- Supports blind resume screening (strips name and demographic info during initial review).

**Scoring / filtering:**
- Recruiters use the Recruiter Hub to sort candidates by parsed skill criteria columns.
- Batch processing: recruiters can select multiple candidates simultaneously to advance
  them through workflow stages.
- Structured interview scorecards for uniform evaluation.

**Recommendation focus:** While Workday's AI matching is more forgiving than Taleo's,
explicit keyword inclusion still matters for initial filtering columns. Focus on
skills intelligence — list related/adjacent skills alongside core ones.

---

## iCIMS Talent Cloud

**Typical users:** Mid-to-large organizations across industries.

**Parsing behavior:**
- Translates ALL documents into raw plain text profiles for algorithmic evaluation.
- Maintains a visual copy for recruiters, but scoring is 100% on the raw parsed data.
- Heavy reliance on section-recognition engines — if a heading doesn't map, all
  keywords in that section are invisible to the algorithm.
- "Role Fit" ranking operates strictly per-job, evaluating extracted experiences
  against requisition parameters.

**Scoring / filtering:**
- Groups candidates into strategic tiers based on clustered scores.
- Recruiters are directed to the highest-ranking tier first.
- Actively expanding AI capabilities through acquisitions.

**Recommendation focus:** Standard typography and conventional section headings are
non-negotiable. Every section must use a recognizable header. Keywords in
unrecognized sections are lost. Plain-text, single-column format.

---

## Greenhouse

**Typical users:** Tech companies, startups, mid-size organizations.

**Parsing behavior:**
- "AI-first" assistive intelligence approach — designed to augment human judgment,
  not replace it.
- Deep OpenAI integration for features like AI-generated scorecard summaries, keyword
  suggestions, and talent matching.
- Resume anonymization during Application Review (scans for names, gender, race,
  marital status, contact info, social media links). Currently optimized only for
  Latin characters.

**Scoring / filtering:**
- Talent Matching: compares resumes against recruiter-defined weighted calibrations.
- Interview Scorecards: AI synthesizes human feedback, highlights consensus/disagreement.
- AI-powered Keyword Suggestions: analyzes job post to generate optimal filter criteria.

**Recommendation focus:** Structure matters less here than with Taleo/iCIMS, but
weighted calibrations rely on keyword presence. Focus on quantified achievements
and specific outcomes — the AI scorecard synthesis looks for concrete evidence.

---

## SAP SuccessFactors

**Typical users:** Global enterprises, especially those already in the SAP ecosystem.

**Parsing behavior:**
- Cloud-based HCM suite with configurable knockout questions and dynamic candidate sorting.
- Core strength: extensive third-party AI integrations (Sniper AI for ranking,
  Phenom for chatbots, Paradox AI for conversational screening).
- Parsing behavior depends heavily on which integrated tools the employer has activated.

**Scoring / filtering:**
- Sniper AI: quick-learns from recruiter feedback to automate screening.
- Third-party integrations may deploy their own scoring models on top of SuccessFactors.
- Paradox AI: conversational AI asks knockout questions via SMS/chat, auto-advances
  qualifying candidates with full audit trails.

**Recommendation focus:** Prepare for both NLP parsing AND conversational AI screening.
Knockout questions may arrive via chat. Resume should still follow standard ATS formatting
for the base SuccessFactors parser, but keywords must also survive conversational filtering.

---

## Eightfold AI (Talent Intelligence)

**Typical users:** Enterprises adopting deep learning-based hiring; U.S. federal agencies
(FedRAMP Moderate authorized).

**Parsing behavior:**
- "Talent Intelligence Platform" — goes beyond keyword filtering to predictive modeling.
- Assesses long-term potential and skills adjacencies, not just past experience.
- Predicts what a candidate could learn/accomplish within a year if developed.
- Deploys "Equal Opportunity Algorithms" to mask demographic traits and ensure
  recommendations are based on capability and learning potential.

**Scoring / filtering:**
- Proprietary Match Score model: evaluates trajectory, not just history.
- Uses deep learning across the entire profile — work history, qualifications,
  unstructured experience — mapped to a shared vector space with the job description.

**Recommendation focus:** Detail matters more than exact keywords. Bullet points should
describe specific outcomes, quantified achievements, and methodologies. The embedding
model maps conceptual relevance — "data modeling + Python scripting + predictive
analytics" will map to "Machine Learning Engineer" even without that exact phrase.
Focus on showing the trajectory of increasing responsibility and skill depth.
