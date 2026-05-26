---
processo: supply-chain-logistics
nivel: 1
abreviacao: SCL
subprocessos:
  - planejamento-de-demanda-e-supply
  - fornecedores-criticos-e-capacidade
  - transporte-e-fretes
  - armazenagem-e-operadores-logisticos
  - importacao-exportacao-e-comercio-exterior
  - otif-sla-e-performance-logistica
  - avarias-perdas-e-sinistros
  - continuidade-e-resiliencia-da-cadeia
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - supply chain risk management
  - contract logistics
  - trade compliance
referencias:
  - context/wcgw/procure-to-pay.md
  - context/wcgw/inventory.md
  - context/wcgw/order-to-cash.md
  - context/wcgw/legal-compliance-third-parties.md
  - context/wcgw/esg-environment-health-safety.md
---

# WCGW — Supply Chain & Logistics (SCL)

Supply Chain & Logistics cobre o fluxo físico e coordenado de demanda, suprimento, transporte, armazenagem, operadores logísticos, comércio exterior e performance de entrega. P2P cobre comprar; Inventory cobre saldo e valoração de estoque; Supply Chain cobre se a cadeia consegue entregar o que foi planejado, no prazo, no custo e com risco controlado.

O risco central é a organização operar com planejamento ruim, dependência crítica, fretes mal controlados, armazenagem terceirizada sem visibilidade, importações/exportações com compliance fraco ou indicadores logísticos que escondem perdas e rupturas.

---

## Subprocesso 1: Planejamento de Demanda e Supply

Etapa de previsão de demanda, S&OP, plano de suprimento, capacidade, cobertura de estoque e alinhamento entre comercial, operações, compras e finanças.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| SCL-001 | Forecast de demanda preparado sem base em histórico, carteira, sazonalidade ou input comercial validado | Initiation | Valoração | Alta |
| SCL-002 | Plano de suprimento não reconciliado com capacidade produtiva, estoque disponível e lead time de fornecedores | Processing | Completude | Alta |
| SCL-003 | Alterações relevantes no plano de demanda não aprovadas ou comunicadas às áreas impactadas | Processing | Existência | Média |
| SCL-004 | Cobertura de estoque calculada com dados incompletos ou parâmetros desatualizados | Processing | Valoração | Média |
| SCL-005 | Rupturas recorrentes não analisadas por causa raiz | Processing | Completude | Média |
| SCL-006 | Plano S&OP usado para decisão sem conciliação com orçamento, vendas e produção | Reporting | Completude | Alta |

**Controles típicos que mitigam:**
- processo formal de S&OP com inputs de vendas, operações, compras e finanças
- comparação forecast x realizado com causa raiz
- revisão de cobertura de estoque e lead times críticos
- aprovação de mudanças relevantes no plano
- conciliação entre plano operacional e orçamento

**Flag de risco elevado:** forecast ajustado manualmente para bater meta comercial sem evidência de demanda real.

---

## Subprocesso 2: Fornecedores Críticos e Capacidade

Etapa de identificação, monitoramento e mitigação de dependência de fornecedores críticos, gargalos de capacidade, single source e riscos de continuidade.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| SCL-007 | Fornecedor crítico não identificado formalmente — dependência operacional invisível | Initiation | Completude | Alta |
| SCL-008 | Dependência de fornecedor single source sem plano de contingência | Processing | Existência | Alta |
| SCL-009 | Capacidade do fornecedor não avaliada antes de assumir compromisso comercial relevante | Processing | Existência | Alta |
| SCL-010 | Atrasos recorrentes de fornecedor crítico não escalados para plano de ação | Processing | Completude | Média |
| SCL-011 | Mudança de fornecedor crítico realizada sem homologação técnica, qualidade ou compliance | Initiation | Existência | Alta |
| SCL-012 | Risco geopolítico, climático, logístico ou financeiro de fornecedor crítico não monitorado | Processing | Completude | Média |

**Controles típicos que mitigam:**
- matriz de fornecedores críticos por impacto, substituibilidade e lead time
- plano de dual sourcing ou contingência para itens críticos
- homologação técnica e de qualidade antes de substituição
- scorecard de fornecedor com atraso, qualidade, capacidade e risco
- revisão periódica de riscos externos da cadeia

**Relação com P2P:** P2P avalia contratação e pagamento; Supply Chain avalia dependência, capacidade e continuidade operacional.

---

## Subprocesso 3: Transporte e Fretes

Etapa de contratação, aprovação, execução, medição, faturamento e controle de fretes inbound, outbound, transferências e frete emergencial.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| SCL-013 | Frete contratado fora da tabela, contrato ou transportador homologado sem aprovação | Initiation | Existência | Alta |
| SCL-014 | Frete emergencial usado recorrentemente sem análise de causa raiz | Processing | Valoração | Média |
| SCL-015 | Cobrança de frete divergente do peso, rota, distância, tabela ou serviço executado | Recording | Valoração | Alta |
| SCL-016 | Frete duplicado faturado por mesma entrega, CT-e ou romaneio | Recording | Existência | Alta |
| SCL-017 | Entrega realizada sem comprovante de entrega válido | Recording | Existência | Alta |
| SCL-018 | Acesso para alterar tabela de frete ou rota não restrito | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- tabela de frete aprovada por rota, peso, cubagem e serviço
- homologação de transportadores
- three-way match logístico: pedido/romaneio, CT-e/fatura e comprovante de entrega
- revisão de fretes emergenciais e exceções
- segregação na manutenção de tabelas e aprovação de pagamento

**Flag de risco elevado:** alta concentração de frete emergencial no fim do mês ou em cliente específico.

---

## Subprocesso 4: Armazenagem e Operadores Logísticos

Etapa de gestão de armazéns próprios e terceiros, operadores logísticos (3PL), movimentação, armazenagem, inventário e cobrança de serviços.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| SCL-019 | Estoque em operador logístico não reconciliado com ERP da empresa | Processing | Completude | Alta |
| SCL-020 | SLA de armazenagem, separação ou expedição não monitorado | Processing | Completude | Média |
| SCL-021 | Cobrança de armazenagem ou handling sem base em volume/atividade real | Recording | Valoração | Alta |
| SCL-022 | Acesso físico ao armazém ou área segregada não controlado | Processing | Existência | Alta |
| SCL-023 | Inventário em 3PL não observado, confirmado ou reconciliado periodicamente | Processing | Existência | Alta |
| SCL-024 | Condição de armazenagem inadequada para produto sensível (temperatura, umidade, segurança) | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- reconciliação periódica ERP x WMS/relatório do operador
- contrato com SLA, penalidade e direito de auditoria
- validação de faturas do 3PL contra atividade real
- inventário físico em armazém terceiro
- monitoramento de condições especiais de armazenagem

**Relação com Inventory:** Inventory cobre existência/valoração do estoque; Supply Chain cobre governança do operador e execução logística.

---

## Subprocesso 5: Importação, Exportação e Comércio Exterior

Etapa de classificação, documentos, Incoterms, desembaraço, custos, compliance aduaneiro, exportação e coordenação com despachantes/forwarders.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| SCL-025 | Incoterm aplicado incorretamente — transferência de risco, custo ou propriedade interpretada de forma errada | Initiation | Apresentação | Alta |
| SCL-026 | Classificação fiscal/NCM de importação divergente da regra tributária aplicável | Initiation | Valoração | Alta |
| SCL-027 | Documento de importação/exportação incompleto ou divergente do pedido, invoice ou embarque | Recording | Completude | Alta |
| SCL-028 | Custos de importação não apropriados corretamente ao estoque ou despesa | Recording | Valoração | Alta |
| SCL-029 | Despachante ou freight forwarder usado sem homologação ou due diligence | Processing | Existência | Alta |
| SCL-030 | Mercadoria em trânsito não monitorada ou registrada no período incorreto | Recording | Corte | Alta |

**Controles típicos que mitigam:**
- revisão de Incoterms e documentação por comércio exterior
- validação de NCM/classificação com tax
- checklist documental de importação/exportação
- reconciliação de custos de importação com estoque e contas a pagar
- homologação de despachantes e forwarders
- tracker de embarques em trânsito

**Relação com Tax:** Tax cobre tratamento tributário; Supply Chain cobre operação, documentação, Incoterms e fluxo logístico.

---

## Subprocesso 6: OTIF, SLA e Performance Logística

Etapa de mensuração de nível de serviço, entregas no prazo e completas, lead time, backlog, devoluções e performance de transportadores/operadores.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| SCL-031 | OTIF calculado com definição inconsistente entre períodos ou unidades | Reporting | Apresentação | Média |
| SCL-032 | Entregas parciais tratadas como completas para inflar indicador | Reporting | Valoração | Alta |
| SCL-033 | Atrasos causados por falta de estoque ou produção classificados como problema de transporte | Reporting | Apresentação | Média |
| SCL-034 | SLA de transportador medido com dados incompletos de coleta, trânsito ou entrega | Processing | Completude | Média |
| SCL-035 | Backlog ou pedidos pendentes não reportados à gestão comercial/operacional | Reporting | Completude | Média |
| SCL-036 | Penalidades ou créditos por descumprimento de SLA não cobrados de transportador/3PL | Processing | Completude | Média |

**Controles típicos que mitigam:**
- definição formal de OTIF, atraso, entrega completa e backlog
- fonte única de eventos logísticos
- reconciliação entre pedido, expedição, comprovante e status de entrega
- scorecard de transportador/3PL revisado periodicamente
- cobrança de penalidades e planos de ação por performance

**Flag de risco elevado:** indicador de serviço melhora enquanto reclamações de clientes ou devoluções aumentam.

---

## Subprocesso 7: Avarias, Perdas e Sinistros

Etapa de identificação, registro, investigação, ressarcimento e contabilização de avarias, perdas em trânsito, roubos, extravios e sinistros.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| SCL-037 | Avaria ou perda em transporte não registrada tempestivamente | Recording | Completude | Alta |
| SCL-038 | Sinistro não comunicado à seguradora dentro do prazo | Processing | Existência | Alta |
| SCL-039 | Ressarcimento de transportador, seguradora ou terceiro não acompanhado até recebimento | Processing | Completude | Média |
| SCL-040 | Produto avariado retornado ao estoque vendável sem inspeção | Processing | Existência | Alta |
| SCL-041 | Perdas recorrentes em rota, transportador ou armazém não analisadas por causa raiz | Processing | Completude | Média |
| SCL-042 | Baixa de perda logística registrada sem evidência de ocorrência, aprovação ou responsabilidade | Recording | Existência | Alta |

**Controles típicos que mitigam:**
- registro formal de avarias, extravios e sinistros
- processo de comunicação à seguradora e ao transportador
- tracker de ressarcimentos
- inspeção de produto retornado/avariado
- análise de perdas por rota, transportador, produto e unidade
- aprovação para baixa contábil de perdas logísticas

---

## Subprocesso 8: Continuidade e Resiliência da Cadeia

Etapa de preparação para interrupções, eventos climáticos, greves, restrições logísticas, crises de fornecedor, indisponibilidade de rota e concentração geográfica.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| SCL-043 | Plano de continuidade da cadeia inexistente para produtos, rotas ou fornecedores críticos | Initiation | Completude | Alta |
| SCL-044 | Cenários de ruptura logística não testados ou atualizados | Processing | Existência | Média |
| SCL-045 | Estoque de segurança definido sem considerar risco de ruptura, lead time e criticidade | Processing | Valoração | Média |
| SCL-046 | Dependência de rota, porto, armazém ou transportador único sem alternativa operacional | Processing | Existência | Alta |
| SCL-047 | Evento externo relevante não incorporado ao plano de supply chain tempestivamente | Processing | Completude | Média |

**Controles típicos que mitigam:**
- mapeamento de nós críticos da cadeia
- plano de contingência por produto, rota, fornecedor e operador
- revisão de estoque de segurança por criticidade e lead time
- testes de cenário e simulações
- monitoramento de eventos externos relevantes

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Forecast e plano operacional frágeis | Planejamento | SCL-001, SCL-002, SCL-006 |
| Dependência crítica sem contingência | Fornecedores, Resiliência | SCL-007, SCL-008, SCL-046 |
| Frete indevido ou duplicado | Transporte | SCL-013, SCL-015, SCL-016 |
| Estoque em 3PL sem visibilidade | Armazenagem | SCL-019, SCL-023 |
| Import/export com documentação ou Incoterm errado | Comércio Exterior | SCL-025, SCL-027, SCL-030 |
| Indicador OTIF inflado ou inconsistente | Performance | SCL-031, SCL-032, SCL-034 |
| Perda logística sem recuperação ou causa raiz | Avarias | SCL-037, SCL-039, SCL-041 |
| Continuidade da cadeia não preparada | Resiliência | SCL-043, SCL-045, SCL-047 |
