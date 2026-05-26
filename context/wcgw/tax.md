---
processo: tax
nivel: 1
abreviacao: TAX
subprocessos:
  - cadastro-fiscal-e-parametros
  - impostos-indiretos-sobre-vendas
  - impostos-indiretos-sobre-compras-e-creditos
  - retencoes-na-fonte
  - impostos-sobre-renda-e-contribuicao-social
  - obrigacoes-acessorias-e-reportes
  - contingencias-fiscais-e-fiscalizacoes
  - incentivos-beneficios-e-regimes-especiais
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - CPC 32
  - IAS 12
  - compliance tributario
referencias:
  - context/wcgw/procure-to-pay.md
  - context/wcgw/order-to-cash.md
  - context/wcgw/record-to-report.md
  - context/wcgw/legal-compliance-third-parties.md
---

# WCGW — Tax / Tributos (TAX)

Tributos conectam operação, cadastro, faturamento, compras, folha, contabilidade e compliance regulatório. O risco não está só em "calcular imposto errado"; está em parametrização fiscal, classificação de produto, uso indevido de crédito, retenções não aplicadas, obrigações acessórias inconsistentes, contingências não reconhecidas e benefícios fiscais sem lastro.

O auditor deve separar três camadas: **determinação do tributo**, **registro contábil/fiscal** e **cumprimento da obrigação**. Quando uma delas falha, a empresa pode pagar imposto a maior, pagar a menor, perder crédito, gerar multa ou distorcer demonstrações financeiras.

---

## Subprocesso 1: Cadastro Fiscal e Parâmetros

Etapa de manutenção de NCM, CFOP, CST/CSOSN, alíquotas, regimes fiscais, municípios, regras por produto/cliente/fornecedor e parametrizações no ERP.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TAX-001 | NCM ou classificação fiscal do produto cadastrada incorretamente — imposto calculado com regra errada | Initiation | Valoração | Alta |
| TAX-002 | CFOP/CST parametrizado de forma incompatível com a natureza da operação | Initiation | Apresentação | Alta |
| TAX-003 | Alíquota fiscal desatualizada no ERP após mudança legal | Processing | Valoração | Alta |
| TAX-004 | Regra fiscal alterada sem aprovação ou revisão da área tributária | Processing | Existência | Alta |
| TAX-005 | Cadastro fiscal de cliente ou fornecedor incompleto — regime tributário, inscrição ou localidade incorretos | Initiation | Completude | Média |
| TAX-006 | Parâmetros fiscais diferentes entre ERP, sistema fiscal e emissor de NF | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- workflow de alteração de parâmetros fiscais com aprovação tributária
- revisão periódica de NCM, CFOP, CST e alíquotas para itens relevantes
- trilha de auditoria de alterações fiscais no ERP
- conciliação entre ERP, sistema fiscal e emissor de NF
- monitoramento de mudanças legais aplicáveis ao negócio

**Flag de risco elevado:** grande volume de operações com parametrização manual ou exceções fiscais por item.

---

## Subprocesso 2: Impostos Indiretos sobre Vendas

Etapa de cálculo, destaque, escrituração e recolhimento de tributos incidentes sobre faturamento e circulação de mercadorias/serviços.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TAX-007 | ICMS, ISS, PIS/COFINS ou outro tributo sobre venda calculado com alíquota incorreta | Recording | Valoração | Alta |
| TAX-008 | Nota fiscal emitida sem destaque de imposto devido | Recording | Completude | Alta |
| TAX-009 | Operação tributada tratada como isenta, não tributada ou suspensa sem base legal | Recording | Valoração | Alta |
| TAX-010 | Base de cálculo fiscal exclui frete, seguro, desconto ou componente obrigatório indevidamente | Recording | Valoração | Alta |
| TAX-011 | Venda interestadual ou internacional tratada com regra fiscal incorreta | Recording | Valoração | Alta |
| TAX-012 | Cancelamento, devolução ou nota de crédito não refletido corretamente na apuração fiscal | Processing | Completude | Média |

**Controles típicos que mitigam:**
- validação automática de regra fiscal na emissão da NF
- revisão de exceções fiscais e operações sem destaque de tributo
- conciliação entre faturamento, XML/NF-e, livros fiscais e razão contábil
- revisão de operações interestaduais, exportações e serviços por amostra dirigida
- aprovação tributária para uso de isenção, suspensão ou benefício

**Relação com OTC:** OTC cobre venda, entrega e AR; Tax cobre o tratamento tributário da venda e sua escrituração.

---

## Subprocesso 3: Impostos Indiretos sobre Compras e Créditos

Etapa de tomada, validação, escrituração e aproveitamento de créditos tributários em compras, insumos, ativo imobilizado e serviços.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TAX-013 | Crédito tributário tomado sobre item ou serviço não elegível | Recording | Existência | Alta |
| TAX-014 | Crédito elegível não aproveitado — pagamento de tributo a maior | Recording | Completude | Média |
| TAX-015 | Crédito registrado com valor divergente do XML/NF ou documento fiscal | Recording | Valoração | Alta |
| TAX-016 | Crédito de fornecedor irregular, inidôneo ou com documento fiscal cancelado | Processing | Existência | Alta |
| TAX-017 | Crédito sobre ativo imobilizado apropriado em parcela, prazo ou base incorreta | Processing | Valoração | Média |
| TAX-018 | Estorno de crédito não realizado quando há devolução, perda, isenção ou mudança de destinação | Processing | Completude | Alta |

**Controles típicos que mitigam:**
- validação automática do XML e situação da NF antes da escrituração
- regra de elegibilidade de crédito por tipo de item, CFOP, CST e uso
- conciliação de créditos entre livro fiscal, razão contábil e apuração
- revisão de fornecedores irregulares ou documentos cancelados
- análise periódica de créditos não aproveitados e estornos obrigatórios

**Relação com P2P:** P2P cobre compra, recebimento e pagamento; Tax cobre se o crédito fiscal foi tomado corretamente.

---

## Subprocesso 4: Retenções na Fonte

Etapa de identificação, cálculo, retenção, recolhimento e informe de tributos retidos de fornecedores, prestadores, aluguéis, autônomos, juros, royalties e pagamentos internacionais.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TAX-019 | Retenção obrigatória não aplicada no pagamento a fornecedor ou prestador | Processing | Completude | Alta |
| TAX-020 | Retenção calculada com alíquota ou base incorreta | Recording | Valoração | Alta |
| TAX-021 | Tributo retido não recolhido no prazo legal | Processing | Completude | Alta |
| TAX-022 | Pagamento internacional realizado sem análise de IRRF, CIDE, IOF ou tratado aplicável | Initiation | Existência | Alta |
| TAX-023 | Comprovante ou informe de retenção emitido com valor divergente do recolhido | Reporting | Valoração | Média |
| TAX-024 | Retenção duplicada ou indevida não recuperada — custo tributário a maior | Processing | Valoração | Média |

**Controles típicos que mitigam:**
- matriz de retenções por tipo de serviço, fornecedor e jurisdição
- bloqueio ou alerta fiscal antes do pagamento
- conciliação entre AP, pagamentos, guias e obrigações acessórias
- revisão tributária de pagamentos internacionais
- calendário de recolhimento com responsável e evidência

**Flag de risco elevado:** serviço tomado de pessoa jurídica com descrição genérica, pagamento internacional ou fornecedor recém-cadastrado.

---

## Subprocesso 5: Impostos sobre Renda e Contribuição Social

Etapa de apuração, provisão, recolhimento, diferidos, adições/exclusões, prejuízo fiscal e reconciliação da taxa efetiva.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TAX-025 | Base de IRPJ/CSLL calculada sem considerar adições e exclusões obrigatórias | Recording | Valoração | Alta |
| TAX-026 | Provisão de imposto corrente não reconciliada com apuração fiscal | Reporting | Valoração | Alta |
| TAX-027 | Ativo fiscal diferido reconhecido sem evidência de lucro tributável futuro | Processing | Existência | Alta |
| TAX-028 | Passivo fiscal diferido não reconhecido sobre diferenças temporárias relevantes | Recording | Completude | Alta |
| TAX-029 | Prejuízo fiscal ou base negativa compensada acima do limite legal | Processing | Valoração | Alta |
| TAX-030 | Reconciliação da taxa efetiva não preparada ou não explica variações relevantes | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- checklist de adições, exclusões e compensações fiscais
- conciliação entre ECF/apuração fiscal, razão e provisão contábil
- análise de recuperabilidade de ativo fiscal diferido
- revisão técnica de diferenças temporárias relevantes
- reconciliação da taxa efetiva com investigação de variações

**Relação com RTR:** RTR cobre fechamento e demonstrações; Tax cobre se tributo corrente/diferido está correto e suportado.

---

## Subprocesso 6: Obrigações Acessórias e Reportes

Etapa de preparação, revisão, entrega e retificação de SPED, EFD, ECF, DCTF, DIRF/eSocial/EFD-Reinf ou obrigações equivalentes.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TAX-031 | Obrigação acessória entregue fora do prazo ou não entregue | Reporting | Completude | Alta |
| TAX-032 | Informações declaradas em obrigação acessória divergem do razão contábil ou apuração fiscal | Reporting | Valoração | Alta |
| TAX-033 | Retificação enviada sem revisão ou aprovação formal | Processing | Existência | Média |
| TAX-034 | Arquivo fiscal gerado a partir de base incompleta ou período incorreto | Processing | Completude | Alta |
| TAX-035 | Inconsistências apontadas por validação oficial não tratadas antes da entrega | Processing | Existência | Alta |
| TAX-036 | Evidência de entrega, recibo e versão final não arquivados em repositório controlado | Recording | Existência | Média |

**Controles típicos que mitigam:**
- calendário tributário com obrigações, responsáveis, prazos e evidências
- conciliação entre obrigação acessória, apuração, razão e documentos fiscais
- revisão independente antes do envio
- controle formal de retificações
- arquivamento de recibos, versões finais e logs de validação

**Flag de risco elevado:** obrigação entregue por consultoria externa sem revisão interna de consistência.

---

## Subprocesso 7: Contingências Fiscais e Fiscalizações

Etapa de monitoramento de autos de infração, discussões administrativas/judiciais, fiscalizações, depósitos judiciais, provisões e divulgações.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TAX-037 | Auto de infração ou discussão fiscal relevante não comunicado à contabilidade | Reporting | Completude | Alta |
| TAX-038 | Classificação de risco provável/possível/remoto sem parecer jurídico ou tributário atualizado | Processing | Valoração | Alta |
| TAX-039 | Provisão fiscal não reconhecida para perda provável e mensurável | Recording | Completude | Alta |
| TAX-040 | Contingência fiscal possível não divulgada adequadamente em nota explicativa | Reporting | Apresentação | Alta |
| TAX-041 | Depósito judicial ou garantia fiscal não conciliado com processo correspondente | Processing | Existência | Média |
| TAX-042 | Fiscalização atendida com informação incompleta ou divergente sem revisão formal | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- inventário de processos fiscais com responsável, valor, status e probabilidade
- atualização periódica com jurídico interno/externo
- conciliação de depósitos judiciais, garantias e provisões
- comunicação formal entre tax, jurídico, contabilidade e auditoria
- revisão de respostas a fiscalizações antes do envio

**Relação com Legal/Compliance:** legal acompanha litígio e resposta; tax avalia impacto tributário, provisão e disclosure.

---

## Subprocesso 8: Incentivos, Benefícios e Regimes Especiais

Etapa de obtenção, manutenção, cálculo e comprovação de incentivos fiscais, regimes especiais, benefícios setoriais e créditos presumidos.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| TAX-043 | Benefício fiscal utilizado sem cumprir requisito formal ou operacional | Initiation | Existência | Alta |
| TAX-044 | Crédito presumido ou incentivo calculado sobre base incorreta | Recording | Valoração | Alta |
| TAX-045 | Condição de manutenção do regime especial não monitorada — risco de perda retroativa do benefício | Processing | Completude | Alta |
| TAX-046 | Documentação comprobatória do benefício não arquivada para suportar fiscalização futura | Recording | Existência | Alta |
| TAX-047 | Incentivo fiscal relevante não divulgado ou apresentado de forma inadequada nas demonstrações | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- inventário de benefícios fiscais com requisitos, prazo, responsável e evidências
- revisão periódica de cumprimento das condições
- cálculo revisado por pessoa independente ou consultor especializado
- dossiê de suporte para fiscalização
- comunicação com contabilidade para apresentação e disclosure

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Parametrização fiscal incorreta | Cadastro fiscal | TAX-001, TAX-003, TAX-006 |
| Tributo sobre venda calculado errado | Vendas | TAX-007, TAX-009, TAX-010 |
| Crédito fiscal indevido ou perdido | Compras e créditos | TAX-013, TAX-014, TAX-018 |
| Retenção não aplicada ou não recolhida | Retenções | TAX-019, TAX-021, TAX-022 |
| Imposto corrente/diferido incorreto | IR/CS | TAX-025, TAX-027, TAX-028 |
| Obrigação acessória inconsistente | Reportes | TAX-031, TAX-032, TAX-035 |
| Contingência fiscal não reconhecida/divulgada | Contingências | TAX-037, TAX-039, TAX-040 |
| Benefício fiscal sem lastro | Incentivos | TAX-043, TAX-045, TAX-046 |
