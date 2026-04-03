---
name: practical-examples
description: Example filled PIPIA excerpts and gap report for training/reference
type: reference
---

# Practical Examples (实务示例)

This file contains example filled excerpts and gap reports to illustrate proper PIPIA drafting and verification.

---

## Example 1: Proper Legal Citation (正确法律引用方式)

### ✅ Correct Example

```markdown
### 4.1 处理合法性分析

本处理活动基于《个人信息保护法》第十三条第一款规定的"取得个人的同意"作为合法性基础。

根据《个人信息保护法》第十三条规定："处理个人信息应当取得个人同意，但有下列情形之一的，不需取得个人同意：（一）取得个人的同意..."

本APP在用户首次注册时，通过隐私政策弹窗明确告知用户个人信息收集目的、类型、方式，并要求用户点击"同意"按钮后方可继续使用。该同意机制符合《个人信息保护法》第十四条关于同意应当"由个人在充分知情的前提下自愿、明确作出"的要求。

具体实现：
- 隐私政策弹窗在注册页面强制展示，不可跳过
- 用户必须点击"同意并继续"按钮才能进入APP
- 同意动作被记录并存储于用户同意日志系统
```

### ❌ Incorrect Example (Do NOT do this)

```markdown
### 4.1 处理合法性分析

本处理活动符合法律规定，因为我们获得了用户同意。用户在注册时同意了隐私政策，所以我们的处理是合法的。
```

**Why incorrect:**
- No citation to specific article number
- No quote of statutory text
- Vague reference to "法律规定" without specificity
- No analysis of whether consent meets §14 requirements

---

## Example 2: Sensitive PI Identification (敏感个人信息识别)

### ✅ Correct Example

```markdown
### 2.2 个人信息类型

根据《个人信息保护法》第二十八条定义："敏感个人信息是一旦泄露或者非法使用，容易导致自然人的人格尊严受到侵害或者人身、财产安全受到危害的个人信息，包括生物识别、宗教信仰、特定身份、医疗健康、金融账户、行踪轨迹等信息，以及不满十四周岁未成年人的个人信息。"

本APP收集的个人信息类型如下：

| 信息类型 | 是否敏感PI | 法律依据 | 收集场景 |
|----------|------------|----------|----------|
| 手机号码 | 否 | — | 用户注册 |
| 用户位置信息 | **是** | PIPL §28 ("行踪轨迹") | 导航功能 |
| 面部识别特征 | **是** | PIPL §28 ("生物识别") | 身份验证 |
| 银行卡号 | **是** | PIPL §28 ("金融账户") | 支付功能 |

**敏感个人信息处理触发PIPIA要求：**
根据《个人信息保护法》第五十五条第一款规定："有下列情形之一的，个人信息处理者应当事前进行个人信息保护影响评估...（一）处理敏感个人信息"，本APP处理用户位置信息、面部识别特征、银行卡号属于处理敏感个人信息，应当事前进行PIPIA。
```

---

## Example 3: Risk Level Determination (风险等级判定)

### ✅ Correct Example

```markdown
### 7.2 风险等级判定

根据GB/T 39335-2020附录D表D.5风险等级判定矩阵：

| 可能性等级 | 影响程度 | 风险等级 |
|------------|----------|----------|
| 很低 (1) | 一般 (1) | 可接受 |
| 低 (2) | 严重 (2) | 中 |
| 中 (3) | 高 (3) | 高 |
| 高 (4) | 极高 (4) | 极高 |

本评估结果：

**安全事件可能性等级：中 (3)**
依据GB/T 39335-2020附录D表D.1，判定依据：
- 技术措施：已实施AES-256加密，访问控制完善 → 降低可能性
- 但存在第三方SDK数据接口，第三方安全能力未经充分验证 → 提升可能性
- 综合判定：中等级

**个人权益影响程度：严重 (2)**
依据GB/T 39335-2020附录D表D.3：
- 敏感个人信息涉及金融账户信息，一旦泄露可能导致财产损失 → 严重影响
- 位置信息泄露可能导致人身安全风险 → 中等影响
- 综合判定：严重程度

**最终风险等级：中**
根据表D.5，可能性(中) × 影响(严重) = 风险等级：中

**风险处置建议：**
针对中等级风险，建议：
1. 加强第三方SDK安全审计（按GB/T 39335-2020 §5.4c）
2. 实施更严格的数据访问权限控制（按PIPL §51）
3. 增加数据出境监控机制
```

---

## Example 4: Gap Report (验证差距报告示例)

### Gap Report Sample

```markdown
## PIPIA Verification Gap Report (个人信息保护影响评估验证差距报告)

### Report Verified
- File: verification-temp/draft-pipia-v1.md
- Iteration: v1
- Assessment Object: XX移动APP个人信息收集处理

### Summary Statistics
- Total items checked: 28
- Fully satisfied (✅): 21
- Partial gaps (⚠️): 4
- Critical gaps (❌): 3

### Legal Requirements Checklist Summary
| Requirement Category | ✅ | ⚠️ | ❌ | Notes |
|----------------------|----|----|-----|-------|
| PIPL §55 triggers | 4 | 1 | 0 | 敏感PI正确识别 |
| PIPL §56 content | 2 | 1 | 2 | 关键差距在§56.1 |
| GB/T 39335 methodology | 15 | 2 | 1 | 数据映射不完整 |
| Cross-border | — | — | — | 不适用 |
| Special subjects | 0 | 0 | 0 | 不涉及儿童PI |

### Detailed Gaps

#### ❌ Gap 1: 处理必要性分析缺失
| Gap # | Requirement | Source Text | Report Deficiency | Remediation Needed |
|-------|-------------|-------------|-------------------|-------------------|
| 1 | §56.1 处理必要性分析 | 《个人信息保护法》第五十六条第一款："（一）个人信息的处理目的、处理方式等是否合法、正当、必要" | 报告§4.2仅描述收集了哪些信息，未分析收集必要性，未引用"常见类型App必要个人信息范围规定" | 补充必要性分析，对照App必要个人信息范围规定§5，逐项分析每类信息收集是否必要 |

#### ❌ Gap 2: 法律引用缺失具体条文
| Gap # | Requirement | Source Text | Report Deficiency | Remediation Needed |
|-------|-------------|-------------|-------------------|-------------------|
| 2 | §56.1 合法性分析引用 | 应引用具体条文并引用原文 | 报告多处使用"根据法律规定"等模糊表述，未指明具体条文号 | 所有法律引用需改为"根据《个人信息保护法》第X条规定"并引用原文 |

#### ❌ Gap 3: 数据映射缺少存储期限信息
| Gap # | Requirement | Source Text | Report Deficiency | Remediation Needed |
|-------|-------------|-------------|-------------------|-------------------|
| 3 | GB/T 39335 §5.3 数据映射完整性 | GB/T 39335-2020第5.3条要求分析"存储位置和期限" | 报告§3数据映射分析未说明各类个人信息存储期限 | 补充每类信息的存储期限，说明删除机制 |

#### ⚠️ Gap 4: 第三方分析不充分
| Requirement | Source Text | Report Deficiency | Remediation Needed |
|-------------|-------------|-------------------|-------------------|
| GB/T 39335 §5.4c 参与人员与第三方 | "分析参与个人信息处理的人员与第三方是否可能引发安全风险" | 报告§5.3提及第三方SDK但未分析其安全能力、合同约束情况 | 补充第三方安全能力评估、数据处理协议审查情况 |

### Verification Conclusion
- **Gaps Found**: 7 gaps requiring remediation (3 critical, 4 partial)
- **Ready for Delivery**: **No**
- **Recommendation**: **Amend and re-verify** — 重点修复❌ Gap 1-3后重新提交验证
```

---

## Example 5: Cross-Border Pathway Determination (跨境传输路径判定)

### ✅ Correct Example

```markdown
## 跨境传输路径分析

### Step 1: 实体类型判定
本公司非关键信息基础设施运营者(CIIO)。依据《网络安全法》第三十一条，关键信息基础设施是指"一旦遭到破坏、丧失功能或者数据泄露，可能严重危害国家安全、国计民生、公共利益的重要网络设施、信息系统等"。本公司为普通互联网企业，未被监管部门指定为CIIO。

### Step 2: 数据量计算
自2025年1月1日起累计向境外提供个人信息量：
- 个人信息主体数量：85万人
- 敏感个人信息主体数量：8千人（含位置信息、银行卡号）

### Step 3: 跨境路径判定
依据《促进和规范数据跨境流动规定》第七条、第八条：

| 条件 | 本公司情况 | 适用路径 |
|------|------------|----------|
| CIIO | 否 | — |
| ≥100万 PI | 否（85万） | — |
| ≥1万敏感PI | **是**（8千 < 1万？） | 需进一步判定 |

**判定结果**：根据《促进和规范数据跨境流动规定》第七条："非关键信息基础设施运营者...自当年1月1日起累计向境外提供10万人以上个人信息或者1万人以上敏感个人信息的，应当申报数据出境安全评估。"

本公司敏感个人信息累计8千人，未达到1万人阈值；个人信息累计85万人，达到10万人阈值但未达到100万人阈值。

**结论**：适用**个人信息出境标准合同**路径。

### Step 4: PIPIA要求
依据《个人信息出境标准合同备案指南（第二版）》要求，使用标准合同向境外提供个人信息前，应当完成个人信息保护影响评估。

**PIPIA需额外关注**（依据备案指南）：
1. 个人信息出境的必要性
2. 接收方的数据保护能力
3. 数据出境后的风险分析
```

---

## Anti-Patterns: What to Avoid

### ❌ Anti-Pattern 1: Summarizing Without Source

```markdown
根据相关法律规定，我们需要保护用户隐私。
```

**Problem**: "相关法律规定" is meaningless without specificity.

### ❌ Anti-Pattern 2: Unsupported Conclusions

```markdown
本APP的数据收集是必要的。
```

**Problem**: No analysis, no citation, no reasoning chain.

### ❌ Anti-Pattern 3: Copying Law Without Application

```markdown
《个人信息保护法》第五条规定："处理个人信息应当遵循合法、正当、必要和诚信原则..."
（然后没有任何分析，直接跳到下一个法律条文）
```

**Problem**: Quoting law is good, but must APPLY it to the specific processing activity.

### ✅ Correct Pattern: Quote → Analyze → Conclude

```markdown
《个人信息保护法》第五条规定："处理个人信息应当遵循合法、正当、必要和诚信原则，不得通过误导、欺诈、胁迫等方式处理个人信息。"

本APP在用户注册环节：
- **合法性分析**：处理基于用户明确同意（§13①），符合合法性要求
- **正当性分析**：收集手机号用于账户安全和身份验证，目的正当
- **必要性分析**：对照《常见类型App必要个人信息范围规定》§5，即时通信类APP必要信息仅为"注册用户移动电话号码"，本APP仅收集手机号，符合必要性要求
- **诚信原则**：隐私政策明确告知，无误导、欺诈行为

**结论**：本APP注册环节个人信息处理符合《个人信息保护法》第五条规定的处理原则。
```