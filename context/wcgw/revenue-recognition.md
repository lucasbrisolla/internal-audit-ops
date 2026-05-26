---
processo: revenue-recognition
nivel: 1
abreviacao: REV
subprocessos:
  - identificacao-de-contrato
  - obrigacoes-de-performance
  - preco-da-transacao
  - alocacao-do-preco
  - reconhecimento-e-cutoff
  - modificacoes-contratuais
  - receita-variavel-e-contraprestacao
  - apresentacao-e-divulgacao
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - IFRS 15
  - CPC 47
  - COSO
  - SOX
referencias:
  - context/wcgw/order-to-cash.md
  - context/wcgw/record-to-report.md
  - context/wcgw/legal-compliance-third-parties.md
  - context/wcgw/fraud-risk-assessment.md
---

# WCGW — Revenue Recognition / Contratos com Clientes (REV)

Revenue Recognition cobre o julgamento contábil sobre quando e por quanto reconhecer receita. OTC cobre a execução comercial e operacional do ciclo de venda; Revenue Recognition cobre a aderência da receita ao contrato, às obrigações de performance, ao preço da transação e à transferência de controle.

O risco central é reconhecer receita cedo demais, tarde demais, pelo valor errado ou com classificação inadequada. Em contratos complexos, a nota fiscal pode estar correta operacionalmente e ainda assim a receita estar errada contabilmente.

---

## Subprocesso 1: Identificação de Contrato

Etapa de avaliar se existe contrato com cliente, direitos e obrigações aprovados, substância comercial e probabilidade de recebimento.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| REV-001 | Receita reconhecida sem contrato aprovado ou evidência de acordo com o cliente | Initiation | Existência | Alta |
| REV-002 | Contrato verbal, carta de intenção ou proposta tratada como contrato executável sem critérios atendidos | Initiation | Existência | Alta |
| REV-003 | Contrato com cliente sem avaliação de capacidade e intenção de pagamento | Initiation | Existência | Média |
| REV-004 | Direitos e obrigações das partes não identificados antes do início do reconhecimento de receita | Initiation | Completude | Alta |
| REV-005 | Contrato sem substância comercial usado para gerar receita artificial | Initiation | Existência | Alta |
| REV-006 | Cancelamento ou direito de rescisão ignorado na avaliação de existência do contrato | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- checklist IFRS 15 / CPC 47 para existência de contrato
- aprovação formal de contrato antes de faturamento ou reconhecimento
- análise de crédito e intenção de pagamento para novos clientes
- revisão jurídica/contábil de contratos não padronizados
- bloqueio de reconhecimento para propostas, LOIs ou minutas não assinadas

**Flag de risco elevado:** receita reconhecida com base em pedido, e-mail comercial ou minuta ainda não assinada.

---

## Subprocesso 2: Obrigações de Performance

Etapa de identificar bens ou serviços prometidos, separáveis ou combinados, e determinar se cada obrigação é distinta.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| REV-007 | Obrigações de performance distintas combinadas indevidamente — receita reconhecida no timing errado | Processing | Valoração | Alta |
| REV-008 | Bens ou serviços prometidos implicitamente não identificados no contrato | Processing | Completude | Alta |
| REV-009 | Serviço de implementação, suporte, manutenção ou garantia tratado incorretamente como obrigação não separada | Processing | Apresentação | Alta |
| REV-010 | Licença, assinatura ou acesso contínuo tratado como venda pontual | Processing | Corte | Alta |
| REV-011 | Garantia de serviço ou performance confundida com garantia padrão de qualidade | Processing | Valoração | Média |
| REV-012 | Bundle comercial vendido como pacote único sem análise de componentes contábeis separados | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- matriz de obrigações de performance por tipo de contrato/produto
- revisão contábil de contratos com múltiplos elementos
- envolvimento de jurídico, comercial e contabilidade na leitura dos compromissos
- política clara para implementação, suporte, manutenção, garantia e licença
- documentação da conclusão sobre obrigação distinta ou não distinta

**Armadilha comum:** usar descrição comercial do pacote como se ela definisse a unidade contábil de receita.

---

## Subprocesso 3: Preço da Transação

Etapa de determinar o valor de contraprestação esperado, incluindo componentes fixos, variáveis, financiamento significativo, contraprestação não monetária e valores pagos ao cliente.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| REV-013 | Receita reconhecida pelo valor bruto sem considerar descontos, rebates, bônus ou penalidades prováveis | Recording | Valoração | Alta |
| REV-014 | Componente de financiamento significativo não identificado em contrato com prazo de pagamento alongado | Recording | Valoração | Média |
| REV-015 | Contraprestação variável estimada sem base histórica ou metodologia documentada | Processing | Valoração | Alta |
| REV-016 | Restrição de receita variável não aplicada quando há alta incerteza de reversão | Processing | Valoração | Alta |
| REV-017 | Valor pago ou a pagar ao cliente tratado como despesa quando deveria reduzir receita | Recording | Apresentação | Alta |
| REV-018 | Receita em moeda estrangeira mensurada sem considerar taxa, data ou cláusula cambial correta | Recording | Valoração | Média |

**Controles típicos que mitigam:**
- checklist de componentes do preço da transação
- revisão de descontos, rebates, bônus e penalidades contratuais
- modelo documentado para estimativa de contraprestação variável
- aprovação contábil para contratos com pagamento alongado ou moeda estrangeira
- conciliação entre contrato, faturamento, contas a receber e receita reconhecida

**Flag de risco elevado:** contrato com meta, bônus, clawback, rebate ou penalidade relevante.

---

## Subprocesso 4: Alocação do Preço

Etapa de alocar o preço da transação às obrigações de performance com base em preço de venda individual ou estimativa apropriada.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| REV-019 | Preço total do contrato não alocado entre obrigações de performance distintas | Recording | Valoração | Alta |
| REV-020 | Standalone selling price estimado sem base observável ou metodologia consistente | Processing | Valoração | Alta |
| REV-021 | Desconto contratual alocado integralmente a uma obrigação sem evidência de que pertence apenas a ela | Processing | Valoração | Média |
| REV-022 | Modificação de preço não realocada entre obrigações remanescentes quando requerido | Processing | Valoração | Alta |
| REV-023 | Receita de bundle reconhecida conforme faturamento, ignorando alocação contábil | Recording | Corte | Alta |

**Controles típicos que mitigam:**
- tabela de preços de venda individuais por produto/serviço
- metodologia aprovada para estimativa de SSP
- revisão de contratos com múltiplas obrigações
- conciliação entre cronograma de faturamento e cronograma de reconhecimento
- análise de descontos relevantes por componente

---

## Subprocesso 5: Reconhecimento e Cut-off

Etapa de reconhecer receita quando ou à medida que a obrigação de performance é satisfeita, no ponto no tempo ou ao longo do tempo.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| REV-024 | Receita reconhecida antes da transferência de controle ao cliente | Recording | Corte | Alta |
| REV-025 | Receita reconhecida tarde demais, após obrigação de performance já satisfeita | Recording | Completude | Média |
| REV-026 | Critério over-time aplicado sem atender requisitos de reconhecimento ao longo do tempo | Processing | Existência | Alta |
| REV-027 | Medição de progresso over-time baseada em input/output não confiável | Processing | Valoração | Alta |
| REV-028 | Receita de serviço recorrente reconhecida upfront em vez de ao longo do período de serviço | Recording | Corte | Alta |
| REV-029 | Bill-and-hold reconhecido sem cumprir critérios específicos | Recording | Existência | Alta |
| REV-030 | Cut-off de receita no fechamento não considera entrega, aceite, instalação ou transferência de risco | Recording | Corte | Alta |

**Controles típicos que mitigam:**
- política de reconhecimento por tipo de produto/serviço
- evidência de transferência de controle antes do reconhecimento
- revisão de contratos over-time e metodologia de progresso
- teste de cut-off com pedido, entrega, aceite, NF e contrato
- aprovação contábil para bill-and-hold, aceite formal ou entrega parcial

**Relação com OTC:** OTC pode confirmar entrega/faturamento; REV determina se isso basta para reconhecer receita.

---

## Subprocesso 6: Modificações Contratuais

Etapa de avaliar aditivos, change orders, renegociações, extensão de prazo, alteração de escopo, preço ou direitos do cliente.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| REV-031 | Aditivo contratual não avaliado para tratamento como contrato separado ou modificação do contrato existente | Processing | Apresentação | Alta |
| REV-032 | Change order reconhecido como receita antes de aprovação pelo cliente | Recording | Existência | Alta |
| REV-033 | Alteração de escopo sem revisão das obrigações de performance remanescentes | Processing | Completude | Alta |
| REV-034 | Renegociação de preço tratada apenas como desconto comercial sem ajuste contábil adequado | Processing | Valoração | Média |
| REV-035 | Cancelamento parcial ou redução de escopo não refletidos no cronograma de receita | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- revisão contábil obrigatória para aditivos e change orders
- bloqueio de receita para alterações não aprovadas pelo cliente
- atualização do memo IFRS 15/CPC 47 após modificação relevante
- conciliação entre contrato vigente, aditivos, faturamento e receita acumulada
- comunicação formal entre jurídico, comercial, PMO e contabilidade

**Flag de risco elevado:** obra, implantação, projeto customizado ou contrato longo com muitos aditivos.

---

## Subprocesso 7: Receita Variável e Contraprestação

Etapa de monitorar volume rebates, bônus, penalidades, SLA, devoluções, direito de retorno, price protection, royalties e estimativas de reversão.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| REV-036 | Provisão para devoluções ou direito de retorno não reconhecida | Recording | Completude | Alta |
| REV-037 | Rebates ou bônus por volume estimados com dados incompletos de vendas acumuladas | Processing | Valoração | Alta |
| REV-038 | Penalidades por SLA ou atraso não consideradas na receita líquida | Processing | Valoração | Alta |
| REV-039 | Receita de royalties reconhecida sem respeitar restrição de sales/usage-based royalties | Recording | Corte | Alta |
| REV-040 | Price protection ou cláusula de ajuste futuro ignorada na estimativa de receita | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- modelo de estimativa para devoluções, rebates e penalidades
- comparação entre estimativa e realização histórica
- revisão de contratos com cláusulas de variável
- integração entre dados de vendas, contratos e provisões
- aprovação de premissas por contabilidade e negócio

**Armadilha crítica:** estimativa de receita variável sempre otimista e sem backtesting.

---

## Subprocesso 8: Apresentação e Divulgação

Etapa de classificação, apresentação, disclosure e reconciliação de saldos de contrato, receita diferida, ativos contratuais e passivos contratuais.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| REV-041 | Receita bruta e líquida apresentadas sem avaliar papel de principal vs agente | Reporting | Apresentação | Alta |
| REV-042 | Ativo contratual, recebível e receita diferida classificados incorretamente | Reporting | Apresentação | Alta |
| REV-043 | Passivo contratual não reconhecido para recebimento antecipado de cliente | Recording | Completude | Alta |
| REV-044 | Disclosure de políticas de receita genérico e não aderente aos contratos reais da empresa | Reporting | Apresentação | Média |
| REV-045 | Saldos de contrato não reconciliados entre receita, AR, faturamento e deferred revenue | Reporting | Completude | Alta |
| REV-046 | Julgamentos significativos de reconhecimento de receita não divulgados | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- matriz de principal vs agente
- conciliação de contract assets, receivables e contract liabilities
- revisão de receita diferida e adiantamentos de clientes
- disclosure checklist IFRS 15/CPC 47
- revisão de políticas contábeis contra contratos reais e práticas operacionais

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Receita sem contrato válido | Identificação de contrato | REV-001, REV-002, REV-005 |
| Obrigações de performance mal identificadas | Obrigações | REV-007, REV-009, REV-012 |
| Receita variável superestimada | Preço, Variável | REV-015, REV-016, REV-037 |
| Bundle reconhecido pelo faturamento | Alocação | REV-019, REV-023 |
| Receita antecipada / cut-off | Reconhecimento | REV-024, REV-028, REV-030 |
| Change order sem aprovação | Modificações | REV-032, REV-035 |
| Devoluções, rebates ou SLA ignorados | Variável | REV-036, REV-038, REV-040 |
| Principal vs agente incorreto | Apresentação | REV-041 |
| Receita diferida/passivo contratual incompleto | Apresentação | REV-043, REV-045 |
