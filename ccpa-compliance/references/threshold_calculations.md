# CCPA Business Applicability — Methodology Guide

## Purpose

This file provides **methodology guidance** for determining CCPA applicability. It does NOT contain threshold values or exemption details — those must be read from the statutory source text.

**CRITICAL**: All threshold values and exemption criteria must be extracted from:
- §1798.140(d) for business thresholds
- §1798.145 for exemptions

Do NOT use values from memory or general knowledge. Read the source text.

---

## Applicability Determination Process

### Phase 1: Threshold Analysis

**Source**: Read §1798.140(d) from `California_CCPA_Title_1.81.5.md`

**How to locate**:
1. Use `references/section_index.md` to find line range for §1798.140
2. Grep for `"1798.140(d)"` or `"1798.140"` then locate subsection `(d)`
3. Read the complete subsection using Read with offset/limit

**What to extract from source text**:
- Each threshold criterion stated in the text
- The exact numerical values or conditions specified
- Any adjustment provisions (e.g., annual CPI adjustments)
- The relationship between thresholds (any one? all? specific combinations?)

**Output format**:
```
Threshold criteria extracted from §1798.140(d):

1. [First criterion from text]: "[Quote exact language]"
2. [Second criterion from text]: "[Quote exact language]"
3. [Third criterion from text]: "[Quote exact language]"
```

**Applying thresholds**:
For each criterion extracted:
```
| Criterion (from source) | Source Quote | Business Facts | Met? |
|-------------------------|--------------|----------------|------|
| [criterion] | "[quote]" | [relevant facts] | [Yes/No/Unknown] |
```

---

### Phase 2: Exemption Analysis

**Source**: Read §1798.145 from `California_CCPA_Title_1.81.5.md`

**How to locate**:
1. Use `references/section_index.md` to find line range for §1798.145
2. Grep for `"1798.145"`
3. Read the complete section using Read with offset/limit

**What to extract from source text**:
- Each exemption category stated in the text
- The exact scope of each exemption
- Any conditions or limitations on exemptions
- Whether exemptions are full or partial

**Output format**:
```
Exemptions extracted from §1798.145:

1. [Exemption category]: "[Quote exact language describing scope]"
   - Applicable to: [from text]
   - Limitations: [from text, if any]

2. [Exemption category]: "[Quote exact language]"
   ...
```

**Applying exemptions**:
For each potentially relevant exemption:
```
| Exemption (from source) | Source Quote | PI Category Involved | Applies? |
|-------------------------|--------------|----------------------|----------|
| [exemption] | "[quote]" | [category] | [Yes/No/Partial] |
```

---

## Calculation Methodologies

The following are **methodologies only**. Actual values come from source text.

### Revenue Threshold Methodology

1. Determine the threshold value by reading §1798.140(d)(1)
2. Determine if any annual adjustment applies by reading §1798.185(a)(5)
3. Check CPPA website for current adjusted value if statute indicates adjustment
4. Compare business annual gross revenue to threshold

**Formula structure** (values from source):
```
Business Revenue [operator] Threshold Value = [result]
```

### PI Volume Threshold Methodology

1. Determine the volume threshold by reading §1798.140(d)(2)
2. Determine what counts toward the volume (buys? receives? sells? shares?)
3. Determine the counting unit (consumers? households? devices? any of these?)
4. Determine the time period (annual? preceding 12 months?)
5. Calculate total volume across all applicable activities
6. Compare to threshold

**Formula structure** (values from source):
```
Total Volume = [sum of applicable activities per source text]
Result = Total Volume [operator] Threshold Value
```

### Sale-Derived Revenue Threshold Methodology

1. Determine the percentage threshold by reading §1798.140(d)(3)
2. Determine what revenue counts (selling? sharing? both?)
3. Calculate revenue from applicable activities
4. Calculate percentage of total revenue
5. Compare to threshold

**Formula structure** (values from source):
```
Percentage = (Applicable Revenue ÷ Total Revenue) × 100
Result = Percentage [operator] Threshold Value
```

---

## "Does Business in California" Analysis

**Source**: This is a factual determination, not a statutory definition.

Factors to consider:
- Does the business have operations in California?
- Does the business sell products/services to California residents?
- Does the business have California-based employees?
- Does the business handle personal information of California residents?

**Note**: Even purely online businesses may "do business in California" if they have California customers.

---

## Threshold Calculation Checklist

Use this checklist structure. Fill in values from source text.

### Step 1: California Business Operations
- [ ] Does business operate in California? [Yes/No]
- [ ] Evidence: [describe]

If NO → CCPA does not apply (no need to check thresholds)

### Step 2: Read Threshold Section
- [ ] Read §1798.140(d) from source
- [ ] Extract threshold values/criteria from text
- [ ] Quote: "[relevant portions]"

### Step 3: Apply Each Threshold
For each threshold found in §1798.140(d):
- [ ] Threshold: [description from text]
- [ ] Source quote: "[quote]"
- [ ] Business facts: [relevant facts]
- [ ] Met? [Yes/No]

### Step 4: Read Exemption Section
- [ ] Read §1798.145 from source
- [ ] Extract exemption categories from text
- [ ] Quote: "[relevant portions]"

### Step 5: Apply Each Relevant Exemption
For each potentially applicable exemption found in §1798.145:
- [ ] Exemption: [description from text]
- [ ] Source quote: "[quote]"
- [ ] PI category: [category]
- [ ] Applies? [Yes/No/Partial]

### Step 6: Conclusion
- Thresholds met: [which ones, with quotes]
- Exemptions apply: [which ones, with quotes]
- CCPA applicable: [Yes/No/Partial]
- Basis: [summary with citations]

---

## Common Analysis Scenarios

These scenarios illustrate the **analysis process**, not the answers.

### Scenario: Mixed Data Contexts

When a business has multiple PI categories:
1. Read §1798.145 to determine which exemptions apply to which categories
2. For each PI category, determine if an exemption applies
3. PI without applicable exemptions remains subject to CCPA
4. Document bifurcated compliance obligations

**Output**:
```
PI Category: [category]
- Exemption analysis: §1798.145(X) "[quote]" — [applies/doesn't apply]
- CCPA applies to this category: [Yes/No]
```

### Scenario: Threshold Fluctuation

When business may cross/uncross thresholds:
1. Monitor each threshold criterion from §1798.140(d) regularly
2. Recalculate based on current facts
3. Document when thresholds are crossed
4. Adjust compliance posture accordingly

### Scenario: Partial Exemptions

When some PI is exempt but other PI is not:
1. Read §1798.145 carefully to determine scope of each exemption
2. Classify each PI category against exemption criteria
3. Maintain separate compliance for non-exempt PI
4. Document which CCPA requirements apply to which PI categories

---

## Important Reminders

1. **Values change**: The CPPA may adjust threshold values annually. Always check:
   - The current statutory text
   - CPPA website for adjusted values
   - Whether adjustments have been published

2. **Read before concluding**: Do NOT determine applicability without:
   - Reading §1798.140(d) for thresholds
   - Reading §1798.145 for exemptions
   - Quoting the text that supports your conclusion

3. **Quote everything**: Every threshold value and exemption criterion must be supported by a quote from source text.

4. **Document gaps**: If you cannot locate relevant text, state this explicitly rather than guessing.

---

## Where to Find Values

| Information Needed | Source Section | How to Locate |
|--------------------|----------------|---------------|
| Threshold criteria and values | §1798.140(d) | Grep `"1798.140"` then find subsection `(d)` |
| Adjustment mechanism | §1798.185(a)(5) | Grep `"1798.185"` then find subsection |
| Exemption categories | §1798.145 | Grep `"1798.145"` |
| Current adjusted values | CPPA website | https://cppa.ca.gov |

**Remember**: This file provides methodology. The actual values come from reading the source text.