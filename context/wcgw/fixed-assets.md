---
processo: fixed-assets
nivel: 1
abreviacao: FA
subprocessos:
  - aquisicao-e-capitalizacao
  - inventario-e-controle-fisico
  - depreciacao-e-vida-util
  - impairment-e-reavaliacao
  - baixa-e-alienacao
assercoes_primarias:
  - existência
  - completude
  - valoração
  - apresentação
frameworks:
  - COSO
  - IAS 16
  - IAS 36
  - IAS 38
  - CPC 27
  - CPC 01
referencias:
  - _method-wiki/processes/entity-level-controls.md
  - _method-wiki/processes/fraud-risk-assessment.md
---

# WCGW — Fixed Assets (FA)

FA cobre o ciclo de vida do imobilizado e intangível — da aquisição à baixa. O risco central é duplo: **ativo fictício** (capitalizado mas inexistente) e **ativo superavaliado** (mantido por mais do que vale, sem reconhecimento de deterioração).

Imobilizado tende a ser relevante para empresas intensivas em capital (industrial, utilities, infraestrutura) e intangível é crítico em empresas de tecnologia, farmácia e pós-aquisição. Em ambos, julgamento contábil é alto — e o incentivo para inflar resultado usando o imobilizado é real.

---

## Subprocesso 1: Aquisição e Capitalização

Decisão de capitalizar ou lançar como despesa — gatilho de reconhecimento do ativo.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FA-001 | Despesa operacional capitalizada indevidamente para inflar ativo e melhorar resultado | Recording | Valoração | Alta |
| FA-002 | Ativo capitalizado sem aprovação formal do investimento (CAPEX não orçado) | Initiation | Existência | Alta |
| FA-003 | Custo de ativo inclui itens que deveriam ser lançados como despesa (manutenção, overhead) | Recording | Valoração | Alta |
| FA-004 | Ativo intangível gerado internamente capitalizado sem atender critérios do IAS 38 | Recording | Existência | Alta |
| FA-005 | Custo de obra em andamento (CIP) mantido indefinidamente sem transferência ao ativo final | Recording | Existência | Alta |
| FA-006 | Ativo adquirido de parte relacionada sem avaliação independente do valor justo | Initiation | Valoração | Alta |
| FA-007 | Múltiplos ativos adquiridos em lote sem alocação individual de custo | Recording | Valoração | Média |

**Controles típicos que mitigam:**
- política de capitalização com critérios claros: valor mínimo, vida útil mínima, natureza do gasto
- aprovação formal de CAPEX por alçada antes da aquisição
- revisão mensal de CIP com análise de itens acima de X meses sem transferência
- segregação entre quem requisita o CAPEX e quem aprova
- avaliação independente para transações com partes relacionadas acima de threshold
- revisão de despesas de manutenção e reparo acima de threshold para verificar capitalização indevida

---

## Subprocesso 2: Inventário e Controle Físico

Garantia de que o ativo registrado existe fisicamente e está onde o sistema diz.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FA-008 | Ativo registrado no sistema mas inexistente fisicamente — imobilizado fictício | Processing | Existência | Crítico |
| FA-009 | Ativo físico existente mas não registrado — imobilizado off-balance | Processing | Completude | Alta |
| FA-010 | Inventário físico não realizado periodicamente — sistema e realidade divergem sem detecção | Processing | Existência | Alta |
| FA-011 | Inventário realizado pela própria equipe que controla o registro — sem verificação independente | Processing | Existência | Alta |
| FA-012 | Ativo transferido entre locais ou áreas sem atualização no sistema — localização incorreta | Recording | Apresentação | Média |
| FA-013 | Ativo dado em garantia (penhor, alienação fiduciária) sem nota de divulgação | Reporting | Apresentação | Alta |

**Controles típicos que mitigam:**
- inventário físico periódico (anual para todos, semestral para ativos de alto valor) com conciliação contra o sistema
- inventário conduzido por equipe independente da custódia e do registro contábil
- processo formal de transferência de ativo entre áreas com atualização sistêmica
- levantamento de ativos em garantia junto ao jurídico antes do fechamento para divulgação

---

## Subprocesso 3: Depreciação e Vida Útil

Cálculo e aplicação sistemática da depreciação — impacto direto no resultado e na posição patrimonial.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FA-014 | Vida útil definida sem base técnica documentada — estimativa arbitrária | Processing | Valoração | Alta |
| FA-015 | Método de depreciação alterado sem justificativa ou divulgação — mudança de estimativa oculta | Recording | Apresentação | Alta |
| FA-016 | Ativo totalmente depreciado ainda em uso sem análise de valor residual ou extensão de vida útil | Processing | Valoração | Média |
| FA-017 | Depreciação calculada sobre base incorreta (custo bruto vs. custo líquido de subsídio ou grant) | Processing | Valoração | Alta |
| FA-018 | Ativo adquirido próximo ao fechamento com depreciação iniciada no período errado — problema de corte | Recording | Corte | Média |
| FA-019 | Revisão periódica de vida útil não realizada — estimativas desatualizadas por anos | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- política de vida útil por categoria de ativo com base técnica documentada (laudo de engenharia ou referência setorial)
- revisão anual de estimativas de vida útil com documentação de conclusão
- análise de ativos totalmente depreciados ainda em uso com decisão documentada
- cálculo de depreciação gerado pelo sistema (não manualmente) com validação periódica dos parâmetros
- controle de corte: depreciação inicia no mês seguinte à entrada em operação ou no mês de aquisição conforme política

---

## Subprocesso 4: Impairment e Reavaliação

Avaliação da recuperabilidade do ativo — risco de manter ativo superavaliado no balanço.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FA-020 | Teste de impairment não realizado quando há indicador de perda de valor (IAS 36) | Processing | Valoração | Alta |
| FA-021 | Indicadores de impairment não monitorados — gestão não identifica gatilhos formalmente | Initiation | Existência | Alta |
| FA-022 | Valor em uso calculado com premissas otimistas não suportadas — impairment subavaliado | Processing | Valoração | Alta |
| FA-023 | Unidade geradora de caixa (UGC) definida de forma ampla para diluir impairment | Processing | Valoração | Alta |
| FA-024 | Reversão de impairment reconhecida sem base em recuperação real dos fluxos (exceto goodwill) | Recording | Valoração | Alta |
| FA-025 | Reavaliação de ativos realizada sem laudo de avaliador independente qualificado | Processing | Valoração | Alta |
| FA-026 | Reavaliação aplicada seletivamente — apenas ativos que melhoram o balanço reavaliados | Processing | Apresentação | Alta |

**Controles típicos que mitigam:**
- processo anual de identificação de indicadores de impairment com documentação por UGC
- teste de impairment formal com premissas revisadas por independente (mínimo goodwill e intangível com vida indefinida)
- premissas de valor em uso confrontadas com plano de negócios aprovado pelo conselho
- reavaliação aplicada à classe inteira de ativos, não seletivamente
- avaliação por perito independente com qualificação reconhecida

**Flag de risco elevado:** empresas em processo de venda ou captação — forte incentivo para manter ativos superavaliados e evitar reconhecer impairment.

---

## Subprocesso 5: Baixa e Alienação

Desreconhecimento do ativo e reconhecimento do resultado da alienação.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| FA-027 | Ativo alienado mas mantido no registro contábil — ativo fictício no balanço | Recording | Existência | Alta |
| FA-028 | Ganho ou perda na alienação calculado incorretamente — valor contábil residual errado | Processing | Valoração | Alta |
| FA-029 | Alienação de ativo relevante sem aprovação formal por alçada competente | Initiation | Existência | Alta |
| FA-030 | Ativo alienado para parte relacionada por valor abaixo do mercado — benefício indevido | Processing | Valoração | Alta |
| FA-031 | Sucateamento de ativo sem laudo técnico — baixa sem evidência de inutilidade | Recording | Existência | Média |
| FA-032 | Baixa de ativo sem comunicação ao setor de seguros — cobertura mantida em ativo inexistente | Processing | Existência | Média |

**Controles típicos que mitigam:**
- aprovação formal de alienação e sucateamento por alçada definida com base no valor contábil
- laudo técnico para sucateamento de ativos com valor acima de threshold
- processo de baixa no sistema integrado ao inventário físico — baixa contábil e física simultâneas
- avaliação de ativos alienados para partes relacionadas por avaliador independente
- notificação ao setor de seguros e jurídico imediatamente após alienação ou baixa

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Despesa capitalizada indevidamente | Aquisição | FA-001, FA-003 |
| CAPEX não aprovado formalmente | Aquisição | FA-002, FA-006 |
| CIP sem transferência — ativo eterno | Aquisição | FA-005 |
| Ativo fictício — inexistente fisicamente | Inventário | FA-008, FA-010 |
| Vida útil sem base técnica | Depreciação | FA-014, FA-019 |
| Impairment não testado | Impairment | FA-020, FA-021 |
| Premissas otimistas — impairment baixo | Impairment | FA-022, FA-023 |
| Alienação para parte relacionada | Baixa | FA-030 |
| Ativo alienado mantido no registro | Baixa | FA-027 |
