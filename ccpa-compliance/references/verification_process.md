# Document Verification Process

This file provides detailed guidance on the independent verification process for CCPA documents, including fallback methods when subagents are not available.

---

## Why Verification Matters

Document drafting carries inherent risk:
- The drafting agent has "author's blind spots" — may miss gaps they created
- Context from the conversation may bias judgment
- CCPA compliance requires precision — small omissions create liability

The verification process implements a "four-eyes principle" — a fresh perspective catches issues the author misses.

---

## Two Verification Methods

### Method A: Independent Subagent Verification (Preferred)

**When available**: Claude Code, environments with Agent tool access

**Advantages**:
- Truly independent — no context contamination
- Fresh perspective with no prior assumptions
- More rigorous "four-eyes" check

**Procedure**: See Workflow 2-A in skill.md

### Method B: Inline Self-Verification (Fallback)

**When required**: Claude.ai, Cowork, environments without subagent access

**Limitations**:
- Same agent, same context — less independent
- Potential for confirmation bias
- Requires deliberate "fresh eyes" mindset

**Procedure**: Follow the steps below

---

## Method B: Inline Self-Verification Procedure

### Step 1: Save Draft and Reset Context

Before starting verification:

1. **Save the draft document** to a file (e.g., `verification-temp/draft-v1.md`)
2. **Deliberately reset your mental context**:
   - Close the drafting conversation mentally
   - Approach the document as if you've never seen it before
   - Assume the author may have made errors
3. **Announce the verification**: "Now performing inline self-verification as independent review..."

### Step 2: Re-Read Statutory Requirements Fresh

**Do NOT rely on memory from the drafting session.**

1. Identify the document type
2. Use `references/statutory_navigation.md` to find ALL applicable sections
3. Read each applicable section from source files using Grep/Read
4. Create a fresh requirements checklist based ONLY on the source text you just read

**Example for Privacy Notice**:
```
# Re-read these sections completely:
1. §1798.130 → Read from statute (notice requirements)
2. §7011 → Read from regulations (privacy policy format)
3. §7012 → Read from regulations (notice at collection)
4. §7013 → Read from regulations (opt-out link)
5. §7014 → Read from regulations (SPI limit link)

# Extract requirements as you read — do NOT use pre-existing checklist
```

### Step 3: Line-by-Line Document Review

Approach the draft document with skepticism:

For each section of the draft:
1. Ask: "What statutory requirement does this address?"
2. Locate the exact source text for that requirement
3. Compare: Draft content vs. Source requirement
4. Note: Any gap, missing element, incorrect language, or omission

**Comparison checklist**:
- [ ] Does the draft include ALL elements the statute requires?
- [ ] Does the draft use language matching or equivalent to statutory language?
- [ ] Does the draft include elements the statute mandates but doesn't explicitly list in one place?
- [ ] Are there statutory requirements the draft completely omits?

### Step 4: Gap Identification Table

Create a systematic gap report:

```
## Verification Gap Report

### Document Verified
- Type: [Privacy Notice / Risk Assessment / Service Provider Agreement / etc.]
- File: [draft file path]
- Iteration: [v1]

### Statutory Requirements Checklist
| Requirement | Source Section | Draft Coverage | Status |
|-------------|----------------|----------------|--------|
| [Each requirement from source reading] | §XXXX | [Found/Partial/Missing] | ✅/⚠️/❌ |

### Gaps Identified
For each ❌ or ⚠️:

| Gap # | Requirement | Source Text (quote) | Draft Deficiency | Remediation Needed |
|-------|-------------|---------------------|------------------|-------------------|
| 1 | [requirement] | [quote exact text] | [what's missing/wrong] | [what to add/fix] |
```

### Step 5: Verification Conclusion

After completing the checklist:

- **No gaps found**: Document ready for delivery
- **Gaps found**: Proceed to amendment

State conclusion explicitly:
```
### Verification Conclusion
- **Gaps Found**: [X gaps requiring remediation]
- **Ready for Delivery**: Yes/No
- **Recommendation**: [Proceed / Amend and re-verify / Escalate to human review]
```

---

## Amendment Loop (If Gaps Found)

### Amendment Process

For each gap:
1. Read the cited source section again
2. Amend the draft to address the gap exactly as the statute requires
3. Save as `draft-v2.md` (increment iteration)
4. Perform verification again (Step 2-5)

### Iteration Limits

- Maximum **3 verification iterations** (v1 → v2 → v3 → v4)
- If gaps persist after 3 iterations:
  - Document residual gaps
  - Proceed to delivery with clear disclosure
  - Recommend human review

---

## Delivery with Verification Disclosure

### If No Gaps (Ready for Delivery)

State clearly:
```
This document has undergone independent verification against CCPA statutory requirements.
No compliance gaps were identified.

Verification performed: [inline self-verification due to environment constraints]
```

### If Residual Gaps After Max Iterations

Disclose transparently:
```
⚠️ Verification Disclosure

This document underwent [X] verification iterations. The following residual gaps
could not be fully resolved:

[List each residual gap with statutory citation]

**Recommendation**: These gaps require human review by a qualified privacy professional
or legal counsel before final use.

Verification performed: [inline self-verification due to environment constraints]
```

---

## Verification Documentation

Maintain a verification log:

| Iteration | Draft File | Gaps Found | Major Amendments |
|-----------|------------|------------|------------------|
| 1 | draft-v1.md | [count] | [summary] |
| 2 | draft-v2.md | [count] | [summary] |
| ... | ... | ... | ... |

This log demonstrates the verification effort and provides audit trail.

---

## Common Verification Pitfalls

### Pitfall 1: Confirmation Bias

**Problem**: You verify your own work and "find" it compliant because you expect it to be.

**Mitigation**: 
- Deliberately adopt skeptical mindset
- Ask "what might be wrong?" not "is this correct?"
- Assume gaps exist until proven otherwise

### Pitfall 2: Incomplete Source Reading

**Problem**: You rely on memory or partial reading, missing requirements.

**Mitigation**:
- ALWAYS re-read source files fresh
- Use Grep to find ALL applicable sections
- Read each section completely, not just portions

### Pitfall 3: Missing Cross-References

**Problem**: A requirement in §1798.130 references requirements in other sections; you miss those.

**Mitigation**:
- When reading a section, note references to other sections
- Read referenced sections too
- Regulations often cross-reference statute; check both

### Pitfall 4: Accepting "Close Enough" Language

**Problem**: Draft uses similar language but not exact statutory language; you accept it.

**Mitigation**:
- Compare exact wording
- If statute says "clear and conspicuous link titled 'Do Not Sell or Share My Personal Information'", the draft must use that exact title
- "Similar" is not always compliant

---

## Verification Environment Considerations

### Claude Code (Subagents Available)

Use Method A (Independent Subagent Verification):
- Spawn general-purpose agent with no context
- Provide self-contained verification prompt
- Receive independent gap report

### Claude.ai (No Subagents)

Use Method B (Inline Self-Verification):
- Follow procedure above
- Explicitly disclose verification method in delivery
- Recommend human review for high-risk documents

### Cowork (Subagents Available, No Display)

Use Method A with modifications:
- Spawn subagent in background
- Wait for task completion notification
- Read output file for gap report
- Use `--static` for any viewer output

---

## Verification Intensity by Document Type

Some documents warrant more rigorous verification than others:

| Document | Risk Level | Verification Intensity |
|----------|------------|------------------------|
| Privacy Policy (public-facing) | High | Full verification, max iterations |
| Risk Assessment (submitted to CPPA) | Very High | Full verification, human review recommended |
| Service Provider Agreement | High | Full verification, 2+ iterations minimum |
| Consumer Rights Procedure | Medium | Standard verification |
| Cybersecurity Audit | High | Full verification |
| Notice at Collection | Medium | Standard verification |
| Internal compliance memo | Low | Basic verification |

**Recommendation**: For "Very High" risk documents, always recommend human review regardless of verification outcome.

---

## What Verification Does NOT Guarantee

Verification confirms:
- Document addresses stated statutory requirements
- No obvious gaps against cited source text

Verification does NOT guarantee:
- Complete legal compliance (statute may have unstated expectations)
- Protection from CPPA enforcement interpretation
- Suitability for your specific business context
- Compliance with evolving regulatory guidance

**Always recommend qualified privacy counsel for final review of high-stakes documents.**