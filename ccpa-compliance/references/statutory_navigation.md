# Statutory Source Navigation Guide

This file provides detailed guidance on how to efficiently navigate the large statutory source files bundled with this skill.

---

## The Challenge

The two primary source files are too large to read entirely:

| File | Size | Token Estimate | Read Limit |
|------|------|----------------|------------|
| `California_CCPA_Title_1.81.5.md` | 280KB+ | ~40,000+ tokens | 2000 lines / 10K tokens max |
| `ccpa_statute_eff_20260101.md` | 103 pages | ~15,000 tokens | 2000 lines / 10K tokens max |

**You cannot read these files in full.** You must use targeted reading strategies.

---

## Navigation Strategy: Grep → Read Targeted Section

### The Two-Step Method

1. **Step 1: Grep** — Find where the relevant content is located
2. **Step 2: Read** — Use `offset` and `limit` to read just that portion

### Example: Finding the Definition of "Sale"

```
# Step 1: Grep for the definition
Grep pattern: "1798.140(ad)" OR "sale"
File: California_CCPA_Title_1.81.5.md

# Result shows line number where §1798.140(ad) appears

# Step 2: Read that portion
Read file: California_CCPA_Title_1.81.5.md
offset: [line number from grep]
limit: 50 (enough to capture the full definition subsection)
```

---

## Grep Pattern Catalog

### By Section Number

| To Find | Grep Pattern | File |
|---------|--------------|------|
| Business duties | `"1798.100"` | statute |
| Right to delete | `"1798.105"` | statute |
| Right to correct | `"1798.106"` | statute |
| Right to know | `"1798.110"` | statute |
| Right to opt-out | `"1798.120"` OR `"1798.135"` | statute |
| Right to limit SPI | `"1798.121"` | statute |
| Non-discrimination | `"1798.125"` | statute |
| Notice requirements | `"1798.130"` | statute |
| Definitions | `"1798.140"` | statute |
| Exemptions | `"1798.145"` | statute |
| Enforcement | `"1798.150"` | statute |
| CPPA authority | `"1798.185"` | statute |
| CPPA agency powers | `"1798.199"` | statute |

| To Find | Grep Pattern | File |
|---------|--------------|------|
| Collection restrictions | `"§ 7002"` | regulations |
| Notice at collection | `"§ 7012"` | regulations |
| Privacy policy | `"§ 7011"` | regulations |
| Opt-out link | `"§ 7013"` | regulations |
| SPI limit link | `"§ 7014"` | regulations |
| Request methods | `"§ 7020"` | regulations |
| Delete requests | `"§ 7022"` | regulations |
| Correct requests | `"§ 7023"` | regulations |
| Know requests | `"§ 7024"` | regulations |
| Preference signals | `"§ 7025"` | regulations |
| Verification | `"§ 7060"` | regulations |
| Children's data | `"§ 7070"` | regulations |
| Cybersecurity audit | `"§ 7120"` | regulations |
| Risk assessment | `"§ 7150"` | regulations |
| ADMT scope | `"§ 7200"` | regulations |

### By Topic Keyword

| Topic | Grep Pattern | Notes |
|-------|--------------|-------|
| "Personal information" definition | `"(o)"` within §1798.140 | Use context to find definition subsection |
| "Sensitive personal information" | `"(ae)"` within §1798.140 | 11 specific categories |
| "Business" threshold | `"(d)"` within §1798.140 | $25M, 100K consumers, 50% revenue |
| "Service provider" | `"(ag)"` within §1798.140 | Contract requirements |
| "Contractor" | `"(j)"` within §1798.140 | Similar to service provider |
| "Sale" | `"(ad)"` within §1798.140 | Monetary/valuable consideration |
| "Sharing" | `"(ah)"` within §1798.140 | Cross-context behavioral advertising |
| "Cross-context behavioral advertising" | `"(k)"` within §1798.140 | Definition |
| "Verifiable consumer request" | `"(ak)"` within §1798.140 | Authentication requirements |
| "Dark patterns" | `"(h)"` within §1798.140 | Prohibited interface designs |
| "Third party" | `"(v)"` within §1798.140 | Not service provider/contractor |

---

## Using the Section Index

The `references/section_index.md` file provides pre-computed line number ranges for major sections.

### How to Use It

1. Read `section_index.md` first to find the section you need
2. Note the `offset` and `limit` values provided
3. Execute Read with those parameters

**Example**:
```
# From section_index.md:
# §1798.140 | Definitions | 381 | offset: 381, limit: 300

# Execute:
Read file: California_CCPA_Title_1.81.5.md
offset: 381
limit: 300
```

This reads approximately lines 381-681, capturing the full definitions section.

---

## When Grep Fails: Fallback Strategies

### Situation: Grep Returns No Results

Possible causes:
1. The term is phrased differently in the statute
2. You're searching in the wrong file
3. The content exists but under different keywords

**Fallback approach**:
1. Try broader/synonymous keywords
2. Search both source files
3. Use section_index.md to navigate by section number instead
4. Read the relevant article/section by offset

### Situation: Grep Returns Too Many Results

The term appears throughout the document (e.g., "personal information").

**Refinement approach**:
1. Add context to your grep pattern (e.g., `"personal information.\"` for definitions)
2. Search for section numbers instead of keywords
3. Use `-n` flag to get line numbers, then select relevant ones

### Situation: Ambiguous Statutory Language

The statute genuinely uses unclear language.

**Handling approach**:
1. Read the full section (expand limit)
2. Check if regulations clarify (search CPPA file)
3. Document the ambiguity explicitly in your response
4. Recommend consulting qualified privacy counsel

---

## Reading Strategy Tips

### Use Multiple Small Reads

Instead of trying to read 2000 lines, read multiple targeted chunks:

```
# Bad: trying to read entire definitions section in one go
Read offset: 381, limit: 2000  → May hit limits

# Good: sequential targeted reads
Read offset: 381, limit: 100   → First part of definitions
Read offset: 481, limit: 100   → Middle part
Read offset: 581, limit: 100   → End part
```

### Prioritize Critical Sections

For most compliance tasks, these sections are most frequently needed:

| Priority | Section | Why |
|----------|---------|-----|
| 1 | §1798.140 (definitions) | All compliance analysis starts here |
| 2 | §1798.145 (exemptions) | Determines applicability first |
| 3 | §1798.100 (business duties) | Core obligations |
| 4 | §1798.130 (notice) | Privacy policy requirements |
| 5 | §1798.135 (opt-out) | Implementation details |

### Cross-Reference Both Files

For any topic, check BOTH the statute AND regulations:

```
# Example: Opt-out links
1. Grep statute for "1798.135" → Read that section
2. Grep regulations for "§ 7013" → Read that section
3. Compare: statute defines WHAT; regulations define HOW
```

---

## Statute vs. Regulations: When to Use Each

| Source | Content | Use For |
|--------|---------|---------|
| **Statute** (Title 1.81.5) | Legal definitions, rights, duties, exemptions, penalties | Determining if something is required; legal analysis; scope questions |
| **Regulations** (CPPA §7000-7304) | Implementation details, formats, timelines, procedures | Determining how to comply; practical implementation; form/content requirements |

**Rule**: Statute = WHAT; Regulations = HOW

Always check both. The statute may say "provide a clear link" but the regulations specify exactly what that link must say and where it must appear.

---

## Error Handling

### If You Cannot Locate Relevant Text

1. **Acknowledge the limitation**: "I could not locate specific statutory text on [topic]"
2. **State your basis**: "This analysis is based on [general principles / adjacent sections / regulatory guidance]"
3. **Recommend verification**: "For authoritative guidance on [topic], consult [specific source or counsel]"
4. **Do NOT fabricate**: Never make up statutory requirements you cannot verify

### If Text Is Genuine Ambiguous

1. **Quote the ambiguous text verbatim**
2. **Present multiple interpretations**: "This text could mean X or Y"
3. **Cite CPPA guidance if available**: Check regulations for clarification
4. **Escalate appropriately**: "This ambiguity warrants review by qualified privacy counsel"

---

## Quick Reference: Most Common Searches

| Task | Primary Grep | Secondary Grep | Read Priority |
|------|--------------|----------------|---------------|
| Does CCPA apply? | `"1798.140(d)"` | `"1798.145"` | exemptions first |
| What is PI? | `"1798.140(o)"` | `"§ 7001"` | statute definitions |
| What is SPI? | `"1798.140(ae)"` | `"§ 7001"` | statute definitions |
| Is this a sale? | `"1798.140(ad)"` | `"§ 7001"` | statute definitions |
| Notice requirements | `"1798.130"` | `"§ 7012"` | both required |
| Opt-out link | `"1798.135"` | `"§ 7013"` | both required |
| Consumer request handling | `"1798.130"` | `"§ 7020-7024"` | regulations practical |
| Service provider contracts | `"1798.140(ag)"` | `"§ 7050"` | both required |
| Cybersecurity audit | `"1798.185(a)(14)(A)"` | `"§ 7120"` | regulations detailed |
| Risk assessment | `"1798.185(a)(14)(B)"` | `"§ 7150"` | regulations detailed |
| ADMT | `"1798.185(a)(15)"` | `"§ 7200"` | regulations primary |