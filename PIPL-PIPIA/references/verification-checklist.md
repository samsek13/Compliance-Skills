---
name: verification-checklist
description: Structured checklist for independent PIPIA verification
type: reference
---

# PIPIA Verification Checklist (PIPIA验证检查清单)

Use this checklist when performing independent verification of a PIPIA report.

---

## Pre-Verification Execution Protocol

**MANDATORY: Execute these reads BEFORE starting verification.**

### Step 1 — Read Primary Legal Sources
Execute these commands in order:

```
1. Grep pattern: "第五十五条" on laws/中华人民共和国个人信息保护法_中国人大网.md
   → Read the complete Article 55 text

2. Grep pattern: "第五十六条" on same file
   → Read the complete Article 56 text

3. Read GB/T 39335-2020 Section 5 (评估实施流程)
```

### Step 2 — Read Scenario-Specific Sources
Based on the report content, read applicable laws per `references/legal-source-roadmap.md`:
- Cross-border? → Read 促进和规范数据跨境流动规定 §5-8
- Sensitive PI? → Read PIPL §28-32
- Children's PI? → Read 儿童个人信息网络保护规定
- App? → Read 常见类型App必要个人信息范围规定

### Step 3 — Verify Source Access
Confirm you have read the actual source files. If any read fails:
- **STOP verification**
- Report: "无法读取[文件/条款]原文，无法完成验证"
- Do NOT proceed with partial verification

---

## Checklist: Legal Requirements (PIPL §55-56)

### Article 55 Trigger Conditions (第五十五条触发条件)

**After reading PIPL §55, fill in the complete quoted text for each requirement:**

| # | Requirement | Source Text (Quote COMPLETE provision from PIPL §55) | Report Coverage | Status |
|---|-------------|------------------------------------------------------|-----------------|--------|
| 55.1 | 处理敏感个人信息 | [Quote: "有下列情形之一的，个人信息处理者应当事前进行个人信息保护影响评估...（一）处理敏感个人信息..."] | [Check report §2.2] | ✅/⚠️/❌ |
| 55.2 | 利用个人信息进行自动化决策 | [Quote complete text from §55（二）] | [Check report §2.3] | ✅/⚠️/❌ |
| 55.3 | 委托处理/向他人提供/公开 | [Quote complete text from §55（三）] | [Check report §2.5] | ✅/⚠️/❌ |
| 55.4 | 向境外提供个人信息 | [Quote complete text from §55（四）] | [Check report cross-border section] | ✅/⚠️/❌ |
| 55.5 | 其他对个人权益有重大影响 | [Quote complete text from §55（五）] | [Check report §6] | ✅/⚠️/❌ |

**Verification notes:**
- The Source Text column must contain the COMPLETE quoted provision, not truncated snippets
- Check if report correctly identifies which trigger condition(s) apply
- If multiple triggers, all must be addressed

### Article 56 Content Requirements (第五十六条内容要求)

**After reading PIPL §56, fill in the complete quoted text:**

| # | Requirement | Source Text (Quote COMPLETE provision from PIPL §56) | Report Coverage | Status |
|---|-------------|------------------------------------------------------|-----------------|--------|
| 56.1 | 处理目的、方式等是否合法、正当、必要 | [Quote: "个人信息保护影响评估应当包括下列内容：（一）个人信息的处理目的、处理方式等是否合法、正当、必要..."] | [Check report §4] | ✅/⚠️/❌ |
| 56.2 | 对个人权益的影响及安全风险 | [Quote complete text from §56（二）] | [Check report §6-7] | ✅/⚠️/❌ |
| 56.3 | 保护措施是否合法、有效并与风险相适应 | [Quote complete text from §56（三）] | [Check report §8] | ✅/⚠️/❌ |
| 56.4 | 评估结论 | [Quote: 报告应包含明确评估结论] | [Check report §10] | ✅/⚠️/❌ |

---

## Checklist: Methodology Requirements (GB/T 39335-2020)

**MANDATORY: Read GB/T 39335-2020 relevant sections before verification.**

### Section 5.3 数据映射分析

| # | Requirement | Source Text (Quote from GB/T 39335-2020) | Report Coverage | Status |
|---|-------------|------------------------------------------|-----------------|--------|
| 5.3.1 | 个人信息类型列表 | [Quote §5.3 requirement] | [Check report §3] | ✅/⚠️/❌ |
| 5.3.2 | 处理目的说明 | [Quote §5.3 requirement] | [Check report §2.1] | ✅/⚠️/❌ |
| 5.3.3 | 收集来源和方法 | [Quote §5.3 requirement] | [Check report §2.3] | ✅/⚠️/❌ |
| 5.3.4 | 存储位置和期限 | [Quote §5.3 requirement] | [Check report §2.3] | ✅/⚠️/❌ |
| 5.3.5 | 第三方处理情况 | [Quote §5.3 requirement] | [Check report §2.5] | ✅/⚠️/❌ |

### Section 5.4 风险源识别

| # | Dimension | Source Text (Quote from GB/T 39335-2020 §5.4) | Report Coverage | Status |
|---|-----------|-----------------------------------------------|-----------------|--------|
| 5.4.a | 网络环境和技术措施 | [Quote §5.4 a) requirement] | [Check report §5.1] | ✅/⚠️/❌ |
| 5.4.b | 个人信息处理流程 | [Quote §5.4 b) requirement] | [Check report §5.2] | ✅/⚠️/❌ |
| 5.4.c | 参与人员与第三方 | [Quote §5.4 c) requirement] | [Check report §5.3] | ✅/⚠️/❌ |
| 5.4.d | 业务特点和规模及安全态势 | [Quote §5.4 d) requirement] | [Check report §5.4] | ✅/⚠️/❌ |

### Section 5.5 个人权益影响分析

| # | Impact Dimension | Source Text (Quote from GB/T 39335-2020 §5.5) | Report Coverage | Status |
|---|------------------|-----------------------------------------------|-----------------|--------|
| 5.5.1 | 限制个人自主决定权 | [Quote §5.5 impact dimension 1] | [Check report §6.2] | ✅/⚠️/❌ |
| 5.5.2 | 引发差别性待遇 | [Quote §5.5 impact dimension 2] | [Check report §6.2] | ✅/⚠️/❌ |
| 5.5.3 | 个人名誉受损或遭受精神压力 | [Quote §5.5 impact dimension 3] | [Check report §6.2] | ✅/⚠️/❌ |
| 5.5.4 | 人身财产受损 | [Quote §5.5 impact dimension 4] | [Check report §6.2] | ✅/⚠️/❌ |

### Section 5.6 安全风险综合分析

| # | Requirement | Source Text (Quote from GB/T 39335-2020 §5.6/Appendix D) | Report Coverage | Status |
|---|-------------|----------------------------------------------------------|-----------------|--------|
| 5.6.1 | 安全事件可能性分析 | [Quote §5.6/Appendix D.1-D.2] | [Check report §7.1] | ✅/⚠️/❌ |
| 5.6.2 | 影响程度判定 | [Quote Appendix D.3-D.4] | [Check report §6.3] | ✅/⚠️/❌ |
| 5.6.3 | 风险等级判定 | [Quote Appendix D.5 risk matrix] | [Check report §7.2] | ✅/⚠️/❌ |

### Section 5.7 评估报告

| # | Requirement | Source Text (Quote from GB/T 39335-2020 §5.7) | Report Coverage | Status |
|---|-------------|-----------------------------------------------|-----------------|--------|
| 5.7.1 | 报告结构完整 | [Quote §5.7 structure requirements] | [All 11 sections?] | ✅/⚠️/❌ |
| 5.7.2 | 基本信息完备 | [Quote §5.7 info requirements] | [Check report §1] | ✅/⚠️/❌ |
| 5.7.3 | 评估结论明确 | [Quote §5.7 conclusion requirements] | [Check report §10] | ✅/⚠️/❌ |

### Section 5.8 风险处置

| # | Requirement | Source Text (Quote from GB/T 39335-2020 §5.8) | Report Coverage | Status |
|---|-------------|-----------------------------------------------|-----------------|--------|
| 5.8.1 | 风险处置建议提出 | [Quote §5.8 disposal options] | [Check report §9] | ✅/⚠️/❌ |
| 5.8.2 | 建议与风险等级匹配 | [Quote §5.8 matching requirements] | [Logical correspondence] | ✅/⚠️/❌ |

---

## Checklist: Cross-Border Transfer (If Applicable)

If the PIPIA involves cross-border transfer, additionally verify:

**MANDATORY: Read 促进和规范数据跨境流动规定 §5-8 before verification.**

| # | Requirement | Source Text (Quote from relevant regulation) | Report Coverage | Status |
|---|-------------|----------------------------------------------|-----------------|--------|
| CB.1 | 跨境传输路径正确判定 | [Quote 促进和规范数据跨境流动规定 §5-8 thresholds] | [Pathway identified] | ✅/⚠️/❌ |
| CB.2 | 数据量计算准确 | [Quote threshold numbers from regulation] | [Volumes stated] | ✅/⚠️/❌ |
| CB.3 | 接收方保护能力分析 | [Quote PIPL §38-39 requirements] | [Check report §2.5] | ✅/⚠️/❌ |
| CB.4 | 标准合同/认证/评估要求满足 | [Quote pathway-specific requirements] | [Pathway addressed] | ✅/⚠️/❌ |

---

## Checklist: Special Subjects (If Applicable)

### Children's PI (儿童个人信息)

**MANDATORY: Read 儿童个人信息网络保护规定 and PIPL §32 before verification.**

| # | Requirement | Source Text (Quote) | Report Coverage | Status |
|---|-------------|---------------------|-----------------|--------|
| CH.1 | 明确识别为儿童PI | [Quote PIPL §32/儿童规定 definition] | [Stated in §2.2] | ✅/⚠️/❌ |
| CH.2 | 监护人同意机制分析 | [Quote 儿童规定 consent requirements] | [Check §4.3] | ✅/⚠️/❌ |
| CH.3 | 儿童特定保护措施 | [Quote 儿童规定 §7-9 protection measures] | [Check §8] | ✅/⚠️/❌ |

### Sensitive PI (敏感个人信息)

**MANDATORY: Read PIPL §28-32 before verification.**

| # | Requirement | Source Text (Quote from PIPL) | Report Coverage | Status |
|---|-------------|-------------------------------|-----------------|--------|
| SP.1 | 正确识别敏感PI类型 | [Quote PIPL §28 definition] | [Check §2.2] | ✅/⚠️/❌ |
| SP.2 | 特定目的和必要性分析 | [Quote PIPL §29 requirements] | [Check §4.2] | ✅/⚠️/❌ |
| SP.3 | 告知要求分析 | [Quote PIPL §30 requirements] | [Check §4.3] | ✅/⚠️/❌ |
| SP.4 | 特别保护措施 | [Quote PIPL §31 requirements] | [Check §8] | ✅/⚠️/❌ |

---

## Gap Classification Guidance

When identifying gaps, classify severity:

| Status | Meaning | Action |
|--------|---------|--------|
| ✅ | Fully satisfied with source quote | No action needed |
| ⚠️ | Partially addressed or missing source quote | Needs amendment |
| ❌ | Missing, incorrect, or contradicts source text | Critical gap |

### ⚠️ Partial Gap Examples:
- Requirement mentioned but not fully analyzed
- Legal citation present but source text not quoted
- Analysis present but conclusion unclear

### ❌ Critical Gap Examples:
- Required section entirely missing
- Incorrect legal interpretation
- No citation to source text
- Conclusion contradicts source text
- Agent used memory instead of reading source file

---

## Verification Report Template

After completing checklist, produce Gap Report:

```markdown
## PIPIA Verification Gap Report (个人信息保护影响评估验证差距报告)

### Report Verified
- File: [draft file path]
- Iteration: [v1/v2/etc.]
- Assessment Object: [from report]

### Source Files Read
[List all source files read during verification, with evidence of reading]

### Summary Statistics
- Total items checked: [N]
- Fully satisfied (✅): [N]
- Partial gaps (⚠️): [N]
- Critical gaps (❌): [N]

### Legal Requirements Checklist Summary
| Requirement Category | ✅ | ⚠️ | ❌ | Notes |
|----------------------|----|----|-----|-------|
| PIPL §55 triggers | | | | |
| PIPL §56 content | | | | |
| GB/T 39335 methodology | | | | |
| Cross-border (if applicable) | | | | |
| Special subjects (if applicable) | | | | |

### Detailed Gaps
For each ❌ and ⚠️:
| Gap # | Requirement | Source Text Expected | Report Deficiency | Remediation |
|-------|-------------|---------------------|-------------------|-------------|
| 1 | [requirement] | [quote expected text] | [what's missing/wrong] | [what to fix] |

### Verification Conclusion
- **Gaps Found**: [X gaps requiring remediation]
- **Ready for Delivery**: Yes/No
- **Recommendation**: [Proceed / Amend and re-verify / Escalate to human legal review]
```