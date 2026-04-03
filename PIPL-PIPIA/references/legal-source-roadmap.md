---
name: legal-source-roadmap
description: Decision tree for which laws apply to different PIPIA scenarios
type: reference
---

# Legal Source Roadmap (法律法规使用指引)

Different PIPIA scenarios require different legal sources. Use this roadmap to determine which laws apply.

## Quick Decision Table

| PIPIA Scenario | Primary Sources | Supporting Sources | Key Provisions |
|----------------|-----------------|-------------------|----------------|
| **General PIPIA** | PIPL, GB/T 39335-2020 | 网络数据安全管理条例 | PIPL §55-56, GB/T 39335 §5 |
| **Cross-border Transfer** | PIPL, 促进和规范数据跨境流动规定 | 数据出境安全评估办法, 个人信息出境认证办法, 个人信息出境标准合同备案指南 | PIPL §38-43, 跨境规定 §5-8 |
| **Processing Sensitive PI** | PIPL §28-32 | 人脸识别技术应用安全管理办法 | PIPL §28 (definition), §29-32 (requirements) |
| **Processing Children's PI** | PIPL, 儿童个人信息网络保护规定 | 未成年人网络保护条例 | PIPL §32, 儿童规定全文 |
| **App/Internet Services** | PIPL, 电信和互联网用户个人信息保护规定 | App违法违规收集使用个人信息行为认定方法, 常见类型App必要个人信息范围规定 | 电信规定 §8-12, App认定方法 |
| **Industrial/Telecom Sector** | 工业和信息化领域数据安全管理办法 | 工信领域数据安全风险评估实施细则, 工信领域数据安全事件应急预案 | 管理办法 §13-25, 实施细则 §5-6 |
| **Automated Decision-making** | PIPL §24, 网络数据安全管理条例 | 互联网信息服务算法推荐管理规定 | PIPL §24, 算法规定 §6-14 |
| **GBA Cross-border** | 粤港澳大湾区个人信息跨境流动标准合同实施指引 | 标准合同、承诺书模板 | 实施指引 §4-5 (PIPIA requirements) |

---

## Primary Sources (Mandatory Reading for ALL PIPIA)

| File | Content | Scope | When to Use |
|------|---------|-------|-------------|
| `GB∕T39335-2020 个人信息安全影响评估指南.md` | PIPIA Methodology Standard | Full assessment methodology, workflow, risk analysis framework | **ALL PIPIA drafting** - this defines the structure and process |
| `laws/中华人民共和国个人信息保护法_中国人大网.md` | PIPL (个人信息保护法) | §§1-74 | Legal basis for PIPIA, processing rules, rights, obligations |

---

## Cross-Border Data Transfer Laws (跨境传输法律)

**Read these when PIPIA involves cross-border transfer of personal information:**

| File | Content | Key Articles | When Required |
|------|---------|--------------|---------------|
| `laws/促进和规范数据跨境流动规定.md` | Cross-border Data Flow Regulation | §5 (exemptions), §7-8 (thresholds) | **ALWAYS** for cross-border PIPIA - determines which pathway applies |
| `laws/数据出境安全评估办法 网信办.md` | Data Export Security Assessment | §2-5 (trigger conditions) | When CII operator, or ≥100万 PI / ≥1万 sensitive PI to foreign |
| `laws/个人信息出境认证办法.md` | PI Export Certification | §5-6 (thresholds, PIPIA content) | When 10万-100万 PI / <1万 sensitive PI (non-CII) |
| `laws/个人信息出境标准合同备案指南（第二版）.md` | Standard Contract Filing Guide | Contract template, filing process | When using standard contract pathway |
| `laws/数据出境安全评估申报指南（第三版）.md` | Data Export Assessment Filing Guide | Filing process, self-assessment template | When filing for security assessment |
| `laws/粤港澳大湾区（内地、香港）个人信息跨境流动标准合同实施指引.md` | GBA Standard Contract Implementation | §4-5 (PIPIA requirements) | When transferring PI within Guangdong-Hong Kong-Macao Greater Bay Area |
| `laws/数据出境安全管理政策问答（2025年4月）.md` | Policy Q&A (Apr 2025) | Practical guidance | For clarification on cross-border rules |
| `laws/数据出境安全管理政策问答（2025年5月）.md` | Policy Q&A (May 2025) | Practical guidance | For clarification on cross-border rules |
| `laws/数据出境安全管理政策问答（2025年10月）.md` | Policy Q&A (Oct 2025) | Practical guidance | For clarification on cross-border rules |

---

## Sector-Specific Laws (行业特定法律)

**Read these when PIPIA involves specific sectors or data types:**

| File | Content | Key Articles | When Required |
|------|---------|--------------|---------------|
| `laws/工业和信息化领域数据安全管理办法（试行）.md` | Industry & IT Data Security Measures | §13-25 (lifecycle management) | When processing industrial/telecom/radio data |
| `laws/工业和信息化领域数据安全风险评估实施细则（试行）.md` | Industry Data Security Risk Assessment | §5-6 (assessment content) | For important/core data in industrial/telecom sector |
| `laws/工业和信息化领域数据安全事件应急预案(试行).md` | Industry Data Security Incident Response | Event classification, response procedures | For incident-related PIPIA in industrial/telecom sector |
| `laws/常见类型移动互联网应用程序必要个人信息范围规定-中共中央网络安全和信息化委员会办公室.md` | App Necessary PI Scope | §5 (39 app types) | **MANDATORY** when assessing mobile app PI collection necessity |
| `laws/电信和互联网用户个人信息保护规定-工信部.md` | Telecom & Internet User PI Protection | §8-13 (collection, security measures) | When processing PI in telecom/internet services |
| `laws/人脸识别技术应用安全管理办法.md` | Face Recognition Security | Processing requirements | When processing facial recognition biometric data |

---

## General Data Protection Laws (通用数据保护法律)

| File | Content | When Required |
|------|---------|---------------|
| `laws/网络安全法.md` | Cybersecurity Law | When assessing network security measures, CII operator obligations |
| `laws/中华人民共和国数据安全法_中国人大网.md` | Data Security Law | When assessing data classification, security protection measures |
| `laws/网络数据安全管理条例.md` | Network Data Security Regulation | Detailed processing rules, cross-border transfer, security measures |
| `laws/个人信息保护合规审计管理办法_中央网络安全和信息化委员会办公室.md` | PI Protection Compliance Audit Rules | When conducting compliance audits, audit requirements |

---

## Special Subject Protection (特殊主体保护)

| File | Content | When Required |
|------|---------|---------------|
| `laws/儿童个人信息网络保护规定 网信办.md` | Children's PI Protection Rules | **MANDATORY** when processing involves children under 14 |
| `laws/未成年人网络保护条例.md` | Minors Network Protection Regulation | When processing involves minors, special protection requirements |

---

## Compliance Assessment Tools (合规认定工具)

| File | Content | When Required |
|------|---------|---------------|
| `laws/App违法违规收集使用个人信息行为认定方法-中共中央网络安全和信息化委员会办公室.md` | App PI Collection Violation Identification | When assessing mobile app compliance, collection practices |

---

## Terminology Reference (术语参考)

| File | Content | When Required |
|------|---------|---------------|
| `laws/数据领域常用名词解释（第一批）.md` | Data Terms (Batch 1) | For understanding key terms: 数据, 数据处理, 数据安全, 隐私保护计算, etc. |
| `laws/数据领域常用名词解释（第二批）.md` | Data Terms (Batch 2) | For understanding key terms: 数据产权, 衍生数据, 可信数据空间, etc. |

---

## Usage Instructions

**All files contain Chinese legal text.** Use targeted reading:
- Search for specific article numbers (e.g., "第五十五条" for PIPIA requirements)
- Use Grep to find key terms before reading specific portions
- Read only the sections relevant to the current assessment

**Reading sequence for typical PIPIA:**
1. Start with Legal Source Roadmap table above to identify applicable laws
2. Always read PIPL §55-56 and GB/T 39335-2020 §5
3. Add cross-border laws if transfer abroad is involved
4. Add sector-specific laws based on industry
5. Add special subject laws if children/minors involved