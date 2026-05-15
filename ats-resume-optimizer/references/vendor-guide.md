# ATS Vendor Profiles

Detailed profiles of major enterprise ATS platforms. Load this file when a vendor is identified from the job posting page.

---

## Oracle Taleo

**Detection**: URLs containing `taleo.net`, Oracle branding on application page.

**Profile**: Dominant among Fortune 500 companies. Operates on a highly structured, hierarchical candidate evaluation methodology. Parsing technology is older and extremely rigid.

**Parser Behavior**:
- Scans for highly specific linguistic patterns aligned to distinct document sections
- For education: hunts for a date range, degree title, and university name
- Particularly vulnerable to formatting anomalies — two-column resumes, non-standard layouts cause catastrophic failure

**Scoring Features**:
- Centralized "Library" of prescreening and disqualification questions
- Required vs. Asset criteria system with "ACE star" visual identifier for high-Asset candidates
- Administrators can trigger automated emails when candidates meet percentage thresholds of Asset criteria
- Custom advanced candidate search form with customized requisition statuses and sorting fields
- Integrates with Partner Services for third-party Screening Services

**Optimization Strategy**:
1. Strict single-column, reverse-chronological layout — non-negotiable
2. Use only standard section headings ("Work Experience", "Education", "Skills")
3. Map JD "preferred" and "nice to have" terms to Asset criteria — explicit inclusion triggers ACE categorization
4. Standard fonts only (Arial, Calibri, Times New Roman)
5. Plain ASCII bullets only

---

## Workday Recruiting

**Detection**: URLs containing `myworkdayjobs.com`, Workday branding.

**Profile**: Differentiates itself with a continuous pipeline model integrated into broader enterprise workforce planning and HCM ecosystems. Replaces isolated applicant databases.

**Parser Behavior**:
- Recruiters manage applicant flow via Recruiter Hub and Candidate Job Applications interface
- Candidates evaluated through strict business process stages (State Talent Acquisition Review, Screen, Assessment)
- Batch processing: recruiters select multiple applicants simultaneously to move them through workflow
- Supports blind resume screening: strips candidate names and demographic info during initial review

**Ai Features**:
- Skills intelligence that identifies exact and adjacent capabilities
- Expands qualified talent pool by matching related skills, not just exact terms

**Optimization Strategy**:
1. Include adjacent and related skills alongside exact JD terms — Workday's skills cloud rewards breadth
2. Structured bullet points with clear outcome statements matter because of Interview Scorecards
3. Blind screening means focus on skills content, not demographic framing
4. Standard single-column layout still critical — Workday's parser also struggles with multi-column

---

## iCIMS Talent Cloud

**Detection**: URLs containing `icims.com`, iCIMS copyright.

**Profile**: Heavily relies on text-based keyword extraction, density analysis, and section-recognition engines. Translates all uploaded documents into raw plain text profiles regardless of visual formatting.

**Parser Behavior**:
- Algorithmic evaluation is entirely dependent on raw parsed data (the visual render is for recruiter viewing only)
- Strict section-recognition engine — failure to map a heading means subsequent keywords are lost
- Constructs a per-job "Role Fit" ranking
- Groups candidates into strategic tiers based on clustered scores

**Optimization Strategy**:
1. Absolute compliance with standard typography and plain-text layouts
2. Conventional section headings are non-negotiable — the section-recognition engine is unforgiving
3. Keyword density matters heavily — repeat high-value terms across multiple sections
4. Favor exact term repetition over synonyms
5. Avoid any graphical elements, tables, or headers/footers — they actively hide content from the parser

---

## Greenhouse

**Detection**: URLs containing `greenhouse.io`, Greenhouse branding.

**Profile**: AI-first methodology aimed at assistive intelligence rather than autonomous black-box decision-making. Deep integrations with OpenAI.

**Ai Features**:
- Interview Scorecards: dynamically generated attributes based on job title and description
- AI synthesizes human feedback, highlighting areas of consensus, disagreement, and key candidate quotes
- Talent Matching (Plus and Pro tiers): compares profiles against recruiter-defined weighted calibrations
- AI-powered Keyword Suggestions: analyzes job post and generates optimal filtering criteria
- Resume Anonymization: conceals names, gender identifiers, racial markers, marital status, contact info, social media links (currently optimized only for Latin characters)

**Optimization Strategy**:
1. Mirror JD language precisely — Greenhouse's Keyword Suggestions feature generates filters directly from the JD
2. Bullet points should be detailed and outcome-oriented (feeds interview scorecards)
3. Weighted calibrations mean recruiters can prioritize specific JD criteria — hit the first 3-5 listed requirements hard
4. Anonymization means skill content is the only differentiator — ensure all skills are spelled out fully, not just acronyms

---

## SAP SuccessFactors

**Detection**: URLs containing `successfactors.com`, SAP branding.

**Profile**: Massive cloud-based HCM suite. Core strength lies in extensive third-party AI integrations.

**Parser Behavior**:
- Knockout questions and dynamic candidate display options configurable by recruiters
- Frequently integrates with specialized third-party platforms:
  - **Sniper AI**: Algorithm-based ranking that quick-learns from recruiter feedback
  - **Phenom**: Chatbots for sourcing, screening, and answering candidate FAQs before ATS logic engages
  - **Paradox AI**: Conversational AI for knockout questions via SMS/chat; auto-advances candidates who pass

**Optimization Strategy**:
1. Prepare for multi-layered screening — chatbot knockout questions may precede ATS parsing
2. Conservative document formatting — SAP's core parser is similar to Taleo in rigidity
3. Contact information clarity matters — Paradox AI may send SMS confirmations
4. Standard ATS formatting rules apply: single-column, standard headings, ASCII bullets

---

## Eightfold AI

**Detection**: URLs containing `eightfold.ai`, Talent Intelligence Platform branding.

**Profile**: "Talent Intelligence Platform" — fundamentally reframes ATS from filtering mechanism to long-term potential assessment. Uses deep learning to assess skills adjacencies and predict trajectory.

**Ai Features**:
- Predictive modeling infers candidate's trajectory — predicts what they could learn and accomplish
- Bespoke Match Score model goes beyond what applicant has achieved
- "Equal Opportunity Algorithms" mathematically ensure recommendations based solely on capability and learning potential
- FedRAMP Moderate Authorized for U.S. federal agency deployment
- Uses neural embeddings — recognizes transferable skills without exact keyword matches

**Optimization Strategy**:
1. Quantified outcomes and methodologies matter more than exact keyword repetition
2. Describe the scope, scale, and impact of achievements — these feed the embedding model
3. Include adjacent skills and learning trajectory indicators (courses, side projects, self-directed learning)
4. Synonyms are recognized — "data modeling" maps to "machine learning" in the shared vector space
5. Career progression narrative matters — show growth and expanding responsibility

---

## Vendor Not Found — General Strategy

Apply the general deterministic scoring framework from the report:

- Weight distribution: Skill Match 40%, Experience Level 30%, Education Relevance 20%, Format and Clarity 10%
- Skill-match ratio: matched skills / total JD skills
- Verbatim vocabulary alignment is heavily rewarded
- TF-IDF and cosine similarity are the default matching mechanisms
- High-value keywords should appear multiple times across the document
- Single-column, standard fonts, ASCII bullets, and conventional headings are universally required
