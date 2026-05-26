---
processo: journal-entry-testing
nivel: 1
abreviacao: JE
subprocessos:
  - populacao-e-integridade
  - selecao-baseada-em-risco
  - execucao-e-evidenciacao
  - management-override
assercoes_primarias:
  - existência
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - SOX
  - NBC TA 240
referencias:
  - _method-wiki/processes/journal-entry-testing.md
  - _method-wiki/heuristics/audit-bias-and-judgment-calibration.md
---

# WCGW — Journal Entry Testing (JE)

JE testing responde ao **risco presumido de management override** — o risco de que a gestão manipule lançamentos contábeis para distorcer o resultado ou a posição financeira. Diferente de outros testes, o risco aqui não é erro inadvertido: é manipulação intencional por quem tem poder de autorizar lançamentos.

O ponto de partida não é "quais JEs parecem estranhos" — é "onde a gestão tem incentivo, oportunidade e como poderia racionalizar a manipulação".

---

## Subprocesso 1: População e Integridade da Base

Antes de selecionar qualquer JE, a base precisa ser completa e precisa. Testar sobre base incompleta invalida qualquer conclusão.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| JE-001 | Base de JE incompleta — lançamentos excluídos antes de chegar ao auditor | Initiation | Completude | Alta |
| JE-002 | Base não inclui lançamentos pós-fechamento (post-closing entries) | Initiation | Corte | Alta |
| JE-003 | Base não inclui lançamentos de consolidação ou eliminação intercompany | Initiation | Completude | Alta |
| JE-004 | Base gerada pelo próprio responsável pelos lançamentos — IPE sem validação | Recording | Completude | Alta |
| JE-005 | Período da base não cobre o exercício completo — lacuna de cobertura | Initiation | Completude | Média |

**Controles típicos que mitigam:**
- tie-out da base de JE contra o razão geral (total de débitos e créditos)
- solicitação da base diretamente do ERP, não via relatório preparado pela gestão
- confirmação de que lançamentos pós-fechamento e de consolidação estão incluídos
- validação de completude por período: contagem de JEs por mês contra expectativa

**Conceito-chave:** qualquer base de JE recebida do cliente é IPE. Validar antes de selecionar.

---

## Subprocesso 2: Seleção Baseada em Risco

A seleção deve ser intencional e documentada — cada recorte precisa ter racional de risco claro.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| JE-006 | Seleção puramente aleatória sem ponderação por risco — alta chance de não cobrir override | Processing | Existência | Alta |
| JE-007 | Recorte de "lançamentos incomuns" sem definição objetiva do que é incomum | Processing | Existência | Alta |
| JE-008 | Lançamentos de fim de período excluídos da seleção — onde override é mais provável | Processing | Corte | Alta |
| JE-009 | Lançamentos manuais não priorizados — foco apenas em lançamentos automáticos | Processing | Existência | Alta |
| JE-010 | Usuários com acesso privilegiado ou incomum não segmentados na seleção | Processing | Existência | Alta |
| JE-011 | Combinações de contas incomuns (débito em conta de resultado × crédito em passivo) não capturadas | Processing | Apresentação | Média |
| JE-012 | Seleção documentada sem racional — "selecionamos por julgamento" sem explicar o julgamento | Processing | — | Média |

**Atributos de maior risco a priorizar:**
- lançamentos de fim de período e pós-fechamento
- lançamentos manuais (source = manual no ERP)
- preparadores com volume anômalo ou incomum
- contas de resultado com contrapartida em balanço sem racional claro
- lançamentos abaixo de threshold de aprovação (risco de fracionamento intencional)
- lançamentos em contas de difícil verificação (provisões, estimativas, intercompany)

---

## Subprocesso 3: Execução e Evidenciação

Para cada JE selecionado, o teste deve responder: esse lançamento tem justificativa de negócio válida, foi autorizado por quem deveria e está corretamente contabilizado?

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| JE-013 | JE sem suporte documental — lançamento sem evidência de origem | Processing | Existência | Alta |
| JE-014 | JE aprovado por usuário sem alçada para aquela conta ou valor | Processing | Existência | Alta |
| JE-015 | JE com justificativa vaga ou circular ("ajuste de fechamento") sem detalhamento | Processing | Existência | Alta |
| JE-016 | Contabilização inconsistente com a natureza da transação descrita | Processing | Valoração | Alta |
| JE-017 | JE lançado no período errado — manipulação de corte | Recording | Corte | Crítico |
| JE-018 | JE revertido logo após fechamento sem explicação — indício de manipulação | Reporting | Existência | Crítico |
| JE-019 | Mesmo usuário prepara e aprova o lançamento — ausência de revisão independente | Processing | Existência | Alta |

**Evidências a solicitar por JE testado:**
- justificativa de negócio (memo, e-mail, solicitação de ajuste)
- aprovação documentada (trilha no ERP ou assinatura)
- suporte da transação subjacente (contrato, NF, cálculo, conciliação)
- coerência entre data do lançamento e período de competência

---

## Subprocesso 4: Management Override

O risco presumido de override é específico: a gestão tem poder de contornar controles existentes. Testes de JE devem ser calibrados para capturar esse risco, não apenas irregularidades operacionais.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| JE-020 | Gestão lança ajustes de fim de período para atingir metas — revenue smoothing | Processing | Existência | Alta |
| JE-021 | Provisões ou estimativas ajustadas para melhorar resultado sem evidência técnica | Processing | Valoração | Alta |
| JE-022 | Receita antecipada via lançamento manual sem base contratual | Recording | Corte | Alta |
| JE-023 | Despesas diferidas ou capitalizadas sem critério contábil claro | Recording | Valoração | Alta |
| JE-024 | Transações intercompany usadas para transferir resultados entre entidades | Processing | Existência | Alta |
| JE-025 | Lançamentos de contrapartida em contas de baixa visibilidade (provisões genéricas, outros passivos) | Recording | Apresentação | Alta |
| JE-026 | Série de pequenos ajustes abaixo do threshold de aprovação que somados são relevantes | Processing | Valoração | Alta |

**Sinais de risco elevado de override:**
- pressão por resultado documentada (metas agressivas, bônus atrelado a lucro)
- empresa em processo de venda, IPO ou captação
- gestão centralizadora com pouca tolerância a questionamentos
- histórico de ajustes recorrentes de fim de período
- CFO ou controller com acesso irrestrito ao ERP sem revisão independente

**Armadilha crítica:** testar JE como rotina mecânica sem conectar cada recorte ao cenário específico de override relevante para aquela empresa. O teste de JE deve ser personalizado — não um procedimento padrão aplicado igualmente em todo engagement.

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Base incompleta / IPE não validada | População | JE-001, JE-004 |
| Seleção não cobre onde override ocorre | Seleção | JE-006, JE-008, JE-009 |
| Lançamento sem justificativa ou aprovação | Execução | JE-013, JE-014, JE-019 |
| Revenue smoothing / manipulação de resultado | Override | JE-020, JE-021, JE-022 |
| Fracionamento abaixo de threshold | Seleção, Override | JE-012, JE-026 |
| Reversão pós-fechamento como indício | Execução | JE-018 |
