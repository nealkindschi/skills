#!/usr/bin/env python3
"""
ATS Resume Analyzer — extracts text from resume and job posting, then produces
a structured JSON analysis report covering format compliance, keyword matching,
section structure, knockout risks, experience/education alignment, and an
estimated ATS match score based on industry research.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Dependency management — import gracefully, flag missing packages
# ---------------------------------------------------------------------------

MISSING_DEPS = []

try:
    import requests
except ImportError:
    requests = None  # type: ignore
    MISSING_DEPS.append("requests")

try:
    import pdfplumber
except ImportError:
    pdfplumber = None  # type: ignore
    MISSING_DEPS.append("pdfplumber")

try:
    import docx
except ImportError:
    docx = None  # type: ignore
    MISSING_DEPS.append("python-docx")

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None  # type: ignore
    MISSING_DEPS.append("beautifulsoup4")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def stderr(msg: str) -> None:
    print(msg, file=sys.stderr)


def warn(missing: list[str]) -> None:
    if missing:
        stderr(f"WARNING: Missing Python packages: {', '.join(missing)}")
        stderr("Install with: pip install " + " ".join(missing))
        stderr("Some input formats may be unavailable.\n")


def is_url(path: str) -> bool:
    parsed = urlparse(path)
    return parsed.scheme in ("http", "https")


def fetch_url(url: str, timeout: int = 30) -> str | None:
    """Fetch a URL and return its text content. Returns None on failure."""
    if requests is None:
        stderr("ERROR: 'requests' package required for URL fetching. Install: pip install requests")
        return None
    try:
        resp = requests.get(url, timeout=timeout, headers={
            "User-Agent": "Mozilla/5.0 (compatible; ATS-Resume-Optimizer/1.0)"
        })
        resp.raise_for_status()
    except requests.RequestException as exc:
        stderr(f"ERROR: Failed to fetch URL '{url}': {exc}")
        return None
    content_type = resp.headers.get("Content-Type", "").lower()
    if "text/html" in content_type:
        return extract_html_text(resp.text)
    return resp.text


def extract_html_text(html: str) -> str | None:
    """Strip HTML tags and return visible text."""
    if BeautifulSoup is None:
        stderr("ERROR: 'beautifulsoup4' required for HTML parsing. Install: pip install beautifulsoup4")
        return None
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        tag.decompose()
    text = soup.get_text(separator="\n")
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return "\n".join(lines)


def extract_pdf_text(filepath: str) -> str | None:
    if pdfplumber is None:
        stderr("ERROR: 'pdfplumber' required for PDF extraction. Install: pip install pdfplumber")
        return None
    try:
        with pdfplumber.open(filepath) as pdf:
            pages = [page.extract_text() or "" for page in pdf.pages]
        return "\n".join(pages).strip()
    except Exception as exc:
        stderr(f"ERROR: Failed to extract PDF '{filepath}': {exc}")
        return None


def extract_docx_text(filepath: str) -> str | None:
    if docx is None:
        stderr("ERROR: 'python-docx' required for DOCX extraction. Install: pip install python-docx")
        return None
    try:
        document = docx.Document(filepath)
        return "\n".join(p.text for p in document.paragraphs).strip()
    except Exception as exc:
        stderr(f"ERROR: Failed to extract DOCX '{filepath}': {exc}")
        return None


def read_txt_file(filepath: str) -> str | None:
    try:
        for encoding in ("utf-8", "latin-1", "cp1252"):
            try:
                with open(filepath, "r", encoding=encoding) as f:
                    return f.read().strip()
            except UnicodeDecodeError:
                continue
        stderr(f"ERROR: Could not decode '{filepath}' with any known encoding.")
        return None
    except OSError as exc:
        stderr(f"ERROR: Failed to read '{filepath}': {exc}")
        return None


def extract_resume_text(path_or_url: str) -> str | None:
    """Route resume extraction based on whether input is a URL or local file."""
    if is_url(path_or_url):
        return fetch_url(path_or_url)
    path = Path(path_or_url)
    if not path.exists():
        stderr(f"ERROR: File not found: {path}")
        return None
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf_text(str(path))
    if suffix == ".docx":
        return extract_docx_text(str(path))
    return read_txt_file(str(path))


def extract_job_text(url: str) -> str | None:
    """Extract text from a job posting URL."""
    return fetch_url(url)


def normalize_text(text: str) -> str:
    """Collapse whitespace and normalize for comparison."""
    return re.sub(r"\s+", " ", text).strip().lower()


# ---------------------------------------------------------------------------
# Section header detection
# ---------------------------------------------------------------------------

STANDARD_SECTIONS = {
    "summary": ["summary", "professional summary", "profile", "objective", "career summary"],
    "experience": ["experience", "work experience", "professional experience",
                   "employment", "work history", "professional background", "career"],
    "education": ["education", "academic background", "academic qualifications",
                  "educational background", "academic history"],
    "skills": ["skills", "technical skills", "core competencies", "core skills",
               "key skills", "areas of expertise", "technical expertise"],
    "certifications": ["certifications", "licenses", "certifications & licenses",
                       "professional certifications", "credentials"],
    "projects": ["projects", "key projects", "relevant projects", "project experience"],
}

CREATIVE_HEADING_RISKS = [
    "career journey", "where i've been", "my story", "what i bring",
    "qualifications snapshot", "capabilities", "proficiencies",
    "academic pursuits", "scholastic record", "professional timeline",
    "career highlights", "selected achievements", "work samples",
]


def detect_sections(text: str) -> dict:
    """Detect standard and non-standard section headers in resume text."""
    lines = text.splitlines()
    headers_found = []
    creative_found = []
    sections_present: dict[str, bool] = {
        "summary": False, "experience": False, "education": False,
        "skills": False, "certifications": False, "projects": False,
    }

    for line in lines:
        stripped = line.strip().rstrip(":").lower()
        if not stripped or len(stripped) < 3 or len(stripped) > 60:
            continue
        if re.search(r"^[\d\.\s\-•]+$", stripped):
            continue

        # Check creative/risky headings
        for risk in CREATIVE_HEADING_RISKS:
            if risk in stripped:
                creative_found.append(line.strip())

        # Check standard headings
        for category, variants in STANDARD_SECTIONS.items():
            if any(v in stripped for v in variants):
                headers_found.append({"category": category, "text": line.strip()})
                sections_present[category] = True

    # Unique categories found
    found_categories = list({h["category"] for h in headers_found})
    missing = [cat for cat, present in sections_present.items() if not present]

    return {
        "standard_sections_found": found_categories,
        "standard_headers_detected": headers_found,
        "critical_missing": missing,
        "creative_risky_headings": creative_found,
        "all_critical_present": all(sections_present.values()),
    }


# ---------------------------------------------------------------------------
# Format audit (single-column, fonts, bullets, etc.)
# ---------------------------------------------------------------------------

FORMAT_RISK_PATTERNS = {
    "unicode_bullets": re.compile(r"[▶►✓✔✦✧◆◇▪▫●○◉◎⦿]" + "|" +
                                  r"[\u2022\u2023\u25E6\u2043\u2219\u25CB\u25CF\u25AA\u25AB]"),
    "multi_column": re.compile(r".{80,}\n.{80,}"),  # heuristic: long paired lines
    "excessive_formatting": re.compile(r"─|━|═|▀|▄|█|▓"),
}


def audit_format(text: str, source_path: str) -> dict:
    """Audit resume for ATS-parser-hostile formatting."""
    issues: list[dict] = []
    lines = [l for l in text.splitlines() if l.strip()]
    lower = text.lower()

    # Unicode bullet check
    unicode_matches = FORMAT_RISK_PATTERNS["unicode_bullets"].findall(text)
    if unicode_matches:
        issues.append({
            "severity": "high",
            "issue": "Non-ASCII bullet symbols detected",
            "detail": (f"Found {len(unicode_matches)} non-ASCII bullets. "
                       "Many ATS parsers (Taleo, iCIMS) fail to interpret "
                       "Unicode glyphs, breaking list-parsing arrays."),
            "fix": "Replace with standard ASCII bullets: - * o",
            "examples": unicode_matches[:8],
        })

    # Length heuristic for multi-column
    wide_lines = 0
    for line in lines:
        if len(line) > 80:
            wide_lines += 1
    if len(lines) > 10 and wide_lines / len(lines) > 0.3:
        issues.append({
            "severity": "medium",
            "issue": "Possible multi-column or wide-format layout",
            "detail": (f"{wide_lines}/{len(lines)} lines exceed 80 characters. "
                       "Some ATS parsers read left-to-right and may scramble "
                       "parallel column content."),
            "fix": "Use a single-column layout with standard margins.",
        })

    # Unconventional heading detection (delegated to detect_sections)
    # But we run a quick pass here too
    heading_issues = []
    for heading in lines:
        s = heading.strip().lower()
        if s.endswith(":") and len(s) < 60:
            # Check if it looks like a heading but is non-standard
            looks_like_heading = (s[0].isalpha() and len(s.split()) <= 6)
            is_standard = any(
                any(variant in s for variant in variants)
                for variants in STANDARD_SECTIONS.values()
            )
            if looks_like_heading and not is_standard:
                heading_issues.append(heading.strip())

    # Document format warnings
    suffix = Path(source_path).suffix.lower() if source_path and not is_url(source_path) else ""
    if suffix == ".pdf":
        issues.append({
            "severity": "info",
            "issue": "PDF format: verify text is selectable",
            "detail": "Image-based PDFs register as blank in ATS parsers. "
                      "Always export as text-selectable PDF from a word processor.",
            "fix": "If this PDF was created from a graphic design tool, re-create as a DOCX or text-selectable PDF.",
        })
    if suffix in (".pages", ".indd", ".ai", ".psd"):
        issues.append({
            "severity": "critical",
            "issue": f"Unsupported file format: {suffix}",
            "detail": "ATS platforms only accept PDF, DOCX, or TXT formats. "
                      "This file will likely be rejected outright.",
            "fix": "Export or save as DOCX or text-selectable PDF.",
        })

    return {
        "issues": issues,
        "issue_count": len(issues),
        "passes_format_audit": len([i for i in issues if i["severity"] in ("high", "critical")]) == 0,
        "risky_headings_detected": heading_issues,
    }


# ---------------------------------------------------------------------------
# Keyword extraction and matching
# ---------------------------------------------------------------------------

COMMON_NOISE_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "will", "would", "could", "should", "may", "might", "can", "shall",
    "has", "have", "had", "do", "does", "did", "this", "that", "these",
    "those", "it", "its", "we", "you", "they", "he", "she", "our", "your",
    "their", "not", "no", "if", "then", "than", "also", "very", "just",
    "about", "above", "after", "all", "any", "each", "every", "other",
    "some", "such", "only", "over", "under", "into", "through", "during",
    "before", "between", "more", "most", "much", "well", "work", "team",
    "role", "position", "looking", "seeking", "candidate", "applicant",
    "opportunity", "company", "including", "across", "within",
}


PHRASE_OCCURS_1ST = re.compile(r'"[^"]{4,80}"')   # quoted phrases (6+ chars)
PHRASE_OCCURS_2ND = re.compile(r"\b(?:[A-Z][a-z]+(?:[\s/-]+[A-Z][a-z]+){1,5})\b")
SINGLE_TERM = re.compile(r"\b([A-Za-z0-9+#.-]{3,30})\b")

# Skill-like patterns: languages, frameworks, tools
SKILL_PATTERNS = re.compile(
    r"\b("
    r"Python|Java|JavaScript|TypeScript|C\+\+|C#|Ruby|Go|Rust|Swift|Kotlin|PHP|"
    r"SQL|NoSQL|React|Angular|Vue|Node\.js|Django|Flask|Spring|Express|Rails|"
    r"AWS|Azure|GCP|Docker|Kubernetes|Terraform|Ansible|Jenkins|GitLab|GitHub|"
    r"Machine Learning|Deep Learning|NLP|Data Science|Power BI|Tableau|Excel|"
    r"Agile|Scrum|Kanban|JIRA|Confluence|REST|GraphQL|gRPC|"
    r"CI/CD|DevOps|SRE|SaaS|PaaS|IaaS|API|SDK|CLI"
    r")\b", re.IGNORECASE
)


def extract_keywords(text: str, source_name: str = "") -> dict:
    """Extract meaningful keyword phrases from job description or resume text."""
    normalized = normalize_text(text)

    # Quoted phrases
    phrases = []
    for m in PHRASE_OCCURS_1ST.finditer(text):
        phrase = m.group(0).strip('"').lower()
        if len(phrase.split()) >= 2:
            phrases.append(phrase)

    # Capitalized multi-word phrases (proper nouns, technologies)
    proper_phrases = []
    for m in PHRASE_OCCURS_2ND.finditer(text):
        phrase = m.group(0).strip().lower()
        words = phrase.split()
        if 2 <= len(words) <= 5:
            proper_phrases.append(phrase)

    # Single terms (filter noise)
    single_terms = []
    for m in SINGLE_TERM.finditer(text):
        term = m.group(0).lower()
        if term not in COMMON_NOISE_WORDS and len(term) >= 3:
            single_terms.append(term)

    # Skill matches
    skills_found = list({m.group(0).lower() for m in SKILL_PATTERNS.finditer(text)})

    term_freq = Counter(single_terms).most_common(40)
    phrase_freq = Counter(phrases + proper_phrases).most_common(20)

    return {
        "source": source_name,
        "skills_detected": sorted(skills_found),
        "top_term_keywords": [{"keyword": k, "frequency": v} for k, v in term_freq if v >= 1],
        "top_phrase_keywords": [{"keyword": k, "frequency": v} for k, v in phrase_freq if v >= 1],
        "total_unique_terms": len(set(single_terms)),
        "total_unique_phrases": len(set(phrases + proper_phrases)),
    }


def match_keywords(resume_kw: dict, job_kw: dict) -> dict:
    """Match job keywords against resume keywords and report gaps."""
    resume_terms = {t["keyword"] for t in resume_kw["top_term_keywords"]}
    job_terms = {t["keyword"] for t in job_kw["top_term_keywords"]}
    resume_phrases = {p["keyword"] for p in resume_kw["top_phrase_keywords"]}
    job_phrases = {p["keyword"] for p in job_kw["top_phrase_keywords"]}
    resume_skills = set(resume_kw["skills_detected"])
    job_skills = set(job_kw["skills_detected"])

    exact_term_matches = job_terms & resume_terms
    missing_terms = job_terms - resume_terms
    exact_phrase_matches = job_phrases & resume_phrases
    missing_phrases = job_phrases - resume_phrases
    exact_skill_matches = job_skills & resume_skills
    missing_skills = job_skills - resume_skills

    total_job_keywords = len(job_terms) + len(job_phrases) + len(job_skills)
    total_matches = len(exact_term_matches) + len(exact_phrase_matches) + len(exact_skill_matches)
    match_pct = round((total_matches / total_job_keywords * 100), 1) if total_job_keywords > 0 else 0.0

    # Flag critical missing keywords (appear multiple times in job posting)
    critical_missing = []
    for kw in job_kw["top_term_keywords"]:
        if kw["keyword"] in missing_terms and kw["frequency"] >= 3:
            critical_missing.append({
                "keyword": kw["keyword"],
                "frequency_in_job": kw["frequency"],
                "reason": "Appears multiple times in job description; heavily weighted in TF-IDF scoring.",
            })
    for kw in job_kw["top_phrase_keywords"]:
        if kw["keyword"] in missing_phrases and kw["frequency"] >= 2:
            critical_missing.append({
                "keyword": kw["keyword"],
                "frequency_in_job": kw["frequency"],
                "reason": "Appears multiple times; likely required or highly weighted term.",
            })

    return {
        "exact_term_matches": sorted(exact_term_matches),
        "missing_terms": sorted(missing_terms),
        "exact_phrase_matches": sorted(exact_phrase_matches),
        "missing_phrases": sorted(missing_phrases),
        "exact_skill_matches": sorted(exact_skill_matches),
        "missing_skills": sorted(missing_skills),
        "keyword_match_percentage": match_pct,
        "critical_missing_keywords": critical_missing,
        "total_job_keywords_extracted": total_job_keywords,
        "total_matches": total_matches,
    }


# ---------------------------------------------------------------------------
# Knockout risk assessment
# ---------------------------------------------------------------------------

KNOCKOUT_PATTERNS = [
    re.compile(r"(?:must\s+(?:have|possess|hold|be)|required(?:\s+to\s+have)?)", re.I),
    re.compile(r"(?:minimum\s+(?:of\s+)?(\d+)[+\s]*(?:years?|yrs?)\s+(?:of\s+)?(?:experience|exp)\.?)", re.I),
    re.compile(r"(?:bachelor'?s|master'?s|ph\.?d\.?|doctorate)\s+(?:degree\s+)?(?:in\s+)?[\w\s]+", re.I),
    re.compile(r"(?:authoriz(?:ed|ation)\s+to\s+work)", re.I),
    re.compile(r"(?:security\s+clearance|secret\s+clearance|top\s+secret)", re.I),
    re.compile(r"(?:certification\s+(?:in|as)|certified\s+[\w\s]+)", re.I),
    re.compile(r"(?:must\s+be\s+(?:able\s+to\s+)?(?:relocate|travel|commute))", re.I),
    re.compile(r"(?:valid\s+(?:driver'?s?\s+)?license)", re.I),
    re.compile(r"(?:U\.?S\.?\s*(?:citizen|person)|permanent\s+resident|green\s+card)", re.I),
    re.compile(r"(?:fluent\s+(?:in|written\s+and\s+spoken)\s+[\w\s]+)", re.I),
]

REQUIRED_VS_PREFERRED = {
    "required": re.compile(
        r"(?:required|must\s+have|mandatory|essential|non-negotiable|qualifications?|"
        r"minimum\s+qualifications?|what\s+you'?ll?\s+bring|you\s+will\s+need|"
        r"basic\s+qualifications?|core\s+requirements?)", re.I
    ),
    "preferred": re.compile(
        r"(?:preferred|nice\s+to\s+have|bonus|desired|asset|plus|advantage|"
        r"it'?s?\s+a\s+plus|would\s+be\s+(?:a\s+)?plus|additional\s+qualifications?)", re.I
    ),
}


def assess_knockout_risks(job_text: str, resume_text: str) -> dict:
    """Identify knockout-question-equivalent requirements in the job posting."""
    risks = []
    resume_lower = resume_text.lower()
    job_lower = job_text.lower()

    # Years of experience
    for m in KNOCKOUT_PATTERNS[1].finditer(job_text):
        years = int(m.group(1))
        context = job_text[max(0, m.start() - 60):m.end() + 60].strip()
        risks.append({
            "type": "minimum_experience",
            "value": f"{years}+ years",
            "match_text": m.group(0),
            "context": context,
            "severity": "critical",
        })

    # Degree requirements
    for m in KNOCKOUT_PATTERNS[2].finditer(job_text):
        context = job_text[max(0, m.start() - 40):m.end() + 80].strip()
        risks.append({
            "type": "degree_requirement",
            "value": m.group(0),
            "context": context,
            "severity": "high",
        })

    # Work authorization
    for m in KNOCKOUT_PATTERNS[3].finditer(job_text):
        risks.append({
            "type": "work_authorization",
            "value": m.group(0),
            "severity": "critical",
        })

    # Security clearance
    for m in KNOCKOUT_PATTERNS[4].finditer(job_text):
        risks.append({
            "type": "security_clearance",
            "value": m.group(0),
            "severity": "critical",
        })

    # Certifications
    for m in KNOCKOUT_PATTERNS[5].finditer(job_text):
        risks.append({
            "type": "certification_requirement",
            "value": m.group(0),
            "severity": "high",
        })

    # Relocation/travel
    for m in KNOCKOUT_PATTERNS[6].finditer(job_text):
        risks.append({
            "type": "relocation_or_travel",
            "value": m.group(0),
            "severity": "medium",
        })

    # Citizenship
    for m in KNOCKOUT_PATTERNS[8].finditer(job_text):
        risks.append({
            "type": "citizenship_requirement",
            "value": m.group(0),
            "severity": "critical",
        })

    # Language fluency
    for m in KNOCKOUT_PATTERNS[9].finditer(job_text):
        risks.append({
            "type": "language_fluency",
            "value": m.group(0),
            "severity": "medium",
        })

    # Classify required vs preferred sections
    required_keywords = set()
    preferred_keywords = set()
    req_section = REQUIRED_VS_PREFERRED["required"].split(job_text)
    pref_section = REQUIRED_VS_PREFERRED["preferred"].split(job_text)

    return {
        "knockout_risks_detected": risks,
        "total_risks": len(risks),
        "critical_risks": len([r for r in risks if r["severity"] == "critical"]),
        "high_risks": len([r for r in risks if r["severity"] == "high"]),
        "note": ("These represent potential auto-disqualification triggers. "
                 "The resume should explicitly address each item. "
                 "In platforms like Oracle Taleo, these map to 'Required' "
                 "criteria that trigger immediate rejection if unmet."),
    }


# ---------------------------------------------------------------------------
# Experience & Education alignment
# ---------------------------------------------------------------------------

def extract_years_experience(text: str) -> int | None:
    """Heuristically extract total years of experience from resume text."""
    patterns = [
        re.compile(r"(\d+)[+\s]*(?:years?|yrs?)\s+(?:of\s+)?(?:total\s+)?(?:professional\s+)?(?:work\s+)?(?:relevant\s+)?experience", re.I),
        re.compile(r"(?:over|more\s+than|above)\s+(\d+)[+\s]*(?:years?|yrs?)", re.I),
    ]
    for pat in patterns:
        m = pat.search(text)
        if m:
            return int(m.group(1))
    # Fallback: count date ranges
    date_ranges = re.findall(r"(\d{4})\s*[-–—to]+\s*(\d{4}|present|current|now)", text, re.I)
    if date_ranges:
        years = 0
        for start, end in date_ranges:
            end_year = 2026 if end.lower() in ("present", "current", "now") else int(end)
            years += max(0, end_year - int(start))
        return years
    return None


def extract_highest_degree(text: str) -> str | None:
    """Extract highest education level from resume text."""
    degree_patterns = [
        (re.compile(r"\b(ph\.?d\.?|doctorate|doctoral)\b", re.I), "Doctorate (Ph.D.)"),
        (re.compile(r"\b(master'?s?|m\.?s\.?|m\.?a\.?|m\.?b\.?a\.?|m\.?eng\.?|m\.?sc\.?|ll\.?m\.?)\b", re.I), "Master's Degree"),
        (re.compile(r"\b(bachelor'?s?|b\.?s\.?|b\.?a\.?|b\.?eng\.?|b\.?sc\.?|undergraduate)\b", re.I), "Bachelor's Degree"),
        (re.compile(r"\b(associate'?s?|a\.?a\.?|a\.?s\.?)\b", re.I), "Associate's Degree"),
    ]
    for pattern, label in degree_patterns:
        if pattern.search(text):
            return label
    return None


def check_experience_education(resume_text: str, job_text: str) -> dict:
    """Align resume experience and education against job posting requirements."""
    years_resume = extract_years_experience(resume_text)
    degree_resume = extract_highest_degree(resume_text)

    # Extract minimum experience from job
    job_exp_match = re.findall(
        r"(\d+)[+\s]*(?:years?|yrs?)\s+(?:of\s+)?(?:relevant\s+)?(?:professional\s+)?(?:work\s+)?experience",
        job_text, re.I
    )
    min_years_job = max(int(y) for y in job_exp_match) if job_exp_match else None

    # Degree required
    degree_required = None
    for pat_str, label in [
        (r"\b(ph\.?d\.?|doctorate|doctoral)\b", "Doctorate (Ph.D.)"),
        (r"\b(master'?s?|m\.?s\.?|m\.?a\.?|m\.?b\.?a\.?)\b", "Master's Degree"),
        (r"\b(bachelor'?s?|b\.?s\.?|b\.?a\.?|undergraduate)\b", "Bachelor's Degree"),
    ]:
        if re.search(pat_str, job_text, re.I):
            degree_required = label
            break

    issues = []
    if min_years_job and years_resume is not None and years_resume < min_years_job:
        issues.append({
            "dimension": "experience",
            "requirement": f"{min_years_job}+ years",
            "candidate": f"{years_resume} years (estimated)",
            "gap": "Candidate may fall below minimum experience threshold.",
        })
    if min_years_job and years_resume is None:
        issues.append({
            "dimension": "experience",
            "requirement": f"{min_years_job}+ years",
            "candidate": "Could not determine from resume text",
            "gap": "ATS parsers extract date ranges. Ensure employment dates use the format YYYY-YYYY or YYYY-Present on separate lines.",
        })

    degree_rank = {"Doctorate (Ph.D.)": 4, "Master's Degree": 3, "Bachelor's Degree": 2, "Associate's Degree": 1}
    if degree_required and degree_resume:
        if degree_rank.get(degree_resume, 0) < degree_rank.get(degree_required, 0):
            issues.append({
                "dimension": "education",
                "requirement": degree_required,
                "candidate": degree_resume,
                "gap": "Degree level may not meet minimum requirement.",
            })
    elif degree_required and not degree_resume:
        issues.append({
            "dimension": "education",
            "requirement": degree_required,
            "candidate": "Could not determine from resume text",
            "gap": "Ensure your degree is listed under a standard 'Education' section header with the degree name, institution, and year.",
        })

    return {
        "experience": {
            "years_parsed_from_resume": years_resume,
            "minimum_required_by_job": min_years_job,
        },
        "education": {
            "highest_degree_parsed": degree_resume,
            "minimum_required_by_job": degree_required,
        },
        "alignment_issues": issues,
        "passes_alignment": len(issues) == 0,
    }


# ---------------------------------------------------------------------------
# Estimated ATS Score (based on industry research weightings)
# ---------------------------------------------------------------------------

def calculate_ats_score(
    keyword_match: dict,
    format_audit: dict,
    sections: dict,
    experience_edu: dict,
    knockout: dict,
) -> dict:
    """
    Calculate an estimated ATS match score using the weighting scheme
    documented in industry research:
      - Skill Match: 40%
      - Experience Level: 30%
      - Education Relevance: 20%
      - Format & Clarity: 10%

    This is an ESTIMATE based on published research, not an actual ATS score.
    """
    # Skill Match (40%)
    skill_pct = keyword_match.get("keyword_match_percentage", 0) / 100.0
    # Penalize missing critical keywords
    critical_miss = len(keyword_match.get("critical_missing_keywords", []))
    skill_penalty = min(0.15, critical_miss * 0.03)
    skill_score = max(0, skill_pct - skill_penalty)

    # Experience Level (30%)
    exp_issues = experience_edu.get("alignment_issues", [])
    exp_issue_count = len([i for i in exp_issues if i["dimension"] == "experience"])
    exp_score = max(0, 1.0 - exp_issue_count * 0.5)

    # Education Relevance (20%)
    edu_issues = len([i for i in exp_issues if i["dimension"] == "education"])
    edu_score = max(0, 1.0 - edu_issues * 0.5)

    # Format & Clarity (10%)
    format_issues = len(format_audit.get("issues", []))
    format_score = max(0, 1.0 - format_issues * 0.2)

    weights = {"skill_match": 0.40, "experience": 0.30, "education": 0.20, "format": 0.10}
    total = (
        weights["skill_match"] * skill_score +
        weights["experience"] * exp_score +
        weights["education"] * edu_score +
        weights["format"] * format_score
    ) * 100

    return {
        "estimated_ats_score": round(total, 1),
        "score_breakdown": {
            "skill_match": {"weight": "40%", "raw_score": round(skill_score * 100, 1), "contribution": round(weights["skill_match"] * skill_score * 100, 1)},
            "experience": {"weight": "30%", "raw_score": round(exp_score * 100, 1), "contribution": round(weights["experience"] * exp_score * 100, 1)},
            "education": {"weight": "20%", "raw_score": round(edu_score * 100, 1), "contribution": round(weights["education"] * edu_score * 100, 1)},
            "format": {"weight": "10%", "raw_score": round(format_score * 100, 1), "contribution": round(weights["format"] * format_score * 100, 1)},
        },
        "disclaimer": (
            "This score is an ESTIMATE based on published ATS research (TF-IDF, "
            "cosine similarity, and weighted dimension models). Actual ATS scores "
            "vary by vendor (Taleo, iCIMS, Workday, Greenhouse, Eightfold), "
            "proprietary algorithms, and the employer's specific configuration of "
            "Required vs Asset criteria. Use this as a directional signal of gaps, "
            "not a prediction of pass/fail."
        ),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def analyze(resume_path: str, job_url: str) -> dict:
    """Run full ATS analysis and return results dict."""
    warn(MISSING_DEPS)

    stderr("Extracting resume text...")
    resume_text = extract_resume_text(resume_path)
    if not resume_text or not resume_text.strip():
        return {"error": "Failed to extract text from resume. Check the file/URL and required dependencies."}

    stderr(f"Resume extracted: {len(resume_text)} characters")

    stderr("Extracting job posting text...")
    job_text = extract_job_text(job_url)
    if not job_text or not job_text.strip():
        return {"error": "Failed to extract text from job posting URL. Check the URL and network connectivity."}

    stderr(f"Job posting extracted: {len(job_text)} characters")

    stderr("Analyzing format...")
    format_audit = audit_format(resume_text, resume_path)

    stderr("Detecting sections...")
    sections = detect_sections(resume_text)

    stderr("Extracting keywords...")
    resume_kw = extract_keywords(resume_text, source_name="resume")
    job_kw = extract_keywords(job_text, source_name="job_description")

    stderr("Matching keywords...")
    keyword_match = match_keywords(resume_kw, job_kw)

    stderr("Assessing knockout risks...")
    knockout = assess_knockout_risks(job_text, resume_text)

    stderr("Checking experience and education...")
    exp_edu = check_experience_education(resume_text, job_text)

    stderr("Calculating estimated ATS score...")
    score = calculate_ats_score(keyword_match, format_audit, sections, exp_edu, knockout)

    return {
        "analysis_metadata": {
            "resume_source": resume_path,
            "job_posting_source": job_url,
            "resume_character_count": len(resume_text),
            "job_posting_character_count": len(job_text),
            "dependencies_missing": MISSING_DEPS,
        },
        "format_audit": format_audit,
        "section_analysis": sections,
        "keyword_analysis": keyword_match,
        "knockout_assessment": knockout,
        "experience_education": exp_edu,
        "ats_score_estimate": score,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="ATS Resume Analyzer — compare resume to job posting for ATS optimization."
    )
    parser.add_argument(
        "--resume", "-r", required=True,
        help="Path to resume file (.pdf, .docx, .txt) or URL to a resume page."
    )
    parser.add_argument(
        "--job", "-j", required=True,
        help="URL of the job posting to compare against."
    )
    parser.add_argument(
        "--pretty", "-p", action="store_true",
        help="Pretty-print JSON output."
    )
    args = parser.parse_args()

    results = analyze(args.resume, args.job)
    indent = 2 if args.pretty else None
    print(json.dumps(results, indent=indent, ensure_ascii=False))


if __name__ == "__main__":
    main()
