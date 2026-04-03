#!/usr/bin/env python3
"""
EDCA Coverage Checklist Generator
Generates a complete 41-article coverage checklist for EDCA compliance audits.

Usage: python coverage_checklist.py [--output-format json|markdown]
"""

import json
from datetime import datetime

# Complete EDCA article list with metadata
EDCA_ARTICLES = [
    {"article": "Art. 1º", "topic": "Scope & applicability", "chapter": "I - Preliminary", "always_apply": True, "vetoed": False},
    {"article": "Art. 1º, parágrafo único", "topic": "Likely access criteria (3 factors)", "chapter": "I", "always_apply": False, "vetoed": False},
    {"article": "Art. 2º", "topic": "Definitions (12 terms)", "chapter": "I", "always_apply": True, "vetoed": False},
    {"article": "Art. 3º", "topic": "Core protection principles", "chapter": "I", "always_apply": False, "vetoed": False},
    {"article": "Art. 4º", "topic": "9 foundations for use", "chapter": "II - Products", "always_apply": False, "vetoed": False},
    {"article": "Art. 5º", "topic": "Duties (prevention, protection, info, security)", "chapter": "II", "always_apply": False, "vetoed": False},
    {"article": "Art. 6º", "topic": "Content safety prevention (6 types)", "chapter": "II", "always_apply": False, "vetoed": False},
    {"article": "Art. 7º", "topic": "Privacy by design/default", "chapter": "II", "always_apply": False, "vetoed": False},
    {"article": "Art. 8º", "topic": "Risk management & anti-compulsive use", "chapter": "II", "always_apply": False, "vetoed": False},
    {"article": "Art. 9º", "topic": "Age-restricted content access", "chapter": "III - Access Prohibition", "always_apply": False, "vetoed": False},
    {"article": "Art. 10º", "topic": "Age-appropriate experiences", "chapter": "IV - Age Measurement", "always_apply": False, "vetoed": False},
    {"article": "Art. 11º", "topic": "Public authority role", "chapter": "IV", "always_apply": False, "vetoed": False},
    {"article": "Art. 12º", "topic": "App stores/OS requirements", "chapter": "IV", "always_apply": False, "vetoed": False},
    {"article": "Art. 13º", "topic": "Age data purpose limitation", "chapter": "IV", "always_apply": False, "vetoed": False},
    {"article": "Art. 14º", "topic": "Technical measures for age info", "chapter": "IV", "always_apply": False, "vetoed": False},
    {"article": "Art. 15º", "topic": "Chain responsibility", "chapter": "IV", "always_apply": False, "vetoed": False},
    {"article": "Art. 16º", "topic": "Parental supervision info", "chapter": "V - Parental Supervision", "always_apply": False, "vetoed": False},
    {"article": "Art. 17º", "topic": "Supervision tools requirements", "chapter": "V", "always_apply": False, "vetoed": False},
    {"article": "Art. 18º", "topic": "Parental capabilities", "chapter": "V", "always_apply": False, "vetoed": False},
    {"article": "Art. 19º", "topic": "Child monitoring products", "chapter": "VI - Monitoring", "always_apply": False, "vetoed": False},
    {"article": "Art. 20º", "topic": "Loot box prohibition", "chapter": "VII - Games", "always_apply": False, "vetoed": False},
    {"article": "Art. 21º", "topic": "Game interaction safeguards", "chapter": "VII", "always_apply": False, "vetoed": False},
    {"article": "Art. 22º", "topic": "Advertising restrictions", "chapter": "VIII - Advertising", "always_apply": False, "vetoed": False},
    {"article": "Art. 23º", "topic": "Erotized content monetization prohibition", "chapter": "VIII", "always_apply": False, "vetoed": False},
    {"article": "Art. 24º", "topic": "Social network account linking", "chapter": "IX - Social Networks", "always_apply": False, "vetoed": False},
    {"article": "Art. 25º", "topic": "Social network data treatment rules", "chapter": "IX", "always_apply": False, "vetoed": False},
    {"article": "Art. 26º", "topic": "Behavioral profiling prohibition", "chapter": "IX", "always_apply": False, "vetoed": False},
    {"article": "Art. 27º", "topic": "Serious violations prevention", "chapter": "X", "always_apply": False, "vetoed": False},
    {"article": "Art. 28º", "topic": "Violation reporting channels", "chapter": "XI - Reporting", "always_apply": False, "vetoed": False},
    {"article": "Art. 29º", "topic": "Content removal duty", "chapter": "XI", "always_apply": False, "vetoed": False},
    {"article": "Art. 30º", "topic": "Removal procedure safeguards", "chapter": "XI", "always_apply": False, "vetoed": False},
    {"article": "Art. 31º", "topic": "Transparency reports (>1M users)", "chapter": "XII - Transparency", "always_apply": False, "vetoed": False},
    {"article": "Art. 32º", "topic": "Abuse of reporting tools", "chapter": "XIII - Abuse", "always_apply": False, "vetoed": False},
    {"article": "Art. 33º", "topic": "False reporting penalties", "chapter": "XIII", "always_apply": False, "vetoed": False},
    {"article": "Art. 34º", "topic": "Governance authority", "chapter": "XIV - Governance", "always_apply": False, "vetoed": False},
    {"article": "Art. 35º", "topic": "Sanctions", "chapter": "XV - Sanctions", "always_apply": True, "vetoed": False},
    {"article": "Art. 36º", "topic": "— (VETOED)", "chapter": "XV", "always_apply": False, "vetoed": True},
    {"article": "Art. 37º", "topic": "Executive branch regulation", "chapter": "XVI - Final", "always_apply": False, "vetoed": False},
    {"article": "Art. 38º", "topic": "Equipment packaging warnings", "chapter": "XVI", "always_apply": False, "vetoed": False},
    {"article": "Art. 39º", "topic": "Proportional application", "chapter": "XVI", "always_apply": True, "vetoed": False},
    {"article": "Art. 40º", "topic": "Legal representative requirement", "chapter": "XVI", "always_apply": False, "vetoed": False},
    {"article": "Art. 41º", "topic": "— (VETOED)", "chapter": "XVI", "always_apply": False, "vetoed": True},
]


def generate_markdown_checklist():
    """Generate markdown format coverage checklist."""
    lines = [
        "# EDCA Coverage Checklist",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "| Article | Topic | Applicability | Status | Findings |",
        "|---------|-------|---------------|--------|----------||",
    ]

    for art in EDCA_ARTICLES:
        if art["vetoed"]:
            applicability = "N/A"
            status = "✅ Vetoed"
            findings = "Not applicable"
        elif art["always_apply"]:
            applicability = "Applied"
            status = "✅ Analyzed"
            findings = "[To be filled]"
        else:
            applicability = "[Applicable/N/A]"
            status = "[Status]"
            findings = "[To be filled]"

        lines.append(f"| {art['article']} | {art['topic']} | {applicability} | {status} | {findings} |")

    lines.extend([
        "",
        "**Coverage Summary**: [X] articles applicable, [Y] articles N/A, [Z] findings total",
    ])

    return "\n".join(lines)


def generate_json_checklist():
    """Generate JSON format coverage checklist."""
    return json.dumps({
        "generated": datetime.now().isoformat(),
        "total_articles": len(EDCA_ARTICLES),
        "vetoed_articles": [a["article"] for a in EDCA_ARTICLES if a["vetoed"]],
        "always_apply": [a["article"] for a in EDCA_ARTICLES if a["always_apply"]],
        "articles": EDCA_ARTICLES
    }, indent=2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate EDCA coverage checklist")
    parser.add_argument("--output-format", choices=["json", "markdown"], default="markdown",
                        help="Output format (default: markdown)")

    args = parser.parse_args()

    if args.output_format == "json":
        print(generate_json_checklist())
    else:
        print(generate_markdown_checklist())