---
processo: order-to-cash
nivel: 1
abreviacao: OTC
subprocessos:
  - cadastro-de-cliente-e-credito
  - pedido-de-venda
  - entrega-e-transferencia-de-risco
  - faturamento
  - reconhecimento-de-receita
  - contas-a-receber-e-cobranca
  - recebimento-e-baixa
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - SOX
  - IFRS 15
  - CPC 47
referencias:
  - _method-wiki/patterns/revenue-billed-vs-unbilled-reconciliation.md
  - _method-wiki/processes/oar-and-business-understanding.md
  - _method-wiki/processes/fraud-risk-assessment.md
---

# WCGW — Order-to-Cash (OTC)

OTC cobre o ciclo completo desde o pedido do cliente até o recebimento do dinheiro. É o espelho do P2P — enquanto P2P controla o que sai, OTC controla o que entra.

O risco central é duplo: **reconhecimento indevido de receita** (mais dinheiro do que realmente ganhou) e **perda de receita legítima** (menos do que deveria receber). Ambos distorcem o resultado — um por excesso, outro por omissão.

O risco de fraude de receita é presumido pelo NBC TA 240 — deve ser avaliado em todo engagement.

---

## Subprocesso 1: Cadastro de Cliente e Crédito

Etapa de onboarding do cliente e definição do limite de crédito. Controla quem pode comprar a prazo e quanto.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| OTC-001 | Cliente cadastrado sem análise de crédito — risco de inadimplência não avaliado | Initiation | Existência | Alta |
| OTC-002 | Limite de crédito definido sem critério formal — aprovação por relação pessoal | Initiation | Existência | Alta |
| OTC-003 | Limite de crédito não revisado periodicamente — cliente com perfil deteriorado mantém limite antigo | Initiation | Valoração | Média |
| OTC-004 | Pedido aceito acima do limite de crédito sem aprovação formal de exceção | Processing | Existência | Alta |
| OTC-005 | Cliente fictício cadastrado para desvio de receita ou triangulação | Initiation | Existência | Crítico |
| OTC-006 | Cadastro de cliente permite alteração de dados bancários por usuário sem autorização | Processing | Existência | Alta |
| OTC-007 | Mesma pessoa cadastra cliente e aprova pedido — segregação quebrada | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- análise de crédito formal com score ou critério documentado antes de cadastrar
- aprovação do limite de crédito por função independente da área comercial
- revisão periódica de limites com base em histórico de pagamento e situação financeira
- bloqueio sistêmico de pedidos acima do limite sem aprovação de exceção
- segregação entre cadastro de cliente e aprovação de pedido

---

## Subprocesso 2: Pedido de Venda

Formalização e aprovação do pedido antes de iniciar entrega ou prestação de serviço.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| OTC-008 | Pedido aceito sem contrato ou ordem de compra formal — compromisso sem respaldo | Initiation | Existência | Alta |
| OTC-009 | Condições comerciais (preço, prazo, desconto) alteradas após aprovação sem nova aprovação | Processing | Valoração | Alta |
| OTC-010 | Desconto concedido acima da alçada do vendedor sem aprovação do gestor | Processing | Valoração | Alta |
| OTC-011 | Pedido duplicado — mesmo cliente, mesmo produto, mesmo período — risco de faturamento em dobro | Recording | Existência | Média |
| OTC-012 | Pedido aceito para cliente com restrição de crédito ativa — override sem registro | Processing | Existência | Alta |
| OTC-013 | Condições especiais (consignação, retorno garantido, venda condicional) tratadas como venda firme | Recording | Existência | Alta |

**Controles típicos que mitigam:**
- pedido vinculado obrigatoriamente a contrato ou OC do cliente no sistema
- tabela de alçadas de desconto com aprovação escalonada por nível
- log de alterações em pedido aprovado com nova aprovação obrigatória
- validação sistêmica de crédito no momento do pedido, não apenas no cadastro
- identificação de condições especiais no pedido com tratamento contábil diferenciado

**Flag de risco elevado:** vendas com cláusula de retorno garantido, consignação ou "direito de devolução" — receita só pode ser reconhecida quando o risco transfere de fato.

---

## Subprocesso 3: Entrega e Transferência de Risco

Etapa onde o bem é entregue ou o serviço é prestado — gatilho para reconhecimento de receita em contratos simples.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| OTC-014 | Receita reconhecida antes da entrega efetiva — faturamento antecipado | Recording | Corte | Alta |
| OTC-015 | Entrega registrada mas produto ainda em trânsito — transferência de risco não ocorreu | Recording | Existência | Alta |
| OTC-016 | Entrega parcial registrada como total — receita superavaliada | Recording | Valoração | Alta |
| OTC-017 | Critério de transferência de risco (FOB origem vs. destino) aplicado inconsistentemente | Recording | Corte | Alta |
| OTC-018 | Para serviços: percentual de conclusão estimado sem metodologia documentada | Processing | Valoração | Alta |
| OTC-019 | Devoluções de cliente não registradas ou registradas no período errado | Recording | Corte | Média |
| OTC-020 | Entrega registrada por quem tem interesse em atingir meta de volume — conflito de interesse | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- sistema registra entrega com base em romaneio ou confirmação de transportadora (não manualmente)
- critério de FOB formalizado em política e aplicado consistentemente
- metodologia de percentual de conclusão para serviços documentada e aprovada
- revisão de devoluções próximas ao fechamento com análise de corte
- segregação entre equipe comercial (que tem meta) e responsável pelo registro de entrega

---

## Subprocesso 4: Faturamento

Emissão da nota fiscal e registro do direito a receber.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| OTC-021 | NF emitida com valor diferente do pedido aprovado — faturamento a maior ou menor | Recording | Valoração | Alta |
| OTC-022 | NF emitida sem entrega correspondente — faturamento sem base | Recording | Existência | Alta |
| OTC-023 | NF duplicada — mesma operação faturada duas vezes | Recording | Existência | Alta |
| OTC-024 | NF emitida após fechamento mas receita reconhecida no período anterior — problema de corte | Recording | Corte | Alta |
| OTC-025 | Créditos a clientes (notas de crédito) não emitidos tempestivamente — passivo oculto | Recording | Completude | Média |
| OTC-026 | NF emitida para cliente diferente do pedido — erro ou fraude de direcionamento | Recording | Existência | Alta |

**Controles típicos que mitigam:**
- validação sistêmica de NF contra pedido aprovado e entrega registrada
- detecção de duplicatas por cliente + produto + valor + período
- revisão de NFs emitidas nos últimos dias do período para análise de corte
- processo formal de emissão de nota de crédito com aprovação e registro no período correto
- reconciliação entre NFs emitidas e receita reconhecida no razão

---

## Subprocesso 5: Reconhecimento de Receita

Etapa contábil de registro da receita — quando e quanto reconhecer. Risco mais alto em contratos complexos (múltiplos elementos, performance obligations, variáveis).

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| OTC-027 | Receita reconhecida no momento do faturamento sem análise de performance obligations (IFRS 15) | Recording | Corte | Alta |
| OTC-028 | Contrato com múltiplos elementos — alocação de preço entre obrigações sem metodologia | Processing | Valoração | Alta |
| OTC-029 | Receita variável (bônus, rebate, penalidade) reconhecida sem estimativa confiável | Processing | Valoração | Alta |
| OTC-030 | Receita de contrato de longo prazo reconhecida pelo método errado (ponto vs. ao longo do tempo) | Recording | Existência | Alta |
| OTC-031 | Receita a faturar (unbilled) acumulada sem reconciliação com razão — saldo não validado | Recording | Completude | Alta |
| OTC-032 | Reversão de receita reconhecida em período anterior sem ajuste retrospectivo adequado | Reporting | Apresentação | Alta |
| OTC-033 | Receita reconhecida em contratos com cliente em dificuldade financeira — coletabilidade duvidosa | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- análise formal de performance obligations por tipo de contrato com documentação
- metodologia de alocação de preço aprovada e aplicada consistentemente
- revisão de contratos novos e modificados para identificar implicações de IFRS 15
- reconciliação mensal de receita a faturar (unbilled) com razão e com contratos
- análise de coletabilidade antes de reconhecer receita de clientes com histórico de inadimplência

**Referência:** `_method-wiki/patterns/revenue-billed-vs-unbilled-reconciliation.md` — validação da amarração entre reconhecimento, faturamento e baixa do saldo.

---

## Subprocesso 6: Contas a Receber e Cobrança

Gestão do saldo de clientes após faturamento — acompanhamento, cobrança e provisão para devedores duvidosos.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| OTC-034 | Provisão para devedores duvidosos (PDD) calculada sem metodologia — subestimada para inflar ativo | Processing | Valoração | Alta |
| OTC-035 | Aging de recebíveis desatualizado ou não reconciliado com o razão | Processing | Completude | Alta |
| OTC-036 | Títulos vencidos há muito tempo mantidos em aberto sem análise — ativo fictício | Processing | Existência | Alta |
| OTC-037 | Baixa de crédito irrecuperável sem aprovação formal — perda não reconhecida | Processing | Valoração | Alta |
| OTC-038 | Crédito renegociado registrado como recebível normal sem ajuste de valor presente | Recording | Valoração | Média |
| OTC-039 | Cobrança repassada a terceiro (factoring, cessão) sem desreconhecimento adequado | Recording | Existência | Alta |
| OTC-040 | Concentração excessiva em poucos clientes sem análise de risco de crédito | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- metodologia de PDD formalizada (por aging, histórico de perdas ou análise individual)
- reconciliação mensal do aging com o razão de clientes
- processo de write-off com aprovação por alçada e documentação de esgotamento de cobrança
- análise periódica de títulos vencidos acima de X dias com decisão documentada
- avaliação de operações de factoring ou cessão para determinar desreconhecimento (IFRS 9)

---

## Subprocesso 7: Recebimento e Baixa

Etapa de entrada do dinheiro e baixa do recebível correspondente.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| OTC-041 | Recebimento não baixado no título correto — saldo de cliente incorreto | Recording | Existência | Média |
| OTC-042 | Recebimento desviado antes de ser registrado — dinheiro recebido mas não lançado | Processing | Existência | Alta |
| OTC-043 | Mesma pessoa recebe pagamento e realiza a baixa — segregação quebrada | Processing | Existência | Crítico |
| OTC-044 | Descontos ou abatimentos concedidos na baixa sem aprovação formal | Processing | Valoração | Alta |
| OTC-045 | Recebimento em conta bancária não monitorada ou não reconciliada | Processing | Completude | Alta |
| OTC-046 | Baixa de títulos sem recebimento correspondente — receita registrada sem entrada de caixa | Recording | Existência | Alta |

**Controles típicos que mitigam:**
- conciliação bancária diária com revisão independente
- segregação entre caixa (recebe) e contas a receber (baixa)
- aprovação formal para descontos ou abatimentos concedidos na liquidação
- reconciliação periódica de recebimentos × baixas × razão de clientes
- todas as contas bancárias da empresa incluídas na conciliação — nenhuma fora do processo

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Reconhecimento antecipado de receita | Entrega, Reconhecimento | OTC-014, OTC-027, OTC-030 |
| Faturamento sem entrega / base | Faturamento | OTC-022, OTC-023 |
| Receita variável sem estimativa | Reconhecimento | OTC-029 |
| PDD subestimada — ativo inflado | Contas a receber | OTC-034, OTC-036 |
| Desvio de recebimento | Recebimento | OTC-042, OTC-043 |
| Desconto/abatimento sem aprovação | Recebimento | OTC-044 |
| Contrato com múltiplos elementos | Reconhecimento | OTC-028 |
| Venda condicional tratada como firme | Pedido | OTC-013 |
