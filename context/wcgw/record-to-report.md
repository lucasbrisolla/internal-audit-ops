---
processo: record-to-report
nivel: 1
abreviacao: RTR
subprocessos:
  - reconciliacao-de-contas
  - lancamentos-manuais-de-fechamento
  - consolidacao-e-intercompany
  - elaboracao-das-demonstracoes
  - divulgacoes-e-notas-explicativas
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - SOX
  - IFRS
  - CPC
referencias:
  - _method-wiki/processes/journal-entry-testing.md
  - _method-wiki/processes/entity-level-controls.md
  - _method-wiki/processes/fraud-risk-assessment.md
---

# WCGW — Record-to-Report (RTR)

RTR cobre o ciclo de fechamento contábil — do registro das transações à publicação das demonstrações financeiras. O risco central é **distorção do reporte**: demonstrações que não representam fielmente a posição patrimonial e o resultado do período.

Diferente dos ciclos operacionais (P2P, OTC, H2R), o RTR é o ponto de convergência — erros e fraudes de qualquer processo chegam aqui. Um RTR fraco pode mascarar distorções introduzidas em outros ciclos.

O risco de fraude de reporte financeiro é presumido pelo NBC TA 240 e a pressão por resultado é o principal fator de incentivo.

---

## Subprocesso 1: Reconciliação de Contas Contábeis

Base da integridade do razão — garante que cada conta contábil tem saldo explicável e suportado por evidência.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| RTR-001 | Contas contábeis relevantes não reconciliadas ao fechamento — saldo não explicado | Processing | Completude | Alta |
| RTR-002 | Reconciliação preparada sem evidência de revisão independente — preparador = aprovador | Processing | Existência | Alta |
| RTR-003 | Itens reconciliantes antigos mantidos sem resolução — diferenças que nunca fecham | Processing | Existência | Alta |
| RTR-004 | Reconciliação realizada sobre saldo de relatório gerencial, não sobre o razão contábil | Processing | Valoração | Alta |
| RTR-005 | Contas intercompany não reconciliadas entre as partes — eliminação incorreta na consolidação | Processing | Existência | Alta |
| RTR-006 | Frequência de reconciliação inadequada ao risco da conta — conta de caixa reconciliada mensalmente | Processing | Completude | Alta |
| RTR-007 | Itens de break na reconciliação classificados como "diferença de timing" sem análise formal | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- política de reconciliação com frequência mínima por tipo de conta (diária para caixa, mensal para contas de patrimônio)
- revisão e aprovação por pessoa independente de quem preparou, com evidência documentada
- prazo máximo para resolução de itens reconciliantes com escalonamento acima de X dias
- reconciliação feita contra extrato do razão extraído do sistema, não contra relatório gerencial
- reconciliação intercompany com confirmação da contraparte antes do fechamento

---

## Subprocesso 2: Lançamentos Manuais de Fechamento

Ajustes contábeis realizados no fechamento — ponto de maior risco de fraude porque dependem de julgamento e acesso ao sistema.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| RTR-008 | Lançamento manual sem documentação de suporte — base do lançamento não verificável | Recording | Existência | Alta |
| RTR-009 | Lançamento aprovado pelo próprio preparador — sem segregação entre preparação e aprovação | Recording | Existência | Alta |
| RTR-010 | Lançamentos manuais concentrados no último dia do período sem explicação — padrão atípico | Recording | Existência | Alta |
| RTR-011 | Lançamento em conta incomum para o tipo de transação — natureza disfarçada | Recording | Apresentação | Alta |
| RTR-012 | Lançamentos reversivos de período anterior não monitorados — manipulação entre períodos | Recording | Corte | Alta |
| RTR-013 | Acesso ao módulo de lançamento manual não restrito — qualquer usuário pode lançar | Processing | Existência | Alta |
| RTR-014 | Lançamentos de estimativas (provisões, depreciação, amortização) calculados sem metodologia documentada | Recording | Valoração | Alta |
| RTR-015 | Variação significativa no volume de lançamentos manuais vs. período anterior sem investigação | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- todos os lançamentos manuais com documentação de suporte obrigatória (voucher, memória de cálculo, aprovação)
- segregação entre quem cria o lançamento e quem aprova — sistema impede autoapprovação
- relatório de lançamentos manuais por usuário revisado pelo Controller pós-fechamento
- acesso ao módulo de lançamento restrito a usuários autorizados com log completo
- teste de lançamentos manuais de alto risco como procedimento padrão (ver JET)

**Referência:** `_method-wiki/processes/journal-entry-testing.md` — processo específico de seleção e teste de lançamentos de risco elevado.

---

## Subprocesso 3: Consolidação e Intercompany

Agregação das demonstrações individuais e eliminação de transações entre entidades do grupo.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| RTR-016 | Escopo de consolidação desatualizado — entidade controlada não incluída | Recording | Completude | Alta |
| RTR-017 | Eliminação de receita intercompany não realizada — inflação de receita consolidada | Recording | Existência | Alta |
| RTR-018 | Eliminação de lucro não realizado em estoques ou ativos intercompany omitida | Recording | Valoração | Alta |
| RTR-019 | Diferenças de câmbio em conversão de subsidiárias estrangeiras tratadas incorretamente | Recording | Valoração | Alta |
| RTR-020 | Políticas contábeis inconsistentes entre entidades consolidadas — não harmonizadas | Processing | Apresentação | Alta |
| RTR-021 | Eliminações intercompany realizadas com saldos diferentes por cada parte — assimetria | Processing | Existência | Alta |
| RTR-022 | Goodwill de aquisição não testado para impairment anualmente (IAS 36) | Recording | Valoração | Alta |

**Controles típicos que mitigam:**
- mapa de consolidação atualizado com todas as entidades controladas e percentuais
- processo formal de match de saldos intercompany antes do fechamento com ambas as partes
- eliminações realizadas em sistema de consolidação (não manualmente) com trilha de auditoria
- política contábil do grupo aplicada por todas as entidades — diferenças documentadas
- teste anual de impairment de goodwill com metodologia e aprovação independente

---

## Subprocesso 4: Elaboração das Demonstrações Financeiras

Preparação das demonstrações e sua revisão antes da aprovação.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| RTR-023 | Demonstrações elaboradas sem comparação com período anterior — variações não explicadas | Reporting | Valoração | Alta |
| RTR-024 | Classificação incorreta entre circulante e não circulante — liquidez distorcida | Reporting | Apresentação | Alta |
| RTR-025 | Itens extraordinários ou não recorrentes classificados como operacionais — EBITDA superavaliado | Reporting | Apresentação | Alta |
| RTR-026 | Demonstração de fluxo de caixa não concilia com DRE e BP — inconsistência interna | Reporting | Completude | Alta |
| RTR-027 | Demonstrações aprovadas sem revisão formal do CFO ou equivalente — controle existe mas sem evidência | Reporting | Existência | Média |
| RTR-028 | Demonstrações finais divergem da versão revisada — alteração pós-aprovação sem rastreabilidade | Reporting | Existência | Alta |

**Controles típicos que mitigam:**
- análise analítica formal (horizontal e vertical) com explicação de variações acima de threshold
- checklist de classificação contábil para itens recorrentes de difícil julgamento
- revisão cruzada entre DRE, BP e DFC antes da aprovação
- aprovação formal das demonstrações pelo CFO com evidência documentada
- controle de versão das demonstrações — alterações pós-aprovação com novo processo formal

---

## Subprocesso 5: Divulgações e Notas Explicativas

Transparência das informações que acompanham as demonstrações — onde a omissão é tão arriscada quanto o erro nos números.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| RTR-029 | Contingências relevantes não divulgadas ou subdivulgadas — usuário não informado sobre risco | Reporting | Completude | Alta |
| RTR-030 | Transações com partes relacionadas não divulgadas adequadamente (CPC 05 / IAS 24) | Reporting | Completude | Alta |
| RTR-031 | Premissas e julgamentos significativos não descritos nas notas — estimativas sem transparência | Reporting | Apresentação | Alta |
| RTR-032 | Eventos subsequentes relevantes não avaliados entre data-base e emissão das demonstrações | Reporting | Completude | Alta |
| RTR-033 | Políticas contábeis descritas de forma genérica — não refletem práticas reais da empresa | Reporting | Apresentação | Média |
| RTR-034 | Divulgação de IFRS 16 (arrendamentos) incompleta — passivos de leasing subdivulgados | Reporting | Completude | Alta |
| RTR-035 | Notas não atualizadas — copiadas de período anterior sem revisão das alterações relevantes | Reporting | Existência | Média |

**Controles típicos que mitigam:**
- checklist de divulgações obrigatórias por norma aplicável (CPC/IFRS) revisado ao fechamento
- processo formal de levantamento de contingências com jurídico e aprovação de provisão
- identificação de partes relacionadas atualizada anualmente com declaração dos executivos
- revisão de eventos subsequentes até a data de emissão com documentação de conclusão
- revisão das notas explicativas por alguém diferente de quem as preparou

**Flag de risco elevado:** empresas com processos judiciais relevantes — risco de subdivulgação de contingências para não sinalizar fragilidade ao mercado ou credor.

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Reconciliação sem revisão independente | Reconciliação | RTR-002, RTR-003 |
| Lançamento manual sem suporte | Lançamentos | RTR-008, RTR-009 |
| Manipulação via lançamentos de fechamento | Lançamentos | RTR-010, RTR-012 |
| Eliminação intercompany omitida | Consolidação | RTR-017, RTR-018 |
| Escopo de consolidação incompleto | Consolidação | RTR-016 |
| Goodwill sem teste de impairment | Consolidação | RTR-022 |
| Classificação inadequada (EBITDA) | Demonstrações | RTR-025 |
| Contingências não divulgadas | Notas | RTR-029, RTR-032 |
| Partes relacionadas subdivulgadas | Notas | RTR-030 |
