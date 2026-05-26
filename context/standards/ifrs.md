# IFRS — Julgamentos Críticos por Processo

Distilação dos julgamentos contábeis de maior risco de auditoria por processo. Foco em pontos onde o auditor interno precisa avaliar adequação do reconhecimento, mensuração e disclosure — não reprodução integral das normas.

Subseção ao final cobre diferenças relevantes CPC vs. IFRS para contexto brasileiro.

---

## 1. IFRS 15 — Receita de Contratos com Clientes (Processo: REV, OTC)

### 5 Etapas do modelo de reconhecimento

| Etapa | Questão de auditoria |
|---|---|
| **1. Identificar o contrato** | Há aprovação e comprometimento das partes? Pagamento é provável? |
| **2. Identificar as obrigações de desempenho** | Existem bens/serviços distintos que devem ser contabilizados separadamente? (bundling, licenças + suporte, serviços de instalação) |
| **3. Determinar o preço da transação** | Há componente variável (descontos, bônus, reembolsos)? Como foi estimado? Existe componente de financiamento significativo? |
| **4. Alocar o preço** | Preço standalone de cada obrigação foi determinado por método adequado (observable, adjusted market, residual)? |
| **5. Reconhecer receita** | Obrigação satisfeita ao longo do tempo ou em momento específico? Critérios corretos aplicados? |

### Julgamentos de maior risco

| Risco | Indicadores de alerta |
|---|---|
| Reconhecimento antecipado (cut-off) | Receita reconhecida antes da transferência de controle; pressão de metas no fechamento de período |
| Estimativa de variável consideration | Constrained revenue não aplicada; reversão provável não considerada |
| Contrato com múltiplas obrigações | Receita alocada integralmente ao primeiro bem entregue sem separar serviços futuros |
| Bill-and-hold | Critérios de separação física e substancial não atendidos |
| Right of return | Passivo de reembolso e ativo de recuperação não reconhecidos |

### Diferença CPC 47 vs. IFRS 15

Normas convergidas — sem diferença conceitual material. CPC 47 = IFRS 15 traduzido com adaptações de terminologia.

---

## 2. IFRS 16 — Arrendamentos (Processo: FA, P2P, contratos)

### Classificação e reconhecimento (perspectiva arrendatário)

| Ponto | Critério |
|---|---|
| **Identificar arrendamento** | Contrato contém arrendamento se: (1) ativo identificado; (2) arrendatário controla o uso pelo prazo | 
| **Isenções práticas** | Arrendamento de curto prazo (≤12 meses) e ativo de baixo valor podem ser registrados como despesa linear — mas a isenção deve ser aplicada consistentemente por classe |
| **Prazo do arrendamento** | Inclui período não cancelável + opções com certeza razoável de exercício |
| **Taxa de desconto** | Taxa implícita do contrato; se não obtida, usar taxa incremental de empréstimo do arrendatário |

### Julgamentos de maior risco

| Risco | Indicadores de alerta |
|---|---|
| Classificação incorreta como serviço | Contrato com ativo identificado e controle do uso registrado como OpEx — subavaliação de passivo |
| Prazo subestimado | Opções de renovação com evidência de exercício ignoradas — ativo e passivo de arrendamento menores que o correto |
| Taxa de desconto inadequada | Taxa usada não reflete risco de crédito e moeda do arrendatário — distorce mensuração inicial |
| Remensuração não feita | Modificação contratual ou renegociação sem ajuste do ativo e passivo |

### Diferença CPC 06 (R2) vs. IFRS 16

Normas convergidas — sem diferença conceitual. CPC 06 (R2) = IFRS 16 com adaptações de terminologia.

---

## 3. IFRS 9 — Instrumentos Financeiros (Processo: TRE, OTC)

### Classificação de ativos financeiros

| Categoria | Critério | Mensuração |
|---|---|---|
| Amortized Cost | Modelo de negócio: hold to collect; fluxos de caixa SPPI (apenas principal e juros) | Custo amortizado; ECL (perdas esperadas) |
| FVOCI | Hold to collect and sell; fluxos SPPI | Fair value; ganhos/perdas em OCI |
| FVTPL | Qualquer outro caso; ou opção de FV | Fair value; ganhos/perdas no resultado |

### ECL — Expected Credit Loss (maior risco em contas a receber, OTC)

| Estágio | Condição | Reconhecimento de perda |
|---|---|---|
| Stage 1 | Sem aumento significativo de risco desde o reconhecimento | 12-month ECL |
| Stage 2 | Aumento significativo de risco de crédito | Lifetime ECL |
| Stage 3 | Evidência objetiva de impairment | Lifetime ECL; juros sobre valor líquido |

### Julgamentos de maior risco

| Risco | Indicadores de alerta |
|---|---|
| Classificação incorreta de instrumento | Derivativo não reconhecido como FVTPL; instrumento híbrido não separado |
| ECL subestimado | PD/LGD desatualizados; informações prospectivas (macro) ignoradas |
| Hedge accounting | Documentação formal ausente; inefetividade não reconhecida |

### Diferença CPC 48 vs. IFRS 9

Normas convergidas — sem diferença conceitual. CPC 48 = IFRS 9 com adaptações.

---

## 4. IAS 36 — Impairment de Ativos (Processo: FA, CAPEX, Goodwill)

### Indicadores de impairment (gatilhos de teste)

**Externos:**
- Queda de mercado significativa além do esperado
- Mudanças adversas tecnológicas, de mercado, legais ou econômicas
- Taxa de juros ou retorno de mercado aumentou (eleva a taxa de desconto)

**Internos:**
- Evidência de obsolescência ou dano físico
- Ativo ocioso, planos de descontinuação ou reestruturação
- Desempenho econômico pior do que esperado (capex-to-budget)

### Teste de impairment

```
Valor recuperável = max(Fair Value menos custo de venda, Valor em Uso)
Impairment = Valor contábil − Valor recuperável  (se positivo)
```

| Componente | Julgamento crítico |
|---|---|
| **Valor em Uso** | Taxa de desconto (WACC pré-tax); projeções de fluxo de caixa (período ≤5 anos + perpetuidade); taxa de crescimento na perpetuidade |
| **Fair Value** | Hierarquia de fair value (Level 1 > 2 > 3); premissas de mercado |
| **CGU (Cash Generating Unit)** | Agrupamento correto dos ativos — CGU muito grande dilui o impairment |

### Julgamentos de maior risco

| Risco | Indicadores de alerta |
|---|---|
| Teste não realizado quando indicador presente | Ativo ocioso ou com perda de receita sem revisão de carrying amount |
| WACC subestimado | Taxa de desconto abaixo do custo de capital real — superavalia valor em uso |
| Projeções otimistas sem base | Crescimento acima do histórico sem fundamentação |
| Goodwill não testado anualmente | Teste anual obrigatório independente de indicadores |

### Reversão de impairment

- Ativos individuais: reversão permitida se motivo do impairment reverteu (exceto Goodwill)
- **Goodwill: reversão proibida** (IAS 36.124)

---

## 5. IAS 37 — Provisões e Passivos Contingentes (Processo: LCT, TAX, RTR)

### Critérios de reconhecimento de provisão

Reconhecer provisão quando **todos** os critérios forem atendidos:
1. Obrigação presente (legal ou construtiva) como resultado de evento passado
2. Provável saída de recursos (>50%)
3. Estimativa confiável do valor

### Hierarquia de disclosure

| Classificação | Critério | Tratamento |
|---|---|---|
| **Provisão** | Saída provável + estimativa confiável | Reconhecer no balanço |
| **Passivo contingente** | Possível (não provável) OU provável mas sem estimativa | Divulgar em nota — não reconhecer |
| **Ativo contingente** | Entrada praticamente certa | Reconhecer; se apenas provável, divulgar |

### Julgamentos de maior risco

| Risco | Indicadores de alerta |
|---|---|
| Subprovisão em contingências fiscais | Classificar como "possível" processo que assessor jurídico avalia como "provável" |
| Provisão insuficiente para reestruturação | Plano formal não anunciado, reconhecimento antecipado indevido |
| Big bath provisioning | Constituição excessiva em período de perda para "limpar" exercícios futuros |

---

## 6. Diferenças CPC vs. IFRS — Resumo Relevante

| Tema | IFRS | CPC | Impacto |
|---|---|---|---|
| Subvenções governamentais | IAS 20 — redução do ativo ou receita diferida | CPC 07 (R1) — permite dedução do custo do ativo ou receita diferida | Diferença de apresentação; empresas brasileiras frequentemente deduzem do ativo (ex: créditos ICMS em FA) |
| Combinações de negócios — entidades sob controle comum | IFRS 3 não se aplica; sem orientação mandatória | CPC 15 (R1) — excluída; pronunciamento técnico ICPC 09 preenche parte | Transações intragrupo podem ter tratamentos distintos |
| Juros sobre capital próprio (JCP) | Não existe — distribuição é dividendo | Dedutível fiscalmente no Brasil; apresentado como despesa financeira ou dedução do PL | Diferença de apresentação do resultado; reconciliar com investidor estrangeiro |
| Estoques — custo de reposição para commodities | IFRS permite fair value para brokers/dealers | CPC 16 — segue IAS 2 sem essa exceção para todos | Diferença para entidades com estoques de commodities |
| Arrendamento de baixo valor | IFRS 16 — isenção disponível para qualquer empresa | CPC 06 (R2) — mesma isenção | Convergido |

---

## 7. Uso no internal-audit-ops

| Situação | Seção |
|---|---|
| Auditar ciclo de receita / OTC | Seção 1 — IFRS 15 julgamentos e red flags |
| Revisar contratos de arrendamento / IFRS 16 | Seção 2 — classificação, prazo, taxa de desconto |
| Testar provisão para devedores duvidosos / crédito | Seção 3 — ECL estágios e risco de subestimação |
| Avaliar impairment de imobilizado ou goodwill | Seção 4 — gatilhos, WACC, CGU, reversão |
| Auditar contingências tributárias / passivos | Seção 5 — IAS 37 critérios e classificação |
| Reconciliar com norma CPC aplicável | Seção 6 — tabela de diferenças |

**Referência cruzada:**
- `context/wcgw/revenue-recognition.md` — WCGWs IFRS 15
- `context/wcgw/fixed-assets.md` — WCGWs IAS 36 e IFRS 16
- `context/wcgw/treasury.md` — WCGWs IFRS 9
- `skills/contract-accounting-review.md` — análise de contratos com IFRS 16
