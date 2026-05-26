---
processo: legal-compliance-third-parties
nivel: 1
abreviacao: LCT
subprocessos:
  - onboarding-e-due-diligence-de-terceiros
  - contratacao-e-aprovacao-legal
  - brindes-conflitos-e-partes-relacionadas
  - pagamentos-sensiveis-e-intermediarios
  - obrigacoes-regulatorias-e-investigacoes
  - ciclo-de-vida-contratual
assercoes_primarias:
  - existência
  - completude
  - valoração
  - apresentação
frameworks:
  - COSO
  - compliance anticorrupcao
  - gestao de terceiros
  - contract lifecycle management
referencias:
  - context/wcgw/procure-to-pay.md
  - context/wcgw/fraud-risk-assessment.md
  - context/wcgw/entity-level-controls.md
---

# WCGW — Legal, Compliance & Third Parties (LCT)

Legal e compliance não são apenas áreas consultivas. Em auditoria interna, eles formam uma camada crítica de prevenção contra perdas, sanções, contratos mal aprovados, exposição reputacional e fraude por intermediários.

O risco central é que a organização opere com terceiros, contratos ou obrigações regulatórias sem saber **quem está assumindo o risco**, **quem aprovou**, **qual cláusula protege a empresa** e **se o compromisso continua válido depois da assinatura**.

---

## Subprocesso 1: Onboarding e Due Diligence de Terceiros

Etapa em que fornecedores, consultores, representantes comerciais, distribuidores, despachantes, agentes públicos indiretos e parceiros são avaliados antes de iniciar relação comercial.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| LCT-001 | Terceiro contratado sem due diligence mínima — risco reputacional, sancionatório ou de fraude não avaliado | Initiation | Existência | Alta |
| LCT-002 | Due diligence executada apenas após assinatura do contrato — controle opera tarde demais | Processing | Existência | Alta |
| LCT-003 | Cadastro de terceiro aprovado mesmo com red flags abertas sem justificativa documentada | Processing | Existência | Alta |
| LCT-004 | Beneficiário final do terceiro não identificado — empresa pode contratar parte relacionada, PEP ou pessoa sancionada sem saber | Initiation | Completude | Alta |
| LCT-005 | Consulta a listas restritivas feita uma única vez e não reexecutada periodicamente | Processing | Completude | Média |
| LCT-006 | Risco do terceiro classificado como baixo sem critério formal — due diligence simplificada aplicada indevidamente | Processing | Valoração | Alta |
| LCT-007 | Terceiro de alto risco aprovado pela própria área interessada na contratação — ausência de revisão independente | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- política de onboarding de terceiros com critérios por risco
- due diligence obrigatória antes de contrato ou primeiro pagamento
- identificação de beneficiário final, PEP, sanções, mídia negativa e partes relacionadas
- workflow de aprovação independente para terceiros de alto risco
- rechecagem periódica de terceiros ativos, especialmente agentes e intermediários

**Flag de risco elevado:** terceiro com baixa estrutura operacional, remuneração variável elevada ou atuação em interface com governo.

---

## Subprocesso 2: Contratação e Aprovação Legal

Etapa de elaboração, revisão, negociação e aprovação de contratos, aditivos, exceções e cláusulas relevantes.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| LCT-008 | Contrato assinado sem revisão jurídica quando política exige — cláusulas críticas podem faltar ou estar inadequadas | Processing | Existência | Alta |
| LCT-009 | Minuta padrão alterada sem evidência de aprovação do jurídico | Processing | Existência | Alta |
| LCT-010 | Contrato assinado por pessoa sem poderes ou alçada formal | Initiation | Existência | Alta |
| LCT-011 | Aditivo contratual altera escopo, preço ou prazo sem nova aprovação por alçada | Processing | Existência | Alta |
| LCT-012 | Cláusulas anticorrupção, confidencialidade, LGPD ou conflito de interesses ausentes em contratos sensíveis | Recording | Completude | Alta |
| LCT-013 | Contrato com obrigação financeira relevante não comunicado ao financeiro/contabilidade — compromisso fora do radar | Recording | Completude | Alta |
| LCT-014 | Exceções contratuais aprovadas por e-mail informal sem registro no repositório oficial | Recording | Existência | Média |

**Controles típicos que mitigam:**
- matriz de alçadas para assinatura e aprovação contratual
- uso obrigatório de minuta padrão ou parecer jurídico para alterações
- repositório central de contratos e aditivos assinados
- checklist jurídico por tipo de contrato
- integração entre jurídico, compras, financeiro e contabilidade para compromissos relevantes

**Armadilha comum:** tratar aprovação de compra como se fosse aprovação jurídica. A OC pode autorizar gasto, mas não substitui revisão de obrigações contratuais.

---

## Subprocesso 3: Brindes, Conflitos e Partes Relacionadas

Etapa de identificação, declaração, aprovação e monitoramento de situações em que interesses pessoais podem afetar decisão corporativa.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| LCT-015 | Funcionários não declaram conflitos de interesse periodicamente — relações relevantes ficam invisíveis | Initiation | Completude | Alta |
| LCT-016 | Declarações de conflito recebidas mas não analisadas por compliance ou gestor independente | Processing | Existência | Alta |
| LCT-017 | Brindes, viagens ou hospitalidades acima do limite aceito sem aprovação formal | Processing | Existência | Alta |
| LCT-018 | Relação com parte relacionada não identificada antes da contratação | Initiation | Completude | Alta |
| LCT-019 | Transação com parte relacionada aprovada pela pessoa beneficiada ou interessada | Processing | Existência | Alta |
| LCT-020 | Registro de brindes e hospitalidades mantido fora de sistema ou planilha controlada — incompleto e não auditável | Recording | Completude | Média |
| LCT-021 | Política de conflito de interesses existe mas não define consequência para omissão ou descumprimento | Initiation | Existência | Média |

**Controles típicos que mitigam:**
- declaração anual de conflito de interesses para público sensível
- registro central de brindes, hospitalidades, patrocínios e doações
- aprovação prévia por compliance para itens acima de limite
- cruzamento periódico entre funcionários, fornecedores e partes relacionadas
- bloqueio de participação de interessado em aprovações relacionadas ao próprio conflito

**Flag de risco elevado:** fornecedor novo indicado por executivo ou gestor sem processo competitivo claro.

---

## Subprocesso 4: Pagamentos Sensíveis e Intermediários

Etapa de aprovação, execução e monitoramento de pagamentos a agentes, consultores, representantes, despachantes, advogados externos, doações, patrocínios e facilitation-risk payments.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| LCT-022 | Pagamento a intermediário sem evidência de serviço prestado — risco de repasse indevido | Processing | Existência | Alta |
| LCT-023 | Comissão ou success fee incompatível com prática de mercado ou sem base contratual clara | Recording | Valoração | Alta |
| LCT-024 | Pagamento realizado em conta bancária de terceiro diferente do contratado | Processing | Existência | Alta |
| LCT-025 | Pagamento fracionado para ficar abaixo do limite de aprovação de compliance ou diretoria | Processing | Existência | Alta |
| LCT-026 | Doação ou patrocínio aprovado sem avaliação de beneficiário, finalidade e vínculo com decisores públicos | Initiation | Existência | Alta |
| LCT-027 | Reembolso de despesa sensível aprovado sem nota, agenda, participante ou justificativa de negócio | Recording | Existência | Alta |
| LCT-028 | Honorários de advogado externo ou consultor aprovados sem carta de contratação, escopo ou evidência de entrega | Processing | Existência | Média |

**Controles típicos que mitigam:**
- categoria de pagamentos sensíveis com aprovação adicional de compliance
- evidência obrigatória de entrega antes do pagamento
- bloqueio para pagamento em conta diferente do terceiro cadastrado
- revisão de comissões, success fees, doações e patrocínios por compliance
- relatório periódico de pagamentos sensíveis por terceiro, valor, aprovador e centro de custo

**Flag de risco elevado:** intermediário remunerado por êxito em obtenção de licença, benefício fiscal, contrato público ou liberação regulatória.

---

## Subprocesso 5: Obrigações Regulatórias e Investigações

Etapa de identificação, cumprimento, reporte e acompanhamento de obrigações legais/regulatórias, notificações, fiscalizações, litígios e investigações internas.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| LCT-029 | Obrigações regulatórias não mapeadas em inventário central — prazos e responsáveis dependem de memória individual | Initiation | Completude | Alta |
| LCT-030 | Licença, autorização ou registro regulatório vencido sem alerta tempestivo | Processing | Existência | Alta |
| LCT-031 | Resposta a órgão regulador enviada sem revisão jurídica ou aprovação competente | Processing | Existência | Alta |
| LCT-032 | Notificação, auto de infração ou processo relevante não comunicado à contabilidade para avaliação de provisão/contingência | Reporting | Completude | Alta |
| LCT-033 | Investigação interna conduzida pela área envolvida na denúncia — independência comprometida | Processing | Existência | Alta |
| LCT-034 | Evidências de investigação não preservadas adequadamente — cadeia de custódia fraca | Recording | Existência | Alta |
| LCT-035 | Plano de remediação de investigação concluída não monitorado até implementação | Reporting | Completude | Alta |

**Controles típicos que mitigam:**
- inventário regulatório com donos, prazos, evidências e alertas
- workflow para notificações e respostas oficiais com revisão jurídica
- comunicação formal de contingências para contabilidade e auditoria
- protocolo de investigação com independência, confidencialidade e preservação de evidência
- tracker de remediação com responsável, prazo e status

**Armadilha crítica:** tratar investigação como evento jurídico isolado. Se a causa raiz for controle fraco, o achado precisa virar remediação operacional.

---

## Subprocesso 6: Ciclo de Vida Contratual

Etapa posterior à assinatura: guarda, monitoramento de vigência, obrigações, reajustes, renovações, rescisões e encerramento de contratos.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| LCT-036 | Contratos assinados não armazenados em repositório central — versão vigente não identificável | Recording | Completude | Alta |
| LCT-037 | Contrato renovado automaticamente sem reavaliação de preço, performance, risco ou necessidade | Processing | Valoração | Média |
| LCT-038 | Reajuste contratual aplicado sem base em índice, data ou cláusula válida | Processing | Valoração | Alta |
| LCT-039 | Obrigações de performance, SLA ou penalidades não monitoradas após assinatura | Processing | Completude | Alta |
| LCT-040 | Contrato encerrado mas acessos, procurações, confidencialidade ou obrigações residuais não revogados/monitorados | Reporting | Completude | Alta |

**Controles típicos que mitigam:**
- repositório central com contrato, aditivos, vigência, owner e alertas
- revisão antes de renovação automática
- controle de reajustes com índice, data-base e aprovação
- monitoramento de SLAs e penalidades contratuais
- checklist de encerramento: acessos, procurações, confidencialidade, dados, ativos e pendências financeiras

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Terceiro de alto risco sem due diligence | Onboarding | LCT-001, LCT-003, LCT-004 |
| Contrato assinado sem proteção jurídica | Contratação | LCT-008, LCT-012 |
| Assinatura sem poderes ou alçada | Contratação | LCT-010, LCT-011 |
| Conflito de interesse não identificado | Brindes e conflitos | LCT-015, LCT-018, LCT-019 |
| Pagamento sensível sem lastro | Pagamentos sensíveis | LCT-022, LCT-023, LCT-027 |
| Doação/patrocínio usado como canal indevido | Pagamentos sensíveis | LCT-026 |
| Obrigação regulatória vencida ou não mapeada | Regulatório | LCT-029, LCT-030 |
| Investigação sem independência ou evidência preservada | Investigações | LCT-033, LCT-034 |
| Contrato vigente ou renovado sem controle | Ciclo de vida contratual | LCT-036, LCT-037, LCT-039 |
| Encerramento incompleto de contrato | Ciclo de vida contratual | LCT-040 |
