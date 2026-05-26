---
processo: capex-projects
nivel: 1
abreviacao: CAPEX
subprocessos:
  - ideacao-e-business-case
  - aprovacao-e-governanca-de-investimento
  - orcamento-e-controle-de-custos
  - contratacao-de-obras-e-servicos
  - medicoes-change-orders-e-pleitos
  - capitalizacao-vs-despesa
  - handover-para-operacao-e-fixed-assets
  - beneficios-pos-implementacao
assercoes_primarias:
  - existência
  - completude
  - valoração
  - corte
  - apresentação
frameworks:
  - COSO
  - project governance
  - IAS 16
  - CPC 27
  - IAS 38
referencias:
  - context/wcgw/fixed-assets.md
  - context/wcgw/procure-to-pay.md
  - context/wcgw/supply-chain-logistics.md
  - context/wcgw/legal-compliance-third-parties.md
---

# WCGW — Capex & Projects (CAPEX)

Capex & Projects cobre o ciclo de investimentos relevantes: da ideia e aprovação do business case até execução, medições, capitalização, entrada em operação e validação dos benefícios. Fixed Assets cobre o ativo já registrado; Capex cobre o projeto que cria, expande ou modifica esse ativo.

O risco central é a empresa aprovar investimento sem racional econômico, gastar acima do aprovado, capitalizar o que deveria ser despesa, aceitar medições frágeis, perder controle de change orders ou colocar ativo em operação sem handover adequado.

---

## Subprocesso 1: Ideação e Business Case

Etapa de identificação da necessidade, elaboração do racional econômico, alternativas, premissas, benefícios e riscos do investimento.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| CAPEX-001 | Projeto iniciado sem business case formal ou justificativa de necessidade | Initiation | Existência | Alta |
| CAPEX-002 | Premissas financeiras do business case não suportadas por dados ou benchmark | Initiation | Valoração | Alta |
| CAPEX-003 | Alternativas de menor custo ou menor risco não avaliadas antes da aprovação | Initiation | Completude | Média |
| CAPEX-004 | Benefícios esperados inflados para viabilizar aprovação do projeto | Initiation | Valoração | Alta |
| CAPEX-005 | Riscos regulatórios, ambientais, operacionais ou de execução não considerados no business case | Initiation | Completude | Alta |
| CAPEX-006 | Escopo do projeto definido de forma vaga — impossibilita medir entrega e custo | Initiation | Existência | Alta |

**Controles típicos que mitigam:**
- template de business case com problema, alternativas, custo, benefício, risco e premissas
- revisão independente de premissas financeiras relevantes
- aprovação de escopo e critérios de sucesso antes do orçamento
- análise de sensibilidade para principais premissas
- envolvimento de operação, financeiro, engenharia, EHS e jurídico conforme natureza do projeto

**Flag de risco elevado:** payback muito agressivo sem evidência operacional ou comercial robusta.

---

## Subprocesso 2: Aprovação e Governança de Investimento

Etapa de aprovação por alçada, comitê, diretoria/conselho, stage gates e definição de owner, sponsor e governança.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| CAPEX-007 | Projeto aprovado por alçada insuficiente para o valor total estimado | Processing | Existência | Alta |
| CAPEX-008 | Aprovação segmentada em fases para evitar alçada superior sem justificativa | Processing | Existência | Alta |
| CAPEX-009 | Stage gate obrigatório não realizado antes de avançar para execução | Processing | Existência | Média |
| CAPEX-010 | Sponsor, owner e responsável financeiro do projeto não definidos formalmente | Initiation | Completude | Média |
| CAPEX-011 | Comitê de investimento aprova projeto sem ata, deliberação ou condições registradas | Recording | Existência | Média |
| CAPEX-012 | Projeto iniciado antes da aprovação formal final | Processing | Existência | Alta |

**Controles típicos que mitigam:**
- matriz de alçadas para capex por valor e tipo de projeto
- aprovação por stage gates
- ata de comitê com decisões, condições e responsáveis
- bloqueio de abertura de projeto/ordem interna sem aprovação
- controle de fracionamento de projetos relacionados

**Armadilha comum:** tratar autorização orçamentária anual como se fosse aprovação específica de cada projeto relevante.

---

## Subprocesso 3: Orçamento e Controle de Custos

Etapa de criação do orçamento do projeto, baseline, controle de comprometido, realizado, forecast, contingência e variações.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| CAPEX-013 | Baseline orçamentário não definido antes do início da execução | Initiation | Existência | Alta |
| CAPEX-014 | Custos comprometidos por contratos/OCs não considerados no forecast do projeto | Processing | Completude | Alta |
| CAPEX-015 | Variações de custo relevantes não analisadas ou aprovadas | Processing | Valoração | Alta |
| CAPEX-016 | Contingência usada para cobrir mudança de escopo sem aprovação | Processing | Existência | Alta |
| CAPEX-017 | Custos de projeto registrados em centro/ordem incorreta | Recording | Apresentação | Média |
| CAPEX-018 | Forecast de conclusão preparado pelo próprio executor sem revisão financeira independente | Reporting | Valoração | Média |

**Controles típicos que mitigam:**
- orçamento baseline aprovado e travado
- relatório periódico de budget, committed, actual, forecast e variance
- revisão financeira independente do forecast
- aprovação formal para uso de contingência
- reconciliação entre OCs, contratos, medições e ordem de projeto

**Flag de risco elevado:** projeto aparentemente "dentro do orçamento" porque custos comprometidos ainda não foram registrados.

---

## Subprocesso 4: Contratação de Obras e Serviços

Etapa de contratação de engenharia, construção, equipamentos, EPC, consultorias técnicas e fornecedores do projeto.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| CAPEX-019 | Contratação de obra/serviço sem concorrência, justificativa ou aprovação de contratação direta | Initiation | Existência | Alta |
| CAPEX-020 | Escopo contratado não corresponde ao escopo aprovado do projeto | Processing | Completude | Alta |
| CAPEX-021 | Contrato de obra sem cláusulas de medição, retenção, garantia, penalidade ou aceite | Initiation | Completude | Alta |
| CAPEX-022 | Fornecedor crítico de projeto contratado sem avaliação técnica, financeira ou compliance | Initiation | Existência | Alta |
| CAPEX-023 | Mobilização de fornecedor antes da assinatura do contrato ou OC | Processing | Existência | Alta |
| CAPEX-024 | Contrato de projeto permite reajuste ou cobrança adicional sem critério objetivo | Processing | Valoração | Alta |

**Controles típicos que mitigam:**
- processo competitivo ou justificativa aprovada para contratação direta
- revisão técnica e jurídica do contrato
- cláusulas de medição, retenção, garantia, penalidade e aceite
- homologação técnica e compliance de fornecedores críticos
- bloqueio de mobilização antes de contrato/OC formal

**Relação com P2P/LCT:** P2P cobre compra e pagamento; LCT cobre contrato; Capex cobre aderência da contratação ao projeto aprovado e seu controle de execução.

---

## Subprocesso 5: Medições, Change Orders e Pleitos

Etapa de medição de obra/serviço, aprovação de boletins, mudanças de escopo, claims, pleitos, aditivos e reequilíbrio econômico.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| CAPEX-025 | Medição aprovada sem evidência física, laudo técnico ou aceite do owner | Processing | Existência | Alta |
| CAPEX-026 | Pagamento de medição acima do avanço físico real | Recording | Valoração | Alta |
| CAPEX-027 | Change order executado antes de aprovação formal | Processing | Existência | Alta |
| CAPEX-028 | Aditivo altera escopo, prazo ou preço sem reaprovação por alçada | Processing | Existência | Alta |
| CAPEX-029 | Pleito de fornecedor aceito sem análise técnica, jurídica e financeira | Processing | Valoração | Alta |
| CAPEX-030 | Retenção contratual, garantia ou penalidade não aplicada conforme contrato | Processing | Completude | Média |

**Controles típicos que mitigam:**
- medição validada por engenharia/owner independente
- evidência física, relatório fotográfico ou laudo para avanço relevante
- workflow de change order antes da execução
- aprovação de aditivos por alçada
- análise técnica, jurídica e financeira de pleitos
- controle de retenções, garantias e penalidades

**Flag de risco elevado:** mudança de escopo "urgente" executada em campo antes de formalização.

---

## Subprocesso 6: Capitalização vs Despesa

Etapa de avaliar quais custos são capitalizáveis, quais devem ir a despesa, quando iniciar/parar capitalização e como tratar juros, treinamento, manutenção e overhead.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| CAPEX-031 | Despesa operacional capitalizada como projeto para melhorar resultado | Recording | Valoração | Alta |
| CAPEX-032 | Custo diretamente atribuível ao ativo registrado como despesa — ativo subavaliado | Recording | Completude | Média |
| CAPEX-033 | Capitalização continua após ativo estar pronto para uso | Recording | Corte | Alta |
| CAPEX-034 | Juros capitalizados sem atender critérios ou calculados sobre base incorreta | Recording | Valoração | Alta |
| CAPEX-035 | Treinamento, start-up, ineficiência ou perda operacional capitalizada indevidamente | Recording | Valoração | Alta |
| CAPEX-036 | Projeto de software capitaliza atividades de pesquisa ou manutenção sem critério IAS 38 | Recording | Existência | Alta |

**Controles típicos que mitigam:**
- política de capitalização alinhada a CPC 27/IAS 16 e IAS 38
- revisão contábil dos tipos de custo por projeto
- cut-off de capitalização na data de pronto para uso
- cálculo revisado de juros capitalizados
- amostra de lançamentos para identificar despesas capitalizadas indevidamente

**Relação com Fixed Assets:** Capex decide se e quando vira ativo; Fixed Assets controla o ativo depois de registrado.

---

## Subprocesso 7: Handover para Operação e Fixed Assets

Etapa de aceite final, entrada em operação, transferência de obra em andamento, cadastro patrimonial, documentação técnica e manutenção.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| CAPEX-037 | Ativo entra em operação sem aceite formal da área usuária | Processing | Existência | Alta |
| CAPEX-038 | Obra em andamento mantida em CIP após ativo estar pronto para uso | Recording | Corte | Alta |
| CAPEX-039 | Ativo transferido para fixed assets sem componentização adequada | Recording | Valoração | Média |
| CAPEX-040 | Documentação técnica, manual, garantia ou licença não entregue no handover | Recording | Completude | Média |
| CAPEX-041 | Plano de manutenção preventiva não criado para ativo relevante | Processing | Completude | Média |
| CAPEX-042 | Cadastro patrimonial criado com localização, owner ou vida útil incorreta | Recording | Apresentação | Média |

**Controles típicos que mitigam:**
- checklist de handover com aceite da operação
- data de pronto para uso comunicada à contabilidade
- transferência tempestiva de CIP para ativo final
- componentização e vida útil revisadas por engenharia/contabilidade
- documentação técnica e garantia arquivadas
- criação de plano de manutenção

**Flag de risco elevado:** projeto fisicamente em operação, mas contabilidade ainda classifica como obra em andamento.

---

## Subprocesso 8: Benefícios Pós-Implementação

Etapa de medir se o projeto entregou benefícios prometidos, lições aprendidas, performance real, savings, capacidade e retorno econômico.

| ID | WCGW | Fase SCOT | Asserção | Severidade |
|---|---|---|---|---|
| CAPEX-043 | Benefícios prometidos no business case não monitorados após implementação | Reporting | Completude | Média |
| CAPEX-044 | Savings ou aumento de capacidade reportado sem metodologia ou baseline consistente | Reporting | Valoração | Média |
| CAPEX-045 | Projeto encerrado sem comparação entre custo final, prazo final e baseline aprovado | Reporting | Completude | Média |
| CAPEX-046 | Lições aprendidas não documentadas para projetos relevantes | Reporting | Existência | Baixa |
| CAPEX-047 | Indicador de sucesso do projeto ignora impacto operacional negativo posterior | Reporting | Apresentação | Média |

**Controles típicos que mitigam:**
- post-implementation review para projetos relevantes
- comparação real x business case
- validação financeira de savings e benefícios
- relatório de prazo, custo, escopo e qualidade
- registro de lições aprendidas e causas de variação

---

## Leitura Rápida por Risco

| Risco Central | Subprocessos Críticos | WCGW-chave |
|---|---|---|
| Projeto sem racional econômico robusto | Business case | CAPEX-001, CAPEX-002, CAPEX-004 |
| Aprovação por alçada insuficiente ou fracionada | Governança | CAPEX-007, CAPEX-008, CAPEX-012 |
| Custo comprometido fora do forecast | Orçamento | CAPEX-014, CAPEX-015, CAPEX-018 |
| Contrato de obra frágil | Contratação | CAPEX-020, CAPEX-021, CAPEX-024 |
| Medição ou change order indevido | Medições | CAPEX-025, CAPEX-026, CAPEX-027 |
| Despesa capitalizada indevidamente | Capitalização | CAPEX-031, CAPEX-035, CAPEX-036 |
| CIP mantido após pronto para uso | Handover | CAPEX-038, CAPEX-042 |
| Benefício prometido não realizado | Pós-implementação | CAPEX-043, CAPEX-044, CAPEX-045 |
