---
name: pipia-report-template
description: Full PIPIA report structure per GB/T 39335-2020 Section 5.7
type: reference
---

# PIPIA Report Template (个人信息保护影响评估报告模板)

This template follows GB/T 39335-2020 Section 5.7 report structure. Use this as the output format for all PIPIA reports.

---

## Template Structure

```markdown
# 个人信息保护影响评估报告

## 一、基本信息
- 评估对象：[产品/服务/项目名称]
- 评估责任部门/人员：[名称]
- 评估时间：[日期]
- 参与评估人员：[名单]

## 二、评估对象描述
### 2.1 个人信息处理目的
[描述处理目的，引用PIPL第五条、第六条关于目的明确性、相关性的要求]

### 2.2 个人信息类型
[列举个人信息类型，标注敏感个人信息，引用PIPL第二十八条敏感个人信息定义]

### 2.3 处理方式
[描述收集、存储、使用等各环节]

### 2.4 处理规模
[涉及个人信息主体数量等]

### 2.5 相关方情况
[涉及的第三方及其角色]

## 三、数据映射分析
[按GB/T 39335-2020附录C表C.1、C.2格式]

## 四、合规性分析
### 4.1 处理合法性分析
[分析是否符合PIPL第十三条规定的合法性基础，逐项对照并引用原文]

### 4.2 处理必要性分析
[分析是否符合PIPL第五条、第六条关于必要性的要求；如涉及App，引用常见类型App必要个人信息范围规定]

### 4.3 告知同意分析
[分析是否符合PIPL第十七条、第二十九条等告知同意要求]

### 4.4 其他合规要点分析
[根据具体情况分析相关法律要求，引用对应的法律原文]

## 五、风险源识别
### 5.1 网络环境和技术措施
[按GB/T 39335-2020第5.4条a)项分析]

### 5.2 个人信息处理流程
[按GB/T 39335-2020第5.4条b)项分析]

### 5.3 参与人员与第三方
[按GB/T 39335-2020第5.4条c)项分析]

### 5.4 业务特点和规模及安全态势
[按GB/T 39335-2020第5.4条d)项分析]

## 六、个人权益影响分析
### 6.1 个人信息敏感程度分析
[按GB/T 39335-2020第5.5条分析]

### 6.2 处理活动特点分析
[分析对个人权益可能产生的影响]

### 6.3 影响程度判定
[按GB/T 39335-2020附录D表D.3、D.4判定影响程度]

## 七、安全风险综合分析
### 7.1 安全事件可能性分析
[按GB/T 39335-2020附录D表D.1、D.2判定可能性等级]

### 7.2 风险等级判定
[按GB/T 39335-2020附录D表D.5判定风险等级]

## 八、保护措施有效性分析
[分析已采取的措施是否合法、有效并与风险程度相适应，引用PIPL第五十一条]

## 九、风险处置建议
[针对识别的风险提出处置建议]

## 十、评估结论
[综合评估结论]

## 十一、附录
[相关支撑材料]
```

---

## Section-by-Section Guidance

### Section 1: 基本信息
Required fields. If information unavailable, note as "待补充" and flag for user.

### Section 2: 评估对象描述
Each subsection must cite relevant PIPL articles:
- 2.1 → PIPL §5-6 (目的明确性、相关性)
- 2.2 → PIPL §4 (个人信息定义), §28 (敏感个人信息定义)
- 2.3 → PIPL §4 (处理活动定义)
- 2.5 → PIPL §21-23 (委托处理、共同处理、提供)

### Section 3: 数据映射分析
Use GB/T 39335-2020 Appendix C tables:
- 表C.1: 个人信息类型列表
- 表C.2: 个人信息处理活动列表

Read GB/T 39335-2020 附录C before drafting this section.

### Section 4: 合规性分析
**Critical**: Each analysis point must quote the exact statutory text.

For 4.1, check against PIPL §13 seven legal bases:
```
（一）取得个人的同意；
（二）为订立、履行个人作为一方当事人的合同所必需...
（三）为履行法定职责或者法定义务所必需...
（四）为应对突发公共卫生事件或者紧急情况下为保护自然人的生命健康和财产安全所必需...
（五）为公共利益实施新闻报道、舆论监督等行为...
（六）依照本法规定在合理的范围内处理个人自行公开或者其他已经合法公开的个人信息...
（七）法律、行政法规规定的其他情形。
```

### Section 5: 风险源识别
Four dimensions per GB/T 39335-2020 §5.4:
- a) 网络环境和技术措施
- b) 个人信息处理流程
- c) 参与人员与第三方
- d) 业务特点和规模及安全态势

Read GB/T 39335-2020 §5.4 before analysis.

### Section 6: 个人权益影响分析
Four impact dimensions per GB/T 39335-2020 §5.5:
1. 限制个人自主决定权
2. 引发差别性待遇
3. 个人名誉受损或遭受精神压力
4. 人身财产受损

Use Appendix D 表D.3、D.4 for degree classification.

### Section 7: 安全风险综合分析
Combine likelihood + impact to determine risk level.
Use Appendix D 表D.1、D.2 (likelihood) and 表D.5 (risk matrix).

### Section 8: 保护措施有效性分析
Check against PIPL §51 obligations:
- 制定内部管理制度和操作规程
- 对个人信息实行分类管理
- 采取相应的加密、去标识化等安全技术措施
- 合理确定个人信息处理的操作权限
- 制定并组织实施个人信息安全事件应急预案
- 定期对从业人员进行安全教育和培训

### Section 9: 风险处置建议
Map to GB/T 39335-2020 §5.8 风险处置 options:
- 接受风险 (有合理理由且影响可接受)
- 降低风险 (采取额外保护措施)
- 规避风险 (停止或改变处理活动)
- 转移风险 (保险、合同分配等)

### Section 10: 评估结论
State clearly:
- Processing activity legality conclusion
- Risk level conclusion
- Whether protection measures are adequate
- Overall recommendation (可继续进行 / 需整改 / 应停止)

### Section 11: 附录
Include:
- Data mapping detailed tables
- Technical documentation excerpts
- Third party agreements summary
- Risk assessment worksheets