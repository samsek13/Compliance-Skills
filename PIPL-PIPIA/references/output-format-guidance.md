---
name: output-format-guidance
description: Standards for PIPIA report formatting and delivery
type: reference
---

# Output Format Guidance (输出格式指引)

This file defines the standards for PIPIA report formatting and delivery.

---

## Report Format

### Primary Output: Markdown (.md)

All PIPIA reports shall be delivered in **Markdown format** with the following standards:

#### File Naming Convention

```
PIPIA_[评估对象名称]_[日期YYYYMMDD].md

Examples:
- PIPIA_XX移动APP_20250403.md
- PIPIA_跨境电商平台用户数据出境_20250403.md
- PIPIA_人脸识别门禁系统_20250403.md
```

#### Markdown Formatting Standards

1. **Headers**: Use standard Markdown headers (#, ##, ###)
   - Title: `# 个人信息保护影响评估报告`
   - Major sections: `## 一、基本信息`
   - Subsections: `### 2.1 个人信息处理目的`

2. **Tables**: Use Markdown table syntax for data mapping, checklists, risk matrices
   ```markdown
   | 信息类型 | 是否敏感PI | 收集场景 |
   |----------|------------|----------|
   | 手机号 | 否 | 注册 |
   | 位置信息 | 是 | 导航 |
   ```

3. **Legal citations**: Use quote blocks for statutory text
   ```markdown
   根据《个人信息保护法》第五十五条规定：
   
   > "有下列情形之一的，个人信息处理者应当事前进行个人信息保护影响评估..."
   ```

4. **Lists**: Use bullet lists for enumerations, numbered lists for sequential steps

5. **Bold/Italic**: 
   - **Bold** for key terms, conclusions, status indicators (✅/⚠️/❌)
   - *Italic* for emphasis on specific points

---

## Document Structure Requirements

### Required Elements

Every PIPIA report must contain:

1. **Title header** with assessment object name
2. **Basic information section** (评估责任方、时间、人员)
3. **All 11 sections** per GB/T 39335-2020 template
4. **Legal citations** with exact quoted text for every legal requirement analysis
5. **Risk matrices** showing likelihood/impact/risk level
6. **Clear conclusion** stating assessment outcome

### Section Labels

Use Chinese section labels matching GB/T 39335:
- 一、二、三... for major sections (Chinese numerals)
- 2.1, 2.2... for subsections (Arabic numerals)

---

## Legal Citation Format

### Standard Citation Pattern

```markdown
根据《[法律名称]》第[条文号]条规定：

> "[引用原文]"

[分析内容]

**结论**：[基于分析的结论]
```

### Example

```markdown
根据《个人信息保护法》第二十八条规定：

> "敏感个人信息是一旦泄露或者非法使用，容易导致自然人的人格尊严受到侵害或者人身、财产安全受到危害的个人信息，包括生物识别、宗教信仰、特定身份、医疗健康、金融账户、行踪轨迹等信息..."

本APP收集的用户位置信息属于上述规定中的"行踪轨迹"类别，为敏感个人信息。

**结论**：用户位置信息为敏感个人信息，触发《个人信息保护法》第五十五条第一款规定的PIPIA要求。
```

### Citation Requirements

1. **Always cite article number**: "第X条" not just law name
2. **Always quote original text**: In Chinese, using quote block
3. **Cite from source file**: Reference the bundled law files, not memory
4. **Cite specific provision**: For articles with multiple items, cite "(一)"/"(二)" etc.

---

## Risk Matrix Format

### Standard Risk Matrix Table

```markdown
| 可能性等级 | 影响程度 | 风险等级 | 判定依据 |
|------------|----------|----------|----------|
| [等级] | [程度] | [最终等级] | GB/T 39335-2020附录D表D.X |
```

### Risk Level Indicators

Use visual indicators:
- **极高风险**: 🔴 需立即整改
- **高风险**: 🟠 需限期整改
- **中风险**: 🟡 建议整改
- **可接受**: 🟢 可继续进行

---

## Delivery Package Structure

### Standard Delivery

When delivering a completed PIPIA, provide:

```
[评估对象名称]_PIPIA交付包/
├── PIPIA_[名称]_[日期].md        (主报告)
├── 附录/
│   ├── 数据映射详细表.md         (详细数据映射)
│   ├── 风险评估工作表.md         (风险评估过程记录)
│   └── 法律引用汇总.md           (所有引用条文汇总)
└── 验证记录/
    ├── 验证差距报告_v1.md        (第一次验证结果)
    ├── 验证差距报告_v2.md        (修订后验证，如有)
    └── 验证最终确认.md           (最终验证通过确认)
```

### Minimal Delivery (When Time-Constrained)

Minimum deliverable:
- PIPIA_[名称]_[日期].md (主报告，包含所有必要章节)
- 验证差距报告_final.md (验证结果)

---

## Appendix: Sample Report Header

```markdown
# 个人信息保护影响评估报告

## 文档信息
- 文档编号：PIPIA-2025-XXX
- 版本：V1.0
- 创建日期：2025年XX月XX日
- 最后修订：2025年XX月XX日

## 基本信息
- 评估对象：[产品/服务/项目全称]
- 评估责任部门：[部门名称]
- 评估负责人：[姓名、职务]
- 参与评估人员：
  - [姓名] - [角色/职责]
  - [姓名] - [角色/职责]
- 评估时间：2025年XX月XX日 至 2025年XX月XX日

## 声明
本报告依据《中华人民共和国个人信息保护法》《信息安全技术 个人信息安全影响评估指南》(GB/T 39335-2020)及相关法律法规编制。报告中所有法律条文引用均来自原始法律文本，分析结论基于对法定要求的系统化对照评估。

---
[报告正文开始]
```

---

## Quality Checklist Before Delivery

Before delivering any PIPIA report, verify:

| Check Item | Requirement |
|------------|-------------|
| 所有法律引用有原文 | Each legal citation includes quoted text |
| 引用条文号准确 | Article numbers are correct per source files |
| 11章节完整 | All 11 sections per template present |
| 风险等级有判定依据 | Risk level references GB/T 39335 Appendix D |
| 结论明确 | Clear conclusion stating outcome |
| 验证已完成 | Independent verification executed |
| 验证差距已处理 | All verification gaps addressed or documented |

---

## Residual Gap Disclosure Format

If verification identifies gaps that cannot be fully remediated:

```markdown
## ⚠️ 验证披露

本报告经历了[X]次独立验证迭代。以下差距未能完全解决：

### 差距清单
| 差距# | 法律要求 | 差距描述 | 建议 |
|-------|----------|----------|------|
| 1 | [条文] | [差距] | [建议措施] |

### 建议
上述差距需由专业个人信息保护法律顾问或律师复核后再行使用。本报告不构成正式法律意见，仅供内部合规参考。
```