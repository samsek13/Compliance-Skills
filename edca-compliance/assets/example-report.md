# Example: EDCA Compliance Audit Report (Partial)

This is an example showing proper bilingual citations and risk-level organization. It demonstrates a hypothetical mobile gaming app audit.

---

## EDCA Compliance Audit Report

### Executive Summary

- **EDCA Applicability**: Applies - game is likely accessed by children/adolescents
- **Overall Compliance Status**: Partially Compliant with significant gaps
- **Key Risk Statistics**: 🔴 3 High | 🟡 5 Medium | 🟢 4 Low
- **Most Critical Findings**:
  1. Loot boxes present (Art. 20º violation)
  2. No parental supervision tools (Art. 17º violation)
  3. Profiling for ad targeting active (Art. 22º violation)
- **Compliance Score**: 42% (Poor)

---

### 1. EDCA Applicability Assessment (Art. 1º)

**Original Text (Portuguese)**:
> Art. 1º Esta Lei dispõe sobre a proteção de crianças e de adolescentes em ambientes digitais e aplica-se a todo produto ou serviço de tecnologia da informação direcionado a crianças e a adolescentes no País ou de acesso provável por eles...

**English Translation**:
> Art. 1º This Law provides for the protection of children and adolescents in digital environments and applies to any information technology product or service directed at children and adolescents in the Country or likely to be accessed by them...

| Criterion | Assessment | Result |
|-----------|------------|--------|
| Directed at children/adolescents | Game has cartoon graphics and PEGI 7 rating | Yes |
| Likely access - attractiveness | Colorful, simple gameplay appeals to children | Yes |
| Likely access - ease of use | Free download, intuitive touch controls | Yes |
| Likely access - risk degree | In-app purchases, social features present | Yes |

**Conclusion**: EDCA applies

---

### 3. Detailed Compliance Findings

#### 🔴 High Risk Findings

| # | Article | Issue | Legal Requirement | Current State | Gap | Recommendation |
|---|---------|-------|-------------------|---------------|-----|----------------|
| 1 | Art. 20º | Loot boxes offered | **Portuguese**: "São vedadas as caixas de recompensa... direcionados a crianças e a adolescentes"<br>**English**: "Loot boxes are prohibited in electronic games directed at children and adolescents" | Game offers "Mystery Boxes" purchasable with real money containing random virtual items | Direct violation | Remove loot box functionality immediately |
| 2 | Art. 17º | No parental supervision tools | **Portuguese**: "deverão... disponibilizar configurações e ferramentas acessíveis e fáceis de usar que apoiem a supervisão parental"<br>**English**: "must provide accessible and easy-to-use settings and tools that support parental supervision" | No parental controls exist | Missing mandatory feature | Implement parental supervision dashboard within 30 days |
| 3 | Art. 22º | Profiling for ad targeting | **Portuguese**: "é vedada a utilização de técnicas de perfilamento para direcionamento de publicidade comercial a crianças e a adolescentes"<br>**English**: "the use of profiling techniques for directing commercial advertising to children and adolescents is prohibited" | User behavior tracked for personalized ads | Direct violation | Disable behavioral profiling for users under 18 immediately |

#### 🟡 Medium Risk Findings

| # | Article | Issue | Legal Requirement | Current State | Gap | Recommendation |
|---|---------|-------|-------------------|---------------|-----|----------------|
| 1 | Art. 7º | Privacy settings not maximally protective by default | **Portuguese**: "garantir, por padrão, a configuração no modelo mais protetivo disponível"<br>**English**: "ensure, by default, the most protective available configuration" | Location sharing and push notifications enabled by default | Partial gap | Set all privacy settings to most protective by default |
| 2 | Art. 8º, IV | No anti-compulsive use features | **Portuguese**: "adotar por padrão configurações que evitem o uso compulsivo"<br>**English**: "adopt by default settings that prevent compulsive use" | No playtime limits or warnings | Missing feature | Implement usage time warnings and auto-pause |
| 3 | Art. 13º | Age data may be used for marketing | **Portuguese**: "utilizados unicamente para essa finalidade"<br>**English**: "used solely for that purpose" | Age verification data stored with marketing profile | Purpose limitation violation | Segregate age data from marketing systems |

#### 🟢 Low Risk Findings

| # | Article | Issue | Legal Requirement | Current State | Gap | Recommendation |
|---|---------|-------|-------------------|---------------|-----|----------------|
| 1 | Art. 31º | Transparency report not published | Required for >1M child users | Not yet required (under threshold) | N/A | Prepare for future requirement |

---

### 7. Penalty Risk Warning

**Original Text (Portuguese)**:
> Art. 35º... II - multa simples, de até 10% (dez por cento) do faturamento do grupo econômico no Brasil no seu último exercício...

**English Translation**:
> Art. 35º... II - simple fine, up to 10% (ten percent) of the economic group's revenue in Brazil in its last fiscal year...

Based on identified violations:
- **Art. 20º violation**: Potential fine + requirement to remove loot boxes
- **Art. 22º violation**: Potential fine up to 10% Brazilian revenue + prohibition order
- **Art. 17º violation**: Warning with 30-day correction period, escalating to fines

---

### Legal Disclaimer

> **⚠️ Legal Advice Disclaimer**: This guidance is informational and based on Lei nº 15.211/2025 (EDCA). It does not constitute legal advice. Consult a qualified Brazilian privacy lawyer for enforcement matters or complex compliance questions.