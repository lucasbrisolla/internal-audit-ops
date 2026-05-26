# skill: risk-scoring

## Goal

Definir critérios de impacto e probabilidade calibrados ao cliente, calcular risco inerente e derivar risco residual a partir do resultado da avaliação de controle. Elimina subjetividade no enquadramento de riscos e garante consistência dentro do engagement.

## Use When

- início de um engagement — antes de pontuar qualquer risco
- rating de risco parece inconsistente entre riscos do mesmo processo
- cliente não tem critérios formais de impacto/probabilidade definidos
- necessidade de calcular risco residual a partir do RI e do resultado do controle
- revisão de matriz de risco produzida por terceiro

## Inputs

- contexto do cliente: porte, setor, volume de receita, número de contratos/transações
- escopo do engagement: processos cobertos, período
- resultado da avaliação de controles (`skills/control-evaluation.md`), se disponível
- matriz de risco existente, se houver

---

## Parte 1 — Escala de Impacto

### Dimensões de impacto

Avaliar impacto em **todas as dimensões relevantes** e usar a **maior** como classificação final.

| Dimensão | O que medir |
|---|---|
| Financeiro | Perda, receita não reconhecida, pagamento indevido, multa |
| Operacional | Volume de transações afetadas, interrupção de processo crítico |
| Compliance | Violação de norma, regulação ou cláusula contratual |
| Reputacional | Exposição ao cliente, imprensa, regulador ou conselho |

### Níveis de impacto — referência padrão

| Nível | Label | Financeiro (referência) | Operacional | Compliance / Reputacional |
|---|---|---|---|---|
| 1 | Baixo | Perda < 0,1% da receita ou valor imaterial | Impacto pontual, sem interrupção de processo | Irregularidade interna sem exposição externa |
| 2 | Moderado | 0,1% a 0,5% da receita | Afeta subprocesso, retrabalho relevante | Não conformidade com política interna |
| 3 | Significativo | 0,5% a 2% da receita | Afeta processo completo, atraso perceptível ao cliente | Violação de contrato ou norma interna relevante |
| 4 | Alto | > 2% da receita ou valor individualmente material | Interrupção de processo crítico ou perda de cliente | Violação regulatória, legal ou com risco de litígio |

**Calibração obrigatória por engagement:** substituir os percentuais por valores absolutos (R$) definidos com base na receita, materialidade ou limites operacionais do cliente antes de usar. Sem calibração, o enquadramento é subjetivo.

Exemplo de calibração para empresa com receita de R$ 50M:
- Baixo: < R$ 50 mil
- Moderado: R$ 50 mil – R$ 250 mil
- Significativo: R$ 250 mil – R$ 1 M
- Alto: > R$ 1 M

---

## Parte 2 — Escala de Probabilidade

| Nível | Label | Critério qualitativo | Frequência de referência |
|---|---|---|---|
| 1 | Improvável | Evento raro, sem histórico recente, requer combinação de falhas | Menos de 1x nos últimos 3 anos |
| 2 | Possível | Pode ocorrer em condições específicas, histórico esporádico | 1–2x por ano |
| 3 | Provável | Ocorre com regularidade, controle frágil ou ausente, histórico documentado | Mensal ou trimestral |
| 4 | Quase Certo | Ocorre frequentemente ou já está ocorrendo, falha sistêmica conhecida | Semanal ou contínuo |

---

## Parte 3 — Risco Inerente (Heat Map)

### Lógica da tabela

O score **não é multiplicação simples** de impacto × probabilidade. É uma tabela de lookup ranqueada onde cada combinação recebe uma prioridade de 1 a 16 baseada em julgamento de risco operacional.

**Por que não multiplicação?**
Multiplicação simples produz resultados simétricos: (3,2) = (2,3) = 6. A tabela abaixo é assimétrica por design — (3,2)=9 e (2,3)=10 são diferentes porque um evento de probabilidade mais alta (2,3) gera pressão operacional maior do que um evento de impacto mais alto mas menos frequente (3,2). Ambas as dimensões são consideradas com peso comparável; a ligeira assimetria reflete urgência operacional.

**Princípio de design:** alinhado à ABNT NBR 31000:2018 / ISO 31000:2018 — risco como função conjunta de consequência e probabilidade, sem fórmula obrigatória, com tabela aprovada pela equipe.

**Células em negrito** = observadas diretamente em dados reais. Demais células completam a tabela por consistência lógica.

| Impacto ↓ / Prob → | Improvável (1) | Possível (2) | Provável (3) | Quase Certo (4) |
|---|---|---|---|---|
| Baixo (1) | 1 | **3** | 5 | 7 |
| Moderado (2) | **2** | **6** | **10** | 12 |
| Significativo (3) | 4 | **9** | **13** | 15 |
| Alto (4) | 6 | 11 | 14 | **16** |

### Bandas de classificação do RI

| Score | Classificação | Lógica |
|---|---|---|
| 1–3 | **Baixo** | Impacto e probabilidade baixos — monitoramento suficiente |
| 4–9 | **Moderado** | Combinação mediana — controle básico requerido |
| 10–12 | **Alto** | Pelo menos uma dimensão alta — controle formal requerido |
| 13–15 | **Alto** | Ambas as dimensões altas — prioridade de remediação |
| 16 | **Crítico** | Máximo em ambas as dimensões — ação imediata |

### Regra de substituição

Esta tabela é o padrão metodológico fixo. Pode ser substituída por tabela oficial do cliente (aprovada por comitê de risco ou conselho) desde que documentada no `context/clients/*/index.md` antes do início do engagement. Sem substituição explícita, esta tabela prevalece.

---

## Parte 4 — Risco Residual

Risco residual = RI ajustado pelo resultado da avaliação do controle mitigador.

### Tabela de redução

| Resultado do controle (`control-evaluation.md`) | Redução de nível |
|---|---|
| Satisfatório (score ≥ 0,90) | Reduz **2 níveis** |
| Satisfatório com melhorias (score 0,75–0,89) | Reduz **1 nível** |
| Requer melhorias significativas (score 0,60–0,74) | Sem redução |
| Não satisfatório (score < 0,60) | Sem redução |
| A confirmar / não testado | Sem redução (conservador) |

### Regras de aplicação

- Nível mínimo de RR = Baixo (não vai abaixo de 1)
- Se múltiplos controles mitigam o mesmo risco, usar o **melhor** controle para a redução — não somar reduções
- Se o risco for **Crítico (16)** com controle Satisfatório, RR = Significativo — nunca Baixo diretamente
- Risco de fraude: redução máxima de 1 nível, independente do resultado do controle

### Exemplo

| Risco | RI | Controle | Score | RR |
|---|---|---|---|---|
| Desconto sem segregação | Alto (13) | FAT.04 — Não satisfatório | 0,45 | Alto (13) |
| Reajuste IPCA sem controle | Alto (10) | FAT.07 — Satisfatório | 0,92 | Moderado (6) |
| Faturamento em lote manual | Moderado (9) | FAT.03 — Satisfatório com melhorias | 0,78 | Baixo (3) |

---

## Parte 5 — Apetite de Risco

### Padrão metodológico fixo

Resposta mínima exigida por nível de RR — válida para qualquer engagement salvo substituição explícita documentada.

| Nível de RR | Resposta padrão | Prazo de remediação |
|---|---|---|
| Baixo | Monitorar — registrar, sem plano de ação imediato | Próximo ciclo de auditoria |
| Moderado | Recomendar melhoria — responsável e prazo definidos | 90–180 dias |
| Alto | Achado formal — plano de ação com owner e data | 30–90 dias |
| Crítico | Achado prioritário — escalada imediata para gestão sênior | Imediato / até 30 dias |

### Diferenciação por categoria (padrão fixo)

Tolerância diferente por natureza do risco — independe do cliente:

| Categoria | Tolerância máxima sem achado formal |
|---|---|
| Fraude | Baixo — qualquer risco acima de Baixo vira achado formal |
| Compliance / Regulatório | Moderado — Alto e Crítico viram achados prioritários |
| Operacional | Moderado — gestão pode aceitar com justificativa documentada |
| Governança / TI | Moderado — depende de criticidade sistêmica |

### Calibração por cliente (sobrescreve o padrão)

O cliente pode definir tolerâncias diferentes documentando em `context/clients/*/index.md`:
- thresholds financeiros específicos
- processos com tolerância zero (ex: faturamento, recebimento)
- processos com tolerância maior (ex: arquivo, suporte)
- nível de escalada (diretoria, CFO, comitê de auditoria, conselho)

Sem calibração documentada, o padrão acima prevalece.

---

## Decision Rules

- Calibrar thresholds financeiros no início do engagement — sem isso, o enquadramento não é comparável entre riscos
- Usar a dimensão de maior impacto, não a média entre dimensões
- Probabilidade deve refletir o ambiente de controle atual — se controle está ausente, probabilidade sobe
- Nunca ajustar RI para baixo por "intenção de melhoria" — pontuar o estado atual
- RR "A confirmar" = tratar como RI para fins de priorização
- Risco de fraude não reduz mais de 1 nível mesmo com controle Satisfatório

## Output Format

### 1. Parâmetros do engagement

| Parâmetro | Valor definido |
|---|---|
| Receita / base de referência | R$ X |
| Threshold Baixo | < R$ X |
| Threshold Moderado | R$ X – R$ Y |
| Threshold Significativo | R$ Y – R$ Z |
| Threshold Alto | > R$ Z |

### 2. Tabela de riscos pontuados

| Cód. | Risco | Impacto | Prob | RI | Controle | Score | RR | Ação |
|---|---|---|---|---|---|---|---|---|

### 3. Riscos acima do apetite

Lista de riscos com RR Significativo ou Alto — esses viram achados prioritários ou programa de trabalho focado.
