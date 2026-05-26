# skill: financial-risk-to-action

## Goal

Priorizar riscos, achados, RCMs ou narrativas de processo pela lente de valor econômico e converter essa priorização em resposta executiva: ação corretiva, quick win, automação, revisão de governança ou monitoramento.

A skill não substitui `risk-scoring.md`, `finding-rating.md` ou julgamento técnico de auditoria. Ela adiciona uma camada de decisão para responder: **onde há potencial real de perda evitável, captura financeira, redução de custo ou melhora de capital de giro?**

## Use When

- CRO, CFO, comitê ou gestão pedir foco em economia de custos, impacto financeiro ou captura de valor
- narrativa de processo trouxer muitos riscos e for preciso escolher onde concentrar auditoria ou remediação
- achados tiverem severidade parecida, mas potencial financeiro diferente
- plano de ação precisar demonstrar racional econômico, não apenas conformidade
- programa de trabalho precisar separar quick wins de correções estruturais
- riscos operacionais precisarem ser traduzidos para linguagem executiva-financeira

## Quando NÃO usar

- quando o objetivo for apenas conformidade normativa sem tese econômica relevante
- quando não houver insumo mínimo sobre processo, volume, valor, frequência ou mecanismo de impacto
- para inflar severidade de achado sem evidência de perda, exposição ou oportunidade capturável
- para substituir materialidade, apetite de risco ou thresholds aprovados pelo cliente

## Inputs

- narrativa, walkthrough, RCM, lista de riscos ou achado
- processo auditado e período coberto
- dados de volume, valor, frequência, carteira, contratos ou transações, se disponíveis
- thresholds financeiros do engagement (`skills/risk-scoring.md`), se definidos
- apetite de risco ou prioridades da CRO/CFO, se documentados
- controles existentes e evidências de operação, se houver

Se faltarem dados quantitativos, classifique o potencial financeiro como **qualitativo** e sinalize a lacuna. Não invente valor.

---

## Parte 1 - Classificar o Mecanismo Econômico

Identifique como o risco se transforma em efeito econômico. Um risco pode ter mais de um mecanismo, mas use o principal para priorização.

| Mecanismo | Pergunta-chave | Exemplos |
|---|---|---|
| Perda de receita | A empresa deixa de faturar ou reconhecer algo devido? | clientes não faturados, valores zerados, reajuste não aplicado |
| Leakage comercial | A empresa concede benefício, desconto ou condição sem governança? | desconto manual, abatimento indevido, exceção comercial sem alçada |
| Custo evitável | A empresa incorre custo que poderia ser reduzido sem perder capacidade? | retrabalho, multa de fornecedor, processamento manual recorrente |
| Pagamento indevido | A empresa paga mais do que deveria ou paga sem base válida? | duplicidade, taxa incorreta, contrato divergente |
| Multa ou penalidade | Há risco de desembolso por lei, contrato ou SLA? | multa regulatória, penalidade contratual, juros |
| Capital de giro | O risco afeta prazo de recebimento, caixa ou necessidade de financiamento? | atraso de faturamento, cobrança contestada, medição pendente |
| Custo de não qualidade | Falha gera correção, atendimento, reprocessamento ou perda operacional? | contestação recorrente, retrabalho de nota, conciliação manual |
| Exposição contábil | Há risco de erro em receita, provisão, competência ou classificação? | faturamento em período errado, receita reconhecida sem base |

## Parte 2 - Avaliar Capturabilidade

Nem todo impacto financeiro vira captura. Avalie se a organização consegue transformar a remediação em ganho, perda evitada ou redução mensurável.

| Dimensão | Alto | Médio | Baixo |
|---|---|---|---|
| Mensurabilidade | Base de cálculo clara e rastreável | Estimativa possível com premissas | Sem base confiável no momento |
| Controle de gestão | Ação depende da área auditada ou poucas áreas | Depende de mais de uma diretoria | Depende de fornecedor, cliente ou evento externo dominante |
| Tempo de captura | 0-90 dias | 90-180 dias | acima de 180 dias |
| Evidência disponível | Dados transacionais ou relatório confiável | Amostra ou evidência parcial | Apenas relato ou hipótese |
| Sustentabilidade | Correção entra no processo ou sistema | Correção depende de rotina manual | Correção pontual, sem prevenção clara |

### Score de capturabilidade

Use julgamento simples:

| Score | Critério |
|---|---|
| 5 | Captura provável, mensurável e rápida |
| 4 | Captura provável, com dependência gerenciável |
| 3 | Captura plausível, mas exige validação ou projeto |
| 2 | Captura incerta ou predominantemente qualitativa |
| 1 | Baixa captura; foco pode ser compliance, governança ou monitoramento |

## Parte 3 - Prioridade Executiva

Combine magnitude financeira com capturabilidade. Se `risk-scoring.md` já trouxe impacto/probabilidade, use esse resultado como base, mas não confunda severidade de risco com oportunidade financeira.

| Prioridade | Condição típica | Resposta esperada |
|---|---|---|
| P1 - Captura imediata | impacto alto + capturabilidade 4-5 | plano de ação executivo, owner, data e métrica financeira |
| P2 - Valor relevante | impacto moderado/alto + capturabilidade 3-4 | remediação planejada e business case leve |
| P3 - Eficiência operacional | impacto baixo/moderado + ganho por escala ou recorrência | quick win, padronização ou automação simples |
| P4 - Governança necessária | valor incerto, mas risco de controle relevante | ação de governança, alçada, trilha de evidência |
| P5 - Monitorar | baixo valor e baixa capturabilidade | registrar, acompanhar em ciclo futuro |

### Regras de desempate

- Priorize perdas recorrentes sobre eventos isolados, salvo materialidade individual relevante.
- Priorize falhas já observadas sobre riscos apenas hipotéticos.
- Priorize ações que alteram sistema, alçada ou rotina preventiva sobre ações apenas educativas.
- Quando dois riscos têm valor parecido, escolha o que melhora evidência, rastreabilidade ou capital de giro.
- Não rebaixe risco regulatório, fraude ou contábil material só porque a captura financeira é baixa.

## Parte 4 - Traduzir para Plano de Ação Orientado a Valor

O plano deve explicar **como a ação captura valor ou evita perda**. Use o DoD de plano de ação em `_method-wiki/checklists/audit-artifacts-definition-of-done.md`.

| Tipo de resposta | Quando usar | Exemplo |
|---|---|---|
| Quick win | Ajuste simples, baixo esforço, captura rápida | reconciliação mensal de clientes não faturados |
| Controle preventivo | Falha nasce antes da transação | bloqueio sistêmico para desconto sem aprovação |
| Controle detectivo | Falha precisa ser detectada após processamento | relatório de exceções de faturamento zerado |
| Automação | Processo manual recorrente gera erro ou custo | workflow de aprovação de descontos |
| Governança de alçada | Decisão financeira sem owner ou aprovação | matriz de alçadas para concessões comerciais |
| Revisão contratual | Valor depende de cláusula, reajuste, multa ou taxa | checklist de IPCA e taxa de continuidade |
| Projeto estrutural | Correção exige sistema, dados ou várias áreas | saneamento de base migrada entre sistema origem e ERP |
| Monitoramento | Valor incerto, mas tema deve permanecer visível | KPI de faturamento pendente e aging |

## Output Format

### 1. Tese executiva

Parágrafo curto respondendo:
- onde está o maior potencial econômico
- qual mecanismo gera perda, economia ou captura
- qual ação deve ser priorizada primeiro

### 2. Ranking financeiro

| Prioridade | Risco / achado | Mecanismo econômico | Sinal de valor | Capturabilidade | Resposta recomendada | Lacuna de dados |
|---|---|---|---|---|---|---|

### 3. Planos de ação orientados a valor

| Risco / achado | Ação | Owner sugerido | Prazo sugerido | Critério de conclusão | Evidência esperada | Métrica de valor |
|---|---|---|---|---|---|---|

### 4. Dados necessários para quantificar

Liste apenas dados úteis para transformar a priorização qualitativa em estimativa financeira:
- população ou volume afetado
- valor médio por transação, contrato ou cliente
- frequência de exceções
- aging, período ou recorrência
- evidência de cobrança, pagamento, contestação ou ajuste

## Guardrails

- Separar economia real, perda evitada, recuperação potencial e melhoria de controle.
- Não chamar de "ganho" o que é apenas regularização contábil sem efeito de caixa.
- Não estimar R$ sem base explícita, premissa documentada ou faixa assumida pelo usuário.
- Não transformar oportunidade financeira em achado se a condição não foi evidenciada.
- Se o ganho depender de mudança de comportamento da gestão ou do cliente, registrar como dependência.
- Quando houver risco contábil ou regulatório, preservar a análise técnica mesmo que a captura financeira pareça pequena.

## Example - Faturamento

| Prioridade | Risco | Mecanismo econômico | Resposta |
|---|---|---|---|
| P1 | clientes não faturados no mês | perda de receita + capital de giro | reconciliação mensal entre sistema origem, ERP e carteira ativa |
| P1 | valores importados zerados na migração | perda de receita + exposição contábil | saneamento de base migrada e relatório de faturamento zerado |
| P2 | descontos aplicados pela mesma pessoa que fatura | leakage comercial | alçada formal + revisão independente de faturas ajustadas |
| P2 | aceite PJ >15 veículos sem evidência | capital de giro + contestação | workflow de medição com aceite rastreável antes da emissão |
| P3 | taxa de continuidade sem comunicação padronizada | perda de receita ou cobrança indevida | confirmação formal Comercial -> Faturamento antes da cobrança |
