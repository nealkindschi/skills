# Compliance and Algorithmic Bias

Legal and regulatory frameworks governing automated hiring. Load when the role is in a regulated industry, government, or when the user asks about bias/legal considerations.

---

## US: EEOC and the Four-Fifths Rule

The Equal Employment Opportunity Commission mandates that hiring algorithms comply with federal anti-discrimination frameworks.

### The Four-Fifths Rule (80% Rule)

```
Adverse impact exists when: Selection rate for a protected group < 80% of the highest group's selection rate
```

**Example**: If an ATS advances 50% of male applicants, it must advance at least 40% of female applicants. If female pass-through drops to 30%, adverse impact is flagged.

**What this means for the candidate**: ATS platforms run continuous selection-rate checks. When disparities are detected, HR teams recalibrate weighted calibrations and algorithm limits. This can lead to sudden changes in which keywords or criteria are prioritized — a system that previously filtered aggressively on "5+ years" might relax that threshold if it creates adverse impact.

### NYC Local Law 144

New York City requires employers using Automated Employment Decision Tools (AEDTs) to:
- Subject their software to independent, third-party bias audits
- Publicly publish audit results
- Explicitly notify candidates that an algorithm is evaluating their application

**Implication**: NYC-based companies or roles may use vendors with published audit results. This transparency can help identify which scoring dimensions carry the most weight.

### OFCCP and Federal Contractors

Federal contractors must maintain affirmative action programs. Their ATS configurations often include:
- Mandatory self-identification forms (gender, race, veteran status, disability) — these are separated from the evaluation pipeline
- Audit trails showing that demographic data was not used in screening

---

## EU: AI Act and GDPR

The EU AI Act categorizes recruitment AI as "high-risk" with strict boundaries:

**Prohibited Practices**:
- Emotion recognition during video screening interviews
- AI that predicts "social scoring" from applicant behavior
- Systems inferring race, gender, political affiliation, or other sensitive traits from biometric data
- Subliminal or manipulative AI techniques

**GDPR Rights for Candidates**:
- Right to meaningful information about the logic involved in automated decisions
- Right to human intervention and to contest automated decisions
- Right to data portability and erasure

---

## Disability and Accessibility

Rigid parsing algorithms can disproportionately exclude candidates with disabilities:
- Non-traditional career trajectories (gaps for medical reasons) may depress chronological scoring
- Chronological scoring disadvantages those with employment gaps
- Image-based resumes (sometimes used by candidates with visual impairments using screen readers) fail entirely
- Document accessibility features may conflict with ATS parsing requirements

---

## Algorithmic Bias: How It Manifests

| Bias Type | Mechanism | Impact |
|---|---|---|
| Historical Bias | Training data reflects decades of biased hiring patterns | AI internalizes and replicates demographic preferences |
| Representation Bias | Certain demographics underrepresented in training data | Model performs poorly on underrepresented groups |
| Measurement Bias | Features chosen for evaluation correlate with demographic traits | Names associated with certain ethnicities may trigger different scoring patterns |
| Aggregation Bias | Single model applied to all demographics | Model optimized for majority group performs worse on minority groups |

---

## Mitigation Strategies (How Vendors Respond)

**Degendering Resumes**: Training models on synthetically altered datasets where gendered pronouns, demographic-identifying affiliations, and name markers are scrubbed or equalized across the semantic vector space. Forces machine learning weightings to prioritize technical capabilities.

**AI Explainability**: Vendors transition away from black-box algorithms toward systems that provide clear, transparent explanations for scores and rankings, including:
- Specific skill gaps identified
- Confidence metrics for predictions
- Audit trails for each scoring decision

**Blind Screening**: Programmatic stripping of names, demographic info, and identifying markers during initial review phases (used by Workday, Greenhouse).

---

## Candidate Implications

- **Do not include**: Photo, age, marital status, religion, political affiliation, social media links, or demographic self-identifiers. These can trigger unintended bias filters or cause the parser to misclassify content.
- **Do include**: Right-to-work status if it's a knockout requirement. Missing this = instant rejection with zero human review.
- **Use universal names**: If the resume format includes a header with only a name, ensure it uses standard Latin characters — some anonymization tools may fail on non-Latin scripts.
